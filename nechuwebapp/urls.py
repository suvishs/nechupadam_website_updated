from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('nechulogin', views.nechulogin, name='nechulogin'),
    path('nechuadminhome', views.nechuadminhome, name='nechuadminhome'),
    path('treatments', views.treatments, name='treatments'),
    path('images', views.images, name='images'),
    path('youtube', views.youtube, name='youtube'),
    path('bookings', views.bookings, name='bookings'),
    path('reviews', views.reviews, name='reviews'),
    path('singlearticle/<int:pk>/', views.singlearticle, name='singlearticle'),
    path('staffs', views.staffs, name='staffs'),
    path('bg', views.bg, name='bg'),


    path('medicalreports', views.medicalreports, name='medicalreports'),
    path('singletreatment/<int:pk>/', views.singletreatment, name='singletreatment'),
    path('addTreatment', views.addTreatment, name='addTreatment'),
    path('edittreatment/<int:pk>/', views.edittreatment, name='edittreatment'),
    path('delete_treatment/<int:pk>/', views.delete_treatment, name='delete_treatment'),
    path('add_image', views.add_image, name='add_image'),
    path('edit_image/<int:pk>/', views.edit_image, name='edit_image'),
    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('add_youtube_category', views.add_youtube_category, name='add_youtube_category'),
    path('add_youtube', views.add_youtube, name='add_youtube'),
    path('add-image-category/', views.add_image_category, name='add_image_category'),
    path('addStaff/', views.addStaff, name='addStaff'),
    path('edit_staff/<int:pk>/', views.edit_staff, name='edit_staff'),
    path('add_bg/', views.add_bg, name='add_bg'),
    path('edit_bg/<int:pk>/', views.edit_bg, name='edit_bg'),
    path('add_bg2/', views.add_bg2, name='add_bg2'),
    path('add_bg3/', views.add_bg3, name='add_bg3'),
    path('edit_bg2/<int:pk>/', views.edit_bg2, name='edit_bg2'),
    path('edit_bg3/<int:pk>/', views.edit_bg3, name='edit_bg3'),


    path('imagecategory', views.imagecategory, name='imagecategory'),
    path('youtubecategory', views.youtubecategory, name='youtubecategory'),
    path('articles', views.articles, name='articles'),
    path('edit_imagecategory/<int:pk>/', views.edit_imagecategory, name='edit_imagecategory'),
    path('delete_imagecategory/<int:pk>/', views.delete_imagecategory, name='delete_imagecategory'),
    path('edit_youtubecategory/<int:pk>/', views.edit_youtubecategory, name='edit_youtubecategory'),
    path('delete_youtubecategory/<int:pk>/', views.delete_youtubecategory, name='delete_youtubecategory'),
    path('add_article', views.add_article, name='add_article'),
    path('edit_article/<int:pk>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),
    path('add_review', views.add_review, name='add_review'),
    path('edit_review/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:pk>/', views.delete_review, name='delete_review'),
    path('delete_staff/<int:pk>/', views.delete_staff, name='delete_staff'),
    path('delete_bg/<int:pk>/', views.delete_bg, name='delete_bg'),


    path('nechulogin/', views.nechulogin, name="nechulogin"),
    path("SignOut",views.SignOut,name="SignOut"),


    path('nechupadam_treatments', views.nechupadam_treatments, name='nechupadam_treatments'),
    path('more_about_treatment/<int:pk>/', views.more_about_treatment, name='more_about_treatment'),
    path('nechupadam_youtube', views.nechupadam_youtube, name='nechupadam_youtube'),
    path('nechupadam_articles', views.nechupadam_articles, name='nechupadam_articles'),
    path('more_about_article/<int:pk>/', views.more_about_article, name='more_about_article'),
    path('booking', views.booking, name='booking'),
    path('medical_report', views.medical_report, name='medical_report'),
    path('nechupadam_images', views.nechupadam_images, name='nechupadam_images'),
    path('nechupadam_history', views.nechupadam_history, name='nechupadam_history'),
    path('nechupadam_process', views.nechupadam_process, name='nechupadam_process'),
    path('general_info', views.general_info, name='general_info'),
    path('team', views.team, name='team'),
    path('doctor_profile', views.doctor_profile, name='doctor_profile'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('nechupadam_contact', views.nechupadam_contact, name='nechupadam_contact'),
    path('nechupadam_location', views.nechupadam_location, name='nechupadam_location'),




]

