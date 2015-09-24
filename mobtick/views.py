from django.shortcuts import render
from .forms import TicketForm

# Create your views here.
def home(request):
    title = "Submit On Site Support Request"
    form = TicketForm(request.POST or None)
    context = {
        "template_title":title,
        "form":form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
        "template_title":"Your Ticket Has been Submitted"
        }


    
    return render(request, "home.html", context)