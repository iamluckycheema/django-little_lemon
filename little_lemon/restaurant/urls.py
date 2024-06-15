from django.urls import path, re_path 
from . import views
app_name='restaurant'
urlpatterns =[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    re_path('book/',views.book, name='book'),
    path('menu_item/<int:pk>', views.display_menu_items, name="menu_item"),
]