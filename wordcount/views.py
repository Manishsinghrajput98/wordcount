from django.http import HttpResponse 
from django.shortcuts import render
def home(request):
	return render (request,'home.html')
def count(request):
	return render (request,'count.html')