from django.shortcuts import render, redirect
from .models import *
from .models import Crm
from .forms import *
from django.views import View
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
import csv
from django.db.models import Q
class Datos(View):
    def get(self,request):
        crm = Crm.objects.all()[:20]
        return render(request, 'main/datos.html', {'crm':crm})
    def post(self,request):
        busqueda = request.POST.get("buscar")
        crm = Crm.objects.all()[:20]
        if busqueda:
            crm = Crm.objects.filter(
            Q(D_mnpio = busqueda) | 
            Q(d_estado = busqueda) |
            Q(d_ciudad = busqueda) |
            Q(d_CP = busqueda)
        ).distinct()
        return render(request, 'main/datos.html', {'crm':crm})


class Paginar(View):
    def get(self , request):
        pagina = int(request.GET['pagina'])
        registros = 1000
        nump = int(Crm.objects.all().count() / registros) + 1
        limiteinf = (registros * (pagina - 1))
        limitesup = (registros * pagina)
        crm = Crm.objects.all()[limiteinf : limitesup]
        return render(request, 'main/datos.html' , {'crm' : crm , 'paginas' : nump, 'pag' : pagina})
    def post(self,request):
        return render(request, 'main/datos.html')

 
class SubirCSV2(View):
    def post(self, request):
        formCSV = CSVForm(request.POST, request.FILES)
        if formCSV.is_valid():
            archivo = request.FILES['archivo']
            decoded_file = archivo.read().decode('latin-1').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                CRM.objects.create(
                    d_codigo =row['d_codigo'],
                    d_asenta =row['d_asenta'],
                    d_tipo_asenta =row['d_tipo_asenta'],
                    D_mnpio = row['D_mnpio'],
                    d_estado = row['d_estado'],
                    d_ciudad =row['d_ciudad'],
                    d_CP =row['d_CP'],
                    c_estado =row['c_estado'],
                    c_oficina =row['c_oficina'],
                    c_CP = row['c_CP'],
                    c_tipo_asenta = row['c_tipo_asenta'],
                    c_mnpio =row['c_mnpio'],
                    id_asenta_cpcons = row['id_asenta_cpcons'],
                    d_zona = row['d_zona'],
                    c_cve_ciudad =row['c_cve_ciudad']
                )
            return redirect('web:datos')
        else:
            return redirect('web:datos')
