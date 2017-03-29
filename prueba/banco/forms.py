from django.forms import ModelForm
from django import forms
from .models import Profile,Transaction,Cuentas

class ProfileForm(ModelForm):
	name = forms.CharField(label = "Name", required = True)
	lastname = forms.CharField(label = "Lastname", required = True)
	email = forms.EmailField(label = "Email",  required = True)
	class Meta:
		model = Profile
		fields=('name','lastname','id_number','email', 'phone','addres',)

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields=('account','to_account','ammount','description')
	def __init__(self, user, *args, **kwargs):
		super(TransactionForm, self).__init__(*args, **kwargs)
		self.fields['account'] = forms.ModelChoiceField(queryset=Cuentas.objects.filter(user=user))
	def clean_ammount(self):
		ammount = self.cleaned_data['ammount']
		account = self.cleaned_data['account']
		if (ammount > account.ammount) or account.ammount==0:
			raise forms.ValidationError("No tienes fondos suficientes")
		return ammount