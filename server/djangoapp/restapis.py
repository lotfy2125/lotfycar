import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth
from django.shortcuts import get_object_or_404, render, redirect


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))




import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data




# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


def post_request(url, json_payload, **kwargs):
    
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
     response = requests.post(url, params=kwargs, json=json_payload)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    print(json_data)

    return json_data


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list

def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
     
        # For each dealer object
        #for dealer_doc in dealers:
        #for dealer in dealers:
        #    address = dealer["address"]
        #   city = dealer["city"]
        #    full_name = dealer["full_name"]
        #    id = dealer["id"]
        #    lat = dealer["lat"]
        #    long = dealer["long"]
        #    short_name = dealer["short_name"]
        #    state = dealer["state"]
        #    st = dealer["st"]
        #    zip = dealer["zip"]
            
          
        #    cardealer_obj = CarDealer( address, city, full_name, id, lat, long, short_name, state, st, zip) 
        #     results.append(cardealer_obj)   

    return dealers





# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list

def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url )
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result["entries"]
   # print(reviews)
    return reviews



def sav_dealer_reviews_to_cf(url,  json_payload , dealer_id):
    results = []
    # Call get_request with a URL parameter
    json_result = post_request(url , json_payload , dealer_id  )
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result["entries"]
    print(reviews)
    return redirect("djangoapp:dealer_details", dealer_id=dealer_id)


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



