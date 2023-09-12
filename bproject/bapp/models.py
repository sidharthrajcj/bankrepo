# models.py
from django.db import models
from django.urls import reverse


class District(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    wikipedia_link = models.URLField()

    def get_url(self):
        return reverse('bapp:district_dropdown',args=[self.slug])

    def __str__(self):
        return self.name
