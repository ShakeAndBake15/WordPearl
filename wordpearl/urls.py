from django.contrib import admin
from django.urls import path
from wordpearl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pearls/', views.pearlList),
    path('pearls/<int:id>', views.getPearlById),
    # path('oysters/', views.oysterList),
    # path('oysters/:id', views.oyster),
    # path('comments/', views.commentList),
    # path('comments/:id', views.comment)
]
