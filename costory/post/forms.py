from django import forms
from post.models import Post
from post.validators import validate_symbols
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    # memo = forms.CharField(max_length=80, validators=[validate_symbols])
    
    class Meta:
        model = Post
        
        # 아래 두 내용은 동일한 내용임
        # fields = '__all__'
        fields = ['title', 'content']
        
        # 필드의 위젯 직접 설정.
        # attr : 위젯의 속성값들 직접 설정 가능
        widgets = {
            "title": forms.TextInput(attrs = {
                "class": "title",
                "placeholder": "제목을 입력하세요.",
                }),
            "content": forms.Textarea(attrs = {
                "class": "content",
                "placeholder": "내용을 입력하세요"
            })
        }
        
    # cleand_data : form 필드를 정의할 때 넣어준 
    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('"*"는 포함될 수 없습니다.')
        
        return title