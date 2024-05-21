from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
def dashboard(request):
    user = User.objects.get(email='admin@admin.com')
    print(user)
    try:
        obj = get_object_or_404(Labor, user=user)
    except Labor.DoesNotExist:
        raise Http404("No Labor matches the given query.")
    print(obj)
    return render(request, 'labor/dashboard.html',{'labor':obj})