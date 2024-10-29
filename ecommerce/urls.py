
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # thêm đường dẫn đến app accounts
   
	path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
	path('', include('store.urls')),
    
	path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# python manage.py migrate
# python manage.py loaddata data.json
# python manage.py runserver