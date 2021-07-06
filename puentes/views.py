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
from puentes.models import IEstJunta,IEstEstribo,IEstApoyoInterno,IOpeTransito,IEstElementoSuperestructura,  IVistaGenPteInfo, IValValoracionEconomica, IDocDocumentacion, IEstElementoServicio, IExgEntorno, IGenPteIdentifLocalizac, IGenInformacionGeneral
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
                ids = list(sum(  IVistaGenPteInfo.objects.values_list('i_idcons'), ()))
            if(len(tablas.keys()) > 0):
                if ("v_gen_pte_info" in tablas.keys()):
                    columnas = tablas['v_gen_pte_info']
                    respuesta =   IVistaGenPteInfo.objects.values(*tuple(columnas)).filter(i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
                if("i_est_estribo" in tablas.keys()):
                    columnas = tablas['i_est_estribo']
                    respuesta = IEstEstribo.objects.prefetch_related("i_idcons").values(*tuple(columnas)).filter(i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
                if ("i_est_junta" in tablas.keys()):
                    columnas = tablas['i_est_junta']
                    respuesta = IEstJunta.objects.prefetch_related("i_idcons").values(*tuple(columnas)).filter(
                        i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
                if ("i_est_elemeto_superestructura" in tablas.keys()):
                    columnas = tablas['i_est_elemeto_superestructura']
                    respuesta = IEstElementoSuperestructura.objects.prefetch_related("i_idcons").values(*tuple(columnas)).filter(
                        i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
                if ("i_ope_transito" in tablas.keys()):
                    columnas = tablas['i_ope_transito']
                    respuesta = IOpeTransito.objects.prefetch_related("i_idcons").values(*tuple(columnas)).filter(
                        i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
                if ("i_est_apoyo_interno" in tablas.keys()):
                    columnas = tablas['i_est_apoyo_interno']
                    respuesta = IEstApoyoInterno.objects.prefetch_related("i_idcons").values(*tuple(columnas)).filter(
                        i_idcons__in=ids)
                    serialized_obj = json.dumps(list(respuesta))
                    return JsonResponse(serialized_obj, content_type='application/json', safe=False)
            else:
                return JsonResponse("Error, No fue inclída en la consulta.", content_type='application/json', safe=False)

        else:
            respuesta =   IVistaGenPteInfo.objects.all().values()
            serialized_obj = json.dumps(list(respuesta))
            return JsonResponse(serialized_obj, content_type='application/json', safe=False)

    @csrf_exempt
    def salvarinfopuente( request ):
        if(request.method == "POST"):
            tablas = json.loads(request.body)
            # Valoración economica
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
            ### General puente identificación
            if ('i_gen_pte_identif_localiz' in tablas.keys()):
                atributos = tablas["i_gen_pte_identif_localiz"]
                gen_pte = IGenPteIdentifLocalizac(**atributos)
                try:
                    IGenPteIdentifLocalizac.objects.get(i_idcons=gen_pte.i_idcons)
                    IGenPteIdentifLocalizac.objects.filter(i_idcons=gen_pte.i_idcons).update(**atributos)
                except IGenPteIdentifLocalizac.DoesNotExist:
                    gen_pte.save()
                tablas.pop("i_gen_pte_identif_localiz")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            ### Documentación
            if ('i_doc_documentacion' in tablas.keys()):
                atributos = tablas["i_doc_documentacion"]
                doc = IDocDocumentacion(**atributos)
                try:
                    IDocDocumentacion.objects.get(i_idcons=doc.i_idcons)
                    IDocDocumentacion.objects.filter(i_idcons=doc.i_idcons).update(**atributos)
                except IDocDocumentacion.DoesNotExist:
                    doc.save()
                tablas.pop("i_doc_documentacion")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            #Apoyo interno
            if ('i_est_apoyo_interno' in tablas.keys()):
                atributos = tablas["i_est_apoyo_interno"]
                est_apoyo = IEstApoyoInterno(**atributos)
                try:
                    IEstApoyoInterno.objects.get(i_idcons=est_apoyo.i_idcons)
                    IEstApoyoInterno.objects.filter(i_idcons=est_apoyo.i_idcons).update(**atributos)
                except IEstApoyoInterno.DoesNotExist:
                    est_apoyo.save()
                tablas.pop("i_est_apoyo_interno")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            ## Elemento servicio
            if ('i_est_elemento_servicio' in tablas.keys()):
                atributos = tablas["i_est_elemento_servicio"]
                est_elemento_servicio = IEstElementoServicio(**atributos)
                try:
                    IEstElementoServicio.objects.get(i_idcons=est_elemento_servicio.i_idcons)
                    IEstElementoServicio.objects.filter(i_idcons=est_elemento_servicio.i_idcons).update(**atributos)
                except IEstElementoServicio.DoesNotExist:
                    est_elemento_servicio.save()
                tablas.pop("i_est_elemento_servicio")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            ### Elemento super estructura
            if ('i_est_elemento_superestructura' in tablas.keys()):
                atributos = tablas["i_est_elemento_superestructura"]
                est_elemento_superestructura = IEstElementoSuperestructura(**atributos)
                try:
                    IEstElementoSuperestructura.objects.get(i_idcons=est_elemento_superestructura.i_idcons)
                    IEstElementoSuperestructura.objects.filter(i_idcons=est_elemento_superestructura.i_idcons).update(**atributos)
                except IEstElementoSuperestructura.DoesNotExist:
                    est_elemento_superestructura.save()
                tablas.pop("i_est_elemento_superestructura")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            ### Estribo
            if ('i_est_estribo' in tablas.keys()):
                atributos = tablas["i_est_estribo"]
                est_estribo = IEstEstribo(**atributos)
                try:
                    IEstEstribo.objects.get(i_idcons=est_estribo.i_idcons)
                    IEstEstribo.objects.filter(i_idcons=est_estribo.i_idcons).update(**atributos)
                except IEstEstribo.DoesNotExist:
                    est_estribo.save()
                tablas.pop("i_est_estribo")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            #### Junta
            if ('i_est_junta' in tablas.keys()):
                atributos = tablas["i_est_junta"]
                est_junta = IEstJunta(**atributos)
                try:
                    IEstJunta.objects.get(i_idcons=est_junta.i_consecid)
                    IEstJunta.objects.filter(i_idcons=est_junta.i_consecid).update(**atributos)
                except IEstJunta.DoesNotExist:
                    est_junta.save()
                tablas.pop("i_est_junta")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            #### Entorno
            if ('i_exg_entorno' in tablas.keys()):
                atributos = tablas["i_exg_entorno"]
                exg_entorno = IExgEntorno(**atributos)
                try:
                    IExgEntorno.objects.get(i_idcons=exg_entorno.i_idcons)
                    IExgEntorno.objects.filter(i_idcons=exg_entorno.i_idcons).update(**atributos)
                except IExgEntorno.DoesNotExist:
                    exg_entorno.save()
                tablas.pop("i_exg_entorno")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)
            #### Transito
            if ('i_ope_transito' in tablas.keys()):
                atributos = tablas["i_ope_transito"]
                ope_transito = IOpeTransito(**atributos)
                try:
                    IOpeTransito.objects.get(i_idcons=ope_transito.i_idcons)
                    IOpeTransito.objects.filter(i_idcons=ope_transito.i_idcons).update(**atributos)
                except IOpeTransito.DoesNotExist:
                    ope_transito.save()
                tablas.pop("i_ope_transito")
                if(len(tablas.keys()) == 0):
                    return JsonResponse("Informacion de valoracion salvada correctamente.", content_type='application/json', safe=False)






    @csrf_exempt
    def test( request ):
        body = "{\"v_gen_pte_info\":[\"i_idcons\",  \"s_territ\", \"s_idsipucol\", \"s_adminvial\",\"s_idpuente\",\"d_valrepos\"] ,\"filter\": [148]}"
        puentes = requests.post('http://127.0.0.1:8000/puentes/consultar', data=body)
        puentesJSON = puentes.json()
        puentes = json.loads(puentes.json())
        return JsonResponse(puentesJSON, content_type='application/json', safe=False)