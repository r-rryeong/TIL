```
# 참고 Notion 주소
https://www.dongyeon1201.kr/c20f7d07-6f23-4134-ae8e-e730dc7b5af6
```

```
# 공개키 기반 인증 SSH 접속
ssh -i "개인키 경로" USER@IP
```

🐬Docker에서 Image란?

어떠한 개발 환경을 구축하기 위해 필요한 라이브러리 및 패키지를 모아 하나의 파일로 만든 것

Docker Image: 사용자가 base image를 사용하여 그 위에 프로그램, 라이브러리, 소스를 설치한 뒤 하나의 파일로 만든 것

🐬Docker에서 Container란?

이미지가 실행된 형태로써, 컨테이너 레벨에 저장되며 호스트와 이미지엔 아무런 영향을 주지 않고 Docker 엔진에서 독립적으로 실행된다.

> 비유
>
> base image: 글자를 한개도 파지 않은 목판
>
> docker image: 책을 찍어내기 위해 글자를 파낸 목판
>
> container: 목판을 사용하여 만든 책



👩‍💻현재 사용자 docker 명령어 사용 허용

기본적으로 root 권한을 사용하여(sudo 명령어) docker 명령어를 사용해야한다.

하지만 매번 명령어를 사용할 때마다 sudo를 입력하기 번거롭다.

(아래 명령어 입력 후 재접속해줘야함)

```
$ sudo usermod -aG docker $USER
```

