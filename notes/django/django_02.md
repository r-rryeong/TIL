# Django Model(22.03.07)

### Model

단일한 데이터에 대한 정보를 가짐, 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함

저장된 데이터베이스의 구조(layout)

Django는 model을 통해 데이터에 접속하고 관리

일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨



- Datebase(DB)

  체계화된 데이터의 모임

- 쿼리(Query)

  데이터를 조회하기 위한 명령어

  조건에 맞는 데이터를 추출하거나 조작하는 명령어

  "쿼리를 날린다" → DB를 조작한다

- Datebase의 기본 구조

  - 스키마(schema)

    데이터베이스의 구조와 제약 조건(자료의 구조, 표현 방법, 관계)에 관련한 전반적인 명세를 기술한 것(열과 데이터의 타입으로 구성)

  - 테이블(Table)

    : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

    열(column): 필드(field) or 속성

    행(row): 레코드(record) or 튜플

  - **PK**(기본키; primary key)⭐

    각 행의 고유값으로 반드시 설정되어야 하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.

    django에서는 id가 곧 pk이다.

> Model 정리
>
> 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
>
> DB를 조작



### ORM(Object-Relational-Mapping)

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django-SQL) 데이터를 변환하는 프로그래밍 기술

OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

Django는 내장 Django ORM을 사용함



- ORM의 장점과 단점

  - 장점

    SQL을 잘 알지 못해도 DB조작이 가능

    SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

  - 단점

    ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음(디테일한 구조)

  ⇒ 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것(생산성)

> 왜 ORM을 사용할까?
>
> DB를 객체로 조작하기 위해



- models.py 작성

  각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨

  - django.db.models 모듈의 Model 클래스를 상속받음

  models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의

  - 각 필드는 클래스의 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑

- **사용 모델 필드**

  `CharField(max_length=None, **options)` : 길이 제한이 있는 문자열을 넣을 때 사용할 때. max_length는 필수 인자!

  `TextField`() : 글자수가 많을 때 사용(길이 제한X)

>full_clean()
>
>유효성 검사



### ⭐Migrations⭐

Django가 model에 생긴 변화를 반영하는 방법(class를 table로 만드는 과정)

- 명령어⭐

  `makemigrations` : model을 변경한 것에 기반한 새로운 migration(like 설계도)을 만들 때 사용

  `migrate` : migration을 DB에 반영하기 위해 사용, 모델의 변경 사항들과 DB가 동기화를 이룸

  > 위 두 개는 table로 만들어가는 명령어

  

  `sqlmigrate` : migration에 대한 SQL 구문을 보기 위해 사용, migration이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인할 수 있음

  `showmigrations` : 프로젝트 전체의migration 상태를 확인하기 위해 사용, migration 파일들이 migrate됐는지 안됐는지 여부를 알 수 있음

  > 위 두 개는 확인 용도

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py sqlmigrate app_name 0001(앱이름/ 설계도 번호)

$ python manage.py showmigrations



- 추가 모델 필드 작성 후 makemigrations 진행

  이전 행의 새로운 컬럼의 데이터를 어떻게 처리할 것인가?

  `1) Provide a one-off default now (will be set on all existig rows) `: makemigrations할때 디폴트값으로 해줘

  `2) Quit, and let me add a default in models.py` : models.py에 써놓을게 그거대로 해줘

- DateField's options⭐

  `auto_now_add`: 데이터가 생성될 때의 시간(최초)

  `auto_now`: 현재 시간을 자동으로 저장, Django ORM이 save를 할 때마다 시간 갱신(최종)

- 테이블 이름

  : 앱이름_클래스명

  ex) ssafy_student



### Database API

- DB API

  DB를 조작하기 위한 도구

  Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움

  Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-access API를 자동으로 만듦

- DB API 구문 - Making Queries

  `Article.objects.all()`

  (class name / manager / queryset api)

  - Manager

    : Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스

    기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가

  - QuerySet(유사 리스트)

    데이터베이스로부터 전달받은 객체 목록

    queryset 안의 객체는 0개, 1개, 여러 개일 수 있음

