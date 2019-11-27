from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db.models import Q
from .decorators import permission_required


class BucketListView(APIView):
    @permission_required()
    def get(self, request):
        try:
            user_id = request.META["user_id"]
            queryset_bucket_list = BucketList.objects.filter(user_id=user_id)
            serializer_data = BucketListSerializer(queryset_bucket_list, many=True).data
            return Response({"status": True, "message": "successfull", "data":serializer_data}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)
    

    @permission_required()
    def delete(self, request, bucket_id=None):
        try:
            BucketList.objects.filter(id=bucket_id).delete()
            return Response({"status": True, "message": "successfully deleted"}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)


    @permission_required()
    def post(self, request):
        try:
            user_id = request.META["user_id"]
            data = request.data
            BucketList.objects.create(**{"bucket_name":data['bucket_name'],"user_id_id":user_id})
            return Response({"status": True, "message": 'bucket name created successfully'}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)

    
    @permission_required()
    def patch(self, request):
        try:
            user_id = request.META["user_id"]
            data = request.data
            BucketList.objects.update_or_create(user_id=user_id,id=data['id'],defaults={"bucket_name": data['bucket_name']})
            return Response({"status": True, "message": 'bucket name updated successfully'}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)


class TodoListView(APIView):
    @permission_required()
    def delete(self, request, list_id=None):
        try:
            TodoList.objects.filter(id=list_id).delete()
            return Response({"status": True, "message": "successfully deleted"}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)

    
    @permission_required()
    def post(self, request):
        try:
            user_id = request.META["user_id"]
            data = request.data
            TodoList.objects.create(**{"todo_name":data['todo_name'],"is_done":data["is_done"],"bucket_id_id":data["bucket_id"]})
            return Response({"status": True, "message": 'todo created successfully'}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)

    
    @permission_required()
    def patch(self, request):
        try:
            user_id = request.META["user_id"]
            data = request.data
            TodoList.objects.update_or_create(bucket_id=data['bucket_id'],id=data['id'],defaults={"todo_name": data['todo_name'],"is_done":data["is_done"]})
            return Response({"status": True, "message": 'todo updated successfully'}, status=200)
        except Exception as e:
            return Response({"status": False, "message": format(e)}, status=200)
