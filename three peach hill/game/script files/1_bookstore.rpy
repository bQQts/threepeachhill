label chapter_one:
    $ chapter_num = 1
    label bookstore:
        scene brown with dissolve
        pause 1.5
        show date_animated_ch1 with dissolve # July 10
        pause 2.5
        stop music fadeout 3.0
        hide date_animated_ch1 with Dissolve(2)
        scene brown with dissolve
        pause 1.0
        show bg bookstore with dissolve
        play music bookstore_vibing fadein 1.0
        pause 1.0
        play sound "sound/Cicada Ambience.flac" volume 0.3 fadein 2.0 loop
        "It's been a slow summer. Slower than usual. The buzzing of cicadas and unyielding humidity drown our little town in syrupy hot summer."

        "The familiar sound seems to say, \"You have all the time in the world.\" A clock hanging by the cluttered storefront counter slowly {i}tic tic tics{/i} in agreement."

        stop sound fadeout 3.0
        "You adjust the angle of your desk fan to get a better breeze. It helps, but sweat still sticks your crisp white dress shirt to your skin."

        "Business has been far too slow."

        "You need to do something about it this summer, but there's no rush."

        "It's a family business. It's been here for ages and will surely carry on well beyond your tenure."
        
        play sound "sound/JingleDoor.flac"

        "Your soft foxen ear twitches at the sound of bells jingling as the shop door swings open. You make a couple more adjustments as you call in the direction of the door."


        a neutral "\"Welcome in, feel free to browse.\""


        "There's an excited giggle. You look up and your breath catches."


        show erin happy at center, erin_size, with dissolve

        "An adorable college girl you've never seen before. Her dark hair is pulled up into a bun and tied with a blue scarf. Heart-meltingly warm brown eyes sparkle warmly at you. Possibilities hang heavy in the air."

        show erin shocked

        "Then she's falling for you."

        "Literally."
        
        "Her lips part in an \"oh\" of surprise as she trips over the box of peaches that your neighbor so kindly left just inside the door."

        "You must have been in the back, because you don't remember them stopping by."

        hide erin with dissolve

        "The fall is epic."
        
        "Her tote bag soars, colored gel pens tumbling out to rain down in a myriad rainbow that bounces on the hardwood floor."
        
        "Loose pages slide from the bag and take flight, scattering across the hardwood floor."

        "The young woman's body slams into the book rack between you and she pivots, angling the shelf away from the front counter."
        
        "Away from {i}you{/i}."

        "She tumbles to the ground in a heap as the rack crashes into a nearby bookshelf. It knocks off the blue heirloom lamp that until this moment had minded its business for as long as you can remember."

        show brokenlamp with dissolve
        "(Oh no...)"

        "A glance tells you the girl survived the fall. The lamp, on the other hand, did not."

        "The mosaic glass panels shattered, reducing what once was a work of art into a pile of shards."
        hide brokenlamp with dissolve
        menu:
            "You should act fast."

            "Check on the girl":
                    $ kind_points += 1
                    show plusone:
                        subpixel True
                        xanchor -1595
                        #xanchor -599 
                        yanchor -643 alpha 0.0 
                        linear 0.18 yanchor -535 alpha 1.0 
                        linear 0.25 yanchor -439 alpha 1.0 
                        linear 0.15 yanchor -351 alpha 0.0 
                    with Pause(0.68)
                    show plusone:
                        yanchor -251 alpha 0.0
                    jump bookstore_Girl

            "Check the lamp":
                jump bookstore_Lamp




        label bookstore_Girl:

            "You rush over, taking hold of her arm and helping her upright."

            a shocked "\"Are you okay?!\""

            "She groans as she sits up in a pile of books, clutching at her left shin. She lightly smacks a palm against her forehead when she sees the destruction her fumble wrought upon the store."

            "The fallen shelves. The shattered lamp. The alarmed and bewildered expression on your face."

            e gloom "\"I'm so sorry!!! I didn't see the box, I hope nothing...\""

            show brokenlamp with dissolve
            
            "Her gaze slides to the broken lamp and she gulps."

            e sad "\"...well, I hope nothing else got too damaged. I'm really sorry. Let me help clean up!\""

            a neutral "\"Don't worry about that right now, are you injured?\""

            "She shakes her head and lets you help her up. Up close, she's even cuter than you realized. Your heart flutters."

            e sad "\"No, but... what about the lamp?\""

            jump deal


        label bookstore_Lamp:
            $ lamp_check = True

            show brokenlamp with dissolve

            "Surveying the shattered lamp yields nothing you didn't already suspect. The glass lampshade was a mosaic of shades of blue stained glass pieces welded together at the seams."
            
            "Four panels had joined at their long edges to create a lampshade reminiscent of a boxy, blue, crystalline moth."

            "Now, the intricate panels are shattered, the floor a dazzling array of blue edges. The electrical fixture, too, is bent at an odd angle."

            show erin gloom at right:
                zoom 0.7 yalign 0.15
            
            "The lamp murderer groans as she sits up in a pile of books, clutching at her left shin. She puts a hand to her brow and makes another small noise of dismay as she sees the destruction her fumble wrought upon the store."
                
            "The fallen shelves. The shattered lamp. Your horrified expression."

            "You almost expect her to run away. She's definitely a college student, but she looks so young. And she's human! You want to say something, to tell her off or ask if she's okay, but..."
            
            "You can't find the words as you watch her stand up, dust herself off, and limp over to inspect the shattered lamp."

            hide erin with dissolve

            e shocked "\"Oh shit, I'm so sorry about that. I didn't see the box... Here, I'll clean this up.\""

            "She reaches down to pick up a large piece of glass."

            # CHOICE
            menu:
                "Grab her hand":
                    $ kind_points += 1
                    show plusone:
                        subpixel True
                        xanchor -1595
                        #xanchor -599 
                        yanchor -643 alpha 0.0 
                        linear 0.18 yanchor -535 alpha 1.0 
                        linear 0.25 yanchor -439 alpha 1.0 
                        linear 0.15 yanchor -351 alpha 0.0 
                    with Pause(0.68)
                    show plusone:
                        yanchor -251 alpha 0.0
                    jump lamp_grab

                "Freeze in surprise":
                    jump lamp_freeze



            label lamp_grab:

                "Your hand darts out to grasp the girl's wrist before she can pick anything up."

                a shocked "\"Don't! Don't, you could hurt yourself.\""

                "She freezes, then turns to look you in the eye."

                "Her face is so close. Her eyes are a warm brown that reminds me of hot chocolate, or perhaps the old walnut table upstairs. It's a familiar, comfortable shade."

                "You feel heat creeping into your cheeks. You're blushing!"

                jump deal


            label lamp_freeze:

                $ lamp_freeze_outcome = True

                "It takes my brain a moment to catch up to what's happening, and by the time I realize what she's doing, it's too late."

                "The girl quickly piles the broken shards and hisses in pain when one odd-angled piece slices a shallow line across her finger."

                a neutral "\"Wait, stop,\""

                "She doesn't stop."

                a tsuntsun "\"Stop!\""

                "Finally, she stops fiddling with the broken shards. She clutches her bleeding finger and looks up at me with watery eyes."

                jump deal