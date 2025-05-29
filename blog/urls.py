from django.urls import path
from . import views

app_name = 'blog'  # para espacios de nombres de URL

urlpatterns = [
    # Aquí defines las rutas URL de tu aplicación
    path('', views.starting_page, name='starting-page'), # Ruta raíz
    path('posts/', views.posts, name='posts-page'), # Ruta para listar posts
    path('posts/<slug:slug>/', views.post_detail, name='post-detail'), # Ruta para detalles de un post específico
    path('autors/', views.autors, name='autors'), # Ruta para listar autors
    path('autors/<slug:slug>/', views.autors_detail, name='autors-detail'), # Ruta para detalles de un autor específico
    path('tags/', views.tags_page, name='tags-page'), # Ruta para todos los tags
    path('tags/<slug:slug>/', views.tag_detail, name='tag-detail'),
]
