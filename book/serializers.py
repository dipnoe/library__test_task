from datetime import datetime

from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    @staticmethod
    def validate_isbn(value):
        if len(value) < 13:
            raise serializers.ValidationError("Слишком короткий ISBN.")
        return value

    @staticmethod
    def validate_publishing_year(value):
        if int(value) > datetime.now().year:
            raise serializers.ValidationError("Дата публикации книги не может быть больше текущего года.")
        return value
