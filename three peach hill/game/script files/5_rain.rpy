label chapter_five:    # 5. The Rain - Caught in the rain… and there was only one bed? Perchance?
    $ chapter_num = 5
    label the_rain:

        scene brown
        show bg orchard with dissolve

        "YOu finish picking the peaches by yourself. By the time you're done, the remaining daylight is nearly smothered by thick clouds."
        
        "You hadn't noticed how dense they had gotten, but a brief glance is enough to confirm that they look heavy and full, as if ready to spill at any moment."

        "You're rolling your small cart quickly through the orchard when you feel the first droplets splash your brow, your hair, your hand. It's a long way back to your bike, and then you'll still have to cycle home from there. You don't even have a jacket."

        a gloom "\"This is going to suck.\""

        play sound "sound/Rain Moderate.flac" fadein 1.5 volume 0.6 loop
        "The dirt path quickly turns to mud that sucks at your feet with every step. But still, you keep on, now dragging a mud-caked cart of peaches as the early evening sets in."


        scene bg rain with dissolve
        pause 1.5

        "You slip in a particularly muddy patch and fall. Winded, you sit in the mud and contemplate your life."
        
        "Your ankle is definitely sprained. You have no idea how you're going to get these peaches back. You're drenched, and you were very recently uncomfortably avoidant toward a girl you really quite like... for really no good reason."

        "You close your eyes and tilt back your head, letting fat raindrops splash across your face. You take a few deep breaths. Nothing to it but to press on."

        "The rain suddenly stops drip-dropping on your face, but you can still hear it splashing in small puddles around you. You open your eyes."

        show erin shocked at center, erin_size

        "It's Erin. She's holding an umbrella over you, looking breathless and disheveled."

        hide erin with dissolve

        e shocked "\"I ran to get an umbrella as soon as I saw how bad the sky was getting. Looks like I didn't make it to you in time though, sorry, Aya. Why are you sitting in the mud? You're soaked through!\""
        

        a sad "\"Erin...\""

        e neutral "The shorter woman hands you the umbrella and helps you to your feet."

        e neutral "\"Can you walk?\""

        a "\"Yes,\""

        "You put weight onto your injured foot and wince."

        a  gloom "\"Well, no. My ankle...\""

        "Erin turns around and crouches, gesturing for you to climb up on her back."

        e happy "\"Get on, I'll carry you.\""

        a sad "\"But I'm taller than you! I'll crush you!\""

        e excited "\"I'm like an ant, I can carry you no problem!\""

        a gloom "\"Erin, I'll just lean on you and we'll go slow.\""

        e "\"Really, I insist! I'm wearing work boots, I won't slip in the mud. Let me carry you.\""

        a sad "\"What about the peaches?\""

        e happy "\"There will be more peaches. I'm more worried about you right now. Now, climb on.\""

        "You climb on, still holding the umbrella in one hand. She hikes you up, grasping below your thighs and leaning forward to balance you. Strands of your wet hair stick to her neck. You try not to think about how much you'd like to press your lips right there..."

        window hide dissolve
        stop sound fadeout 3.0
        pause 1.0
        scene brown
        show cg piggyback with Dissolve(3)

        pause 120.0

        window show dissolve
        "It takes a while, but you do make it down the big hill. Erin is stronger than she looks, and though she's breathing hard by the time you get back to the entrance of the orchard she hasn't once lost her grip or stumbled."


        e neutral "\"Just hang on tight, I'll get you home.\""

        "You let the umbrella rest over your backs, which you think might make you look like an overly large beetle, and let the sway of her steps and the sound of her breathing lull you into a half-slumber."
        
        window hide
        $ make_night()
        scene brown with Dissolve(3)
        stop music fadeout 3.0
        stop sound fadeout 3.0
        pause 3.0
        show bg gate night with dissolve
        window show

        e "\"What's your door code? ...Aya?\""

        "She's hunched over at the side door of the bookshop that leads up to your house. You blink, rubbing your sleepy eyes with the back of a damp hand."

        e neutral "\"Hey, Aya? You okay?\""

        "There's concern in her voice and you try to answer, but it comes out as a mumble. You eventually stumble through the words."

        a gloom "\"Eleven... zero... two.\""

        play sound "sound/keypad-door.flac"
        
        "You hear the beep of her punching in the code, then the click of the bolt sliding open."

        "She gently pries the umbrella from your arms and leaves it just inside the front door to dry on the doormat. Most of the mud washed off of you both from the rain, but you're still drenched."

        hide bg gate night with dissolve
        show bg bathroom night with dissolve 

        "She deposits you gently on the entryway bench and peels your dripping shoes and socks off."

        e shocked "\"We need to get you clean and dry, let's get upstairs, okay?\""

        "With her help you climb the stairs, leaving little puddles behind you."

        "Your house is still quite warm from the summer day, but dehumidifiers and a little bit of magic always ensure that the house stays dry and relatively cool, to preserve the condition of the books on the first floor."
        
        play music romance fadein 3.5
        
        "Erin looks around for the bathroom, finds it, and leads you over to it. She flicks on the lights."

        $ make_day()
        show bg bathroom with dissolve

        e neutral "\"Get out of those clothes and into a nice hot shower, okay? I'd help you, but...\""

        "There's a faint blush growing brighter on her cheeks that snaps you out of my miserable fugue."

        a blush "\"No! No, it's okay, I got it.\""

        "You step into the bathroom and shut the door behind you. A moment later, you peek out and offer Erin a towel."

        a tsuntsun "\"So you can dry off while you wait for your turn.\""

        e neutral "\"I can just go home, it's alright.\""

        a "\"It's pouring out there! You'll catch a cold. Dry off for now, I'll find you a change of clothes once I'm out of the shower.\""
        
        # shower/water sounds?

        "Soapy water cleanses your body and the heat clears your mind. You feel the tightness leave stiff muscles. You pat yourself dry and wrap a towel tightly around your body, leaving your wet and muddy clothes in one of the two bathroom sinks."
        
        "When you crack open the bathroom door you see Erin sitting on the rug with hair down and a towel draped over her shoulders. Her bare lower back peeks out beneath the towel."

        "Her soaking wet shirt is hanging from the back of a wooden chair. A dish towel on the floor catches the water dripping off of the discarded clothing. You make a small noise and she turns her head to look at me."

        "Just her head. Thankfully."

        "Your words pour out like a flood, one word tripping after the other."

        a blush "\"Bathroom's open your turn I'll get you some clothes DON'T LOOK AT ME!\""

        "You hobble across the hall to your bedroom and swing the door shut before digging out a t-shirt and sweatpants for yourself. You lay out another tee and pair of drawstring shorts that should probably fit Erin."

        "When you're dressed, you take the extra clothes and knock on the bathroom door."

        e happy "\"Almost done!\""

        a happy "\"Take your time, I'm just setting some clothes for you by the door.\""

        hide bg bathroom with dissolve
        show bg kitchen with dissolve

        "Erin finds you in the kitchen. Your water heater is half-done boiling water for tea and there's an ice pack on your ankle, which you've propped up on a second kitchen chair."
        
        e blush "\"Thank you, the clothes fit well!\""

        "Your clothes are, in fact, too big on her. The effect is absolutely adorable. She has a hand towel draped over top of her head, and the shirt is long enough that it almost covers the cotton shorts."

        a blush "\"It's no trouble. I'll start some laundry, just, uh, check your pockets before I put it in the machine.\""

        e neutral "\"I appreciate that, but you should just sit there and rest your ankle. I'll start it for you, just tell me if there's anything special about the machine, okay?\""

        a excited "\"You carried me all the way here. The least I can do is wash your wet clothes.\""

        "Despite your protests, she opens a couple of doors until she finds the little closet with the washer and dryer."

        e  happy "\"You need to rest! I'll tie you down if I need to! Wait here.\""


        # CHOICE
        menu:
            "Tie you down? You didn't think you were into that, but...":
                jump kinda_hot

            "But this is MY house! I should be a good host!":
                jump my_house_laundry

        label kinda_hot:
            a blush "\"Why was that kinda hot?\""

            "Erin peeks her head out from the laundry room."

            e neutral "\"Did you say something?\""

            a excited "\"Nope! Carry on!!\""

            a "(I'm going to file this thought away for later.)"

            "You shake your head furiously and clap palms to your cheeks."
            
            a blush "(ANYWAYS.)"

            jump one_bed

        label my_house_laundry:

            a "(The audacity to boss me around in my own home!)"

            a tsuntsun "(What am I going to do with this girl?)"

            jump one_bed

    label one_bed:

        "The storm has worsened. You're each on your second cup of tea and it's getting late into the night."

        "The windows rattle from the storm."

        a neutral "\"I think you might want to stay here tonight.\""

        "Erin gives me a look."

        e neutral "\"I thought you wouldn't want me to stay here.\""

        a shocked "\"Well, I'm not sending you out in that weather.\""

        e gloom "\"Okay, that's fair. I can sleep on the couch, do you have some blankets?\""

        a "\"No!\""

        e blush "\"N-no?\""

        "Your cheeks redden."

        a blush "\"I mean, w-well, the couch really isn't all that comfortable to sleep on. And I have extra blankets. And my bed is, well, kind of massive. So there's plenty of room! We wouldn't even touch, I guarantee it.\""

        "She plays it cool."

        e "\"Oh well I suppose that would work.\""

        a "\"Cool! Cool. Great!\""

        e rizzler "\"You know, I wouldn't mind if we did touch—\""

        a tsuntsun "\"Ack! It's over this way!!!\""

        "You show her to your room and sit on the bed, bouncing a little."

        show bg bedroom with dissolve
        pause 2.0


        a happy "\"Right. So! There are blankets on the dresser over there. Use whichever ones you want.\""

        e happy "\"Thanks!\""

        "She grabs a soft, blue cotton blanket and the fluffy winter duvet. You raise an eyebrow at that."

        a neutral "\"Won't you be hot? It's still summer...\""

        e excited "\"I sleep better with some layers on me, I won't overheat!\""

        "So cute."

        "You each build your little nests and tuck into bed. You pull the lamp cord."

        $ make_night()
        show bg bedroom night with dissolve

        play sound "sound/Rain Drippy.flac" volume 0.2 fadein 2.0 loop

        e happy "\"Aya?\""

        a happy "\"Mmhm?\""

        "She rolls onto her side to face you. You're close enough that you can feel the warmth of her breath."

        e excited "\"Thank you for this... you're really sweet, you know.\""

        a blush "\"Y-you're sweet, too.\""

        "In the dim light I can see the curve of her cheek as she smiles."

        "You smile back and roll over, burying your face in the pillow."

        "You're about to doze off when you feel a shiver up your spine."

        "Your tail is draped across her, you must have shifted in your sleep."

        "And Erin... she's petting your tail. Your very fluffy, very soft, very SENSITIVE tail."

        "You bite your lip to hold back a noise you definitely don't want to make in front of her and slowly slip your tail from beneath her hand."

        "You whisper hoarsely,"

        a blush "\"Erin!\""

        "She mumbles and rubs at her eyes."

        e neutral "\"What's up...?\""

        a "\"W-well, you were, um... petting my tail.\""

        "She gives you an innocent, sleepy smile."
        
        e "\"It's so soft.\""

        "Then she looks alarmed and half sits up."

        e shocked "\"Wait, was that wrong? Did I super mess up???\""

        a "\"Well, fox tails are very sensitive... in a certain way...\""

        e "\"Oh no. No no no no. I'm so sorry, I didn't realize! I wasn't trying to... I didn't mean to...! It was just draped over me and was sooo soft and I thought it was an invitation...!\""

        e neutral "\"I didn't mean to make you uncomfortable. I'm genuinely sorry.\""

        a happy "\"I'm really not upset. It was VERY nice. Just unexpected.\""

        e neutral "\"Now that I know, I'll be sure to keep my hands to myself.\""

        e rizzler "\"Or not, if you'd like.\"" 
        
        e happy "\"But you have to let me know. You set the pace.\""

        a blush "(I would NOT like. I definitely would NOT like to brush her hair and tuck it behind her ear, and pull up her covers and pull her close. I most certainly would NOT like to see how soft her lips are as she pets my tail...)"

        "You squeak out an \"Okay!\""

        "You roll over and pull your blanket over your head, hiding from her and from your wandering thoughts."

        "You can practically feel her smile on your back."

        "Eventually, the patter of the rain on the roof lulls yo uboth until you can't keep awake any longer. You fall into a dreamless sleep."

        "This feels... right."
        
        scene brown with dissolve
        stop music fadeout 2.0
        stop sound fadeout 2.0
        pause 3.0
    
    menu:
        "Wake up bright and early":
            jump rain_wake_early

        "Sleep in":
            jump rain_sleep_in

    label rain_wake_early:
        $ make_day()
        show bg bedroom with dissolve
        play music coffee fadein 0.5

        "You wake up pleasantly warm."

        "Erin is curled up at near your back with the blankets piled atop her. One arm escaped the blanket nest and flopped to the side. She's not touching you, but... Your fluffy tail is once again draped across her body."

        "Weak morning sunlight peeks through the shut curtains, casting cool rays across her bundled-up form."

        "You roll over carefully. When you slip your tail gently off her she mumbles a bit in protest."

        "She's {i}so{/i} cute sleepy."

        a happy "(I wonder what it would be like to wake up like this every morning?)"

        "You're sure you can't be thinking like that."

        a neutral "\"I have to stop!\""

        "You clap a hand over your mouth in horror."

        a "(I did NOT mean to say that out loud.)"

        "But you didn't seem to wake her, thankfully."

        "You slip out of the bed and tiptoe to the bathroom to get yourself ready for the day."

        "You take your time. When you're feeling fresh and ready for the day you plod over to the kitchen. Your ankle feels better today."
        a happy "\"Maybe I should make her breakfast.\""

        jump the_call

    label rain_sleep_in:
        $ make_day()
        show bg bedroom with dissolve
        play music coffee fadein 0.5

        "The bed is empty when you wake, Erin's blankets folded neatly on the side table."
        
        "You rub the sleep from your eyes and slip from the bed, heading to the bathroom."

        a neutral "(Did she leave?)"

        "You get ready for the day and plod to the kitchen. Your ankle feels better today."
        
        show bg kitchen with dissolve

        "Something's out of place."

        "There's a plate on the dining table with an overturned bowl on it. You lift the bowl, revealing still-warm eggs and a bagel inside."

        "It looks like Erin cooked breakfast! You need a drink, then you should find her and thank her."

        jump the_call