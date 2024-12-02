label chapter_eight:
    $ chapter_num = 8
    label lost_market:

        "The next couple of weeks are peaceful. The air keeps getting cooler, the farmers markets have been lovely."

        "I get into a sort of routine with Erin."

        menu:
            "We meet at the bookstore":
                jump lost_market_bookstore
            
            "We meet at the orchard office":
                jump lost_market_office
            
            "We meet at my house":
                jump lost_market_aya_house


    label lost_market_bookstore:
        show bg bookstore with dissolve
        play music bookstore_sunshine fadein 0.5 noloop
        "The bookstore is the perfect place to meet up and talk about marketing plans."

        jump lost_market_cont

    label lost_market_office:
        show bg orchard with dissolve
        play music happy_village fadein 0.5 noloop
        "The office has lots of room to meet with people and map out plans on the big, clear tables."

        jump lost_market_cont

    label lost_market_aya_house:
        show bg kitchen with dissolve
        play music romance fadein 0.5
        "My house. It's comfortable, private, and we can make as much of a mess of notes and projects as we want."

        jump lost_market_cont


    label lost_market_cont:

        "When Erin isn't working, we make drafts, print posters and fliers, and make this our base of operations for the Great Bookstore Revival."

        "Erin calls investors and organizations who might help with such a funding project, while I call local shops to discuss business collaborations."

        "It's really nice."

        window hide

    label lost_market_find_out:
        scene brown with irisin
        stop music fadeout 3
        pause 2.0
        show date_animated_ch8 with dissolve    # August 19, Monday
        pause 5.0
        $ make_night()
        scene brown with dissolve

        "Erin didn't show up at the usual meeting time. I wait 20 minutes."

        play music rain_transition noloop

        "Twenty minutes turns into an hour, then two. She's not answering her phone."
        show bg bookstore night with dissolve 
        "I check near the bookstore. She's not there."
        hide bg bookstore night with dissolve
        show bg cornerstore night with dissolve

        "I call the cornerstore and the orchard office, and am told she's not there either."
        hide bg cornerstore night with dissolve
        scene brown with dissolve

        "I bite my lip. I'm starting to worry that something has happened."
        show bg kitchen night with dissolve
        "At home, I put on a jacket and sneakers and pace in the front room, trying to decide where to start looking for her."
        hide bg kitchen night with dissolve
        show bg gate night with dissolve
        
        play sound "sound/Knocking-2.flac"
        
        "There's a knock at the door, and I run to open it."

        a shocked "\"Erin? Oh, Lydia! What are you doing here?\""
        show lydia night at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300
        "It's not who I was hoping it would be, and judging by Lydia's expression, I'm not about to be happy that she's here either."

        lyd "\"You haven't found a spell to fix that lamp yet, right?\""

        a neutral "\"N-no, not yet, we're planning to go find the Lost Market in a few days. Do you want to come in?\""

        lyd "\"The Market came early, Aya.\""

        "I get a sinking feeling in my stomach."

        a shocked "\"No. She couldn't have...\""

        lyd "\"She did. Terry the fox spirit saw her go in unaccompanied and ran to tell me.\""

        a "\"Shit. And you didn't call...\""

        lyd "\"...because I still don't own a phone.\""

        "Of course this ancient cat still hasn't gotten a phone."

        a neutral "\"I need to find her, fast. Where's the entrance?\""

        lyd "\"The alley between the grocer and the barber. Be safe, and be quick. I hope you find her in time.\""
        
        window hide
        hide lydia night with dissolve
        scene brown with dissolve
        "I run."

        stop music fadeout 2.0

        jump lost_market_inside

    label lost_market_inside:

        scene brown
        show bg rain night
        show aya at center
        stop music fadeout 3.0
        play music spirit fadein 0.5

        "I run faster than I ever have before. My legs and lungs burn, and I gasp for air, but I push through it and finally make it to the entrance."

        "The entrance to the Lost Market always looks like a really, really, REALLY long, dark alleyway with floating lights at the far end of it."

        "It doesn't usually pose a risk to humans, since you have to be a spirit or in a pact with a spirit to be able to see it at all."

        "And if you can't see it, it can't see you back."

        scene brown with dissolve
        show bg rain night with dissolve

        "I slow down and start walking down the alley. It's actually faster to walk than it is to run. It's tricky like that."

        "The floating lights start to illuminate faint edges of structures in the alleyway; the ground, the brick walls, loose rocks, some cardboard boxes."

        "The amber glow grows, and I step out of the alley into a street full of spirits of all shape and size."
        hide bg rain night with dissolve
        scene brown
        window hide
        $ make_day()
        show bg nightmarket with dissolve
        pause 1.0
        
        show aya fox at center with dissolve:
            subpixel True zoom 0.39 


        window hide
        play sound "sound/Deep Echo Passby 01.flac"
        show aya fox:
            subpixel True 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            linear 1.82 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-696.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        with Pause(1.92)
        show aya fox:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-696.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        pause 2.0
        window show


        "As naturally as breathing, I shift fully into my spirit form: an enormous pink three-tailed fox with small red horns. I sniff the air and stretch out each leg, feeling my paws against the cool ground."



        "Tall, shapeless giants and tiny floating imps float alongside animal spirits like myself."

        "I don't waste any time."

        "I run, weaving through the silent crowd, following the faint, unmistakable glowing tether of the pact we made. I pick up the citrus and apple scent of Erin's shampoo."

        "I have to go faster!"

        "I run and I run, and finally I know I'm drawing near when the tether glows brighter. A small crowd has formed a circle around her."

        show bg nightmarket red with dissolve
        
        window hide
        $ make_night()
        hide aya with dissolve

        with Pause(3.10)

        show oni night at right, oni_size
        show erin neutral at center, erin_size


        show aya fox at left with dissolve:
            subpixel True zoom 0.39 
        window show



        "She's standing boldly before an oni girl with impossibly sharp horns. A red ribbon floats around the oni, and a tendril begins to reach towards Erin."

        "I leap, snapping at the ribbon. It shatters into sparkling shards of light between my sharp teeth."

        hide erin with dissolve


        "Oni" "\"You dare to intefere? This human wished to make a pact with me, fox. I was simply going to lead her out of here.\""
        
        hide aya
        a fox "\"In exchange for what?\""
        
        show aya fox at left:
            subpixel True zoom 0.39 
        "Oni" "\"A trifling matter. She was to bring me across to the mortal realm with her.\""
        
        hide aya 
        a fox "\"I'm afraid that is not going to be possible. This human is spoken for. She's already in a pact with me.\""
        
        show aya fox at left:
            subpixel True zoom 0.39 
        "Oni" "\"If that is so, why did she need a guide out?\""
        
        hide aya
        a fox "\"I was merely busy for a moment, but am here now.\""
        
        show aya fox at left:
            subpixel True zoom 0.39 
        "Erin looks at me, astonished at my form."

        hide erin with dissolve
        hide aya with dissolve
        e shocked "\"Wait... Aya?! You can... talk like that?\""

        a fox "\"Of course. I'm still me.\""
     
        show aya fox at left:
            subpixel True zoom 0.39 
        "I address the oni."

        hide aya
        a fox "\"We must depart. Kindly find someone else to bargain with.\""

        show aya fox at left:
            subpixel True zoom 0.39 
        "The oni glares at me and crosses her arms."
        
        hide aya
        a fox "\"Erin, climb upon my back. I'll take us out of here.\""

        e sad "\"Are you sure? Shouldn't we find that spell?\""

        a fox "\"Not tonight.\""

        show aya fox at left:
            subpixel True zoom 0.39 
        "She reluctantly grabs hold of my fur and hauls herself onto my back, hugging my neck tightly."
        
        hide oni night with dissolve
        show bg nightmarket night with dissolve

        "I fly like the wind and take us back to the alley. The streets shift around us, but I know exactly where to go."
        hide aya
        a fox "\"Close your eyes.\""

        show aya fox at left:
            subpixel True zoom 0.39 
        "We race across the border between the spirit and mortal worlds. It's easier to leave with both of us present."


        "The air around us blurs and I shift back, now holding Erin in my arms."

        stop music fadeout 3.0
        scene brown with dissolve
        pause 2.0
        show bg market night with dissolve
        play music quiet_village fadein 0.5

        a blush "\"You can open your eyes now, Erin.\""

        "She does."

        e blush "\"Uh, you don't have to keep carrying me.\""

        a "\"Ah, sorry.\""

        "I set her on her feet and help straighten out her clothes. I check her for the telltale ribbons of other pacts but see none."

        a sad "\"Are you alright? You didn't make any other bargains while there, right?\""

        e neutral "\"No, no. That was close, though. I had been there for hours, and had been hounded by all sorts of spirits wanting... different things.\""

        e "\"That last one was kinder than the others, though, so it seemed like my best option for getting back home.\""

        a "\"She may have seemed kinder, but that doesn't mean she didn't have ill-intent. If you had brought her over, she would have eaten you.\""

        "Erin blanches."

        e "\"O-oh.\""

        "I soften my expression."

        a neutral "\"How did you get there, anyway?\""

        e "\"Well, I was following that little grey cat and it went down this alley. It disappeared, and I was curious about the lights, so... I kept walking. I had never seen that before.\""

        a "\"Oh, Erin.\""

        "I pull her into my arms and hold her tightly."

        a shocked "\"I'm so glad I found you in time. That was so reckless!\""

        e gloom "\"I didn't know what would happen!\""

        "I smooth her hair and heave a sigh of relief."

        a happy "\"I know. It's okay. Just... don't go into any weird alleys like that without me, okay? Don't make me worry like that!\""

        e sad "\"I won't. But do you think that cat is okay?\""

        a "\"I'm positive it is. Cats have a way of slinking across the boundary with more ease than practically any other creature. If it crossed over, it can simply stroll right back.\""

        a excited "\"And since it's just a cat, nothing is going to bother it.\""

        e excited "\"Thank goodness!\""

        "We stay embraced for a few long breaths as our heartbeats slow, then I release her."

        a happy "\"I'll walk you home.\""

        e happy "\"Sure, I'd like that.\""
        
        window hide
        scene brown with dissolve
        pause 2.0

        jump date

