
# from msilib.schema import ListView
from django.views.generic import ListView
from django.urls import path
from django.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('accounts/login/',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('', views.postListView.as_view(), name='landing'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
