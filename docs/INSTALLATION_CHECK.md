# 설치 확인 기록

[README](../README.md) · [사용 안내](USAGE.md) · [출처·라이선스](../SOURCES.md)

## 확인 결과

2026-10-28, 공개 저장소에서 `verification-before-completion`을 내려받아 Codex 사용자 스킬 폴더에 설치했습니다. 새 Codex 실행에서 목록 인식, 지침 읽기, 검증 명령 실행을 확인했습니다.

| 항목 | 결과 |
|---|---|
| 공개 저장소 다운로드 | GitHub 인증 환경변수 없이 다운로드 성공 |
| 설치 | 내장 Skill Installer의 download 방식으로 완료 |
| 원본 일치 | 설치한 SKILL.md의 SHA-256이 sources.lock.json과 일치 |
| 출처 보존 | MIT LICENSE와 원본 저장소·커밋 기록 포함 |
| Codex 인식 | 새 실행에서 스킬 이름과 설치 경로 확인 |
| 지침 읽기 | 설치된 SKILL.md 읽기 명령 종료 코드 0 |
| 실행 확인 | 검증 명령 종료 코드 0, 예상 출력 일치 |

## 확인 환경

| 항목 | 값 |
|---|---|
| 운영체제 | macOS |
| 실행 도구 | 데스크톱 앱에 포함된 Codex CLI 0.165.0-alpha.1.2 |
| 실행 범위 | 읽기 전용 임시 세션 |
| 설치 위치 | `~/.agents/skills/verification-before-completion` |
| 다운로드 저장소 | [parkhyunjae01/ai-work-skills](https://github.com/parkhyunjae01/ai-work-skills) |
| 확인한 저장소 커밋 | `1042d347d6455af06cd972859c358f84212fca06` |
| 원본 | [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) |

설치한 경로:

```text
vendor/obra/superpowers/skills/verification-before-completion
```

확인한 `SKILL.md` SHA-256:

```text
2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3
```

## 실행 기록

새 Codex 세션에 설치된 스킬을 찾고 읽도록 요청한 후 다음 명령의 실행을 확인했습니다.

```bash
python3 -c 'assert sum([1, 2, 3]) == 6; print("verification probe passed")'
```

```text
verification probe passed
Exit code: 0
```

이 검사는 다운로드·설치·탐색·지침 읽기·기본 명령 실행을 확인합니다. 스킬의 성능 향상이나 복잡한 작업의 정확도를 측정한 결과는 아닙니다.

## 적용 범위

- 이 확인은 독립형 스킬 한 개를 대상으로 합니다. 후보 전체를 일괄 설치한 결과가 아닙니다.
- 상위 `CONNECTORS.md` 등을 참조하는 업무 스킬은 원래 폴더 구조를 유지해 읽어야 합니다. 동일한 단일 폴더 설치가 모든 스킬에 적합하지는 않습니다.
- 특정 회사·평가 환경에서의 설치 허용 여부나 네트워크 지원을 보증하지 않습니다. 해당 환경의 규정을 별도로 확인해야 합니다.
- 실제 설치한 스킬은 다음 대화부터 사용할 수 있습니다. 필요하면 `$verification-before-completion`으로 지정합니다.
