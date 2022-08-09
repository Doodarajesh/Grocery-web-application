from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import GetOrderUserSerializer
from Groceryapp.models import ItemOrder


class GetAllOrderUser(APIView):
    QuerySet = GetOrderUserSerializer


    # queryset = Itemdetails

    def get(self, request,UserId):
        # try:
        item = ItemOrder.objects.filter(UserId=UserId)
        serializer = GetOrderUserSerializer(item, many=True)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        return Response({'Message': 'Successful',
                         'Result': serializer.data,
                         'HasError': False,
                         'Status': 200})

        # return HttpResponse("success", content_type="application/json")
        # except Exception as e:
