from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import ItemSerializer, GetAllItemSerializer
from Groceryapp.models import Itemdetails


class GetAllItems(APIView):
    QuerySet = GetAllItemSerializer


    # queryset = Itemdetails

    def get(self, request):
        # try:
        item = Itemdetails.objects.all()
        serializer = GetAllItemSerializer(item, many=True)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        return Response({'Message': 'Successful',
                         'Result': serializer.data,
                         'HasError': False,
                         'Status': 200})

        # return HttpResponse("success", content_type="application/json")
        # except Exception as e:
