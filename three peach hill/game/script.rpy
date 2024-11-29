# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aya", image="aya", who_color= "#faf6f5")
define e = Character("Erin", image="erin", who_color= "#faf6f5")

define lyd = Character("Lydia")
define joy = Character("Joy")


default kind_points = 0
default lamp_freeze_outcome = False
default lamp_check = False
default cobblerfirst = False
default cornerstorefirst = False
default picked_clumsy = False
default milk_carton = False




image black = "#000"
image white = "#fff"



label start:

label startbutitsalabel:
    stop music fadeout 3.0
    with dissolve

    scene black
    pause 1.0
    #play music "music/SpiritChase.flac" fadein 1.5  ## uncomment this line and comment the next one to test out songs at beginning of game lol
    play music "music/Bookstore Lofi.flac" fadein 2.0
    show bg bookstore with dissolve



    jump bookstore

label ending:
    scene black with dissolve
    stop music fadeout 10.0

    "To Be Continued..."

    screen hide

    jump credits
    # This ends the game.

    return
