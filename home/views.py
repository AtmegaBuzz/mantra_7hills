from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages
from django.views import View

from .models import Notice, Event,EventForm
from .forms import EventRegistrationForm


# Create your views here.

def getLatest(request,dataArray,message,tags):
    if(len(dataArray)!=0):
        return dataArray.order_by('-updated_at')[0:6]
        
    messages.info(request,message,extra_tags=tags)
    return []

def index(request):

    notice_desc = getLatest(request,Notice.objects.all(),"no notices available","notice") # gets latest 5 notice
    events_desc = getLatest(request,Event.objects.all(),"no events available","events") #gets latest 5 events
    
    context = {
        'notice_desc':notice_desc,
        'events_desc':events_desc,
        'notice_len': len(notice_desc),
        'events_len': len(events_desc),
    }

    return render(request,'index.html',context)


def notices(request):
    
    notices = Notice.objects.all().order_by('-updated_at')

    if(len(notices)==0):
        
        messages.info(request,"no notices for now.")
        return render(request,'notices.html')
    

    context = {
        'notices':notices,
    }

    return render(request,'notices.html',context)


#  making class based view for events get and post

def Events_view(request):
    events = Event.objects.all().order_by('-updated_at')
    context = {
            'events':events,
            'form':EventRegistrationForm,
           }
    if(len(events)==0):
            messages.info(request,"no events for now.")
            return render(request,'events.html')      

    return render(request,'events.html',context)


class DetailEvents_view(View):
    model = EventForm
    

    def get(self,request,pk):

        event = get_object_or_404(Event,pk=pk)
        context = {
            'event':event,
            'form':EventRegistrationForm,
           }


        return render(request,'detailEvent.html',context)

    def post(self,request,pk):

        event = get_object_or_404(Event,pk=pk)
        context = {
            'event':event,
            'form':EventRegistrationForm,
           }
    
        form = EventRegistrationForm(request.POST)
        
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.event_name = event.event_name
            form.save()
            messages.success(request,"form submitted",extra_tags="success")
            

        return render(request,'detailEvent.html',context)
    