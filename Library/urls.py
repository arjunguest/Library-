from django.urls import path
from Library import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'Library'
urlpatterns = [
        path('login/',views.Login,name='login'),   
        path('',views.dashboard.as_view(),name='dashboard'),
        path('event_details/<int:pk>',views.BookDetails.as_view(),name='eventdetails'),
        path('logout/',views.Logout,name='logout'),
    ]