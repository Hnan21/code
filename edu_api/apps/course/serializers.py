from rest_framework.serializers import ModelSerializer

from course.models import CourseCategory, Course, Teacher, CourseChapter


# 课程分类序列化
class CourseCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ("id", "name")


# 教师表序列化
class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "name", "title", "signature", "image")


class CourseModelSerializer(ModelSerializer):
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ("id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher", "lesson_list",
                  "discount_name", "discount_price")


class CourseChapterModelSerializer(ModelSerializer):
    class Meta:
        model = CourseChapter
        fields = ("id", "name", "chapter", "summary", "lesson_list")


class CourseToModelSerializer(ModelSerializer):
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ("id", "name", "course_img", "students", "lessons", "level_name", "pub_lessons", "price", "teacher",
                  "lesson_list", "brief_html",
                  "discount_name", "discount_price", "active_time")
