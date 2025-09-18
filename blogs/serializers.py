from rest_framework import serializers
from .models import Blogs, Comment



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    # commet comes in Blog
    comments = CommentsSerializer(many=True, read_only = True)   # name must be related_name in comments
    class Meta:
        model = Blogs
        fields = '__all__'