from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *
import hashlib
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class UserList(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Account
    context_object_name = 'users'
    template_name = 'User/home.html'

    def get_queryset(self):

        return Account.objects.all()[:5:-1]

class UserDetail(LoginRequiredMixin, generic.DetailView):
    model = Account
    template_name = 'User/detail.html'

    # def get_queryset(self):
    #     transaction = Transaction.objects.filter(username=self.request.POST.get('username'))
    #     print(transaction)
    #     return transaction
    # def get_queryset(self):
    #     return Transaction.objects.filter(user__id=self.request.user.pk)

class AddUser( generic.CreateView):
    model = Account
    form_class = newUser
    template_name = 'User/newUser.html'
    success_url = '/'

    def form_valid(self, form):
        f = form.save(commit=False)

        username_to_hash = bytes(f.username, 'utf-8')
        hash_username = hashlib.md5(username_to_hash)
        f.username = hash_username.hexdigest()

        user = User.objects.create_user(username=f.username,password=f.password)
        user.save()

        password_to_hash = bytes(f.password, 'utf-8')
        hash_password = hashlib.md5(password_to_hash)
        f.password = hash_password.hexdigest()
        # self.password.save()



        # user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['password'])
        # user.save()
        return super().form_valid(form)

class makeTransaction(LoginRequiredMixin, generic.CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'User/newTransaction.html'
    success_url = '/'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
        # form.user = self.request.user
        # return super().form_valid(form)

    

class AllTransaction(generic.ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'User/transaction.html'