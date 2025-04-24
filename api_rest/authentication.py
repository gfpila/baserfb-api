from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import os
from dotenv import load_dotenv
load_dotenv()

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        expected_key = os.getenv('API_KEY')
        
        if not api_key or api_key != expected_key:
            raise AuthenticationFailed('Invalid or missing API key')

        return (None, None)