from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# creating a basic model with text and date fields
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        # returning string representation of model
        return self.text
class Entry(models.Model):
    # to add entry about topic
    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        return self.text[:50] + "..."

class DiaryEntry(models.Model):
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        return self.text[:50] + "..."