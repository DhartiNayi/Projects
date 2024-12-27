from rest_framework.decorators import api_view
from rest_framework.response import Response

from Myapp.models import Person
from Myapp.serializers import PeopleSerializer

@api_view(['GET','POST','PUT'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['Flask' , 'Django' ,'Tornado' , 'FastApi'],
        'course_provider' : 'Scaler'
        }
    
    if request.method == 'GET':
        print(request.GET.get('search'))
        print('YOU HIT A GET METHOD') 
        return Response(courses)     
    
    elif request.method =='POST':
        data = request.data
       
        # print(data)
        print(data['name'])    
        print(data['age'])    
        print('YOU HIT A POST METHOD')
        return Response(courses)  
    
    elif request.method =='PUT':
        print('YOU HIT A PUT METHOD')
        return Response(courses)  
    

    
@api_view(['GET','POST','PUT','PATCH','DELETE'])     
def person(request):
    if request.method== 'GET':
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)             
        
        
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)              
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id= data['id'])
        serializer = PeopleSerializer(data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)          
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' : 'person deleted'})