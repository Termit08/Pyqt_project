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
В папке хранится весь код, все классы, а также дизайны в формате py

Классы:
1.  **main.py** - Окно с главным меню и с классом **Main**
####   Методы класса Main:
>-**__init__** - Инициализация
>
>-**go_game** - Эта функция открывает окно с игрой
>
>-**go_instruction** - Эта функия открывает открывается окнос с инструкцией
2.  **game.py** - Окно с игрой и с классом **Game_window** и с классом **Dictionary**
####   Методы класса Game_window:
>-**__init__** - Инициализация
**Классы:**
>-**random_number** - Функция, которая выдаёт пользователю случайный бокс с суммой, также здесь формируется нумерация кнопок и случайно сгенерированный словарь, а  также в поле с возиожными суммами выйгрыша появляются суммы
>
>-**turn** - Эта фунция удаляет кнопку,которую выделил пользователь, а также убирает из списка возможных выиграшей выбывшую сумму, и она отображается в окне с выбывшими суммами
>
>-**banker** - Функция, при которой банкир либо предлагает, либо предлагает сумму окончания игры
>
>-**offer** - В этой функции генерируется и предлагается определённая сумма
>
>-**rejected_sum** - Эта функция нужна, если человек отказался от предложения, она высвечивает специальный текст в окне банкира
>
>-**winning_sum** - Функция нужна, если человек согласился на эту сумму. Также в окне появляется сумма выйгрыша и в окне с банкиром появляется специальный текст
>
>-**change** - Эта функция предлагает обмен, на который пользователь должен лтбо согласиться, либо отказаться
>
>-**accept_change** - Эта функция нужна, если пользователь согласился на обмегн и она ему предлагает выбрать из оставшихся коробок, также в окне с банкиром появляется специальный текст
>
>-**confirm** - Эта функция кнопки **confirm_button**, при нажатии которой пользователь подтверждает свой выбор и в окне с номером коробки, появляется новый номер
>
>-**reject_change** - Функция, которая нужна на случай, если пользователь отказывается от обмена, функция высвечивает спецтальный текст в окне с банкиром и продолжает игру
>
>-**game_over** - Функция, которая высвечивает сумму выйгрыша в специальном окне, если оно пустое
>
>-**go_dictionary** - Функция открывает для нас класс **Dictionary**, в котором можно посмотреть в какой коробке, лежала та или иная сумма
####   Методы класса Dictionary:
>-**__init__** - Инициализация
>
>-**show_dictionary** - Фунция кнопки **show_button**, при нажатии, которой пользователя показывается, где лежала та или иная функция
3.  **window_with_instruction.py** - Окно с инструкцией и с классом **Instruction**
####  Методы класа Instruction:
>-**__init__** - Инициализация
### py.designs
Папка с дизайнами в формате py
>-**main_menu.py** - Дизайн главного меню в формате py
>
>-**game_window.py** - Дизайн окна с игрой
>
>-**dictionary_window.py** - Дизайн окна со словарём
