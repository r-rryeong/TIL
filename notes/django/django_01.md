# Django

### Web framework

클라이언트 ;웹브라우저(크롬) → 서버(요청)

서버 ;django → 클라이언트(응답)

- Static web page(정적 웹 페이지)

  서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

  모든 상황에서 모든 사용자에게 동일한 정보를 표시

- Dynamic web page(동적 웹 페이지)

  추가적인 처리 과정 이후 클라이언트에게 응답을 보냄

  방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름

  서버 사이드 프로그래밍 언어(Python, Jave, C++ 등)가 사용되며, 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

- Framework

  개발 환경, tool 제공

  재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움

- Web framework 목적

  웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적임



- Django를 사용해야하는 이유

  대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨

- Framework 구조

  MVC Design Pattern(model-view-controller)

  Django는 **MTV Pattern**이라고 함(특별한 의미없음, 더 잘 맞는 것 같아서)

- MTV Pattern

  Model

  : (추가, 수정, 삭제)

  Template

  : 실제 보여지는 부분(presentation)

  View⭐

  : HTTP 요청을 수신하고 HTTP응답을 반환, template에게 응답의 서식 설정을 맡김

  

  ![image-20220302125229192](django_01.assets/image-20220302125229192.png)

> 정리



### Django Intro

URL → VIEW → TEMPLATE (데이터의 흐름)

1. 가상환경 생성 및 활성화

2. django 설치

3. 프로젝트 생성

   ⭐프로젝트 생성 명령어

4. 서버 켜서 로켓 확인

5. 앱 생성

6. 앱 등록

(git으로 관리할 때는 venv는 커밋하지 않기. requirements.txt만 커밋)

- 프로젝트 구조

  settings.py : 애플리케이션의 모든 설정 포함

  **urls.py** : 사이트의 url과 적절한 views의 연결 지정

  위 두 개의 파일만 터치(다른 파일은 터치할 일 없음)

- Application 생성

- Application 구조

  admin.py

  models.py

  views.py

  위 세 개의 파일만 터치



- **Project & Application**

  - Project

    프로젝트에는 여러 앱이 포함될 수 있음

    앱은 여러 프로젝트에 있을 수 있음(이 단계까지 넓히지 않음)

  - Application

    앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당

    하나의 프로젝트는 여러 앱을 가짐

- 앱 등록

※ 반드시 생성 후 등록! INSTALLED_APPS에 먼저 등록하고 생성하려면 앱이 생성되지 않음

※ django가 권장하는 앱 등록 순서가 있음. 해당 순서를 지키지 않아도 수업 과정에서는 문제가 없지만, 추후 advanced한 내용을 대비하기 위해 지키는 것을 권장(로딩순서, 가장 위에 있을수록 우선 로딩)



### 요청과 응답

- View

  함수의 인자로는 request로 지정(요청정보) (관행적 약속)

  함수의 return으로 render() (사용자에게 응답 결과 전달)

- Templates

  반드시 앱 폴더 내부에 'templates'폴더 내부에 html 파일이 있어야함

- LANGUAGE_CODE: 영어로 쓰는 것 권장



### Template

- Django Template Language(DTL)

  조건, 반복, 변수 치환, 필터 등의 기능 제공

  단순히 Python이 HTML에 포함된 것이 아니며, 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것

- DTL Syntax

  1. Variable

     render()를 사용하여 view.py에서 정의한 변수를 template파일로 넘겨 사용하는 것

     render()안의 변수명은 context로 지정(관행적 약속)

     render()의 세번째 인자로 {'key': value}와 같이 딕셔너리 형태로 넘겨주며 여기서 

  2. Filters

     표시할 변수를 수정할 때 사용

     여러 개의 필터 chained가 가능하며 일부 필터는 인자를 받기도 함

  3. Tags

     {% tag %}

     출력 텍스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만듬

     일부 태그는 시작과 종료 태그 필요(범위 지정이 있는 for문...)

     > https://docs.djangoproject.com/en/3.2/ref/templates/builtins/
     >
     > ⭐for문 파트 읽어보기

  4. Comments

     {# 내용 #} : 한줄 주석에만 사용

     ctrl + ' / ': 여러 줄 주석에 사용

- Template inheritance(템플릿 상속)



### HTML Form





### URL

