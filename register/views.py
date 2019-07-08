from django.shortcuts import render

# Create your views here.
def registerView(request):
    render('register/', 'register.html' , {})

