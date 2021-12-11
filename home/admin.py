from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'number', 'email']
    search_fields = ['firstname', 'lastname', 'number', 'email']
admin.site.register(Customer, CustomerAdmin)


admin.site.register(Product)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['track_number', 'buyer', 'product', 'status']
    search_fields = ['track_number']


admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon)
admin.site.register(Discount)


class Setting_AIAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_title', 'course_description', 'left_button', 'right_button', 'course_feature_title1', 'course_feature_description1',
                    'course_feature_title2', 'course_feature_description2', 'course_feature_title3', 'course_feature_description3',
                    'course_feature_title4', 'course_feature_description4', 'david_video_title', 'david_video_description1', 'david_video_description2',
                    'skills_title', 'skills_title1', 'skill_description1', 'skill_description1_1', 'skills_title2', 'skill_description2', 'skill_description2_2','skills_title3',
                    'skill_description3', 'skill_description3_3', 'skills_title4', 'skill_description4', 'skill_description4_4', 'course_topic', 'course_skill_topic',
                    'teacher_name', 'teacher_description', 'suitable_for_title', 'suitable_for_title1', 'suitable_for_title2',
                    'suitable_for_title3', 'suitable_for_title4', 'title_of_document', 'david_video_title_under_register',
                    'david_video_description_under_register', 'who_are_we_title', 'who_are_we_description1', 'who_are_we_description2',
                    'right_course_title', 'right_course_description', 'right_course_price', 'left_course_title', 'left_course_description',
                    'left_course_price']
    list_editable = ['course_title', 'course_description', 'left_button', 'right_button', 'course_feature_title1', 'course_feature_description1',
                    'course_feature_title2', 'course_feature_description2', 'course_feature_title3', 'course_feature_description3',
                    'course_feature_title4', 'course_feature_description4', 'david_video_title', 'david_video_description1', 'david_video_description2',
                    'skills_title', 'skills_title1', 'skill_description1', 'skill_description1_1', 'skills_title2', 'skill_description2', 'skill_description2_2','skills_title3',
                    'skill_description3', 'skill_description3_3', 'skills_title4', 'skill_description4', 'skill_description4_4', 'course_topic', 'course_skill_topic',
                    'teacher_name', 'teacher_description', 'suitable_for_title', 'suitable_for_title1', 'suitable_for_title2',
                    'suitable_for_title3', 'suitable_for_title4', 'title_of_document', 'david_video_title_under_register',
                    'david_video_description_under_register', 'who_are_we_title', 'who_are_we_description1', 'who_are_we_description2',
                    'right_course_title', 'right_course_description', 'right_course_price', 'left_course_title', 'left_course_description',
                    'left_course_price']


admin.site.register(Setting_AI, Setting_AIAdmin)




class Setting_AndroidAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_title', 'course_description', 'left_button', 'right_button', 'course_feature_title1',
                    'course_feature_description1',
                    'course_feature_title2', 'course_feature_description2', 'course_feature_title3',
                    'course_feature_description3',
                    'course_feature_title4', 'course_feature_description4', 'david_video_title',
                    'david_video_description1', 'david_video_description2',
                    'skills_title', 'skills_title1', 'skill_description1', 'skill_description1_1', 'skills_title2',
                    'skill_description2', 'skill_description2_2', 'skills_title3',
                    'skill_description3', 'skill_description3_3', 'skills_title4', 'skill_description4',
                    'skill_description4_4', 'course_topic', 'course_skill_topic',
                    'teacher_name', 'teacher_description', 'suitable_for_title', 'suitable_for_title1',
                    'suitable_for_title2',
                    'suitable_for_title3', 'suitable_for_title4', 'title_of_document',
                    'david_video_title_under_register',
                    'david_video_description_under_register', 'who_are_we_title', 'who_are_we_description1',
                    'who_are_we_description2',
                    'right_course_title', 'right_course_description', 'right_course_price', 'left_course_title',
                    'left_course_description',
                    'left_course_price']
    list_editable = ['course_title', 'course_description', 'left_button', 'right_button', 'course_feature_title1',
                     'course_feature_description1',
                     'course_feature_title2', 'course_feature_description2', 'course_feature_title3',
                     'course_feature_description3',
                     'course_feature_title4', 'course_feature_description4', 'david_video_title',
                     'david_video_description1', 'david_video_description2',
                     'skills_title', 'skills_title1', 'skill_description1', 'skill_description1_1', 'skills_title2',
                     'skill_description2', 'skill_description2_2', 'skills_title3',
                     'skill_description3', 'skill_description3_3', 'skills_title4', 'skill_description4',
                     'skill_description4_4', 'course_topic', 'course_skill_topic',
                     'teacher_name', 'teacher_description', 'suitable_for_title', 'suitable_for_title1',
                     'suitable_for_title2',
                     'suitable_for_title3', 'suitable_for_title4', 'title_of_document',
                     'david_video_title_under_register',
                     'david_video_description_under_register', 'who_are_we_title', 'who_are_we_description1',
                     'who_are_we_description2',
                     'right_course_title', 'right_course_description', 'right_course_price', 'left_course_title',
                     'left_course_description',
                     'left_course_price']



