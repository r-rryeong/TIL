# Vue 03(22.05.11)

### Vue Intro



state - data

state도 .vue에서 받아쓸때는 computed에 들어가야한다.(data에 x, 데이터를 받아쓰는 것이기 때문에 변화가 일어나면 안됨)

view - HTML

action - method



2. Mutation(변이) => commit

   state를 바꿈

3. Action => dispatch

   actions에 있는 함수안의 인자 context는 만능(state, getters, mutations에 모두 접근 가능)
   
4. Getters : 캐시 메모리에 미리 데이터를 준비해놓고 필요할 때마다 가져다 씀, return값 필요



v-for와 key(바인딩)는 세트!

mutations의 함수명은 모두 대문자 권장

push() - 추가 , splice() - 삭제

mutations의 함수는 actions로 한번더 감쌈(?), actions을 통해서 호출

유라 교수님 코드에 (todo) 붙히기

const commit = context.commit과 함수 인자로 { commit }을 받는 것은 같다.(key랑 value가 중복이기 때문. 맥가이버 칼에서 필요한 기능만 뽑아서 쓰는 느낌)



### d

