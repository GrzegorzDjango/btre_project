from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        # listing_id jest ukrytym polem w naszej formie i teraz je zbieramy
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # sprawdzamy że user już składał zapytanie
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        # w settings na dole ustawiliśmy szczegóły naszej poczty żeby można było wysyłać mejle
        # nie zadziałało bo google zblokowało
        send_mail(
            'This is subjectProperty Listing Inquire',
            'This is body. There as been inquire for '+ listing + '. Sign into the admin panel for more info',
            'grzegorz.kania1983@gmail.com', # kto wysyła
            [realtor_email, 'wladi83@poczta.onet.pl'], # do kogo wysyłamy
            fail_silently=False,

        )

        messages.success(request, 'Your request has been submitter, a realtor will get back to  you soon')

        return redirect('/listings/'+listing_id)
