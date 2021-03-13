from django.urls import path

from .views import TaskList, TaskItem

app_name = 'foo'
urlpatterns = [
	path('', TaskList.as_view(), name='list'),
    path('<pk>', TaskItem.as_view(), name='item')
]