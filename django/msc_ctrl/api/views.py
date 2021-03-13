from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('<h3>Hello from django</h3>')
