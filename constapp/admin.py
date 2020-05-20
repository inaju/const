from django.contrib import admin
from .models import Check, Date, Goals, JoinModel
# Register your models here.
admin.site.register(Check)
admin.site.register(Date)
admin.site.register(Goals)
admin.site.register(JoinModel)

