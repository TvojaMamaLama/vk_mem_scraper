from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .services import save_group_info, get_group, get_list_group
from .models import Group, Request


class GroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Get group info from vk and save it"""
        status_code, data = save_group_info(request)
        return Response(status=status_code, data=data)

    def get(self, request):
        status_code, data = get_list_group(request)
        return Response(status=status_code, data=data)

class GetGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, screen_name):
        status_code, data = get_group(screen_name)
        return Response(status=status_code, data=data)


class RequestMemeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Make request for best, worst meme"""

