from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display= ("first_name", "last_name", "guest_count", "reservation_time", "comments")
    search_fields= ("first_name__startswith",)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")