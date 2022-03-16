## 트리

### 트리

- 한 개 이상의 노드로 

### 이진 트리

자식이 두개뿐인 트리구조

- 완전 이진 트리

  왼쪽부터 채워진 트리

- 이진트리-순회(traversal)

  순회: 트리의 노드들을 체계적으로 방문하는 것

  - 전위 순회 (노드의 왼쪽에 점을 찍고 따라가면 편리함)
  - 중위 ( 노드의 아래에 점을 찍고 따라가면 편리함)
  - 후위(노드의 오른쪽에 점을 찍고 따라가면 편리함)

  전위 순회 알고리즘

  ```python
  def preorder_traverse(T):
      if T:
          dosomething(T)
          preorder_traverse(T.left)
          preorder_traverse(T.right)
  ```

  

### 이진탐색 트리

```python
c = 5    # 정점 c의 조상찾기
anc = []
while par[c] != 0:
    anc.append(par[c])
    c = par[c]
print(*anc)
```



### 힙

- 힙(Heap)
  - 

```python
# 최대힙

def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2
tree = [0]*101
last = 0
```

- 힙 연산 - 삽입
- 힙 연산 - 삭제
- 