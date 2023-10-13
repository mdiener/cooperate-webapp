from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
import pandas
from operator import itemgetter
from .models import Ad, AdType
from .forms import AdTypeForm, AdForm


def combine_ads() -> pandas.DataFrame:
  ads = Ad.objects.all()
  data = []
  for ad in ads:
    data.append(ad.to_dict())
  df_ads = pandas.DataFrame(data)

  return df_ads.groupby(["ad_type", "date"]).agg({"id": ["count"], "actual_spend": ["sum"], "cost_share": [lambda cs: cs.tolist()[0]], "reimbursement": ["sum"]})


@login_required(login_url="/")
def index(request):
  df = combine_ads()
  data = []
  for row in df.iterrows():
    data.append({
      "date": row[1].name[1].strftime("%m-%d-%Y"),
      "count": row[1]["id"]["count"],
      "actual_spend": "${0:.2f}".format(row[1]["actual_spend"]["sum"]),
      "cost_share": "${0:.2f}".format(row[1]["cost_share"]["<lambda>"]),
      "ad_type": row[1].name[0],
      "reimbursement": "${0:.2f}".format(row[1]["reimbursement"]["sum"])
    })

  return render(request, "ads/index.html", { "ads": sorted(data, key=itemgetter("date"), reverse=True) })


@login_required(login_url="/")
@user_passes_test(lambda user: user.has_perms(["ads.change_ad", "ads.view_ad", "ads.delete_ad", "ads.add_ad"]), login_url="/", redirect_field_name="/ads/")
def manage(request):
  if request.method == "GET":
    return render(request, "ads/manage.html", { "form": AdTypeForm() })


@login_required(login_url="/")
@user_passes_test(lambda user: user.has_perms(["ads.change_ad", "ads.view_ad", "ads.delete_ad", "ads.add_ad"]), login_url="/", redirect_field_name="/ads/")
def manage_ad_type(request):
  if request.method == "POST":
    form = AdTypeForm(request.POST)

    if form.is_valid():
      ad_type = AdType.objects.all().filter(id=form.cleaned_data["ad_type"]).first()

      ad_form = AdForm()
      if ad_type is not None:
        ad_form.fields["ad_type"].initial = ad_type.id

      if ad_type.limit_min is not None and ad_type.limit_max is not None:
        ad_form.fields["actual_spend"].min_value = ad_type.limit_min
        ad_form.fields["actual_spend"].max_value = ad_type.limit_max
        ad_form.fields["actual_spend"].widget = forms.NumberInput(attrs={ "min": ad_type.limit_min, "max": ad_type.limit_max })

        if ad_type.limit_min == ad_type.limit_max:
          ad_form.fields["actual_spend"].initial = ad_type.limit_max
          ad_form.fields["actual_spend"].widget = forms.NumberInput(attrs={ "readonly": True })

    return render(request, "ads/manage_actual_spend.html", { "form": ad_form, "min": ad_type.limit_min, "max": ad_type.limit_max })


@login_required(login_url="/")
@user_passes_test(lambda user: user.has_perms(["ads.change_ad", "ads.view_ad", "ads.delete_ad", "ads.add_ad"]), login_url="/", redirect_field_name="/ads/")
def manage_actual_spend(request):
  if request.method == "POST":
    form = AdForm(request.POST)
    if form.is_valid():
      ad_type = AdType.objects.all().filter(id=form.cleaned_data["ad_type"]).first()
      ad = Ad(
        date=form.cleaned_data["date"],
        actual_spend=form.cleaned_data["actual_spend"],
        ad_type=ad_type
      )
      ad.save()

      return HttpResponseRedirect("/ads")

    return render(request, "ads/manage_actual_spend.html", { "form": form, "min": 0, "max": 0 })
