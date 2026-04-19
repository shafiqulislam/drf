from rest_framework import serializers
from .models import Member
import re

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    # Name validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value

    # Email validation (already handled by EmailField, but extra check optional)
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    # Phone validation
    def validate_phone(self, value):
        pattern = r'^\d{10,15}$'  # Only digits, length 10–15
        if not re.match(pattern, value):
            raise serializers.ValidationError("Phone must be 10-15 digits.")
        return value