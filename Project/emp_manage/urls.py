
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path("", views.home , name='home'),
   path("addemp/",views.addemp, name='addemp'),
   path("userdata/",views.userdata , name='userdata'),
   path('userdelete/<int:emp_id>', views.delete_user, name='delete_user'),
   path('userupdate/<int:emp_id>',views.updateuser, name='updateuser'),
   path('updation/<int:emp_id>',views.updation, name='updation'),
   path("testimonial/",views.testi, name='testi'),
   path('feedbackform/',views.feedback, name='feedback')
] + static(settings.MEDIA_URL,
                       document_root=settings.MEDIA_ROOT)
