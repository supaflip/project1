from .models import Week, Day, Workout, Profile
from .serializers import WeekSerializer, DaySerializer, WorkoutSerializer, ProfileSerializer
# from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class WeekViewSet(APIView):
    def get(self, request, week_number=None):
        if week_number: 
            data = Week.objects.get(week_number=week_number)
            serializer = WeekSerializer(data)
        else:
            data = Week.objects.all()
            serializer = WeekSerializer(data, many=True)
        return Response({"result": serializer.data})
    
class DayViewSet(APIView):
    def get(self, request, day_number=None):
        if day_number: 
            data = Day.objects.get(day_number=day_number)
            serializer = DaySerializer(data)
        else:
            data = Day.objects.all()
            serializer = DaySerializer(data, many=True)
        return Response({"result": serializer.data})
    
class WorkoutViewSet(APIView):
    def get(self, request, id=None): # id or title?
        if id: 
            data = Workout.objects.get(id=id)
            serializer = DaySerializer(data)
        else:
            data = Workout.objects.all()
            serializer = WorkoutSerializer(data, many=True)
        return Response({"result": serializer.data})
    
class ProfileViewSet(APIView): # requires token authentication, viewable only by admin
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None): # returns list of all users
        usernames = [user.username for user in Profile.objects.all()]
        return Response(usernames)
    
    @api_view(['POST'])
    def create_profile(request, user_id):
        user = get_object_or_404(Profile, pk=user_id)
        profile = Profile(user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def update(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
  

# class WeekViewSet(viewsets.ModelViewSet):
#     queryset = Week.objects.all() 
#     serializer_class = WeekSerializer

# class DayViewSet(viewsets.ModelViewSet):
#     queryset = Day.objects.all() # .prefetch_related('week')
#     serializer_class = DaySerializer

# class WorkoutViewSet(viewsets.ModelViewSet):
#     queryset = Workout.objects.all()
#     serializer_class = WorkoutSerializer

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all().order_by('username)
#     serializer_class = ProfileSerializer
#     filter_fields = ('username', 'weights') 
