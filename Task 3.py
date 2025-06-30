import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # автоматично скидає стиль після кожного print

def print_directory_tree(path: Path, indent: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{Style.BRIGHT}{item.name}{Style.RESET_ALL}/")
                print_directory_tree(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        sys.exit(1)
    directory_path = Path(sys.argv[1])
    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.{Style.RESET_ALL}")
        sys.exit(1)
    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"Структура директорії: {directory_path.resolve()}\n")
    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()
