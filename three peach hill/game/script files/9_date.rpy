label chapter_nine:
    $ chapter_num = 9
    label date:
        scene brown
        stop music fadeout 2.0
        $ make_day()
        show bg bathroom with dissolve
        "You check your hair in the mirror one more time and take a calming breath, then grab your keys and coat and head for the door."

        "After what happened at the Lost Market, Erin took the last two days off to rest. She slept for about 20 hours the first day, which had you worried."

        ## phone buzz sound effect
        "Your phone buzzes. It's a text from Erin."
        
        "\"See you in a bit!\""
    
        "You asked her to meet you at the nearby cafe so you could check on her, and because you've come to a decision."

        "No more wishy-washiness."

        scene brown with dissolve
        play music coffee fadein 0.5
        show bg lydias with dissolve

        play sound "sound/Cup.flac"
        "You set your coffee cup down. The ceramic clinks against the saucer."

        a neutral "\"I've given it a lot of thought, and... I don't want to go to the Lost Market tomorrow.\""

        e shocked "\"What? Then how will you get that spell?\""

        a sad "\"I'm not happy about how close you came to getting eaten by a tricky spirit, and I don't think it's a good idea for us to go back so soon.\""

        e "\"It was one time, and I was by myself! You'll be there this time, right? So what happened last time isn't going to happen again.\""

        a neutral "\"It's too risky. Those spirits were really agitated.\""

        "You hesitantly reach across the table and rest a hand over hers."

        a "\"I wanted to go to get back something precious to me, but...\""

        a "\"The lamp is just a lamp. There's something far more precious sitting right in front of me.\""

        "Erin doesn't seem soothed by this."

        e neutral "\"Right, a human life is more important than a lamp, I get it. But I don't want to owe you something. I broke that lamp, I should take care of it.\""

        a blush "\"I don't think you do get it, actually.\""

        a "(It isn't clicking for her. But this is as good a time as any...)"

        a "(I'll need to be more direct.)"

        menu:
            
            "\"You're what's precious to me, Erin. You.\"":
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

        "Your cheeks are DEFINITELY pink, but you gather all the rizz in your heart."

        a "\"Sounds like we should do something about it, then.\""

        e rizzler "\"Yeah??\""

        "If Erin were a puppy, her tail would be wagging her out of her chair right now."

        a happy "\"Let's start with this.\""

        "With a wave of your left hand, you summon the contract you signed together. It's as simple as plucking the page from the air."

        show signed contract with dissolve

        "You take the contract in one hand, still holding Erin's hand with the other, and when you speak your words ring clear as a bell."
        
        a neutral "\"I release you from the pact.\""

        hide signed contract with dissolve
        play sound "sound/Magic Spell Push.flac" volume 0.5

        "With those simple words, the page crumbles into dust."

        "The contract between you breaks with a faint snap."

        a excited "\"Now you don't owe me anything. The debt is forgiven, both figuratively and literally.\""

        e sad "\"That means a lot to me, and I'm SO happy you confessed, but... does this mean you're giving up on fixing the lamp? It's so important to you.\""

        a happy "\"I'll have more opportunities to fix it in the future. Spirits are long-lived, I have plenty of time.\""

        a "\"So... even if you're only here for a little while, I want to spend time with you.\""

        e shocked "\"That's morbid, I'm not {i}dying{/i} anytime soon!\""

        "You blink."

        a blush "\"I, uh, guess it did sound that way, huh? I just meant, you're probably going back to school soon...\""

        e blush "\"Oooooh! Well, I haven't decided what to do yet. But for now... whaddya say, wanna go out?\""

        a blush "\"Haha, yes! I'd like that. A lot.\""

        e happy "\"Okay!! Take me on a date! I mean, I'd like to go on a date. With you. If you want!\""

        "You gently trace her cheek with a light touch and give her a reassuring smile."

        a excited "\"So confident. But you seem nervous, too. You were so gung-ho about this before—were you all bark and no bite?\""

        e shocked "\"I'm not nervous! I just have, uh, a lot of nervous energy!\""

        "She ducks in to give you a quick peck on the cheek. Her lips are soft against your skin."

        e rizzler "\"I'm not too nervous for that, see?\""

        "You ache for more than just that fleeting kiss. You've BEEN wanting this."

        "With a confidence you didn't know you had, you reach up and pull her into you."

        "The kiss is everything you wanted. Hot and sweet and tender and exciting."

        "You've still got a lamp to fix and a bookstore to save, but now you also have..."

        "A girlfriend."

        window hide

        scene brown with irisin
        stop music fadeout 3.0
        pause 1.0

        show tbc with dissolve
        pause 3.5

        hide tbc with Dissolve(3)
        pause 2.0


        jump credits