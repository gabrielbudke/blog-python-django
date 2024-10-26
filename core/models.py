from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100, unique=True, verbose_name='Titulo')
  content = models.TextField(verbose_name='Descrição')
  tags = models.ManyToManyField('Tag', verbose_name='Tags', related_name='posts')
  created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Criado em')
  
  def __str__(self):
    return self.title
  

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True, verbose_name='Nome')

  def __str__(self):
    return self.name