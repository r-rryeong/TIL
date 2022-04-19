## Authentication SystemⅠ

### The Django Authentication System

Django 인증 시스템은 django.contrib.auth에 Django contrib module로 제공

필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS 설정에 나열된 아래 두 항목으로 구성됨

1. django.contrib.auth

   : 인증 프레임워크의 핵심과 기본 모델을 포함

2. django.contrib.contenttypes

   : 사용자가 생성한 모델과 권한을 연결할 수 있음

Django 인증 시스템은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공(처리)하며, 이러한 기능이 어느 정도 결합되어 일반적으로 인증 시스템이라고함

- 인증(Authentication)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- 권한, 허가(Authorization)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정



- 두번째 앱(accounts) 생성하기

  app 이름이 반드시 accounts일 필요는 없음

  단, auth와 관련해 Django 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 되도록 accounts로 지정하는 것을 권장



### 쿠키와 세션

- HTTP 특징

  HTTP(Hyper Text Transfer Protocol)란? HTML 문서와 같은 리소스(자원, 데이터)들을 가져올 수 있도록 해주는 프로토골(규칙, 규약), 웹에서 이루어지는 모든 데이터 교환의 기초

  - 비연결지향

    서버는 요청에 대한 응답을 보낸 후 연결을 끊음

  - 무상태

    연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나면 상태 정보가 유지되지 않음

    클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적임

  ⇒ 클라이언트와 서버의 지속적인 관계를 유지하기 위해 쿠키와 세션이 존재



- 쿠키 개념

  서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

  사용자가 웹사이트를 방문할 경우 해당 웹 사이트의 서버를 통해 사용자의 컴퓨터에 자리잡게 되는 작은 기록 정보 파일

  - 브라우저(클라이언트)는 쿠키를 로컬에 key-value의 데이터 형식으로 저장
  - 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

  

  HTTP 쿠키는 상태가 있는 세션을 만들어 줌

  쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용

  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문

  ⇒ 웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 함께 전송

- 쿠키 사용 목적
  1. 세션 관리(로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리)
  2. 개인화(사용자 선호, 테마 등의 설정)
  3. 트래킹(사용자 행동을 기록 및 분석)

- 세션(session)

  - 사이트와 특정 브라우저 사이의 '상태'를 유지시키는 것
  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 발급받은 session id를 쿠키에 저장
  - ID는 세션을 구별하기 위해 필요하며, 쿠키에는 ID만 저장함

- 쿠키 lifetime

  쿠키의 수명은 두 가지 방법으로 정의할 수 있음

  1. session cookies

     현재 세션이 종료되면 삭제됨

     브라우저가 현재 세션이 종료되는 시기를 정의

  2. persistent cookies(or permanent cookies)

     expires 속성에 지정된 날짜 혹은 max-age 속성에 지정된 기간이 지나면 삭제

- Session in Django

  Django의 세션은 미들웨어를 통해 구현됨

  Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄

  - 세션 정보는 Django DB의 django_session 테이블에 저장됨

  > MIDDLEWARE
  >
  > HTTP요청과 응답 처리 중간에 작동하는 시스템
  >
  > Django는 HTTP 요청이 들어오면 미들웨어를 거쳐 해당 URL에 등록되어 있는 view로 연결해주고 HTTP 응답 역시 미들웨어를 거쳐서 내보냄

### 로그인

로그인은 session을 create하는 로직과 같음

인증에 관한 built-in forms 제공

- AuthenticationForm

  사용자 로그인을 위한 form

  request를 첫번째 인자로 취함

- login 함수(request, user, backend=None)

  HttpRequest객체와 User 객체 필요

  Django는 session framework를 사용하여 세션에 user의 ID 저장(=로그인)

  login 함수 이름을 auth_login으로 변경 ⇒ login view 함수와의 혼동 방지

  로그인 후 브라우저와 Django DB에서 Django로부터 발급받은 sessionid 확인



