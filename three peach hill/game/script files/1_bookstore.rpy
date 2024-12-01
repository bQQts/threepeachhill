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

    "It's been a slow summer. Slower than usual. The buzzing of cicadas and unyielding humidity drown our little town in syrupy hot summer."

    "The familiar sound seems to say, \"You have all the time in the world.\" A clock hanging by the cluttered storefront counter slowly {i}tic tic tics{/i} in agreement."

    "I adjust the angle of my desk fan to get a better breeze. It helps, but sweat still sticks my crisp white dress shirt to my skin."

    "Business has been far too slow."

    "I need to do something about it this summer, but I'm not in a rush."

    "It's a family business. It's been here for ages and will surely carry on well beyond my tenure."
    
    play sound "sound/JingleDoor.flac"

    "My ear twitches at the sound of bells jingling, the shop door swinging open slowly. I fidget with the fan some more and say,"


    a neutral "\"Welcome in, feel free to browse.\""


    "I look up and my breath catches."


    show erin happy at center, erin_size, with dissolve

    "She's adorable. Beautiful, really. Her warm brown eyes sparkle, and her dark hair is pulled up into a bun tied with a blue scarf. I have just a moment to take it all in before time freezes."

    show erin shocked

    "She locks eyes with me. Her breath catches, and she's falling for me."

    "Literally."
    
    "Her lips part in an \"oh\" of surprise as she trips over the box of peaches that my neighbor so kindly left by the door for me."

    "(Damnit! I knew I should have moved it while it was on my mind.)"

    hide erin with dissolve

    "The fall is epic."

    "The moment feels suspended in time."
    
    "Her tote bag soars, colored gel pens tumbling out to rain down in a myriad rainbow that bounces on the hardwood floor."
    
    "Loose pages slide from the bag, valiantly taking flight, and each sheaf makes its lazy way to earth."

    "Her body slams into the book rack near the entrance and she pivots, angling the shelf away from the front counter."
    
    "Away from {i}me{/i}."

    "She tumbles to the ground in a heap as the rack slams into a nearby bookshelf, knocking off the blue heirloom lamp that, moments before, had minded its own business for as long as I can remember."

    "(Oh no...)"

    "A glance tells me the girl survived the fall. The lamp, on the other hand, did not."

    "The mosaic glass panels shattered back into un-mosaicked shards. My heart lurches."

menu:
    "Quick! What should I do?!"

    "Check on the girl":
            $ kind_points += 1
            jump bookstore_Girl

    "Check the lamp":
        jump bookstore_Lamp




label bookstore_Girl:

    "I rush over to her, taking hold of her arm and helping her upright."

    a shocked "\"Are you okay?!\""

    "She groans as she sits up in a pile of books, clutching at her left shin. She puts a hand to her brow and makes another small noise of dismay as she sees the destruction her fumble wrought upon the store."

    "The fallen shelves. The shattered lamp. My concern."

    e gloom "\"I'm so sorry!!! I didn't see the box, I hope nothing...\""

    "Her gaze slides to the broken lamp and she gulps."

    e sad "\"...well, I hope nothing else got too damaged. I'm really sorry. Let me help clean up!\""

    a neutral "\"Don't worry about that right now, are you injured?\""

    "She shakes her head and lets me help her up. Up close, she's even cuter than I realized. My heart flutters."

    e sad "\"No, but... what about the lamp?\""

    jump deal


label bookstore_Lamp:
    $ lamp_check = True

    "Surveying the shattered lamp yields nothing I didn't already suspect. The glass lampshade was a mosaic of shades of blue stained glass pieces welded together at the seams."
    
    "Four panels had joined at their long edges to create a lampshade reminiscent of a boxy, blue, crystalline moth."

    "Now, the intricate panels are shattered, the floor a dazzling array of blue edges. The electrical fixture, too, is bent at an odd angle."

    show erin gloom at right:
        zoom 0.7 yalign 0.15
    
    "The lamp murderer groans as she sits up in a pile of books, clutching at her left shin. She puts a hand to her brow and makes another small noise of dismay as she sees the destruction her fumble wrought upon the store."
        
    "The fallen shelves. The shattered lamp. My concern."

    "I almost expect her to run away. She's young, maybe a college student? And she's human! I open my mouth to say something, to tell her off or ask if she's okay, but..."
    
    "I can't find the words as I watch her stand up, dust herself off, and limp over to inspect the shattered lamp."

    hide erin with dissolve

    e shocked "\"Oh shit, I'm so sorry about that. I didn't see the box... Here, I'll clean this up.\""

    "She reaches down to pick up a large piece of glass."

    # CHOICE
    menu:
        "Grab her hand":
            $ kind_points += 1
            jump lamp_grab

        "Freeze in surprise":
            jump lamp_freeze



    label lamp_grab:

        "My hand darts out and grabs hold of the girl's wrist."

        a shocked "\"Don't! Don't, you could hurt yourself.\""

        "She freezes, then turns to look me in the eye."

        "Her face is so close. Her eyes are a warm brown that reminds me of hot chocolate, or perhaps the old walnut table upstairs. It's a familiar, comfortable shade."

        jump deal


    label lamp_freeze:

        $ lamp_freeze_outcome = True

        "It takes my brain a moment to catch up to what's happening, and by the time I realize what she's doing, it's too late."

        "The girl quickly piles the broken shards and hisses in pain when one odd-angled piece slices a shallow line across her finger."

        a neutral "\"Wait, stop,\""

        "She doesn't stop."

        a tsuntsun "\"Stop!\""

        "Finally, she stops fiddling with the broken shards. She clutches her bleeding finger and looks up at me."

        jump deal