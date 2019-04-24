from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


def index(request):
    # można jednocześnie sortować i filtrować
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    #paginator, ile listingow na stronie, mozna to ladnie zrobic paginatorem... i zwrocic go jako liste listingow

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # szukamy konkretnej nieruchomości
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # request z url bierzemy jako dictionary i wyciagamy z niego wartoście np. 'keywords'
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # czy w polu description jest słowo szukane
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # City musi się zgadzać dokładnie
            queryset_list = queryset_list.filter(city__iexact=city)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # bedrooms mniejsze rowne <= == lte
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # State musi się zgadzać dokładnie
            queryset_list = queryset_list.filter(state__iexact=state)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # bedrooms mniejsze rowne <= == lte
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'listings': queryset_list,
        'values': request.GET,  #dodajemy, żeby serach zapamiętał o co pytaliśmy i żeby to nie snikało
    }
    return render(request, 'listings/search.html', context)
