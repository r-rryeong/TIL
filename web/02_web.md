## CSS layout

- CSS layout techniques

  - Display
  
  - Position
  
  - Float (1996)
  
  - **Flexbox** (2012)
  
  - Grid (2017)
  
  - 기타(Responsive Web Design)
  
    

### Float (알고는 있자! 잘안씀)

- CSS 원칙(Normal Flow)

  block은 div 태그, inline은 span 태그 주로 사용

- Float

  박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소(float된 블록 주변을 감쌈)들이 주변을 wrapping 하도록함.

  요소가 normal flow를 벗어나도록함.

  (인터넷 쇼핑몰에서 많이 활용하는 레이아웃)

- Float 속성

  - none: 기본값
  - left: 요소를 왼쪽으로 띄움
  - right: 오른쪽으로 띄움
  
- Clearing Float

  - Float는 Normal Flow에서 벗어사 부동상태이므로 이후 요소에 대해 Float 속성이 적용되지 않도록 Clearing이 필수적임
  - `::after`: 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
  - clear 속성 부여

- Float 정리

  Float는 레이아웃을 구성하기 위해 필수적으로 활용되었으나, 최근에는 Flexbox, Grid 등장과 함께 사용도가 낮아짐.

  Float 활용 전략 - Normal Flow에서 벗어난 레이아웃 구성

  - 원하는 요소들을 Float로 지정하여 배치
  - 부모 요소에 반드시 Clearing Float를 하여 이후 요소부터 Normal Flow를 가지도록 지정



### Flexbox

- **CSS Flexible Box Layout**

  - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

  - 축⭐

    - main axis: 정렬 기본방향(기본값: row)

    - cross axis: 교차 축

  - 구성 요소

    - Flex Container(부모 요소)

      flexbox 레이아웃을 형성하는 기본적인 모델

      Flex Item들이 놓여있는 영역

      display 속성을 flex 혹은 inline-flex로 지정

    - Flex Item(자식 요소)

      컨테이너에 속해 있는 컨텐츠

- Flexbox 축

  - flex-direction : row

  

- 왜 Flexbox를 사용해야할까?

  이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position.

  수직정렬, 아이템의 너비와 높이 혹은 간격 동일하게 배치하는 것이 더 수월함

- 활용 레이아웃

- Flex 속성

  1. **배치 설정**

  - flex-direction

    row, row-reverse, column, column-reverse

  - flex-wrap: 아이템이 컨테이너 밖으로 벗어나지 않도록 설정

    wrap: 넘치면 그 다음 줄로 배치

    nowrap: (기본값) 한줄에 배치
  
  - flex-flow: flex-direction과 flex-wrap의 shorthand(차례대로 작성)
  
  2. **공간 나누기**
  
  - justify-content: main axis를 기준으로 공간 배분
  
    flex-start, flex-end, center, space-between, space-around(아이템을 둘러싼 영역을 균일하게 분배), space-evenly(전체 영역에서 아이템 간 간격을 균일하게 분배)
  
  - align-content: cross axis를 기준으로 공간 배분(아이템이 한줄로 배치되는 경우 확인할 수 없음)
  
    flex-start, flex-end, center, space-between, space-around, space-evenly
  
  3. **정렬**
  
  - align-items: 모든 아이템을 cross axis 기준으로 정렬
  
    stretch(컨테이너를 가득 채움), flex-start, flex-end, center, baseline
  
  - align-self: 개별 아이템을 Cross axis 기준으로 정렬
  
    stretch, flex-start, flex-end, center

- Flex 기타 속성

  flex-grow: 남은 영역을 아이템에 분배

  order: 배치 순서

  

> flex로 만들 수 있는 10가지 레이아웃
>
> https://d2.naver.com/helloworld/8540176



## Bootstrap

- spacing

  | m      | p       |
  | ------ | ------- |
  | margin | padding |

  | t    | top         |
  | ---- | ----------- |
  | b    | bottom      |
  | s    | left        |
  | e    | right       |
  | x    | left, right |
  | y    | top, bottom |

  | class name | rem  |  px  |
  | :--------: | :--: | :--: |
  |    m-1     | 0.25 |  4   |
  |    m-2     | 0.5  |  8   |
  |    m-3     |  1   |  16  |
  |    m-4     | 1.5  |  24  |
  |    m-5     |  3   |  48  |

- color

- text



### ⭐Bootstrap Grid system(web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본요소
  - Column: 실제 컨텐츠를 포함하는 부분
  - Gutter: 칼럼과 칼럼 사이의 공간(사이 간격)
  - Container: Column들을 담고 있는 공간

- Bootstrap Grid system은 flexbox로 제작됨
- 12개의 column, 6개의 grid breakpoints !



class="container" - 좌우 공백 확보(가독성↑)

⭐"row" - 부모요소 안에 "col" 작성

⭐breakpoints

⭐nesting: 부모의 영역을 12등분한다.

offset: 

