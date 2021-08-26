from django.db import models
from postgres_copy import CopyManager



class Csv(models.Model):
  file_name = models.FileField(upload_to='csvs')
  uploaded = models.DateTimeField(auto_now_add=True)
  activated = models.BooleanField(default=False)

  def __str__(self):
    return f'File id {self.id}'


class Sale(models.Model):
  InvoiceNo = models.CharField(max_length=200, null=True, blank=True)
  StockCode= models.CharField(max_length=200, null=True, blank=True)
  Description= models.CharField(max_length=255,null=True,blank=True)
  Quantity = models.IntegerField(null=True , blank=True)
  InvoiceDate= models.CharField(max_length=200, null=True, blank=True,)
  UnitPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  CustomerID=models.CharField(max_length=255,null=True,blank=True)
  Country= models.CharField(max_length=255,null=True,blank=True)
  objects = CopyManager()



  @classmethod
  def search_sale(cls,search_term):
        sale = cls.objects.filter(Description__icontains=search_term)
        return sale    


  def __str__(self):
        return str(self.StockCode)

  class Meta:
        ordering = ['-pk']     
      


