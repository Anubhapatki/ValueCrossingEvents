from rest_framework import serializers
from .crossingEvents import CrossingEvents


class ValueCrossingsSerializer(serializers.Serializer):
    signal = serializers.ListField()
    value = serializers.IntegerField(max_value=10)
    #sum = serializers.IntegerField()


    def update(self, instance, validated_data):
        instance.email = validated_data.get('signal', instance.signal)
        instance.content = validated_data.get('value', instance.content)
        #instance.created = validated_data.get('created', instance.created)
        return instance

    def create(self, validated_data):
        return CrossingEvents(**validated_data)