from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

""" rooms = [
    {'id': 1, 'name': 'Lets learn .net!'},
    {'id': 2, 'name': 'Lets learn aws!'},
    {'id': 3, 'name': 'Lets learn linux!'}
] """

def home(request):
    query_param = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=query_param)
                                | Q(name__icontains=query_param)
                                | Q(description__icontains=query_param))
    topics = Topic.objects.all()
    room_count = rooms.count()
    
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = next(item for item in rooms if item["id"] == int(pk))
    context = {'room': room}
    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request, 'base/room_form.html',context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':room})