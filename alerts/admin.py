from django.contrib import admin
from .models import Alert, AlertVote


class VoteInline(admin.StackedInline):
    model = AlertVote
    extra = 1


class AlertAdmin(admin.ModelAdmin):
    fieldsets = [
        ('WhistleBlower details',       {'fields':['alert_whistleblower', 'alert_timestamp']}),
        ('Station Details',             {'fields':['alert_station', 'alert_line']}),
        ('Alert votes',                 {'fields':['alert_votes'], 'classes':['collapse']})
    ]
    inlines = [VoteInline]

admin.site.register(Alert, AlertAdmin)