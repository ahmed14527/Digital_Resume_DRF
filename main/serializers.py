from rest_framework import serializers
from .models import Skill, UserProfile, ContactProfile, Testimonial, Media, Portfolio, Blog, Certificate

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'score', 'image', 'is_key_skill']


class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'avatar', 'title', 'bio', 'skills', 'cv']


class ContactProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactProfile
        fields = ['timestamp', 'name', 'email', 'message']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['thumbnail', 'name', 'role', 'quote', 'is_active']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['image', 'url', 'name', 'is_image']


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['date', 'name', 'description', 'body', 'image', 'slug', 'is_active']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['timestamp', 'author', 'name', 'description', 'body', 'slug', 'image', 'is_active']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['date', 'name', 'title', 'description', 'is_active']