from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

    def __str__(self):
        return self.name


class Work(models.Model):
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    postalZip = models.CharField(max_length=128)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.company


class Account(models.Model):
    pin = models.IntegerField(max_length=128)
    acc_num = models.CharField(max_length=128)
    pan = models.CharField(max_length=128)
    cvv = models.IntegerField(max_length=128)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_num




