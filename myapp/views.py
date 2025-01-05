from django.shortcuts import render


# Create your views here.


def html_response(request):
    return render(request, 'myapp/template.html')


from django.http import HttpResponse


def text_response(request):
    return HttpResponse("Это текстовый ответ")