admin.site.register(Setting_Android, Setting_AndroidAdmin)


class Setting_WebAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_title', 'course_description', 'left_button', 'right_button', 'course_feature_title1',
                    'course_feature_description1',
                    'course_feature_title2', 'course_feature_description2', 'course_feature_title3',
                    'course_feature_description3',
                    'course_feature_title4', 'course_feature_description4', 'david_video_title',
                    'david_video_description1', 'david_video_description2',
                    'skills_title', 'skills_title1', 'skill_description1', 'skill_description1_1', 'skills_title2',
                    'skill_description2', 'skill_description2_2', 'skills_title3',
                    'skill_description3', 'skill_description3_3', 'skills_title4', 'skill_description4',
                    'skill_description4_4', 'course_topic', 'course_skill_topic',
                    'teacher_name', 'teacher_description', 'suitable_for_title', 'suitable_for_title1',
                    'suitable_for_title2',
                    'suitable_for_title3', 'suitable_for_title4', 'title_of_document',
                    'david_video_title_under_register',
                    'david_video_description_under_register', 'who_are_we_title', 'who_are_we_description1',
                    'who_are_we_description2',
                    'right_course_title', 'right_course_description', 'right_course_price', 'left_course_title',
                    'left_course_description',
                    'left_course_price']
    list_editable = ['course_title', 'course_description', 'left_button', 'right_button', 'course_feature_title1',
                     'course_feature_description1',
                     'course_feature_title2', 'course_feature_description2', 'course_feature_title3',
                     'course_feature_description3',
                     'course_feature_title4', 'course_feature_description4', 'david_video_title',
                     'david_video_description1', 'david_video_description2',
                     'skills_title', 'skills_title1', 'skill_description1', 'skill_description1_1', 'skills_title2',
                     'skill_description2', 'skill_description2_2', 'skills_title3',
                     'skill_description3', 'skill_description3_3', 'skills_title4', 'skill_description4',
                     'skill_description4_4', 'course_topic', 'course_skill_topic',
                     'teacher_name', 'teacher_description', 'suitable_for_title', 'suitable_for_title1',
                     'suitable_for_title2',
                     'suitable_for_title3', 'suitable_for_title4', 'title_of_document',
                     'david_video_title_under_register',
                     'david_video_description_under_register', 'who_are_we_title', 'who_are_we_description1',
                     'who_are_we_description2',
                     'right_course_title', 'right_course_description', 'right_course_price', 'left_course_title',
                     'left_course_description',
                     'left_course_price']

admin.site.register(Setting_Web, Setting_WebAdmin)


class Setting_PackAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_title', 'course_description', 'left_button', 'right_button', 'title_of_document', 'david_video_title_under_register',
                    'david_video_description_under_register', 'course_feature_title1', 'course_feature_description1', 'course_feature_title2',
                    'course_feature_description2', 'course_feature_title3', 'course_feature_description3', 'course_feature_title4', 'course_feature_description4',
                    'course_topic', 'course_under_description1', 'course_under_description2', 'course_web_title', 'course_web_description1', 'course_web_description2', 'course_web_description3',
                    'course_web_description4', 'course_android_title', 'course_android_description1', 'course_android_description2', 'course_android_description3',
                    'course_android_description4', 'course_ai_title', 'course_ai_description1', 'course_ai_description2', 'course_ai_description3', 'course_ai_description4',
                    'first_teacher_name', 'first_teacher_description', 'first_teacher_button', 'second_teacher_name', 'second_teacher_description',
                    'second_teacher_button', 'third_teacher_name', 'third_teacher_description', 'third_teacher_button']


admin.site.register(Setting_Pack, Setting_PackAdmin)