- Django shell

  일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음

  그래서 장고 프로젝트 설정이 load 된 Python shell을 활용해 DB API 구문 테스트 진행

  기본 Django shell보다 더 많은 기능을 제공하는 shell_plus를 사용해서 진행

  - Django-extensions 라이브러리의 기능 중 하나

$ pip install ipython

$ pip install django-extensions (settings.py에 앱 등록)



### CRUD(Create Read Update Delete)

대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create, Read, Update, Delete를 묶어서 일컫는 말



- CREATE 생성

  첫번째 방법 - 인스턴스 생성 후 인스턴스 변수 설정

  두번째 방법 - 초기 값과 함께 인스턴스 생성

  세번째 방법 - Query API `create()` 사용 (save하지 않아도됨)

- CREATE 관련 메서드

  - `save()` method

    객체를 데이터베이스에 저장함

    데이터 생성 시 save()를 호출하기 전에는 객체의 ID값이 무엇인지 알 수 없음

    단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요

- str method:  print할 때 나오는 형태 지정

  표준 파이썬 클래스의 메소드인 str()을 정의하여 각각의 objects가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음 (작성 후 반드시 shell_plus를 재시작해야 반영됨)



- READ

  - `all()`

    현재 QuerySet의 복사본을 반환

    `>>> Article.objects.all()`

  - `get()`

    주어진 lookup 매개변수와 일치하는 객체를 반환

    객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생 시킴

    `>>> article = Article.objects.get(pk=100)`

    `DoesNotExist: Article matching query does not exist.`

  - `filter()`

    주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

- UPDATE

  불러오고, 수정하고, 저장한다

  article 인스턴스 객체의 인스턴스 변수의 값을 변경 후 저장

- DELETE

  `delete()`: QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고

  삭제된 객체수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환

- Field lookups

  조회 시 특정 검색 조건을 지정

  `filter()`, `exclude()`, `get()`에 대한 키워드 인수로 지정

>pk lookup shortcut
>
>https://docs.djangoproject.com/en/4.0/topics/db/queries/#the-pk-lookup-shortcut

> 데이터 베이스 조작을 위한 다양한 QuerySet API methods는 공식문서를 반드시 참고하여 학습할 것



### Admin Site(Automatic admin interface)

사용자가 아닌 서버의 관리자가 활용하기 위한 페이지(web으로 DB를 관리)

Model class를 admin.py에 등록하고 관리

- admin 생성

  $ python manage.py createsuperuser

  관리자 계정 생성 후 서버를 실행한 다음 /admin으로 가서 관리자 페이지 로그인

  내가 만든 Model을 보기 위해서는 admin.py에 작성하여 Django 서버에 등록

- admin 등록

  admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것

  `admin.site.register(Article)`

  models.py에 정의한 `__str__`의 형태로 객체가 표시됨



- ModelAdmin options

  `list_display`: models.py 정의한 각각의 컬럼들의 값을 admin 페이지에 출력

  `list_filter`

  `list_display_links`

  `list_editable`



>다양한 ModelAdmin options 참고
>
>https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#modeladmin-options



### CRUD with views

- HTTP method

  `GET`

  : 반드시 데이터를 가져올 때만 사용해야함

  CRUD에서 R을 담당

  ⭐`POST`

  : 서버로 데이터를 전송할 때 사용

  서버에 변경사항을 만듦

  CRUD에서 C/U/D 역할을 담당

- 사이트 간 요청 위조(cross-site request forgery)

  사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

- CSRF 공격 방어

  Security Token 사용방식(CSRF Token)

  사용자가 데이터에 임의의 난수 값을 부여해, 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함

  이후 서버에서 요청 받을 때마다 전달된 token값이 유효한지 검증

- csrf_token template tag

  ⭐`{% csrf_token %}`

  일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용

- Django shortcut function - **redirect()**

  새 URL로 요청을 다시 보냄

  파이썬 문법을 적용받음





----------------

### django_02 summary

~63 페이지까지

model 수정

orm의 장점과 단점



⭐migrations 명령어



get()으로 데이터 하나만 받아올때는 return이 인스턴스(객체)

그렇지 않을때는 queryset(유사리스트)으로 return