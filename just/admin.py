from django.contrib import admin
from . import models

myModels = [models.Details, models.Price]  # iterable list
admin.site.register(myModels)
