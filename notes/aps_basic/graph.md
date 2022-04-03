## 그래프&백트래킹(APS 응용)

### 그래프 기본

- 그래프는 아이템들과 이들 사이의 연결 관게를 표현
- 그래프는 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료 구조
- |V|: 정점의 개수, |E|: 그래프에 포함된 간선의 개수
- |V|개의 정점을 가지는 그래프는 최대 |V|(|V|-1)/2 간선이 가능



### 그래프 탐색





### 서로소 집합들(Disjoint-sets)

- 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들. 교집합이 없다.
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. 이를 대표자라 한다.



- 상호배타 집합을 표현하는 방법

  - 연결 리스트
  - 트리

- 상호배타 집합 연산

  Make-Set(x)

  Make-Set(y)

  Union(x, y) (대표 원소)

  Find-Set(y)   (return x; y가 속한 집합의 대표원소)

- 상호 배타 집합 표현 - 트리

  Make-Set(a)~Make-Set(f) 각각이 대표 원소

  



### 최소 비용 신장 트리(MST)

그래프를 트리로 만든다. 최소비용으로 트리를 만들 수 있으면 MST라고 한다.

- prim 알고리즘

  정점을 기준으로 정렬

- kruskal 알고리즘

  간선을 기준으로 정렬

  (간선의 개수가 적을 때는 요게 유리함)

  비용이 낮은 것부터 오름차순으로 정렬 후, 낮은 것부터 선택, 싸이클 유무 확인(Find-set)

  

### 최단 경로
