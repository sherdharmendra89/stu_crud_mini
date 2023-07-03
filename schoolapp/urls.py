from django.urls import path
from .views import *

urlpatterns = [
    path('', index),

    # Fetch all Student & School List

    path('school-list/', SchoolRetrieveDetails.as_view({'get':'list', 'put':'create'})),
    path('school-list/<int:pk>/', SchoolRetrieveDetails.as_view({'get':'list', 'put':'create', 'get':'retrieve'})),

    path('student-list/', StudentRetrieveDetails.as_view({'get':'list', 'put':'create'})),
    path('student-list/<int:pk>/', StudentRetrieveDetails.as_view({'get':'list', 'put':'create', 'get':'retrieve'})),

    path('sch-list/', sch_list),
    path('stu-list/', stu_list),
    path('add-student/', add_student),
    path('add-school/', add_school),
    path('update-student/<int:pk>/', edit_student),
    path('update-school/<int:pk>/', edit_school),

    path('delete-student/<int:pk>/', delete_student),
    path('delete-school/<int:pk>/', delete_school),

    # new operations

    path('add-data/', add_data, name='add_data'),
    path('all-data/', all_data, name='all_data'),
    path('update-data/<int:id>/', update_data, name='update_data'),
    path('delete-data/<int:id>/', delete_data, name='delete_data'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


]