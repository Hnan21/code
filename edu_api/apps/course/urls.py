from django.urls import path

from course import views

urlpatterns = [
    path("category/", views.CourseCategoryAPIView.as_view()),
    path("courses/", views.CourseAPIView.as_view()),
    path('chapter/',views.CourseLessonAPIView.as_view({'get':'chapter'})),
    path('cours/',views.CourseToAPIView.as_view({'get':'course'})),
]