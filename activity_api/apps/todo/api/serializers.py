from rest_framework.serializers import ModelSerializer
from apps.todo.models import Activity


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
