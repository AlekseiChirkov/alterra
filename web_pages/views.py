from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    context = {}
    return render(request, 'web_pages/index.html', context)
