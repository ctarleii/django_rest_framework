from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import SignUpSerializer
from accounts.tokens import create_jwt_pair_for_user


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    @swagger_auto_schema(
        operation_summary="Create a user account",
        operation_description="This sign up a user"
    )
    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User created successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    @swagger_auto_schema(
        operation_summary="Generate JWT pair",
        operation_description="This logins a user with email and password"
    )
    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login Successfull",
                "tokens": tokens
            }

            return Response(data=response)

        return Response(data={
            "message": "Invalid data"
        })

    @swagger_auto_schema(
        operation_summary="Get request info",
        operation_description="This show a request info"
    )
    def get(self, request: Request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }

        return Response(data=content, status=status.HTTP_200_OK)
