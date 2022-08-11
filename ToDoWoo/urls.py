from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #Todos
    path('create/', views.createTodo, name='createTodo'),
    path('current/', views.current, name='current'),
    path('completed/', views.completedTodo, name='completedTodo'),
    path('todo/<int:todo_pk>', views.viewTodo, name='viewTodo'),
    path('todo/<int:todo_pk>/complete', views.completeTodo, name='completeTodo'),
    path('todo/<int:todo_pk>/delete', views.deleteTodo, name='deleteTodo'),
    
]
