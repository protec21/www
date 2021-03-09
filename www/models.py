from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    file = models.FileField(null=True, blank=True, upload_to="")
