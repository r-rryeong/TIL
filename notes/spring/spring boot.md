### Spring 표기법(강의 기준)

json 파일(Body)은 스네이크 케이스

클래스명은 파스칼 케이스

변수, 함수명은 카멜 케이스

### 단축키

- alt + Enter: 수행할 action을 보여줌(import, replace,...)
- ctrl + space: method 자동완성(arrow method)
- 

# 🌱TIL

- var: 타입 추론하는 단축된 약어(자바11부터 추가)

- dependency

- throws: 예외던지기

### API

- port번호 변경하기
  
  application.properties에서 server.port=9090 입력

- @RestController: 해당 Class는 REST API 처리하는 Controller

- @RequestMapping(): URI를 지정해주는 Annotation
  
  ex) @RequestMapping("/api") 를 입력하면 URI는 'http://localhost:8080/api'

- @JsonNaming(value = ) : @JsonProperty()와 다르게 해당 클래스에 일괄적으로 모든 naming 룰을 적용

- @PathVariable: URL Path Variable Parsing

- ResponseEntity<>: 객체에 대해 httpstatus code 지정

- @Controller : return 하는 리소스를 찾게됨

- @ResponseBody : body를 그대로 내려줌

- @JsonInclude(): null 이나 비어있는 필드를 표시하지 않을 수 있음

### CRUD

- GET: 리소스 취득, R

- POST: 리소스 생성, 추가, C

- PUT: 리소스 갱신, 생성, C / U

- DELETE: 리소스 삭제, D

### AOP

- Join Point: 타겟 객체가 구현한 인터페이스의 모든 메서드는 조인 포인트가 된다.
- Aspect: AOP의 기본 모듈, Advice + Pointcut
- Pointcut: Advice를 적용할 타겟의 메서드를 선별하는 정규표현식

> **레스토랑 비유를 사용한 설명**
> 
> 외식 할 때 메뉴를보고 선택할 수있는 몇 가지 옵션이 표시됩니다. 메뉴에있는 항목 중 하나 이상을 주문할 수 있습니다. 그러나 실제로 주문하기 전까지는 “식사 기회”일뿐입니다. 주문하고 웨이터가 테이블로 가져 오면 식사입니다.
> 
> Joinpoint는 메뉴의 옵션이고 Pointcut은 사용자가 선택하는 항목입니다.
> 
> Joinpoint는 코드 내에서 측면을 적용 할 수있는 기회입니다. 그 기회를 잡고 하나 이상의 Joinpoint를 선택하고 그것에 측면을 적용하면 Pointcut이 있습니다.

- Bean은 Component와 다르게 클래스에 붙힐 수 없다. 메서드에 가능

- @Target(): 애노테이션을 부착할 수 있는 타입 지정

- @Retention(): 해당 애노테이션이 언제까지 유지될 수 있는지 알려주는 애노테이션

- Thread.sleep(): 실행 중인 스레드를 잠시 멈춘다

### object mapper

```
Text JSON -> Object
Object -> Text JSON

controller req json(text) -> object
response object -> json(text)


object -> text
// object mapper get method를 활용한다.
objectMapper.writeValueAsString(변수);

text -> object
// object mapper는 default 생성자를 필요로 한
objectMapper.readValue(바꿀 변수명, 바꿀 타입);
```

- jackson-databind (2.12.1)

> JSON Validator 사이트

- @JsonProperty(): 해당 변수는 요청 보낼 때 특정 이름으로 매칭시킬 것이다.
  
  변수명이 카멜케이스, 스네이크케이스도 아닌 약어를 가질 때도 사용

- JsonNode: Jackson 라이브러리에서 제공하는 JSON을 표현하기 위한 추상 클래스

- ArrayNode: Json의 node 중에 배열 형태로 값이 들어가있는 노드에 접근하기 위한 클래스

- convertValue: object를 원하는 type으로 바꿔서 파싱하기 위한 메서드

### Spring Boot Annotations

| Annotation             | 의미                                             |
| ---------------------- | ---------------------------------------------- |
| @SpringBootApplication | Spring boot application으로 설정                   |
| @Controller            | View를 제공하는 controller로 설정                      |
| @RestController        | REST API를 제공하는 controller로 설정                  |
| @RequestMapping        | URL 주소를 맵핑(원하는 Http method 지정해야함)              |
| @GetMapping            | Http GetMethod URL 주소 맵핑                       |
| @PostMapping           | Http PostMethod URL 주소 맵핑                      |
| @PutMapping            | Http PutMethod URL 주소 맵핑                       |
| @DeleteMapping         | Http DeleteMethod URL 주소 맵핑                    |
| @RequestParam          | URL Query Parameter 맵핑                         |
| @RequestBody           | Http Body를 Parsing 맵핑                          |
| @Valid                 | POJO Java class의 검증                            |
| @Configration          | 1개 이상의 bean을 등록 할 때 설정                         |
| @Component             | 1개의 Class 단위로 등록할 때 사용                         |
| @Bean                  | 1개의 외부 library로부터 생성한 객체를 등록 시 사용(Class에는 사용X) |
| @AutoWired             | DI를 위한 곳에 사용                                   |
| @Qualifier             | @AutoWired 사용시 bean이 2개 이상일 때 명시적으로 사용         |
| @Resource              | @AutoWired + @Qualifier 의 개념으로 이해              |
| @Aspect                | AOP 적용시 사용                                     |
| @Before                | AOP 메소드 이전 호출 지정                               |
| @After                 | AOP 메소드 호출 이후 지정 (예외 발생 포함)                    |
| @Around                | AOP 이전/이후 모두 포함 (예외 발생 포함)                     |
| @AfterReturning        | AOP 메소드의 호출이 정상일 때 실행                          |
| @AfterThrowing         | AOP시 해당 메소드가 예외 발생시 실행되도록 지정                   |

### Validation

프로그래밍에 있어서 가장 필요한 부분. 특히 Java에서는 null값에 대해서 접근하려고 할 때 null pointer exception이 발생함으로, 이러한 부분을 방지하기 위해서 미리 검증하는 과정을 Validation이라고 한다.

1. 검증해야 할 값이 많은 경우 코드의 길이가 길어진다.
2. 구현에 따라서 달라질 수 있지만 Service Logic과의 분리가 필요하다
3. 흩어져 있는 경우 어디에서 검증을 하는지 알기 어려우며, 재사용의 한계가 있다.
4. 구현에 따라 달라질 수 있지만, 검증 Logic이 변경되는 경우 테스트 코드 등 참조하는 클래스에서 

| @Size               | 문자 길이 측정                | Int Type 불가         |
| ------------------- | ----------------------- | ------------------- |
| @NotNull            | null 불가                 |                     |
| @NotEmpty           | null, "" 불가             |                     |
| @NotBlank           | null, "", " " 불가        |                     |
| @Past               | 과거 날짜                   |                     |
| @PastOrPresent      | 오늘이거나 과거 날짜             |                     |
| @Future             | 미래 날짜                   |                     |
| @FutureOrPresent    | 오늘이거나 미래 날짜             |                     |
| @Pattern            | 정규식 적용                  |                     |
| @Max                | 최대값                     |                     |
| @Min                | 최소값                     |                     |
| @AssertTrue / False | 별도 Logic 적용             | method가 is로 시작해야한다. |
| @Valid              | 해당 object validation 실행 |                     |

① gradle dependecies

​    implementation 'org.springframework.boot:spring-boot-starter-validation'

② bean validation spec

​    https://beanvalidation.org/2.0-jsr380/

③ 핸드폰번호 정규식

​    "``^\\d{2, 3}-\\d{3, 4}-\\d{4}$``"

- ResponseEntity: 사용자의 HttpRequest에 대한 응답 데이터를 포함하는 클래스(HttpStatus, HttpHeaders, HttpBody를 포함)
- BindingResult: 검증 오류가 발생할 경우 오류 내용을 보관하는 객체

### Custom Validation

1. AssertTrue / False와 같은 method 지정을 통해 Custom Logic 적용 가능
2. ConstraintValidator를 적용하여 재사용이 가능한 Custom Logic 적용 가능
- @Constraint: annotation을 Bean Validation Constraint로 만들어 주는 annotation

### Exception 처리

Web Application의 입장에서 바라보았을때, 에러가 났을 때 내려줄 수 있는 방법은 많지 않다.

1. 에러 페이지
2. 4XX Error or 5XX Error
3. Client가 200 외에 처리를 하지 못할 때는 200을 내려주고 별도의 에러 메세지 전달

| @ControllerAdvice | Global 예외 처리 및 특정 package / Controller 예외처리 |
| ----------------- | ------------------------------------------- |
| @ExceptionHandler | 특정 Controller의 예외처리                         |

- int와 integer: int는 null로 초기화할 수 없고 산술연산 가능, integer는 산술 연산이 불가능하지만 null 값 처리가 용이하다.

- e.getlocalizedmessage와 e.getMessage: 오류 처리를 수행하는 동안 catch 블록에서 발생하는 메시지를 가져오기 위해 두 가지 메서드를 사용. getlocalizedmessage는 현지 언어로 예외 이름을 반환한다.

- @MethodArgumentNotValidException: @Valid 애너테이션으로 데이터를 검증하고, 해당 데이터에 에러가 있을 경우 예외 메세지를 JSON으로 처리하는 ExceptionHandler 처리 방법

- @RestController: @Controller에 @ResponseBody가 결합된 annotation. @Controller와 달리 @RestController는 컨트롤러 클래스의 각 메서드마다 @ResponseBody를 추가할 필요가 없다.

- getRejectValue(): 필드 오류, 즉 특정 필드 값을 거부하는 이유를 캡슐화한다.

### Filter-Interceptor

Filter란 Web Application에서 관리되는 영역으로써 Spring Boot Framework에서 Client로 부터 오는 요청/응답에 대해서 최초/최종 단계의 위치에 존재하며, 이를 통해서 요청/ 응답의 정보를 변경하거나, Spring에 의해서 데이터가 변환되기 전의 순수한 Client의 요청/ 응답 값을 확인할 수 있다.

유일하게 ServletRequest, ServletResponse의 객체를 변환할 수 있다.

주로 Spring Framework에서는 request/response의 Logging 용도로 활용하거나, 인증과 관련된 Logic들을 해당 Filter에서 처리한다.

이를 선/후 처리함으로써, Service business logic과 분리 시킨다.

- Lombok: annotation을 통해 getter, setter, toString 모두 생성 가능

- Slf4j: 로깅에 대한 추상 레이어를 제공하는 인터페이스의 모음. System.out을 사용하지 않아도 console에 보기 좋게 log가 찍히는 것을 볼 수 있다.

- Servlet: 웹 프로그래밍에서 클라이언트 요청을 처리하고 처리 결과를 클라이언트에 전송하는 기술. 자바로 구현된 CGI(Common gateway Interface)
  
  - 클라이언트의 요청에 대해 동적으로 작동하는 웹 어플리케이션 컴포넌트
  - html을 사용해서 요청에 응답한다
  - Java thread를 통해 동작한다
  - MVC패턴 중 Controller로 이용된다

### DB

- Optional: Optional<T>는 null이 올 수 있는 값을 감싸는 Wrapper 클래스

- 추상 클래스: 추상 클래스란 말 그대로 추상적으로 밖에 그려지지 않은 클래스라고 한다. 즉, 클래스가 전체적인 구성을 다 가지지 못한 채 설계만 되어있는 클래스이다. 추상클래스로 인스턴스를 생성할 수 없다. 추상 클래스는 상속을 통해서 자식 클래스에 의해 완성이 된다. 그래서 추상 클래스는 자체로는 제 기능을 다하지는 못하지만, 새로운 기능을 정의하는데 있어서 바탕이 될 수 있다.

### 0720 스터디

> VueAPI 프로젝트 참고

mapper와 .xml파일을 연결하는데 properties에서 미리 dto를 인식하도록 연결해놓음

@RestController를 사용하면 @ResponseBody를 사용하지 않음(알아서 처리)

@Autowired는 서버가 실행될때 class를 다 긁어모아서 주입해줌

ResponseEntity<?>나 ResponseEntity<Map<String, Object>> 나 같다.

HttpSession: token을 가져올 때 사용

throws로 예외처리를 해주면 controller에서 모아서 잡아줌(try, catch)
** 작성 순서**
Dto -> Controller -> Service(service interface, service class) -> Mapper

### SecurityConfig 설정
- @EnableWebSecurity: 웹보안 활성화를 위한 annotation, WebSecurityconfigureAdapter를 상속하는 설정 객체에 붙혀주면 SpringSecurityFilterChain에 등록된다.
- Form Login 인증
  1. Client에서 Get 방식으로 Home Url 자원접근 요청
  2. Server에서는 인증된 사용자만 접근가능하다고 판단해 인증이 안되면 로그인 페이지로 리다이렉트
  3. Client는 로그인페이지의 username/password 입력하여 Post 방식으로 인증 시도
  4. Server에서는 Session ID 생성후 인증결과를 담은 인증 토큰(Authentication) 생성 및 저장
  5. Client에서 /home 접근요청 시 세션에 저장된 인증 토큰으로 접근 및 인증 유지


## 💡에러 해결

❗`Identify and stop the process that's listening on port 8080` 에러

첫번째 방법,

1단계: 명령 프롬프트를 사용하여 Windows에서 프로세스 ID 찾기

ex) netstat -ano | findstr 8080

2단계: 명령 프롬프트를 사용하여 프로세스 종료

ex) taskkill /F /PID 19788

두번째 방법,

application.properties파일에서 server.port=9090 입력

(port 번호를 바꾸자)
