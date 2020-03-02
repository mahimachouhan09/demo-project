from django import forms
from .models import Activity, Answer,Profile,Question,Topic
from django.forms import ModelForm
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100 )
    last_name = forms.CharField(max_length = 100)
    contact_number = forms.IntegerField()
    profile_pic = forms.ImageField(required= False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        profile_pic = self.cleaned_data['profile_pic']
        contact_number = self.cleaned_data['contact_number']
        p = Profile(user = user , contact_number= contact_number ,profile_pic = profile_pic)
        p.save()
        return user

class TopiclistForm(forms.Form):
    OPTIONS = [(topic.id, topic.name) for topic in Topic.objects.all() ]
    topics = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    def save(self, request):
        profile = request.user.profile
        topics = self.cleaned_data['topics']
        for topic in topics:
            topic = Topic.objects.get(pk=topic)
            profile.topics.add(topic)
            profile.save()

class ProfileForm(forms.Form):
    class Meta:
        model=Profile
        fields = ('username', 'email','first_name','last_name','contact_number', 'topics')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {'user' : forms.HiddenInput()}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),
                   'question': forms.HiddenInput(),}

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),
                   'activity_type': forms.HiddenInput(),
                   'content_type': forms.HiddenInput(),
                    }
