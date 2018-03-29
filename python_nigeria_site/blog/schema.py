
from python_nigeria_site.blog.models import BlogModel
from graphene_django import DjangoObjectType
import graphene

class Blog(DjangoObjectType):
    class Meta:
        model = BlogModel

class Query(graphene.ObjectType):
    blogs = graphene.List(Blog)

    def resolve_users(self, info):
        return BlogModel.objects.all()

schema = graphene.Schema(query=Query)

