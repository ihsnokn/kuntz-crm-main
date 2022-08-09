

from django.urls import path
from .views import file_list, file_update, file_delete, FileListView,  FileUpdateView, FileDeleteView

from . import views
app_name = "files"

urlpatterns = [
    path('', FileListView.as_view(), name='file-list'),
   # path('<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('<int:id>/', views.FileDetail, name='filedetail'),
    path('<int:pk>/update', FileUpdateView.as_view(), name='file-update'),
    path('<int:pk>/delete', FileDeleteView.as_view(), name='file-delete'),
    path('create/', views.FileCreateView, name='File_create'),
    path('sign_out/', views.sign_out, name='sign_out'),
    #path('create/', FileCreateView.as_view(), name='file-create'),
]
