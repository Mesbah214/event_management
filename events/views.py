from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import CategoryModelForm, EventModelForm, ParticipantModelForm
from events.models import Event, Participant, Category
from django.db.models import Count, Q
from datetime import date
from django.contrib import messages


# Create your views here.


def all_events(request):
    events = Event.objects.select_related(
        'category').annotate(num_par=Count('participant'))
    num_events = Event.objects.count()
    context = {'events': events, 'num_events': num_events}
    return render(request, 'events.html', context)


def dashboard(request):
    type = request.GET.get('type', 'all')
    participants = Participant.objects.all().count()
    base_query = Event.objects.annotate(
        num_par=Count('participant')).select_related('category')
    counts = Event.objects.aggregate(
        events=Count("id"),
        upcoming=Count("id", filter=Q(date__gt=date.today())),
        past=Count("id", filter=Q(date__lt=date.today()))
    )
    events = base_query.filter(date__month=date.today().month)
    heading = "today's"

    if type == 'total_events':
        events = base_query.all()
        heading = "total"
    elif type == 'upcoming_events':
        events = base_query.filter(date__gt=date.today())
        heading = "upcoming"
    elif type == 'past_events':
        events = base_query.filter(date__lt=date.today())
        heading = "past"

    context = {
        "number_of_participants": participants,
        "counts": counts,
        "events": events,
        "heading": heading
    }
    return render(request, 'home.html', context)


def categories(request):
    form = CategoryModelForm
    cats = Category.objects.all()
    num_of_cats = Category.objects.count()

    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, "categories.html", {
                "form": form,
                "message": "Category added successfully",
                "cats": cats,
                "number_of_categories": num_of_cats
            })
    context = {'form': form, 'cats': cats, 'number_of_categories': num_of_cats}
    return render(request, 'categories.html', context)


def participants(request):
    form = ParticipantModelForm()
    participants = Participant.objects.all()
    number_of_participants = Participant.objects.count()

    if request.method == 'POST':
        form = ParticipantModelForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'participants.html', {
                "form": form,
                "message": "Task added succesfully",
                "participants": participants,
                'number_of_participants': number_of_participants
            })

    context = {'form': form, "participants": participants,
               'number_of_participants': number_of_participants}
    return render(request, 'participants.html', context)


def new_event(request):
    form = EventModelForm()

    if request.method == 'POST':
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()

            # return render(request, 'new_event.html', {'form': form, "message": "Event added succesfully"})
            messages.success(request, 'Task created successfully')
            return redirect('new-event')
    context = {'form': form}
    return render(request, 'new_event.html', context)


def details_event(request):
    return render(request, 'details_event.html')
