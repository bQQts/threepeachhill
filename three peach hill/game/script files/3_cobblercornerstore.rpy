label chapter_three:
    $ chapter_num = 3
    label pursuit:
        pause 1.5
        stop music fadeout 1.5
        play music quiet_village fadein 1.5

        show date_animated_ch3 with dissolve # July 20
        pause 2.5

        hide date_animated_ch3 with Dissolve(2)

        play sound "sound/Cicada Ambience.flac" volume 0.3 fadein 2.0 loop
        "The next week is much less eventful. The air is as humid as ever. The cicadas continue to play their summer soundtrack. Finally, a totally open weekend comes calling."

    menu:
        "Which should I do first?"

        "Make peach cobbler":
            $ cobblerfirst = True
            jump cobbler
            
        "Go to the cornerstore":
            $ cornerstorefirst = True
            jump cornerstore

    label cobbler:
        stop sound fadeout 2.0
        stop music fadeout 2.0
        play music happy_village fadein 1.0
        show bg kitchen with dissolve

        "Fortunately, the peaches had sustained no damage at all during The Incident, and I'm able to whip up a couple of test cobblers."

        "The local peaches aren't quite in season yet, so these are just some of the early bloomers that Joy at the orchard set aside for me."

        "The cobblers aren't bad. They're not as sweet as I had hoped they'd be, but that makes sense since peach season starts next month. I should have accounted for the difference and adjusted my recipe, but this is good practice for the real thing!"

        "I divide the cobblers into plastic food storage bins and pack a small picnic basket with the bins I don't put in the fridge. Some of my older friends will probably love this."

        menu:
            "Who should I visit today?"

            "Joy, the orchardist":
                jump orchardist

            "The cat spirit":
                jump lydia_chat

    label orchardist:
        "Joy and I have been friends for almost my whole life. She's been running the orchard for as long as I can remember, and is probably in her 60s now."

        "We run into each other now and then, and we're friends on social media. She's a much more active poster than I am, and the extra marketing has been helpful for her orchard. People come from all over to pick peaches."

        "(It's nearly time for peach picking to open up, but not quite yet!)"

        "Since she spends all her time managing the business, she doesn't tend to do a lot of baking. I try to bring her things once in a while to check in."

        "I take my bike to her office, which is a small two-story building at the very foot of the orchard's hills. Wind chimes hang from the stoop, and the sign on the door says OPEN. When I swing the door open and step inside, I'm greeted by a couple of my neighbors sipping coffee in the lobby."
        
        scene brown with dissolve
        show bg orchard with dissolve

        pause 0.5

        show timothy at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300

        timothy "\"Well hey there! You lookin' for Joy, by any chance?\""

        a excited "\"Hey! Sure am.\""

        timothy "\"She's out in the trees today.\""

        a happy "\"Oh! No problem, I'll just drop this off upstairs.\""

        hide timothy with dissolve

        "The gentlemen wave in acknowledgement. I and my cobbler-laden picnic basket take the stairs to the second floor break room."

        "I borrow a sticky note from Joy's desk and jot down a note mentioning the cobbler, then put the cobbler in the break room fridge."

        "It's cozy, very lived-in for an administrative building. Joy's turned the downstairs into a social space with couches, bar counters, and plenty of plants so visitors and farmers alike have a place to relax out of the sun."

        "Upstairs, however, has the must and dust of decades of unchanging use. It's where the real business happens."

        "I'm fixing my hair in an old mirror in the break room when I hear Joy approach."
        
        show joy at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300   

        joy "\"Aya! The boys told me someone was here for me, it's good to see you.\""

        a excited "\"It's good to see you too! I left you a note, there's peach cobbler in the fridge for you. Not too sweet.\""

        joy "\"That's awful kind of you, thanks for thinking of me. I'll be sure to bring it home with me tonight.\""

        a happy "\"Putting in a full work day?\""

        joy "\"The work never stops! And we're getting ready for picking season. How's the bookstore?\""

        a sad "\"Not so good, at least not lately. Having a hard time getting customers.\""

        joy "\"Sorry to hear that, have you thought about doing more social media marketing?\""

        a excited "\"Joy, you sound like such a youngster when you say stuff like that. But you know I'm not as tech-savvy as you. And I don't know how well would work for a bookstore...\""

        joy "\"Ah, sorry, Aya. I didn't mean to go straight into giving you unsolicited advice. Let me know if there's anything I can do to help, okay? And take care of yourself, honey. You focus too much on work.\""

        "She takes my hand and pats it comfortingly."

        a happy "\"I'll take care of myself. You eat that cobbler, okay? And give me notes!\""

        scene brown with irisin
        stop music fadeout 3.0
        pause 3.0
        scene bg bookstore with dissolve
        play music bookstore_sunshine

        # title where it's "back at the bookstore"

        "(I should call her.)"

        "I stare at the broken lightbulb in the dustbin."

        "I dial the number I had saved to my contacts after Erin left the shop that day."

        "It rings once... twice..."

        e neutral "\"*click* Hello?\""

        "(She answered!!)"

        "(What do I say?! I didn't think this through!)"

    menu:
        "Hey, this is Aya":
            jump cobbler_call_aya

        "Uhhhhh":
            jump cobbler_call_uhh

        "(Say nothing)":
            jump cobbler_call_nothing

    label cobbler_call_aya:
        $ milk_carton = True
        e excited "\"The bookstore fox!\""

        a tsuntsun "\"Fox {i}spirit{/i}, thank you.\""

        e "\"I'm so glad you called so I have your number, I saw this cat today and wanted so badly to send you a picture of it!\""

        a happy "\"Oh, sure! I'd like that.\""

        e "\"One sec,\""

        "A faint rustle emits from the phone as Erin finds the photo and sends it to me."

        show kitty day with dissolve
        "*ding*"

        "It\'s adorable. A little grey cat, barely more than a kitten, is napping in a milk carton lit by a perfect sunbeam."

        a excited "\"This is so cute! Where did you take this?\""

        if cobblerfirst == True:
            e rizzler "\"Trade secret, I\'m afraid!\""

            a neutral "\"For what trade?\""

            e "\"It\'s a secret I\'ll trade for a kiss!\""

            a blush "\"A kiss, huh? Now, how will I do that if I don\'t know where you are?\""

            "Erin giggles, the sound partly clipped by the phone\'s mic."

            e blush "\"I suppose you have a point. Darn.\""

        if cornerstorefirst == True:
            e excited "\"At work!\""

            a happy "\"Makes sense!\""

        hide kitty day with dissolve
        e happy "\"So, was there a reason you called me?\""


        menu:
            "\"I wanted to know if you're staying in town...\"":
                $ kind_points += 1
                jump cobbler_erin_stayed

            "(Lie) \"I didn\'t really have a reason.\"":
                jump cobbler_erin_no_reason


    label cobbler_erin_stayed:

        a neutral "\"...or if you're going back to the city.\""

        e neutral "\"Oh, you think I\'m a city kid, huh?\""

        a "\"Aren\'t you?\""

        e happy "\"I hate it there! I decided to stick around, so I\'m still out here. I\'m sure we\'ll run into each other again soon.\""
        
        if cobblerfirst == True:        
            e happy "\"You'll just have to figure out where I'm spending my time.\""

        if cornerstorefirst == True:
            e happy "\"I'll be at the cornerstore a lot of the time, truth be told.\""

        e "\"Anyway, I gotta go! I\'ll text you later, bye!\""

        "*click*"

        "Okay, that was {i}definitely{/i} flirting, right?"

        scene brown with dissolve
        jump cobbler_end


    label cobbler_erin_no_reason:

        e excited "\"Oh, okay! Well I\'m glad to hear from you anyway!\""

        e blush "\"Would you... like to get coffee sometime?\""

        a neutral "\"I\'m more of a tea drinker.\""

        "She sounds a little deflated when she responds."

        e gloom "\"Right, of course. That\'s alright. Well... I gotta get going, I\'ll text you later! Bye!\""

        "Wait... wait. WAIT. Was she asking me out?"

        scene brown with dissolve
        jump cobbler_end





    label cobbler_call_uhh:

        a blush "\"I...\""

        e neutral "\"Who is this?\""

        "I clear my throat."

        a neutral "\"This is Aya.\""

        jump cobbler_call_aya



    label cobbler_call_nothing:

        e sad "\"Another spam caller??? Stop calling me!\""

        "Well, that didn't go the way I thought it would. Not sure what I was expecting..."

        scene brown with dissolve
        jump cobbler_end



    label lydia_chat:

        scene brown
        show bg market with dissolve

        "Lydia is a cat spirit who tends a large garden near the post office. She has a little cottage that's perfect for just her, and she likes living alone."

        "In fact, she thrives by spending her time humming to budding flowers and sprouting vegetables, taking naps in her sun chair, and just being outside in general. But not in a sporty way, she's just kind of an outside cat."

        "I try to catch up with her regularly, but I'm a bit more of an indoorsy spirit. Still, it's good to have other spirits as friends nearby, especially at a time like this."

        "She might have a spell to fix broken lamps, which would save me a lot of time and effort."

        "I swing open the garden gate and look for her."

        "I find her weeding a garden box of catnip, looking blissed as all hell. She has a small, curvaceous figure and wears a painter's jumpsuit with thick yellow gardening gloves."
        
        show lydia at right, lydia_size
        
        "Her thick, calico colored hair is pulled back into a low ponytail, and a broad straw sunhat shades her head and shoulders. Holes are cut into the hat to leave room for her ears. Her spotted tail is adorned with a blue ribbon and a little gold bell that jingles lighty as her tail swings back and forth."

        "Lydia always looks like she's no older than 40, but I know she's much, much older. Spirits age slowly."

        a happy "\"I hope I'm not interrupting!\""

        "My tone is warm, and as I speak I sway my picnic basket in front of me."

        lyd "\"What have you brought me this time? I hope it isn't more pickles. You know how I hate pickles.\""

        a "\"Well, I know that now. I didn't know at the time! It was supposed to be a surprise.\""

        lyd "\"Surprise? More like jumpscare. Come on in, let's see what you have.\""

        "She peels off her gloves and tucks the heels of them into the back pocket of her jumpsuit."

        scene brown
        show bg lydias with dissolve
        show lydia at right, lydia_size

        "Inside the cottage, Lydia puts on a kettle of tea and pulls out two handcrafted glazed mugs. We scoop the cobbler into a ceramic pot and put it into the oven to heat."

        "I don't say anything. Lydia likes to take her time and bristles if she's rushed."

        "The teapot whistles. She pours tea: spearmint for her and Earl Grey for me. The cobbler is hot and ready after another twenty minutes of quiet contemplation."

        "As we begin to eat, she finally asks me the reason for my visit."

        a excited "\"I simply wanted to share this with you. I thought you'd enjoy it.\""

        "She gives me a look from below lowered lashes."

        lyd "\"And that's all?\""

        a blush "\"Well... there is something, actually.\""

        "I explain that I'm looking for a spell that fixes a broken lamp, and tell her about Erin and the pact she made with me."

        lyd "\"Ah, a human girl... tell me more about her.\""
        hide lydia with dissolve

