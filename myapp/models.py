from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 30)
    cpf = models.CharField(max_length = 30)
    data = models.DateField()
    especialidade= models.CharField(max_length = 30)


    def __str__(self):
        return self.cpf