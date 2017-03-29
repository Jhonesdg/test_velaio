from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Cuentas,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,TransactionForm
from django.contrib.auth.models import User




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def account_list(request):
    cuentas = Cuentas.objects.filter(user=request.user)
    context = {'cuentas': cuentas}
    return render(request, 'Banco/account_list.html', context)

@login_required
def profile_edit(request):
    try:
        profile=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile=Profile(user=request.user)
        profile.save()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            email = request.POST.get("email", None)
            name = request.POST.get("name", None)
            lastname = request.POST.get("lastname", None)
            user = User.objects.get(pk=request.user.pk)
            if email:
                user.email = email
            if name:
                user.first_name = name 
            if lastname:
                user.last_name = lastname
            user.save()
            
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()
            return redirect('cuentas_list')
    else: 
        form = ProfileForm(instance=profile)
    context = {'form': form, 'create': True}
    return render(request, 'Banco/account_form.html', context)

def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(user=request.user,data=request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            account=transaction.account
            account.ammount=float(account.ammount)-float(transaction.ammount)
            account.save()
            to_account=transaction.to_account
            to_account.ammount=float(to_account.ammount)+float(transaction.ammount)
            to_account.save()
            transaction.save()
            form.save_m2m()
            return redirect('cuentas_list')
    else:
        form = TransactionForm(user=request.user)
    context = {'form': form, 'create': True}
    return render(request, 'Banco/transaction_form.html', context)


