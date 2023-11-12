# Models
> Django 프레임워크에서 데이터베이스와 상호작용하기 위한 핵심 구성 요소 중 하나.  
>
> 모델은 데이터베이스의 테이블을 Python 클래스로 나타내며, 데이터베이스 테이블의 
> 스키마를 정의하고 데이터를 다루기 위한 도구를 제공한다. 
> 
> **Django 모델의 주요 특징과 개념에 대한 설명**
> 
> **✏️ 모델 클래스 정의**  
> 모델 클래스는 Django의 ***`models.Model`*** 클래스를 상속하여 정의.  
> 각 모델 클래스는 데이터베이스의 테이블을 나타내며, 클래스의 속성은 데이터베이스 테이블의
> 열에 해당한다.


<hr/>

### Django Model의 주요 데이터 필드  
> **👉🏻 CharField**  
> 텍스트 데이터 저장 가능한 필드  
>
> **👉🏻 TextField**  
> 매우 긴 텍스트 데이터 저장 가능한 필드  
>
> **👉🏻 DateTimeField**  
> 날짜와 시간 정보를 저장하는 데 사용되는 필드  
>   - Parameter
>     *  **`verbose_name`**  
>       사람이 읽기 쉬운 이름을 정의하는 데 사용. 이 이름은 모델 폼 및 관리자 페이지에서
>       필드 레이블로 표시됨.
>     * **`auto_now`**  
>       매개변수를 `True`로 설정하면 객체가 저장될 때 해당 필드에 현재 시간을  
>       자동으로 업데이트  
>     * **`auto_now_add`**
>       매개변수를 True로 설정하면 객체가 처음 생성될 때만 해당
>       필드를 현재 시간으로 설정하며, 이후 객체가 수정될 때는 업데이트하지 않음.  
>
> **👉🏻 IntegerField**  
> integer 변수를 사용하기 위한 필드  

<hr/>

# Forms
> 사용자로부터 데이터를 수집하고 검증하는 데 사용되는 django에서 제공하는 도구.   
> Django 폼은 HTML 폼 요소를 생성하고 데이터를 처리하는 기능을 제공하여  
> 개발자가 폼을 쉽게 만들고 사용할 수 있도록 한다.

**form 클래스는 다음과 같이 정의할 수 있다.**  
1. **프로젝트 앱에 `forms.py` 파일 생성**  

2. **`form.py` 작성**  
  ```python
  from django import forms    # >> form 클래스를 정의하기 위한 모듈 import
  
  # form 작성 시에는 model의 필드와 동일하게 설정하여야 한다.
  class PostForm:
    title = forms.CharField(max_length = 50, label = "제목")
    content = forms.CharField(label = '본문', widget = forms.Textarea)
    score = forms.IntegerField(label = '점수')
    .
    .
    .
  ```

  3. **`views.py`에서 정의한 form 인스턴스 생성**  
    ```python
    from post.forms import PostForm
    .
    .
    .

    def post_create(request):
      # 정의한 form을 인스턴스화 및 context에 추가(이름 : form)
      post_form = PostForm()
      return render(request, '템플릿.html', { "form": post_form })
    ```

  4. **template에서 사용**  
    ```html
    <form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type='submit' value='전송'/>
    </form>```


# 테스트 데이터 생성 (DataBase Seeding)
> **dump 데이터 파일(.json) 생성 명령어**  
> **`python manage.py dumpdata post [--indent=4]> post_data.json`**  
> **`python manage.py loaddata post_data.json`**
<hr/>  

### 대량의 데이터 생성(Django-seed)
> **정의 :** 모델에 정의된 필드를 보고 임의의 데이터를 자동으로 생성해 주는 패키지  
> 1. **`pip install django-seed==0.2.2`**  
> 2. settings.py => INSTALLED_APPS에 `django_seed` 추가(⭐꼭!!! 언더스코어('_') 사용⭐)
> 3. python manage.py seed post --number=50

🎆 **만약 데이터 유효성 체크를 추가하고, 기존 데이터에 유효성 체크를 수행하려면 logic 작성 후 shell에서 해당 함수 실행하면 됨.**



# 페이지네이터(Paginator)
> ```python
> # Django에서 제공하는 기본 페이지네이터
> from django.core.paginator import Paginator
> from post.models import Post
> posts = Post.objects.all()
> pages = Paginator(posts, 6)   # posts 6개를 하나의 페이지로 설정
> pages.page_range              # return : 페이지 범위 >>> range(1, 10) 1 ~ 9페이지 까지 존재
>
> # 하나의 페이지 가져오기
> page = pages.page(1)
> # 해당 페이지의 리스트 보기
> page.object_list
>
> # 다음 페이지 / 이전 페이지 여부 보기
> page.has_next()
> page.has_previous()
> 
> # 다음 페이지가 몇 페이지일까?
> page.next_page_number()
> ```






# Class-Based-View, Generic View

# Context