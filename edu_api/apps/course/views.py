from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course.models import CourseCategory, Course, CourseChapter
from course.serializers import CourseCategoryModelSerializer, CourseModelSerializer, CourseToModelSerializer, \
    CourseChapterModelSerializer
from course.service import CoursePageNumberPagination


class CourseCategoryAPIView(ListAPIView):
    """课程分类查询"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategoryModelSerializer


class CourseAPIView(ListAPIView):
    """课程列表"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer
    # 根据点击的分类的id不同来展示对应课程
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)
    # 排序
    ordering_fields = ("id", "students", "price")
    # 分页的实现
    pagination_class = CoursePageNumberPagination


# 文章
class CourseLessonAPIView(ModelViewSet):
    def chapter(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        cap = CourseChapter.objects.filter(is_show=True, is_delete=False, course=id).order_by('orders').all()
        return Response({
            'message': '查询成功',
            'data': CourseChapterModelSerializer(cap, many=True).data
        }, status=status.HTTP_200_OK)


# 课程
class CourseToAPIView(ModelViewSet):
    def course(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        course = Course.objects.filter(is_delete=False, is_show=True, id=id).order_by('orders').first()
        return Response({
            'message': '查询成功',
            'data': CourseToModelSerializer(course).data
        }, status=status.HTTP_200_OK)
