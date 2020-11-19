from rest_framework import serializers


from .models import Group, Request, Meme


class CreateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
