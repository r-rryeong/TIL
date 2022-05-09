# REST API(22.04.20)

### HTTP

- HTTP(HyperText Transfer Protocol)

  - 웹상에서 컨텐츠를 전송하기 위한 약속

  - 웹에서 이루어지는 모든 데이터 교환의 기초(요청과 응답)

- 기본 특성

  - stateless
  - connectionless
  - 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록함

- HTTP request methods

  자원에 대한 행위(수행하고자 하는 동작)를 정의

  예시: GET(조회), POST(작성), PUT(수정), DELETE(삭제)

- HTTP response status codes

  특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
  
  1. Informational responses(1xx)
  2. Successful responses(2xx)
  3. Redirection messages(3xx)
  4. Client error responses(4xx)
  5. Server error responses(5xx)



- 웹에서의 리소스 식별

  HTTP요청의 대상을 리소스(자원)라고 함

  리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음

  URI(Uniform Resource Identifier)로 식별됨

- URL, URN

  - URL(Uniform Resource Locator)

    통합 자원 위치

    네트워크 상에 자원이 어디 있는지 알려주기 위한 약속

    과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성

    '웹주소', '링크'라고 불림

  - URN(Uniform Resource Name)

    통합 자원 이름

    URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함

    - ISBN(국제표준도서번호)

- URI(Uniform Resourc Identifier)

  - 통합 자원 식별자

  - 인터넷의 자원을 식별하는 유일한 주소(정보의 자원을 표현)

  - 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열

  - 하위 개념

    URL, URN

    URI는 크게 URL과 URN으로 나눌 수 있지만, URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도함

- URI의 구조

  - Scheme(protocol)

    브라우저가 사용해야하는 프로토콜

    http(s), data, file, ftp, mailto

    `https://`www.example.com:80/path/to/myfile.html/?key=value#quick-start

  - Host(Domain name)

    요청을 받는 웹 서버의 이름

    IP address를 직접 사용할 수도 있지만, 실 사용이 불편하므로 그리 자주 사용하지 않음(google의 IP address - 142.251.42.142)

    https://`www.example.com`:80/path/to/myfile.html/?key=value#quick-start

  - Port

    웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문(gate)

    HTTP 프로토콜의 표준 포트

    - HTTP 80
    - HTTPS 443
  
    https://www.example.com`:80`/path/to/myfile.html/?key=value#quick-start
  
  - Path
  
    웹 서버 상의 리소스 경로
  
    초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 물리적은 실제 위치가 아닌 추상화 형태의 구조로 표현
  
    https://www.example.com:80`/path/to/myfile.html`/?key=value#quick-start
  
  - Query(Identifier)
  
    Query String Parameters
  
    웹서버에 제공되는 추가적인 매개 변수
  
    & 로 구분되는 key-value 목록
  
    https://www.example.com:80/path/to/myfile.html/`?key=value`#quick-start
  
  - Fragment
  
    Anchor
  
    자원 안에서의 북마크의 한 종류를 나타냄
  
    브라우저에게 해당 문서(HTML)의 특정 부분을 보여주기 위한 방법
  
    브라우저에게 알려주는 요소이기 때문에 부분 식별자라고 부르며 `#`뒤의 부분은 요청이 서버에 보내지지 않음(데이터로서 전달되는 것 X)
    
    https://www.example.com:80/path/to/myfile.html/?key=value`#quick-start`



### RESTful API

- API(Application Programming Interface)

  - 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

    애플리케이션과 프로그래밍으로 소통하는 방법

  - Web API

    웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

    현재 웹 개발은 모든 것을 직접 개발하기보다 여러 open API를 활용하는 추세

    ex) TMDB

  - 응답 데이터 타입

    HTML, XML, JSON 등

  - 대표적인 API 서비스 목록

    Youtube API, Naver Papago API, Kakao Map API...



- REST

  - REpresentational State Transfer

  - API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론

  - 네트워크 구조 원리의 모음

    자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법

  - REST 원리를 따르는 시스템을 RESTful 이란 용어로 지칭함

  - 자원을 정의하는 방법에 대한 고민

    ex) 정의된 자원을 어디에 위치 시킬 것인가

  

  - REST의 자원과 주소의 지정 방법

    1. 자원

       URI

    2. 행위

       HTTP Method

    3. 표현

       자원과 행위를 통해 궁극적으로 표현되는 (추상화된)결과물

       JSON으로 표현된 데이터를 제공

  - JSON

    JavaScript Object Notation

    JavaScript의 표기법을 따른 단순 문자열
    
    - 특징
    
      사람이 읽거나 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉬움
    
      파이썬의 딕셔너리, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료구조로, 쉽게 변화할 수 있는 key-value 형태의 구조를 갖고 있음

  

  - REST의 핵심 규칙
    1. '정보'는 URI로 표현
    2. 자원에 대한 '행위'는 HTTP Method로 표현(GET, POST, PUT, DELETE)

- RESTful API

  REST원리를 따라 설계한 API

  프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성



### Response

- Create Dummy Data

  django-seed 라이브러리를 사용해 모델 구조에 맞는 데이터 생성

- Response - JsonResponse

  - Content - Type entity header

    데이터의 media type을 나타내기 위해 사용됨

    응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌

  - JsonResponse objects

    JSON으로 인코딩된 객체를 만들어줌

    - "safe" parameter

      True(기본값)

      dict 이외의 객체를 직렬화(Serialization)하려면 False로 설정해야함(들어오는 인자가 딕셔너리가 아니라면)

- Serialization
  - 직렬화(변화가 용이하도록 중간 과정의 데이터타입으로 변환해주는 과정)
  
  - 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  
  - Serialization in Django
  
    Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어줌
  
