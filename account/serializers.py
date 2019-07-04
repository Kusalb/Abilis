from rest_framework import serializers

from .models import *



class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        # fields = ('username', 'email')
        fields = '__all__'
        # for returning all values

class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = '__all__'


class categoryinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DocumentationSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='new_category', allow_null=True)

    class Meta:
        model = Documentation
        fields = '__all__'


class userpullSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ('username',)


class ForumQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form_question
        fields = ("id", "user", "question", 'date')


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(queryset=Form_question.objects.all(), slug_field='question')
    class Meta:
        model = Form_answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    user  = serializers.SlugRelatedField(queryset=user.objects.all(), slug_field='name')
    class Meta:
        model = Form_question
        fields = ('id','question', 'user')

class AllAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Form_answer
        fields = ('question', 'answer')