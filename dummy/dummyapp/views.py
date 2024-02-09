from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dummyapp.models import Student
from dummyapp.serializer import StudentSerializer

class StudentGet(APIView):
    
    def get( self,request):
        
        data = Student.objects.all()
        
        serial = StudentSerializer(data, many=True)
        
        if serial.is_valid:
            return Response( {"data":serial.data})
          
        return Response(serial.error, status=status.HTTP_404_NOT_FOUND)

class AddStudent(APIView):
    def post( self , request):
        serial = StudentSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response ( {"Data":serial.data})
        return Response( serial.error ,status=status.HTTP_400_BAD_REQUEST)
    