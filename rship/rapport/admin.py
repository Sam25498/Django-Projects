from django.contrib import admin
from .models import Description
# Register your models here.

#admin.site.register(Description)
@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_text', 'reminder_date', 'event_date')
