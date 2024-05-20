import requests
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from decouple import config


# Create your views here.
class SessionViewSet(viewsets.ViewSet):
    VERBEUX_API_URL = "https://generative-api.verbeux.com.br"
    VERBEUX_ASSISTANT_ID = 52

    def create(self, request):
        resource_url = f"{self.VERBEUX_API_URL}/session"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api-key": f"{config('API_PRIVATE_KEY')}",
        }
        body = {
            "assistant_id": self.VERBEUX_ASSISTANT_ID,
        }
        resp = requests.post(resource_url, headers=headers, json=body)
        if resp.status_code == status.HTTP_201_CREATED:
            return Response(resp.json(), status=status.HTTP_201_CREATED)
        else:
            return Response(resp.json(), status=resp.status_code)
        
    def update(self, request, pk=None):
        resource_url = f"{self.VERBEUX_API_URL}/session/{pk}/"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api-key": f"{config('API_PRIVATE_KEY')}",
        }
        body = request.data
        resp = requests.put(resource_url, headers=headers, json=body)
        if resp.status_code == status.HTTP_200_OK:
            return Response(resp.json(), status=status.HTTP_201_CREATED)
        else:
            return Response(resp.json(), status=resp.status_code)
