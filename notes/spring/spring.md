## Spring 소개

- Model2 Architecture : MVC Pattern
- Spring Web MVC : 기존 Servlet의 요청 분석, client 데이터 추출, 결과 페이지 이동 역할 수행
- Spring DI(Dependency Injection) : 객체 생성, 연동 역할 수행(factory 기능 포함)
- IoC(Inversion of Control;제어의 반전) : 제어를 개발자가 아닌 framework가 수행
- View Resolver : View 선택 역할 수행
- DB 연동 framework
  - Spring jdbc
  - MyBatis : sql 쿼리 생성 단계를 따로 빼서 query.xml 파일에서 수행
  - JPA
- Spring Framework의 장점
  - web을 자동화, 빠르게 개발 가능
  - 라이브러리가 쪼개져있어서 가볍게 사용할 수 있다.(경량 컨테이너)
  - Spring DI로 인해서 coupling이 낮아졌다. 유지보수성, 확장성 증가
- Spring Framework의 단점
  - 학습 필요, 시간 소요



## Container

- 스프링은 자바 객체를 담고 있는 컨테이너
  - 언제든지 스프링 컨테이너로부터 필요한 자바 객체를 불러와 사용 가능
- 스프링 컨테이너는 객체의 생성, 사용, 소멸에 해당하는 라이프사이클을 관리
  - 라이프사이클을 기본으로 애플리케이션 사용에 유용한 기능을 제공
- 기능
  - 라이프사이클 관리
  - Dependency 객체 제공
  - Thread 관리
  - 기타 애플리케이션 실행에 필요한 환경
- 필요성
  - 비즈니스 로직 외 부가적인 기능들이 독립적으로 관리되도록 하기 위함
  - 서비스 look up이나 Configuration에 대한 일관성을 갖기 위함
  - 서비스 객체를 사용하기 위해 개발자가 직접 Factory 또는 Singleton 패턴을 직접 구현하지 않아도 됨



## Spring Framework 구조

### Pojo(Plain old java object)

- 특정 프레임워크에 종속되지 않은 객체지향 원리에 충실한 자바 객체(프레임워크 내 특별한 객체를 상속하지 않음)
- 일반 자바 객체(이식성이 좋음)

> Spring의 특징

### IoC(Inversion of Control)

: 제어의 반전(사람이 제어하다가 기계가 제어한다는 뜻..)

- 스프링에서 객체의 생성과 생명주기를 관리하는 Spring Container 혹은 IoC Container가 존재한다.
- @component: Beans 생성(객체를 생성하면 IoC가 관리)

### DI(Dependency Injection)

  : 의존성 주입

- IoC 구현 방법 중 하나가 DI이다.
- @Inject: DI 구현(어노테이션을 이용해서 구현 가능)
  ⇒ 둘다 Container가 관리

### AOP(Aspect Oriented Programming, 관점지향 프로그래밍)

- 같은 기능을 여러개 쓰고 싶을 때, 여러 servlet에 적용하고 싶을 때
- 로그인 여부를 확인하는 모듈을 생성하여 특정 클래스의 함수에 적용하고 싶을 때
- 로그 출력

### PSA(Portable Service Abstraction)

- Mybatis 관련
- @tranjection



## Spring MVC 모델

### Model

- 컨트롤러로부터 데이터를 받아 로직을 처리
- Service는 비즈니스 로직, DAO는 DB로직, Java Beans는 로직을 처리한 후 반환되는 객체를 저장하는 역할로 또 다시 나눠진다.(DAO는 Data Access Object의 줄임말로 데이터베이스의 data에 접근하기 위한 객체이다.)
- Java Beans는 DTO나 VO를 만드는데 활용
- DTO(Data Transfer Object)는 로직을 가지지 않는 순수한 데이터 객체, 데이터를 전달하는 객체(바구니)
  - 오직 getter/setter 메서드 만을 갖는다.
  - setter를 삭제하고 불변객체로 만들 수 있다.
  - 
- VO(Value Object)는 DTO 객체의 값을 반환할 때 사용되는 객체, 값 그 자체를 의미하는 객체

### View

- 클라이언트에게 보낼 응답 페이지(vue, html, jsp...)

### Controller

- 클라이언트의 요청을 처리
- @Controller와 @RequestMapping을 활용하여 컨트롤러와 함수 단위의 매핑 가능
  - @Controller는 클래스에만, @RequestMapping은 클래스와 함수에 적용 가능

## client와 server

1. client에서 요청을 보낸다.
- HttpServletRequest, HttpServletResponse 객체 생성
2. server에서 DispatcherServlet을 호출 → HandlerMapping 호출
- servlet
  - servlet 하나는 controller 하나를 맡는다.
  - '요청을 받고 응답을 해주는 서블릿을 호출하는 서블릿(1개)'과 '모델을 호출하여 반환값을 받는 서블릿(여러개 일수도)'이 있다.
3. servlet 여러개 호출
4. servlet이 service 호출
5. service에서 dao 호출(mapper->mapper.xml, dao가 큰 개념)
6. DB 호출
7. service 반환
8. view에 응답(JSON 형태, postman안쓰고 swagger 사용, @ApiParam)

## Lombok 알아보기
- @Getter: getter 생성
- @Setter: setter 생성
> 마우스 우클릭 -> Refactor -> Delombok을 클릭하면 어노테이션이 작성해주는 코드를 볼 수 있음
- @ToString: 객체의 내용을 보여준다.
- @NoArgsConstructor: 인자없이 생성되는 생성자
> JPA에서 거의 필수
- @AllArgsConstructor: 객체가 가지고 있는 모든 필드를 인자로 받아서 생성
- @RequiredArgsConstructor: 필요한 인자만을 이용해서 생성자를 만든다.(일반적인 경우에는 @NoArgsConstructor와 같음, 변수에 @NotNull을 이용하면 필수값이 됨)
- @EqualsAndHashCode: equals 메서드와 hashcode 메서드를 오버라이딩하기 위해 사용
- @Data: @Getter, @Setter, @RequiredArgsConstructor, @ToString, @EqualsAndHashCode를 모두 선언한 것과 동일
- @Builder: @AllArgsConstructor와 비슷하게 객체를 생성하고 필드값을 주입해주는데, Builder의 형식으로 제공

## Spring Security
Security가 필요한 이유
- 웹사이트는 각종 서비스를 하기 위한 리소스와 서비스를 사용하는 유저들의 개인 정보를 가지고 있다. 이들 리소스를 보호하기 위해 일반적으로 웹사이트는 두가지 보안 정책을 설정해야 한다.
  - 서버 리소스
  - 유저들의 개인정보

## OAuth2
### CommonOAuth2Provider
아래 4개의 Provider에 대해 기본 정보들을 제공합니다.
- Google
- Github
- facebook
- OKTA
- naver
- kakao

### OAuth2User
- facebook, naver, kakao
- OAuth2User: UserDetails를 대체합니다.
- OAuth2UserService: UserDetailService를 대체합니다. 기본 구현체는 DefaultOAuth2UserService 입니다.

1. OAuth2 Provider(인증 제공자)
- Authentication Server(인증 서버)
  - 사용자 정보를 담고 있다.
- Resource Server(리소스 서버)
  - 사이트에 가입한 사용자 정보 
  > 리소스
  사용자가 위임한 개인정보
  프로바이더가 제공하는 서비스 정보
2. 인증을 위임한/인증 서비스를 이용하는 서비스
- Client Server, 3rd Party Server
- 우리 서버
3. 서비스 이용자
- Client
