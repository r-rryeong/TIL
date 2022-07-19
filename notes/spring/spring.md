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
