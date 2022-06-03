from django.urls import path
from PAGE_Count_APP import views
urlpatterns = [
    path('count/',views.Page_Count),
    path('details/<int:pk>/', views.Details, name='post_detail'),
    path('set/',views.set_session),
    path('get/',views.get_session),
    path('del/',views.delete_session),
    
]
