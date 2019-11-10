import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    # user_id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    # date_time_created = graphene.types.datetime.DateTime()

    #2
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    #3
    def mutate(self, info, first_name, last_name, email):
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.save()

        return CreateUser(
            # id=link.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )


#4
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()