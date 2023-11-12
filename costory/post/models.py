from django.db import models
from django.core.validators import MinLengthValidator
from post.validators import validate_symbols

# Create your models here.
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=50, unique=True, error_messages={ 'unique': '이미 있는 제목입니다.' })
    
    # 내용(valiator 적용)
    content = models.TextField(validators = [
                                    MinLengthValidator(10, "본문 내용을 10자 이상 적어주세요."), 
                                    validate_symbols        # 직접 정의한 유효성 검사
                                ])
    
    # 작성일
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    
    # 기수정일
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
    
    def __str__(self):
        return self.title