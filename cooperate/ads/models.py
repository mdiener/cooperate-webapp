from django.db import models
from itertools import chain
from decimal import Decimal


class AdType(models.Model):
  name = models.CharField(max_length=200)
  cost_share = models.DecimalField(decimal_places=2, max_digits=14)
  limit_min = models.DecimalField(decimal_places=2, max_digits=14, default=0)
  limit_max = models.DecimalField(decimal_places=2, max_digits=14, default=0)

  def __str__(self):
    return self.name

  def to_dict(self):
    opts = self._meta
    data = {}

    for f in chain(opts.concrete_fields, opts.private_fields):
      data[f.name] = f.value_from_object(self)

    return data


class Ad(models.Model):
  date = models.DateField("date published")
  actual_spend = models.DecimalField(decimal_places=2, max_digits=14)
  ad_type = models.ForeignKey(AdType, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.ad_type.name} - {self.date} - {self.actual_spend}"

  def to_dict(self):
    opts = self._meta
    data = {}

    for f in chain(opts.concrete_fields, opts.private_fields):
      if f.name != "ad_type":
        data[f.name] = f.value_from_object(self)

    data["ad_type"] = self.ad_type.name
    data["cost_share"] = self.ad_type.cost_share
    data["reimbursement"] = round(Decimal(self.ad_type.cost_share * self.actual_spend), 2)

    return data
