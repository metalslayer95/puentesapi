"""puentesAPI URL Configuration

The `urlpatterns` list routes URLs to puentesbkp. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function puentesbkp
    1. Add an import:  from my_app import puentesbkp
    2. Add a URL to urlpatterns:  path('', puentesbkp.home, name='home')
Class-based puentesbkp
    1. Add an import:  from other_app.puentesbkp import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from puentes import views as puentes

urlpatterns = [
    path('puentes/consultar', puentes.Puentes.obtenerpuentes),
    path('puentes/salvarinfo', puentes.Puentes.salvarinfopuente),
    path('puentes/test', puentes.Puentes.test),
]
