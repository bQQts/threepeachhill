# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aya", image="aya", who_color= "#faf6f5")
define e = Character("Erin", image="erin", who_color= "#faf6f5")

define lyd = Character("Lydia")
define joy = Character("Joy")
define jeff = Character("Jeff", image="jeff")
define timothy = Character("Timothy", image="timothy")


default kind_points = 0
default lamp_freeze_outcome = False
default lamp_check = False
default cobblerfirst = False
default cornerstorefirst = False
default picked_clumsy = False
default milk_carton = False




image black = "#000"
image white = "#fff"
image brown = "#1F1B1B"



label start:

label startbutitsalabel:


    #play music ### fadein 1.5  ## uncomment this line and comment the next one to test out songs at beginning of game lol

    jump bookstore

label ending:
    scene black with dissolve
    stop music fadeout 10.0

    "To Be Continued..."

    screen hide

    # This ends the game.

    return
