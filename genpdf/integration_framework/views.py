from django.http import JsonResponse
from rest_framework.decorators import api_view
import simplejson as json


@api_view(["POST","GET"])
def result(request):
    data = json.loads(request.body)
    print(data)
    token = request.META.get("HTTP_AUTHORIZATION")
    print(token)
    token = token.replace("Bearer ", "")
    try:
        return JsonResponse({"ok": False})
    except:
      return JsonResponse({"ok": True})