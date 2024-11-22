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

image aya = "side aya neutral.png"
#image define aya excited = "side aya excited.png"
#image define aya gloom = "side aya gloom.png"
#image define aya happy = "side aya happy.png"
#image define aya neutral = "side aya neutral.png"
#image define aya sad = "side aya sad.png"
#image define aya shocked = "side aya shocked.png"
#image define aya tsun = "side aya tsuntsun.png"

image erin = "erin neutral.png"
#image erin neutral = "erin neutral.png"
#image erin blush = "erin blush.png"
#image erin excited = "erin excited.png"
#image erin gloom = "erin gloom.png"
#image erin happy = "erin happy.png"
#image erin rizz = "erin rizzler.png"
#image erin sad = "erin sad.png"
#image erin shocked = "erin shocked.png"

image bg bathroom = "bathroom.png"
image bg bedroom = "bedroom.png"
image bg bookstore = "bookstore.png"
image bg cornerstore = "cornerstore.png"
image bg gate = "gate.png"
image bg kitchen = "kitchen.png"
image bg lydias = "lydias.png"
image bg market = "market.png"
image bg nightmarket = "nightmarket.png"
image bg orchard = "orchard.png"
image bg rain = "rain.png"

image bg bathroom night = "bathroom night.png"
image bg bedroom night = "bedroom night.png"
image bg bookstore night = "bookstore night.png"
image bg cornerstore night = "cornerstore night.png"
image bg gate night = "gate night.png"
image bg kitchen night = "kitchen night.png"
image bg lydias night = "lydias night.png"
image bg market night = "market night.png"
image bg nightmarket night = "nightmarket night.png"
image bg orchard night = "orchard night.png"
image bg rain night = "rain night.png"

image bg nightmarket red = "nightmarket red.png"

image cg piggyback = "cg_piggyback.png"


image black = "#000"
image white = "#fff"



label start:

label startbutitsalabel:
    stop music fadeout 3.0
    with dissolve

    scene black
    pause 1.0
    play music "music/bookstore lofi.flac" fadein 2.0
    show bg bookstore with dissolve



    jump bookstore

label ending:
    scene black with dissolve
    music fadeout 5.0

    "To Be Continued..."

    screen hide with dissolve

    jump credits
    # This ends the game.

    return
