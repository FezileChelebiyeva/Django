from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Esas sehife</h1>")

def about(request):
    return HttpResponse("<h1>Sehife haqqinda</h1>")

def contact(request):
    return HttpResponse("<h1>Elaqe</h1>")

def archive(request,year):
    return HttpResponse(f'<h1>il ilə bağlı arxiv</h1><p>{year}</p>')

def users(request,username):
    return HttpResponse(f'<h1>Username -- {username}')

def user(request, name = 'undefined', age = 0):
    return HttpResponse(f"<h2> Name: {name} <br/> Age: {age}</h2>")


# kwargs
def index(request):
    return HttpResponse("<h1>Women tətbiqinin səhifəsi</h1>")
  
def categories(request, name, age):
    return HttpResponse(f"""
            <h2>Kateqoriyalar üzrə məqaləlr</h2>
            <p>Name: {name}</p>
            <p>Age: {age}</p>
    """)

# error sehifesi
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Səhifə tapılmadı</h1>')
