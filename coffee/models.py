import datetime

from django.db import models
from django.utils import timezone



class Coffee(models.Model):
     
    freeText = models.CharField(max_length=200)
    orderDate = models.DateTimeField('date published')
    
    def was_ordered_recently(self):
        return self.orderDate >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return str(self.orderDate)
    
