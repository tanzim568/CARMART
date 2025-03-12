from django.shortcuts import render,redirect
from CarModel.models import Car
from BrandModel.models import Brand



def home(request,brand_slug=None):
    data=Car.objects.all()
    if brand_slug is not None:
        brand=Brand.objects.get(slug=brand_slug)
        data=Car.objects.filter(brand=brand)
    brands=Brand.objects.all()
    return render(request,'./home.html',{'data':data,'brands':brands})


# def home(request,brand_slug=None):
#     data=Car.objects.all()
#     brands=Brand.objects.all()
#     if brand_slug is not None:
#         brands=Brand.objects.filter(slug=brand_slug)
#         data=Car.objects.filter(brand=brands)
#     return render(request,'./home.html',{'data':data,'brands':brands})
