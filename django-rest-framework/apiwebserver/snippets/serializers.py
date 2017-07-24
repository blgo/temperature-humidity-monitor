from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('created','id','humidity','temperature')
    #id = serializers.IntegerField(read_only=True)
    #created = serializers.DateTimeField(required=False)
    #temperature = serializers.CharField(required=True, allow_blank=False, max_length=10)
    #humidity = serializers.CharField(required=True, allow_blank=False, max_length=10)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.created)
        instance.temperature = validated_data.get('temperature', instance.humidity)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.save()
        return instance
