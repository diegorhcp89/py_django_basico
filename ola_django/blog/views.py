from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('blog')

    context = {'text': 'Olá blog'}

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('exemplo')

    context = {'text': 'Olá exemplo', "title": 'Essa é uma página de Exemplo - '}

    return render(request, 'blog/exemplo.html', context)
