from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('admin_login/',views.admin_login, name = 'admin_login'),
    path('signup/', views.signup, name = 'signup'),
    path('login/',views.login, name = 'login'),
    path('home/',views.home, name = 'home'),
    path('logout/',views.logout, name = 'logout'),
    path('upload/',views.upload, name = 'upload'),
    path('profile/',views.profile, name = 'profile'),
    path('bio/',views.bio, name = "bio"),
    path('userprofile/<int:user_id>',views.userprofile, name = "userprofile"),
    path('upload_photo/',views.upload_photo, name = "upload_photo"),
    path('edit/<int:id>',views.edit,name = 'edit'),
    path('delete/<int:id>',views.delete, name = 'delete'),
    path('update/',views.update,name = 'update'),
    path('follow_user/',views.follow_user,name = 'follow_user'),
    path('search/',views.search, name ="search"),
    path('follower/',views.followers,name = "followers"),
    path('notification/',views.notification,name = "notification"),
    path('following/',views.following,name = "following")
]