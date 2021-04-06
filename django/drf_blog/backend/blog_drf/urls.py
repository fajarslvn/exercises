from django import urls
from django.contrib import admin
# All new
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), # new
    path('summernote/', include('django_summernote.urls')), # new
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # new

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]