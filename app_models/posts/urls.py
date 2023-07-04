from django.urls import path
from . import views
urlpatterns = [
    path('addpost/',views.addpost,name='addpost'),
    path('post/',views.posts,name='post'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>/',views.delete_post, name='delete_post'),
    path('post/<int:post_id>/comment/add/',views.add_comment, name='add_comment'),
    # path('post/<int:post_id>/toggle-like/', views.toggle_like, name='toggle_like'),
]