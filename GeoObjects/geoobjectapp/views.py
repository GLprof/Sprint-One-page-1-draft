from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GeogrObject
from .serializers import GeogrObjectSerializer

@api_view(['POST'])
def submitData(request):
    if request.method == 'POST':
        serializer = GeogrObjectSerializer(data=request.method)
        if serializer.is_valid():
            geogr_object=serializer.save()
            return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': geogr_object.id
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 400,
                'massage': 'Нехватка полей',
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'status': 500,
            'message': f'Ошибка при выполнении операции'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



