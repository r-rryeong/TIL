- 문제풀이 과정의 목표

  아이디어(규칙성) 구현 → 알고리즘(템플릿을 익히고 연습하자)

  그림을 그려보면서 이해하기(시각적)

  

  문제풀이는 구현 중심으로 접근(파이썬을 먼저 생각하는게 아닌)

- 문제풀이

  많이 풀어야한다!

  - 문제 읽기(빨리 읽는 연습)

  - 접근방법 구상(사람x, 프로그램이 푸는 방법)

    - 완전히 새로운 문제는 없다. 이전에 풀었던 문제와 유사한지, 특정 자료구조 적용, 전형적인 알고리즘 적용가능한지 체크

    - 유형/규칙성을 발견하기 힘들다면

      가능한 모든 경우를 처리하면서 풀이가능한지 체크

      전체문제가 아닌 일부분을 나누거나, 단계를 나누어 접근

      반대로 접근하는 경우 체크

  - 핵심코드 손코딩 : 시각적(arr, 범위, 반복)

  - 코드구현

  - 디버깅 및 개선

- 문제풀이 연습

  - 기본기는 탄탄하게

    실수없는 **2차원 배열** 사용, **다중 루프제어**

    가장 효율적인, 짧은, 멋있는 코드보다 기본적인 반복/조건을 빈틈없이 구현

    ⭐**손코딩**: 사용하는 주요 배열, 범위, 핵심코드를 시각적으로 설계하고 접근

  >1시간 동안 찾지 못한 디버깅은 싹 지우고 새로 시작하자
  >
  >이미 머리속에 문제는 들어와있을 것
  >
  >죽어가는 내 문제를 살릴 수 있는 골든타임은 1시간

  - 나만의 환경/루틴에서 안정적으로 구현

    TC 입력파일, A4용지, 풀이 순서

    익숙한 이름: 입력받는 변수, 선언한 변수 등

    함수호출, 조건, 반복, break 등 익숙한 방법으로 구현

---------------------------

- BFS 기본틀

  ```python
  def bfs(si, sj, ei, ej):
      q = []    # 초기화
      visited[[0] * N for _ in range(N)]
      
      q.append([si, sj])
      visited
  ```

  