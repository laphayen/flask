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


# 라우팅 이용하기
* 라우팅 - 요청한 곳의 URL와 실제로 처리를 담당하는 함수를 연결하는 작업을 가리킨다.
* 함수 앞의 데코레이터라는 함수 @app.route()를 추가하여 루트를 추가
<pre><code>@app.route("/hello")
def hello():
    return "hello, world!"
</code></pre>

* 라우팅 정보 확인하기 - flask routes 명령어
<pre><code>(venv) $ flask routes
</code></pre>


# HTML 폼에서 이용하는 HTTP 메서드
* HTTP 메서드 - 클라이언트가 서버에 대해서 요청을 송신할 때에 서버에게 실행하기 를 바라는 조작을 전달하기 위해 사용, HTML 폼에서 GET 메서드, POST 메서드를 사용.
* GET 메서드 - 검색 등 리소스를 얻는 경우에 이용, 폼이 아닌 평소의 브라우징도
* POST 메서드 - 로그인이나 문의 송신 등 폼의 값을 등록, 갱신하는 경우에 이용

# 엔드포인트에 이름 붙이기
* 엔드포인트 - 일반적으로 API에 접근하기 위한 URI를 가리키는데, 플라스크에서는 URI와 연결된 함수명 또는 함수에 붙인 이름
* 기본값으로 @app.route로 수식된 함수명
* 엔드포인트를 미지정 시 함수명이 엔드포인트명으로 변경
<pre><code>@app.route("/", endpoint="dendpoint-name")
</code></pre>

* * *

# 허가할 HTTP 메서드 지정
* @app.route 데코레이터로 허가할 HTTP 메서드를 지정
* methods에 HTTP 메서드명을 지정, 미지정 시 GET이 기본값
<pre><code>@app.route("/", methods=["GET", "POST"]
</code></pre>

* 플라스크 버전 2.0 이후는 route() 생략
<pre><code>@app.get("/hello")
@app.post("/hello")
</code></pre>

* 예시 - GET, POST 메서드 요청 받음.
<pre><code>@app.route("/hello",methods=["GET", "POST"])
def hello():
    return "Hello, Flask!"
</code></pre>

* * *

# Rule에 변수 지정
* @app.route 데코레이터의 Rule에 변수 지정
* <변수명> 으로 지정
<pre><code>@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"
</code></pre>

* <컨버터: 변수명> - 옵션으로 컨버터 타입으로 데이터의 타입 지정
* string - 슬래시가 없는 텍스트
* int - 양의 정수
* float - 양의 부동 상수점
* path - 슬래시가 있는 텍스트를 허용
* uuid - UUID 문자열

* * *

# 템플릿 엔진 사용
* 템플릿(모형)과 데이터를 합성하여 성과 문서를 출력하는 소프트웨어
* 플라스크 기본 템플릿 엔진, 기본 설치 시 동시 설치 - Jinja2
* render_template 함수에 템플릿의 이름과 키워드 인수로서 변수를 넘겨 사용
* 템플릿에서 {{ 변수명 }} 이라고 기술한 부분은 Jinja2가 변수를 전개하여 렌더링

* * *

# Jinja2의 사용법
* 변수 값 출력 - 변수의 값 표시 {{ }}, render_template의 2번째 인수 이후에 설정한 키워드 인수 또는 사전 오브젝트에 지정한 변수명 사용
<pre><code><h1>Name: {{ name }}</h1></code></pre>

* 조건식 if문의 사용법 - {% %}사용
<pre><code>{% if name %}
<h1>Name: {{ name }}>/h1>
{% else %}
<h1>Name:</h1>
{% endif %}
</code></pre>

* 반복 for문 - {% %} 사용
<pre><code><ul>
    {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
</ul>
</code></pre>

* * *

# url_for 함수를 사용해서 URL 생성하기
* 엔드포인트의 URL을 사용하기 위해 url_for 함수 사용
* 통상 HTML 파일이나 View 파일에 /name과 같이 기술, 이것을 url_for("name")와 같이 기술
* 엔드 포인트에 대응하는 Rule이 바뀐다고 해도 HTML 파일이나 View에 기술하는 URL을 변경할 필요x

* * *

# 정적 파일 사용 - HTML, CSS, JS
* static 디렉터리애 배치
* static 엔드 포인트 사용
<pre><code>url_for("static", filename="style.css)
</code></pre>

* * *

# 애플리케이션 컨텍스트
* 요청으로 앱 레벨의 데이터를 이용
* current_app - 액티브 앱(실행 중의 앱)의 인스턴스
* g - 요청을 통해 이용할 수 있는 전역 임시(일시) 영억, 요청마다 리셋

* * *

# 요청 컨텍스트
* 요청이 있는 동안 요청 레벨의 데이터를 이용 가능.
* request와 session
* 수도으로 취득하여 푸시 -> test_request_contest 함수 사용
* 

* * *
# 컨텍스트의 라이프 사이클
* 1. 요청 처리 시작
  2. 애플리케이션 컨텍스트 작성(스택으로 push)
  3. 요청 컨텍스트를 작성(스택으로 push)
  4. 요청 처리를 종료
  5. 요청 컨텍스트를 삭제(스택으로부터 pop)
  6. 애플리케이션 컨텍스트 삭제(스텍으로부터 pop)
