﻿##############################################################################
# The tenant v1.0 demo scriptcode
##############################################################################
# Настройки и конфигурация

init -1 python hide:
    
    config.gl_resize = False # Запрет на ресайз окна игры # Наблюдается плавающий баг с размерами окна...
    
    config.developer = True # Для отладки
    
    config.window_icon = "source/images/icon.png" # Иконка игры
    config.windows_icon = "source/images/icon.png"
    
    config.has_autosave = True # Автосохранение включено
    config.autosave_frequency = 20
    
    #config.quit_action = ShowMenu("my_global_exit") # Кастомный выход # Не работает, сука

    ## Эти управляют шириной и высотой экрана.

    config.screen_width = 800
    config.screen_height = 600

    ## Это управляет заголовком окна, когда Ren'Py
    ## запущен в оконном режиме.

    config.window_title = u"Арендатор"

    # Эти управляют именем и версией игры, которые указываются
    # в журналах отладки.
    config.name = "Арендатор"
    config.version = "1"

    #########################################
    # Темы

    ## Затем, мы захотим вызвать функцию темы. theme.roundrect
    ## это тема, поддерживающая круглые прямоугольники.
    ##
    ## Функция темы берет несколько параметров, которые
    ## настраивают цветовую схему.

    theme.regal(
        ## Theme: CyberNoir
        ## Color scheme: DeepBlue

        ## The color of an idle widget face.
        widget = "#3aaeeb",

        ## The color of a focused widget face.
        widget_hover = "#2892c9",

        ## The color of the text in a widget.
        widget_text = "#094463",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#021a27",

        ## The color of a disabled widget face.
        disabled = "#e3ebf0",

        ## The color of disabled widget text.
        disabled_text = "#5e696e",

        ## The color of informational labels.
        label = "#3aaeeb",

        ## The color of a frame containing widgets.
        frame = "#0c3951",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "source/images/main_menu_blank.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = im.Scale("source/images/house_mainscreen_ingame.png", 800, 600),

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## Эти настройки позволяют вам настроить окно,
    ## содержащее диалоги и текст "от автора", замещая его
    ## изображением.

    ## Фон окна. В Frame, числа символизируют размер
    ## левого/правого и верхнего/нижнего бордюров
    ## соответственно.

    #style.window.background = Frame("source/images/mainmenu_bg.jpeg", 12, 12)

    ## Внешние поля - пространство, окружающее окно, на котором
    ## не рисуется фон.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Внутренние поля - пространство внутри окна, где
    ## рисуется фон.

    style.window.left_padding = 16
    style.window.right_padding = 16
    style.window.top_padding = 16
    style.window.bottom_padding = 16

    ## Это минимальная высота окна, включая поля.

    style.window.yminimum = 240


    #########################################
    ## Это позволит вам изменить расположение главного меню.

    ## Это работает так: мы находим точку-якорь внутри
    ## объекта и точку позиции (pos) на экране.
    ## Затем, мы размещаем объект так, чтобы эти точки совпадали.

    ## Якорь/pos можно задавать как целое или действительное число.
    ## Если целое, оно принимается как кол-во пикселей от
    ## левого верхнего угла. Если действительное, число
    ## принимается как доля размера объекта или экрана.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Это позволяет настроить шрифт текста в Ren'Py.

    ## Файл, содержащий шрифт.

    # style.default.font = "DejaVuSans.ttf"
    
    ## Размер текста по умолчанию.

    style.default.size = 18

    ## Заметьте, что это изменит стиль лишь некоторого
    ## текста. У других кнопок свои стили.


    #########################################
    ## Эти настройки позволят изменить некоторые звуки
    ## Ren'Py.

    ## Установите False если в игре нет звуковых эффектов.

    config.has_sound = True

    ## Установите False если в игре нет музыки.

    config.has_music = True

    ## Установите True если в игре есть озвучка.

    config.has_voice = False

    ## Звуки при нажатии на кнопки и imagemap-ы.

    style.button.activate_sound = "source/sound/clicksound1.mp3"
    style.imagemap.activate_sound = "source/sound/clicksound1.mp3"

    ## Звуки при входе и выходе из игрового меню.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук для проверки громкости.

    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.

    config.main_menu_music = "source/sound/mainmenu_sound.mp3"
    config.mouse = { 'default' : [ ('source/images/my_cursor.png', 0, 0)] } 


    #########################################
    ## Справка.

    ## Это позволит настроить опцию справки в меню Ren'Py.
    ## Это могут быть:
    ## - Метка в сценарии. В этом случае эта метка вызывается
    ##   для показа помощи.
    ## - Имя файла отнсоительно основной директории.
    ##   Он будет открыт в веб-браузере.
    ## None. Помощь будет выключена.
    config.help = "about.html"


    #########################################
    ## Переходы.

    ## Используется при входе в игровое меню.
    config.enter_transition = dissolve

    ## Используется при выходе из игрвого меню.
    config.exit_transition = dissolve

    ## Используется между экранами игрового меню.
    config.intra_transition = dissolve

    ## Используется при входе в игровое меню из главного.
    config.main_game_transition = dissolve

    ## Используется при возвращении в главное меню из игры.
    config.game_main_transition = dissolve

    ## Используется при переходе в главное меню из окна загрузки.
    config.end_splash_transition = dissolve

    ## Используется при переходе в главное меню после окончания игры.
    config.end_game_transition = dissolve

    ## Используется при загрузке игры.
    config.after_load_transition = dissolve

    ## Используется при отображении окна.
    config.window_show_transition = dissolve

    ## Используется при скрытии окна.
    config.window_hide_transition = dissolve

    ## Используется при переходе в режим NVL сразу после режима ADV.
    config.adv_nvl_transition = dissolve

    ## Используется при переходе в режим ADV сразу после режима NVL.
    config.nvl_adv_transition = dissolve

    ## Используется при отображении yesno.
    config.enter_yesno_transition = dissolve

    ## Используется при скрытии yesno.
    config.exit_yesno_transition = dissolve

    ## Используется при входе в реплей.
    config.enter_replay_transition = None

    ## Используется при выходе из реплея.
    config.exit_replay_transition = None

    ## Используется при изменении изображения с помощью "say" с изобразительными атрибутами.
    config.say_attribute_transition = None

    #########################################
    ## Имя директории, где хранятся данные игры.
    ## (это необходимо задать рано, чтобы постоянная информация могла быть
    ## найдена на стадии инициализации.)
python early:
    config.save_directory = "saved_data"

init -1 python hide:
    #########################################
    ## Стандартные значения настроек.

    ## Эти опции используются лишь при первом запуске игры.
    ## Чтобы применить их снова, удалите game/saves/persistent.

    ## Запустить в полноэкранном режиме?

    config.default_fullscreen = False

    ## Скорость текста по умолчанию, в знаках в секунду. 0 - бесконечность.

    config.default_text_cps = 45

    ## Время авто-режима по умолчанию.

    config.default_afm_time = 10

    #########################################
    ## Остальные настройки могут быть ниже.


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "the_tenant-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "the_tenant"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
    
    
    

    