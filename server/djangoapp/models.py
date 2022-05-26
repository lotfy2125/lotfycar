from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarDealer(models.Model):

    
      city = models.CharField(max_length=100)
      state = models.CharField(max_length=100)
      st = models.CharField(max_length=2)
      address =  models.CharField(max_length=200)
      zip = models.IntegerField()
      lat = models.FloatField()
      long = models.FloatField()
      short_name = models.CharField(max_length=100)
      full_name = models.CharField(max_length=100)

      def __str__(self):
          return self.id +" "+ self.full_name + " "+ self.state


class DealerReview(models.Model):
    
      
      name = models.CharField(max_length=100)
      dealership = models.IntegerField()
      review = models.CharField(max_length=200)
      purchase = models.BooleanField()
      purchase_date = models.DateField()
      car_make =  models.CharField(max_length=100)
      car_model = models.CharField(max_length=100)
      car_year = models.DateField()
      
      def __str__(self):
        return self.name 

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name 



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

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
    year = models.DateField()

    def __str__(self) :
        
             return self.name 




# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):
    def __init__(self , address , city , full_name , id , lat , long , short_name , st , state ,zip ) :
          self.address = address      
          self.city = city
          self.full_name = full_name
          self.id = id         
          self.lat = lat
          self.long = long
          self.short_name = short_name
          self.st = st          
          self.state = state
          self.zip = zip
          
          return self.id + " " + self.full_name

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
    def __init__(self , id , name , dealership , review , purchase , purchase_date , car_make , car_model , car_year  ) :           
        self.id = id
        self.name = name 
        self.dealership = dealership
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        
        return self.id + " " + self.name + " " + self.review

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


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
