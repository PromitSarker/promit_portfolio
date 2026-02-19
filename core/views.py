from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Project, BlogPost, ContactMessage
from .serializers import ProjectSerializer, BlogPostSerializer, ContactMessageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        return Response(serializer.errors, status=400)

from .models import Project, BlogPost, ContactMessage, Experience, Education, Publication, PortfolioProfile, PhilosophyTrait, SkillCategory

def home(request):
    projects = Project.objects.all()
    blog_posts = BlogPost.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    publications = Publication.objects.all()
    profile = PortfolioProfile.objects.first()
    traits = PhilosophyTrait.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    
    return render(request, 'index.html', {
        'projects': projects,
        'blog_posts': blog_posts,
        'experiences': experiences,
        'educations': educations,
        'publications': publications,
        'profile': profile,
        'traits': traits,
        'skill_categories': skill_categories
    })

