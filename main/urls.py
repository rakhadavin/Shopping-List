from django.urls import path
from . import views
from main.views import show_main, create_product,  show_json, show_xml_by_id, show_json_by_id 
from django.contrib.auth import logout
app_name = "main"
urlpatterns = [
    path('',views.show_main,name="show_main"),
    path('create-product',views.create_product,name="create_product"),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit-product/<int:id>', views.edit_product, name='edit_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
    
    
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
