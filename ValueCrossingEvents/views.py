from django.shortcuts import render
from .serializer import ValueCrossingsSerializer
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from .crossingEvents import CrossingEvents
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import json

class ValueCrossingEvents(APIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get(self,request, format=None):

        #content = {
        #    'user': request.user,
        #    'auth': request.auth
        #}
        signal = [1, 2, 3, 3, 4, 5, 5, 6, 3, 2, 1]
        value = 5
        event = CrossingEvents(signal,value)
        serializer = ValueCrossingsSerializer(event)
        return Response(serializer.data)


    def post(self,request,format=None):

        serializer = ValueCrossingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print (serializer.data["signal"], serializer.data["value"])

            sum_events = CrossingEvents(serializer.data["signal"],int(serializer.data["value"])).get_number_of_value_crossings()
            print (sum_events)
            return Response({"sum_value_crossing_events": sum_events}, status=status.HTTP_201_CREATED)
            #return Response(sum_events, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)





