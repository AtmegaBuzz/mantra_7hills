from django.db import models

# Create your models here.

class Notice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Event(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    event_name = models.CharField(max_length=40)
    joinEvent = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name


class EventForm(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)

    FLAT = [
        ("C","C"),
    ]
    BLOCK = [
        ("C1","C1"),
        ("C2","C2"),
    ]

    flat = models.CharField(max_length=1,choices=FLAT,default="C")
    block = models.CharField(max_length=2,choices=BLOCK,default="C1")

    flat_no = models.IntegerField(blank=False)

    event_name = models.CharField(max_length=40,blank=True,null=True)
    