from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from contact.models import Contact
from contact.seralizer import ContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from utils.pagination import mypagination


class ContactViewSet(ModelViewSet):
    """
    A ViewSet for managing Contact model.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = mypagination
    permission_classes = [IsAuthenticated]  # Optional, uncomment to restrict access
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["name", "email", "phone", "message"]
    ordering_fields = ["name", "created_at"]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # Perform a hard delete
        return Response(
            {"success": True, "message": "Contact deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        no_pagination = request.query_params.get("no_pagination", "").lower() == "true"
        
        if no_pagination:
            serializer = self.serializer_class(queryset, many=True)
            return Response({"success": True, "data": serializer.data})
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response({"success": True, "data": serializer.data})

        serializer = self.serializer_class(queryset, many=True)
        return Response({"success": True, "data": serializer.data})
