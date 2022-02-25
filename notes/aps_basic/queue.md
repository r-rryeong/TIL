## 큐(Queue)

- 특성

  스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

  (큐의 뒤에서는 삽입만 하고, 앞에서는 삭제만 이루어지는 구조)

- 선입선출구조(FIFO: First In First Out)

  머리(front): 저장된 원소 중 첫 번째 원소(또는 삭제된 위치)

  꼬리(rear): 저장된 원소 중 마지막 원소

  - 기본연산

    삽입: enQueue

    삭제: deQueue

  - 주요 연산

    enQueue(item)

    deQueue()

    createQueue(): 공백 상태의 큐를 생성

    isEmpty(): 큐가 공백상태인지 확인

    isFull(): 큐가 포화상태인지 확인

    Qpeek(): 큐의 앞쪽에서 원소를 삭제없이 반환하는 연산

- 연산 과정

- 선형큐

  : 1차원 배열을 이용한 큐

  큐의 크기 = 배열의 크기

  front: 저장된 첫 번째 원소의 인덱스

  rear: 저장된 마지막 원소의 인덱스

  - 상태 표현

    초기 상태: front = rear = -1(0앞에 -1을 의미)

    공백 상태: front == rear

    포화 상태: rear == n-1 (배열의 마지막 인덱스)

- 삽입: enQueue(item)

  