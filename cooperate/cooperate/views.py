from django.shortcuts import HttpResponseRedirect


def handler404(request, *args, **argv):
  return HttpResponseRedirect("/")


def handler500(request, *args, **argv):
  return HttpResponseRedirect("/")
