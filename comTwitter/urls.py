
# from msilib.schema import ListView
from django.views.generic import ListView
from django.urls import path
from django.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('login_user/', views.login_user, name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register_user/', views.register_user, name='register'),
    path('landing/', views.landing, name='landing'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('posts/',views.Category, name='category'),
    path('new/post/', views.postListView.as_view(), name='new_post'),
    path('business/new/', views.business, name='business'),
    path('business/', views.businessshow, name='businessshow'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
