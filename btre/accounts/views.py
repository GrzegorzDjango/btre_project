from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contacts.models import Contact
#żeby sprawdzić czy User już istnieje
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Register User
        # w message damy eerror który pójdzie do register w kórym będzie partial _alerts.html

        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'That email is taken')
            return redirect('register')
        else:
            pass
            # Looks good, let's register user !!
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            # tak można by zrobić ale koniec końców zrobimy inaczej
            #auth.login(request, user)
            #messages.success(request, 'You are now logged in')
            #return redirect('index')

            #robimy tak
            user.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')

        return redirect('register')
    else:
        return render(request, 'accounts/register.html' )

def login(request):
    if request.method == 'POST':
        # login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html' )

# po logout chcemy iść do strony głównej
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')



def dashboard(request):
    # szukamy kontaktór walogowanego usera
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context )