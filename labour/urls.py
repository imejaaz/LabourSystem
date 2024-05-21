from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('ceo/', include('ceo.urls')),
    path('supervisor/', include('supervisor.urls')),
    path('labor/', include('labor.urls')),
    path('recruitment/', include('recruitment.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)