from datetime import datetime
from uuid import UUID

from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer, UserSerializer
from .filters import RoomFilter


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price', 'capacity']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(user=user)

    def perform_create(self, serializer):
        room_id = self.kwargs.get('room_id')
        room = Room.objects.get(id=room_id)
        check_in_date = serializer.validated_data['check_in_date']
        check_out_date = serializer.validated_data['check_out_date']

        conflicting_reservations = Reservation.objects.filter(
            room=room,
            check_out__gt=check_in_date,
            check_in__lt=check_out_date
        )

        if conflicting_reservations.exists():
            raise serializers.ValidationError("Room is not available for booking")

        serializer.save(room=room, user=self.request.user)

    @action(detail=True, methods=['delete'])
    def cancel(self, request, reservation_id=None):
        reservation = self.get_object()
        if reservation.user == request.user:
            reservation.delete()
            return Response(
                {'message': 'Reservation canceled successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {'message': 'You do not have permission to cancel this reservation'},
                status=status.HTTP_403_FORBIDDEN
            )


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            request=request, username=username, password=password
        )

        if user is not None:
            login(request, user)
            return Response({'detail': 'Login successful'}, status=200)
        else:
            return Response({'detail': 'Invalid credentials'}, status=401)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful.'}, status=200)


class UserReservationsAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(user=user)
