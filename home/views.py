from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'text' : 'home page'
    }

    return render(
        request,
        'home/index.html',
        context
    )