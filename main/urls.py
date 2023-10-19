from django.urls import path
from .views import *

urlpatterns = [
    path('create_direction/', create_direction),    #done
    path('get_directions/', get_directions),    #done
    path('change_direction/<int:pk>/', change_direction),   #done   #done
    path('delete_direction/<int:pk>/', delete_direction),   #done

    path('create_student/', create_student),    #done
    path('get_students/<int:pk>/', get_students),   #done
    path('get_student/<int:pk>/', get_student),     #check if student is teacher's student
    path('change_student/<int:pk>/', change_student),

    path('create_group/', create_group),
    path('get_groups/', get_groups),    #done
    path('get_group/<int:pk>/', get_group), #done
    path('change_group/<int:pk>/', change_group),
    path('add_student_to_group/<int:pk>/', add_student_to_group),
    path('remove_student_from_group/<int:pk>/', remove_student_from_group),

    path('create_region/', create_region),  #done
    path('get_regions/', get_regions),  #done
    path('change_region/<int:pk>/', change_region), #done

    path('create_payment/', create_payment),
    path('get_payments/', get_payments),    #done
    path('change_payment/<int:pk>/', change_payment),   #done
    path('get_payment/<int:pk>/', get_payment), #done
    path('get_unpayed_students/', get_unpayed_students),

]