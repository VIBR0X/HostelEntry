from pytz import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True) 
    return Response(serializer.data) 

@api_view(['POST'])
def addItem(request):
    task = Item.objects.create()
    task.Roll_Number_1=request.data["Roll_Number_1"]
    task.Roll_Number_2=request.data["Roll_Number_2"]
    task.save()
    serilizer=ItemSerializer(task)
    return Response(serilizer.data)


@api_view(['PUT'])
def updateItem(request, pk):
    task = Item.objects.get(id = pk)
    task.save()
    serilizer=ItemSerializer(task)
    return Response(serilizer.data)


   
@api_view(['GET'])
def getItem(request,pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item) 
    return Response(serializer.data) 


@api_view(['DELETE'])
def Delete(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response() 
