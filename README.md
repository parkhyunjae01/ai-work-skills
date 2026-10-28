# AI Work Skills

개발·데이터 분석·업무 문서 작성에 활용하는 공개 AI 스킬 모음입니다. 작업에 맞는 지침을 선택하고, 원본 출처와 사용 조건을 확인할 수 있습니다.

**스킬 32개** · 원본 포함 24개 · 링크 제공 8개 · 플러그인 6개 · MCP 3개

[스킬 목록](docs/CATALOG.md) · [사용 안내](docs/USAGE.md) · [모델 역할](docs/MODELS.md) · [플러그인·MCP](docs/PLUGINS.md) · [출처·라이선스](SOURCES.md)

## 빠른 시작

```bash
git clone https://github.com/parkhyunjae01/ai-work-skills.git
cd ai-work-skills
```

1. 작업의 요구사항과 결과물 형식을 확인합니다.
2. 아래 표 또는 [전체 목록](docs/CATALOG.md)에서 필요한 스킬 2~3개를 선택합니다.
3. 해당 `SKILL.md`와 연결된 참조 파일을 읽고 작업에 적용합니다.

이 저장소는 선택한 지침을 읽어 사용하는 방식입니다. 다운로드 시 전역 설치나 자동 등록을 수행하지 않습니다.

<details>
<summary>Codex 요청 예시</summary>

> 현재 작업의 요구사항을 확인한 뒤 https://github.com/parkhyunjae01/ai-work-skills 를 내려받아 README.md와 catalog.json을 읽어줘. 필요한 스킬 2~3개의 local_path를 찾아 SKILL.md와 참조 파일을 읽고 적용해줘. link-only 항목은 자동 설치하지 말고, 현재 환경의 규정과 내 요청을 우선해줘.

</details>

## 업무별 선택

| 업무 | 시작할 스킬 |
|---|---|
| 요구사항·완료 기준 정리 | [write-spec](vendor/anthropics/knowledge-work-plugins/product-management/skills/write-spec/SKILL.md) |
| 화면 설계·구현 | [frontend-design](vendor/anthropics/skills/skills/frontend-design/SKILL.md) |
| 데이터 구조·결측·중복 조사 | [explore-data](vendor/anthropics/knowledge-work-plugins/data/skills/explore-data/SKILL.md) |
| 분석 결과·계산 검증 | [validate-data](vendor/anthropics/knowledge-work-plugins/data/skills/validate-data/SKILL.md) |
| 오류 재현·원인 분석 | [systematic-debugging](vendor/obra/superpowers/skills/systematic-debugging/SKILL.md) |
| 완료 전 실행 결과 확인 | [verification-before-completion](vendor/obra/superpowers/skills/verification-before-completion/SKILL.md) |
| 업무 프로세스 개선 | [process-optimization](vendor/anthropics/knowledge-work-plugins/operations/skills/process-optimization/SKILL.md) |
| 고객 문의 분류 | [ticket-triage](vendor/anthropics/knowledge-work-plugins/customer-support/skills/ticket-triage/SKILL.md) |

## 저장소 구성

| 경로 | 내용 |
|---|---|
| [docs/](docs/) | 스킬 비교표, 사용 방법, 모델·플러그인 선택 안내 |
| [vendor/](vendor/) | 공개 원본 스킬과 참조 파일, 라이선스 |
| [catalog.json](catalog.json) | 후보별 원본 주소, 로컬 경로, 포함 상태 |
| [sources.lock.json](sources.lock.json) | 원본 커밋과 파일별 SHA-256 |
| [SOURCES.md](SOURCES.md) | 출처, 보관 범위, 라이선스 고지 |

## 파일 검증

Python 3.9 이상에서 실행합니다.

```bash
python3 scripts/verify_bundle.py
```

파일 누락·변경, 목록의 일치 여부, 상위 참조 문서를 검사합니다. 네트워크 연결이나 원본 스킬의 스크립트 실행은 수행하지 않습니다.

공개 다운로드와 Codex 설치·인식 결과는 [설치 확인 기록](docs/INSTALLATION_CHECK.md)에서 확인할 수 있습니다.

## 출처와 라이선스

직접 작성한 문서는 [MIT](LICENSE), `vendor/`의 제3자 자료는 각 원본 라이선스를 따릅니다. 원본 파일은 수정 없이 보관하며, 원래 참조 경로가 유지되도록 폴더 구조를 보존합니다.

라이선스·지원 상태를 고려해 일부 후보는 링크만 제공합니다. 포함 범위와 제외 사유는 [SOURCES.md](SOURCES.md), 실행 환경과 호환성 조건은 [사용 안내](docs/USAGE.md)를 참고하세요.

자료 확인일: **2026-10-28**
