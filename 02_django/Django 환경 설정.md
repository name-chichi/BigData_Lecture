## Django 환경 설정

Web Application 



### 1.Web Server



### 2. Python Project

- Web application 추가
- django Server



### 3. 개발 순서

1. Python Project 생성

2. django, mysql-client 등 모듈 설치

   ```bash
   pip install django
   ```

3. Web Application 환경으로 변환

   ```bash
   django-admin startproject config .
   ```

4. Project 안에 Web Application 생성

   ```bash
   python manage.py startapp hello
   ```

   ```bash
   python manage.py runserver
   ```

5. html 폴더 설정

   - hello > templates

6. config > settings.py를 수정

   ```bash
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'hello' # 웹애플리케이션 이름 
   ]
   ```

7. config / urls.py 수정

   ```python
   urlpatterns = [
   	path('admin/', admin.site.urls),
   	path('', include('hello.urls')),
   ]
   ```

8. hello / urls.py 파일을 hello 폴더에 복사

   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name='home'),
   ]
   ```

9. views.py 파일에 home 함수 추가

   ```python
   def home(request):
   	return render(request, 'home.html')
   ```

10. templates 폴더에 home.html 생성 후 서버 실행

    ```bash
    python manage.py runserver 80
    ```



cf. 이미지 입력

```bash
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]
```

cf. 임시 URL 설정

```python
path('', TemplateView.as_view(template_name='home.html'), name='home'),
path('js01', TemplateView.as_view(template_name='js01.html'), name='js01'),
path('js02', TemplateView.as_view(template_name='js02.html'), name='js02'),
```

