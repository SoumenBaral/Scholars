from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.AddPostCreateView.as_view(),name="addCourse"),
    path('edit/<int:id>/',views.UpdatePost.as_view(), name='edit'),
    path('delete/<int:id>/',views.DeleteViewed.as_view(), name='delete'),
    path('details/<int:id>/',views.DetailsPost.as_view(),name="details_view")
    
]
