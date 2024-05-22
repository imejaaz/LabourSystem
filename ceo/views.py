from django.shortcuts import render

def ceo_dashboard_view(request):
    return render(request, 'ceo/dashboard.html')