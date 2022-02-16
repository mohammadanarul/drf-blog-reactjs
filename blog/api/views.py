from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post

@api_view(['GET'])
def blog_post_list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success",
                "data": serializer.data
            })

@api_view(['PUT'])
def update_blog_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success",
                "data": serializer.data,
                'message': 'Successfully your post updated'
            })
    
@api_view(['PATCH'])
def partiali_update_blog_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success",
                "data": serializer.data,
                'message': 'Successfully your post partial updated'
            })
        
        
@api_view(['DELETE'])
def partiali_update_blog_post(request, pk):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=False)
    serializer.delete()