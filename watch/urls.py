from django.urls import path
from watch.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='home'),
    path('viewproduct',view_product,name='viewproduct'),
    path('view_watch/<int:id>/',view_watches,name='view_watches'),
    path('signinuser',signinuser,name='signin'),
    path('loginuser',loginuser,name='login')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
