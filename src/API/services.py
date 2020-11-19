from rest_framework import status

from .vk_services import get_group_info, get_best_worst_meme
from .models import Group, Request, Meme
from .serializers import CreateGroupSerializer


def save_group_info(request, token) -> (int, dict):
    """Save group information into db"""
    group = get_group_info(link=request['link'], token=token)
    if 'error' in group:
        return status.HTTP_400_BAD_REQUEST, {'error': group['error']['error_msg']}
    serializer = CreateGroupSerializer(group)
    serializer.is_valid(raise_exception=ValueError)
    serializer.save()
    return status.HTTP_201_CREATED, serializer.data

