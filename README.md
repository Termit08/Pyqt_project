# Структура проекта

## Папка data
в папке data у меня хранятся папки
с фонами, картинки дизайнов, дизайны в формате ui
1.  **Ui.designes**
>-**game_window.ui** - Дизайн окна с игрой в формате ui
>
>-**main_menu.ui** - Дизайн главного меню в формате ui
2.  **phones**
>-**game_phone.jpeg** - Фон окна с игрой
>
>-**main_menu.jpg** - Фон главного меню
3.  **designs_picture**
>-**main_menu_design.png** - Фото главного меню
>
>-**instruction.png** - Фото с иструкцией
## Папка src
в папке хранится весь код, а также дизайны в формате py
### Windows 
Папка с классами и методами
1.  **main.py** - Окно с главным меню и с классом **Main**
####   Методы класса Main:
>-**__init__** - Инициализация
>
>-**go_game** - Эта функция открывает окно с игрой
>
>-**go_instruction** - Эта функия открывает открывается окнос с инструкцией
2.  **game.py** - Окно с игрой и с классом **Game_window**
####   Методы класса Game_window:
>-**__init__** - Инициализация
>
>-**random_number** - Функция, которая выдаёт пользователю случайный бокс с суммой, также здесь формируется нумерация кнопок и случайно сгенерированный словарь, а  также в поле с возиожными суммами выйгрыша появляются суммы
>
>-**turn** - Эта фунция удаляет кнопку,которую выделил пользователь, а также убирает из списка возможных выиграшей выбывшую сумму, и она отображается в окне с выбывшими суммами
>
>-**banker** - Функция, при которой банкир либо предлагает, либо предлагает сумму окончания игры
>
3.  **window_with_instruction.py** - Окно с инструкцией и с классом **Instruction**
####  Методы класа Instruction:
>-**__init__** - Инициализация
### py.designs
Папка с дизайнами в формате py
>-**main_menu.py** - Дизайн главного меню в формате py
>
>-**game_window.py** - Дизайн окна с игрой
