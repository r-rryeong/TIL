## stack_2

### 계산기

- 문자열 수식 계산의 일반적 방법

  step1. 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용)

  (중위표기법: 연산자를 피연산자의 가운데 표기하는 방법)

  step2. 후위 표기법의 수식을 스택을 이용하여 계산

  (후위표기법: 연산자를 피연산자 뒤에 표기하는 방법)

  

- 중위표기식을 후위표기식으로 변환하는 방법1

  수식의 각 연산자를 **우선순위**에 따라 괄호를 사용하여 다시 표현

  → 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동

  → 괄호 제거

- 중위표기식을 후위표기식으로 변환하는 방법2(스택 이용)

  입력 받은 중위 표기식에서 토큰을 읽는다

  → 토큰이 피연산자이면 토큰을 출력

  → 토큰이 연산자(괄호 포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않으면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후, 토큰의 연산자를 push한다. (만약 top에 연산자가 없으면 push)

  → 토큰이 ')'이면 스택 top에 왼쪽 괄호'('가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력. '('를 만나면 pop만 하고 출력하지 않는다

  → 중위 표기식에 더 읽을 것이 없다면 중지하고, 있다면 다시 반복

  → 스택에 남아있는 연산자를 모두 pop하여 출력
  
- 후위 표기법의 수식을 스택을 이용하여 계산

  피연산자를 만나면 스택에 push

  → 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push

  → 수식이 끝나면, 마지막으로 스택을 pop하여 출력



### 백트래킹

: 해를 찾는 도중 막히면(해가 아니면) 되돌아가서 다시 해를 찾는 기법

- 미로찾기 알고리즘

- 백트래킹과 DFS의 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 어이질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄임(가지치기)
  
    가지치기(pruning): 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.
  
  - DFS가 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단하여 일반적으로 경우의 수가 줄어듬

### 부분집합

- 어떤 집합의 원소 개수가 n일 경우, 부분집합의 개수는 2^n개 이다

- 백트래킹 기법으로 powerset을 구해보자

  n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용

  여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    
    if k == input:
        process_solution(a, k)   # 답이면 원하는 작업을 한다
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0]*NMAX
backtrack(a, 0, 3)
```

- 백트래킹을 이용하여 순열 구하기

  ```python
  def backtrack(a, k, input):
      global MAXCANDIDATES
      c = [0]*MAXCANDIDATES
      
      if k == input:
          for i in range(1, k+1):
              print(a[i], end=' ')
          print()
      else:
          k += 1
          ncandidates = construct_candidates(a, k, input, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k, input)
  def construct_candidates(a, k, input, c):
      in_perm = [False]*NMAX
      
      for i in range(1, k):
          in_perm[a[i]] = True
          
      ncandidates = 0
      for i in range(1, input+1):
          if in_perm[i] == False:
              c[ncandidates] = i
              ncandidates += 1
      return ncandidates
  ```

  

### 분할 정복

- 거듭제곱

  ```python
  def Power(Base, Exponent):
      if Base == 0:
          return 1
      result = 1    # Base^0은 1이므로
      for i in range(Exponent):
          result *= Base
      return result
  ```

  

### 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬(합병정렬과 동일?)
- 다른점1: 퀵정렬은 분할할 때, 기준 아이템(pivot)중심으로 이보다 작은 것은 왼쪽, 큰 것은 오른쪽에 위치시킨다
- 다른점2: 각 부분 정렬이 끝난 후, 합병정렬은 합병이란 후처리가 필요하지만 퀵정렬은 필요로 하지 않는다

```python
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
def partition(a, begin, end):
    pivot = (begin + end)//2
    L = begin
    R = end
    while L < R:
        while L<R and a[L]<a[pivot]:
            L += 1
        while L<R and a[L]>=a[pivot]:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
```

