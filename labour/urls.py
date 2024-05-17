from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('labor/', include('account.urls')),
    path('ceo/', include('ceo.urls')),
    path('supervisor/', include('supervisor.urls')),
    path('labor/', include('labor.urls')),

]
