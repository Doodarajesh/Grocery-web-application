from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import UserLoginSerializer
from Groceryapp.models import UserModel
from django.contrib.auth.hashers import check_password


class UserLogin(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        # try:
        username = request.data.get("Username")
        print(username)
        passwd = request.data.get("Password")
        data = UserModel.objects.get(Username=username)
        if username == data.Username and check_password(passwd,data.Password):
            # data.save()
            serializer = UserLoginSerializer(data, partial=True)
            # serializer.is_valid(raise_exception=True)
            # user = serializer.save()
            return Response({'Message': 'Login Successful',
                             'Results':serializer.data,
                             'HasError': False,
                             'Status': 200
                             })
        else:
            return Response("please enter valid username and password")