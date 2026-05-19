%%{init: {'theme': 'base', 'themeVariables': { 'background': 'transparent', 'fontSize': '15px', 'fontFamily': 'system-ui, sans-serif' }}}%%
flowchart TD
    %% Стили узлов
    classDef external fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#111;
    classDef process fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#111;
    classDef datastore fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#111;
    classDef legend fill:#fafafa,stroke:#999,stroke-width:1px,color:#111,stroke-dasharray: 4 4;

    %%  Условные обозначения (Легенда)
    subgraph Legend["Условные обозначения"]
        direction LR
        LE["Внешняя сущность"]:::external
        LP["Процесс"]:::process
        LD["Хранилище данных"]:::datastore
    end
    class Legend legend;

    %% Внешние сущности
    Client["Клиент"]:::external
    Admin["Администратор"]:::external

    %% Процессы
    P1["1. Валидация и создание заявки"]:::process
    P2["2. Управление статусами"]:::process
    P3["3. Агрегация данных для аналитики"]:::process

    %% Хранилища данных
    D1[("D1: Заявки<br/>CSV/SQLite")]:::datastore
    D2[("D2: Сессии и настройки")]:::datastore

    %% Потоки данных
    Client -->|"1.1 Данные формы (услуга, имя, телефон)"| P1
    P1 -->|"1.3 Подтверждение отправки"| Client
    P1 -->|"1.2 Новая запись (статус: Новая)"| D1

    Admin -->|"2.1 Проверка авторизации"| D2
    D2 -->|"2.2 Данные сессии"| Admin

    Admin -->|"2.3 Запрос списка заявок"| P2
    D1 -->|"2.4 Чтение"| P2
    P2 -->|"2.5 Список заявок"| Admin
    Admin -->|"2.7 Изменение статуса"| P2
    P2 -->|"2.8 Обновление записи"| D1

    Admin -->|"3.1 Данные для отчётов"| P3
    P3 -->|"2.6 Отображение списка"| Admin
    P3 -->|"3.3 Графики и метрики"| Admin

    %% 🖋️ Принудительное оформление стрелок и подписей
    linkStyle default stroke:#333,stroke-width:1.5px,color:#111;
