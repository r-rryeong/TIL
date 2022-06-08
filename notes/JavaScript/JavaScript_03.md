# JavaScript 03(22.05.02)

### AJAX

- AJAX란?

  서버와 통신하기 위해 XMLHttpRequest 객체를 활용

- XMLHttpRequest 객체

  이름과 달리 XML뿐만 아니라 모든 종류의 데이터를 받아올 수 있음

  생성자 :



### Asynchronous JavaScript

- 동기식

  순차적, 직렬적 Task 수행

- 비동기식

  XMLHttpRequest 요청(비동기 처리)

  병렬적 Task 수행

  요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐

- 왜 비동기(Asynchronous)를 사용하는가?

  "사용자 경험"(UX)

  동기식 코드라면 데이터를 모두 불러온 뒤 앱이 실행됨

  - 즉, 데이터를 모두 불러올 때까지 앱이 멈춘 것처럼 보임
  - 코드 실행을 차단하여 화면이 멈추고 응답하지 않는 것 같은 사용자 경험을 제공

  비동기식 코드라면 데이터를 요청하고 응답받는 동안, 앱 실행을 함께 진행함



- Concurrency model

  2. Web API

     시간 관련, 

  3. Task Queue
  
  4. Event Loop



> event loop 참고
>
> 'javascript event loop visualizer' 검색



> 흐름 정리
>
> Axios ⇐ Promise ⇐ callback ⇐ Asynchronous ⇐ Event Loop ⇐ single thread



### [참고] async & await

(promise를 이쁘게 적은것, 함수로 묶는 작업)

(promise로 이루어진 코드만 리팩토링 가능)

해당 함수 맨 앞에 async 라는 키워드로 표시 남긴다

함수 블록 내부에, 비동기로 동작하는 함수들을 찾아서 앞에 await를 남긴다



------------------------------

5월 3일 실습 정리

좋아요 버튼을 누리면 page 새로고침 → JS로 preventDefault →  (form의 기본동작을 막았기 때문에)요청이 되지 않음 → axios를 통해 요청 → 좋아요가 눌린 건지 응답 data 갱신 → .then() → DOM 조작 → page 새로고침 없이 좋아요 동작