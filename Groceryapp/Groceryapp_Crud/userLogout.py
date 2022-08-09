from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import UserLogOutSerializer
from Groceryapp.models import UserModel
from django.contrib.auth.hashers import check_password


class UserLogout(APIView):
    serializer_class = UserLogOutSerializer

    def post(self, request):
        # try:
        username = request.data.get("Username")
        print(username)
        data = UserModel.objects.get(Username=username)
        if data:
            # data.save()
            serializer = UserLogOutSerializer(data, partial=True)
            # serializer.is_valid(raise_exception=True)
            # user = serializer.save()
            return Response({'Message': 'Logout Successful',
                             'Results':serializer.data,
                             'HasError': False,
                             'Status': 200
                             })
        else:
            return Response("User is not found")