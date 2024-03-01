from django.db import models


class Post(models.Model):
    title = models.CharField('Título', max_length=255)
    content = models.TextField('Conteúdo')
    pub_date = models.DateTimeField(auto_now_add=True)
