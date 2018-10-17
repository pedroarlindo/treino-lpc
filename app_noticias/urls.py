from django.urls import path
from app_noticias.views import noticia_detalhes, noticias_autor, noticias_categoria, estatisticas_noticias

urlpatterns = [
    path('noticia/<int:id_noticia>/detalhes/', noticia_detalhes, name='noticia-detalhes'),
    path('autor/<int:id_pessoa>/noticias/', noticias_autor, name='noticias-autor'),
    path('categoria/<int:id_categoria>/autor/', noticias_categoria, name='noticias-categoria'),
    path('noticias/estatisticas', estatisticas_noticias, name='noticias-estatisticas')
]