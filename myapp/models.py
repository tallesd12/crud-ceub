from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 30)
    cpf = models.IntegerField()
    data = models.DateField()


    def __str__(self):
        return self.nome