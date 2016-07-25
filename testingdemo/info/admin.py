from django.contrib import admin

# Register your models here.
from models import person
from models import quiz

admin.site.register(person)
admin.site.register(quiz)