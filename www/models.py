from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()

class NoticeAttach(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True, blank=True, upload_to="")
