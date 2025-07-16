from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        # Logic to retrieve users
        return Response({"message": "Users retrieved successfully"}, status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self, request):
        # Logic to retrieve teams
        return Response({"message": "Teams retrieved successfully"}, status=status.HTTP_200_OK)

class ActivityView(APIView):
    def get(self, request):
        # Logic to retrieve activities
        return Response({"message": "Activities retrieved successfully"}, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    def get(self, request):
        # Logic to retrieve leaderboard
        return Response({"message": "Leaderboard retrieved successfully"}, status=status.HTTP_200_OK)

class WorkoutView(APIView):
    def get(self, request):
        # Logic to retrieve workouts
        return Response({"message": "Workouts retrieved successfully"}, status=status.HTTP_200_OK)
