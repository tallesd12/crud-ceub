from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 30)
    cpf = models.IntegerField()
    data = models.DateField()
    especialidade= models.CharField(max_length = 30, null=True)


    def __str__(self):
        return self.nome