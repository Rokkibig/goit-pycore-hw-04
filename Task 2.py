def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"Некоректний рядок у файлі: {line.strip()}")
                    continue
                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# ====== ОСНОВНИЙ КОД ДЛЯ ЗАПУСКУ ======

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
