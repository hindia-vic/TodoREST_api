from django.urls import path
from .views import Homeview,PostDetail

urlpatterns = [
    path('todo/',Homeview.as_view()),
    path('todo/<int:todo_id>/',PostDetail.as_view()),
]
