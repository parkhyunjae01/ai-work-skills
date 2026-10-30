# Skill 카탈로그

[README](../README.md) · [사용 안내](USAGE.md) · [모델 역할](MODELS.md) · [플러그인·MCP](PLUGINS.md)

개발·데이터·문서·운영 업무를 위한 공개 원본 스킬 32개와 직접 작성한 스킬 1개입니다. 아래 표에서 용도와 의존성을 비교하고 `SKILL.md`를 확인할 수 있습니다. 확장 자료의 Polars 스킬은 [실무 도구 안내](TOOLKIT.md)에 따로 정리되어 있습니다. 저장소 포함 여부와 사용 방법은 [README](../README.md) 및 [사용 안내](USAGE.md)를 참고하세요.

## 직접 작성한 Skill

| Skill | 용도·산출물 | 적용 시점 |
|---|---|---|
| [work-review](../skills/work-review/SKILL.md) | 과제 폴더의 `WORK_REVIEW.md` 하나에 업무 목표, 구현 흐름, 선택 이유, 시행착오, 검증, AI 활용과 남은 한계를 근거와 함께 정리 | AI 사용이 허용된 작업 단계의 주요 변경 후와 제출 전 |

설명·회고를 준비하기 위한 스킬입니다. 실행하지 않은 테스트나 본인이 하지 않은 판단을 만들어 쓰지 않습니다. 서술형 등 AI가 금지된 단계에서는 실행하지 않으며, 그 단계에서 기록 파일을 볼 수 있다고 가정하지 않습니다. 공개 저장소에는 [빈 양식](../skills/work-review/assets/WORK_REVIEW.md)만 보관합니다.

## 작업에 맞춰 먼저 고르기

| 해야 할 일 | 시작 조합 | 얻을 결과 |
|---|---|---|
| 요구사항을 구현 가능한 범위로 정리 | write-spec + verification-before-completion | 수용 기준과 완료 확인 방법 |
| 재현되는 오류 수정 | systematic-debugging + verification-before-completion | 원인·최소 수정·재현 결과 |
| 중요한 계산·입력 규칙 구현 | test-driven-development + verification-before-completion | 실패·성공·회귀를 확인하는 테스트 |
| 화면 제작과 소스 검토 | frontend-design + web-design-guidelines | 화면 구조와 접근성·사용성 검토 |
| CSV 분석과 결과 보고 | explore-data + validate-data | 데이터 구조와 검증된 계산; 그래프가 필요하면 data-visualization 추가 |
| 절차서·문의 대응 문서 작성 | process-doc 또는 ticket-triage | 업무 흐름이나 문의 분류 기준 |

한 번에 모두 적용할 필요는 없다. 지금 만들 산출물에 필요한 지침부터 선택하고, 실행에 필요한 도구가 있는지 확인한다.

## 개발 Skill 12개

