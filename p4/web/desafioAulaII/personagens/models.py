from django.db import models


class Personagem(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    habilidades = models.TextField()
    imagem = models.ImageField(upload_to='personagens/', null=False, blank=False)
    data_inclusao = models.DateTimeField(auto_now_add=True)
