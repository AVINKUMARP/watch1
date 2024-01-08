
from django.urls import path

from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('watch/<int:watch_id>/',views.details,name='details'),
    # path('add/',views.add_watch,name='add_watch'),
    # path('update/<int:id>/',views.update,name="update"),
    # path('delete/<int:id>/',views.delete,name="delete"),
    path('register/',views.register,name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('support/', views.support, name="support"),
    path('mec/', views.mec, name="mec"),
    path('auto/', views.auto, name="auto"),
    path('smt/', views.smt, name="smt"),
    path('qur/', views.qur, name="qur"),
    path('cro/', views.cro, name="cro"),
    path('about/', views.about, name="about"),
]