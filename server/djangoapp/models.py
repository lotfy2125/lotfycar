from django.db import models
from django.utils.timezone import now
import datetime


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name 



def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year


class CarModel(models.Model):
    
    CHOICES = (
        ('Sedan','Sedan'),
        ('SUV','SUV'),
        ('WAGON','WAGON')

    )

    

    make = models.ForeignKey(CarMake , default=1 , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    dealer_id =models.IntegerField()
    type = models.CharField( max_length=100, choices= CHOICES )
    year = models.IntegerField(choices=year_choices(), default=current_year())

    def __str__(self) :
        
             return self.name 
    

 



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):

    def __init__(self, address, city, full_name, id, lat, long, short_name, state, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.state = state
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_st(self):
        return self.st    
    def get_zip(self):
        return self.zip
    def get_full_name(self):
        return self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    def __init__(self , id , name , dealership , review , purchase , purchase_date , car_make , car_model , car_year,sentiment  ) :           
        self.id = id
        self.name = name 
        self.dealership = dealership
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        
       

    def get_name(self):
        return self.name
    def get_review(self):
        return self.review
    def get_car_make(self):
        return self.car_make   
    def get_car_model(self):
        return self.car_model
    def get_car_year(self):
        return self.car_year

    def __str__(self):
        return "name: " + self.name + "review: " + self.review

# Create your models here.

class car(models.Model):
   name = models.CharField(max_length=100)
   make = models.CharField(max_length=100)



# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
