## 문자열(String)

### 문자의 표현

- ASCII
- 확장 아스키



- 유니코드

  유니코드도 다시 Character Set으로 분류

- big-endian, little endian

- 유니코드 인코딩(UTF: unicode transformation format)
  - UTF-8
  - UTF-16
  - UTF-32
- Python 인코딩



### 패턴 매칭

- 고지식한 알고리즘

- KMP 알고리즘(위의 알고리즘 보완)

  > http://whocouldthat.be/visualizing-string-matching/
  >
  > 패턴 이해 참고 사이트

  LPS table 만들기 연습

- 보이어-무어 알고리즘

  오른쪽에서 왼쪽으로 이동, 뒤에서부터 비교

  비교 대상이 나의 패턴에 있는지 확인하고 있다면 그 자리수를 맞춰서 점프 후 확인

  비교 문자가 내 패턴 내에 존재하지 않는 경우 패턴 길이만큼 한꺼번에 점프

  꽤 복잡한 개념, 문제에 적용하려면 더 간단한 개념인 호스풀(horspool) 알고리즘을 사용