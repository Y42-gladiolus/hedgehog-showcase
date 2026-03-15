# 🦔 Hedgehog Core — Визуализация Отказоустойчивости

**Демо-проект портфолио** — демонстрация архитектуры верификации с консенсусом.

🌐 **Live Demo:** https://y42-gladiolus.github.io/hedgehog-showcase/

---

## 📋 КРАТКОЕ ОПИСАНИЕ

Система демонстрирует **визуализацию отказоустойчивости** через независимую верификацию:

- **5 независимых реализаций** (OCaml/Rust/Ada/Nim/Zig)
- **4 ортогональных стражника** (Forth/Scheme/Julia/Lean4)
- **75% консенсус** (Byzantine fault tolerance)
- **SQLite audit trail** (доказательство для аудиторов)

---

## 💼 ПРАКТИЧЕСКАЯ ЦЕННОСТЬ (для бизнеса)

### Сравнение подходов

| Задача | Традиционный подход | Hedgehog Core |
|--------|---------------------|---------------|
| **Проверка целостности** | ✅ Считает байты | ✅ Считает + 5 языков подтверждают |
| **Если баг в CRC32 библиотеке** | ❌ Никто не узнает | ✅ 4 из 5 языков покажут mismatch |
| **Если атака на логи** | ❌ Логи можно подменить | ✅ SQLite audit + consensus |
| **Если компрометирован 1 компонент** | ❌ Система пала | ✅ 75% консенсус продолжает работать |
| **Compliance / Аудит** | ❌ "Доверяйте коду" | ✅ "Вот 3 голоса в БД за последний час" |
| **Новый тип логов** | ❌ Переписывать код | ✅ rules.json без изменения ядра |

### Ключевое отличие

> **Традиционный скрипт:** "Доверяйте мне, он работает"
>
> **Hedgehog Core:** "Не доверяйте никому. Проверяйте консенсус."
>
> **Когда всё правильно — разницы нет.**  
> **Когда что-то НЕПРАВИЛЬНО — разница спасает.**

---

## 🔐 ГДЕ БЕЗОПАСНОСТЬ? (конкретно)

| Угроза | Традиционный подход | Hedgehog |
|--------|---------------------|----------|
| **Баг в библиотеке CRC32** | Пропустит ошибку | 4 других языка покажут mismatch |
| **Подмена логов** | Заметят постфактум | SQLite WAL + consensus timestamp |
| **Компрометация сервера** | Полная потеря | Нужно скомпрометировать 3 из 5 языков |
| **Дрейф спецификации** | Никто не заметит | Lean4/Coq spec → тесты упадут |
| **Человеческая ошибка** | Один человек = точка отказа | Consensus = коллективная ответственность |

---

## 🧩 АРХИТЕКТУРА ПЛАГИНОВ

### Пример: Добавить новый тип лога

**Без изменения кода** — только конфигурация:

```json
// rules.json — добавить 3 строки
"new_log_type": {
  "meaning": "Security alert",
  "priority": "critical",
  "color": "red",
  "action": "alert"
}
Результат:
✅ Без перекомпиляции
✅ Без изменения ядра
✅ Без риска
ЧТО ПРОДАЁМ? (ценность для клиента)
Компонент
Ценность для бизнеса
5 языков × 113 bytes
Независимая верификация (не доверяй одному)
4 стражника × 75%
Byzantine tolerance (отказоустойчивость)
SQLite audit.db
Compliance (доказательство для аудиторов)
Plugin architecture
Масштабируемость (новые логи без переписывания)
Semantic parser
Человекочитаемость (не байты, а "✅ Система цела")
ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
Сфокусируйся на конкретной боли, не продавай "верификацию":
Use-Case
Боль
Решение Hedgehog
Финтех
"Как доказать регулятору что логи не подменены?"
SQLite audit + 75% consensus
Медицина
"Как убедиться что данные не искажены?"
5 независимых проверок
IoT
"Что если одно устройство скомпрометировано?"
Byzantine tolerance (3 из 5)
DevOps
"Как быстро добавить новый тип лога?"
Plugin: rules.json без перекомпиляции
БЫСТРЫЙ СТАРТ
1. Скачивание
# Git
git clone https://github.com/Y42-gladiolus/hedgehog-showcase.git
cd hedgehog-showcase

# Или скачай ZIP с Releases
wget https://github.com/Y42-gladiolus/hedgehog-showcase/releases/download/v1.0/hedgehog-showcase-v1.0.tar.gz
tar -xzf hedgehog-showcase-v1.0.tar.gz
. Запуск
# Автоматический запуск всех реализаций
./run.sh

# Или по отдельности
./bin/hedgehog-ocaml
./bin/hedgehog-rust
./bin/hedgehog-ada
./bin/hedgehog-nim
./bin/hedgehog-zig
Ожидаемый вывод:
Serialized: 113 bytes
CRC32: xxxxxxxx
✓ Frame v1: PASS
. Просмотр витрины
# Linux
xdg-open index.html

# macOS
open index.html

# Windows
start index.html
СТРУКТУРА ПРОЕКТА
hedgehog-showcase/
├── bin/                      # Бинарники (5 реализаций)
│   ├── hedgehog-ocaml        # Reference implementation
│   ├── hedgehog-rust         # Performance
│   ├── hedgehog-ada          # Safety-critical
│   ├── hedgehog-nim          # Fast compilation
│   └── hedgehog-zig          # C-compatible
├── run.sh                    # Скрипт запуска
├── rules.json                # Конфигурация (без кода)
├── index.html                # Витрина (веб-демо)
├── README.md                 # English documentation
├── README_RU.md              # Русская документация
└── quick-start.md            # Быстрый старт
КОНФИГУРАЦИЯ
Настройка правил (без кода!)
Отредактируй rules.json:
{
  "consensus_threshold": 0.75,
  "actions": {
    "log": { "severity": "info", "notify": false },
    "warn": { "severity": "warning", "notify": true },
    "alert": { "severity": "critical", "notify": true, "sound": true }
  },
  "frame_sizes": {
    "113": { "meaning": "Standard frame", "priority": "normal" },
    "other": { "meaning": "Anomaly detected", "priority": "high" }
  }
}
ДЛЯ СПЕЦИАЛИСТОВ
Архитектура
Clean Core + Dirty Plugins — ядро верифицировано, плагины гибкие
5 независимых реализаций — каждая на своём языке
4 ортогональных стражника — разные парадигмы (Stack/Symbolic/Array/Formal)
75% консенсус — Byzantine fault tolerance (3 из 4 должны согласиться)
Верификация
Coq: Классические доказательства (25KB spec)
Lean4: Dependent types (WIP)
Agda: Homotopy types (planned)
Исходный код
Полный исходный код (включая доказательства):
🔗 https://codeberg.org/Y42-gladiolus/hedgehog-core
КОНТАКТЫ
Разработчик: Yuri Statkevich (Y42-gladiolus)
Для заказов и предложений:
Email: [твой email]
Telegram: [твой Telegram]
GitHub: https://github.com/Y42-gladiolus
 ЛИЦЕНЗИЯ
MIT License — используйте на свой страх и риск.
"Не доверяйте никому. Проверяйте консенсус."
Hedgehog Core v1.0 — Когда всё правильно — разницы нет.
Когда что-то НЕПРАВИЛЬНО — разница спасает.
