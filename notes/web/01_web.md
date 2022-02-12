## HTML(Hyper Text Markup Language)

- 현재의 웹표준

  W3C --> WHATWG

  > caniuse 사이트

- Hyper Text

  텍스트에 하이퍼링크가 포함

- Markup Language

  태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- 웹 페이지를 작성(구조화)하기 위한 언어

  web의 뼈대를 만들기 위한 언어!



### HTML 기본구조

> alt + b 키로 html 페이지 열기

- html : 문서의 최상위 요소

- head : 문서 메타데이터 요소

  문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

  일반적으로 브라우저에 나타나지 않는 내용

- body : 실제 화면 구성과 관련된 내용

```
<!DOCTYPE html>   # 해당 문서가 html5로 구성되어 있음
<html lang="ko">
<head>

<body>

</html>
```

- head 예시

  - `<title>`: 브라우저 상단 타이틀
  - `<meta>`: html 문서의 정보를 담당
  - `<link>`: 외부 리소스 연결 요소(CSS파일, favicon 등)
  - `<script>`: 스크립트 요소 (jave script 시간에 다시 학습)
  - `<style>`: CSS 직접 작성

- DOM(Document Object Model) 트리 구조

  - body (부모요소)

    - h1 (자식요소)

    - ul (자식요소)

      h1과 ul은 형제요소

  - html은 2칸 띄워쓰기

- 요소(element)

  요소는 태그와 내용으로 구성되어 있다

  ```
  <h1>contents</h1>
  # 여는 태그와 닫는 태그
  ```

  - 태그는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의

  - 내용이 없는 태그들

    (br, hr, img, input, link, meta)

  - 요소는 중첩될 수 있음

  - 열림과 닫힘 태그의 쌍 구분할 것

    오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

- 속성(attribute)

  열리는 태그에 속성을 작성!(닫히는 태그에 작성하면 작동x)

  속성명과 속성값으로 구성

  ```
  <a 속성명="속성값"></a>   # 하이퍼링크를 넣는 tag
  # 쌍따옴표 사용!공백 No!
  ```

  - 태그에 부가적인 정보를 설정할 수 있음
  - 모든 요소는 속성을 가질 수 있음
  - 속성 이름과 값이 하나의 쌍으로 존재
  - 태그별로 사용할 수 있는 속성은 다르다(몇개는 공통적으로 사용할 수 있음)

- HTML Global Attribute

  모든 HTML요소가 공통으로 사용할 수 있는 대표적인 속성

  `id`: 유일한 고유 식별자 지정 

  `class`: 공백으로 구분된 해당 요소의 클래스의 목록

  --> 위 두 개는 식별자

  `data-*`: 사용자 정의 데이터를 저장

  `style`: 해당 요소를 꾸밀 때

  `title`: 요소에 대한 추가 정보 지정

  `tabindex`: 탭 순서

  > mdn tabindex 사이트

- 시맨틱 태그(영역을 구분하기 위한 태그)

  - HTML5에서 의미론적 요소를 담은 태그의 등장

    기존 영역을 의미하는 div태그를 대체하여 사용

    구조화, 명시적 표현가능 --> 가독성 up, 유지보수 수월

  - 대표적인 태그 목록

    `header`

    `nav`: 상단 메뉴(내비게이션)

    `aside`: 사이드에 위치한 공간

    `section`: 문서의 일반적인 부분, 컨텐츠의 그룹을 표현

    `article`: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역

    `footer`: 문서 전체나 섹션의 푸터(마지막 부분)

  - Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음



### HTML 문서 구조화

- 텍스트 요소

  - a 태그

  `<a></a>`: 하이퍼링크 생성

  - b 태그(bold)

  `<b></b>`: 굵은 글씨 요소

  `<strong></strong>`: 굵은 글씨 요소(의미적요소(굵게)가 추가된 시맨틱 태그)

  `<i></i>`: 기울임

  `<em></em>`: 기울임(시맨틱 태그)

  `<br>`: 텍스트에 줄 바꿈 생성

  `<img>`: 이미지 표현

  `<span></span>`: 의미없는 인라인 컨테이너

- 그룹 컨텐츠

  `<p></p>`: 하나의 문단

  `<hr>`: 수평선

  `<ol></ol>`: 순서가 있는 리스트

  `<ul></ul>`: 순서가 없는 리스트

  `<pre></pre>`: HTML에 작성한 내용을 그대로 표현

  `<blockquote></blockquote>`: 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨

  `<div></div>`: 의미없는 블록 레벨 컨테이너

  

