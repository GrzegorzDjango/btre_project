from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor
# choices to jest plik z wartościami stałymi w słownikach które chcemy dodać do list rozwijalnych na stronie
from listings.choices import price_choices, bedroom_choices, state_choices


# funcje poniżej są wywoływane przez urls
# np urlpatterns = [
#     path('', views.index, name='index'),
# name='index' wykorzystujemy w plikach w linkach do innych stron <a href="{% url 'index' %}">
def index(request):
    # chcemy na głównej stronie wyświetlić 3 nieruchomości
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get mvp
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
