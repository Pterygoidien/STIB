import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from transports.models import Station, Line
from django.urls import reverse


class Alert(models.Model):
    alert_whistleblower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alert_timestamp = models.DateTimeField(default=timezone.now)
    alert_time = models.TimeField(default=timezone.now)
    alert_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    alert_line = models.ForeignKey(Line, on_delete=models.CASCADE)
    alert_votes = models.IntegerField(default=0)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.alert_timestamp <= now

    def __str__(self):
        return f'({self.id}) - {self.alert_station}'

    def get_absolute_url(self):
        return reverse('alerts:detail', kwargs={'pk':self.pk})


class AlertVote(models.Model):
    vote_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alert_id = models.ForeignKey(Alert, on_delete=models.CASCADE)
    vote_type_list = [
        ('UP', 'upvote'),
        ('DO', 'downvote')
    ]
    vote_type = models.CharField(
        max_length=2,
        choices=vote_type_list,
        default='UP'
    )
    vote_timestamp = models.DateTimeField(auto_now=True)
    vote_remark = models.TextField(blank=True, null=True)



