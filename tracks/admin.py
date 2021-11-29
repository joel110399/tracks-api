from django.contrib import admin
from .models import Artist, Track, Genre

models = (Artist, Track, Genre)

for model in models:
    admin.site.register(model)