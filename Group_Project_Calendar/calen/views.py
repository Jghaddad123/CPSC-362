from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm

# Create your views here.
def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calen/calendar.html'

    def get_context_data(self, **kwargs):
        t = datetime.today()
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        calen = Calendar(d.year, d.month)
        calen.setfirstweekday(6)
        html_calen = calen.formatmonth(withyear=True)
        #html_calen = calen.setfirstweekday(6)
        html_calen = html_calen.replace('>%i<'%t.day, '<b><u><mark id="CalenMark" style="background-color:#ff85b4">%i</mark></u></b><'%t.day)
        context['calendar'] = mark_safe(html_calen)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
        
    else:
        instance = Event()
    '''
    if instance.end_time <= datetime.now():
        instance.delete()
'''
    if "cancel_event" in request.POST:
        return HttpResponseRedirect(reverse('calen:calendarhome'))
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        if "delete_event" in request.POST:
            #event_id = int(request.POST.get('event_id'))
            #event_item = Event.objects.get(id=event_id)
            #event_item.delete()
            #form.delete()
            #instance.deleted = True
            instance.delete()
            return HttpResponseRedirect(reverse('calen:calendarhome'))
        else:
            form.save()
            return HttpResponseRedirect(reverse('calen:calendarhome'))   
    return render(request, 'calen/event.html', {'form':form})

#def check_date_expired(event):

'''
def delete(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        events = Event.ogbjects.all()
        event_id = int(request.POST.get('event_id'))
        event_item = Event.objects.get(id=event_id)
        event_item.delete()
        return render(request, 'calen/event.html', {'form':form, 'event':events})
'''
