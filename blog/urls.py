from django.urls import path
from blog.views import blog, BlogCreateView

urlpatterns = [
    path('blog/', blog, name = 'blog'),
    path('blog-create/', BlogCreateView.as_view(), name = 'blog-create')
]