from django.db import models


class AdType(models.Model):
  name = models.CharField(max_length=200)
  cost_share = models.DecimalField(decimal_places=2, max_digits=3)

  def __str__(self):
    return self.name


class Ad(models.Model):
  date = models.DateField("date published")
  actual_spend = models.DecimalField(decimal_places=2, max_digits=14)
  ad_type = models.ForeignKey(AdType, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.ad_type.name} - {self.date} - {self.actual_spend}"
