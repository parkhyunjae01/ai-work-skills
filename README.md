# AI Work Skills

개발·데이터 분석·업무 문서 작성에 활용하는 공개 스킬·하네스·템플릿·도구 모음입니다. 작업에 맞는 자료를 선택하고 원본 출처와 적용 조건을 확인할 수 있습니다.

**스킬 목록 33개**(공개 원본 32개 + 직접 작성 1개) · **확장 자료 41개** · 추가 원본 파일 35개 · 작업 관리 양식 9개

확장 자료는 하네스·지침 16개, 실무 도구 24개, Polars 공식 스킬 1개입니다. 일부 프로젝트는 기존 스킬 목록과 겹칩니다. 전체 도구를 일괄 설치하지 않습니다.

[처음 시작](docs/START_HERE.md) · [하네스·계획 도구](docs/HARNESSES.md) · [실무 도구](docs/TOOLKIT.md) · [스킬 목록](docs/CATALOG.md) · [문제 해결 순서](docs/WORKFLOW.md)

## 기본 구성

**제공된 Codex + 작업 기록 파일 + 필요한 스킬 2~3개**로 시작합니다. 새 AI 실행기 설치 없이 요구사항·진행·결정·검증을 파일로 관리합니다.

| 준비할 것 | 바로가기 |
|---|---|
| 시작 요청·업무별 추천 조합 | [START_HERE](docs/START_HERE.md) |
| 과제 형식에 관계없이 처음부터 제출까지 진행 | [시간 제한 실무 과제 진행표](docs/TIMED_WORK.md) |
| 요구사항·계획·진행·검증·재개 기록 | [작업 관리 템플릿](templates/work-session/README.md) |
| 실행·사용 방법, AI 협업 과정, 문제 해결 기록 정리 | [work-review](skills/work-review/SKILL.md)로 지정된 제출 문서 갱신. 지정이 없으면 과제 폴더의 `WORK_REVIEW.md` 하나에 정리 |
| Spec Kit·OpenSpec·Planning with Files·BMAD·GSD·ExecPlans 원본 | [추가 원본 파일](extras/README.md) |
| OMX·Ralph·Ruflo·Trellis 등 전체 설치 조건 | [하네스 비교](docs/HARNESSES.md) |
| pandas·DuckDB·FastAPI·문서·테스트·화면 도구 | [실무 도구 비교](docs/TOOLKIT.md) |

## 빠른 시작

```bash
git clone https://github.com/parkhyunjae01/ai-work-skills.git
cd ai-work-skills
```

1. 작업의 요구사항과 결과물 형식을 확인합니다.
2. [작업 시작](docs/START_HERE.md)에서 필요한 구성과 스킬 2~3개를 선택합니다.
3. 해당 지침과 참조 파일을 읽고, **실제 구현은 과제 작업 폴더에서** 진행합니다.

이 저장소는 선택한 지침을 읽어 사용하는 방식입니다. 다운로드 시 전역 설치나 자동 등록을 수행하지 않습니다.

설치·준비가 끝났다면 [문제 해결 순서](docs/WORKFLOW.md)의 요구사항 분석 → 담당자 확인 → 구현 → 검증 흐름을 따릅니다. 단계별 Codex 요청과 업무 예시를 함께 제공합니다.

<details>
<summary>Codex 요청 예시</summary>

> 현재 작업의 README와 제출 지침을 읽고 https://github.com/parkhyunjae01/ai-work-skills 의 README.md, docs/START_HERE.md, catalog.json, resources.json에서 필요한 자료만 골라 적용해줘. 실행·사용 안내나 AI 협업 기록을 요구하면 지정된 파일명(대소문자 포함)·경로·양식의 항목을 따라줘.
>
> 문제가 생기면 재현 방법과 실제 증상, 원인 가설과 근거, 수정 내용과 같은 조건에서 다시 확인한 결과를 적어줘. AI가 제안한 일과 내가 판단하거나 확인한 일도 구분해줘. 제공 Codex 버전·인증·권한은 바꾸지 말고, 새 AI 실행기나 외부 계정은 연결하지 마. 먼저 미확인 질문과 최소 구현 흐름을 정리해줘.

</details>

## 업무별 선택

| 업무 | 시작할 스킬 |
|---|---|
| 요구사항·완료 기준 정리 | [write-spec](vendor/anthropics/knowledge-work-plugins/product-management/skills/write-spec/SKILL.md) |
| 구현 이유·시행착오·검증 결과 설명 | [work-review](skills/work-review/SKILL.md) |
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
| [skills/work-review/](skills/work-review/) | 직접 작성한 작업 회고 스킬과 빈 복습 양식 |
| [extras/](extras/) | 7개 출처의 추가 원본 템플릿·지침·고지 35개 |
| [templates/work-session/](templates/work-session/) | 직접 작성한 작업 관리 양식과 사용 안내 |
| [catalog.json](catalog.json) | 후보별 원본 주소, 로컬 경로, 포함 상태 |
| [resources.json](resources.json) | 하네스·개발 도구 41개와 적용 조건·확인 근거 |
| [sources.lock.json](sources.lock.json) | 원본 커밋과 파일별 SHA-256 |
| [resources.lock.json](resources.lock.json) | 추가 원본의 고정 커밋·SHA-256 |
| [scripts/start_work.py](scripts/start_work.py) | 기존 파일을 보존하며 새 작업 기록 폴더 생성 |
| [SOURCES.md](SOURCES.md) | 출처, 보관 범위, 라이선스 고지 |

## 파일 검증

Python 3.9 이상에서 실행합니다.

```bash
python3 scripts/verify_bundle.py
python3 scripts/verify_resources.py
```

파일 누락·변경, 목록의 일치 여부, 상위 참조 문서를 검사합니다. 네트워크 연결이나 원본 스킬의 스크립트 실행은 수행하지 않습니다.

확장 자료는 원본 다운로드·문서 검토 범위를 기록했습니다. 전체 프레임워크·라이브러리를 설치하거나 특정 제공 환경에서 실행한 결과로 해석하지 않습니다.

공개 다운로드와 Codex 설치·인식 결과는 [설치 확인 기록](docs/INSTALLATION_CHECK.md)에서 확인할 수 있습니다.

## 출처와 라이선스

직접 작성한 스킬·문서·코드는 [MIT](LICENSE), `vendor/`와 `extras/`의 제3자 자료는 각 원본 라이선스를 따릅니다. 원본 파일은 수정 없이 보관하며 폴더 구조를 보존합니다. 추가 원본의 출처는 [extras/README](extras/README.md)에 정리했습니다.

라이선스·지원 상태를 고려해 일부 후보는 링크만 제공합니다. 포함 범위와 제외 사유는 [SOURCES.md](SOURCES.md), 실행 환경과 호환성 조건은 [사용 안내](docs/USAGE.md)를 참고하세요.

공개 상태 유지가 필요한 용도에서는 요구된 기간까지 이 저장소를 공개로 유지합니다. 실제 과제·입력 데이터·비밀키·개인 접속 링크는 이 공개 저장소에 저장하거나 push하지 않습니다.

[사용 안내](docs/USAGE.md) · [모델 역할](docs/MODELS.md) · [플러그인·MCP](docs/PLUGINS.md)

확장 자료 확인일: **2026-10-30** · 기존 스킬 검토일: **2026-10-28**
