from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from CarModel.models import Car
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth import logout,update_session_auth_hash
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from cart.models import Cart
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages



class signup(CreateView):
    form_class = forms.RegisterForm
    template_name = './register.html'
    success_url = reverse_lazy('login')  
    
    def form_valid(self, form):
        messages.success(self.request,"Account created successfully")
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='Signup'
        return context
    
    
# class profile(CreateView):
#     # template_name = './profile.html'
#     # success_url = reverse_lazy('login')
#     def get (self,request):
#         # current_user = request.user
#         # # print(current_user)
#         data=Cart.objects.get(user=request.user)
#         cars=data.car
#         print(cars.name)
#         return render(request,'./profile.html',{"cars":cars.name})  


# from django.shortcuts import render
# from django.views import View
# from .models import Cart

class Profile(View):  # Use View instead of CreateView
    def get(self, request):
        # Get all cars in the user's cart
        cart_items = Cart.objects.filter(user=request.user)  

        # Extract car names
        cars = [item.car.name for item in cart_items]  

        # Debugging
        for items in cart_items:
            print(items.car)    

        return render(request, 'profile.html', {"cars": cart_items})
        # return render(request, 'profile.html')

    

class user_loginview(LoginView):
    form_class=AuthenticationForm
    template_name='./register.html'
    success_url=reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,"Login Successfull")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
class user_logoutview(LogoutView):
    # success_url=reverse_lazy('login')
    
    def get(self,request,*args, **kwargs):
        logout(self.request)
        messages.success(self.request,"Logged Out Successfully")
        return redirect("login")

class update_profile(UpdateView):
    model = User
    form_class = forms.UserUpdateForm
    template_name = './edit_profile.html'
    success_url = reverse_lazy('profile')
    # pk_url_kwarg='id'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request,"Password Updated")
        return super().form_valid(form)
 
class pass_change(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = './pass.html'
    success_url = reverse_lazy('profile')

    
    def form_valid(self, form):
        update_session_auth_hash(self.request,form.user)
        messages.success(self.request,"Password Updated")
        return super().form_valid(form)
    
# class buy_now(CreateView):


# def buy_now(request, id):
#     data = Car.objects.get(pk=id)
#     if request.method == 'POST':
#         if data.quantity > 0:
#             data.quantity -= 1
#             data.save()
#             cart = Cart.objects.filter(user=request.user)
#             # cart.car.add(data)
#             # print(cart)
#             for items in cart:
#                 items.car = data
#                 items.save()
#                 print(items.car)
#             # cart.save()
#         return render(request, './profile.html',{'cars':cart})
#         # return render(request, './profile.html', {"cars": cart.car.all()})






def buy_now(request, id):
    car = get_object_or_404(Car, pk=id)

    if request.method == 'POST':
        if car.quantity > 0:
            car.quantity -= 1  # Reduce stock quantity
            car.save()

            # Instead of updating existing, create a new cart entry every time
            cart_item = Cart.objects.create(user=request.user, car=car, quantity=1)
            cart_item.save()

            messages.success(request, "Car added to your cart!")

        else:
            messages.error(request, "Sorry, this car is out of stock.")

    # Get all cars in the cart for the user
    cart_items = Cart.objects.filter(user=request.user)

    return render(request, 'profile.html', {'cars': cart_items})

  
    
     
    