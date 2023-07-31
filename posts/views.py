from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view


posts = [
    {
        "id": 1,
        "title": "JSON Example 1",
        "content": "This is an example JSON object with three fields: id, title, and content."
    },
    {
        "id": 1,
        "title": "JSON Example 1",
        "content": "This is an example JSON object with three fields: id, title, and content."
    },
    {
        "id": 3,
        "title": "JSON Example 3",
        "content": "This is a third example JSON object with three fields: id, title, and content."
    },
]


@api_view(http_method_names=['GET', 'POST'])
def homepage(request: Request):
    if request.method == 'POST':
        data = request.data
        response = {"message": "Hello World", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def list_posts(request: Request):
    return Response(data=posts, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def post_detail(request: Request):

