from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path("sign",views.sign,name="sign"),
    path("login",views.login,name="login"),
    path("roc",views.roc,name="roc"),
    path("rac",views.rac,name="rac"),
    path("rmc",views.rmc,name="rmc"),
    path("userview",views.userview,name="userview"),
    path("secindex",views.secindex,name="secindex"),
    path("viewstatus",views.viewstatus,name="viewstatus"),
    path("coplogin",views.coplogin,name="coplogin"),
    path("copview",views.copview,name="copview"),
    path("sendmail",views.sendmail,name="sendmail"),
    path("vmp",views.vmp,name="vmp"), 
    path("vca",views.vca,name="vca"),
    path("index",views.index,name="index")

    
    #path("viewvmp",views.viewvmp,name="viewvmp"),
   # path("viewvca",views.viewvca,name="viewvca")
    

]
urlpatterns =urlpatterns + static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 