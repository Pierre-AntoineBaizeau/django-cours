from django.urls import path, include
from django.contrib import admin

appname = 'app'
urlpatterns = [
    path('app/',include('app.urls')),
    path('admin/', admin.site.urls)
    # path('<int:question_id>/', views.detail, name='detail')
]