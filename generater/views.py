from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
        return render(request, 'generater/home.html')

def about(request):
        return render(request, 'generater/about.html')

def password(request):

        characters = list('abcdefghijklmnopqrstzwxyz')
        if request.GET.get('uppercase'):
                characters.extend('ABCDEFGHIJKLMNOPQRSTVWXYZ')
        if request.GET.get('special'):
                characters.extend('!@#$%^&*()_+')  
        if request.GET.get('number'):
                characters.extend('0123456789')       
        len = int(request.GET.get('length'))
        thepassword = ''
        for x in range(len):
                thepassword += random.choice(characters)

        return render(request, 'generater/password.html', { 'password' : thepassword })