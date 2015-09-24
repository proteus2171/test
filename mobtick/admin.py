from django.contrib import admin

from .forms import TicketForm

from .models import ticket
# Register your models here.

class ticketadmin(admin.ModelAdmin):
    list_display = ["tickid","tech","timestamp"]
    form = TicketForm
    # class Meta:
    #     model = ticket

admin.site.register(ticket, ticketadmin,)