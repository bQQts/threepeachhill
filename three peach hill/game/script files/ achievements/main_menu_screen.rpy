screen achievements:
    tag menu

    default device = "keyboard"

    use game_menu(scroll="viewport"):

        style_prefix "achievements"

        vbox:
            spacing 30

            hbox:
                xalign 0.5
                yalign 0.5
                ysize 1100
        vbox:
            xcenter 0.5 ycenter 0.5
            if achievement.has("hello_world"):
                text "Hello world!" color "#000"
            else:
                text "Hello world - ???" color "#fff"