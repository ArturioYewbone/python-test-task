Простой инструмент на Python для генерации отчётов о зарплате сотрудников на основе CSV-файлов.

Возможности
- Поддержка нескольких входных файлов
- Расчёт выплат на основе часов и ставки
- Группировка по отделам
- Чистый форматированный вывод с использованием `tabulate`
- Поддержка альтернативных названий столбцов: `rate`, `hourly_rate`, `salary`
- Покрытие тестами с `pytest`

Пример входного CSV
```csv
id,email,name,department,hours_worked,rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40

Как запустить

python main.py data1.csv data2.csv --report payout