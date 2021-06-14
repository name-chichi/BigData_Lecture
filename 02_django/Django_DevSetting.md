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



## 4. 그 외 다른 환경설정

- 이미지 입력

```bash
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]
```

- 임시 URL 설정

```python
path('', TemplateView.as_view(template_name='home.html'), name='home'),
path('js01', TemplateView.as_view(template_name='js01.html'), name='js01'),
path('js02', TemplateView.as_view(template_name='js02.html'), name='js02'),
```

- static한 data폴더를 지정 → 분석한 데이터 파일을 읽을때 개발환경에 구애받지 않는 경로 설정

```python
# config>settings.py

DATA_DIRS = [
    os.path.join(BASE_DIR, 'data')
]
```

```python
# 장고 static 경로 설정이 없는 경우
f = open('data/age.csv', 'r', encoding='UTF-8')
f = open('../data/age.csv', 'r', encoding='UTF-8')

# 장고 static한 DATA_DIRS 경로 설정 후
f = open(DATA_DIRS[0] + '\\age.csv', 'r', encoding='UTF-8')
```

- 로그(Log)

```python
LOG_FILE = os.path.join(BASE_DIR,'data/mylog.csv');

LOGGING = {
    'version': 1,
    # 기존의 로깅 설정을 비활성화 할 것인가?
    'disable_existing_loggers': False,
    # 포맷터
    # 로그 레코드는 최종적으로 텍스트로 표현됨
    # 이 텍스트의 포맷 형식 정의
    # 여러 포맷 정의 가능
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
        'format3': {
            'format': '%(asctime)s,%(message)s',
            'datefmt': '%Y-%m-%d-%H-%M-%S'
        },
    },
    # 핸들러
    # 로그 레코드로 무슨 작업을 할 것인지 정의
    # 여러 핸들러 정의 가능
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'format3',
        },
        # 콘솔(터미널)에 출력
    'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        'formatter': 'format3',
    }
    },
    # 로거
    # 로그 레코드 저장소
    # 로거를 이름별로 정의
    'loggers': {
        'users': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'items': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'iot_file': {
            'handlers': ['file','console'],
            'level': 'DEBUG',
        },
    },
}
```

