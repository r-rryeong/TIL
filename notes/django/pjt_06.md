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