- table

  table의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>` 요소를 활용

  `thead`: tr > th

  `tbody`: tr > td

  `tfoot`: tr > td

  `tr`로 가로줄을 구성하고 내부에는`th` 혹은 `td`로 셀 구성

  - `colspan`, `rowspan` 속성을 활용하여 셀 병합
  - `<caption>`을 통해 표 설명 또는 제목을 나타냄

- form(Django 굉장히 자주 사용)

  `<form>`은 데이터를 서버에 제출하기 위한 영역

  - `<form>` 기본속성

    **action**: form을 처리할 서버의 URL

    method: form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)

    enctype:  method가 post인 경우 데이터의 유형

    - application/x-ww-form-urlencoded : 기본값
    - multipart/form-data : 파일 전송시

- input

  - 다양한 입력을 받을 수 있게끔 다양한 위젯이 제공됨

  - `<input>`대표 속성

    name: form control에 적용되는 이름(이름/값 페어로 전송됨)

    value: form control에적용되는 값(이름/값 페어로 전송됨)

    required(필수입력), readonly, autofocus(커서 깜빡임), autocomplete(자동완성), disabled(비활성화) 등 <-- 단일 속성

  > mdn input 사이트

- input label
  - label을 클릭하여 input 자체에 초점을 맞출 수 있음
  - `<input>`에 id속성을, `<label>`에는 for 속성을 활용하여 상호 연관 시킴
  
- input 유형 - 일반

  일반적으로 입력을 받기 위해 제공되며 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음

  - text: 일반 텍스트 입력
  - password: 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email: 이메일 형식이 아닌 경우 form 제출 불가
  - number: min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file: accept 속성을 활용하여 파일 타입 지정 가능

- input 유형 - 항목 중 선택

  - 일반적으로 label을 사용하여 내용을 작성하여 항목 중 선택할 수 있는 input을 제공

  - 동일 항목에 대해서는 name을 지정하고 선택된 항목에 대한 value를 지정해야함

    `checkbox`: 다중 선택

    `radio`: 단일 선택

- input 유형 - 기타

  - 다양한 종류의 input을 위한 picker를 제공

    `color`: color picker

    `data`: data picker

  - hidden input을 활용하여 사용자가 입력을 받지 않고 서버에 전송되어야 하는 값을 설정

    `hidden`: 사용자에게 보이지 않는 input



## CSS(Cascading Style Sheets)

- CSS

  스타일을 지정하기 위한 언어

  선택하고 스타일을 지정한다.

  - CSS 기본문법 ⭐

  ```
  h1 {    # 선택자(selector)
  color: blue;
  font-size: 15px;   # 속성(property):값(value)
  }
  # 매 줄 끝에 세미콜론 작성!
  ```

  - 선택자를 통해 스타일을 지정할 HTML요소 선택
  - 중괄호 안에 속성과 값, 하나의 쌍으로 선언
  - 속성(property)은 어떤 스타일 기능을 변경할지 결정, 값은 어떻게 스타일 기능을 변경할지 결정

>선택자 연습 사이트
>
>https://flukeout.github.io/

- CSS 정의 방법

  - 인라인(inline) : 해당 태그에 직접 style 속성 활용

  - 내부 참조 : `<style></style>`태그 내부에 CSS 문법 적용

    --> 위의 두 방법은 유지보수 어려움, 테스트 시에 사용(또는 간단한 style 적용)

  - **외부 참조(link file) - 분리된 CSS 파일 **: 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기

    --> 하나의 CSS파일로 여러 개의 HTML파일을 바꿀 수 있다.

> 주로 사용하는 속성 위주로 기억하자!

- CSS 개발자 도구

  style : 해당 요소에 선언된 모든 CSS

  computed : 해당 요소에 최종 계산된 CSS



## ⭐CSS Selectors

- 선택자 유형⭐
  - 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  - 결합자
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
  
  - 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 속성 선택자



- 선택자 정리
  - 요소 선택자: HTML 태그를 직접 선택
  - 클래스 선택자: 마침표(.)로 시작되며, 해당 클래스가 적용된 항목을 선택
  - id 선택자: #문자로 시작하며, 해당 아이디가 적용된 항목을 선택, 단일 id를 사용하는 것을 권장
  - 전체 선택자
- CSS 적용 우선순위⭐
  1. 중요도 : `!important` 0순위 (사용시 주의)
  2. 우선순위 : 인라인 > id(#) > class(.), (속성, pseudo-class) > 요소, pseudo-element > 전체(*)
  3. CSS 파일 로딩 순서 :  가장 마지막이 우선순위가 높다

> CSS selector 우선순위 사이트

- CSS 상속

  CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

  - 상속 되는 것 예시

    Text 관련 요소(font, color, text-align) 등

  - 상속 되지 않는 것 예시

    Box model 관련 요소(width, height, margin, padding 등)
    
    position 관련 요소(position, top/right/bottom 등) 등

> mdn에서 확인하기



## CSS 기본 스타일

- 크기 단위

  - 픽셀

    모니터 해상도의 한 화소인 '픽셀' 기준

    픽셀의 크기는 변하지 않기 때문에 고정적인 단위

  - %

    백분율 단위

    가변적인 레이아웃에서 자주 사용

  - em(배수)

    (바로 위 부모 요소에 대한)상속의 영향을 받음

  - rem(root)

    **상속 영향 받지 않음**

    최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

  - viewport

    웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠 영역(디바이스 화면), viewport를 기준으로 상대적인 사이즈 결정

    vw, vh, vmin, vmax

- 색상 단위

  - 색상 키워드

    대소문자 구분x

  - RGB 색상

    `#` 16진수 표기법

    rgb() 함수형 표기법

  - HSL 색상

    색상, 채도, 명도를 통해 특정 색 표현

  - a는 alpha(투명도)



## Selectors 심화

- 결합자

  - 자손 결합자(띄워쓰기로 표현)

    selectorA 하위의 모든 selectorB 요소

  - 자식 결합자(`>`로 표현)

    selectorA 바로 아래의 selectorB 요소

  - 일반 형제 결합자(`~`로 표현)

    selector A의 형제 요소 중 뒤에 위치하는 selector B 요소를 모두 선택

  - 인접 형제 결합자(`+`로 표현)

    selectorA의 형제 요소 중 바로 뒤에 위치하는 selector B 요소를 선택



## CSS Box model

- CSS 원칙

  모든 HTML요소는 네모(박스모델)이고, 위에서 아래로, 좌에서 우로 쌓인다.(Normal Flow;기본흐름)

- Box model

  - content: 글이나 이미지 등 요소의 실제 내용
  - padding: 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
  - border: 테두리 영역
  - margin: 테두리 바깥의 외부 여백 배경색을 지정할 수 없다

- **Box-sizing**⭐

  - 기본적으로 모든 요소의 box-sizing은 content-box

    padding을 제외한 순수 contents 영역만을 box로 지정

  - 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px로 보는 것을 원함 - 이 경우, box-sizing을 border-box로 설정



## CSS Display

- display에 따라 크기와 배치가 달라진다.

- 대표적으로 활용되는 display

  - display: block

    줄 바꿈이 일어나는 요소

    화면 크기 전체의 가로 폭을 차지한다

    블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

  - display: inline

    줄 바꿈이 일어나지 않는 행의 일부 요소

    content 너비만큼 가로 폭을 차지한다.
    
    width, height, margin-top, margin-bottom을 지정할 수 없다
    
    상하 여백은 line-height로 지정

- 블록 레벨 요소와 인라인 레벨 요소

  - 대표적인 블록 레벨 요소

    div / ul, ol, li / p / hr / form 등

  - 대표적인 인라인 레벨 요소(text 관련 요소)

    span / a / img / input, label / b, em , i, strong 등

- 속성에 따른 수평 정렬

  - margin-right:auto; / text-align:left;
  - margin-left:auto; / text-align:right;
  - margin-right:auto;margin-left:auto; / text-align:center;

- display

  - display : inline-block
  
    block과 inline 레벨 요소의 특징을 모두 가짐
  
  - display : none
  
    해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  
    이와 비슷한 hidden은 해당 요소가 공간은 차지하나 화면에 표시되지 않음



## CSS position

- CSS position

  - 문서 상에서 요소 위치를 지정

  - static: 모든 태그의 기본 값(기준 위치)

    일반적인 요소의 배치 순서에 따름(좌측 상단)

    부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨

  - relative⭐

    : 상대 위치(내자리 유지), normal flow 유지

  - absolute⭐

    : 절대 위치(내자리x), normal flow 벗어남

    static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
  
  - fixed: 스크롤에서 항상 같은 곳에 위치   ex) 광고창
  
  > mdn position
  
  