- get_user()

  AuthenticationForm의 인스턴스 메서드

  user_cache는 인스턴스 생성 시에 None으로 할당되며, 유효성 검사를 통과했을 경우 로그인 한 사용자 객체로 할당 됨

  인스턴스의 유효성을 먼저 확인하고, 인스턴스가 유효할 때만 user를 제공하려는 구조



### Authentication data in templates

- context processors

  템플릿이 렌더링 될 때 자동으로 호출 가능한 context 데이터 목록

- Users

  템플릿을 렌더링할 때, 현재 로그인한 사용자를 나타내는 auth.

  로그인하지 않은 경우는 AnonymousUser 인스턴스

  템플릿 변수 {{ user }}에 저장됨



### 로그아웃

로그아웃은 session을 delete하는 로직과 같음

- logout(request)

  HttpRequest 객체를 인자로 받고 반환 값이 없음

  현재 요청에 대한 session data를 DB에서 완전히 삭제하고, 클라이언트의 쿠키에서도 sessionid가 삭제됨

  이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, **이전 사용자의 세션 데이터레 액세스하는 것을 방지하기 위함**

  

### 로그인 사용자에 대한 접근 제한

- 로그인 사용자에 대한 엑세스 제한 2가지 방법

  1. is_authenticated

     - User model의 속성 중 하나

     - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성

       (AnonymousUser에 대해서는 항상 False)

  2. @login_required

     - 사용자가 로그인되어 있지 않으면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect함

       LOGIN_URL의 기본값은 '/accounts/login/'

       app 이름을 accounts로 했던 이유 중 하나

     - 사용자가 로그인되어 있으면 정상적으로 view함수 실행

     - 인증 성공 시 사용자가 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨

       ex) /accounts/login/?next=/articles/create/

     - "next" query string parameter

       로그인이 정상적으로 진행되면 기존에 요청했던 주소로 redirect 하기 위해 마치 주소를 keep해주는 것

       단, 별도로 처리 해주지 않으면 우리가 view에 설정한 redirect 경로로 이동



- 두 데코레이터로 인해 발생하는 구조적 문제와 해결

  - @require_POST 작성된 함수에 @login_required를 함께 사용하는 경우 **에러 발생**
  - 로그인 이후 "next" 매개변수를 따라 해당 함수로 다시 redirect되는데, 이 때 @require_POST 때문에 405 에러가 발생
  - 두가지 문제 발생
    1. redirect 과정에서 POST 데이터의 손실
    2. redirect 요청은 POST 방식이 불가능하기 때문에 GET 방식으로 요청됨

  ⇒ login_required는 GET method request를 처리할 수 있는 view 함수에서만 사용해야함



## Authentication SystemⅡ

### 회원가입

- UserCreationForm

  - 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

  - 3개의 필드를 가짐
    1. username
    2. password1
    3. password2



### 회원탈퇴

회원탈퇴는 DB에서 사용자를 삭제하는 것과 같음

반드시 탈퇴 후 로그아웃순으로 처리해야함



### 회원정보 수정

- UserChangeForm

  사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- UserChangeForm 사용 시 문제점

  일반 사용자가 접근해서는 안될 정보를(fields)까지 모두 수정이 가능해짐

  따라서 UserChangeFormd을 상속받아 CustomUserChangeForm이라는 클래스를 작성해서 접근 가능한 field를 조정

- get_user_model()

  현재 프로젝트에서 활성화된 사용자 모델 반환

  `django.contrib.auth.get_user_model()`을 사용하여 참조해야한다(**강조**)



### 비밀번호 변경

- PasswordChangeForm

  사용자가 비밀번호를 변경할 수 있도록 하는 Form

  이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

  SetPasswordForm의 첫번째 인자는 user

- 암호 변경 시 세션 무효화 방지

  - update_session_auth_hash(request, user)

    현재 요청과 새 session hash가 파생될 업데이트 된 사용자 객체를 가져오고, session hash를 적절하게 업데이트

    비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 로그인 상태를 유지할 수 없기 때문

    암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session을 업데이트함