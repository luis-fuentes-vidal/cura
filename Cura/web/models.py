from django.db import models


class Crm(models.Model):
    d_codigo=models.CharField(max_length=250, blank=True)
    d_asenta=models.CharField(max_length=250, blank=True)
    d_tipo_asenta=models.CharField(max_length=250, blank=True)
    D_mnpio=models.CharField(max_length=250, blank=True)
    d_estado=models.CharField(max_length=250, blank=True)
    d_ciudad=models.CharField(max_length=250, blank=True)
    d_CP=models.CharField(max_length=250, blank=True)
    c_estado=models.CharField(max_length=250, blank=True)
    c_oficina=models.CharField(max_length=250, blank=True)
    c_CP=models.CharField(max_length=250, blank=True)
    c_tipo_asenta=models.CharField(max_length=250, blank=True)
    c_mnpio=models.CharField(max_length=250, blank=True)
    id_asenta_cpcons=models.CharField(max_length=250, blank=True)
    d_zona=models.CharField(max_length=250, blank=True) 
    c_cve_ciudad=models.CharField(max_length=250, blank=True)
    @property
    def Crm_id(self):
        return unicode(self.id)
    def __str__(self):
        return "%s" % (self.d_codigo)
    class Meta:
        db_table = 'crm'