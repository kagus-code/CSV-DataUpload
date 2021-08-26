from datafull.models import Csv, Sale
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
import datetime as dt
from .forms import CsvModelForm
import csv
from django.db import connection
from django.core.management.base import BaseCommand

# Create your views here.
def upload(request):
    date = dt.date.today()
    if request.method == 'POST':
      form = CsvModelForm(request.POST or None, request.FILES or None)
      if form.is_valid():
        csvFile = form.save(commit=False)
        csvFile.save()
        obj = Csv.objects.get(activated=False)
        # with open(obj.file_name.path, 'r',encoding='latin1') as f:
        insert_count = Sale.objects.from_csv(obj.file_name.path,encoding='latin1')
        print (f"{insert_count} records inserted")




      

          
          # reader = csv.reader(f)

          # for i, row in enumerate(reader):
          #   if i==0:
          #     pass
          #   else:
          #     Sale.objects.create(
          #     InvoiceNo = row[0],
          #     StockCode = row[1],
          #     Description =row[2],
          #     Quantity = int(row[3]),
          #     InvoiceDate = row[4],
          #     UnitPrice =float(row[5]),
          #     CustomerID = row[6],
          #     Country = row[7],
          #     )
              


        return redirect(upload)
    else:
        form = CsvModelForm
    return render(request, 'upload.html' ,{"date": date, 'form':form})