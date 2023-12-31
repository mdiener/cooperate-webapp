"""
URL configuration for cooperate project.

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
  1. Import the include() function: from django.urls import include, path
  2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path
from user import views as user_views
from ads import views as ads_views

urlpatterns = [
  path("", user_views.login, name="index"),
  path("admin/", admin.site.urls),
  path("signup/", user_views.signup, name="signup"),
  path("login/", user_views.login, name="login"),
  path("logout/", user_views.logout, name="logout"),
  path("ads/", ads_views.index, name="ads"),
  path("ads/manage/", ads_views.manage, name="manage_ads"),
  path("ads/manage_ad_type/", ads_views.manage_ad_type, name="manage_ads_ad_type"),
  path("ads/manage_actual_spend/", ads_views.manage_actual_spend, name="manage_ads_actual_spend")
]
