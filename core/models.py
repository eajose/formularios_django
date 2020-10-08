from django.db import models


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=14)
    salario = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=45)
    endereco_completo = models.TextField()

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'

    def __str__(self):
        return self.pessoa.nome
