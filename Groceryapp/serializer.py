from django.apps import apps
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber']

    def create(self, validated_data):
        user = UserModel.objects.create(Firstname=validated_data['Firstname'],
                                        Lastname=validated_data['Lastname'],
                                        Email=validated_data['Email'],
                                        Username=validated_data['Username'],
                                        Password=make_password(validated_data['Password']),
                                        MobileNumber=validated_data['MobileNumber'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['Username', 'Password']


class UserLogOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['Username']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemdetails
        fields = ['Item_name', 'Description', 'Category', 'Variants', 'Price', 'Rating', 'reviews']

    def create(self, validated_data):
        item = Itemdetails.objects.create(Item_name=validated_data['Item_name'],
                                          Description=validated_data['Description'],
                                          Category=validated_data['Category'],
                                          Variants=validated_data['Variants'],
                                          Price=validated_data['Price'],
                                          reviews=validated_data['reviews'],
                                          Rating=validated_data['Rating'])
        item.save()
        return item


class GetAllItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemdetails
        fields = "__all__"


class OrderItemsSeralizers(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = ['UserId', 'ItemId', 'Quantity']

    def create(self, validated_data):
        itemset = validated_data['ItemId']
        quality = validated_data['Quantity']
        amount = itemset.Price*quality
        order = ItemOrder.objects.create(UserId=validated_data['UserId'],
                                         ItemId=itemset,
                                         Quantity=quality,
                                         amount=amount)
        order.save()
        return order

class GetOrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = ['UserId', 'ItemId', 'Quantity', 'amount']
