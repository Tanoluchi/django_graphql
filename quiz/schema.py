import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Quizzes, Answer, Question


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")
 
class Query(graphene.ObjectType):
    quiz = graphene.String()

    def resolve_quiz(root, info):
        return f"This is the first question"


schema = graphene.Schema(query=Query)


