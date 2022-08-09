from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import OrderItemsSeralizers


class OrderItemPost(APIView):
    serializer_class = OrderItemsSeralizers

    def post(self, request):
        # try:
        serializer = OrderItemsSeralizers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'Message': 'Successful',
                         'Result': serializer.data,
                         'HasError': False,
                         'Status': 200})
        # return HttpResponse("success", content_type="application/json")
        # except Exception as e:

