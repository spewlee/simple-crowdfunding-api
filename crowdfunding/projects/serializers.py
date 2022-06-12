from rest_framework import serializers
from .models import Project, Pledge, Comment

# TRY SIMPLIFY THIS IN THE FUTURE BY USING serializers.ModelSerializer

# Pledge Serializer
class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['amount','comment', 'annoymous', 'project', 'supporter']

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['project', 'author', 'date', 'body']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class CommentDetailSerializer(CommentSerializer):

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
       model = Project
       fields= ['title', 'description', 'goal_amount', 'image', 'date_created', 'due_date', 'owner']

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

