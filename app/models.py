from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=50, blank=True)
    file_one = models.FileField(upload_to='', blank=True)
    file_two = models.FileField(upload_to='', blank=True)


    def __str__(self):
        return self.title
