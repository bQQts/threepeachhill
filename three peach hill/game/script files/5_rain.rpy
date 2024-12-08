label chapter_five:    # 5. The Rain - Caught in the rain… and there was only one bed? Perchance?
    $ chapter_num = 5
    label the_rain:

        scene brown
        show bg orchard with dissolve

        "I finish picking the peaches by myself. By the time I'm done, the remaining daylight is nearly smothered by thick clouds. I hadn't noticed how dense they had gotten, but a brief glance is enough to confirm that they look heavy and full, as if ready to spill at any moment."

        "I'm rolling my small cart quickly through the orchard when I feel the first droplets splash my brow, my hair, my hand. It's a long way back to my bike, and then I'll still have to cycle home from there. I don't even have a jacket."

        a gloom "\"This is going to suck.\""

        play sound "sound/Rain Moderate.flac" fadein 1.5 volume 0.6 loop
        "The dirt path quickly turns to mud that sucks at my feet with every step. But still, I keep on, now dragging my mud-caked cart of peaches as the early evening sets in."


        scene bg rain with dissolve
        pause 1.5

        "I slip in a particularly muddy patch and fall. I sit in the mud, contemplating my life."
        
        "My ankle is definitely sprained. I have no idea how I'm going to get these peaches back. I'm drenched, and I was just not very nice to a girl I really quite like for really no good reason."

        "I close my eyes and tilt my head back, letting the raindrops splash across my face. I take a few deep breaths."

        "The rain stops drip-dropping on my face, but I can still hear it around me. I open my eyes."

        show erin shocked at center, erin_size

        "It's Erin. She's holding an umbrella over me, looking breathless and disheveled."

        hide erin with dissolve

        e shocked "\"I ran to get an umbrella as soon as I saw how bad the sky was getting. Looks like I didn't make it to you in time though, sorry, Aya. Why are you sitting in the mud? You're soaked through!\""
        

        a sad "\"Erin...\""

        e neutral "The shorter woman hands me the umbrella and helps me to my feet."

        e neutral "\"Can you walk?\""

        a "\"Yes,\""

        "I put weight onto my foot and wince."

        a  gloom "\"Well, no. My ankle...\""

        "Erin turns around and crouches, gesturing for me to climb up on her back."

        e happy "\"Get on, I'll carry you.\""

        a sad "\"But I'm taller than you! I'll crush you!\""

        e excited "\"I'm like an ant, I can carry you no problem!\""

        a gloom "\"Erin, I'll just lean on you and we'll go slow.\""

        e "\"Really, I insist! I'm wearing work boots, I won't slip in the mud. Let me carry you.\""

        a sad "\"What about the peaches?\""

        e happy "\"There will be more peaches. I'm more worried about you right now. Now, climb on.\""

        "I climb on, still holding the umbrella in one hand. She hikes me up, grasping below my thighs and leaning forward. My wet hair sticks to her neck. I try not to think about it."

        window hide dissolve
        stop sound fadeout 3.0
        pause 1.0
        scene brown
        show cg piggyback with Dissolve(3)

        pause 120.0

        window show dissolve
        "It takes a while, but we do make it down the big hill. Erin is stronger than she looks, and though she's breathing hard by the time we get back to the entrance of the orchard she hasn't once lost her grip or stumbled."


        "Erin" "\"Just hang on tight, I'll get you home.\""

        "I let the umbrella rest over our backs, which probably makes us look like an overly large beetle, and let the sway of her steps and the sound of her breathing lull me into a half-slumber."
        
        window hide
        $ make_night()
        scene brown with Dissolve(3)
        stop music fadeout 3.0
        stop sound fadeout 3.0
        pause 3.0
        show bg gate night with dissolve
        window show

        e "\"What's your door code? ...Aya?\""

        "She's hunched over at the side door of the bookshop that leads up to my house. I blink, rubbing my sleepy eyes with the back of a hand."

        e neutral "\"Hey, Aya? You okay?\""

        "There's concern in her voice and I try to answer, but it comes out as a mumble. I eventually stumble through the words."

        a gloom "\"11... 0... 2.\""

        play sound "sound/keypad-door.flac"
        
        "I hear the beep of her punching in the code, and the click of the bolt sliding open."

        "She gently pries the umbrella from my arms and leaves it just inside the front door to dry on the doormat. Most of the mud washed off us from the rain, but we're still drenched."

        hide bg gate night with dissolve
        show bg bathroom night with dissolve 

        "She deposits me gently on the entryway bench and peels our dripping shoes and socks off."

        e shocked "\"We need to get you clean and dry, let's get upstairs, okay?\""

        "We climb the stairs, leaving little puddles behind us."

        "My house is still quite warm from the summer day, but dry—dehumidifiers and a little bit of magic always ensure that the house stays dry and relatively cool, to preserve the condition of the books on the first floor."
        
        play music "music/Romance LoFi.flac" fadein 3.5
        
        "Erin looks around for the bathroom, finds it, and leads me over to it. She flicks on the lights."

        $ make_day()
        show bg bathroom with dissolve

        e neutral "\"Get out of those clothes and into a nice hot shower, okay? I'd help you, but...\""

        "There's a faint blush growing brighter on her cheeks that snaps me out of my miserable fugue."

        a blush "\"No! No, it's okay, I got it.\""

        "I step in and shut the door behind me. A moment later, I peek out and offer Erin a towel."

        a tsuntsun "\"So you can dry off while you wait for your turn.\""

        e neutral "\"I can just go home, it's alright.\""

        a "\"It's pouring out there! You'll catch a cold. Dry off for now, I'll find you a change of clothes once I'm out of the shower.\""

        "Soapy water cleanses my body and the heat clears my mind. I feel the tightness leave stiff muscles. I pat myself dry and wrap a towel tightly around myself, leaving my wet and muddy clothes in one of the two bathroom sinks."
        
        "Then I crack open the bathroom door to see Erin sitting on the rug with the towel draped over her now-bare shoulders."

        "Bare? Shoulders? I glance to a nearby kitchen chair, where her soaking wet shirt is hanging. A dish towel on the floor catches the water dripping off of the discarded clothing. I clear my throat and she turns her head to look at me."

        a blush "\"Bathroom's open, your turn, I'll get you some clothes, DON'T LOOK AT ME!\""

        "I hobble across the hall to my bedroom and swing the door shut before digging out a t-shirt and sweatpants for myself, and another tee and pair of drawstring shorts that should probably fit Erin."

        "When I'm dressed, I take the extra clothes and knock on the bathroom door."

        e happy "\"Almost done!\""

        a happy "\"Take your time, I'm just setting some clothes for you by the door.\""

        hide bg bathroom with dissolve
        show bg kitchen with dissolve

        "When Erin comes out, I have an instant kettle heating water for tea and an ice pack on my ankle, which I've propped up on a second kitchen chair."
        
        e blush "\"Thank you, the clothes fit well!\""

        "My clothes are, in fact, too big on her. The effect is absolutely adorable. She has a hand towel draped over top of her head, and the shirt is long enough that it almost covers the cotton shorts."

        a blush "\"It's no trouble. I'll start some laundry, just check your pockets before I put it in the machine.\""

        e neutral "\"I appreciate that, but you should just sit there and rest your ankle. I'll start it for you, just tell me if there's anything special about the machine, okay?\""

        a excited "\"You carried me all the way here. The least I can do is wash your wet clothes.\""

        "Despite my protests, she opens a couple of doors until she finds the little room with the washer and dryer."

        e  happy "\"You need to rest! I'll tie you down if I need to! Wait here.\""


        # CHOICE
        menu:
            " Oh my. That was kinda... you know...":
                jump kinda_hot

            "But this is MY house!":
                jump my_house_laundry

        label kinda_hot:
            a blush "\"Why was that kinda hot?\""

            "Erin peeks her head out from the laundry room."

            e neutral "\"Did you say something?\""

            a excited "\"Nope! Carry on!!\""

            "(I'm going to file this thought away for later.)"

            "I shake my head furiously and clap my palms to my cheeks."
            
            "(ANYWAYS.)"

            jump one_bed

        label my_house_laundry:

            "(The audacity to boss me around in my own home!)"

            "(What am I going to do with this girl?)"

            jump one_bed

    label one_bed:

        "The storm has worsened. We're each on our second cup of tea and it's getting late into the night."

        a neutral "\"I think you might want to stay here tonight.\""

        "Erin gives me a look."

        e neutral "\"I thought you wouldn't want me to stay here.\""

        a shocked "\"Well, I'm not sending you out in that weather.\""

        e gloom "\"Okay, that's fair. I can sleep on the couch!\""

        a "\"No!\""

        e blush "\"N-no?\""

        "My cheeks redden."

        a blush "\"I mean, w-well, the couch really isn't all that comfortable to sleep on. And I have extra blankets. And my bed is, well, kind of massive. So there's plenty of room! We wouldn't even touch, I guarantee it.\""

        "She plays it cool."

        e "\"Oh well I suppose that would work.\""

        a "\"Cool! Cool. Great!\""

        e rizzler "\"You know, I wouldn't mind if we did touch—\""

        a tsuntsun "\"Ack! It's over this way!!!\""

        "I show her to my room and sit on the bed, bouncing a little."

        show bg bedroom with dissolve
        pause 2.0


        a happy "\"Right. So! There are blankets on the dresser over there. Use whichever ones you want.\""

        e happy "\"Thanks!\""

        "She grabs a soft, blue cotton blanket and the fluffy winter duvet. I raise my eyebrow at that."

        a neutral "\"Won't you be hot? It's still summer...\""

        e excited "\"I sleep better with some layers on me, I won't overheat!\""

        "So cute."

        "We build our little nests and tuck into bed. I pull the lamp cord."

        $ make_night()
        show bg bedroom night with dissolve

        play sound "sound/Rain Drippy.flac" volume 0.2 fadein 2.0 loop

        e happy "\"Aya?\""

        a happy "\"Mmhm?\""

        "She rolls onto her side, facing me. Our faces are close enough that I can feel the warmth of her breath."

        e excited "\"Thank you for this... you're really sweet, you know.\""

        a blush "\"Ahh, don't make it weird.\""

        "In the dim light I can see the curve of her cheek as she smiles."

        e rizzler "\"I can keep my hands and thoughts to myself. Or not, if you'd like. Just let me know.\""

        "(I would NOT like. I definitely would NOT like to brush her hair and tuck it behind her ear, and pull up her covers and pull her close. I most certainly would NOT like to see how soft her lips are...)"

        "I roll over and pull my blanket over my head, hiding from her and from my thoughts."

        "I can practically feel her smile on my back."

        "Eventually, the patter of the rain on the roof lulls me until I can't keep myself awake any longer. I fall into a dreamless sleep."

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

        "I wake up pleasantly warm."

        "Erin is curled up at my back with the blankets piled atop her. One arm escaped the blanket nest and comfortably hugs my fluffy tail close to her body."

        "Weak morning sunlight peeks through the shut curtains, casting cool rays across her bundled-up form."

        "I roll over carefully. When I slip my tail gently from her arms she mumbles a bit in protest."

        "She's {i}so{/i} cute."

        "(I wonder what it would be like to wake up like this every morning?)"

        "I can't think like that!"

        a gloom "\"What the hell, Aya!\""

        "I clap a hand over my mouth in horror."

        "I did NOT mean to say that out loud."

        "But I didn't seem to wake her, thankfully."

        "I slip out of the bed and tiptoe to the bathroom to get myself ready for the day."

        "I take my time. When I'm feeling fresh and ready for the day I plod over to the kitchen. Maybe I should make her breakfast."

        jump the_call

    label rain_sleep_in:
        "The bed is empty when I wake up, Erin's blankets folded neatly back up on the side table."
        
        "I rub the sleep from my eyes and slip from the bed, heading to the bathroom."

        "Did she leave?"

        "I get myself ready for the day and trod to the kitchen."

        "Something's out of place."

        "There's a plate on the dining table with an overturned bowl on it. I lift the bowl, revealing still-warm eggs and a bagel inside."

        "It looks like Erin cooked breakfast! I need a drink, then I should find her and thank her."

        jump the_call