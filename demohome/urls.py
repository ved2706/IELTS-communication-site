from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path("",views.index,name="index"),
   path("payment/",views.payment,name="payment"),
   path("nick/",views.nick,name="nick"),
   path("refrence/",views.refrence,name="refrence"),
   path("uk/",views.uk,name="uk"),
   path("usa/",views.usa,name="usa"),
   path("australia/",views.australia,name="australia"),
   path("login/",views.login,name="login"),
   path("signup/",views.signup,name="signup"),
   path("welcome/",views.welcome,name="welcome"),
   path("back/",views.back,name='back'),
]
