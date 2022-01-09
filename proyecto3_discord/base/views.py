from django.shortcuts import render
from .models import Room

""" rooms = [
    {'id': 1, 'name': 'Lets learn .net!'},
    {'id': 2, 'name': 'Lets learn aws!'},
    {'id': 3, 'name': 'Lets learn linux!'}
] """

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = next(item for item in rooms if item["id"] == int(pk))
    context = {'room': room}
    return render(request, 'base/room.html', context)