- Response - Django Serializer

  Django의 내장 HttpResponse를 활용한 JSON 응답 객체

  주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어 줄 필요 없음

  + 위와 달리 model, pk 추가됨

- Response - Django REST Framework

  Django REST Framework(DRF) 라이브러리를 사용한 JSON 응답

  Article 모델에 맞춰 자동으로 필드를 생성해 serialize해주는 ModelSerializer

  DRF의 Response()를 활용해 Serialize 된 JSON 객체 응답

  - Django REST Framework(DRF)

    Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리

    DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

  - Web API

    웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

- Django ModelForm & DRF Serializer

  |          | Django    | DRF        |
  | -------- | --------- | ---------- |
  | Response | HTML      | JSON       |
  | Model    | ModelForm | Serializer |

  

### Single Model⭐

- DRF with Single Model

  단일 모델의 data를 serialization하여 JSON으로 변환하는 방법에 대한 학습

  단일 모델을 두고 CRUD 로직을 수행 가능하도록 설계

  API 개발을 위한 핵심 기능을 제공하는 도구 활용

  - DRF built-in form

  - Postman

    API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼

    설계, 테스트, 문서화 등의 도구를 제공함으로써 API를 더 빠르게 개발 및 생성할 수 있도록 도움

- ModelSerializer

  모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortsut

  아래 핵심 기능을 제공

  1. 모델 정보에 맞춰 자동으로 필드 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
  3. .create() & .update()의 간단한 기본 구현이 포함됨

- 'many' argument

  `many=True`

  단일 인스턴스 대신 QuerySet 등을 serialization하기 위해서는 serializer를 인스턴스화 할 때 many=True를 키워드 인자로 전달해야함



- Build RESTful API

  |             | GET          | POST    | PUT         | DELETE      |
  | ----------- | ------------ | ------- | ----------- | ----------- |
  | articles/   | 전체 글 조회 | 글 작성 |             |             |
  | articles/1/ | 1번 글 조회  |         | 1번 글 수정 | 1번 글 삭제 |

  ⇒ view 함수 2개 필요

- 1. GET - Article List

  - 'api_view' decorator

    기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405로 응답

    view 함수가 응답해야하는 HTTP 메서드의 목록을 리스트의 인자로 받음

    DRF에서는 선택이 아닌 필수적으로 작성해야 해당 view 함수가 정상적으로 동작함

- 2. GET - Article Detail

- 3. POST - Create Article

  201 Created 상태 코드 및 메시지 응답

  RESTful 구조에 맞게 작성(URI는 자원을 표현, 자원을 조작하는 행위는 HTTP Method)

  article_list 함수로 게시글을 조회하거나 생성하는 행위를 모두 처리 가능

  - Status Codes in DRF

    DRF에는 status code를 보다 명확하고 읽기 쉽게 만드는 데 사용할 수 있는 정의된 상수 집합을 제공

    status 모듈에 HTTP status code 집합이 모두 포함되어 있음

    (단순히 status=201 같은 표현도 사용할 수 있지만 권장하지 않음)

  - 'raise_exception' argument

    `is_valid()`는 유효성 검사 오류가 있는 경우, ValidationError 예외를 발생시키는 raise_exception 인자를 사용할 수 있음

    DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, 기본적으로 HTTP status code 400을 응답으로 반환함

- 4. DELETE - Delete Article

  204 No Content 상태 코드 및 메시지 응답

  article_detail 함수로 상세 게시글을 조회하거나 삭제하는 행위 모두 처리 가능

- 5. PUT - Update Article

  article_detail 함수로 상세 게시글을 조회하거나 삭제, 수정하는 행위 모두 처리 가능



> swagger 문서
>
> https://drf-yasg.readthedocs.io/en/stable/custom_spec.html#the-swagger-auto-schema-decorator



### 1:N Relation

1:N 관계에서의 모델 data를 serialization하여 JSON으로 변환하는 방법에 대한 학습

2개 이상의 1:N 관계를 맺는 모델을 두고 CRUD 로직을 수행 가능하도록 설계하기

- 1. GET - Comment List

- 2. GET - Comment Detail

- 3. POST - Create Comment

  Article 생성과 달리 Comment 생성은 생성 시에 참조하는 모델의 객체 정보 필요(1:N 관계에서 N은 어떤 1을 참조하는지에 대한 정보가 필요하기 때문)

  - .save()

    .save() 메서드는 특정 serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음(인스턴스를 저장하는 시점에 추가 데이터 삽입이 필요한 경우)

  - Read Only Field(읽기 전용 필드)

    어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 serialization하는 과정에서 article 필드가 유효성 검사를 통과하지 못함

    이때는 읽기 전용 필드 설정을 통해 serialization하지 않고 반환 값에만 해당 필드가 포함되도록 설정할 수 있음

- 4. DELETE & PUT - delete, update Comment



- 1:N Serializer

  1. 특정 게시글에 작성된 댓글 목록 출력하기

     Serializer는 기존 필드 override하거나 추가 필드를 구성할 수 있음

     - PrimaryKeyRelatedField

       필드가 to many relationships를 나타내는데 사용되는 경우 many=True 속성 필요
  
       해당 필드 값을 form-data로 받지 않으면 read_only=True 설정 필요
  
       (역참조 시 생성되는 comment_set을 다른 매니저 이름으로 override할 수 있음. 단, 다음과 같이 수정할 경우 이전 serializers.py에서의 클래스 변수명도 일치하도록 수정)
  
     - Nested relationships
  
       중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
  
       두 클래스의 상하위치 변경
  
  2. 특정 게시글에 작성된 댓글의 개수 구하기
  
     새로운 필드 추가
     
     - 'source' arguments
     
       필드를 채우는 데 사용할 속성의 이름
     
       점(dot)표기법을 사용하여 속성 탐색