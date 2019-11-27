from .models import *
from rest_framework import serializers


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields  = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields  = '__all__'


class BucketListSerializer(serializers.ModelSerializer):
    bucket_id_todo = TodoListSerializer(many=True)
    class Meta:
        model = BucketList
        fields  = ["bucket_id_todo","id","bucket_name"]

