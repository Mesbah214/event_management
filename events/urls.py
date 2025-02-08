from django.urls import path
from events.views import all_events, dashboard, categories, new_event, details_event, participants

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('events/', all_events, name='events'),
    path('new-event/', new_event, name='new-event'),
    path('details-event/', details_event, name='details-event'),
    path('participants/', participants, name='participants'),
    path('categories/', categories, name='categories'),
]
