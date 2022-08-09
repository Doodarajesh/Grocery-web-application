from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import UserSerializer


class UserRegister(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        # try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'Message': 'Successful',
                         'Result': serializer.data,
                         'HasError': False,
                         'Status': 200})
        # return HttpResponse("success", content_type="application/json")
        # except Exception as e:

