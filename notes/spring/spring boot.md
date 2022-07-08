### Spring 표기법(강의 기준)

json 파일(Body)은 스네이크 케이스

클래스명은 파스칼 케이스

변수, 함수명은 카멜 케이스



### 단축키

- alt + Enter: 수행할 action을 보여줌(import, replace,...)



# 🌱TIL

- var: 타입 추론하는 단축된 약어(자바11부터 추가)
- dependency
- throws: 예외던지기



**AOP**

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



**object mapper**

- jackson-databind (2.12.1)

> JSON Validator 사이트

- @JsonProperty()
- JsonNode: Jackson 라이브러리에서 제공하는 JSON을 표현하기 위한 추상 클래스

- ArrayNode: Json의 node 중에 배열 형태로 값이 들어가있는 노드에 접근하기 위한 클래스
- convertValue: object를 원하는 type으로 바꿔서 파싱하기 위한 메서드



**Spring Boot Annotations**

| Annotation             | 의미                                                         |
| ---------------------- | ------------------------------------------------------------ |
| @SpringBootApplication | Spring boot application으로 설정                             |
| @Controller            | View를 제공하는 controller로 설정                            |
| @RestController        | REST API를 제공하는 controller로 설정                        |
| @RequestMapping        | URL 주소를 맵핑(원하는 Http method 지정해야함)               |
| @GetMapping            | Http GetMethod URL 주소 맵핑                                 |
| @PostMapping           | Http PostMethod URL 주소 맵핑                                |
| @PutMapping            | Http PutMethod URL 주소 맵핑                                 |
| @DeleteMapping         | Http DeleteMethod URL 주소 맵핑                              |
| @RequestParam          | URL Query Parameter 맵핑                                     |
| @RequestBody           | Http Body를 Parsing 맵핑                                     |
| @Valid                 | POJO Java class의 검증                                       |
| @Configration          | 1개 이상의 bean을 등록 할 때 설정                            |
| @Component             | 1개의 Class 단위로 등록할 때 사용                            |
| @Bean                  | 1개의 외부 library로부터 생성한 객체를 등록 시 사용(Class에는 사용X) |
| @AutoWired             | DI를 위한 곳에 사용                                          |
| @Qualifier             | @AutoWired 사용시 bean이 2개 이상일 때 명시적으로 사용       |
| @Resource              | @AutoWired + @Qualifier 의 개념으로 이해                     |
| @Aspect                | AOP 적용시 사용                                              |
| @Before                | AOP 메소드 이전 호출 지정                                    |
| @After                 | AOP 메소드 호출 이후 지정 (예외 발생 포함)                   |
| @Around                | AOP 이전/이후 모두 포함 (예외 발생 포함)                     |
| @AfterReturning        | AOP 메소드의 호출이 정상일 때 실행                           |
| @AfterThrowing         | AOP시 해당 메소드가 예외 발생시 실행되도록 지정              |



**Validation**

프로그래밍에 있어서 가장 필요한 부분. 특히 Java에서는 null값에 대해서 접근하려고 할 때 null pointer exception이 발생함으로, 이러한 부분을 방지하기 위해서 미리 검증하는 과정을 Validation이라고 한다.

1. 검증해야 할 값이 많은 경우 코드의 길이가 길어진다.
2. 구현에 따라서 달라질 수 있지만 Service Logic과의 분리가 필요하다
3. 흩어져 있는 경우 어디에서 검증을 하는지 알기 어려우며, 재사용의 한계가 있다.
4. 구현에 따라 달라질 수 있지만, 검증 Logic이 변경되는 경우 테스트 코드 등 참조하는 클래스에서 

| @Size               | 문자 길이 측정              | Int Type 불가 |
| ------------------- | --------------------------- | ------------- |
| @NotNull            | null 불가                   |               |
| @NotEmpty           | null, "" 불가               |               |
| @NotBlank           | null, "", " " 불가          |               |
| @Past               | 과거 날짜                   |               |
| @PastOrPresent      | 오늘이거나 과거 날짜        |               |
| @Future             | 미래 날짜                   |               |
| @FutureOrPresent    | 오늘이거나 미래 날짜        |               |
| @Pattern            | 정규식 적용                 |               |
| @Max                | 최대값                      |               |
| @Min                | 최소값                      |               |
| @AssertTrue / False | 별도 Logic 적용             |               |
| @Valid              | 해당 object validation 실행 |               |

① gradle dependecies

​	implementation 'org.springframework.boot:spring-boot-starter-validation'

② bean validation spec

​	https://beanvalidation.org/2.0-jsr380/

③ 핸드폰번호 정규식

​	"``^\\d{2, 3}-\\d{3, 4}-\\d{4}$``"



- ResponseEntity: 사용자의 HttpRequest에 대한 응답 데이터를 포함하는 클래스(HttpStatus, HttpHeaders, HttpBody를 포함)
- BindingResult: 검증 오류가 발생할 경우 오류 내용을 보관하는 객체




## 💡에러

❗`Identify and stop the process that's listening on port 8080` 에러

첫번째 방법,

1단계: 명령 프롬프트를 사용하여 Windows에서 프로세스 ID 찾기

ex) netstat -ano | findstr 8080

2단계: 명령 프롬프트를 사용하여 프로세스 종료

ex) taskkill /F /PID 19788



두번째 방법,

application.properties파일에서 server.port=9090 입력

(port 번호를 바꾸자)





## ❓질문

```
// JSON 내려주기
// req -> object mapper -> object -> method -> object -> object mapper -> json -> response
```

