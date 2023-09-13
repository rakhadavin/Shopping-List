from django.urls import path
from . import views
from main.views import show_main, create_product,  show_json, show_xml_by_id, show_json_by_id 

app_name = "main"
urlpatterns = [
    path('',views.show_main,name="show_main"),
    path('create-product',views.create_product,name="create_product"),
path('json/', show_json, name='show_json'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
