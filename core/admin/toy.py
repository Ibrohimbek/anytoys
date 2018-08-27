from django.contrib import admin

from core.models import Toy


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'type',
        'owner_name',
        'owner_phone_number',
        'changed_at',
    )
