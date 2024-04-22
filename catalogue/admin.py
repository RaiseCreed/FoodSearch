from django.contrib import admin
from django.contrib.admin import register
from .models import Profile,Tag,Recipe, Review

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Review)
