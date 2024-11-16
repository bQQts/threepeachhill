# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Erin", image="erin neutral")
define a = Character("Aya", image="aya neutral")
define lyd = Character("Lydia")
define joy = Character("Joy")


default kind_points = 0
default lamp_freeze_outcome = False
default lamp_check = False
default cobblerfirst = False
default cornerstorefirst = False
default picked_clumsy = False
default milk_carton = False

image aya neutral = "Aya Neutral.png"
image aya excited = "Aya Excited.png"
image aya gloom = "Aya Gloom.png"
image aya happy = "Aya Happy.png"
image aya neutral = "Aya Neutral.png"
image aya sad = "Aya Sad.png"
image aya shocked = "Aya Shocked.png"
image aya tsun = "Aya TsunTsun.png"
image erin blush = "Erin Blush.png"
image erin excited = "Erin Excited.png"
image erin gloom = "Erin Gloom.png"
image erin happy = "Erin Happy.png"
image erin neutral = "Erin Neutral.png"
image erin rizz = "Erin Rizzler.png"
image erin sad = "Erin Sad.png"
image erin shocked = "Erin Shocked.png"
image bg bathroom = "bathroom.png"
image bg bedroom = "bedroom.png"
image bg bookstore = "bookstore.png"
image bg gate = "gate.png"
image bg kitchen = "kitchen.png"
image bg orchard = "orchard.png"
image bg rain = "rain.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg bookstore
    show bg bookstore:
        subpixel True yanchor 1.13 zoom 1.42
    show aya neutral at left:
        subpixel True
        zoom 0.3
    with Pause(0.12)

    # These display lines of dialogue.

    jump bookstore

label ending:
    "The End"
    # This ends the game.

    return
