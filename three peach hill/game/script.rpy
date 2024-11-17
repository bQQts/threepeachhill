# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aya", image="aya")
define e = Character("Erin", image="erin")

define lyd = Character("Lydia")
define joy = Character("Joy")


default kind_points = 0
default lamp_freeze_outcome = False
default lamp_check = False
default cobblerfirst = False
default cornerstorefirst = False
default picked_clumsy = False
default milk_carton = False

image define aya excited = "side aya excited.png"
image define aya gloom = "side aya gloom.png"
image define aya happy = "side aya happy.png"
image aya = "aya neutral.png"
image define aya neutral = "side aya neutral.png"
image define aya sad = "side aya sad.png"
image define aya shocked = "side aya shocked.png"
image aya tsun = "aya tsuntsun.png"
image erin blush = "erin blush.png"
image erin excited = "erin excited.png"
image erin gloom = "erin gloom.png"
image erin happy = "erin happy.png"
image erin neutral = "erin neutral.png"
image erin rizz = "erin rizzler.png"
image erin sad = "erin sad.png"
image erin shocked = "erin shocked.png"
image bg bathroom = "bathroom.png"
image bg bedroom = "bedroom.png"
image bg bookstore = "bookstore.png"
image bg gate = "gate.png"
image bg kitchen = "kitchen.png"
image bg orchard = "orchard.png"
image bg rain = "rain.png"
image black = "#000"

# The game starts here.

label start:

label startbutitsalabel:

    scene bg

    show bg bookstore:
        zoom 1.75 yoffset -250


    jump bookstore

label ending:
    "The End"
    # This ends the game.

    return
