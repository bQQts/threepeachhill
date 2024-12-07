
init -100 python:

    import logging

    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
        filename=f"{renpy.config.gamedir}/my_log.txt",  # Log output file
        filemode='w'  # Overwrite the log file each time
    )

    is_night = True

    from enum import Enum

    class FilePageType(Enum):
        QUICKSAVE = 1
        AUTO = 2
        NORMAL = 3

    page_type = FilePageType.NORMAL
    page_num = 1

    class TrackedFilePage(FilePage):  # page, new_page_type = FilePageType.NORMAL):
        def __init__(self, page_num, page_type = FilePageType.NORMAL):
            self.page_num = page_num
            self.page_type = page_type

            file_page_input = page_num
            if page_type == FilePageType.QUICKSAVE:
                file_page_input = "quick"
            elif page_type == FilePageType.AUTO:
                file_page_input = "auto"

            super().__init__(file_page_input)

        def __call__(self):
            global page_type, page_num
            page_type = self.page_type
            page_num = self.page_num
            super().__call__()

    class TrackedFilePagePrevious(FilePagePrevious):
        def __call__(self):
            global page_type, page_num

            if page_type == FilePageType.AUTO:
                return
            elif page_type == FilePageType.QUICKSAVE:
                page_type = FilePageType.AUTO
            elif page_num == 1:
                page_type = FilePageType.QUICKSAVE
                page_num = 0
            else:
                page_num = page_num - 1

            super().__call__()

    class TrackedFilePageNext(FilePageNext):
        def __call__(self):
            global page_type, page_num

            if page_num == 9:
                return
            elif page_type == FilePageType.QUICKSAVE:
                page_type = FilePageType.NORMAL
                page_num = 1
            elif page_type == FilePageType.AUTO:
                page_type = FilePageType.QUICKSAVE
            else:
                page_num = page_num + 1

            super().__call__()

    class OptionsPageType(Enum):
        SLIDERS = 1
        BUTTONS = 2

    options_page_type = OptionsPageType.SLIDERS

    class OpenOptionsPageSliders(Action, DictEquality):
        def __call__(self):
            global options_page_type
            options_page_type = OptionsPageType.SLIDERS
            renpy.restart_interaction()

    class OpenOptionsPageButtons(Action, DictEquality):
        def __call__(self):
            global options_page_type
            options_page_type = OptionsPageType.BUTTONS
            renpy.restart_interaction()


    class SelectionMenuType(Enum):
        QUIT = 1
        CONFIRM = 2

    selection_menu_type = SelectionMenuType.QUIT

    class SelectionMenuSelection(Enum):
        QUIT = 1
        MAIN_MENU = 2

    selection_menu_selection = SelectionMenuSelection.QUIT

    class OnSelectionMenuQuitConfirm(Action, DictEquality):
        def __call__(self):
            global selection_menu_selection, selection_menu_type
            selection_menu_selection = SelectionMenuSelection.QUIT
            selection_menu_type = SelectionMenuType.CONFIRM
            renpy.restart_interaction()
            
    class OnSelectionMenuTitleConfirm(Action, DictEquality):
        def __call__(self):
            global selection_menu_selection, selection_menu_type
            selection_menu_selection = SelectionMenuSelection.MAIN_MENU
            selection_menu_type = SelectionMenuType.CONFIRM
            renpy.restart_interaction()

    class ResetSelectionMenu(Action, DictEquality):
        def __call__(self):
            global selection_menu_type
            selection_menu_type = SelectionMenuType.QUIT
            renpy.hide_screen("selection_menu")
            renpy.restart_interaction()
    
    class ResetAndReturnToMain(Action, DictEquality):
        def __call__(self):
            renpy.full_restart()
