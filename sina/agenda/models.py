from django.db import models


class List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    list = models.ForeignKey(List)
    name = models.CharField(max_length=255)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return self.name