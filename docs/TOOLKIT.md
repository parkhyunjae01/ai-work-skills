# 실무 도구 목록

[README](../README.md) · [작업 시작](START_HERE.md) · [하네스](HARNESSES.md) · [기계 판독 목록](../resources.json)

확인일: **2026-10-30**. 원본 페이지와 공개 다운로드를 확인한 후보입니다. 라이브러리 코드는 이 저장소에 통째로 포함하지 않으며, 설치·실행 검증과 구분합니다. 과제에 필요한 도구만 현재 환경에 맞춰 사용합니다.

## 빠른 선택

| 필요한 작업 | 시작점 |
|---|---|
| CSV·Excel 집계 | pandas; SQL 조인 중심이면 DuckDB |
| 큰 표·지연 실행 | Polars + 추가 수록한 공식 Skill |
| Excel 결과 파일 | openpyxl(기존 파일 편집), XlsxWriter(새 보고서 작성) |
| PDF·Word·발표 파일 | pypdf, python-docx, python-pptx, ReportLab |
| API·입력 검증 | FastAPI, Pydantic |
| 데이터 검증·자동 테스트 | Pandera, pytest; 필요한 경우 Hypothesis |
| 웹 UI·대시보드 | 기존 프로젝트 우선; Vite·shadcn/ui 또는 Streamlit·Plotly |
| 반복 실행 CLI | Typer, Rich |

## 원본과 적용 조건

