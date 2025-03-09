from django.db import models
from django.conf import settings
from django.utils import timezone
from map.models import Location


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location, related_name='place', blank=True, null=True, on_delete=models.PROTECT)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title