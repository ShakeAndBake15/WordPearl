from django.contrib import admin
from django.urls import path
from wordpearl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pearls/', views.pearlList),
    path('pearls/<int:id>', views.getPearlById),
    path('oysters/', views.oystersList),
    path('oysters/<int:id>', views.oysterList),
    path('comments/', views.commentList),
    path('comments/<int:id>', views.comment),
]
