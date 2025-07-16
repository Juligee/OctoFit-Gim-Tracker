from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.EmailField())

class ActivitySerializer(serializers.Serializer):
    user = serializers.EmailField()
    description = serializers.CharField()
    date = serializers.DateTimeField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.EmailField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    user = serializers.EmailField()
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
