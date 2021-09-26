from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from dca_app.schema import schema


urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema))
]
