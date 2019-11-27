from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db.models import Q

import jwt
import datetime

private_key = open('jwt-key').read()
public_key = open('jwt-key.pub').read()

class UserRegistration(APIView):
    def post(self, request):
        try:
            data = request.data
            if 'email_id' not in data or 'password' not in data:
                return Response({"status": False, "message":'All fields are required'}, status=200)
            query = UserAccount.objects.filter(email_id=data['email_id'])
            serializer = UserAccountSerializer(query, many=True).data
            if serializer:
                return Response({"status": False, "message":'email already registered'}, status=200)
            else:
                UserAccount.objects.create(**{"email_id":data["email_id"],"password":data["password"],'first_name':data['first_name'],'last_name':data['last_name']})
                return Response({"status": True, "message":'successfull created'}, status=200)
        except Exception as e:
            return Response({"status": False, "message":format(e)}, status=200)


class Login(APIView):
    def post(self, request):
        data = request.data
        if (('email_id' and 'password') or 'refresh_token') in data.keys():
            if 'password' in data.keys():
                query = UserAccount.objects.filter(email_id=data['email_id'],password=data['password'])
                serializer = UserAccountSerializer(query, many=True).data
                if serializer:
                    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
                    payload = {"iat":datetime.datetime.utcnow(),"exp":exp,"user_id":serializer[0]['id']} 
                    access_token = jwt.encode(payload,private_key,algorithm='RS256')
                    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
                    payload = {"iat":datetime.datetime.utcnow(),"exp":exp,"user_id":serializer[0]['id']}
                    refresh_token = jwt.encode(payload,private_key,algorithm='RS256')
                    return Response({"status": True, "message": "LOGIN_SUCCESS","data": {"access_token": access_token, "refresh_token": refresh_token}}, status=200)
                else:
                    return Response({"status": False, "message":"LOGIN_EMAIL_ID_PASSWORD_WRONG"}, status=200)
            else:
                try:
                    refresh = data["refresh_token"]
                    payload = jwt.decode(refresh, public_key, algorithms=['RS256'])
                    payload["iat"] = datetime.datetime.utcnow();
                    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=60);
                    access_token = jwt.encode(payload, private_key, algorithm='RS256')
                    payload["iat"] = datetime.datetime.utcnow();
                    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=120);
                    refresh_token = jwt.encode(payload, private_key, algorithm='RS256')
                    return Response({"status": True, "message": "LOGIN_SUCCESS","data": {"access_token": access_token, "refresh_token": refresh_token}}, status=200)
                except Exception as e:
                    return Response({"status": False, "message":"LOGIN_REFRESH_TOKEN_EXPIRED"}, status=200)
        else:
            return Response({"status": False, "message":"LOGIN_FIELDS_MISSING"}, status=200)

