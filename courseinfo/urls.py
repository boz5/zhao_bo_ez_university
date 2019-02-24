from django.urls import path
from courseinfo.views import (
    InstructorList,
    SectionList,
    CourseList,
    SemesterList,
    StudentList,
    RegistrationList,
    InstructorDetail,
    SectionDetail,
    StudentDetail, CourseDetail, SemesterDetail, RegistrationDetail)

urlpatterns = [
    path('instructor/',
          #option+return
          InstructorList.as_view(),
          name='courseinfo_instructor_list_urlpattern'),

    #data type and parameter, note int:pk no spaces
    path('instructor/<int:pk>/',
          InstructorDetail.as_view(),
          name='courseinfo_instructor_detail_urlpattern'),


    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),

    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_detail_urlpattern'),


    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),

    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_detail_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),

    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='courseinfo_semester_detail_urlpattern'),

    path('student/',
         StudentList.as_view(),
         name='courseinfo_student_list_urlpattern'),

    path('student/<int:pk>/',
         StudentDetail.as_view(),
         name='courseinfo_student_detail_urlpattern'),


    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_registration_list_urlpattern'),

    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_detail_urlpattern'),

]