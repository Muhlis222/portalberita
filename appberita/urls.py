from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, CategoryList, CategoryDetail, CommentList, CommentDetail,  UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('post/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
]