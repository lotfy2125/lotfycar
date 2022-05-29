from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect


from .models import *
from .restapis import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create an `about` view to render a static about page
# def about(request):
# ...
def about_us(request):
    
        return render(request, 'djangoapp/about.html')






# Create a `contact` view to return a static contact page
#def contact(request):
def contact_us(request):
    
        return render(request, 'djangoapp/contact.html')



# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/user_login_bootstrap.html', context)
    else:
        return render(request, 'djangoapp/user_login_bootstrap.html', context)





# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)




# Update the `get_dealerships` view to render the index page with a list of dealerships

def get_dealerships(request):
   if request.method == "GET":
        url = "https://86cac1fe.us-south.apigw.appdomain.cloud/delerships/entries"

        dealer_list = []
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)

    #    for dealer in dealerships:
    #        address = dealer.address
    #        city = dealer.city
    #        full_name = dealer.full_name
    #       id = dealer.id
    #        lat = dealer.lat
    #        long = dealer.long
    #        short_name = dealer.short_name
    #        state = dealer.state
    #        st = dealer.st
    #        zip = dealer.zip
            
        
    #       cardealer_obj = CarDealer( address, city, full_name, id, lat, long, short_name, state, st, zip) 
    #        dealer_list.append(cardealer_obj)   

       # print(dealer_list)

        # Concat all dealer's short name
        #dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return render( request , 'djangoapp/index.html' , {'dealerships': dealerships})

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...


def get_dealer_details(request, dealer_id):
    dealer_id = dealer_id
    if request.method == "GET":
        url = "https://86cac1fe.us-south.apigw.appdomain.cloud/review/entries"

       
        details = []
        # Get dealers from the URL
        dealers_details = get_dealer_reviews_from_cf(url , dealer_id )
     #   print(dealers_details)
      #  for dealer in dealers_details :
       #     if dealer.id == dealer_id :
         #       details.append(dealer) 

    return render( request , 'djangoapp/dealer_details.html'  , {'dealers_details': dealers_details , 'dealer_id' : dealer_id })
# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

