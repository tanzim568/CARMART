from django.db import models
from django.contrib.auth.models import User
from CarModel.models import Car
from BrandModel.models import Brand

# Create your models here.

# class Cart(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
#     car=models.ManyToManyField(Car)
#     date=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"User:{self.user.first_name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)  # ✅ One user can have multiple cart entries
    car = models.ForeignKey(Car, on_delete=models.CASCADE,null=True,blank=True)  # ✅ Each entry represents a specific car
    quantity = models.IntegerField(default=1,null=True,blank=True)  # ✅ Track quantity per car

    def __str__(self):
        return f"{self.user.username} - {self.car.name} (x{self.quantity})"
