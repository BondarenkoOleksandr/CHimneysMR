from rest_framework import serializers

from locations.models import State, City, FSCity, SSCity, TSCity, FSState, SSState, TSState


class FirstScreenStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FSState
        fields = '__all__'


class SecondScreenStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSState
        fields = '__all__'


class ThirdScreenStateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image.image', allow_null=True)

    class Meta:
        model = TSState
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class StateDetailSerializer(serializers.ModelSerializer):
    fsstate = FirstScreenStateSerializer()
    ssstate = SecondScreenStateSerializer()
    tsstate = ThirdScreenStateSerializer()

    class Meta:
        model = State
        fields = '__all__'


class FirstScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FSCity
        fields = '__all__'


class SecondScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCity
        fields = '__all__'


class ThirdScreenSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image.image', allow_null=True)

    class Meta:
        model = TSCity
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    fscity = FirstScreenSerializer()
    sscity = SecondScreenSerializer()
    tscity = ThirdScreenSerializer()

    class Meta:
        model = City
        fields = '__all__'

