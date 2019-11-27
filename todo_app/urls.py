from django.urls import path,include
from .views import *
from .todo_views import *

urlpatterns = [
    path('login/',Login.as_view()),
    path('register/',UserRegistration.as_view()),
    path('bucket-list/',BucketListView.as_view()),
    path('bucket-list/<int:bucket_id>/',BucketListView.as_view()),
    path('todo-list/',TodoListView.as_view()),
    path('todo-list/<int:todo_id>/',TodoListView.as_view())
]
