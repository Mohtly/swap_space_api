import graphene
import graphql_jwt

import items.schema, matches.schema
import users.schema


class Query(users.schema.Query, items.schema.Query, matches.schema.Query, graphene.ObjectType):
    pass

class Mutation(items.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)