from rest_framework import status

from .vk_services import get_group_info, get_best_worst_meme
from .models import Group, Request, Meme
from .serializers import CreateGroupSerializer, GroupSerializer


def save_group_info(request) -> (int, dict):
    """Checking a group for existence,if not save group information into db"""
    screen_name = request.data['link'].strip().split('/')[-1]
    try:
        Group.objects.get(screen_name=screen_name)
    except Group.DoesNotExist:
        token = request.user.vk_token
        group = get_group_info(group_ids=screen_name, token=token)
        if 'error' in group:
            return status.HTTP_400_BAD_REQUEST, {'error': group['error']['error_msg']}
        serializer = CreateGroupSerializer(data=group)
        serializer.is_valid(raise_exception=ValueError)
        serializer.save()
        return status.HTTP_201_CREATED, serializer.data
    return status.HTTP_200_OK, {'message': 'This group already parsed'}


def get_group(screen_name: str) -> (int, dict):
    """Get group by screen_name"""
    try:
        group = Group.objects.get(screen_name=screen_name)
    except Group.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'message': 'group not found'}
    serializer = GroupSerializer(group)
    return status.HTTP_200_OK, serializer.data


def get_list_group(request):
    groups = Group.objects.filter(subscribers=request.user)
    serializer = GroupSerializer(groups, many=True)
    return status.HTTP_200_OK, serializer.data
