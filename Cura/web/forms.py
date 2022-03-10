from django import forms
from .models import *

class CrmForm(forms.ModelForm):
    class Meta:
       model = Crm
       fields = ('d_codigo', 'd_asenta','d_tipo_asenta', 'D_mnpio', 'd_estado', 'd_ciudad', 'd_CP',
        		'c_estado', 'c_oficina', 'c_CP', 'c_tipo_asenta', 'c_mnpio', 'id_asenta_cpcons', 'd_zona', 'c_cve_ciudad',)
       widgets = {
             'd_codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_codigo', 'id':'d_codigo_cr'}),
             'd_asenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_asenta', 'id':'d_asenta_cr'}),
             'd_tipo_asenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_tipo_asenta', 'id':'d_tipo_asenta_cr'}),
             'D_mnpio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'D_mnpio', 'id':'D_mnpio_cr'}),
             'd_estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_estado', 'id':'d_estado_cr'}),
             'd_ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_ciudad', 'id':'d_ciudad_cr'}),
             'd_CP': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_CP', 'id':'d_CP_cr'}),
             'c_estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_estado', 'id':'c_estado_cr'}),
             'c_oficina': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_oficina', 'id':'c_oficina_cr'}),
             'c_CP': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_CP', 'id':'c_CP_cr'}),
             'c_tipo_asenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_tipo_asenta', 'id':'c_tipo_asenta_cr'}),
             'c_mnpio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_mnpio', 'id':'c_mnpio_cr'}),
             'id_asenta_cpcons': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'id_asenta_cpcons', 'id':'id_asenta_cpcons_cr'}),
             'd_zona': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_zona', 'id':'d_zona_cr'}),
             'c_cve_ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_cve_ciudad', 'id':'c_cve_ciudad_cr'}),
        }
class CrmFormModal(forms.ModelForm):
    class Meta:
       model = Crm
       fields = ('d_codigo', 'd_asenta','d_tipo_asenta', 'D_mnpio', 'd_estado', 'd_ciudad', 'd_CP',
        		'c_estado', 'c_oficina', 'c_CP', 'c_tipo_asenta', 'c_mnpio', 'id_asenta_cpcons', 'd_zona', 'c_cve_ciudad',)
       widgets = {
             'd_codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_codigo', 'id':'d_codigo_cr1'}),
             'd_asenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_asenta', 'id':'d_asenta_cr1'}),
             'd_tipo_asenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_tipo_asenta', 'id':'d_tipo_asenta_cr1'}),
             'D_mnpio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'D_mnpio', 'id':'D_mnpio_cr1'}),
             'd_estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_estado', 'id':'d_estado_cr1'}),
             'd_ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_ciudad', 'id':'d_ciudad_cr1'}),
             'd_CP': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_CP', 'id':'d_CP_cr1'}),
             'c_estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_estado', 'id':'c_estado_cr1'}),
             'c_oficina': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_oficina', 'id':'c_oficina_cr1'}),
             'c_CP': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_CP', 'id':'c_CP_cr1'}),
             'c_tipo_asenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_tipo_asenta', 'id':'c_tipo_asenta_cr1'}),
             'c_mnpio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_mnpio', 'id':'c_mnpio_cr1'}),
             'id_asenta_cpcons': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'id_asenta_cpcons', 'id':'id_asenta_cpcons_cr1'}),
             'd_zona': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'d_zona', 'id':'d_zona_cr1'}),
             'c_cve_ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'c_cve_ciudad', 'id':'c_cve_ciudad_cr1'}),
        }
        
class CSVForm(forms.Form):
    archivo = forms.FileField(widget = forms.FileInput(attrs = {'class' : 'form-control'}))