from django.contrib import admin
from .models import *


# Set homepage from admin login 
admin.site.site_url = "/templates/homepage.html"

# Dispaly custom heading for admin site
admin.site.site_header = 'Student Tracker Application'


# Set Course list shown in admin page
class CourseAdmin(admin.ModelAdmin):
    list_display = ("cou_name", "cou_building", "cou_room", "cou_term",)
admin.site.register(Course, CourseAdmin)


# Set Student list shown in admin page
class StudentAdmin(admin.ModelAdmin):
    list_display = ("stu_name", "stu_dob", "stu_email", "stu_phone", "stu_address", "stu_city", "stu_postcode", "stu_course", "stu_term",)
admin.site.register(Student, StudentAdmin)


# Set Lecturer list shown in admin page
class LecturerAdmin(admin.ModelAdmin):
    list_display = ("lec_name", "lec_dob", "lec_email", "lec_phone", "lec_address", "lec_city", "lec_postcode", "lec_course",)
admin.site.register(Lecturer, LecturerAdmin)





