from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
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