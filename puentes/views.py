import simplejson as json
import ast
import urllib.request as urllib2
from urllib.request import urlretrieve, urlcleanup
from urllib.parse import urlsplit
from os.path import basename
from django.core.files import File
import zipfile
import os
import datetime
import shutil
import time
from django.core.mail import send_mail
import subprocess
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.generic import base
from django.core.files.storage import default_storage
from random import *
from django.conf import settings
from django.db.models import Count
from puentes.models import IEstJunta,IEstEstribo,IEstApoyoInterno,IOpeTransito,IEstElementoSuperestructura,VGenPteInfo, IValValoracionEconomica, IDocDocumentacion, IEstElementoServicio, IExgEntorno, IGenPteIdentifLocalizac, IGenInformacionGeneral
from django.views.decorators.csrf import csrf_exempt
import requests



class Puentes():
    @csrf_exempt
    def obtenerpuentes( request ):
        if(request.method == "POST"):
            tablas = json.loads(request.body)
            if('filter' in tablas.keys()):
                ids = tablas['filter']
            else:
                ids = list(sum(VGenPteInfo.objects.values_list('i_idcons'), ()))
            if('v_gen_pte_info' in tablas.keys()):
                if("i_est_estribo" in tablas.keys()):
                    print("hola mundo")
                    columnas = tablas['i_est_estribo']
                    respuesta = IEstEstribo.objects.prefetch_related("i_idcons").values().filter(i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
                else:
                    columnas = tablas['v_gen_pte_info']
                    respuesta = VGenPteInfo.objects.values(*tuple(columnas)).filter(i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)

            else:
                return JsonResponse("Error, v_gen_pte_info no incluido en la consulta.", content_type='application/json', safe=False)

        else:
            respuesta = VGenPteInfo.objects.all().values()
            serialized_obj = json.dumps(list(respuesta))
            return JsonResponse(serialized_obj, content_type='application/json', safe=False)

    @csrf_exempt
    def salvarinfopuente( request ):
        if(request.method == "POST"):
            tablas = json.loads(request.body)
            if('i_val_valoracion_economica' in tablas.keys()):
                atributos = tablas["i_val_valoracion_economica"]
                valoracion = IValValoracionEconomica(**atributos)
                try:
                    IValValoracionEconomica.objects.get(i_idcons=valoracion.i_idcons)
                    IValValoracionEconomica.objects.filter(i_idcons=valoracion.i_idcons).update(**atributos)
                except IValValoracionEconomica.DoesNotExist:
                    valoracion.save()
                tablas.pop("i_val_valoracion_economica")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            if ('i_gen_pte_identif_localiz' in tablas.keys()):
                atributos = tablas["i_gen_pte_identif_localiz"]
                gen_pte = IGenPteIdentifLocalizac(**atributos)
                try:
                    IGenPteIdentifLocalizac.objects.get(i_idcons=gen_pte.i_idcons)
                    IGenPteIdentifLocalizac.objects.filter(i_idcons=gen_pte.i_idcons).update(**atributos)
                except IValValoracionEconomica.DoesNotExist:
                    gen_pte.save()
                tablas.pop("i_gen_pte_identif_localiz")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)


    @csrf_exempt
    def test( request ):
        body = "{\"v_gen_pte_info\":[\"i_idcons\",  \"s_territ\", \"s_idsipucol\", \"s_adminvial\",\"s_idpuente\",\"d_valrepos\"], \"i_est_estribo\": [\"d_bsilla\"],\"filter\": [148]}"
        puentes = requests.post('http://127.0.0.1:8000/puentes/consultar', data=body)
        puentes = puentes.json()
        print(puentes)
        return JsonResponse(puentes, content_type='application/json', safe=False)