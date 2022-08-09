from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from Groceryapp.serializer import ItemSerializer


class ItemPost(APIView):
    serializer_class = ItemSerializer

    def post(self, request):
        # try:
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'Message': 'Successful',
                         'Result': serializer.data})
        # return HttpResponse("success", content_type="application/json")
        # except Exception as e:
        #     return Response({'Message': 'Successful',
        #                      'Result': e,
        #                      'HasError': False,
        #                      'Status': 200})
