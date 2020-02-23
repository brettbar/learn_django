from django.db import models

# Create your models here.

class Person(models.Model):
  name = models.CharField(max_length=60)
  sub_text = models.CharField(max_length=60)
  era = models.CharField(max_length=60)
  bio = models.TextField()

  def __str__(self):
    return self.name