### 데이터·검증

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [pandas](https://github.com/pandas-dev/pandas) | CSV·Excel 정리, 결측·중복 조사, 그룹별 집계 | [BSD-3-Clause](https://github.com/pandas-dev/pandas/blob/HEAD/LICENSE) | 데이터가 메모리에 들어오는 일반 표 분석. Excel 엔진은 별도 의존성일 수 있다. |
| [DuckDB](https://github.com/duckdb/duckdb) | CSV·Parquet를 SQL로 조인·집계하는 로컬 분석 | [MIT](https://github.com/duckdb/duckdb/blob/HEAD/LICENSE) | 별도 DB 서버 없이 실행. 외부 연결·확장 다운로드는 필요한 경우만 허용 환경에서 사용. |
| [Polars](https://github.com/pola-rs/polars) | 대용량 표의 지연 실행·조인·집계 | [MIT](https://github.com/pola-rs/polars/blob/HEAD/LICENSE) | 현재 설치 버전에 맞는 API 확인. pandas와 같은 결과·정렬·null 처리라고 가정하지 않는다. |
| [Pandera](https://github.com/unionai-oss/pandera) | DataFrame의 열·범위·중복 등 데이터 품질 검증 | [MIT](https://github.com/unionai-oss/pandera/blob/HEAD/LICENSE.txt) | 사용하는 데이터프레임 백엔드 extra를 선택하고 설치 버전에 맞는 import를 확인. |

### API·백엔드

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [FastAPI](https://github.com/fastapi/fastapi) | Python API와 입력 검증, 자동 API 명세 | [MIT](https://github.com/fastapi/fastapi/blob/HEAD/LICENSE) | 웹 API가 요구될 때 사용. 설치된 ASGI 서버와 실제 포트·환경을 확인. |
| [Pydantic](https://github.com/pydantic/pydantic) | 입력·설정·JSON 스키마 검증 | [MIT](https://github.com/pydantic/pydantic/blob/HEAD/LICENSE) | 로컬 Validation 기능 사용. Logfire 등 외부 관측 서비스는 별도 제품이므로 자동 연결하지 않는다. |

### 테스트·코드 품질

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [pytest](https://github.com/pytest-dev/pytest) | 핵심 계산·API·파일 처리 회귀 검사 | [MIT](https://github.com/pytest-dev/pytest/blob/HEAD/LICENSE) | 브라우저 자동조작 플러그인 없이 로컬 함수·파일·API 검사를 수행. |
| [Hypothesis](https://github.com/HypothesisWorks/hypothesis) | 경계값·다양한 입력을 생성하는 속성 기반 테스트 | [MPL-2.0](https://github.com/HypothesisWorks/hypothesis/blob/HEAD/LICENSE.txt) | 명확한 불변조건이 있는 계산·파서에 선택 적용. 테스트 수와 실행시간을 제한. |
| [Ruff](https://github.com/astral-sh/ruff) | Python 정적 검사와 포맷 | [MIT](https://github.com/astral-sh/ruff/blob/HEAD/LICENSE) | check 결과를 먼저 검토하고 자동 수정은 필요한 범위만 적용. |

### 문서·파일

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [pypdf](https://github.com/py-pdf/pypdf) | PDF 텍스트 추출·분할·병합 | [BSD-3-Clause](https://github.com/py-pdf/pypdf/blob/HEAD/LICENSE) | 텍스트 PDF 대상. 이미지 스캔 PDF의 OCR을 제공하는 것으로 오해하지 않는다. |
| [python-docx](https://github.com/python-openxml/python-docx) | Word 문서의 문단·표 읽기와 DOCX 작성 | [MIT](https://github.com/python-openxml/python-docx/blob/HEAD/LICENSE) | Office 앱 없이 파일 생성. 페이지 배치·최종 렌더링 검토는 별도. |
| [python-pptx](https://github.com/scanny/python-pptx) | PowerPoint 슬라이드·표·차트 생성과 읽기 | [MIT](https://github.com/scanny/python-pptx/blob/HEAD/LICENSE) | PowerPoint 앱 없이 파일 생성. 글자 넘침·한글 폰트·최종 시각 검토는 별도. |
| [XlsxWriter](https://github.com/jmcnamara/XlsxWriter) | 서식·차트·수식이 있는 새 Excel 결과 파일 생성 | [BSD-2-Clause](https://github.com/jmcnamara/XlsxWriter/blob/HEAD/LICENSE.txt) | 새 XLSX 작성용. 기존 파일 읽기·수정 도구로 사용하지 않는다. |
| [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl) | 기존 Excel 통합문서 읽기·수정·저장 | [MIT/Expat](https://openpyxl.readthedocs.io/en/stable/index.html) | 공식 소스는 GitHub가 아닌 Heptapod. 수식 계산 엔진이 아니며 원본을 별도 보존한다. |
| [ReportLab](https://docs.reportlab.com/) | 표·문단·차트가 있는 PDF 보고서 생성 | [BSD (open-source toolkit)](https://docs.reportlab.com/developerfaqs/) | 오픈소스 PDF Toolkit만 해당. ReportLab Plus는 별도 상용 제품. 한글 폰트와 줄바꿈·페이지 넘침을 검토한다. |

### 분석 대시보드

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [Streamlit](https://github.com/streamlit/streamlit) | Python 분석을 간단한 내부 대시보드로 제공 | [Apache-2.0](https://github.com/streamlit/streamlit/blob/HEAD/LICENSE) | 로컬 서버로 실행하고 클라우드 배포는 제외. .streamlit/config.toml에서 browser.gatherUsageStats=false, server.headless=true 권장. |
| [Plotly.py](https://github.com/plotly/plotly.py) | 상호작용 차트와 자체 포함 HTML 보고서 | [MIT (code); docs CC BY 4.0](https://github.com/plotly/plotly.py/blob/HEAD/LICENSE.txt) | write_html(include_plotlyjs=True, auto_open=False)로 로컬 출력. 원격 업로드 없이 사용. 코드와 문서 라이선스가 다르다. |

### 화면·대시보드

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [shadcn/ui](https://github.com/shadcn-ui/ui) | 필요한 React UI 컴포넌트 소스 참고·추가 | [MIT](https://github.com/shadcn-ui/ui/blob/HEAD/LICENSE.md) | React 등 기존 프로젝트 구성 확인 후 필요한 컴포넌트만 추가. 전체 앱 대체 템플릿으로 쓰지 않는다. |
| [Vite](https://github.com/vitejs/vite) | 프런트엔드 개발 서버와 빌드 | [MIT](https://github.com/vitejs/vite/blob/HEAD/LICENSE) | 제공 프로젝트가 있으면 유지. 현재 Node 버전과 의존성 호환을 확인하고 새 스캐폴딩은 필요할 때만 사용. |

### 도식·문서화

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [Mermaid](https://github.com/mermaid-js/mermaid) | 텍스트로 업무 흐름·시퀀스·구조도 작성 | [MIT](https://github.com/mermaid-js/mermaid/blob/HEAD/LICENSE) | 로컬 또는 지원하는 Markdown 뷰어에서 렌더링. 원격 다이어그램 서비스로 업무 자료를 보내지 않는다. |

### 실행·개발 도구

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [uv](https://github.com/astral-sh/uv) | Python 의존성·가상환경 관리 | [MIT OR Apache-2.0](https://github.com/astral-sh/uv/blob/HEAD/LICENSE-MIT) | 제공 환경에 이미 있으면 활용. Codex나 제공 시스템 자체를 업그레이드하지 않는다. |

### 외부 문서 연결

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [Context7](https://github.com/upstash/context7) | 버전별 공개 라이브러리 문서 검색 | [MIT](https://github.com/upstash/context7/blob/HEAD/LICENSE) | 현재 빠른 설치는 OAuth 인증과 API 키 발급을 포함. 개인 키 금지 환경에서는 기본 설치 대상 제외; 질의에 업무 원문을 보내지 않는다. |

### 명령행 자동화

| 도구·원본 | 용도 | 라이선스 | 적용 조건 |
|---|---|---|---|
| [Typer](https://github.com/fastapi/typer) | 파일 처리 등을 명령행 도구로 구성 | [MIT](https://github.com/fastapi/typer/blob/HEAD/LICENSE) | 간단한 도구면 표준 argparse도 충분. 전역 셸 설정 변경 없이 프로젝트 안에서 사용. |
| [Rich](https://github.com/Textualize/rich) | 터미널 표·진행률·오류 메시지 가독성 개선 | [MIT](https://github.com/Textualize/rich/blob/HEAD/LICENSE) | 핵심 업무 처리 후 필요할 때만 추가. 자동 UI 조작 도구가 아닌 출력 라이브러리. |

## Polars 지침 원본도 포함

[SKILL.md](../extras/polars-inc/skills/skills/polars/SKILL.md)와 참조 문서 6개, MIT LICENSE를 함께 보관했습니다. 원본 README에 Codex 지원이 명시되어 있습니다. Polars 2.0 기준이므로 실제 라이브러리 버전과 대조합니다. 지침 다운로드는 Python 패키지 설치와 별개입니다.

## 실제 실행 전에

- 프로젝트의 기존 의존성을 확인하고 필요한 패키지만 추가합니다. 버전 고정 환경의 Codex는 업데이트하지 않습니다.
- Streamlit은 사용 통계를 끄고 headless로 실행합니다. Plotly 보고서는 필요에 따라 자체 포함 HTML을 사용합니다. 원격 서비스·공유·배포 기능을 자동으로 사용하지 않습니다.
- Context7 등 원격 연결은 별도 인증·개인 키·전송 조건을 확인해야 하므로 기본 구성에서 제외합니다. 공개 문서나 제공 파일만으로 진행할 수 있으면 먼저 활용합니다.
- PDF 텍스트 추출과 스캔 이미지 OCR은 다릅니다. pypdf만으로 이미지 속 글자가 추출된다고 가정하지 않습니다.
- 공개 README나 문서를 내려받았다는 사실은 해당 패키지의 설치 성공·실행 성공을 의미하지 않습니다.

## 확인 범위

실무 도구 24개에 대해 작은 공개 README 또는 공식 설명 문서의 인증 없는 다운로드가 성공했습니다. 주소·바이트 수·SHA-256은 `resources.json`의 `public_download_check`에 남겼습니다. 이 점검은 조사 시점의 읽기 가능성을 확인하며 전체 패키지 설치나 대상 환경의 네트워크를 보증하지 않습니다.
