label chapter_nine:
    $ chapter_num = 9
    label date:
        scene black
        stop music fadeout 2.0
        $ make_day()
        show bg bathroom with dissolve
        "I check my hair in the mirror one more time and take a calming breath, then grab my keys and coat and head for the door."

        "After what happened at the Lost Market, Erin took the last two days off to rest. She slept for about 20 hours the first day, which had me worried."

        "My phone buzzes. It's a text from Erin."
        
        "\"See you in a bit!\""
    
        "I asked her to meet me at the nearby cafe so I could check on her, and because I've come to a decision."

        scene black with dissolve
        play music coffee fadein 0.5
        show bg lydias with dissolve

        a neutral "\"I've given it a lot of thought, and... I don't want to go to the Lost Market tomorrow.\""

        e shocked "\"What? Then how will you get that spell?\""

        a sad "\"I'm not happy about how close you came to getting eaten by a tricky spirit, and I don't think it's a good idea for us to go back so soon.\""

        e "\"It was one time, and I was by myself! You'll be there this time, right? So what happened last time isn't going to happen again.\""

        a neutral "\"It's too risky.\""

        "I hesitantly reach across the table and rest a hand over hers."

        a "\"I wanted to go to get back something precious to me, but...\""

        a "\"The lamp is just a lamp. There's something far more precious sitting right in front of me.\""

        "Erin doesn't seem soothed by this."

        e neutral "\"Right, a human life is more important than a lamp, I get it. But I don't want to owe you something. I broke that lamp, I should take care of it.\""

        a blush "\"I don't think you do get it, actually.\""

        "(It isn't clicking for her. But this is as good a time as any...)"

        "(I'll need to be more direct.)"

        menu:
            
            "\"You are precious to me, Erin.\"":
                jump confession

            "\"I like you.\"":
                jump confession

    

    label confession:
        "Erin's jaw drops. Then she punches the air with her free hand."

        e excited "\"YES! I KNEW IT!!!\""

        "Several other patrons turn their heads to see what her outburst is about."

        e "\"You like me!!!\""

        a blush "\"Yes, I like you.\""

        e "\"And I like you too!\""

        "My cheeks are DEFINITELY pink, but I try to play it cool."

        a "\"Sounds like we should do something about it, then.\""

        e rizzler "\"Yeah??\""

        "If Erin were a puppy, her tail would be wagging her out of her chair right now."

        a happy "\"Let's start with this.\""

        "With a wave of my left hand, I summon the contract we signed. It's as simple as plucking the page from the air."

        "I take the contract in one hand, still holding Erin's hand with the other, and when I speak my words ring clear as a bell."
        
        a neutral "\"I release you from the pact.\""

        "With those simple words, the page crumbles into dust."

        "I can feel the faint snap of the contractual bond between us breaking."

        a excited "\"Now you don't owe me anything. The debt is forgiven, both figuratively and literally.\""

        e sad "\"That means a lot to me, but... does this mean you're giving up on fixing it?\""

        a happy "\"I'll have more opportunities to fix it in the future. Spirits are long-lived, I have plenty of time.\""

        a "\"So... even if you're only here for a little while, I want to spend time with you.\""

        e shocked "\"That's morbid, I'm not {i}dying{/i} anytime soon!\""

        "I blink."

        a blush "\"I, uh, guess it did sound that way, huh? I just meant, you're probably going back to school soon...\""

        e blush "\"Oooooh! Well, I haven't decided what to do yet. But for now... whaddya say, wanna go out?\""

        a "\"Pfft. Yes, I'd like that.\""

        e happy "\"Okay!! Take me on a date! I mean, I'd like to go on a date. With you. If you want!\""

        "I gently trace her cheek with my fingertips and give her a reassuring smile."

        a excited "\"So confident. But you seem nervous, too. You were so gung-ho about this before—were you all bark and no bite?\""

        e shocked "\"I'm not nervous! I just have, uh, a lot of nervous energy!\""

        "She ducks in to give me a quick peck on the cheek. Her lips are soft against my skin."

        e rizzler "\"But I'm not too nervous for that!\""

        "We leave the cafe hand in hand."

        window hide

        scene black with irisin
        stop music fadeout 3.0
        pause 1.0

        show tbc with dissolve
        pause 3.5

        hide tbc with Dissolve(3)
        pause 2.0


        jump credits