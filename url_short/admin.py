from django.contrib import admin
from .models import FellaURL
from analytics.models import ClickEvent

class ClickEvent(admin.StackedInline):
    model = ClickEvent
    extra = 0


@admin.register(FellaURL)
class FellaURLAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortcode', 'timestamp', 'updated', 'active']
    inlines = [ClickEvent]
