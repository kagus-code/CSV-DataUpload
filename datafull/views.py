from django.utils.translation import activate
from datafull.models import Csv, Sale
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
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
            with open(obj.file_name.path, 'r',encoding='latin1') as f:
                insert_count = Sale.objects.from_csv(
                    f,
                    delimiter=",", 
                    drop_constraints=True, 
                    drop_indexes=True, 
                    encoding="latin-1",
                    ignore_conflicts=True
                    )
                print(f"{insert_count} records inserted")
                Csv.objects.filter(activated=False).update(activated=True)

            return redirect(upload)
    else:
        form = CsvModelForm
    return render(request, 'upload.html', {"date": date, 'form': form})
