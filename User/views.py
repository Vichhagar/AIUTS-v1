from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *

class UserList(generic.ListView):
    model = Account
    context_object_name = 'users'
    template_name = 'User/home.html'

class UserDetail(generic.DetailView):
    model = Account
    template_name = 'User/detail.html'

# class AddUser(generic.CreateView):
#     model = Account
#     form_class = newUser
#     template_name = 'User/newUser.html'
#     success_url = '/'

def newUser(request):
    """Add new topic"""
    if request.method != 'POST':
        # meaning that no data is submitted
        form = newUser()
    else:
        # There is a data POST
        form = newUser(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            string = new_user.password
            hash_object = hashlib.md5(b'{string}')
            new_user.password = hash_object.hexdigest()

            string = new_user.username
            hash_object = hashlib.md5(b'{string}')
            new_user.username = hash_object.hexdigest()


            new_user.save()
            return redirect('/')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'User/newUser.html', context)

class makeTransaction(generic.CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'User/newTransaction.html'
    success_url = '/'

    

class AllTransaction(generic.ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'User/transaction.html'