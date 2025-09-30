# Python Print Examples – Quick Guide

이 저장소는 Python의 다양한 `print()` 사용법을 짧은 예제로 보여주고, 
VS Code/터미널/Jupyter에서 실행하는 방법만 간단히 정리합니다.

---

## 파일 목록

### 1) `main_print_v1.py`
- **설명**: 표준 `print()` 활용 예제.
- **주요 기능**
  - 기본 출력, 여러 값 출력(`sep`, `end`)
  - f-string, `str.format()`, C 스타일(`%`) 포맷
  - 딕셔너리 출력, 멀티라인 출력(`\n`, 삼중따옴표)
  - 간단한 계산/함수 호출을 포함한 f-string
- **실행 방법**:
  - VS Code: 파일 열고 우측 상단 **Run Python File**(▶)
  - 터미널:  
    - Windows: `python main_print_v1.py` (또는 `py main_print_v1.py`)  
    - macOS/Linux: `python3 main_print_v1.py`

---

### 2) `main_print_v2.py`
- **설명**: 콘솔을 보기 좋게 꾸미기 위해 `rich` 라이브러리를 사용하는 예제.
- **주요 기능**
  - 컬러/스타일 텍스트 출력 (`rich.print`)
  - `Panel` 로 박스형 테이블/패널 출력
  - `Table` 로 딕셔너리/레코드 출력
  - `end`, `sep` 옵션 조합
- **실행 전 준비**: `pip install rich`
- **실행 방법**:
  - VS Code: 파일 열고 **Run Python File**(▶)
  - 터미널:  
    - Windows:
      ```powershell
      pip install rich
      python main_print_v2.py
      ```
    - macOS/Linux:
      ```bash
      pip install rich
      python3 main_print_v2.py
      ```
