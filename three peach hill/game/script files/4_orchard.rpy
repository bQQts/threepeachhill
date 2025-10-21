label chapter_four:
    $ chapter_num = 4
    label orchard:
        pause 1.5
        show date_animated_ch4 with dissolve  # August 3
        pause 2.5
        hide date_animated_ch4 with Dissolve(2)
        
        scene brown
        show bg bookstore with dissolve
        play music bookstore_vibing fadein 2.0

        "Another week goes by. You manage to avoid running into Erin. She's sent more pictures of the gray cat outside of the cornerstore, but you haven't replied."

        "She's really persistent and dripping with optimism. But you suspect she can probably tell that something's off."

        "The whole thing—trying to smother your feelings, avoiding her—it's got you in a sour mood. So, today you're going out."

        "Your first stop is the orchard. Three Peach Hill started very small, and like the name implies, it began with just three peach saplings on the big hill."

        "The orchard expanded outward from that hill. Those first three peach trees are now massive. They should be well past their prime, but through magic they've stayed young and healthy and continue to produce beautiful fruit every season."

        "You've loved resting under their boughs since you were a kit. It's not a private place by any means, but it's {i}your{/i} spot. A visit seems like just the thing to center you right now."
        
        hide bg bookstore with dissolve
        show bg orchard with dissolve

        stop music fadeout 3.0
        queue music quiet_village fadein 0.5

        "The team who tends the orchard under Head Orchardist Joy have been busy now that harvest season's here."
        
        show joy at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300

        a excited "Joy is directing a couple of young men loading her truck with an order of peaches. You wave to her as you park your bicycle alongside the orchard's front office building. She waves back with a big grin."

        "Yesterday she had posted a picture of the juciest looking peaches hanging heavy on their branches to her social media page with the caption, \"Peach picking is open! Come by to fill a cart or basket!\""
        hide joy with dissolve
        "You couldn't make it out here yesterday, but it's a nice Saturday, you have the whole day free, and this is your favorite place to relax. The pie you're gonna make out of these is going to be legendary."

        "You're walking up the hill when you hear her voice. Your heart beats a little faster. Is it anxiety, or excitement?"

        "Erin is here of all places, on today of all days. Just your luck."

        "She looks incredible in her oversized shirt and messy bun. She wipes her brow with the back of a work-gloved hand, laughing at something a girl in a VOLUNTEER vest said."
        
        "There's a basket of peaches on the ground beside them. You keep walking, hoping she doesn't notice you."

        e happy "\"Aya,\""

        "Erin calls out to you, jogging to catch up as you {i}very subtly{/i} pick up your pace."

        e excited "\"Oh my god hi! I didn't expect to see you here!\""

        "You reply without looking back:"

        a gloom "\"Hi.\"" 

        "You can't hide your mood. In fact, you're sure your ears are flopped down pathetically."

        "How rude of her to thwart your avoidance of her by total coincidence!" 
        
        "Surely she'll get the memo if you're brusque with her. Right? So maybe you should be a little crabbier. That'll push her away."

        "You walk faster."

        e neutral "\"Wait!\"" 

        "She catches your hand and you lurch as she tugs your arm gently but firmly. You yank your arm back, and she immediately lets go. The lack of resistance throws you off balance. You stumble."

        "You know you're being dramatic. The embarassment of it all stings."

        a sad "\"What... what do you want?\""

        e sad "\"Oh, sorry, didn't mean to throw you off balance. I just wanted to talk 'cuz it seems like you've been avoiding me—or maybe I'm just reading into it? But you haven't responded to any of my cat pics and I haven't seen you around the cornerstore.\""

        a "\"...\""

        "You sigh."

        a neutral "\"I have been. Avoiding you, that is.\""

        e neutral "\"I didn't do anything, though.\""
        
        a sad "\"No, you're right. That's true... but...\""

        e sad "\"Was I sending too many pictures of Cloud? Or maybe... was I being too much?\""

        "Her tone alarms you. This isn't what you wanted!"

        a blush "\"No! No, I...\""

        "You don't want her to stop doing any of that."
        
        e neutral "\"Wait...\""

        a "(Oh no. Stay cool, Aya.)"

        "She lookes closer at your face and sees the blush creeping across your cheeks."

        e rizzler "\"Were you possibly avoiding me because youuuu like me back?\""

        "It's too much. The closeness of her face, her directness... You flush hot red."

        e excited "\"Eeeeee! You like me!!!\""

        "She covers a grin with her hand and giggles."

        a tsuntsun "\"What! No! That's absurd!\""

        e gloom "\"Your face says otherwise, but fine.\""
        
        e neutral "\"Explain it to me, then. If I haven't done anything wrong, why are you avoiding me? I think it's because you like me and are just feeling shy. Am I wrong?\""

        "She looks a bit hurt, and my heart aches at the sight."
        
        "But... I really don't want to get involved in something temporary. Whether or not I like her, I need to do this."

        stop music fadeout 1.0

    menu:
        "I've got to put an end to this before something starts."

        "\"You're wrong!\" (Be harsh)":
            jump shut_this_down

        "(2+ Hearts) \"I do like you, but...\" (Be gentle)" if kind_points >= 2:
            jump let_her_down_gently

    label shut_this_down:
        queue music rain_transition fadein 1.0 noloop
        queue music rain

        a "\"I don't like you at all.\""

        "...is what you said. It's a blatant lie. But you say it with enough conviction that it sells the lie."
        
        a sad "(I don't want it to hurt when she leaves.)"

        "Erin's eyes mist with tears."

        e sad "\"But, I thought... at the market, and then at your house...\""

        "Your heart hurts. You loved that day. You reach for something to say that might get you out of here."

        a sad "\"W-we're just not a good fit.\""

        e neutral "\"What do you mean? Oh my gosh, is there someone else? If so I'm sorry, I didn't realize...!\""

        a neutral "\"No, that's not it. There's no one. I just can't.\""

        e neutral "\"Are you afraid to like me?\""

        "You don't respond. That's answer enough for Erin."

        e "\"...I hope I can earn your trust, Aya. I'll give you some space.\""

        "Without another word, she turns and walks away."

        "You wonder if you blew it. But maybe that's what you wanted."
        
        "What have you done?"

        scene brown with dissolve
        pause 2.0
        jump the_rain



    label let_her_down_gently:
        queue music rain_transition fadein 0.5
        queue music rain
        a blush "\"I'm, uh, taking some time to work on myself.\""

        e happy "\"Oh, that's okay! I don't need you to be different. You can just be yourself...!\""

        "That hurts your heart. She's almost too sweet." 

        "It would break your heart for her to leave you."

        a tsunstsun "\"I can't!\""

        e gloom "\"What?\""

        a gloom "(I do like you. But you have school, you're bound to leave, and I don't think you'll come back out here when you're done.)"

        a gloom "\"...What if I mess up?\""

        e shocked "\"So, you like me, but you're too scared to do anything about it because you think you'll mess it up or something?\""
        
        e sad "\"I like who you are.\""

        "Then she shoves her hands into her shorts pockets and strides back down the hill, eyes downcast."

        "She's right. You are afraid."
        
        scene brown with dissolve
        pause 2.0
        jump the_rain
