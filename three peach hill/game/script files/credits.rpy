label credits:
    play music credits noloop

    $ credits_speed = 80
    scene brown with dissolve
    show credits at Move((0.5, 1.0), (0.5, -5.0), credits_speed, xanchor=0.5, yanchor=0) with Pause(credits_speed+40) 
    stop music fadeout 5.0

    #"\"Journey To Ascend\" Kevin MacLeod
    #(incompetech.com)"
    #"Licensed under Creative Commons: By Attribution 4.0 License"
    #"http://creativecommons.org/licenses/by/4.0/"


#    "Jeff and Timothy Silhouettes"
#    "Character Silhouettes: Bureaucrats by RAIT Visual Works"
#    "https://witching-metal.itch.io/character-silhouettes-bureaucrats"