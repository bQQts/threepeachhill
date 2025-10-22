label chapter_six:
    $ chapter_num = 6
    label the_call:

        scene bg kitchen
        "You're filling a glass of water when you hear Erin's muffled voice. She must be out on the balcony, and by the sound of it she's not having a very fun conversation."
        
        stop music fadeout 4.0
        "When she comes in she seems deflated."

        a neutral "\"Oh, there you are! Were you on the phone?\""

        e neutral "\"Yeah. It was my parents. They want me to come back to the city.\""

        "Your stomach drops. This can't be happening."

        a "\"I see. So... are you going?\""

        e gloom "\"Sigh. I haven't decided yet, to be honest. It's nice out here, and...\""

        "She looks sidelong at you through lowered lashes."
        play music romance fadein 1.0
        e happy "\"I've found somewhere I like being. This feels like a place I could belong.\""

        "Oh."

        a "\"Don't you want to finish college?\""

        e neutral "\"There are other ways. I could postpone it or do it online. Anyway, the point is that I'm not really ready to go back to the city. I don't want to go.\""

        a "\"What about your parents?\""

        e "\"What about them? I appreciate that they want to look out for me, but I'm doing just fine. I'm not doing anything wrong by trying to be happy.\""

        a happy "\"That's kind of a great outlook.\""

        e happy "\"Right?\""

        "You can't help yourself. You reach out and rub her shoulder."

        a "\"I'm glad you found somewhere you want to be. Belonging somewhere is something everyone needs, humans and spirits alike.\""

        "She smiles shyly at you."

        "That's when YOU get a call. One you're totally unprepared for."
        window hide
        scene brown with irisin
        pause 2.0
        jump the_plan