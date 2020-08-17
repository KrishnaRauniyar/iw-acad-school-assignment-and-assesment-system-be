from django.urls import path
from .views import ClassCreateApiView, ClassListApiView, ClassUpdateview, ClassDeleteAPIView, ClassRetrieveView
from .views import StudyCreateApiView, StudyListApiView, StudyUpdateview, StudyDeleteAPIView, StudyRetrieveView
urlpatterns = [
    path('studymaterial_class_create/', ClassCreateApiView.as_view()),
    path('studymaterial_class_list/', ClassListApiView.as_view()),
    path('studymaterial_class_delete/<pk>/', ClassDeleteAPIView.as_view()),
    path('studymaterial_class_update/<int:pk>/', ClassUpdateview.as_view()),
    path('studymaterial_class_retrieve/<int:pk>/', ClassRetrieveView.as_view()),
    #### url for studymaterial
    path('studymaterial_material_create/', StudyCreateApiView.as_view()),
    path('studymaterial_material_list/<pk>', StudyListApiView.as_view()),
    path('studymaterial_material_delete/<pk>/', StudyDeleteAPIView.as_view()),
    path('studymaterial_material_update/<int:pk>/', StudyUpdateview.as_view()),
    path('studymaterial_material_retrieve/<int:pk>/', StudyRetrieveView.as_view()),
]