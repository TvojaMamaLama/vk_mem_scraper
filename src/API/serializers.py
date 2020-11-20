from rest_framework import serializers


from .models import Group, Request, Meme


class CreateGroupSerializer(serializers.ModelSerializer):
    """Serializer for creation group"""

    class Meta:
        model = Group
        exclude = ('subscribers', )


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for show group"""

    class Meta:
        model = Group
        fields = '__all__'