| 원본 Skill | 실제 활용 | 의존성·선택 기준 |
|---|---|---|
| [verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 수정 후 빌드·테스트 결과를 확인하고 완료 근거 정리 | Superpowers MIT. 프로젝트의 실행·검증 명령 필요. lint 통과만으로 기능 완성을 판단하지 않는다. |
| [systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 오류 재현 → 가설 검증 → 최소 수정 | Superpowers MIT. 같은 폴더의 참조 문서와 연결된 테스트 지침 확인. 재현 가능한 문제에 유용하다. |
| [test-driven-development](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md) | 계산·검증·상태 전이의 실패 테스트부터 작성 | Superpowers MIT. 테스트 실행기와 `writing-good-tests.md` 필요. 변경 위험과 범위에 맞춰 적용한다. |
| [writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) | 여러 파일에 걸친 변경을 작은 실행 단계로 나누기 | Superpowers MIT. 다른 실행·에이전트 지침으로 이어질 수 있다. 작은 수정에는 일반 계획으로 충분하다. |
| [brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 대안·제약·설계를 구현 전에 비교 | Superpowers MIT. 설계 승인 등 절차와 선택 기능이 포함된다. 요구가 이미 명확하면 필요한 부분만 참고한다. |
| [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 레이아웃·타이포그래피·상태가 일관된 화면 제작 | 개별 Apache-2.0. 실제 프레임워크와 디자인 제약을 함께 전달한다. |
| [vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) | React/Next.js 요청·번들·재렌더 문제 검토 | 원문 MIT 표기. `rules/`·`AGENTS.md` 포함 확인. 실제 스택과 버전에 맞는 규칙 선택. |
| [vercel-composition-patterns](https://github.com/vercel-labs/agent-skills/blob/main/skills/composition-patterns/SKILL.md) | 조건 분기가 많은 컴포넌트와 상태 공유 구조 정리 | 원문 MIT 표기. `rules/`·`AGENTS.md` 포함 확인. React 19 전용 항목은 버전 확인. |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) | UI 소스에서 폼·포커스·오류·빈 상태 점검 | 외부 `command.md`를 추가 조회하는 지침. 개별 라이선스는 별도 확인이 필요하며 이 카탈로그는 원문 링크를 제공한다. |
| [property-based-testing](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | 파서·정규화·계산이 다양한 입력에서도 지켜야 할 성질 검증 | Trail of Bits CC BY-SA 4.0. `references/`와 Hypothesis·fast-check 같은 실행 환경 필요. |
| [security-best-practices](https://github.com/openai/skills/blob/main/skills/.curated/security-best-practices/SKILL.md) | Python·JS/TS·Go의 보안 검토 항목 참고 | **원문 링크만 제공·번들 제외.** 개별 Apache-2.0이나 상위 `openai/skills` 저장소는 deprecated 안내가 있다. 현행 기본 설치 대상으로 취급하지 않는다. |
| [differential-review](https://github.com/trailofbits/skills/blob/main/plugins/differential-review/skills/differential-review/SKILL.md) | 기존 코드 변경이 인증·권한·입력 처리에 미치는 영향 검토 | Trail of Bits CC BY-SA 4.0. Git 이력·참조 문서와 추가 도구 의존성 확인. 변경 전후 비교가 있을 때 유용하다. |

라이선스 출처: [Superpowers](https://github.com/obra/superpowers/blob/main/LICENSE), [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt), [Trail of Bits](https://github.com/trailofbits/skills/blob/main/LICENSE), [security-best-practices](https://github.com/openai/skills/blob/main/skills/.curated/security-best-practices/LICENSE.txt). 구 OpenAI 저장소의 상태는 [README](https://github.com/openai/skills/blob/main/README.md), 현행 Plugin 구성은 [openai/plugins](https://github.com/openai/plugins)를 참고한다.

## 업무 Skill 16개

다음 16개는 Anthropic `knowledge-work-plugins`의 공개 업무 지침이다. 저장소의 [Apache-2.0 기본 라이선스](https://github.com/anthropics/knowledge-work-plugins/blob/main/LICENSE)와 각 폴더의 별도 고지 여부를 함께 확인한다. `CONNECTORS.md` 또는 `~~category` 같은 표기는 연결 범주를 설명하며, 외부 계정이나 도구를 자동 제공하지 않는다.

| 원본 Skill | 실제 활용·산출물 | 필요한 입력·실행 조건 |
|---|---|---|
| [write-spec](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/write-spec/SKILL.md) | 모호한 요청을 목표·비목표·수용 기준으로 정리 | 제공한 요구사항으로 초안 작성 가능. 상위 연결 안내 참고. |
| [metrics-review](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/metrics-review/SKILL.md) | KPI 변화와 목표 대비 차이 설명 | 지표 정의·비교 기간·수치 필요. 분석 서비스 직접 조회는 별도 연결 필요. |
| [synthesize-research](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/synthesize-research/SKILL.md) | 인터뷰·설문에서 근거가 있는 주제와 차이 추출 | 원문 텍스트와 표본·수집 맥락 필요. 관찰과 해석을 구분한다. |
| [explore-data](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/explore-data/SKILL.md) | 컬럼·키·결측·중복·분포 파악 | 데이터 파일과 파일 형식에 맞는 읽기 도구 필요. |
| [sql-queries](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/sql-queries/SKILL.md) | 스키마를 바탕으로 조회·집계 SQL 작성 | SQL 작성은 스키마로 가능. 실행에는 대상 DB 또는 로컬 엔진 필요. |
| [statistical-analysis](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/statistical-analysis/SKILL.md) | 분포·추세·검정과 불확실성 설명 | 데이터와 Python 분석 라이브러리 필요. 검정 가정과 표본 한계 확인. |
| [validate-data](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/validate-data/SKILL.md) | 분모·합계·기간·조인으로 생긴 분석 오류 점검 | 원자료·집계 기준·독립 재계산 필요. 보고서 공유 전에 유용하다. |
| [data-visualization](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/data-visualization/SKILL.md) | 비교·분포·추세를 적절한 그래프로 표현 | matplotlib·seaborn·plotly 등 선택한 도구 필요. 축·단위·출처 표시. |
| [build-dashboard](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/build-dashboard/SKILL.md) | KPI·필터·표가 있는 HTML 대시보드 제작 | 예제에 Chart.js·날짜 어댑터 CDN 사용. 오프라인 필요 시 의존성을 별도로 준비한다. |
| [process-doc](https://github.com/anthropics/knowledge-work-plugins/blob/main/operations/skills/process-doc/SKILL.md) | 담당·입출력·예외가 있는 SOP 작성 | 절차 설명으로 문서화 가능. 위키 게시는 별도 연결·권한 필요. |
| [process-optimization](https://github.com/anthropics/knowledge-work-plugins/blob/main/operations/skills/process-optimization/SKILL.md) | 대기·재작업·인수인계의 병목과 개선안 도출 | 현재 절차·시간·품질 측정치 필요. 추정 효과와 관측 결과를 구분한다. |
| [risk-assessment](https://github.com/anthropics/knowledge-work-plugins/blob/main/operations/skills/risk-assessment/SKILL.md) | 영향·완화 조치·담당자가 있는 위험대장 작성 | 업무 맥락과 근거 필요. 확인하지 않은 확률·비용은 가정으로 표시한다. |
| [ticket-triage](https://github.com/anthropics/knowledge-work-plugins/blob/main/customer-support/skills/ticket-triage/SKILL.md) | 문의 분류·우선순위·담당 추천 | 제공한 문의로 가능. 기존 티켓 조회·수정은 서비스 연결 필요. |
| [draft-response](https://github.com/anthropics/knowledge-work-plugins/blob/main/customer-support/skills/draft-response/SKILL.md) | 사실과 정책에 맞는 고객 답변 초안 | 문의 내용·정책·확인된 사실 필요. 초안과 실제 발송은 별도 작업. |
| [customer-escalation](https://github.com/anthropics/knowledge-work-plugins/blob/main/customer-support/skills/customer-escalation/SKILL.md) | 재현·영향·시도 내용을 정리한 전달 문서 | 제공 맥락으로 초안 작성 가능. 담당자 지정·외부 전달은 연결과 권한 필요. |
| [kb-article](https://github.com/anthropics/knowledge-work-plugins/blob/main/customer-support/skills/kb-article/SKILL.md) | 해결 사례를 FAQ·사용법·문제 해결 문서로 정리 | 해결 근거와 대상 독자 필요. 기존 지식 문서 조회·게시는 별도 연결. |

과거 이름으로 경로를 찾는 경우: `feature-spec` → `write-spec`, `metrics-tracking` → `metrics-review`, `user-research-synthesis` → `synthesize-research`, `data-exploration` → `explore-data`, `data-validation` → `validate-data`, `interactive-dashboard-builder` → `build-dashboard`, `response-drafting` → `draft-response`, `escalation` → `customer-escalation`, `knowledge-management` → `kb-article`. 링크는 위 표의 경로를 사용한다.

## 문서 Skill 4개 — 링크만 제공

다음 4개는 공개 소스를 읽을 수 있지만 **별도 제한 조건이 있는 source-available 자료**다. 이 저장소에 원문·스크립트를 복사해 번들로 배포하지 않으며 자동 설치 대상에도 넣지 않는다. 사용 여부는 각 라이선스와 이용 환경을 확인해 판단한다. 문서 작업은 사용 중인 도구가 제공하는 기능과 허용된 라이브러리로도 수행할 수 있다.

| 원본 Skill | 다루는 작업 | 라이선스·주요 도구 |
|---|---|---|
| [pdf](https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md) | PDF 추출·병합·폼·OCR | [제한 라이선스](https://github.com/anthropics/skills/blob/main/skills/pdf/LICENSE.txt). Python·Poppler·OCR·참조 파일. |
| [xlsx](https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md) | Excel 수식·서식·재계산 | [제한 라이선스](https://github.com/anthropics/skills/blob/main/skills/xlsx/LICENSE.txt). openpyxl·pandas·LibreOffice·스크립트. |
| [docx](https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md) | Word 작성·수정·변경 추적 | [제한 라이선스](https://github.com/anthropics/skills/blob/main/skills/docx/LICENSE.txt). Node docx·pandoc·렌더·검증 도구. |
| [pptx](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | PowerPoint와 템플릿 기반 발표자료 | [제한 라이선스](https://github.com/anthropics/skills/blob/main/skills/pptx/LICENSE.txt). pptxgenjs·렌더·검증 스크립트. |

원본의 문서 Skill 구분은 [Anthropic Skills README](https://github.com/anthropics/skills/blob/main/README.md)를 참고한다. 이 목록은 모든 부속 코드의 보안 감사나 모든 AI 도구에서의 설치·동작 검증을 의미하지 않는다. `main` 링크의 내용은 이후 바뀔 수 있다.
