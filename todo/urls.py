from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todo-app-backend/admin/', admin.site.urls),
    path('todo-app-backend/',include('todo_app.urls')),
]

