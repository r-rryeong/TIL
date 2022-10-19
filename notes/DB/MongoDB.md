# MongoDB

- 개념

  - Database

    MongoDB에서 사용하는 데이터베이스의 가장 큰 단위

  - Collection

    Database의 하위에 속하는 개념

    (테이블 같은 개념)

  - Field

    filed가 모여서 하나의 컬렉션을 구성

    (컬럼과 같은 개념)

  - Document

    (row와 같은 개념)

  - BSON

    BSON은 JSON 형태의 문서를 바이너리 형태로 인코딩한 바이트 문자열이다.

    인코딩과 디코딩하는 과정이 필수이기에 이를 수행하는 서비스가 필요하다.

    애플리케이션과 MongoDB 데이터베이스 서버를 연결하는 드라이버는 주어진 문서를 Insert하거나, 쿼리할 때 그 문서를 서버에 보내기 전에 BSON으로 인코딩하는 역할을 담당한다.

    디코딩 또한 드라이버의 역할이며, 데이터베이스 서버에서 내려준 BSON 형태의 바이너리 데이터를 드라이버가 디코딩하여 데이터를 요청한 서버로 보낸다.

    - 특징
      - 문서 자체의 여백을 줄여 효율적으로 데이터 저장 공간을 절약하는 경량형태이다. 따라서 네트워크를 통해 데이터를 전달하고 표현하는 방식에 적합하다.
      - BSON 데이터 형태가 C언어의 데이터 형태를 사용하는 덕분에 인코딩, 디코딩 속도가 빠르다.
      - 문자열 값이 길이를 접두사로 붙이는 기능이 있어 문자열의 끝을 빠르게 파악한다. 데이터를 탐색하는데 도움이 된다.



### MongoDB 사용하기

```
# 공식문서
- shell로 접속하기
https://www.mongodb.com/docs/mongodb-shell/run-commands/
- springboot에서 사용하기
https://www.mongodb.com/compatibility/spring-boot
```



- Springboot 연동 및 테스트

```
# 참고 포스팅
https://sangmaeng.tistory.com/m/25
https://velog.io/@tekies09/SpringBoot-%EC%97%90%EC%84%9C-mongoDB-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0
```

