from django.shortcuts import render

# Placeholder view for core ERP

def home(request):
    return render(request, 'core_erp/home.html')
