- Handling HTTP requests

  Django에서 HTTP 요청을 처리하는 방법

  1. Django shortcut functions
  2. view decorators

  - Django shortcut functions

    shortcuts functions 종류

    : render(), redirect(), get_object_or _404()

    - get_object_or _404()

      모델 manager인 objects에서 get()을 호출하지만, 해당 객체가 없을 경우 doesnotexist 예외 대신 http 404 raise

      get()의 경우 조건에 맞는 데이터가 없을 경우 예외를 발생

    > http 응답 상태 코드
    >
    >  mdn 문서 참고

  - Django view decorators

    어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 연장해주는 함수

    즉, 원본 함수를 수정하지 않으면서 추가 기능만을 구현할 때 사용