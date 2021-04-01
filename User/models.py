from django.db import models

class Account(models.Model):
    username = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=50 )
    accountAmount = models.IntegerField(default=100)

    def __str__ (self):
        return self.username


class Transaction(models.Model):
    transactionID = models.AutoField(primary_key=True)
    username = models.ForeignKey(Account,  on_delete=models.CASCADE, related_name="Sender")
    Receiver = models.ForeignKey(Account,  on_delete=models.CASCADE, related_name="Receiver")
    Time = models.DateTimeField(auto_now_add=True)
    Amount = models.IntegerField(default=0)
    Message = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return f"transaction: {self.transactionID}"

