# pjt06 (22.04.08)

### Handling HTTP requests

Django에서 HTTP 요청을 처리하는 방법

1. Django shortcut functions
2. view decorators

- Django shortcut functions

  shortcuts functions 종류

  : render(), redirect(), get_object_or _404()

  - get_object_or _404()

    해당 객체가 없을 경우 doesnotexist 예외 대신 http 404 raise

    get()의 경우 조건에 맞는 데이터가 없을 경우 예외를 발생
    
  - get_list_or_404()

  > http 응답 상태 코드
  >
  > mdn 문서 참고

  

- Django view decorators

  Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터 제공

  데코레이터란?
  
  어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 연장해주는 함수
  
  즉, 원본 함수를 수정하지 않으면서 추가 기능만을 구현할 때 사용
  
  - Allowed HTTP methods
  
    요청 메서드에 따라 view함수에 대한 엑세스를 제한
  
    요건이 조건을 충족시키지 못하면 HttpResponseNotAllowed을 return(405; method not allowed)
  
    1. require_http_methods(): 특정한 method 요청에 대해서만 허용하도록
    2. require_POST()
    3. require_safe(): GET만 허용하도록(조회; index, detail)



### Media files

사용자가 웹에서 업로드하는 정적 파일

유저가 업로드한 모든 정적 파일

- Model field

  - ImageField()

    이미지 업로드에 사용하는 모델 필드

    FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며, 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함

    ImageField 인스턴스는 최대 길이가 100자인 문자열(경로)로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음

    (사용하려면 반드시 Pillow 라이브러리 필요)

  - FileField()

    파일 업로드에 사용하는 모델 필드

    2개의 선택 인자를 가지고 있음

    1. upload_to
    2. storage

  

- ImageField 작성

  - upload_to='images/'

  - blank=True

    이미지 필드에 빈 값이 허용되도록 설정(이미지를 선택적으로 업로드 할 수 있도록)

  - `upload_to` argument

    업로드 디렉토리와 파일 이름 설정하는 2가지 방법

    1. 문자열 값이나 경로 지정

       파이썬의 strftime() 형식이 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체됨

       `(upload_to='uploads/%Y/%m/%d/')`

       > time 모듈의 strftime()
       >
       > - time.strftime(format[, t])
       >
       > - 날짜 및 시간 객체를 문자열 표현으로 변환하는데 사용됨
       > - 하나 이상의 형식화된 코드 입력을 받아 문자열 표현을 반환

    2. 함수 호출

  - Model field option - `blank`

    기본값: False

    유효성 검사에서 사용됨(is_valid)

  - Model field option - `null`

    기본값: False

    True인 경우 django는 빈 값에 대해 DB에 NULL로 저장

    

    ※ 주의사항

    CharField, TextField와 같은 **문자열 기반 필드에는 사용하는 것을 피해야함**

    문자열 기반 필드에 True로 설정 시 '데이터 없음'에 "빈 문자열"과 "NULL" 2가지의 가능한 값이 있음을 의미하게 됨

    대부분의 경우 '데이터 없음'에 대해 두 개의 가능한 값을 갖는 것은 중복되는 것이며, Django는 NULL이 아닌 빈문자열을 사용하는 것이 규칙

  - blank & null 비교

    - blank

      validation-related

      유효성 검사에서 사용

    - null

      Database-related

      데이터베이스에 관여

    - 문자열 기반 및 비문자열 기반 필드 모두에 대해 null은 DB에만 영향을 미치므로, form에서 빈 값을 허용하려면 blank=True를 설정해야함

  

  - ImageField를 사용하기 위한 몇가지 단계

    1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
    2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정
    3. 업로드 된 파일의 경로는 django가 제공하는 'url'속성을 통해 얻을 수 있음

  - MEDIA_ROOT

    사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로

    django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음

    (실제 데이터베이스에 저장되는 것은 파일의 경로)

    ※ MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야함

  - MEDIA_URL

    MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL

    업로드된 파일의 주소를 만들어 주는 역할

    비어있지 않은 값으로 설정한다면 반드시 `/`로 끝나야함

    ※ MEDIA_URL는 STATIC_URL와 반드시 다른 경로로 지정해야함

  - 개발 단계에서 사용자가 업로드한 파일 제공하기

    설정 방법 공식 문서 참고

    (사용자가 업로드한 파일이 프로젝트에 업로드되더라도 실제로 사용자에게 제공하기 위해서는 업로드된 파일의 url이 필요하기 때문)



### 이미지 업로드(CREATE)

게시글 작성 form에 enctype 속성 지정

method는 FILES

{{ model클래스명.필드명.url }}

- form 태그 - enctype(인코딩) 속성

  1. multipart/form-data

     파일/이미지 업로드 시에 반드시 사용해야함(전송되는 데이터의 형식을 지정)

     `<input type="file">`을 사용할 경우에 사용

     (`accept='image/*'`는 modelform의 imagefield가 자동 설정)

- input 요소 - accept 속성

  입력 허용할 파일 유형을 나타내는 문자열

  파일을 검증하는 것은 아님(accept 속성 값이 image라 하더라도 비디오나 오디오 및 다른 형식 파일을 제출할 수 있음)



### 이미지 업로드(UPDATE)

- 이미지 수정하기

  하나의 데이터 덩어리(바이너리 데이터)이기 때문에 텍스트처럼 일부만 수정하는 것은 불가능

  새로운 사진으로 덮어씌우는 방식 사용

  

  조건문을 걸어서 `if article.image`

  이미지가 없이 작성된 게시글은 detail 페이지가 출력되지 않는 문제 해결

  image가 없는 게시글의 경우 출력할 이미지 경로가 없기 때문



### 이미지 Resizing

- 이미지 크기 변경하기

  실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업

  img tag에서 직접 사이즈를 조정할 수도 있지만(width와 height 속성 사용), 업로드 될 때 이미지 자체를 resizing하는 것을 고려하자

  (django-imagekit 라이브러리 활용)

  > 코드는 공식 문서 참고

- 원본 이미지를 재가공하여 저장(원본저장X, 썸네일O)

  기존 image field는 삭제

  (blank=True 추가)

- 원본 이미지를 재가공하여 저장(원본저장O, 썸네일O)

  기존 image field도 사용하고 추가로 field 작성
