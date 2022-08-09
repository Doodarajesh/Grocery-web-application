from django.shortcuts import render
from Groceryapp.Groceryapp_Crud.user_register import UserRegister
from Groceryapp.Groceryapp_Crud.userLogin import UserLogin
from Groceryapp.Groceryapp_Crud.userLogout import UserLogout
from Groceryapp.Groceryapp_Crud.ItemPost import ItemPost
from Groceryapp.Groceryapp_Crud.getall_item import GetAllItems
from Groceryapp.Groceryapp_Crud.getallUserData import GetAllUser
from Groceryapp.Groceryapp_Crud.OrderItemPost import OrderItemPost
from Groceryapp.Groceryapp_Crud.GetUserOrder import GetAllOrderUser


# Create your views here.

UserRegister()
UserLogin()
UserLogout()
ItemPost()
GetAllItems()
GetAllUser()
OrderItemPost()
GetAllOrderUser()

