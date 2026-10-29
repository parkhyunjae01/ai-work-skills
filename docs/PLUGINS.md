# Plugin·MCP 선택

외부 계정·네트워크 사용이 제한된 환경에서는 [작업 시작](START_HERE.md)의 로컬 구성을 먼저 사용합니다. 아래 서비스 목록은 일반적인 연결 후보이며, 특정 환경에서의 사용 허가나 사전 설치를 뜻하지 않습니다.

**Skill은 작업 지침, MCP는 도구 연결 방식, Plugin은 지침·도구·설정을 묶는 호스트별 패키지**입니다. 이 저장소는 선택과 활용을 안내하며, Plugin 설치나 외부 계정 연결을 수행하지 않습니다.

외부 자료 검색·저장에 필요한 연결만 선택합니다. 제공 파일·텍스트의 분석과 초안 작성은 연결 없이 가능합니다. Claude용 구성의 Codex 호환은 별도 확인합니다. [OpenAI Plugin 구성](https://github.com/openai/plugins) · [Anthropic 업무 패키지](https://github.com/anthropics/knowledge-work-plugins)

## 서비스 Plugin

공개 `plugin.json` 링크입니다. 실제 설치·도구·조직 권한은 제품에서 확인합니다.

| Plugin | 용도 | 연결 조건 | 작업 범위 |
|---|---|---|---|
| [GitHub](https://github.com/openai/plugins/blob/main/plugins/github/.codex-plugin/plugin.json) | 코드·이슈·PR·CI 검토 | 지원 connector 또는 CLI 인증, 비공개 저장소 권한 | 조회와 push·PR 생성 구분 |
| [Figma](https://github.com/openai/plugins/blob/main/plugins/figma/.codex-plugin/plugin.json) | 디자인·컴포넌트·변수와 구현 대조 | 계정·파일 권한, 지원 MCP와 도구 확인 | 읽기와 편집·업로드 구분 |
| [Notion](https://github.com/openai/plugins/blob/main/plugins/notion/.codex-plugin/plugin.json) | 팀 지식 검색·회의·요구사항 정리 | 지원 원격 MCP/OAuth, 워크스페이스·페이지 권한 | 검색·수정 범위와 게시 위치 지정 |
| [Google Drive](https://github.com/openai/plugins/blob/main/plugins/google-drive/.codex-plugin/plugin.json) | 파일 검색·Docs·Sheets·Slides 분석 | 앱 인증·파일 권한, 지원 형식·편집 기능 확인 | 로컬 파일과 클라우드 생성·수정·공유 구분 |
| [Linear](https://github.com/openai/plugins/blob/main/plugins/linear/.codex-plugin/plugin.json) | 이슈·프로젝트·후속 작업 정리 | 지원 앱/MCP, 팀·프로젝트 권한 | 변경할 이슈·담당자·상태 명시 |
| [Slack](https://github.com/openai/plugins/blob/main/plugins/slack/.codex-plugin/plugin.json) | 대화 검색·결정 요약·답변 초안 | 앱 인증·채널 권한, 검색·작성 도구 확인 | 발송 시 사용자 요청·채널·수신자 확인 |

검색 결과는 접근 범위에 한정됩니다. 검색에 나오지 않은 자료가 존재하지 않는다고 단정하지 않습니다.

## MCP

반복 호출이 필요할 때 추가합니다. 단순 검색·집계는 기존 브라우저·셸·Python·SQL로 충분할 수 있습니다.

| MCP | 용도 | 계정·실행 조건 | 확인 사항 |
|---|---|---|---|
| [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp) | OpenAI API·Codex 공식 문서 조회 | 읽기 전용 `https://developers.openai.com/mcp`, 안내상 인증 불필요, 지원 호스트·네트워크 필요 | 검색어가 원격으로 전송되므로 불필요한 내부 자료 제외 |
| [Context7](https://github.com/upstash/context7) | 라이브러리·프레임워크의 버전별 문서 조회 | 연결·인증·한도는 [API 안내](https://context7.com/docs/api-guide) 확인, 무키 사용 보장 없음 | 로컬 실행도 원격 질의 가능, 설치 버전과 문서 버전 대조 |
| [DuckDB MCP](https://github.com/motherduckdb/mcp-server-motherduck) | CSV·Parquet·DuckDB 반복 SQL 분석 | 로컬 파일·stdio·`uvx` 환경 확인, 토큰 없는 로컬 예제 제공, MotherDuck·S3는 별도 연결·인증 | DB 경로·읽기/쓰기 모드 지정, 읽기 전용과 네트워크 차단은 별개 |

연결 가능 여부는 호스트 지원과 조직 정책에 따릅니다.

## 연결 순서

1. 필요한 동작과 기존 도구의 지원 범위를 확인합니다.
2. 작은 읽기 작업으로 연결·계정·워크스페이스·권한을 확인합니다.
3. 생성·수정·공유의 대상과 범위를 지정합니다.
4. 실패 시 기존 도구·파일로 진행하고 미확인 사항을 표시합니다.

`~~category`는 연결 범주 표시일 수 있습니다. [Data CONNECTORS.md](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/CONNECTORS.md) · [Codex Plugin 안내](https://learn.chatgpt.com/docs/plugins)
