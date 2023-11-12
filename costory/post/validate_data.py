'''
1. 모든 Post 데이터 가져오기
2. 각각의 Post 데이터의 content에 '&'가 있는지 체크
3. '&' 기호가 있다면 삭제
4. 데이터 save
'''

from post.models import Post


def validate_post():
    posts = Post.objects.all()

    for post in posts:
        # '&' 기호 처리
        if '&' in post.content:
            print("'&' 포함된 ID : " + str(post.id))
        
        post.content = post.content.replace('&', '')
        post.save()
        
        # 수정일 / 생성일 처리
        if post.dt_modified < post.dt_created:
            post.save()