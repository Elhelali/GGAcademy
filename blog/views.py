from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Topic, Subtopic

# Create your views here.
def post (request, b_slug=None):
    if b_slug!=None:
	    post= get_object_or_404 (Post,slug=b_slug)
	    topics= Topic.objects.filter (post_id=post)
    subtopics = []
    for topic in topics:
        subtopics.append(Subtopic.objects.filter (topic_id=topic))
        print (subtopics)
    
    
    return render (request, 'post.html', {'post':post,'topics':topics} )