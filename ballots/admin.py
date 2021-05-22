from django.contrib import admin
from .models import Ballot

class BallotAdmin(admin.ModelAdmin):
    exclude = []

admin.site.register(Ballot, BallotAdmin)