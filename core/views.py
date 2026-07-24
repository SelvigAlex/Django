from django.shortcuts import render

def index(request):
    context = {
        'title': 'Добро пожаловать!',
        'message': 'Привет! Это мой первый Django-проект на Netlify.',
        'author': 'Ваше Имя',
        'year': 2026,
    }
    return render(request, 'core/index.html', context)