from django.contrib import admin
from django.urls import path, include
from website.views import homepage_view, products_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name="homepage"),
    path('products/', products_view, name="products"),
    path('business/', include('business.urls')),
]
