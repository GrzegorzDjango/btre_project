from django.urls import path
from . import views

#urlpatterns = [
# ...
#   path('listings/',include('listings.urls')),
# te urlpatterns zostały załączone w urls.py w btre i dlatego ich początek będzie listints/...

urlpatterns = [
    path('', views.index, name='listings'),
    # /listings/id   we views mamy def listing(request, listing_id):
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),

]
