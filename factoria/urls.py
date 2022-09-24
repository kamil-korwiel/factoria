from django.contrib import admin
from django.urls import path, include
from website.views import homepage_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name="homepage"),
    path('product/', include('products.urls')),
    path('business/', include('business.urls')),
]
