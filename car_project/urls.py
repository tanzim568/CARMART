
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from  .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage' ),
    path('brandmodel/<slug:brand_slug>/', views.home,name='brandwise'),
    path('carmodel/', include('CarModel.urls')),
    path('brandmodel/', include('BrandModel.urls')),
    path('accounts/', include('Profile.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)