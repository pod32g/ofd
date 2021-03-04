from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from .models import OFDStatus
import json
import pytz

# Create your views here.


@csrf_exempt
def getStatus(request):

    tz = pytz.timezone('America/Mexico_City')

    if request.method != "GET":
        return JsonResponse({"Error": "Method not allowed"}, status=405)

    last_updates = OFDStatus.objects.all().order_by('-id')[:2]

    old = last_updates[1]
    new = last_updates[0]

    payload = {
        "last_updated": new.timestamp.astimezone(tz).strftime("%Y-%m-%d at %I:%M:%S %p"),
        "old": {
            "timestamp": old.timestamp.astimezone(tz).strftime("%Y-%m-%d at %I:%M:%S %p"),
            "size": old.size
        },
        "new": {
            "timestamp": new.timestamp.astimezone(tz).strftime("%Y-%m-%d at %I:%M:%S %p"),
            "size": new.size
        },
        "difference": int(new.size)-int(old.size)
    }

    return JsonResponse(payload, status=200)


@csrf_exempt
def setStatus(request):
    if request.method != 'POST':
        return JsonResponse({"Error": "Method not allowed"}, status=405)

    data = json.loads(request.body)

    status = OFDStatus(size=data['size'])
    status.save()

    payload = {
        "status": "Created",
        "object": {
            "id": status.id,
            "size": status.size,
            "timestamp": str(status.timestamp.strftime("%Y-%m-%d %H:%M:%S"))
        }
    }

    return JsonResponse(payload, status=200)
