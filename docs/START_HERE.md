# 작업 시작

[README](../README.md) · [문제 해결 순서](WORKFLOW.md) · [스킬 목록](CATALOG.md)

## 기본 구성

**제공된 Codex + 작업 기록 파일 + 필요한 스킬 2~3개**로 시작합니다. 별도 에이전트 실행기를 설치할 필요는 없습니다.

| 필요한 것 | 선택 |
|---|---|
| 요구사항·진행·결정을 파일로 기억하기 | [작업 관리 템플릿](../templates/work-session/README.md) |
| 검증하며 구현하기 | 기존 `verification-before-completion` + 업무에 맞는 스킬 |
| 복잡한 변경의 단계별 계획 | [하네스·계획 도구 안내](HARNESSES.md)에서 하나 선택 |
| 데이터·문서·API·화면 처리 도구 | [도구 목록](TOOLKIT.md)에서 필요한 항목만 선택 |

이 구성은 파일을 읽고 갱신하는 작업 방식입니다. 백그라운드에서 AI를 반복 호출하는 자율 실행기는 포함하지 않습니다.

## Codex에 보낼 시작 요청

```text
현재 작업의 README와 제공 자료부터 읽고 필수 결과물·제약·완료 기준을 정리해줘.
https://github.com/parkhyunjae01/ai-work-skills 의 README와 docs/START_HERE.md,
catalog.json 및 resources.json에서 이번 작업에 필요한 자료만 골라줘.
templates/work-session의 필요한 파일로 작업 공간 안에 목표·계획·진행·검증 기록을 만들어줘.
기존 지침·파일은 보존하고, 선택한 스킬과 참조 파일을 읽어 적용해줘.
제공된 Codex 버전·인증·권한은 바꾸지 말고, 새 AI 실행기나 외부 계정은 연결하지 마.
담당자에게 확인할 핵심 질문과 가장 작은 구현 흐름부터 제시해줘.
```

이미 저장소를 내려받았다면 로컬 경로를 알려주면 됩니다. 목록 전체와 원본 지침 전체를 한꺼번에 읽힐 필요는 없습니다.

## 작업별 조합

| 작업 | 스킬 | 필요할 때 추가하는 도구 | 첫 검증 |
|---|---|---|---|
| CSV·Excel 분석 | `explore-data`, `validate-data` | pandas 또는 DuckDB, openpyxl | 작은 샘플의 집계·분모·중복을 수동 대조 |
| 보고서·업무 문서 | `process-doc` 등 해당 업무 스킬 | python-docx, XlsxWriter, python-pptx | 원문 근거·숫자·저장 파일 확인 |
| API·자동화 | `write-spec`, `verification-before-completion` | FastAPI, Pydantic, pytest | 정상 입력·오류 입력의 실제 응답 |
| 웹 화면 | `frontend-design`, `verification-before-completion` | Vite, shadcn/ui, 기존 프로젝트 프레임워크 | 실제 데이터 연결과 사용자의 직접 확인 |
| 현황 대시보드 | `build-dashboard`, `validate-data` | Plotly, Streamlit | 계산 기준과 실제 입력의 일치 |
| 재현되는 오류 | `systematic-debugging` | 기존 테스트 도구 | 수정 전 재현·수정 후 같은 사례 재검증 |

설치된 라이브러리와 제공 코드가 있으면 우선 활용합니다. 목록에 있다는 이유로 모든 패키지를 설치하지 않습니다.

## 기록 파일 만들기

저장소 루트에서 실행하는 예시입니다. 작업 대상 폴더는 실제 환경에 맞게 바꿉니다.

```bash
python3 scripts/start_work.py --destination /path/to/task/work-notes --dry-run
python3 scripts/start_work.py --destination /path/to/task/work-notes
```

Python 표준 라이브러리만 사용합니다. 지정한 폴더가 이미 있으면 중단하며, 기존 `AGENTS.md`·Codex 설정·모델·인증은 변경하지 않습니다. 새 폴더가 필요 없으면 템플릿의 필요한 부분만 기존 기록에 반영합니다.

실제 업무 내용은 **작업 환경 안의 기록 파일에만** 작성합니다. 내려받은 공개 자료 저장소에 과제·원본 데이터·비밀키를 넣거나 원격으로 push하지 않습니다.

## 중간에 맥락이 끊겼을 때

```text
작업 기록의 TASK.md, PROGRESS.md, HANDOFF.md를 읽고 현재 파일·실행 결과와 대조해줘.
완료한 부분은 유지하고, 기록된 다음 작업부터 이어서 진행해줘.
확인하지 않은 결과는 완료로 취급하지 마.
```

모델 전환이나 재시작 전에 `HANDOFF.md`에 결정 사항, 수정 파일, 마지막 검증, 다음 행동을 짧게 남깁니다. 파일 이름 자체가 자동 기억을 보장하지 않으므로 재개 시 읽을 경로를 명시합니다.

## 제한된 환경에서 적용

- 실행 환경의 최신 안내와 과제 요구사항을 먼저 따릅니다.
- Codex 버전 고정 환경에서는 설치기가 Codex를 업데이트하거나 교체하는지 확인합니다. 필요한 경우 문서·템플릿만 읽습니다.
- 외부 AI 호출, 개인 키·계정 연결, 원격 업로드, UI 자동 조작이 제한되면 해당 기능은 사용하지 않습니다.
- 공개 자료 획득과 업무 데이터의 외부 전송을 구분합니다. 검색·원격 MCP 요청에도 내부 원문을 포함하지 않습니다.
- 공개 상태 유지가 필요한 용도라면 활용한 저장소의 공개 상태를 요구된 기간까지 유지합니다.

## 참고

Codex는 `AGENTS.md`를 프로젝트 지침으로 읽습니다. 이 저장소의 `AGENTS.example.md`는 검토용 예시이며 자동 적용되는 파일명이 아닙니다. 기존 프로젝트 지침과 필요한 항목을 합치거나 현재 대화에서 명시적으로 읽게 합니다. [공식 AGENTS.md 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

계획·결정·진행 상황을 파일로 남기는 방식은 OpenAI의 [장시간 작업 계획 예시](https://developers.openai.com/cookbook/articles/codex_exec_plans)도 참고할 수 있습니다. 이 저장소의 작업 관리 템플릿은 별도로 작성했으며, 원문은 `extras/`에 출처·라이선스와 함께 보관합니다.
