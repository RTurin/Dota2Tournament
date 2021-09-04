from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import DateField

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    auth_token = models.CharField(max_length=100,default="" )
    is_verified = models.BooleanField(default=False)



    def __str__(self):
        return self.full_name


class Product(models.Model):

    title = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField(blank=True,null=True)
    selling_price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
            return self.title


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)

positionChoice =(
    ('Safelane','Safelane'),
    ('Midlane','Midlane'),
    ('Offlane','Offlane'),
    ('Soft Support','Soft Support'),
    ('Hard Support','Hard Support'),
)

class Player(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    position = models.CharField(max_length=50,choices=positionChoice)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name        = models.CharField(max_length=50,null=True,blank=True)
    salane      = models.CharField(max_length=50,null=True,blank=True)
    midlane     = models.CharField(max_length=50,null=True,blank=True)
    offlane     = models.CharField(max_length=50,null=True,blank=True)
    softsupport = models.CharField(max_length=50,null=True,blank=True)
    hardsupport = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    title       = models.CharField(max_length=50,null=True,blank=True)
    prizepool   = models.IntegerField()


    def __str__(self):
        return self.title

class TournamentParticipate(models.Model):
    team        = models.ForeignKey(Team,on_delete=models.CASCADE)
    tournament  = models.ForeignKey(Tournament,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tournament.title) + "." + str(self.team.name)
    
matchChoice =(
    ("Group Stage","Group Stage"), 
    ("Play Offs","Play Offs"),
)


class Match(models.Model):
    matchType   = models.CharField(max_length=50,choices=matchChoice,blank=True,null=True)
    tournament  = models.ForeignKey(Tournament,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tournament.title) + "." + str(self.matchType)

class MatchDetail(models.Model):

    match       = models.ForeignKey(Match,on_delete=models.CASCADE)    
    
    date        = models.DateField(null=True,blank=True)

    team1       = models.CharField(max_length=50,blank=True,null=True)
    team2       = models.CharField(max_length=50,blank=True,null=True)


    duration    = models.FloatField(null=True,blank=True)

    matchid     = models.IntegerField(null=True,blank=True)

    victory     = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return str(self.team1) + " vs " + str(self.team2) + " (" + str(self.match.tournament.title) + "." + str(self.match.matchType) + ") "

# Testing Quearies Django 
