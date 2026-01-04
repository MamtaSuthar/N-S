from django.contrib import admin
from django.urls import path
from apps.portfolio.views import home,about,service,project,contact,blog,single

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('about', about, name='about'),  
    path('service', service, name='service'),
    path('project', project, name='project'),  
    path('contact', contact, name='contact'),  
    path('blog', blog, name='blog'),
    path('single', single, name='single'),
]
