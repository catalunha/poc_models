from django.contrib import admin
from .models import PersonModel


@admin.register(PersonModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
