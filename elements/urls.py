from django.urls import path
from elements import views 

urlpatterns = [
    path('import', views.import_element),
    path('detail/<element_name>', views.detail),
    path('detail/<element_name>/<int:element_id>', views.detail),
    path('reset/', views.reset_db)
]
