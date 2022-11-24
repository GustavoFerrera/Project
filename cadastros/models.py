from django.db import models

# Create your models here.
class Demissoe(models.Model):
    num_registro = models.CharField(max_length=50, verbose_name="Número registro")
    nome = models.CharField(max_length=50)
    sede_empresarial= models.CharField(max_length=50, verbose_name="Sede empresarial")
    setor= models.CharField(max_length=50)

    def __str__(self):
        return "{} ({})".format(self.num_registro, self.nome)

class Feria(models.Model):
    num_registro = models.CharField(max_length=12, verbose_name= "Número registro")
    nome = models.CharField(max_length=50)
    sede_empresarial = models.CharField(max_length=50, verbose_name="Sede empresarial")
    setor = models.CharField(max_length=50)

    def __str__(self):
        return "{} ({})".format(self.num_registro)

class Afastamento(models.Model):
    num_registro = models.CharField(max_length=12, verbose_name= "Número registro")
    nome = models.CharField(max_length=50)
    sede_empresarial = models.CharField(max_length=50, verbose_name="Sede empresarial")
    setor = models.CharField(max_length=50)

    def __str__(self):
        return "{} ({})".format(self.num_registro, self.nome)

class Licenca(models.Model):
    num_registro = models.CharField(max_length=12, verbose_name= "Número registro")
    nome = models.CharField(max_length=50)
    sede_empresarial = models.CharField(max_length=50, verbose_name="Sede empresarial")
    setor = models.CharField(max_length=50)

    def __str__(self):
        return "{} ({})".format(self.num_registro, self.nome)
