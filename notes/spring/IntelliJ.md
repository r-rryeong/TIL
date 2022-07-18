## 인텔리제이 단축키

### 단축키 기본Ⅰ

- 프로젝트 창 포커스: Alt + 1

- ESC: 에디터 창으로 돌아오기

- Space: 프로젝트 창 미리보기

- 에디터 창 키우기: ctrl + shift + F12

- 에디터 창 이동: ctrl + tab

- 새 파일 생성
  
  - 에디터에서: ctrl + alt + Insert
  - 프로젝트 창에서: alt + Insert

- 커서 이동
  
  - 단어별 이동: ctrl + ←→
  - 라인 시작/끝 이동: home, end
  - 페이지 위/아래: page up, page down

- 선택 확장/축소: ctrl + W, ctrl + shift + W

- 주석 처리
  
  - 한줄 주석: ctrl + /
  - 블록 주석: shift + ctrl + /

- 인덴트
  
  - 인덴트: tab
  - 인덴트 취소: shift + tab

- 자동 인덴트: ctrl + alt + I

- 사용처 찾기
  
  - 찾기: alt + F7
  - 빠른 찾기: ctrl + B

- 파일 검색
  
  - 찾기: ctrl + F
  - 찾은 결과 이동: F3, shift + F3

- 경로내 검색: ctrl + shift + F

- 전체 검색: shift 2번

- 최근 파일 열기: ctrl + E

### 단축키 기본Ⅱ

- Live template
  
  - psvm: public static void main(String[] args) {}
  - sout: System.out.println();
  - ctrl + J

- 퀵픽스: alt + enter

- 코드 이슈 별로 이동: F2, shift + F2

- Import 최적화: ctrl + alt + O

- 코드 생성: alt + Ins

- 메소드 자동완성
  
  - override: ctrl + o
  - implement: ctrl + I

- 터미널 창: Alt + F12

- 구문 완성: shift + ctrl + enter

- 대체하기
  
  - 파일 내 대체: ctrl + R
  - 경로 내 대체: ctrl + shift + R

- Run anything: ctrl 2번

- 실행
  
  - 에디터 실행: ctrl + shift + F10
  - 실행: shift + F10

- 종료: ctrl + F2

- 라인 수정
  
  - 복사: ctrl + D
  - 삭제: ctrl + y

- 파라미터 정보: ctrl + P

- Quick Definition: ctrl + shift + I

- Quick Document: ctrl + Q

- 기능(action)찾기: shift + ctrl + A

> Help → Keymap Reference 참고

💡한글 깨짐 현상 해결

1. File - Settings에 들어가서 File Encoding 메뉴에 들어간다.
   
   Global Encoding과 Project Encoding, Properties Feils 모두 UTF-8로 변경

2. Help - Edit Custom VM Option 메뉴에 들어간다.
   
   ```
   -Dfile.encoding=UTF-8
   -Dconsole.encoding=UTF-8
   ```
   
   위의 문구를 추가해준다.