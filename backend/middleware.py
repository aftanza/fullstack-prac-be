from django.conf import settings
from django.http import JsonResponse
from rest_framework import status

from dotenv import load_dotenv
import os

load_dotenv()

env_api_key = str(os.getenv("API_KEY"))


class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for API key in the request headers
        api_key = request.headers.get("X-API-Key")
        if api_key != env_api_key:
            print("Yoo got error in api key")
            testRes = JsonResponse(
                {"error": "Unauthorized access"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
            print(testRes)
            return testRes

        response = self.get_response(request)
        return response
