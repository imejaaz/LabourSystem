from django.shortcuts import render

def supervisor_dashboard(request):

    return render(request, 'supervisor/dashboard.html')