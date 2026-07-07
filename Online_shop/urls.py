from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('orders/', include('orders.urls', namespace='orders')),

    # API
    path('api/accounts/', include('accounts.api_urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
