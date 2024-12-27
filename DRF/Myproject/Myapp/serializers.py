from rest_framework import serializers
from .models import Person, Color 

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = ['color_name','id']
        
class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name','age']
        # depth = 1
    
    def get_color_info(self,obj):
        # return "India"
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name': color_obj.color_name,'hex_code': '#000'}
        
    def validate(self, data):
        
        special_characters = "!@#$%^&*()-=+?/<>,_."
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name cannot contain special characters')
        
        if data['age'] < 17:
            raise serializers.ValidationError('age should be greater than 17')
        
        return data    