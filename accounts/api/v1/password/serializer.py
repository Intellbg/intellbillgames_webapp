from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):

    password1 = serializers.CharField(
        min_length=8,
        error_messages={"min_length": "Password must be longer than 8 characters"},
    )
    password2 = serializers.CharField()

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data
