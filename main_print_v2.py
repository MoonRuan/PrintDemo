# pip install rich 가 필요합니다.
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 변수 설정
name = "Alice"
age = 25
score = 95.5
data = {"name": name, "age": age, "score": score}

# 1) 문자열의 출력 (f-string)
rprint(f"[bold green]Hello, {name}![/]/ Your score is [cyan]{score:.2f}[/]")

# 2) 패널(Panel)로 멀티라인 출력
panel_text = f"""
[bold]Student Info[/]
Name: [yellow]{name}[/]
Age: [magenta]{age}[/]
Score: [cyan]{score:.2f}[/]
"""
rprint(Panel(panel_text, title="Profile", border_style="blue"))

# 3) 테이블을 생성하여 디스크리미너리/리스트로 출력
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")
for k, v in data.items():
    table.add_row(k, str(v))
rprint(table)

# 4) sep, end 옵션과 그 다음 출력 (rich.print도 동일하게 적용)
rprint("2025", "09", "23", sep="-", end="\n")
