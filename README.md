# CLI Tools

## 1. sys_tool.py

```powershell
python src/sys_tool.py
python -c "import src.sys_tool"
```

## 2. click_tool.py

```powershell
python src/click_tool.py say --name Alice
python src/click_tool.py say --name peter
python src/click_tool.py --help
```

## 3. fire_expose.py

Функції: `greet(name)` і `goodbye(name)` у файлі `src/utils.py`.

```powershell
python src/fire_expose.py greet Alice
python src/fire_expose.py goodbye Bob
python src/fire_expose.py --help
```