import graphene

import users.schema, items.schema, matches.schema


class Query(items.schema.Query, users.schema.Query, matches.schema.Query, graphene.ObjectType):
    pass

class Mutation(items.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)