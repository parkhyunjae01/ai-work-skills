# 하네스와 계획 도구

[README](../README.md) · [작업 시작](START_HERE.md) · [전체 확장 목록](../resources.json)

## 먼저 고를 구성

**별도 실행기 설치는 필수가 아닙니다.** 제공된 Codex에서 [작업 관리 템플릿](../templates/work-session/README.md)과 필요한 스킬부터 사용합니다. 계획·기억·검증을 정리하는 자료와 AI를 반복 실행하는 하네스는 구분합니다.

| 상황 | 권장 시작점 |
|---|---|
| 현재 맥락·다음 작업을 잊음 | 작업 관리 템플릿 또는 Planning with Files |
| 완료 기준·작업 순서가 모호함 | Spec Kit 또는 OpenSpec의 필요한 양식 하나 |
| 긴 구현에서 결정·검증 근거가 사라짐 | Codex ExecPlans |
| 담당자 요구를 제품 명세로 정리해야 함 | BMAD 브리프·PRD의 필요한 부분 |
| 전체 팀 실행·자동 반복이 필요함 | 별도 런타임의 권한·설정·통신·제공 버전 호환 확인 후 검토 |

## 확인한 공개 프로젝트

확인일: **2026-10-30**. 인기 순위나 성능 순위가 아닙니다. 같은 작업을 여러 프레임워크로 동시에 관리하지 않습니다.

