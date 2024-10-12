from django.urls import path
from . import views
from .views import signup_view
from .views import signup

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('view-appointment/', views.view_appointment, name='view_appointment'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('signup/', signup, name='signup'),
    path('services/facials/', views.facials_services, name='facials_services'),
    path('services/manicure_pedicure/', views.manicure_pedicure_services, name='manicure_pedicure_services'),
    path('services/hairstyling/', views.hairstyling_services, name='hairstyling_services'),
    path('services/makeup/', views.makeup_services, name='makeup_services'),
    path('services/body-treatments/', views.body_treatments_services, name='body_treatments_services'),  # New path for body treatments
    path('services/spa-packages/', views.spa_packages_services, name='spa_packages_services'),
    path('products/moisturizer/', views.moisturizer, name='moisturizer'),
]

