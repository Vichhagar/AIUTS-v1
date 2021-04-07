from django.db import models
from django.contrib.auth.models import User
import hashlib

class Account(models.Model):
    username = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=50 )
    accountAmount = models.IntegerField(default=100)

    def __str__ (self):
        return self.username

    # def save(self, *args, **kwargs):
    #     print("this run too!!")

    #     username_to_hash = bytes(self.username, 'utf-8')
    #     hash_username = hashlib.md5(username_to_hash)
    #     self.username = hash_username.hexdigest()
    #     # self.username.save()

    #     # user = User.objects.create_user(username=self.username, password=self.password)
    #     # user.save()

    #     password_to_hash = bytes(self.password, 'utf-8')
    #     hash_password = hashlib.md5(password_to_hash)
    #     self.password = hash_password.hexdigest()
    #     # self.password.save()

        # super(Account, self).save(*args, **kwargs)


class Transaction(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    transactionID = models.AutoField(primary_key=True)
    username = models.ForeignKey(Account,  on_delete=models.CASCADE, related_name="Sender")
    Receiver = models.ForeignKey(Account,  on_delete=models.CASCADE, related_name="Receiver")
    Time = models.DateTimeField(auto_now_add=True)
    Amount = models.IntegerField(default=0)
    Message = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return f"transaction: {self.transactionID}"

    def save(self, *args, **kwargs):
        if self.Amount > self.username.accountAmount:
            return False
        else:
            self.username.accountAmount -= self.Amount
            self.username.save()
            print(self.username.accountAmount)
            super(Transaction, self).save(*args, **kwargs)

        self.Receiver.accountAmount += self.Amount
        self.Receiver.save()
        print(self.Receiver.accountAmount)
        super(Transaction, self).save(*args, **kwargs) # Call the real save() method

    # def update(self, *args, **kwargs):
    #    self.Receiver.accountAmount += self.Amount
    #    self.Receiver.save()
    #    super(Transaction, self).save(*args, **kwargs) # Call the real save() method