| 프로젝트 | 용도 | 이 저장소의 제공 범위 | 기본 사용 판단 |
|---|---|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) | 명세·계획·작업 목록을 연결하는 개발 절차 | 일부 원본 파일 포함 | 템플릿부터 |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | 변경 제안·설계·명세·작업 목록을 추적하는 개발 절차 | 일부 원본 파일 포함 | 템플릿부터 |
| [Planning with Files](https://github.com/OthmanAdi/planning-with-files) | task_plan·findings·progress로 계획과 작업 상태를 파일에 보관 | 일부 원본 파일 포함 | 템플릿부터 |
| [Superpowers](https://github.com/obra/superpowers) | 설계·계획·테스트·디버깅·완료 검증 스킬 모음 | 기존 스킬 포함 | 개별 지침 선택 |
| [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) | 제품 브리프·PRD·설계·구현·검토를 연결하는 역할별 워크플로 | 일부 원본 파일 포함 | 전체 설치 조건부 |
| [Oh My Codex (OMX)](https://github.com/Yeachan-Heo/oh-my-codex) | Codex CLI 주변의 계획·역할·팀 실행·훅·상태 관리 계층 | 원본 링크 | 전체 설치 조건부 |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | 계획·구현·검토·학습 기록을 축적하는 스킬 플러그인 | 원본 링크 | 개별 지침 선택 |
| [GSD Core](https://github.com/open-gsd/gsd-core) | 단계별 논의·계획·구현·검증과 지속 상태를 제공하는 프레임워크 | 일부 원본 파일 포함 | 전체 설치 조건부 |
| [Get Shit Done (archived)](https://github.com/gsd-build/get-shit-done) | GSD 구버전 템플릿과 워크플로 보관본 | 원본 링크 | 참고용 |
| [GSD Codex Fork](https://github.com/Oisinwang/get-shit-done-codex) | Codex 중심의 GSD 커뮤니티 포크 | 원본 링크 | 전체 설치 조건부 |
| [Ralph](https://github.com/snarktank/ralph) | PRD 항목이 끝날 때까지 새 AI 세션을 반복하는 자율 루프 | 원본 링크 | 제공 Codex 환경의 실행기로 제외 |
| [Ruflo (formerly Claude Flow)](https://github.com/ruvnet/ruflo) | 다중 에이전트·메모리·MCP·라우팅을 결합하는 메타 하네스 | 원본 링크 | 전체 설치 조건부 |
| [Trellis](https://github.com/mindfold-ai/Trellis) | 프로젝트 명세·작업·기록을 지속하고 필요 문맥을 주입하는 엔지니어링 프레임워크 | 원본 링크 | 참고용 |
| [Agent OS](https://github.com/buildermethods/agent-os) | 코드베이스 기준을 정리하고 주입하며 명세를 다듬는 지침 시스템 | 원본 링크 | 참고용 |
| [OpenAI Codex ExecPlans](https://developers.openai.com/cookbook/articles/codex_exec_plans) | 단계별 계획·진행·결정·완료 조건을 파일로 관리하는 공식 예시 | 일부 원본 파일 포함 | 템플릿부터 |
| [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 프로젝트 지침을 Codex에 전달하는 공식 파일 규약 | 원본 링크 | 지침부터 |

## 프로젝트별 적용 조건

### GitHub Spec Kit

templates/*.md를 읽고 필요한 표와 항목만 적용. 전체 CLI 설치는 선택 사항.

- Codex 근거: 공식 문서에 Codex 통합 명시
- 라이선스: MIT
- 확인한 커밋: `d605a15b1926b48e1762b5be5502c8277e8946d5`
- 전체 설치에는 specify CLI 및 Python/uv 등 해당 배포 경로의 의존성이 필요하다.
- 현재 제공된 Codex 버전을 바꾸지 말 것.
- 수록 파일: [spec-template.md](../extras/github/spec-kit/templates/spec-template.md)
- 수록 파일: [plan-template.md](../extras/github/spec-kit/templates/plan-template.md)
- 수록 파일: [tasks-template.md](../extras/github/spec-kit/templates/tasks-template.md)
- 수록 파일: [checklist-template.md](../extras/github/spec-kit/templates/checklist-template.md)
- 수록 파일: [constitution-template.md](../extras/github/spec-kit/templates/constitution-template.md)
- 근거: [원본 1](https://github.com/github/spec-kit) · [원본 2](https://github.github.com/spec-kit/)

### OpenSpec

schemas/spec-driven/templates의 단순 Markdown 양식부터 사용.

- Codex 근거: README에 Codex용 $openspec-propose와 도구별 통합 명시
- 라이선스: MIT
- 확인한 커밋: `6d04a1b58dedc95729d34e4f223d9d483aae210a`
- 전체 CLI는 설치·초기화가 필요하다.
- CLI는 익명 사용 통계를 기본 수집하므로 사용 시 OPENSPEC_TELEMETRY=0 등 공식 옵트아웃 설정 확인.
- 템플릿 파일 자체를 읽는 방식은 CLI 실행과 다르다.
- 수록 파일: [proposal.md](../extras/Fission-AI/OpenSpec/schemas/spec-driven/templates/proposal.md)
- 수록 파일: [design.md](../extras/Fission-AI/OpenSpec/schemas/spec-driven/templates/design.md)
- 수록 파일: [tasks.md](../extras/Fission-AI/OpenSpec/schemas/spec-driven/templates/tasks.md)
- 수록 파일: [spec.md](../extras/Fission-AI/OpenSpec/schemas/spec-driven/templates/spec.md)
- 근거: [원본 1](https://github.com/Fission-AI/OpenSpec)

### Planning with Files

세 Markdown 템플릿으로 계획·발견·진행 기록만 유지.

- Codex 근거: README에 Codex CLI와 .codex용 배포 경로 명시
- 라이선스: MIT
- 확인한 커밋: `5d29800bf8b919ca9a88ee7885b90050b5cb64ed`
- 자동 복구·매턴 주입 기능은 훅 설치와 별도 호환성 확인이 필요하다.
- 일반 텍스트 템플릿만 가져오면 자동 복구 훅까지 설치되는 것은 아니다.
- 수록 파일: [task_plan.md](../extras/OthmanAdi/planning-with-files/templates/task_plan.md)
- 수록 파일: [findings.md](../extras/OthmanAdi/planning-with-files/templates/findings.md)
- 수록 파일: [progress.md](../extras/OthmanAdi/planning-with-files/templates/progress.md)
- 근거: [원본 1](https://github.com/OthmanAdi/planning-with-files)

### Superpowers

필요한 개별 SKILL.md와 참조 파일만 읽고 적용.

- Codex 근거: README에 Codex 설치 경로 존재; 현재 모음에서 일부 원본 이미 제공
- 라이선스: MIT
- 확인한 커밋: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`
- 전체 워크플로의 승인·분기·서브에이전트·테스트 요구를 현재 과제 범위에 맞춰 적용.
- 스킬 간 참조 경로 유지 필요.
- 수록 파일: [SKILL.md](../vendor/obra/superpowers/skills/verification-before-completion/SKILL.md)
- 근거: [원본 1](https://github.com/obra/superpowers)

### BMad Method

브리프·PRD 양식 일부 참고. 전체 설치는 숙련된 경우에만 선택.

- Codex 근거: README에 Codex plugin marketplace 경로 명시
- 라이선스: MIT with trademark notice
- 확인한 커밋: `61e01f82644c4bb533750cfa0d6d61ab61d2cc9b`
- GitHub API license는 NOASSERTION이지만 실제 LICENSE에 MIT 본문과 상표 고지가 있다.
- LICENSE와 TRADEMARK.md·CONTRIBUTORS.md 관련 고지 보존.
- 설치 시 다수 스킬·설정이 생성되며 프로젝트 준비 절차가 추가된다.
- 수록 파일: [prd-template.md](../extras/bmad-code-org/BMAD-METHOD/skills/bmad-prd/assets/prd-template.md)
- 수록 파일: [brief-template.md](../extras/bmad-code-org/BMAD-METHOD/skills/bmad-product-brief/assets/brief-template.md)
- 근거: [원본 1](https://github.com/bmad-code-org/BMAD-METHOD) · [원본 2](https://www.bmadcode.com/method)

### Oh My Codex (OMX)

자료로 보관하고, 환경 호환성과 설정 변경을 확인한 경우에만 설치 검토.

- Codex 근거: Codex CLI 실행 엔진을 유지하는 전용 workflow layer라고 README에 명시
- 라이선스: MIT
- 확인한 커밋: `865fb25eae087a20ebc59fb083e52d630d01a561`
- Node.js 20+와 인증된 Codex CLI 필요; 권장 팀 런타임은 tmux 요구.
- setup은 프로젝트/사용자 설정·AGENTS·훅 등을 변경한다.
- 문서의 Codex 설치·업데이트 예시는 제공 버전 유지 조건과 함께 읽어야 한다.
- 권한 완화 플래그·외부 통합·세션 export를 자동 적용하지 말 것.
- 근거: [원본 1](https://github.com/Yeachan-Heo/oh-my-codex)

### Compound Engineering

ce-plan·ce-doc-review 같은 필요한 개별 지침을 선택적으로 검토.

- Codex 근거: README에 Codex CLI native plugin과 $ce-plan 호출 명시
- 라이선스: MIT
- 확인한 커밋: `fbd794f329f5b65d0ea00a5e6487336c385ff2be`
- /lfg 기본 흐름에는 browser tests, remote push, PR 생성이 포함된다. 제한 환경에서는 그대로 실행하지 않는다.
- 외부 모델 author routing·oracle 기능은 별도 모델 사용 조건을 확인해야 한다.
- 전체 플러그인 설치·재시작 및 기존 Codex의 plugin 지원 여부 확인 필요.
- 근거: [원본 1](https://github.com/EveryInc/compound-engineering-plugin)

### GSD Core

현재 공식 이동 대상. 상태 관리와 요구사항 추적 방식을 참고.

- Codex 근거: README에서 Codex를 지원 런타임으로 명시
- 라이선스: MIT
- 확인한 커밋: `67f661afc4760187740ca0b2e93381266c578169`
- 공식 README는 교차 런타임 호환을 위해 installer 사용 필수라고 명시한다.
- agents/commands 파일만 복사해 정상 설치라고 간주하지 않는다.
- fresh-context subagents·parallel waves·ship/PR 단계가 기본 방법론에 포함되므로 제한 환경과 시간에 맞춘 조정 필요.
- 수록 파일: [state.md](../extras/open-gsd/gsd-core/gsd-core/templates/state.md)
- 수록 파일: [requirements.md](../extras/open-gsd/gsd-core/gsd-core/templates/requirements.md)
- 수록 파일: [continue-here.md](../extras/open-gsd/gsd-core/gsd-core/templates/continue-here.md)
- 수록 파일: [verification-report.md](../extras/open-gsd/gsd-core/gsd-core/templates/verification-report.md)
- 근거: [원본 1](https://github.com/open-gsd/gsd-core)

### Get Shit Done (archived)

구버전 상태·요구사항 양식을 참고하는 용도. 신규 설치 기본 추천 제외.

- Codex 근거: 이전 Codex 지원 이력은 있으나 현재 README는 GSD Core로 이동 안내
- 라이선스: MIT
- 확인한 커밋: `bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815`
- 보관 상태(archived). 현행 프로젝트와 구분합니다.
- 2026-06-26 archived; 현재 소스는 open-gsd/gsd-core로 이동.
- 오래된 설치 명령을 현행 기본 명령으로 안내하지 않는다.
- 근거: [원본 1](https://github.com/gsd-build/get-shit-done) · [원본 2](https://github.com/gsd-build/get-shit-done/blob/main/README.md)

### GSD Codex Fork

공식 이동 대상과 별개의 커뮤니티 포크로 구분해 보관.

- Codex 근거: README에 Codex primary runtime, local/global skill install 경로 명시
- 라이선스: MIT
- 확인한 커밋: `b9317ff784e8eab69789f56982fc033a60224a4e`
- 설치 스크립트가 .codex/skills와 AGENTS.md를 생성한다.
- 다른 런타임용 설치·권한 완화 예시가 함께 있으므로 그대로 일괄 적용하지 않는다.
- 제공 Codex 버전·hook 호환성은 실제 환경에서 확인해야 한다.
- 근거: [원본 1](https://github.com/Oisinwang/get-shit-done-codex)

### Ralph

아이디어 참고용 링크만 제공. 실행 루프는 권장하지 않음.

- Codex 근거: 현재 README 지원 도구는 Amp 또는 Claude Code; Codex 지원 확인 안 됨
- 라이선스: MIT
- 확인한 커밋: `6c53cb0b831ebe8739c6a003e22af14902d8b0b5`
- 원본 실행은 Amp/Claude Code 인증을 요구한다.
- 외부 AI 금지 환경의 제공 Codex 대체 실행기로 사용하지 않는다.
- 자동 반복은 호출 비용과 종료 조건 관리가 필요하다.
- 근거: [원본 1](https://github.com/snarktank/ralph)

### Ruflo (formerly Claude Flow)

고급 참고용. 단기 과제 기본 구성에 자동 설치하지 않음.

- Codex 근거: README에 Codex/MCP client setup 및 Codex adapter 문서 존재
- 라이선스: MIT
- 확인한 커밋: `7f6fb3345b7f4ea1d7acc4905ea88bad29136066`
- 기본 소개 경로에는 Claude Code 플러그인 설치가 포함된다. Codex 경로와 분리 필요.
- MCP 설정, 모델 routing, 추가 저장소/서비스의 실제 동작과 통신 범위를 확인해야 한다.
- 전체 런타임 호환성·평가 환경 사용 가능 여부는 미검증.
- 근거: [원본 1](https://github.com/ruvnet/ruflo) · [원본 2](https://github.com/ruvnet/ruflo/blob/main/v3/%40claude-flow/codex/README.md)

### Trellis

구조 참고용 링크. 이번 모음에는 원본 파일 미포함 권장.

- Codex 근거: README에 Codex 관련 플랫폼 링크와 지원 안내
- 라이선스: AGPL-3.0
- 확인한 커밋: `f089cb3286071199e84118dee86b6d76aab032f1`
- 현재 LICENSE는 AGPL-3.0이며 MIT로 표시하면 안 된다.
- 재배포/결합 시 라이선스 적용 범위를 별도로 확인해야 한다.
- 전체 설정·주입 훅은 제공 런타임에서 호환성 확인 필요.
- 근거: [원본 1](https://github.com/mindfold-ai/Trellis)

### Agent OS

공개 Markdown의 standards·shape-spec 구조 참고.

- Codex 근거: README는 Claude Code·Cursor·Antigravity·other AI tools 명시; Codex native 설치는 이번 확인에서 확정 못함
- 라이선스: MIT
- 확인한 커밋: `e892e61d322759165e7d9173e92c1010406c9f4d`
- Codex에서 텍스트로 읽는 것과 공식 native 통합은 구분.
- 설치 스크립트를 실행하기 전에 생성 경로와 다른 런타임 설정 여부 확인.
- 근거: [원본 1](https://github.com/buildermethods/agent-os)

### OpenAI Codex ExecPlans

계획 문서 구조를 참고하며 현재 과제에 필요한 항목만 적용.

- Codex 근거: OpenAI 공식 Codex Cookbook 예시
- 라이선스: MIT
- 확인한 커밋: `a8132ca2f7a5de3a6cf15d9e79d172787b42b697`
- 원문의 모델 추천·장시간 작업·commit 지시는 현재 환경과 과제 규정을 우선하여 적용.
- 원본을 읽는 것만으로 자동 재개·반복 실행기가 생기지는 않는다.
- 수록 파일: [codex_exec_plans.md](../extras/openai/openai-cookbook/articles/codex_exec_plans.md)
- 근거: [원본 1](https://developers.openai.com/cookbook/articles/codex_exec_plans)

### Codex AGENTS.md

기존 프로젝트 지침을 확인하고 필요한 짧은 지침만 추가.

- Codex 근거: 공식 지원 파일 규약
- 라이선스: 공식 문서 링크만 제공
- 기존 AGENTS.md를 덮어쓰거나 전역 설정을 임의 변경하지 않는다.
- 현재 세션 중 새로 추가한 문서는 명시적으로 읽게 한다.
- 근거: [원본 1](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## 설치·실행 경계

원본 템플릿과 라이선스를 고정 커밋에서 가져와 보관했습니다. 프레임워크 전체나 AI 실행기를 일괄 설치하지 않았고, 제공 환경에서의 런타임 호환성은 검증하지 않았습니다.

기본 구성은 Codex 업데이트, 새 AI 인증, 외부 모델 호출, 원격 업로드, 브라우저 자동 조작, 반복 AI 호출을 수행하지 않습니다. 외부 도구의 원문에 그런 단계가 있더라도 현재 환경에서 허용된 작업만 선택합니다. 원문의 설치 명령은 검토 없이 실행하지 않습니다.

정적 템플릿에는 CLI 전용 명령·다른 문서 자리표시자가 남아 있을 수 있습니다. 필요한 항목을 현재 작업에 맞춰 쓰며, 파일 일부를 보관했다고 전체 명령이 작동하는 것으로 보지 않습니다.
