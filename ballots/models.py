from django.db import models
from django.urls import reverse


class Ballot(models.Model):
    votes = models.IntegerField()

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})

    def __str__(self):
        return str(self.votes)
