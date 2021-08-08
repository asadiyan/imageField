from rest_framework import serializers

from .models import Spent, Image


class SpentSerializer(serializers.ModelSerializer):
    # we extend this serializer from ModelSerializer so ModelSerializer it self has
    # set of default fields, automatically populated and
    # Default `.create()` and `.update()` implementations are provided
    class Meta:
        # so here in meta class we define our model and fields
        # then the ModelSerializer automatically will do all the things
        model = Spent
        fields = '__all__'


class SpentRetrieveSerializer(serializers.Serializer):
    # because our serializer is extended from normal serializer
    # we should define all fields from method here to
    # and we use SerializerMethodField to define our field
    # spent_amount = serializers.SerializerMethodField("get_spent_amount")
    # in signature we have a method name but in example we dont have
    # there is no need to write it why?
    # because SerializeMethodField automatically search for that name
    # when we use name there?
    # when we want to use another method name instead
    spent_amount = serializers.SerializerMethodField()
    spent_date = serializers.SerializerMethodField()
    spent_description = serializers.SerializerMethodField()

    def get_spent_amount(self, obj):
        return obj.spent_amount

    def get_spent_date(self, obj):
        return obj.spent_date

    def get_spent_description(self, obj):
        # obj is same as object
        # we have passed this object in api.py file when we define serializer
        return obj.spent_description


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    
    def create(self, validated_data):
        return super(ImageSerializer, self).create(validated_data)
