# flask
Python Web Framework

* 웹 서비스를 개발하기 위한 파이썬 웹 마이크로 프레임워크
* 최소한의 규약, 데이터베이스 기능의 확장

# 1. flask 설치하기

### 로컬 환경에서 가상 환경 만들기
* 가상 환경(venv) 모듈로 로컬 환경에 가상 환경을 작성 - 파이썬에 표준 탑재된 가상 환경용 모듈, 프로젝트별로 독립된 파이썬 패키지군 설치 가능
<pre><code>python3 -m venv venv
</code></pre>

### 가상 환경 활성화하기
* 가상 환경을 생성 후 활성화하여 패키지를 설치 가능하도록 한다.
<pre><code>source venv/bin/activate
</code></pre>

### 가상 환경 비활성화하기
* 가상 환경 사용을 중단한다.
<pre><code>deactivate
</code></pre>

### 플라스크 설치하기
<pre><code>pip install flask
</code></pre>

### 플라스크가 의존하는 패키지
* click - 명령어 라인용 프레임워크, 플라스크의 커스텀 명령어 사용
* itsdangerous - 데이터의 정합성 확보(안전하게 데이터 서명), 플라스크의 세션이나 쿠키를 보호
* Jinja2 - 디폴터 HTML 템플릿 엔진
* MarkupSafe - 인젝션 공격을 회피하기 위해 템플릿을 렌더링할 때에 신뢰할 수 없는 입력을 취소
* Werkzeug - WSGI 툴킷으로 플라스크의 코어 구현은 Werkzeug 를 바탕으로 만들어 짐

### 플라스크 명령어
* 플라스크 명령어 사용
<pre><code>flask
</code></pre>
<pre><code>flask --help
</code></pre>


* flask run - 플라스크의 내장 서버를 실행
<pre><code>flask run --help
</code></pre>

* flask routes - 앱의 라우팅 정보 출력 - 요청한 곳의 URL과 실제로 처리하는 함수의 연결 잡업
* Endpoint - URL에 접근 시 실행할 함수 또는 지정한 이름, static은 정적 파일용의 엔드포인트로, 고정으로 존재
* Methods - 사용할 HTTP 메서드, 지정이 없는 경우는 GET이 기본
* Rule - 사용할 URL 규칙
<pre><code>flask routes
</code></pre>

# flask shell - 플라스크 앱의 컨텍스트(실행 환경)에서 파이썬 인터랙티브 셸을 사용할 경우
* 디버깅이나 테스트


# 플라스크 실행하기
## 1. 파이썬 스크립트(코드) 작성
<pre><code># flask 클래스를 import 한다.
from flask import Flask

# flask 클래스를 인스턴스화한다.
app = Flask(__name__)

# URL과 실행할 함수를 매핑한다.
@app.route("/")
def index():
    return "Hello, Flask!"
</code></pre>


## 2. 환경 변수를 설정
* FLASK_APP - 앱의 위치
* FLASK_ENV - development(디버그 모드 on) 또는 production 지정
* 디렉터리 이동
<pre><code>(venv) $ cd app.py의 위치
</code></pre>

* 환경변수 설정
<pre><code>(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
</code></pre>


## 3. flask run 명령어 실행
<pre><code>(venv) $ flask run
</code></pre>

# .env 환경 변수 설정
* export로 설정한 환경 변수는 콘솔에서 로그아웃 시 제거
* .env로 앱 단위로 환경 변수를 설정
* .flaskenv 사용 가능
* python-dotenv 패키지 사용
<pre><code>pip install python-dotenv
</code></pre>


# 애플리케이션 루트
* 앱을 실행하는 현재 디렉터리, 모듈, 패키지를 읽어 들이는 경로는 애플리케이션 루트로 결정
* 플라스크 내부에서 python-dotenv 패키지를 호출 python-dotenv 설치 후, .env가 없는 경우에 애플리케이션 루트가 바뀜
* -> .env 없는 경우 - flask run 명령어를 실행한 디렉터리가 애플리케이션 루트
* -> .env 있는 경우 - .env 파일이 있는 디렉터리가 애플리케이션 루트
