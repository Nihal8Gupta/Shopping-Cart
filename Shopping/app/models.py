from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200,primary_key=True)
    image = models.ImageField(upload_to='category',null=True)
    def __str__(self):
        return self.category
    
class Product(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to="product")
    details = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    price = models.FloatField()
    discount_price = models.FloatField(default=0)
    actual_price = models.FloatField(null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product_cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    counter = models.PositiveIntegerField(default=0)
    ammount = models.PositiveBigIntegerField(null=True)
    def __str__(self):
        return self.name.name



class Order_history(models.Model):
    order_status = [('Pending','Pending'),('Packed','Packed'),('Delivered','Delivered'),('Cancel','Cancel')]
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveBigIntegerField()
    status = models.CharField(max_length=200,choices=order_status,default='Pending')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user.first_name


class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    user_pic = models.ImageField(upload_to='user_pic',default='avtar.jpg')
    address = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.username.username