label tell_lydia_about_erin:

    menu:
        "She was clumsy" if picked_clumsy == False:
            $ picked_clumsy = True
            jump shes_clumsy

        "She was bold":
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
            jump shes_bold

        "She was cute":
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
            jump shes_cute

        "(Change the subject)":
            jump lydia_change_subject

    label shes_clumsy:
        show lydia at right, lydia_size
        lyd "\"Well, obviously.\""

        lyd "\"Is that all?\""
        hide lydia with dissolve
        jump tell_lydia_about_erin


    label shes_bold:
        show lydia at right, lydia_size
        a blush "\"I liked her. The way she was so resolved to pay me back was charming. And she was so bold when she left.\""

        lyd "\"How so?\""

        a tsuntsun "\"She called me beautiful. Out of the blue!\""

        lyd "\"Aya, that's adorable!\""

        a sad "\"It was probably just a compliment and not actual flirting, right?\""

        lyd "\"But what if it WAS flirting? And you liked her. So you should give her a chance and see where it goes.\""

        a "\"I don't want to assume that and get hurt, you know? It's been hard since mom and dad left. You know I haven't dated anyone since then. Plus, she's younger than me\""

        lyd "\"I get where you're coming from, but you need to live a little. Have a little summer romance. It'll be fine, it'll be fun! And don't talk to me about age, you're both youngsters. You don't know how annoying age gap problems can be when you get to be 300 instead of 30.\""

        if cobblerfirst == True:
            a neutral "\"Right, sorry. Well, I haven't seen her again since then. She could have bailed and gone back home.\""

            lyd "\"You two made a pact, though. If she's so {i}bold{/i}, she'll show up.\""

        else:
            a neutral "\"That's fair. I guess I did see her at the cornerstore...\""
            
            lyd "\"See? She's staying!\""

        "Lydia primly sips her tea. I know she's probably right, but I just don't know..."

        "I guess I'll just have to see what happens if I run into her."
        
        hide lydia with dissolve

        jump cobbler_end


    label shes_cute:
        show lydia at right, lydia_size
        a blush "\"Really cute. Clumsy and cute.\""

        lyd "\"Oh my, does little Aya have a crush?\""

        a tsuntsun "\"I don't really have time for a crush...\""

        "Lydia snorts."

        lyd "\"All you have is time. You're just moldering away among those books. You're a cute girl, Aya, and you'd be extra cute with a cutie by your side.\""

        a excited "\"Lyd!! I barely know her!\""

        lyd "\"Just saying!\""

        "I grumble something into my teacup and she pretends to not hear me, ears swiveled away."
        hide lydia with dissolve
        jump cobbler_end


    label lydia_change_subject:
        show lydia at right, lydia_size
        "I don't really want to talk about Erin..."

        a tsuntsun "\"She's just some girl, I don't have much to say about her.\""

        "Which is more or less true. I don't like the way Lydia looks at me, though. She's got this \"knowing old woman\" expression that looks out of place on her unlined face."
        
        hide lydia with dissolve

        jump cobbler_end



    label cobbler_end:
        if cobblerfirst:
            scene brown with dissolve
            pause 1.5
            "It's been a big day. I'll go to the cornerstore tomorrow."

            scene brown with dissolve
            pause 3.0  
            jump cornerstore

        else:
            if cornerstorefirst:
                "What a weekend. It was good, but I'm so tired... at least the bookstore will be quiet this week!"
                scene brown with dissolve
                pause 3.0
                jump farmers_market


    label cornerstore:
        stop sound fadeout 2.0
        "The cornerstore is on the far side of town but it's a nice day, so I leave my bike behind and equip myself with a couple of sturdy tote bags."
        
        "It's been a couple weeks since I've gone, so I'll probably grab a bunch of snacks and drinks to supplement the usual groceries."

        "Some little birds peck at scattered seeds and tiny crumbs on the sidewalk. The little fellows hop out of the way when I walk past."

        if milk_carton == True:
            "Outside the cornerstore I see a stack of familiar blue milk cartons."
            a excited "\"No way.\""
            "I guess this is where she's been... closer than I thought!"
            pause 2.0

        stop music fadeout 1.0
        show bg cornerstore with dissolve
        play music cornerstore

        "I nod at a couple I recognize in the cornerstore. I don't know them by name, but I know they're locals. We've been nodding at each other for years."

        e neutral "\"Aya? Is that you?\""

        show erin happy at center, erin_size with dissolve

        "She's here. Like a breath of fresh air."

        a shocked "\"Oh! Erin!\""

        "I take in her apron and the box of candies she's holding tucked under one arm."

        a "\"So this is where you've been?\""

        hide erin with dissolve

        e happy "\"Mostly! Doing jobs here and there. I'm renting a room from the owner.\""

        a neutral "\"Cindy, right? She's very sweet. I'm glad you found a place to stay, but why aren't you back home?\""

        e excited "\"I wasn't ready to go back yet. Besides... I still gotta help you find that spell, right?\""

        "Right... but that's not for another month. I thought she'd just come back when it's time, but I guess not."

        a happy "\"Ah, well... it's good to see you. I hope you've been well?\""

        "She steps past me and starts to unpack the box, restocking the shelf."

        "She's close enough that the light scent of citrus and apples wafts from her hair. It's a very bright and happy scent that suits her."

        e rizzler "\"I have! So, you doing some shopping today? Or did you just come here to find me?\""

        a tsuntsun "\"I didn't know where to find you, really.\""
        
        a happy "\"Just here to pick some things up that I missed at the grocer.\""

        e happy "\"Nice! What are you doing later? I'm here 'til 7, but not busy tonight. We could hang out!\""

        "This seems like a hint. I'm not doing anything, but I want to keep to myself this weekend and recharge..."

        menu:
            "\"Having some downtime to myself tonight.\"":
                jump cornerstore_downtime
            
            "(Lie.) \"Magic stuff. Spirit things.\"":
                jump cornerstore_lie


    label cornerstore_downtime:
        a sad "\"So I'll be busy, sorry.\""

        "She tucks a loose strand of hair behind her ear and smiles up at me from where she squats next to a shelf."

        e excited "\"That's alright! Another time, then.\""

        jump cornerstore_cont

    label cornerstore_lie:

        "Erin nods sagely and smiles guilelessly up at me from where she squats next to a shelf."

        e happy "\"That sounds important, I don't want to intrude on that.\""

        "I feel a little bad for the lie."
        
        jump cornerstore_cont

    label cornerstore_cont:

        e excited "\"Well, I don't want to keep you from your shopping! You know where to find me now, so don't be a stranger, okay?\""

        e blush "\"I could come visit your bookstore after work!\""

        a blush "\"No! I mean, we'll be closed, sorry.\""

        "She nods and makes a wry smirk, but focuses on shelving the candies."

        a happy "\"Catch you later, Erin.\""

        "The rest of my shopping goes by quickly, though I do steal a few glances of Erin busying herself around the shop. She was certainly quite clumsy at my shop, but it looks like she's doing good work here."
        
        "Time to head home."
        window hide
        scene brown with dissolve
        jump cornerstore_end
        

    label cornerstore_end:

        if cornerstorefirst:     
            "I unpack the groceries and make myself a cold lemonade."
            "I think I'll chill for the rest of today and make cobbler tomorrow."
            scene brown with dissolve
            jump cobbler

        else:
            if cobblerfirst:
                "I unpack the groceries and make myself a cold lemonade."
                "What a weekend. It was good, but I'm so tired... at least the bookstore will be quiet this week!"
                scene brown with dissolve
                jump farmers_market


