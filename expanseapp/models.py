from django.db import models

# Create your models here.
class Expense(models.Model):
    purpose = models.CharField(max_length=250)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add= True)


    def __str__(self):
        return self.purpose
    
