from django.shortcuts import render


def ceo_dashboard_view(request):
    print('cem ds')
    return render(request, 'ceo/dashboard.html')