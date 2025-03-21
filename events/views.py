from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import CategoryModelForm, EventModelForm, ParticipantModelForm
from events.models import Event, Participant, Category
from django.db.models import Count, Q
from datetime import date
from django.contrib import messages


# Create your views here.


def all_events(request):
    search = request.GET.get('q', '')

    events = Event.objects.select_related(
        'category').annotate(num_par=Count('participant')).order_by("name")

    if search:
        events = events.filter(name__icontains=search)

    context = {'events': events, 'num_events': events.count()}
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
    events = base_query.filter(date=date.today())
    heading = "today's"

    if type == 'total_events':
        events = base_query.all().order_by("name")
        heading = "total"
    elif type == 'upcoming_events':
        events = base_query.filter(date__gt=date.today()).order_by("name")
        heading = "upcoming"
    elif type == 'past_events':
        events = base_query.filter(date__lt=date.today()).order_by("name")
        heading = "past"

    context = {
        "number_of_participants": participants,
        "counts": counts,
        "events": events,
        "heading": heading
    }
    return render(request, 'dashboard.html', context)


def categories(request):
    form = CategoryModelForm()
    cats = Category.objects.all().order_by('name')

    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Category added successfully")
            return redirect('categories')

    context = {
        'form': form, 'cats': cats,
        'number_of_categories': cats.count(),
        "heading": "create new category"
    }
    return render(request, 'categories.html', context)


def update_categories(request, id):
    category = Category.objects.get(id=id)
    form = CategoryModelForm(instance=category)
    cats = Category.objects.all().order_by('name')
    num_of_cats = Category.objects.count()
    context = {'form': form, 'cats': cats,
               'number_of_categories': num_of_cats, "heading": "update category"}

    if request.method == 'POST':
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

            messages.success(request, 'Category updated successfully')
            return redirect('update-categories', id=id)

    return render(request, 'categories.html', context)


def delete_category(request, id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        try:
            category.delete()
        except:
            messages.error(request, "Can not be deleted")
            return redirect("categories")

        messages.success(request, "Category deleted successfully")
        return redirect("categories")

    else:
        messages.error(request, "Something went wrong!")
        return redirect("categories")


def participants(request):
    form = ParticipantModelForm()
    participants = Participant.objects.all().order_by("name")

    if request.method == 'POST':
        form = ParticipantModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Participant added successfully")
            return redirect("participants")

    context = {'form': form, "participants": participants,
               'number_of_participants': participants.count(), "heading": "create new participant"}

    return render(request, 'participants.html', context)


def update_participants(request, id):
    participant = Participant.objects.get(id=id)
    form = ParticipantModelForm(instance=participant)
    participants = Participant.objects.all().order_by("name")

    if request.method == 'POST':
        form = ParticipantModelForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()

        messages.success(request, "Participant updated successfully")
        return redirect('update-participants', id=id)

    context = {'form': form, "participants": participants,
               'number_of_participants': participants.count(), "heading": "update participant"}
    return render(request, 'participants.html', context)


def delete_participant(request, id):
    if request.method == 'POST':
        participant = Participant.objects.get(id=id)
        participant.delete()

        messages.success(request, "Participant deleted successfully")
        return redirect("participants")

    else:
        messages.error(request, "Something went wrong!")
        return redirect("participants")


def new_event(request):
    form = EventModelForm()

    if request.method == 'POST':
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Event created successfully')
            return redirect('new-event')

    context = {'form': form, "heading": "create new event"}
    return render(request, 'new_event.html', context)


def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()

        messages.success(request, "Event deleted successfully")
        return redirect("events")

    else:
        messages.error(request, "Something went wrong!")
        return redirect("events")


def update_event(request, id):
    event = Event.objects.get(id=id)
    form = EventModelForm(instance=event)

    if request.method == 'POST':
        form = EventModelForm(request.POST, instance=event)
        if form.is_valid():
            form.save()

            messages.success(request, 'Event updated successfully')
            return redirect('update-event', id=id)

    context = {'form': form, "heading": "update event"}
    return render(request, 'new_event.html', context)


def details_event(request, id):
    event = Event.objects.select_related(
        "category").prefetch_related("participant_set").get(id=id)
    num_par = event.participant_set.count()
    participants = event.participant_set.all().order_by('name')
    return render(request, 'details_event.html', {"event": event, "num_par": num_par, "participants": participants})
