from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    #path('', views.home, name='home'),
    #path('post/<int:id>', views.post_number, name='post_page'),
    path('', views.homepage.as_view(), name='home'),
    path('post/<int:pk>', views.post_number.as_view(), name='post_page'),
    path('edit-post', views.edit_post.as_view(), name='edit_post'),
    path('update-post/<int:pk>', views.update_post.as_view(), name='update_post'),
    path('delete-post/<int:pk>', views.delete_post.as_view(), name='delete_post'),
    path('login', views.NewLogin.as_view(), name='login_page'),
    path('register', views.NewRegistration.as_view(), name='register_page'),
    path('logout', views.NewLogout.as_view(), name='logout_page'),
]
