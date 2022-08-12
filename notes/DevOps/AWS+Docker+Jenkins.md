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



✔현재 호스트에 존재하는 Image 확인

```
$ docker images
```

❌특정 이미지 삭제

```
$ docker rmi [option] imagename [imagename... (여러 개 삭제 시) ]
```

🦼Container 생성

```
$ docker create [option] [imagename]:[tag]
```



✔Container 목록 확인

(정지된 컨테이너 목록까지 확인하고 싶은 경우 -a 추가)

```
$ docker ps [옵션]
```

🛑Container 중지

```
$ docker stop [container name OR container ID]
```

❌Container 삭제(컨테이너가 중지된 상태여야 한다.)

```
# 컨테이너 이름 or ID로 중지
$ docker rm [container name OR container ID]

# 컨테이너 강제 삭제
$ docker rm -f [container name OR container ID]

# 모든 컨테이너 삭제
$ docker container prune
```



### ❗에러

1. Error: Could not find or load main class org.gradle.wrapper.GradleWrapperMain

   ```
   $ gradle wrap
   ```

   wrapper 폴더 내의 gradle-wrapper.jar, gradle-wrapper.properties를 지우고 다시 깔아준다.

2. ```
   Step 11/12 : COPY ./default.conf /etc/nginx/conf.d/default.conf
   COPY failed: file not found in build context or excluded by .dockerignore: stat default.conf: file does not exist
   ```

   ```
   # Dockerfile 수정
   COPY --from=build-stage /app/build /usr/share/nginx/html
   ```

3. 
