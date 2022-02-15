## 배열 2(Array2)

### ⭐2차원 배열

- 2차원 배열

  copy할 때 주의

- 배열 순회

  - 행 우선 순회

  - 열 우선 순회

  - 지그재그 순회

  ```python
  # 지그재그 공식
  array[i][j + (m-1-2*j) * (i % 2)]
  # -2j는 끝에서 끝으로 가는 것을 나타냄
  # (i % 2): 홀짝 판별
  
  # if ~ else로 하는 것이 가독성은 좋음
  for i in range(n):
      if i % 2 == 0:   # 짝수행
  ```

  - ⭐델타를 이용한 2차 배열 탐색⭐

  ```python
  for i in range(N):
      for j in range(N):
          di = [0, 1, 0, -1]
          dj = [1, 0, -1, 0]:
              for k in range(4):
                  ni = i + di[k]
                  nj = j + dj[k]
                  if 0 =< ni < N and 0 =< nj < M:
                      arr[ni][nj]
  ```

  - 전치행렬

  ```python
  # for문으로 나타내는 방법
  
  # zip으로 나타내는 방법
  ```

  

- 부분집합 합

  ```python
  ```

  

- 비트 연산자

  전기버스 문제를 비트 연산자를 이용해서 풀어보자

- 검색
  - 순차 검색
    - 정렬되어 있지 않은 경우
    - 정렬되어있는 경우
  - 이진 검색(Binary Search)



- 인덱스

- **선택 정렬(Selection Sort)**

  버블 정렬과 비교하여 정리!