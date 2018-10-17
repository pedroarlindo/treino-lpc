from django.db import models

# ----------------------------------------- Pessoa
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=128)
    email = models.EmailField('E-mail', max_length=128)

    def __str__(self):
        return self.nome


# ----------------------------------------- Categoria
class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=128)
    slug = models.SlugField('Slug')

    def __str__(self):
        return self.nome


# ----------------------------------------- Noticia
class Noticia(models.Model):
    titulo = models.CharField('Título', max_length=128)
    conteudo = models.TextField('Conteúdo', max_length=512)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo