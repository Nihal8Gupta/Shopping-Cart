from django.contrib import admin
from .models import *

admin.site.site_header='Shopping || Admin Portal'
admin.site.site_title="Shopping"

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','user_pic','address']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk','name','image','details','category','price','discount_price','actual_price','is_available']

@admin.register(Product_cart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ['pk','user','name','counter','ammount']

@admin.register(Order_history)  
class OrderhistoryAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','status']