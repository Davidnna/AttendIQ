from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def healthz(request):
    return HttpResponse("ok", content_type="text/plain", status=200)


def error_404(request, exception):
    return render(request, "errors/404.html", status=404)


def error_500(request):
    return render(request, "errors/500.html", status=500)
