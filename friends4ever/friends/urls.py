from django.conf.urls import url
from friends import views

app_name = 'friends'
urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^slide',views.slide,name='slide')
]
