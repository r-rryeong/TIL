### Form Class

- Django's forms

  - Form은 Django의 **유효성 검사** 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

  - Form과 관련한 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공하여 개발자로 하여금 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함

  - Django는 form에 관련된 작업의 아래 세 부분을 처리해 줌
    1. ㅇㅇ

- Django 'Form Class'

- Form rendering options

  - as_p() : p 태그로 감싸준다 <p>
  - as_ul() : li 태그로 감싸준다
  - as_table() : tr 태그로 감싸준다

- HTML input 요소 표현 방법 2가지

  - Form fields

    input에 

>
>
>https://docs.djangoproject.com/en/3.2/topics/forms/#rendering-fields-manually

>choices 확인
>
>django coding style(문서)

>Form fields 문서 참고
>
>https://docs.djangoproject.com/en/3.2/ref/forms/fields/

> widgets 문서 참고
>
> https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
>
> attrs : CSS 적용

### ModelForm

Form에서 Modle 필드를 재정의하는 행위가 중복될 수 있음

- Meta class(정보의 정보 느낌; 부가설명)

  (참고)Inner Class

  model, fields, (exclude) 정보 필요



modelform과 form은 뭐가 더 좋고 할 것없이 역할이 다르다

modelform: 데이터 베이스 관련, 

form: 데이터 베이스 관련 x, model 정보 가지고 있지 않음, 데이터를 저장할 필요없을 때(로그인 할 때)

- 모델폼이 쉽게 해주는 것
  1. 모델 필드 속성에 맞는 html element를 만들어 주고
  2. 이를 통해 받은 데이터를 view함수에서 유효성 검사를 할 수 있도록 함

error : noreversematch

-> 해당 템플릿 url 체크



- create view 수정
  1. modelform을 이용해서 전달되는 request.POST 정보를 가지는 인스턴스를 생성
  2. 인스턴스의 유효성 검사
  3. DB에 저장한다(유효성검사를 통과하면)
- 

### Rendering fields manually

>
>
>django bootstrap 5