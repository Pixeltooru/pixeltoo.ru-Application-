### Описание кода для GitHub

#### Описание проекта

Этот проект предназначен для управления ПК через MQTT-брокер и отправки статуса активного окна. С помощью этой программы можно выполнять удаленные команды, такие как выключение компьютера, перевод в спящий режим и пробуждение, а также отслеживать, какое окно активно в данный момент.

---

#### Основные функции:

1. **Удаленное управление ПК через MQTT:**
   - **Выключение компьютера** (`shutdown_pc()`).
   - **Переход в спящий режим** (`sleep_pc()`).
   - **Обработка пользовательских команд**, таких как `shutdown`, `sleep`, `wake_up`, и пользовательская логика `OFF()`.

2. **Мониторинг активного окна:**
   - Отправка названия активного окна через MQTT в заданный топик.
   - Обработка окон с учетом пользовательских условий (например, выделение окон с YouTube или Яндекс).

3. **Интеграция с MQTT:**
   - Подключение к MQTT-брокеру с использованием учетных данных.
   - Подписка на топики для получения команд.
   - Публикация статуса активного окна в отдельный топик.

4. **Обработка активного окна:**
   - Использует библиотеку `pygetwindow` для получения текущего активного окна.
   - Обработка названия активного окна и выполнение действий в зависимости от содержания.

---

#### Настройка и запуск:

1. Установите необходимые библиотеки (см. файл `requirements.txt` ниже).
2. Настройте параметры подключения в разделе конфигурации:
   - **`BROKER`**: IP-адрес вашего MQTT-брокера.
   - **`PORT`**: Порт для подключения.
   - **`USERNAME` и `PASSWORD`**: Учетные данные.
3. Запустите скрипт, выполнив команду:
   ```bash
   python main.py
   ```

---

#### Структура MQTT:

- **Команды**:
  - `home/pc/commands` — принимает команды, такие как `shutdown`, `sleep`, `wake_up`, `OFF`.
- **Статус**:
  - `home/pc/status/sensor_pc_active_window` — отправляет название текущего активного окна.

---



Установите их командой:

```bash
pip install -r requirements.txt
```

---

#### Примечания:

 **Платформа**: Код разработан для Windows, так как использует команды `os.system` для управления питанием и библиотеку `pygetwindow`.
