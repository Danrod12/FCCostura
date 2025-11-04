from django.db import models

class Disfraz(models.Model):
    CATEGORIAS = [
        ('cosplay', 'Cosplay y personajes famosos'),
        ('uniforme', 'Uniformes profesionales'),
        ('creativo', 'Disfraces personalizados y creativos'),
        ('decoracion', 'Decoración y exhibición'),
    ]

    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='catalogo/')

    def __str__(self):
        return self.titulo

class CatalogoItem(models.Model):
    CATEGORIAS = [
        ('cosplay', 'Cosplays y personajes famosos'),
        ('uniformes', 'Uniformes profesionales'),
        ('personalizados', 'Disfraces personalizados'),
        ('otros', 'Otros'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='catalogo/')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='otros')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

