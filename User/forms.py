from django import forms
from .models import *
import hashlib

class newUser(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 
                    'password']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'username',
            'Receiver',
            'Amount',
            'Message'
        ]




