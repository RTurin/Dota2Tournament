from django.contrib import admin
from .models import *



# Register your models here.


from .models import *
# Create your models here.
admin.site.register(
    [
    # Customer,Product,Cart,CartProduct,
    Team,Tournament,TournamentParticipate,
    Match,MatchDetail,
    ]
)
