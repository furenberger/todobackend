from django.conf.urls import include, url
from todo import views
from rest_framework.routers import DefaultRouter

#create a router and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

#API urls are now automaitcally determined by the router
urlpatterns = [
	url(r'^', include(router.urls))
]