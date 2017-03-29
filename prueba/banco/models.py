from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cuentas(models.Model):
	name=models.CharField("Name",max_length=300)
	ammount=models.CharField("Ammount",max_length=200)
	user=models.ForeignKey(User)
	number=models.IntegerField(unique=True, max_length=20)

class Transaction(models.Model):
	account=models.ForeignKey(Cuentas,null=False,related_name='account_transaction')
	user=models.ForeignKey(User)
	to_account=models.ForeignKey(Cuentas,null=False,related_name='account_to')
	ammount=models.CharField("Ammount",max_length=200)
	description=models.CharField("Description",max_length=200,null=True,blank=True)
	date=models.DateField( auto_now_add=True)

class Profile(models.Model):
	user=models.ForeignKey(User,unique=True)
	id_number=models.CharField("id_number",max_length=50,null=True)
	phone=models.IntegerField("phone",max_length=50,null=True)
	addres=models.CharField("addres",max_length=100,null=True)

	def get_profile(user):
		return Profile.objects.get(user=user)

