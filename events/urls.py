from django.urls import path
from events.views import all_events, dashboard, categories, new_event, details_event, participants, update_event, update_categories, update_participants, delete_event

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('events/', all_events, name='events'),
    path('new-event/', new_event, name='new-event'),
    path('update-event/<int:id>/', update_event, name='update-event'),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
    path('details-event/<int:id>/', details_event, name='details-event'),
    path('participants/', participants, name='participants'),
    path('categories/', categories, name='categories'),
    path('update_categories/<int:id>/',
         update_categories, name='update-categories'),
    path('update_participants/<int:id>/',
         update_participants, name='update-participants'),
]
