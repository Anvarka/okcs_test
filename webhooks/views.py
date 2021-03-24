from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def webhook(request):
	print(request.body)

	fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.',
					   'body': f'{request.body}'}

	return JsonResponse(fulfillmentText, safe=False)