# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Erin")
define a = Character("Aya")

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.75

default kind_points = 0
default lamp_freeze_outcome = False
default lamp_check = False


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    jump bookstore

label ending:
    "The End"
    # This ends the game.

    return
