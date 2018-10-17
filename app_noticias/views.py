from django.http import Http404
from django.shortcuts import render
from .models import Noticia, Categoria, Pessoa

# --------------------------------------------------------- noticia_detalhes
def noticia_detalhes(request, id_noticia):
    try:
        noticia = Noticia.objects.get(pk=id_noticia)
        return render(request, 'app_noticias/noticia-detalhes.html', {'noticia': noticia})
    except Noticia.DoesNotExist:
        raise Http404('Desculpe! Sua notícia não foi encontrada.')


# --------------------------------------------------------- noticias_autor
def noticias_autor(request, id_pessoa):
    try:
        pessoa = Pessoa.objects.get(pk=id_pessoa)
        noticias = Noticia.objects.filter(autor=pessoa)
        return render(request, 'app_noticias/noticias-autor.html', {'noticias': noticias})
    except Pessoa.DoesNotExist:
        raise Http404('Desculpe! O Autor não foi encontrado.')


# --------------------------------------------------------- noticias_categoria
def noticias_categoria(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
        noticias = Noticia.objects.filter(categoria=categoria)

        porcentagem = noticias.count()/Noticia.objects.count()*100

        return render(request, 'app_noticias/noticias-categoria.html',{
            'categoria':categoria,
            'noticias':noticias,
            'porcentagem':porcentagem
        })
    except Categoria.DoesNotExist:
        raise Http404('Desculpe! A Categoria não foi encontrada.')


# --------------------------------------------------------- estatisticas_noticias
def estatisticas_noticias(request):
    qtd_autores = Pessoa.objects.count()

    nome_autor = None
    qtd_noticias_autor = 0
    for autor in Pessoa.objects.all():
        aux = Noticia.objects.filter(autor=autor).count()
        if aux > qtd_noticias_autor:
            nome_autor = autor.nome
            qtd_noticias_autor = aux

    qtd_total_noticias = Noticia.objects.count()
    categorias = Categoria.objects.all()
    for categoria in categorias:
        qtd_noticias_categoria = Noticia.objects.filter(categoria=categoria).count()
        porcentagem = qtd_noticias_categoria/qtd_total_noticias*100
        categoria.porcentagem = porcentagem

    return render(request, 'app_noticias/estatisticas.html', {
        'qtd_autores':qtd_autores,
        'nome_autor':nome_autor,
        'qtd_noticias_autor':qtd_noticias_autor,
        'categorias':categorias
    })