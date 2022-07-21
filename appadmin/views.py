from django.shortcuts import render
 
# Create your views here.

def admin_login(request):
    return render(request,'appadmin/login.html')

def user_details(request):
    return render(request,'appadmin/userdetails.html')

def profile_update(request):
    return render(request,'appadmin/profileupdate.html')

def stock_update(request):
    return render(request,'appadmin/stockupdate.html')

def payment_details(request):
    return render(request,'appadmin/paymentdetails.html')   

    
