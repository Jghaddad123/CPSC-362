from django.urls import path
from calen import views

app_name = 'calen'
urlpatterns = [
    path('calendar/', views.CalendarView.as_view(template_name="calen/calendar.html"), name='calendarhome'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
    path('event/delete/<int:event_id>/', views.event, name='delete_event'),
]