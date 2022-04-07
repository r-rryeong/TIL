### Form Class

우리는 지금까지 HTML form, input을 통해 사용자로부터 데이터를 받음

이렇게 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시해야함

이 과정을 모두 코드로 구현하는 것은 많은 노력이 필요함

Django는 이러한 작업과 반복 코드를 줄여준다!

- Django's forms

  - Form은 Django의 **유효성 검사** 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

  - Form과 관련한 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공하여 개발자로 하여금 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함

  - Django는 form에 관련된 작업의 아래 세 부분을 처리해 줌
    1. 렌더링을 위한 데이터 준비 및 재구성
    1. 데이터에 대한 HTML forms 생성
    1. 클라이언트로부터 받은 데이터 수신 및 처리

- Django 'Form Class'

  Django 내의 forms 라이브러리에서 파생된 Form 클래스를 상속받음

  form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러 메세지를 결정

- Form 선언하기

  $ from django import forms

  Model을 선언하는 것과 유사하며 같은 필드타입을 사용

  

- Form rendering options

  - as_p() : 각 필드가 `<p>`태그로 감싸져서 렌더링됨
  - as_ul() : `<li>`태그로 감싸져서 렌더링됨. `<ul>`태그는 직접 작성해야함
  -  as_table() : `<tr>`태그(테이블행)으로 감싸져서 렌더링됨. `<table>`태그는 직접 작성



- HTML input 요소 표현 방법 2가지

  - Form fields

    input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨
    
  - Widgets

    웹 페이지의 HTML input 요소 렌더링

    GET/POST 딕셔너리에서 데이터 추출

    widgets은 반드시 Form fielsd에 할당됨

    (attrs: CSS 적용)

  ※ 주의사항

  Form Fields와 혼동되어서는 안됨

  Form Fields는 input의 유효성 검사 처리

  widgets은 웹페이지에서 input 요소 단순 렌더링 처리(보여지는 부분)

>rendering fields
>
>https://docs.djangoproject.com/en/3.2/topics/forms/#rendering-fields-manually

>choicefields(디폴트 위젯:select)
>
>https://docs.djangoproject.com/ko/3.2/internals/contributing/writing-code/coding-style/#template-style

>Form fields
>
>https://docs.djangoproject.com/en/3.2/ref/forms/fields/

> widgets
>
> https://docs.djangoproject.com/en/3.2/ref/forms/widgets/



### ModelForm

Django Form을 사용하다 보면 Model에 정의한 필드를 유저로부터 입력받기 위해 Form에서 Modle 필드를 재정의하는 행위가 중복될 수 있음

Django는 Model을 통해 Form class를 만들 수 있는 ModelForm을 제공!

- ModleForm Class

  Model을 통해 Form Class를 만들 수 있다

  일반 Form class와 같은 방식으로 view에서 사용 가능

- ModleForm 선언하기

  forms 라이브러리에서 파생된 ModelForm 클래스 상속받음

  정의한 클래스 안에 meta클래스를 선언하고, 어떤 model을 기반으로 form을 작성할 것인지에 대한 정보를 meta클래스에 지정

  model, fields, (exclude) 정보 필요

  ※ 클래스 변수 fields와 exclude는 동시에 사용할 수 없음



- Meta class(정보의 정보 느낌; 부가설명)

  model의 정보를 작성하는 곳

  modelform을 사용할 경우 사용할 모델이 있어야 하는데 meta class가 이를 구성함
  
  - 해당 model에 정의한 field 정보를 form에 적용하기 위함
  
  > (참고)Inner Class
  >
  > 클래스 내에 선언된 다른 클래스
  >
  > 관련 클래스를 함께 그룹화하여 가독성 및 프로그램 유지 관리 지원(논리적으로 묶어서 표현)
  >
  > 외부에서 내부 클래스에 접근할 수 없으므로 코드의 복잡성을 줄일 수 있음
  
  >Meta 데이터
  >
  >'데이터에 대한 데이터'
  >
  >사진 촬영-사진 데이터-사진의 메타 데이터(촬영 시각, 렌즈 등)



ModelForm과 Form은 뭐가 더 좋고 나쁘고 할 것 없이 역할이 다르다!

ModelForm: 데이터 베이스 관련, 데이터를 저장   ex) 회원가입

Form: 데이터 베이스 관련 x, model 정보 가지고 있지 않음, 데이터를 저장할 필요없을 때  ex) 로그인

- ModelForm이 쉽게 해주는 것
  1. 모델 필드 속성에 맞는 html element를 만들어 주고
  2. 이를 통해 받은 데이터를 view함수에서 유효성 검사를 할 수 있도록 함



- create view 수정
  1. ModelForm을 이용해서 전달되는 request.POST 정보를 가지는 인스턴스를 생성
  2. 인스턴스의 유효성 검사
  3. DB에 저장(유효성검사를 통과하면)
  
- is_valid() method

  유효성 검사를 실행하고 데이터가 유효한지 여부를 boolean으로 반환

  데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공

  유효성 검사: 데이터베이스 각 필드 조건에 올바르지 않은 데이터가 서버로 전송되거나 저장되지 않도록 하는 것

- save() method

  Form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장

  ModelForm의 하위 클래스는 기존 모델 인스턴스를 키워드 인자 instance로 받아들일 수 있음

  - 이것이 제공되면 save()는 해당 인스턴스를 수정(UPDATE)
  - 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)

  Form의 유효성이 확인되지 않은 경우, save()를 호출하면 form.errors를 확인하여 에러 확인 가능



- create view 함수 구조 변경

  new 함수와 create함수는 같은 목적(CREATE)을 가지고 있지만 GET, POST 메서드 방식 차이 존재

  ⇒ 두 함수를 합치자

  context가 받는 form 형태는 두 가지로 나뉨. 첫 번째는 유효성 검사를 통과하지 못한 form(에러메세지 포함), 두 번째는 그냥 인스턴스로 받은 form

  끝나면 new의 흔적지우기,,,

> error 체크!
>
> noreversematch ⇒ 해당 template의 url 확인

- UPDATE

  CREATE 로직과 같다. but, 차이점 존재

  첫 번째는 인스턴스로 바로 불러옴.

  두 번째는 pk 사용, 데이터에서 정보를 찾아온다.

- forms.py 파일 위치

  app폴더 내부에 작성하자. 관리하기 편리함

  

### Rendering fields manually

>
>
>django bootstrap 5

- rendering fields manually

  form.필드명.요소

  