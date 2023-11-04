from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from apps.todo.api.serializers import ActivitySerializer
from apps.todo.models import Activity


# Create your views here.


class ActivityViewSet(ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all().order_by("-updated_on")
    permission_classes = []
    authentication_classes = []

    @action(
        detail=True,
        methods=["POST"],
        url_path="change-status",
        url_name="Change status of the activity",
    )
    def add_question_to_form(self, request, pk):
        return Response(
            {"message": "Question added successfully"}, status=status.HTTP_201_CREATED
        )
