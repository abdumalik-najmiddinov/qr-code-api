from django.urls import path

from app.views import QRCodeView

urlpatterns = [
    path("qr/", QRCodeView.as_view()),

]
