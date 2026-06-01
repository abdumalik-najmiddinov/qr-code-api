import qrcode
from io import BytesIO
from django.http import HttpResponse
from rest_framework.views import APIView

class QRCodeView(APIView):
    def get(self, request):
        text = request.GET.get("text")
        if not text:
            return HttpResponse("text entry required!", status=400)

        qr = qrcode.make(text)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        return HttpResponse(
            buffer.getvalue(),
            content_type="image/png"
        )