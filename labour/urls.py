from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('ceo/', include('ceo.urls')),
    path('supervisor/', include('supervisor.urls')),
    path('labor/', include('labor.urls')),
    path('recruitment/', include('recruitment.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Labour Management System"
admin.site.site_title = "Labour Portal"
admin.site.index_title = "Welcome to Labour portal"