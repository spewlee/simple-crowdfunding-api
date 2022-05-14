from rest_framework import serializers
from .models import Project, Pledge, Comment

# TRY SIMPLIFY THIS IN THE FUTURE BY USING serializers.ModelSerializer

# Pledge Serializer
class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=None)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


# Comment Serializer
class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project = serializers.ReadOnlyField(source='project.id')
    author = serializers.ReadOnlyField(source='author.id')
    date = serializers.DateField()
    body = serializers.CharField(max_length=None)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class CommentDetailSerializer(CommentSerializer):

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

# Project Serializer
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal_amount = serializers.IntegerField()
    amount_raised = serializers.IntegerField()
    image = serializers.URLField()
    date_created = serializers.DateField()
    date_due = serializers.DateField()
    owner = serializers.ReadOnlyField(source='owner.id')
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)



class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
          instance.title = validated_data.get('title', instance.title)
          instance.description = validated_data.get('description', instance.description)
          instance.goal_amount = validated_data.get('goal_amount', instance.goal_amount)
          instance.amount_raised = validated_data.get('amount_raised', instance.amount_raised)
          instance.image = validated_data.get('image', instance.image)
          instance.date_due = validated_data.get('date_due', instance.date_due)
          instance.save()
          return instance

