
from django.contrib import admin
from django.urls import path
from ucrud.views import user_get,user_post,user_delete,user_edit
from ucrud.views import user,userged
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_get,name='user_get'),
    path('add/',user_post,name='user_post'),
    path('delete/<int:id>/',user_delete,name='user_delete'),
    path('edit/<int:id>/',user_edit,name='user_edit'),
    # DRF
    path('user/',user,name='user'),
    path('user/<int:id>/',userged,name='userged'),
]
