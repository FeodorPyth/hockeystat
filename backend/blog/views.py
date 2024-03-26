from django.shortcuts import render


def index(request):
    template_name = 'blog/index.html'
    return render(request, template_name)

def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)

def contacts(request):
    template_name = 'pages/contacts.html'
    return render(request, template_name)
