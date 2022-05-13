# Vue 01 (22.05.04)

## Intro





p. 68 오타

hidden → none



- v-model

  HTML의 input요소와 data를 한몸으로 만들어버림



methods : data를 바꾸는 로직 위주(setter 함수들)

computed : data를 통한 값을 얻음(getter 함수들)



watch는 명령형, vue에서 우리가 선호하는 것은 선언형

거의 쓰지 않음. computed 사용

(watch 공식문서 참고)

❓watch와 method의 차이점



function자리에 화살표함수가 들어가면 안되지만 function 안에 화살표함수가 들어가는건 function의 this를 그대로 물려받기때문에 사용이 가능합니다

물려받기보다는 화살표함수에 this자체가 없어서 상위 함수의 this 를 찾아간다는 느낌



watch

사용할 일 x



![image-20220504173903910](vue_01.assets/image-20220504173903910.png)



----------------------

### summary

vue.js란?

SPA

CSR, SSR 각각의 장점과 단점

바닐라 JS와 Vue.js 비교

MVVM Pattern



⭐Quick Start of Vue.js



Vue 인스턴스

syntax



⭐template syntax

v-text, v-html 비교

v-show, v-if 비교

v-for

v-on, v-bind

(디렉티브 실습문서)

v-model(trim)

⭐computed

computed & methods & watch

filter

⭐Lifecycle Hooks