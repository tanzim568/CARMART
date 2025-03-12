from django.urls import path
from  .import views


urlpatterns = [
    # path('register/',views.signup,name='register' ),
    path('register/',views.signup.as_view(),name='register' ),
    path('profile/',views.Profile.as_view(),name='profile' ),
    path('cart/<int:id>/',views.buy_now,name='buy' ),
    path('password/',views.pass_change.as_view(),name='pass_change' ),
    path('edit_profile/',views.update_profile.as_view(),name='edit_profile' ),
    path('login/',views.user_loginview.as_view(),name='login' ),
    path('logout/',views.user_logoutview.as_view(http_method_names=['get','post']),name='logout' ),
]


