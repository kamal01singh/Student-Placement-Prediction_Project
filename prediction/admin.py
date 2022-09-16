from django.contrib import admin
from .models import RegisterModel
from .models import PredictionModel

admin.site.register(RegisterModel)
admin.site.register(PredictionModel)
