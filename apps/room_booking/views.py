from datetime import datetime
from uuid import UUID

from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer, UserSerializer


class RoomListAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('check_in_date')
        end_date = request.query_params.get('check_out_date')
        sort_by = request.query_params.get('sort_by')
        sort_order = request.query_params.get('sort_order')

        rooms = Room.objects.all()

        # Filter rooms based on availability for the specified dates
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            rooms = rooms.exclude(
                reservation__check_in__lt=end_date,
                reservation__check_out__gt=start_date
            )

        # Sort rooms by price or number of seats
        if sort_by == 'price':
            if sort_order == 'asc':
                rooms = rooms.order_by('price')
            else:
                rooms = rooms.order_by('-price')
        elif sort_by == 'capacity':
            if sort_order == 'asc':
                rooms = rooms.order_by('capacity')
            else:
                rooms = rooms.order_by('-capacity')

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookRoomAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id: UUID):
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')

        room = Room.objects.get(id=room_id)

        if not request.user.is_authenticated:
            return Response(
                {'message': 'User must be logged in to book a room'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            check_in_date = datetime.strptime(
                check_in_date, '%Y-%m-%d'
            ).date()
            check_out_date = datetime.strptime(
                check_out_date, '%Y-%m-%d'
            ).date()
        except ValueError:
            return Response(
                {'message': 'Invalid date format. Please provide'
                            'dates in the format YYYY-MM-DD'},
                status=status.HTTP_400_BAD_REQUEST)

        # Check if the room is already booked for the given dates
        conflicting_reservations = Reservation.objects.filter(
            room=room,
            check_out__gt=check_in_date,
            check_in__lt=check_out_date
        )

        if conflicting_reservations.exists():
            return Response(
                {'message': 'Room is not available for booking'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'message': 'Room booked successfully'},
            status=status.HTTP_201_CREATED
        )


class CancelReservationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, reservation_id: UUID):
        try:
            reservation = Reservation.objects.get(
                id=reservation_id, user=request.user
            )
        except Reservation.DoesNotExist:
            return Response(
                {'message': 'Reservation not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        reservation.delete()
        return Response(
            {'message': 'Reservation canceled successfully'},
            status=status.HTTP_204_NO_CONTENT
        )


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user
            user = serializer.save()

            # Authenticate and log in the user
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful.'}, status=200)


class UserReservationsAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(user=user)
