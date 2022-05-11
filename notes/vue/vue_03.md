# Vue 03(22.05.11)

### Vue Intro



state - data

view - HTML

action - method



2. Mutation(변이) => commit

   state를 바꿈

3. Action => dispatch

   actions에 있는 함수안의 인자 context는 만능(state, getters, mutations에 모두 접근 가능)



v-for와 key는 세트!

mutations의 함수명은 모두 대문자 권장

push() - 추가 , splice() - 삭제

mutations의 함수는 actions로 한번더 감쌈(?), actions을 통해서 호출

유라 교수님 코드에 (todo) 붙히기

const commit = context.commit과 함수 인자로 { commit }을 받는 것은 같다.(key랑 value가 중복이기 때문. 맥가이버 칼에서 필요한 기능만 뽑아서 쓰는 느낌)

