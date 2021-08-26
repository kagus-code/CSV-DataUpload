from django.shortcuts import render
import datetime as dt
# Create your views here.
def upload(request):
    date = dt.date.today()
    return render(request, 'upload.html' ,{"date": date,})