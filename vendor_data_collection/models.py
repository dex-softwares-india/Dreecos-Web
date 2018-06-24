from django.db import models

VENDOR_TYPE_CHOICES=(
    ('ice-cream','Ice Cream Vendor'),
    ('vegetables','Vegetable/Fruits Vendor'),
    ('street-food','Street Food Vendor'),
    ('drinks','Drinks')
)

AVAILABILITY_CHOICES=(
    ('year','Yearly'),
    ('season','Seasonally')
)


# Create your models here.
class Vendor_p1(models.Model):
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    availability=models.CharField(max_length=20,choices=AVAILABILITY_CHOICES,default='year')
    paytm_available=models.BooleanField(default=False)
    vendor_type=models.CharField(max_length=20,choices=VENDOR_TYPE_CHOICES,default='street-food')
    id_field=models.AutoField(primary_key=True)
    
    def __str__(self):
        return str(self.id_field)
