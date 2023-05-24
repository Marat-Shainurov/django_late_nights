from django.shortcuts import render

from main.models import MainChannels


def index(request):
    data = list(MainChannels.objects.all().values())
    context = {'channels': data}
    return render(request, 'main/index.html', context)
