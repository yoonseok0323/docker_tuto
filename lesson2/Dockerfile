From python:3-alpine
# ubuntu는 무거운 tool이기에 위와 같은 방법으로 경량화 작업을 할 수 있다
#python3 설치할 필요가 없다.

ENV PORT 8080

WORKDIR /app

COPY . /app
# 해당 디렉터리에 위치한 모든 파일(main.py,requirements.txt)을 app에 복사

Run pip install -r requirements.txt
# API 설치



CMD ["python", "main.py"]
# CMD에서 python으로 main.py를 실행
