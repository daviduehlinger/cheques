"""
URL configuration for cheques project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cheques_app.views import cargar_cheque, confirmacion_cheque
from consultas_app.views import consultar_cheques
from cheques.views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('cargar_cheque/', cargar_cheque, name='cargar_cheque'),
    #path('cheque_cargado', cheque_cargado, name='cheque_cargado'),
    path('consultar_cheques/', consultar_cheques, name='consultar_cheques'),
    path('confirmacion/', confirmacion_cheque, name='confirmacion_cheque'),
]
