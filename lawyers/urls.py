import imp
from django.urls import path
from .views import LawyerListView, LawyerCreateView, LawyerDetailView, LawyerUpdateView, LawyerDeleteView

app_name='lawyers'

urlpatterns = [

    path('', LawyerListView.as_view(), name='lawyer-list'),
    path('<int:pk>/', LawyerDetailView.as_view(), name='lawyer-detail'),
    path('<int:pk>/update', LawyerUpdateView.as_view(), name='lawyer-update'),
    path('<int:pk>/delete', LawyerDeleteView.as_view(), name='lawyer-delete'),
    path('create/', LawyerCreateView.as_view(), name='lawyer-create'),
    

    #5:14:36


]