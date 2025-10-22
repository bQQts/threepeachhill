label chapter_eight:
    $ chapter_num = 8
    label lost_market:

        "The next couple of weeks are peaceful. The air keeps getting cooler, the farmers markets have been lovely."

        "You get into a sort of routine with Erin."

        menu:
            "You meet in the bookstore":
                jump lost_market_bookstore
            
            "You meet at the orchard office":
                jump lost_market_office
            
            "You meet at your house":
                jump lost_market_aya_house


    label lost_market_bookstore:
        show bg bookstore with dissolve
        play music bookstore_sunshine fadein 0.5 noloop
        "The bookstore is the perfect environment to meet up and talk about marketing plans, surrounded by generations of words of wisdom and creative ideas."

        jump lost_market_cont

    label lost_market_office:
        show bg orchard with dissolve
        play music happy_village fadein 0.5 noloop
        "The office has lots of room to meet with people and map out plans on the big glass tables."

        jump lost_market_cont

    label lost_market_aya_house:
        show bg kitchen with dissolve
        play music romance fadein 0.5
        "Your house. It's comfortable, private, and you can make as much of a mess of notes and projects as you want."

        jump lost_market_cont


    label lost_market_cont:

        "When Erin isn't working, you make drafts, print posters and fliers, and otherwise enact the Great Bookstore Revival."

        "Erin calls investors and organizations who might help with such a funding project while you call local shops to discuss business collaborations."

        "She's so supportive and optimistic that you can't help but catch her energy and feel that way, too."

        window hide

    label lost_market_find_out:
        scene brown with irisin
        stop music fadeout 3
        pause 2.0
        show date_animated_ch8 with dissolve    # August 19, Monday
        pause 5.0
        $ make_night()
        scene brown with dissolve

        "Erin didn't show up at the usual meeting time."
        
        "You wait twenty minutes."

        play music rain_transition noloop

        "Twenty minutes turns into an hour, then two. She's not answering her phone."
        show bg bookstore night with dissolve 
        "You check near the bookstore. She's not there."
        hide bg bookstore night with dissolve
        show bg cornerstore night with dissolve

        "You call the cornerstore and the orchard office and are told she's not there either."
        hide bg cornerstore night with dissolve
        scene brown with dissolve

        "You bite your lip. What if something's happened"
        show bg kitchen night with dissolve

        "At home, you put on a jacket and sneakers and pace in the front room, trying to decide where to start looking for her."
        hide bg kitchen night with dissolve
        show bg gate night with dissolve
        
        play sound "sound/Knocking-2.flac"
        
        "There's a knock at the door, and you run to open it."

        a shocked "\"Erin--! Oh, Lydia? What are you doing here?\""
        show lydia night at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300
        "It's not who you were hoping it would be, and judging by Lydia's expression, you're not about to be happy that she's here either."

        lyd "\"You haven't found a spell to fix that lamp yet, right?\""

        a neutral "\"N-no, not yet, we're planning to go find the Lost Market in a few days. Do you want to come in?\""

        lyd "\"The Market came early, Aya.\""

        "No... Oh no..."

        a shocked "\"She couldn't have...\""

        lyd "\"She did. Terry the fox spirit saw her go in unaccompanied and ran to tell me.\""

        a "\"Shit. And you didn't call...\""

        lyd "\"...because I still don't own a phone.\""

        "Of course this ancient cat still hasn't gotten a phone."

        a neutral "\"I need to find her, fast. Where's the entrance?\""

        lyd "\"The alley between the grocer and the barber. Be safe, and be quick. I really do hope you find her in time.\""
        
        window hide
        hide lydia night with dissolve
        scene brown with dissolve
        "You run."

        stop music fadeout 2.0

        jump lost_market_inside

    label lost_market_inside:

        scene brown
        show bg rain night
        show aya at center
        stop music fadeout 3.0
        play music spirit fadein 0.5

        "You run faster than you ever have before. Your legs and lungs burn and you gasp for air, but push through the exhaustion and make it to the entrance."

        "No matter where it shows up, the entrance to the Lost Market always looks like a really, REALLY long and dark alleyway with floating lights flickering at the far end of it."

        "It doesn't usually pose a risk to humans, since you have to be a spirit or in a pact with a spirit to be able to see it at all."

        "And if you can't see it, it can't see you back."

        scene brown with dissolve
        show bg rain night with dissolve

        "You slow down and start walking down the alley. It's faster to walk than to run. It's tricky like that."

        "The floating lights start to illuminate faint edges of structures in the alleyway; the ground, the brick walls, loose rocks, some cardboard boxes."

        "The amber glow grows. You step out of the alley into a street full of spirits of all shape and size."
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


        "As naturally as breathing, you shift fully into your spirit form: an enormous pink three-tailed fox with small red horns. You sniff the air and stretch out each leg, feeling your paws against the cool ground."



        "Tall, shapeless giants and tiny floating imps float alongside animal spirits like yourself."

        "You don't waste any time."

        "You run, weaving through the silent crowd, following the faint, unmistakable glowing red tether of the pact you made. Your sensitive nose picks up the citrus and apple scent of Erin's shampoo."

        "You have to go faster!"

        "You run and run, and finally you know you're drawing near when the tether glows brighter."
        
        "A small crowd has formed a circle around Erin, and she's not alone."

        window hide
        show bg nightmarket red with dissolve
           
        $ make_night()
        hide aya with dissolve

        show oni night at right with dissolve:
            subpixel True
            zoom 0.7   
            yoffset -300
        show erin neutral at center with dissolve:
            subpixel True
            zoom 0.35
            yoffset -200
        show aya fox at left with dissolve:
            subpixel True zoom 0.39 
        window show



        "She's standing boldly before an oni girl with impossibly sharp horns. A red ribbon--not yours--floats around the oni, and a tendril of it begins to reach towards Erin."

        "You leap, snapping at the ribbon. It shatters into sparkling shards of light between your sharp teeth."

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
        "Erin gapes at you, astonished."

        hide erin with dissolve
        hide aya with dissolve
        e shocked "\"Wait... Aya?! You can... talk like that?\""

        "Wait, she's not surprised that you're a fox... just surprised that you can talk?"

        a fox "\"Of course. I'm still me.\""
     
        show aya fox at left:
            subpixel True zoom 0.39 
        "You address the oni."

        hide aya
        a fox "\"We must depart. Kindly find someone else to bargain with.\""

        show aya fox at left:
            subpixel True zoom 0.39 
        "The oni glares at you and crosses her arms."

        "The crowd around you becomes agitated."

        "You had better not linger."
        
        hide aya
        a fox "\"Erin, climb upon my back. I'll take us out of here.\""

        e sad "\"Are you sure? Shouldn't we find that spell?\""

        "You shake your head."

        a fox "\"Not tonight.\""

        show aya fox at left:
            subpixel True zoom 0.39 
        "She reluctantly grabs hold of your fur and hauls herself onto your back, hugging your neck tightly."
        
        hide oni night with dissolve
        show bg nightmarket night with dissolve

        "You fly like the wind and take her back to the alley. The streets shift around you, but you know exactly where to go."
        hide aya
        a fox "\"Close your eyes.\""

        "You can't tell if she followed the instruction, so you just have to hope she heard you."

        show aya fox at left:
            subpixel True zoom 0.39 
        "You race across the border between the spirit and mortal worlds. It's easier to leave with the both of you present."


        "The air around you blurs and you shift back, now holding Erin in your arms."

        "Her eyes are shut tight."

        stop music fadeout 3.0
        scene brown with dissolve
        pause 2.0
        show bg market night with dissolve
        play music quiet_village fadein 0.5

        a blush "\"You can open your eyes now, Erin.\""

        "She opens her eyes and gazes into yours from so very close."

        "Her body is warm against yours."

        "Her lips part invitingly."

        "You could kiss her if you just..."

        e blush "\"Uh, you don't have to keep carrying me.\""

        a "\"Ah, sorry.\""

        "You set her on her feet and straighten her clothes, looking her all over. There are no telltale ribbons of other pacts, but you have to be sure."

        a sad "\"Are you alright? You didn't make any other bargains while there, right?\""

        e neutral "\"No, no. That was close, though. It felt like I had been there for hours, and had been hounded by all sorts of spirits wanting... different things.\""

        e "\"That last one was kinder than the others, though, so it seemed like my best option for getting back home.\""

        a "\"She may have seemed kinder, but that doesn't mean she didn't have ill-intent. If you had brought her over, she would have eaten you.\""

        "Erin blanches."

        e "\"O-oh.\""

        "You soften your expression."

        a neutral "\"How did you get there, anyway?\""

        e "\"Well, I was following that little grey cat and it went down this alley. It disappeared, and I was curious about the lights, so... I kept walking. I had never seen that before.\""

        a "\"Oh, Erin.\""

        "You pull her into your arms and hold her tightly. You feel so... protective of her."

        a shocked "\"I'm so glad I found you in time. That you didn't get hurt!\""

        e gloom "\"I didn't know how dangerous it was... So scary...\""

        "You smooth her hair and heave a sigh of relief."

        a happy "\"I know. It's okay. Just... don't go following weird lights like that without me, okay?\""

        e sad "\"I won't. But do you think that cat is okay?\""

        a "\"I'm positive it is. Cats have a way of slinking across the boundary with more ease than practically any other creature. If it crossed over, it can simply stroll right back.\""

        a excited "\"And since it's just a cat, nothing is going to bother it.\""

        e excited "\"Thank goodness!\""

        "You stay embraced for a few long breaths as your heartbeats slow."

        a happy "\"I'll walk you home.\""

        e happy "\"Sure, I'd like that.\""
        
        window hide
        scene brown with dissolve
        pause 2.0

        jump date

