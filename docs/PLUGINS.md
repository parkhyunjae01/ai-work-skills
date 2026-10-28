# Plugin과 MCP 선택 안내

**Skill은 작업 지침, MCP는 도구를 연결하는 방식, Plugin은 지침·도구·설정을 묶는 호스트별 패키지**다. 공개 저장소에 구성이 있어도 설치·인증·사용 권한이 자동으로 생기지는 않는다. 이 저장소의 Skill 설치는 아래 서비스에 로그인하거나 계정을 연결하지 않는다.

외부 서비스의 기존 자료를 검색하거나 결과를 저장할 일이 있을 때 연결을 검토한다. 제공받은 파일·텍스트만으로 끝나는 분석과 초안 작성은 해당 서비스 연결 없이 진행할 수 있다. Claude용 marketplace·명령·에이전트 구성이 Codex에서 그대로 작동한다고 가정하지 않는다. [OpenAI Plugin 구성](https://github.com/openai/plugins) · [Anthropic 업무 패키지](https://github.com/anthropics/knowledge-work-plugins)

## 서비스 Plugin 6개

각 링크는 공개 `plugin.json`이다. 설치 안내와 실제 도구 목록은 사용 중인 제품에서 확인한다. **외부 계정 연결은 해당 서비스를 쓰려는 경우에만 필요**하며, 조직이 제공하는 연결과 접근 권한을 우선 확인한다.

| Plugin·공개 구성 | 도움이 되는 업무 | 필요한 연결·권한 | 작업할 때 구분할 것 |
|---|---|---|---|
| [GitHub](https://github.com/openai/plugins/blob/main/plugins/github/.codex-plugin/plugin.json) | 저장소 구조·이슈·PR·CI를 함께 읽고 변경 배경이나 실패 원인 정리 | 제품이 제공하는 GitHub connector 또는 지원 CLI 인증. 비공개 저장소는 해당 저장소 권한 필요. | 공개 코드 읽기, 비공개 자료 조회, 브랜치 push·PR 생성은 서로 다른 권한과 작업이다. |
| [Figma](https://github.com/openai/plugins/blob/main/plugins/figma/.codex-plugin/plugin.json) | 디자인 맥락·컴포넌트·변수·디자인 시스템을 구현과 대조 | Figma 계정·파일 권한과 지원 MCP 연결. 사용 가능한 도구는 연결 방식에 따라 확인. | 디자인 읽기와 Figma 파일 편집·새 자료 업로드를 구분한다. |
| [Notion](https://github.com/openai/plugins/blob/main/plugins/notion/.codex-plugin/plugin.json) | 팀 지식 검색·회의 준비·요구사항 정리·관련 페이지 연결 | 지원 원격 MCP/OAuth와 대상 워크스페이스·페이지 접근 권한. | 제공 텍스트 요약은 로컬에서도 가능하다. 실제 페이지 검색·생성·수정은 연결된 범위에 따르며 게시 위치를 지정한다. |
| [Google Drive](https://github.com/openai/plugins/blob/main/plugins/google-drive/.codex-plugin/plugin.json) | Drive 파일 검색, Docs·Sheets·Slides 자료를 근거로 문서와 분석 정리 | 앱 인증과 파일별 접근 권한. 지원 파일 형식·편집 기능은 실제 연결에서 확인. | 로컬 파일 생성과 클라우드 문서 생성·수정·공유는 별도 작업이다. |
| [Linear](https://github.com/openai/plugins/blob/main/plugins/linear/.codex-plugin/plugin.json) | 이슈·프로젝트 맥락 파악, 진행 상황과 후속 작업 정리 | 제품이 지원하는 앱/MCP 연결과 팀·프로젝트 권한. | 이슈 분석과 생성·담당자·상태 변경을 구분한다. 실제 변경 시 대상 이슈와 변경값을 명시한다. |
| [Slack](https://github.com/openai/plugins/blob/main/plugins/slack/.codex-plugin/plugin.json) | 접근 가능한 대화 검색, 결정·요청 요약, 답변 초안 | 앱 인증, 워크스페이스·채널 접근 권한과 검색/작성 도구 제공 여부. | 검색 결과와 초안 작성이 메시지 발송을 뜻하지 않는다. 발송은 사용자 요청과 대상 채널·수신자를 확인한다. |

연결 후에는 작은 읽기 작업으로 대상 계정·워크스페이스·권한을 확인한다. 검색 결과에 없는 자료를 존재하지 않는다고 단정하지 않으며, 접근 범위와 미확인 부분을 결과에 표시한다.

## MCP 3개

MCP는 반복적인 도구 호출이 필요한 경우에 추가한다. 단순한 문서 검색이나 CSV 집계는 기존 브라우저·셸·Python·SQL 도구로 충분할 수 있다.

| MCP·공식 자료 | 적합한 용도 | 계정·실행 조건 | 연결 전에 확인할 점 |
|---|---|---|---|
| [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp) | OpenAI API·Codex의 공식 문서를 반복 검색·조회 | 공개 문서 읽기 전용 서버 `https://developers.openai.com/mcp`. 안내상 인증 불필요. MCP를 지원하는 호스트와 네트워크 필요. | 공개 문서 조회용이다. 검색어가 원격 서비스로 전송되므로 질문에 불필요한 내부 자료를 넣지 않는다. |
| [Context7](https://github.com/upstash/context7) | 라이브러리와 프레임워크의 문서·버전별 API 확인 | 원격 문서 조회 서비스. 제공 연결·인증 방식·사용 한도를 현행 안내에서 확인. 무키 사용을 보장하지 않는다. | 로컬 실행 방식도 문서 질의를 원격으로 보낼 수 있다. 설치한 패키지 버전과 조회한 문서 버전을 대조한다. |
| [DuckDB MCP](https://github.com/motherduckdb/mcp-server-motherduck) | CSV·Parquet·DuckDB 파일에 반복 SQL 실행 | 로컬 파일·stdio 모드와 `uvx` 실행 환경을 확인. 클라우드 토큰 없는 로컬 예제가 있다. MotherDuck·S3 등 원격 접근은 별도 연결·자격 증명 조건. | 로컬 DB 경로와 읽기/쓰기 모드를 정한다. read-only가 네트워크 차단을 뜻하지 않으며 원격 파일 접근 여부는 별도로 확인한다. |

Context7의 인증·한도는 [API 안내](https://context7.com/docs/api-guide), DuckDB MCP의 모드와 제한은 [저장소 안내](https://github.com/motherduckdb/mcp-server-motherduck)를 기준으로 한다. 공개 서버가 현재 사용 중인 제품에서 연결 가능하다는 보장은 없으며 호스트의 지원 방식과 조직 정책도 적용된다.

## 연결을 고르는 순서

1. 필요한 동작을 정한다. 예: 공개 API 문서 반복 조회, 사내 이슈 검색, 로컬 CSV 분석.
2. 현재 도구로 수행할 수 있는지 확인한다. Skill의 `~~category`는 실제 연결 이름이 아닌 범주 표시일 수 있다.
3. 필요한 연결 하나를 준비하고 작은 읽기 작업으로 작동을 확인한다.
4. 외부 자료 생성·수정·공유가 필요하면 대상과 작업 범위를 명확히 지정한다.
5. 연결이 실패하면 제공 파일이나 기존 도구로 가능한 작업을 계속하고, 연결 때문에 확인하지 못한 부분을 표시한다.

Skill별 연결 범주의 예시는 [Data CONNECTORS.md](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/CONNECTORS.md), 호스트의 설치 개념은 [Codex Plugin 안내](https://learn.chatgpt.com/docs/plugins)를 참고한다. 공개 구성의 존재와 실제 설치·인증·동작 상태는 각각 확인해야 한다.
