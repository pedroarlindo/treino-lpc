from django.contrib import admin
from .models import Pessoa, Categoria, Noticia

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass