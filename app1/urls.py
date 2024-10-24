
from django.urls import path,include

from . import views
from .views import page_not_found

urlpatterns = [

    # path('', views.index, name='index'),
     path('', views.IndexHome.as_view(), name='index'),
    path('about/', views.about, name='about'),
    # path('addpage/', views.addpage, name='add_page'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    # path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('category/<slug:cat_slug>/', views.PostCategory.as_view(), name='category'),
    # path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
]


