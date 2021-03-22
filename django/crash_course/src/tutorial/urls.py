from django.contrib import admin
from django.urls import path, include # Set 4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')), # Set 4
]
