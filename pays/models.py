from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField('Sim Service:', max_length=20 )

    def __str__(self):
        return self.name
    

class Plan(models.Model):
    service = models.ForeignKey(Service,related_name='services' , on_delete=models.CASCADE)
    amount = models.IntegerField(default=100)
    int_data = models.IntegerField("Data:GB",default=1)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.service}-Rs{self.amount}"
    
class Recharge(models.Model):
    username = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10, blank=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=100)

    def __str__(self):
        return f'{self.username} recharge of {self.plan}'
    
