from django.urls import path
<<<<<<< HEAD
from .views import TodoList,TodoDetail,TodoCreate,TodoDelete,TodoUpdate,ToDoComment,Toplist

urlpatterns = [
    path('', Toplist.as_view(), name='list'),
=======
from .views import TodoList,TodoDetail,TodoCreate,TodoDelete,TodoUpdate

urlpatterns = [
>>>>>>> da6386698c765c6adc43569e0f1d9ab7088399e8
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/',TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>',TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>',TodoUpdate.as_view(), name='update'),
<<<<<<< HEAD
    #
    path('abc/', ToDoComment.as_view(), name='comment'),
]
=======
]

>>>>>>> da6386698c765c6adc43569e0f1d9ab7088399e8
