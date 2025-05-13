import argparse
from collections import defaultdict
from tabulate import tabulate
from typing import List, Dict, Any, Callable


def calculate_payout(hours_worked: int, hourly_rate: int) -> int:
    """Считает зарплаты"""
    return hours_worked * hourly_rate


def generate_payout_report(files: List[str]) -> None:
    """Генерирует отчет по зарплатам"""
    for file in files:
        print(f"Файл: {file}")
        records: List[Dict[str, str]] = read_csv_manually(file)

        departments: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for r in records:
            hours = int(r.get("hours_worked", 0))
            rate = int(r.get("hourly_rate") or r.get("rate") or r.get("salary") or 0)#если разные названия столбцов менять тут
            payout = calculate_payout(hours, rate)

            r["hours_worked"] = hours
            r["hourly_rate"] = rate
            r["payout"] = payout

            departments[r["department"]].append(r)

        for dept, employees in departments.items():
            print(dept)
            table: List[List[Any]] = []
            total_hours: int = 0
            total_payout: int = 0

            for emp in employees:
                table.append([
                    "------------",
                    emp["name"],
                    emp["hours_worked"],
                    emp["hourly_rate"],
                    f"${emp['payout']}"
                ])
                total_hours += emp["hours_worked"]
                total_payout += emp["payout"]

            table.append(["Summa", "", total_hours, "", f"${total_payout}"])
            print(tabulate(table, headers=["", "name", "hours", "rate", "payout"]))
            print()


def generate() -> None:
    """Заглушка для нового отчета"""
    print("Что-то еще")


def read_csv_manually(filepath: str) -> List[Dict[str, str]]:
    """Чтение входного файла"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return []

    if not lines:
        print(f"Файл пустой: {filepath}")
        return []

    header: List[str] = lines[0].strip().split(",")
    data: List[Dict[str, str]] = []

    for line in lines[1:]:
        fields: List[str] = line.strip().split(",")
        record: Dict[str, str] = dict(zip(header, fields))
        data.append(record)

    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация отчётов по сотрудникам из CSV-файлов.")
    parser.add_argument("files", nargs="+", help="Пути к входным CSV-файлам (можно несколько)")
    parser.add_argument("--report", required=True, choices=["payout", "maybe"], help="Тип отчёта")

    args = parser.parse_args()
    report_handlers: Dict[str, Callable[[List[str]], None]] = {
        "payout": generate_payout_report,
        "maybe": generate
    }

    report_func = report_handlers.get(args.report)
    report_func(args.files)

if __name__ == "__main__":
    main()
