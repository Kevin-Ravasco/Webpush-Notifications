from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pushapp.urls')),
    # to register the service worker at the root of our project
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
    path('webpush/', include('webpush.urls')),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
