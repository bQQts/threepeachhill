# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aya", image="aya", who_color= "#faf6f5", voice_tag="a")
define e = Character("Erin", image="erin", who_color= "#faf6f5", voice_tag="e")

define lyd = Character("Lydia", voice_tag="lyd")
define joy = Character("Joy", voice_tag="joy")
define jeff = Character("Jeff", voice_tag="jeff")
define timothy = Character("Timothy", voice_tag="timothy")
define Oni = Character("Oni", voice_tag="Oni")

init python:
    # renpy.music.register_channel("narrator", "narrator")
    # renpy.music.register_channel("Aya", "aya")
    # renpy.music.register_channel("Erin", "erin")
    # renpy.music.register_channel("Lydia", "lydia")
    # renpy.music.register_channel("Joy", "joy")
    # renpy.music.register_channel("Jeff", "jeff")
    # renpy.music.register_channel("Timothy", "timothy")
    SetCharacterVolume("a", volume=None)
    SetCharacterVolume("e", volume=None)
    SetCharacterVolume("lyd", volume=None)
    SetCharacterVolume("joy", volume=None)
    SetCharacterVolume("jeff", volume=None)
    SetCharacterVolume("timothy", volume=None)
    SetCharacterVolume("Oni", volume=None)

# default preferences.volume.aya = 1.0
# default preferences.volume.erin = 1.0
# default preferences.volume.lydia = 1.0
# default preferences.volume.joy = 1.0
# default preferences.volume.jeff = 1.0
# default preferences.volume.timothy = 1.0
# default preferences.volume.oni = 1.0

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
