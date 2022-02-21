## 배열 2(Array2)

### ⭐2차원 배열

- 2차원 배열

  copy할 때 주의

- 배열 순회

  - 행 우선 순회
  - 열 우선 순회

  ```python
  for j in range(m):
      for i in range(n):
          arr[i][j]
  ```

  - 지그재그 순회

  ```python
  # 지그재그 공식
  arr[i][j + (m-1-2*j) * (i % 2)]
  # -2j는 끝에서 끝으로 가는 것을 나타냄
  # (i % 2): 홀짝 판별
  
  # if ~ else로 하는 것이 가독성 좋음
  for i in range(n):
      for j in range(m):
          arr[i][j + (m-1-2*j) * (i%2)]
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
                  if 0 <= ni < N and 0 <= nj < N:
                      arr[ni][nj]
  ```

  - 전치행렬

  ```python
  # for문으로 나타내는 방법
  
  # zip으로 나타내는 방법
  col_arr = list(zip(*arr))
  ```




### 부분집합 생성

- 부분집합의 합

- 비트 연산자

  (전기버스 문제를 비트 연산자를 이용해서 풀어보자)

  `&`: 비트 단위로 and 연산을 한다

  - i & (1<<j): i의 j번째 비트가 1인지 아닌지를 검사

  `|`: 비트 단위로 or 연산을 한다

  `<<`: 피연산자의 비트 열을 왼쪽으로 이동시킨다

  - 1<<n:2^n 즉, 원소 n개일 경우의 모든 부분집합의 수를 의미

  `>>`: 피연산자의 비트 열을 오른쪽으로 이동시킨다

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):  # 부분집합의 개수
    for j in range(n):   # 원소의 수만큼 비트 비교
        if i & (1<<j):   # i의 j번째 비트가 1인 경우
            print(arr[j], end = ', ')
    print()
print()
```



- 검색

  저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

  - 순차 검색(Sequential Search)
    - 정렬되어 있지 않은 경우

    ```python
    def sequentialSearch(a, n, key):
        i = 0
        while i < n and a[i] != key:
            i += 1
        if i < n :
            return i
        else:
            return -1
    ```

    - 정렬되어있는 경우

    

### 이진 검색(Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법(자료가 정렬된 상태여야함)

```python
def binarySearch(a, N, key):
    s = 0
    e = N-1
    while s <= e:
        middle = (s + e) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            e = middle - 1
        else:
            s = middle + 1
    return False
```

- 재귀 함수 이용



### 선택 정렬(Selection Sort)

버블 정렬과 비교하여 정리!

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 주어진 리스트 중에서 최소값을 찾고 그 값을 리스트의 맨 앞에 위치한 값과 교환한다. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복

```python
def selectionSort(a, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1, N):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
```



### 셀렉션 알고리즘(Selection Algorithm)

저장되어 있는 자료부터 k번째로 큰 혹은 작은 원소를 찾는 방법

최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다

- 과정

  정렬 알고리즘을 이용하여 자료 정렬하기

  원하는 순서에 있는 원소 가져오기

```python
def select(arr, k):
    for i in range(k):
        minidx = i
        for j in range(i+1, len(arr)):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr[k-1]
```

