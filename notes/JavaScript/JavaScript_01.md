### JavaScript 기초

- 브라우저

  웹 브라우저

  URL로 

- JavaScript의 필요성

  브라우저 화면을 동적으로 만들기 위함

  브라우저를 조작할 수 있는 **유일한 언어**

- 브라우저에서 하는 일

  - DOM 조작

    파싱(Parsing)

    문서(document)

  - BOM

    인터넷 브라우저(window)

    브라우저의 창을 지칭

    자바스크립트가 브라우저와 소통하기 위한 모델

- JavaScript core





### ECMA Script

- ECMA



### 세미클론

선택적으로 사용 가능

수업에서는 세미클론 쓰지 않을 것



### 코딩 스타일 가이드

- 코딩 스타일 가이드

  - 코딩 스타일의 핵심은 합의된 원칙과 일관성

  - 다양항 자바스크립트 가이드

    수업에서는 Airbnb Style Guide를 중심으로 진행할 예정

    

### 변수와 식별자

- 식별자 정의와 특징

  식별자는 변수를 구분할 수 있는 변수명을 말함

  식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작

- 식별자 작성 스타일

  - 카멜 케이스(calmelCase, lower-camel-case)

    변수, 객체, 함수에 사용

  - 파스칼 케이스(PascalCase, upper-camel-case)

    클래스, 생성자에 사용

  - 대문자 스네이크 케이스(SNAKE_CASE)

    상수에 사용

    상수: 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미

- 변수 선언 키워드(let, const)

  - let :
  - var : (안쓴다고 생각)



### 데이터 타입

- 종류

  자바스크립트의 모든 값은 특정한 데이터 타입을 가짐

  크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨



### 연산자





### 조건문

- if

  들여쓰기를 안해줘도 실행이 되지만 쓰도록 하자

- switch

  switch로 동작되는 것은 if 문으로도 작성할 수 있음

  복잡한 조건문인 경우는 if 문보다 switch문이 더 간단하게 작성할 수도 있음



### 함수

- 함수 in JavaScript

  - 참조 타입 중 하나로써 function 타입에 속함
  - JavaScript 

- Spread operator

  파이썬의 언패킹 생각



오타 - 132p. 화살표, 괄호 생략됨

for Each 제외하고 다른 메서드는 콜백 필수

- reduce

  [, 초기화 설정값] - 생략 가능

- ES6

  ⭐구조 분해 할당



### this 정리

roiem 문서 참고



### Lodash



> https://lodash.com/



```html
 // 1. 해당 코드를 template string 을 활용하여 리팩토링하시오.
    const name = 'Tom'
    console.log('Hi, my name is ' + `${name}`)

    // 2. 해당 코드를 arrow function 으로 리팩토링하시오.
    add = (x, y) => x + y

    square = x => x ** 2
```

