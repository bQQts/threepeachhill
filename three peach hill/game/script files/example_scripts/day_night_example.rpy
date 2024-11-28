label example_day_night:
    show bg bookstore

    show side erin happy

    e "\"I got here at noon like I promised!\""
    
    a happy "\"Neat! Watch this:\""

    menu:
        "Abra Cadabra..."

        "Switch to Night!":
            $ make_night()


    show bg bookstore night with dissolve

    show side erin shocked
    e "\"Woah, it suddenly became night!\""

    a "\"Pretty cool, right? Let me change it back.\""

    menu:
        "Arbadac Arba..."

        "Switch to Day":
            $ make_day()


    show bg bookstore with dissolve

    show side erin happy
    e "\"Yay!\""

    a "\"Woo hoo\""