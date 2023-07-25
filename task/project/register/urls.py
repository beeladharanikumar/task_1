from django.urls import path,include
from register import views
urlpatterns = [
    path('register/',views.display,name = 'register-page'),
    path('login/',views.login_logout,name = 'login-page'),
    # path('home/',views.home,name = 'home-page'),
    path('register_api/',views.register_api.as_view(),name='test-api'),
    path('api-auth/',include('rest_framework.urls')),
    path('login_api/',views.login_api, name = "login-api"),
    path('update/',views.update_pwd.as_view(),name = 'update-password'),
    path('delete_account/',views.remove_api.as_view(),name = 'delete-account'),
    path('profile/',views.profile.as_view(),name="myapi"),
    path('profile_update/',views.update_profile.as_view(),name = 'update-profile'),
    path('test_ser/',views.test_serializer.as_view(),name = 'serializer'),
    path('update_temp/',views.post_data_into_temp,name="post_data"),
    path('add_task/<int:id>/', views.add_task, name='add-task'),
    path("relation/",views.ParentToChildView.as_view(),name= 'relation'),
    path('relation1/',views.childtoparentview.as_view(),name = 'relation1'),
    path('file_upload/',views.upload_file,name = 'file-upload'),
]