from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
# from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.core.paginator import Paginator

from post.models import Post
from post.forms import PostForm


# Create your views here.

''' Generic View '''
# 생성
class PostCreateView(CreateView):
    model = Post            # Model 지정
    form_class = PostForm   # Form 지정
    template_name = 'posts/post_form.html'           # Template 지정
    
    def get_success_url(self):
        # reverse : url name으로부터 url을 찾는다, kwargs : keyword argument
        # self.object : 클래스 안에 생성된 model 객체에 접근
        return reverse('post-detail', kwargs={ 'post_id': self.object.id})


# 리스트보기
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    # context_object_name = 'posts'
    ordering = ['-dt_created']      # 최신 순 내림차순
    paginate_by = 6
    # page_kwarg = 'page'             # 현재 페이지를 qryString의 어떤 값으로 조회하는지 알려줌.


# 상세보기
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'            # 조회할 id(urls에 정의되어 있는 id 사용)
    context_object_name = 'post'


# 수정
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={ 'post_id': self.object.id})


# 삭제
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    
    def get_success_url(self):
        return reverse('post-list')


def index(request):
    return redirect('post-list')




''' ClassView '''
# class PostCreateView(View):
#     ''' post, get, put, patch, delete 등 HTTP 메서드에 따라 오버라이딩 가능 '''
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', { 'form': post_form })

#     def post(self, request):
#         post_form = PostForm(request.POST)
#         # 유효성 체크
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id = new_post.id)



''' 함수형 '''
# def post_create(request): 
#     if request.method == 'POST':
#         # ⭐⭐⭐ 기존의 Form을 ModelForm으로 수정한 방법(위/아래 내용은 동일)
#         # title = request.POST['title']
#         # content = request.POST['content']
#         # new_post = Post(
#         #     title = title, 
#         #     content = content
#         # )
#         # new_post.save()
        
#         post_form = PostForm(request.POST)  # form과 model을 바운딩
        
#         # 유효성 체크
#         if post_form.is_valid():
#             # DB에 신규 데이터 저장
#             new_post = post_form.save()
#             # redirect 경로를 url 이름으로 지정
#             return redirect('post-detail', post_id = new_post.id)
        
#     else :
#         # form 데이터 입력 이전의 화면 렌더
#         post_form = PostForm()
        
#     return render(request, 'posts/post_form.html', { 'form': post_form })



# def post_list(request): 
#     ''' 페이지 적용 이전 방식'''
#     # posts = Post.objects.all()
#     # context = { "posts": posts }
#     # return render(request, 'posts/post_list.html', context)
    
#     posts = Post.objects.all()
    
#     # Query String에 접근하는 방법
#     paginator = Paginator(posts, 6)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', { 'page': page })




# ''' 조회(Read) '''
# def post_detail(request, post_id): 
#     # try:
#     #     post = Post.objects.get(id=post_id)
#     # except Post.DoesNotExist:
#     #     raise Http404()
#     ''' 데이터 없으면 catch문 수행하게 해주는 함수 '''
#     post = get_object_or_404(Post, id = post_id)
#     context = { "post": post }
    
#     return render(request, 'posts/post_detail.html', context)



# ''' 수정(Update) '''
# def post_update(request, post_id): 
#     # post_form = PostForm(instance = post)
#     post = get_object_or_404(Post, id = post_id)
    
#     # GET방식일 때는 기존 데이터 조회하여 화면에 출력
#     if request.method == "POST":
#         # 조회한 post 데이터를 Form에 초기화
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id = post.id)
#     else:
#         post_form = PostForm(instance = post)
#     return render(request, 'posts/post_form.html', { 'form': post_form })



# ''' 삭제(Delete) '''
# def post_delete(request, post_id): 
#     post = get_object_or_404(Post, id = post_id)
#     # post = Post.objects.get(id = post_id)
    
#     if(request.method == "POST"):
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', { 'post': post})
