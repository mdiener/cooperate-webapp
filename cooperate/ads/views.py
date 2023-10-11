from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Ad


def combine_ads(ads):
  combined = {}

  for ad in ads:
    combined[ads.date]


@login_required(login_url='/')
def index(request):
  ads = Ad.objects.all()
  ads0011 = list(ads.filter(ad_type__name="0011"))
  ads1011 = ads.filter(ad_type__name="1011")
  ads1111 = ads.filter(ad_type__name="1111")
  ads1010 = ads.filter(ad_type__name="1010")

  print(ads0011)

  return render(request, "ads/index.html")
