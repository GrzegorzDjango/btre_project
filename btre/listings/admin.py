from django.contrib import admin
from .models import Listing


#dodajemy więcej pól do adminu
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('realtor',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

# rejesturujemy model żeby było go widać w adminie
admin.site.register(Listing, ListingAdmin)
