from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.AddPostCreateView.as_view(),name="addCourse"),
    path('teacher/',views.TeacherDashBoardView.as_view(),name='teacher'),
    path('edit/<int:id>/',views.UpdatePost.as_view(), name='edit'),
    path('delete/<int:id>/',views.DeleteViewed.as_view(), name='delete'),
    path('details/<int:id>/',views.DetailsPost.as_view(),name="details_view"),
    path('enroll/<int:id>/', views.EnrolledCourseView.as_view(), name='enrolled'),
    path('student/',views.StudentView.as_view(),name='student')
]
