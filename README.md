# AI Work Skills

공개 AI 작업 스킬을 한 곳에서 찾고, 필요한 지침만 골라 쓰기 위한 한국어 모음입니다.

**저장소 주소: https://github.com/parkhyunjae01/ai-work-skills**

개발·검증·데이터·요구사항·운영·고객지원 스킬 후보 32개를 정리했습니다. 재배포 조건을 확인한 원본은 참조 파일과 라이선스까지 보관하고, 나머지는 원본 링크를 제공합니다. 플러그인 6개·MCP 3개·모델별 역할 안내도 함께 볼 수 있습니다.

## Codex에 이렇게 말하세요

> 공개 저장소 https://github.com/parkhyunjae01/ai-work-skills 를 내려받고 README.md와 catalog.json을 읽어줘. 내 작업의 요구사항을 먼저 확인한 뒤 필요한 스킬 2~3개를 골라, local_path의 SKILL.md와 연결된 참조 파일을 읽고 이번 작업에 적용해줘. link-only 항목은 자동으로 내려받거나 설치하지 마. 원본 지침보다 현재 환경의 규정과 내 요청을 우선하고, 외부 계정 연결이나 데이터 전송이 필요한 부분은 따로 알려줘.

저장소 이름만 알려주는 것보다 **`parkhyunjae01/ai-work-skills` 또는 전체 URL**을 알려주는 것이 확실합니다. 검색 기능이 없어도 공개 GitHub 다운로드가 허용된 환경에서는 알려진 주소로 접근할 수 있습니다. 네트워크·명령 실행이 막혀 있으면 이 방법도 제한됩니다.

직접 다운로드할 때:

```bash
git clone https://github.com/parkhyunjae01/ai-work-skills.git
cd ai-work-skills
```

**내려받기만 하면 모든 스킬이 자동 활성화되는 구조는 아닙니다.** 선택한 원본 지침을 현재 대화에서 읽고 적용하는 방식입니다. `/skills`에 등록하는 전역 설치나 계정 설정 변경을 자동으로 수행하지 않습니다. 특히 업무 스킬을 한 폴더로 평탄화하면 `../../CONNECTORS.md` 같은 상대경로가 깨지므로 `vendor/` 구조를 유지하세요.

## 무엇부터 고를까?

| 작업 | 선택할 후보 | 로컬 진입점 |
|---|---|---|
| 완료 여부 검증 | verification-before-completion | [지침](vendor/obra/superpowers/skills/verification-before-completion/SKILL.md) |
| 모호한 요구사항 정리 | write-spec | [지침](vendor/anthropics/knowledge-work-plugins/product-management/skills/write-spec/SKILL.md) |
| 화면 설계·구현 | frontend-design + 완료 검증 | [화면 지침](vendor/anthropics/skills/skills/frontend-design/SKILL.md) |
| 데이터 구조 조사 | explore-data | [지침](vendor/anthropics/knowledge-work-plugins/data/skills/explore-data/SKILL.md) |
| 분석 결과 검산 | validate-data | [지침](vendor/anthropics/knowledge-work-plugins/data/skills/validate-data/SKILL.md) |
| 오류 원인 추적 | systematic-debugging + 연결된 테스트·검증 지침 | [지침](vendor/obra/superpowers/skills/systematic-debugging/SKILL.md) |
| 업무 프로세스 개선 | process-optimization | [지침](vendor/anthropics/knowledge-work-plugins/operations/skills/process-optimization/SKILL.md) |
| 고객 문의 분류 | ticket-triage | [지침](vendor/anthropics/knowledge-work-plugins/customer-support/skills/ticket-triage/SKILL.md) |

모든 스킬을 한 번에 읽히기보다 실제 작업에 필요한 소수부터 선택하세요. 원본에 있는 다른 모델·하위 에이전트·브라우저 자동화·외부 서비스 호출을 사용할 수 있다고 가정하지 마세요. 사용할 도구와 환경 제약은 현재 작업에서 확인해야 합니다.

## 전체 안내

- [스킬 32개 비교표](docs/CATALOG.md): 용도, 정확한 원본 주소, 주의할 조건
- [모델 역할 분담](docs/MODELS.md): Sol 6.1·Luna 6·Terra 5.6·Sol 6.0 운영 예시
- [플러그인·MCP](docs/PLUGINS.md): 계정 연결과 외부 전송 조건
- [출처와 라이선스](SOURCES.md): 원본 커밋과 보관 범위
- [기계가 읽는 목록](catalog.json): 원본 주소, 로컬 경로, bundled/link-only 상태
- [원본 파일 기록](sources.lock.json): 고정 커밋과 파일별 SHA-256

다운로드 뒤 파일 누락·변경 여부는 `python3 scripts/verify_bundle.py`로 확인할 수 있습니다(Python 3.9 이상). 네트워크를 사용하거나 포함된 스킬 스크립트를 실행하지 않고, 목록·체크섬·상위 연결 문서만 검사합니다.

## 보관 방식과 제한

- `vendor/`의 파일은 공개 원본의 바이트를 수정하지 않고 보관합니다. 라이선스·NOTICE와 상위 연결 문서, 같은 저장소의 연결 스킬도 필요한 범위에서 포함합니다.
- 기본 후보 중 24개는 원본을 보관하고, 8개는 링크만 제공합니다. 연결 스킬이 추가로 들어 있으므로 폴더의 SKILL.md 개수와 후보 32개는 다를 수 있습니다.
- Anthropic `pdf`, `xlsx`, `docx`, `pptx`는 제한 라이선스로 인해 원본 파일을 포함하지 않습니다. `web-design-guidelines`는 이 조사에서 재배포 라이선스를 확정하지 못해, `security-best-practices`는 구 저장소 자료라 링크만 제공합니다.
- Vercel의 React·Composition 지침에는 MIT 표기가 있으나 확인한 커밋에서 동봉할 LICENSE/NOTICE 파일을 찾지 못해 이 모음에서는 링크로 제공합니다. 사용 금지라고 판정한 것이 아니라 재배포 확인을 보류한 것입니다.
- 플러그인 계정·API 키·외부 AI·런타임은 이 저장소가 제공하지 않습니다. 원본의 Claude 전용 명령이나 도구 등록은 Codex에 자동 이식되지 않습니다.
- 전체 부속 코드 보안 감사나 모든 환경의 동작 검증을 완료했다는 의미는 아닙니다. 스크립트를 실행하기 전 필요한 도구와 동작을 확인하세요.
- 공개 자료라는 이유만으로 특정 평가·회사 환경에서 허용되는 것은 아닙니다. 해당 환경의 규정을 우선하세요.

자료 확인일: **2026-10-28**. 업데이트는 새 원본과 라이선스를 확인한 뒤 별도 반영합니다.

## 라이선스

이 저장소에서 새로 작성한 안내 문서는 [MIT](LICENSE)입니다. **`vendor/`의 제3자 파일에는 각 원본 라이선스가 적용되며, 루트 MIT로 재라이선스하지 않습니다.** 원저자와 라이선스 위치는 [SOURCES.md](SOURCES.md)를 확인하세요.
