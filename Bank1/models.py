from django.db import models

# Create your models here.
from rest_framework.authtoken.admin import User


class Sogebanque(models.Model):
    sogebanque_user=models.ForeignKey(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=100)
    username=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=500)
    compte=models.DecimalField(max_digits=10,decimal_places=2)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.nom
    @property
    def Update_compte(self):
        if self.compte < 20:
            return " le montant de ce compte est inferieur a 20"
        else:
            return self.compte

class Unibanque(models.Model):
    nom=models.CharField(max_length=100)
    username=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    compte=models.DecimalField(max_digits=10,decimal_places=2)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.nom
    @property
    def Update_compte(self):
        if self.compte < 20:
            return " le montant de ce compte est inferieur a 20"
        else:
            return self.compte

#un a plusieurs
class OneToManyKey(models.Model):
    keyhere=models.ForeignKey(Unibanque,on_delete=models.CASCADE)

class ManyToManyKey(models.Model):
    keyhere=models.ManyToManyField(Unibanque,related_name='keyhere')


