### 함수

- 함수를 사용하는 이유

  복잡한 내용을 모르더라도 사용할 수 있도록(블랙박스)

  재사용성과 가독성 up , 유지보수 수월



### 함수 기초

- 함수의 정의

  - 함수(Function)

    특정한 기능을 하는 코드와 조각

    특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

  - 사용자 정의 함수

    구현되어 있는 함수가 없는 경우 사용자가 직접 함수를 작성 가능

- 함수 기본 구조

  - 선언과 호출(define & call)
  
    함수의 선언은 def 키워드 활용
  
    함수는 함수명()으로 호출
  
  - **입력(Input)**
  
  - 문서화
  
  - 범위
  
  - **결과값**
  
    동작 후에 return을 통해 결과값 전달(return 값이 없으면, None 반환)

​	` 0119.py` 참고



### 함수의 결과값(Output)

- 값에 따른 함수의 종류

  - Void function

    명시적인 return 값이 없는 경우, none을 반환하고 종료

  - Value returning function

    함수 실행 후, return문을 통해 값 반환

    return을 하면 **값 반환 후 함수가 종료**

> 주의
>
> return은 함수 안에서만 사용되는 키워드
>
> print는 출력을 위해 사용되는 함수
>
> REPL환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로 두 동작이 같은 것이라 착각할 수 있음

- 두개 이상의 값 반환

  아래 코드의 문제점은?

  ```python
  def m(x,y):
      return x - y
  	return x + y   # 사용 안됨~
  
  print(m(1,2))
  ```

  함수는 항상 단일한 값만을 반환. return문을 만나면 함수 종료

​	=> 반환 값으로 튜플 사용

```python
def minus_and(x, y):
    return x - y, x * y

y = minus_and(4, 5)
(-1, 20)
```

`02.rectangle.py` 



### 함수의 입력(Input)

- Parameter(매개변수)와 Argument(전달인자)

  Parameter: (이름)함수를 실행할 때, 함수 내부에서 사용되는 식별자

  Argument: (값)함수를 호출할 때 넣어주는 값

  - Argument

    필수 Argument: 반드시 전달되어야 하는

    선택 Argument: 값을 전달하지 않아도 되는 경우는 기본 값 전달

- Positional Arguments(위치인자)

  기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

- Keyword Arguments(키워드 인자)

  `03_add.py` 참고

  **주의**❗ 단, 키워드 인자 다음에 위치 인자가 올 수 없다

- Default Arguments Values(기본 인자값)

  : 함수를 정의할 때, 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않도록 함

  **주의**❗ 단, 기본 인자값을 가지는 인자 다음에 기본값이 없는 인자가 올 수 없다

  

- 정해지지 않은 여러개의 Arguments 처리

  `04_input_02.py` 참고

  - 가변 인자 리스트

    개수가 정해지지 않은 임의의 인자를 받기 위해서는 함수를 정의할 때 가변 인자 리스트 `*args`를 활용. tuple형태로 처리되며 매개변수에 `*`로 표현

  - 가변 키워드 인자

    정해지지 않은 키워드 인자들은 함수를 정의할 때 가변 키워드 인자 `**kwargs`를 활용

    dict 형태로 처리되며 매개변수에 `**`로 표현

- Keyword Arguments Packing/Unpacking

  `05_input_03.py` 참고

  ```
  # 이름(식별자)='값'
  ```


### 정리!

함수(input/output)

- input- 호출(위치, 키워드 )/ 정의(필수, 선택:기본값,여러개:tuple과 dictionary)
- output- 반드시 하나의 객체 반환(0은 none, 여러개는 tuple)



### 함수의 범위(Scope)

- 추상화

  내부에 어떤 코드가 작동하는지 우린 모름(블랙박스). 인풋을 넣으면 아웃풋이 나올 뿐

- 함수의 범위

  함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope

  `06_local_global.py` 참고

  - 전역 스코프(global scope): 코드 어디에서든 참조할 수 있는 공간
  - 지역 스코프(local scope): 함수가 만든 스코프로 함수 내부에서만 참조 가능
  - 전역 변수(global variable): 전역 스코프에 정의된 변수
  - 지역 변수(local variable): 로컬 스코프에 정의된 변수

- **이름 검색 규칙(Name Resolution)**

  파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장

  - LEGB Rule

    Local scope : 함수

    Enclosed scope : 특정 함수의 상위 함수

    Global scope : 함수 밖의 변수 혹은 import된 모듈

    Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

  

### 함수의 문서화

- Docstring(Document String)

  함수, 코드 설명

- Naming Convention

  - 좋은 함수와 parameter 이름을 짓는 방법

    상수 이름은 영문 전체를 대문자

  - 스스로를 설명

    함수의 이름만으로 어떠한 역할을 하는 함수인지 파악 가능해야함

  - 약어 사용 지양

    보편적으로 사용하는 약어 제외하고 되도록 약어 사용 지양



### 함수 응용

- map

  map(function, iterable)

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환

  - 활용 사례

    알고리즘 문제 풀이시 input을 바로 숫자로 활용하고 싶을 때

    ```python
    a = input().split()
    map(int, a)
    list(map(int,a))
    # 최종 코드
    n,m = map(int, input().split())
    print(n, m, type(n), type(m))
    ```

- filter

  filter(function, iterable)

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과가 True인 것들을 filter object에 반환

- zip

  zip(*iterables)

  복수의 iterable 객체를 모아 zip()

  결과는 튜플의 모음으로 구성된 zip object를 반환함

- lambda 함수

  lambda[parameter] : 표현식

  - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림

  `02.py` 참고

  

### 재귀 함수(recursive function)

자기 자신을 호출하는 함수

1개 이상의 **base case(종료되는 상황)**가 존재하고, **수렴하도록 작성**

- 반복문과 재귀 함수 비교

  - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수 사용
  - 코드가 더 직관적이고 이해하기 쉬운 경우가 있음
  - 재귀 호출은 변수 사용을 줄여줄 수 있음
  - 재귀 호출은 입력 값이 커질수록 연산 속도가 오래 걸림

--------------------------------------------------

### 모듈

- 모듈과 패키지

  모듈: 파이썬 파일 단위

  패키지: 여러 모듈의 집합

  라이브러리(library): 여러 패키지를 하나의 묶음으로

- 모듈과 패키지 불러오기

  - **import** module   # 책상 서랍에 있는 것들을 꺼내어는 함수
  - **from** modele **import** var, function, Class
  - **from** modele **import** *     # 전부를 가져옴
  - **from** package **import** module
  - **from** package.module **import** var, function, Class



### 파이썬 표준 라이브러리(PSL)

파이썬에 기본적으로 설치된 모듈과 내장함수

> https://docs.python.org/ko/3/library/index.html

- 파이썬 패키지 관리자(pip) 명령어

  pip list: 목록 정보 확인

  pip freeze: 패키지 정보 기록=> `requirements.txt`에 기록

  pip install: 구매 `-r requirements.txt`



### 사용자 모듈과 패키지

- 모듈 활용하기

- 패키지

- 패키지 만들기

  `패키지` 참고



### 가상환경

가상환경을 만들고 관리하는데 사용되는 모듈

- 가상환경 생성
