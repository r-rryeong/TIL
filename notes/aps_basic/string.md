## 문자열(String)

### 문자열

- 오늘날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII형식을 사용한다

​	→ 인터넷이 전 세계로 발전하면서 국가간에 정보를 주고 받을 때 문제 발생

​		유니코드가 위의 보완책

- 유니코드

  다국어 처리를 위한 표준 마련

  유니코드는 다시 Character Set으로 분류

- big-endian, little endian

- 유니코드 인코딩(UTF: unicode transformation format)
  - UTF-8
  - UTF-16
  - UTF-32
  
- Python 인코딩

- Python에서의 문자열 처리

  `+`: (연결)문자열을 이어주는 역할

  `*`: (반복)수만큼 문자열이 반복

  - 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
  - 튜플과 같이 요소값을 변경할 수 없음(immutable)

- 문자열 비교

  `==`: 같은 값을 가졌는지 비교

  `is`: 같은 객체를 가졌는지 비교

- 실습

  str()함수를 사용하지 않고, itoa() 구현하기



### 패턴 매칭

- 고지식한 알고리즘(Brute Force)

  본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식

  ```python
  p = "is"
  t = "This is a book~!"
  M = len(p)
  N = len(t)
  
  der BruteForce(p, t):
      i = 0   # t의 인덱스
      j = 0   # p의 인덱스
      while j < M and i < N:
          if t[i] != p[j]:
              i = i - j
              j = -1
          i = j + 1
          j = j + 1
      if j == M :
          return i - M
      else:
          return -1
  ```

  → 최악의 경우 시간 복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 됨

  

- KMP 알고리즘(위의 알고리즘 시간 복잡도 보완)

  - 불일치가 발생한 텍스트의 앞 부분에 어떤 문자가 있는지 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행

  - 패턴을 전처리하여 배열 `next[M]`(불일치가 발생했을 경우 이동할 다음 위치)을 구해서 잘못된 시작을 최소화함
  - 시간 복잡도 : O(M+N)
  - 쉽게 말하자면 문자열이 불일치 할 때 탐색을 시작했던 위치의 다음 문자부터가 아닌 일정 부분을 건너뛸 수 있다고 가정하자. 건너뛴 후의 탐색 문자열의 앞 부분과 원본 문자열의 뒷부분이 일치해야한다 가 전제조건으로 성립해야함.(탐색 문자열의 접두사와 접미사 미리 계산)
  - 즉, 탐색 문자열의 앞부분과 원본 문자열의 뒷부분이 동일한 부분까지는 문자열 탐색을 건너뛸 수 있다!

  > http://whocouldthat.be/visualizing-string-matching/
  >
  > 패턴 이해 참고 사이트

  - LPS : 패턴 문자열에서 접두사와 접미사가 일치하는 최대 길이를 저장한 배열

  - LPS 연습 예시

    ```py
    input.txt
    5
    AAACAAAAB
    ABCAABCBA
    ACACAACACC
    ABCAABCACABACA
    ACACABACACACAB
    ```

    ```python
    output.txt
    #1 -1 0 1 2 0 1 2 3 3
    #2 -1 0 0 0 1 1 2 3 0
    #3 -1 0 0 1 2 3 1 2 3 4
    #4 -1 0 0 0 1 1 2 3 4 0 1 2 1 0
    #5 -1 0 0 1 2 3 0 1 2 3 4 5 4 5
    ```

    

- 보이어-무어 알고리즘

  - 오른쪽에서 왼쪽으로 이동, 뒤에서부터 비교

  - 비교 대상이 나의 패턴에 있는지 확인하고 있다면 그 자리수를 맞춰서 점프 후 확인

  - 비교 문자가 내 패턴 내에 존재하지 않는 경우 패턴 길이만큼 한꺼번에 점프

  - 꽤 복잡한 개념, 문제에 적용하려면 더 간단한 개념인 호스풀(horspool) 알고리즘을 사용

---------------------------------------------

- 참고

  문자열 암호화

  문자열 압축