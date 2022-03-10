from django.urls import include, path
from .views import *
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
app_name = 'web'
urlpatterns = [
	path('', Datos.as_view()),
    path('datos/', Datos.as_view(), name='datos'),
    path('subirCSV2/', SubirCSV2.as_view(), name="subirCSV2"),
    path('paginar/', Paginar.as_view(), name="paginar"),
]