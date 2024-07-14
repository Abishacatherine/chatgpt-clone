from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai
import logging

logger = logging.getLogger(__name__)

# Set your API key here
openai.api_key = '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'  # Replace with your actual API key

@csrf_exempt
def chat(request):
    try:
        if request.method == 'POST':
            user_input = request.POST.get('text')
            logger.info(f"Received user input: {user_input}")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use a model that supports chat
                messages=[{"role": "user", "content": user_input}]
            )
            gpt_response = response['choices'][0]['message']['content']
            logger.info(f"GPT response: {gpt_response}")
            return JsonResponse({'response': gpt_response})
        elif request.method == 'GET':
            logger.info("Rendering chat.html")
            return render(request, 'myapp/chat.html')
        else:
            logger.error(f"Invalid request method: {request.method}")
            return JsonResponse({'error': 'Invalid request method'}, status=400)
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        return JsonResponse({'error': str(e)}, status=500)
