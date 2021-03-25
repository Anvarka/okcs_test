from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def webhook(request):
    request_message = json.loads(request.body)

    text = ''

    if request_message['session']['new']:
        text = 'Привет новичек'
    else:
        text = request_message['request']['original_utterance']

    derived_session_fields = ['session_id', 'user_id', 'message_id']
    response_message = {
        "response": {
            "text": text,
            "tts": text,
            "end_session": False
        },
        "session": {derived_key: request_message['session'][derived_key] for derived_key in derived_session_fields},
        "version": request_message['version']
    }

    return JsonResponse(response_message, safe=False)
