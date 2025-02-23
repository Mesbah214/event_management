from django.shortcuts import render
from django.http import HttpResponse
from events.forms import EventForm
from events.participant_form import ParticipantModelForm
from events.models import Event, Participant
from django.db.models import Count

# Create your views here.


def all_events(request):
    events = Event.objects.select_related('category').annotate(num_par=Count('participant'))
    num_events = Event.objects.count()
    context = {'events': events, 'num_events': num_events}
    return render(request, 'events.html', context)


def dashboard(request):
    return render(request, 'home.html')


def categories(request):
    return render(request, 'categories.html')


def participants(request):
    form = ParticipantModelForm()
    participants = Participant.objects.all()

    if request.method == 'POST':
        form = ParticipantModelForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'participants.html', {"form": form, "message": "Task added succesfully", "participants": participants})

    context = {'form': form, "participants": participants}
    return render(request, 'participants.html', context)


def new_event(request):
    form = EventForm()
    context = {'form': form}
    return render(request, 'new_event.html', context)


def details_event(request):
    return render(request, 'details_event.html')
