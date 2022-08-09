from django.db import models


# Create your models here.

class UserModel(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Username = models.CharField(max_length=60, unique=True)
    Password = models.CharField(max_length=50)
    MobileNumber = models.BigIntegerField()
    objects = models.Manager

    class Meta:
        db_table = "user_data"


class Status(models.TextChoices):
    RICE = 'RICE'
    OIL = 'OIL'
    MILK = 'MILK'


class Itemdetails(models.Model):
    Item_name = models.CharField(max_length=30)
    Description = models.CharField(max_length=255)
    Category = models.CharField(max_length=30, choices=Status.choices)
    Variants = models.CharField(max_length=30)
    Price = models.IntegerField()
    Rating = models.IntegerField()
    Quantity = models.CharField(max_length=30)
    reviews = models.CharField(max_length=50)
    objects = models.Manager


class ItemOrder(models.Model):
    UserId = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='User')
    ItemId = models.ForeignKey(Itemdetails, on_delete=models.CASCADE, related_name='Item')
    Quantity = models.IntegerField()
    amount = models.IntegerField()
    objects = models.Manager





