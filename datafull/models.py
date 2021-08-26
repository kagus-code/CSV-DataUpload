from django.db import models

# Create your models here.
class Csv(models.Model):
  file_name = models.FileField(upload_to='csvs')
  uploaded = models.DateTimeField(auto_now_add=True)
  activated = models.BooleanField(default=False)

  def __str__(self):
    return f'File id {self.id}'


class Sale(models.Model):
  InvoiceNo = models.IntegerField(null=True , blank=True)
  StockCode= models.CharField(max_length=200, null=True, blank=True,unique=True)
  Description= models.CharField(max_length=255,null=True,blank=True)
  Quantity = models.PositiveIntegerField(null=True , blank=True, default=0)
  InvoiceDate= models.CharField(max_length=200, null=True, blank=True,)
  UnitPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  CustomerID=models.IntegerField(null=True , blank=True)
  Country= models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
        return str(self.StockCode)


  def save_sale(self):
        self.save()