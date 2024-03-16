from django.shortcuts import render

# Create your views here.

# myapp/views.py
from django.http import HttpResponse


def home(request):
    user_email = request.META.get("HTTP_X_MS_CLIENT_PRINCIPAL_NAME", "Guest")
    return HttpResponse(f"Welcome {user_email}")
