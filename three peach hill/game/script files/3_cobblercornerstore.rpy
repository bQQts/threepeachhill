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
        "You have two goals today. Which will you do first?"

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

        "Fortunately, the peaches had sustained no damage at all during The Incident and you're able to whip up a couple of test cobblers."

        "The local peaches aren't quite in season yet. These are early bloomers that your friend Joy at the orchard had set aside for you."

        "The cobblers aren't bad. They're not as sweet as you had hoped they'd be, but that makes sense since peach season starts next month. You wish you had accounted for the difference and adjusted your recipe, but this is good practice for the real thing!"

        "You divide the cobblers into plastic food storage bins, packing some into a small picnic basket and the rest into the fridge. Some of my older friends will probably love this."

        menu:
            "Baking went quickly and you have some time to kill, which friend do you want to share some pie with?"

            "The wholesome old orchardist":
                jump orchardist

            "The gossipy old cat spirit":
                jump lydia_chat

    label orchardist:
        "Joy has been an ever-present friend for most of your life. She's been running the orchard for as long as you can remember and is probably in her 60s now."

        "You run into each other now and then, but you see each other most on social media. She's a much more active poster than you are and the extra marketing has been helpful for her orchard. People come from all over to pick peaches from Three Peach Hill."

        a excited "(It's nearly time for peach picking to open up, but not quite yet!)"

        "Since she spends all her time managing the business, she doesn't tend to do a lot of baking. You try to bring her things once in a while to check in."

        "You bike to her office, a small two-story building at the very foot of the orchard's hills. Wind chimes hang from the stoop, and the sign on the door says OPEN. The door jingles as you push it open and step inside. You're greated by your neighbor Timothy and his very good friend."
        
        scene brown with dissolve
        show bg orchard with dissolve

        pause 0.5

        show timothy at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300

        timothy "\"Well if it isn't our resident bookworm! You looking for Joy, by any chance?\""

        a excited "\"Hey! Sure am.\""

        timothy "\"She's out in the trees today.\""

        a happy "\"Oh! No problem, I'll just drop this off upstairs.\""

        hide timothy with dissolve

        "The gentlemen wave in acknowledgement. You haul your cobbler-laden picnic basket to the second floor."

        "This orchard front house is cozy, very modern for a historic administrative building. Joy turned the downstairs into a social space with couches, bar counters, and plenty of plants so visitors and farmers alike have a place to relax out of the sun."

        "The modern space is in stark contrast to the must and dust of the upstairs, which largely resembles an attic. It's where the real business happens."

        "Joy's cluttered desk has a notepad, so you jot down a note mentioning the cobbler and place it atop her keyboard. The cobbler goes right into the fridge."

        "You're fixing your hair in an old mirror on the wall when your sensitive ears hear Joy's soft footsteps as she climbs the stair steps."
        
        show joy at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300   

        joy "\"Aya! The boys told me someone was here for me, it's good to see you. Did you like those peaches?\""

        a excited "\"It's good to see you too, ma'am! Yes, I turned it into cobbler! There's some in the fridge for you. Not too sweet.\""

        joy "\"That's awful kind of you, dearie. You're always so thoughtful. I'll be sure to bring it home for a midnight snack.\""

        a happy "\"Putting in a full work day?\""

        joy "\"The work never stops! And we're getting ready for real picking season. How's the bookstore?\""

        a sad "\"Not so good, at least not lately. Having a hard time getting customers.\""

        joy "\"Ah! Have you thought about doing more social media marketing?\""

        a excited "\"Joy, you sound like such a youngster when you say stuff like that. But you know I'm not as tech-savvy as you. And I don't know how well it would work for a bookstore... But I have time! No need for a solution today, ha!\""

        joy "\"I must apologize, I didn't mean to go straight into giving you unsolicited advice. Let me know if there's anything I can do to help, okay? And take care of yourself, honey. You focus too much on work for a fox in the prime of her life!\""

        "She takes your hand and pats it comfortingly."

        "You chuckle ruefully."

        a happy "\"I'll take care of myself. You eat that cobbler, okay? And give me notes!\""

        scene brown with irisin
        stop music fadeout 3.0
        pause 3.0
        scene bg bookstore with dissolve
        play music bookstore_sunshine

        # title where it's "back at the bookstore"

        "You stare at the broken lightbulb in the dustbin."

        a neutral "(Joy's right... I should call her.)"

        "You dial the number you saved to your contacts after Erin left the shop that day."

        # add dial tone sound
        "It rings once... twice..."

        e neutral "\"*click* Hello?\""

        "(She answered!!)"

        a tsuntsun "(What do I say?! I didn't think this through!)"

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

        a tsuntsun "\"Well, fox {i}spirit{/i}. But yeah, it's me~\""

        e "\"I'm so glad you called so I have your number, I saw this cat outside just now and wanted so badly to send you a picture of it!\""

        a happy "\"Oh, sure! I'd like that.\""

        e "\"One sec,\""

        "A faint rustle emits from the phone as Erin finds the photo and sends it."

        show kitty day with dissolve
        "*ding*"

        "It\'s adorable. A little grey cat, barely more than a kitten, is napping in a milk carton lit by a perfect sunbeam."

        a excited "\"This is so cute! Where did you take this?\""

        if cobblerfirst == True:
            e rizzler "\"Trade secret, I\'m afraid!\""

            a neutral "\"Trade secret?\""

            e "\"Yeees, in that it\'s a secret I\'ll trade for a kiss!\""

            a blush "\"A kiss, huh? Now, how will I do that if I don\'t know where you are?\""

            "Erin giggles, the sound partly clipped by the phone\'s mic."

            e blush "\"I suppose you have a point. Darn.\""

        if cornerstorefirst == True:
            e excited "\"I'm at work!\""

            a happy "\"Oh! Wonderful!\""

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

        a "\"Well, aren\'t you?\""

        e happy "\"I hate it there! I decided to stick around these parts a while longer. I\'m sure we\'ll run into each other again soon.\""
        
        if cobblerfirst == True:        
            e happy "\"You'll just have to figure out where I'm spending my time.\""

        if cornerstorefirst == True:
            e happy "\"I'll be at the cornerstore a lot of the time, truth be told.\""

        e "\"Anyway, I gotta go! I\'ll text you later, bye!\""

        "*click*"

        "That was {i}definitely{/i} flirting... right?"

        scene brown with dissolve
        jump cobbler_end


    label cobbler_erin_no_reason:

        e excited "\"Oh, okay! Well I\'m glad to hear from you anyway!\""

        e blush "\"Would you... like to get coffee sometime?\""

        a neutral "\"I\'m more of a tea drinker.\""

        "She sounds a little deflated when she responds."

        e gloom "\"Right, of course. That\'s alright. Well... I gotta get going, I\'ll text you later! Bye!\""

        "*click*"

        "You wonder at the strange lilt of disappointment in her voice. What just happened?"

        scene brown with dissolve
        jump cobbler_end





    label cobbler_call_uhh:

        a blush "\"I...\""

        e neutral "\"Who is this?\""

        "I clear my throat."

        a neutral "\"This is Aya.\""

        jump cobbler_call_aya



    label cobbler_call_nothing:

        e sad "\"Helloooo? Another spam caller??? Hmph!\""

        "*click*"

        "Well, that didn't go the way you thought it would. Though you're not sure what reaction you were expecting..."

        scene brown with dissolve
        jump cobbler_end



    label lydia_chat:

        scene brown
        show bg market with dissolve

        "Lydia is a sassy old calico who tends a large garden near the post office. Her little cottage is the perfect size for her to sprawl out and enjoy her solitude."

        "But Lydia is no hermit. She revels in spending her time humming to budding flowers and sprouting vegetables, taking naps in her sun chair, and just being outside in general. And more than anything else, Lydia looooves gossip."
b
        "You try to catch up with her regularly; it's good to have other spirits as friends nearby, especially at times where you need some magical help."

        "She might have a spell to fix broken lamps, which would save you a lot of time and effort."

        "You push open the wooden garden gate and listen for the sound of her voice."

        "You find her weeding a garden box of catnip, looking way beyond blissed-out. A painter's jumpsuit flatters her small, curvaceous figure, and thick yellow gardening gloves protect her paws from the weeds."
        
        show lydia at right, lydia_size
        
        "Her thick hair is pulled back into a low ponytail, and a broad straw sunhat shades her head and shoulders. Holes are cut into the hat to leave room for her ears. Her spotted tail is adorned with a blue ribbon and a little gold bell that jingles lighty as her tail swings back and forth."

        "Lydia always looks like she's no older than 40, but she's much, much older. Spirits age slowly."

        a happy "\"I hope I'm not interrupting...\""

        "You sway your picnic basket tantalizingly."

        a happy "\"...but I did bring a treat to make my surprise appearance worth your time!\""

        lyd "\"What have you brought me this time? I hope it isn't more cucumber salad. You know how I hate cucumber.\""

        a "\"Well, I know that now. I didn't know at the time! It was supposed to be a surprise.\""

        lyd "\"Surprise? More like jumpscare. Come on in, let's see what you have.\""

        "She peels off her gloves and tucks the heels of them into the back pocket of her jumpsuit."

        scene brown
        show bg lydias with dissolve
        show lydia at right, lydia_size

        "Inside the cottage, Lydia puts on a kettle of tea and selects two handcrafted glazed mugs. She scoops the cobbler into a ceramic pot and put it in the oven to heat."

        "You don't say anything, not yet. Lydia likes to take her time and bristles if she's rushed."

        "The teapot whistles. She pours tea: spearmint for her and Earl Grey for you. The cobbler is hot and ready after another twenty minutes of quiet contemplation."

        "As you begin to eat, she finally asks for the reason for your visit."

        a excited "\"I simply wanted to share this with you. I thought you'd enjoy it.\""

        "She gives you a disbelieving look from below lowered lashes."

        lyd "\"And that's all?\""

        a blush "\"Well... there is something, actually.\""

        "You explain that you're looking for a spell that fixes a broken lamp. You describe Erin and the pact she made with you."

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

        a tsuntsun "\"She called me gorgeous!\""

        lyd "\"Aya, that's adorable!\""

        a sad "\"It was probably just a compliment and not actual flirting, right?\""

        lyd "\"But what if it WAS flirting? And you liked her. So you should give her a chance and see where it goes.\""

        a "\"I don't want to assume that and get hurt, you know? It's been hard since mom and dad left. You know I haven't dated anyone since then. Plus, she's younger than me...\""

        lyd "\"I get where you're coming from, but you need to live a little. Have a little summer romance. It'll be fine, it'll be fun! And don't talk to me about age, you're both youngsters. You don't know how annoying age gap problems can be when you get to be 300 instead of 30.\""

        if cobblerfirst == True:
            a neutral "\"Right, sorry. Well, I haven't seen her again since then. She could have bailed and gone back home.\""

            lyd "\"You two made a pact, though. If she's so {i}bold{/i}, she'll show up.\""

        else:
            a neutral "\"That's fair. I guess I did see her at the cornerstore...\""
            
            lyd "\"See? She's staying!\""

        "Lydia primly sips her tea. You know she's probably right, but..."

        "You'll have to see what happens."
        
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

        "You grumble something rude into your teacup and she pretends to not hear, ears swiveled away."
        hide lydia with dissolve
        jump cobbler_end


    label lydia_change_subject:
        show lydia at right, lydia_size
        "You don't really want to talk about Erin..."

        a tsuntsun "\"She's just some girl, I don't have much to say about her.\""

        "Which is more or less true. Lydia gives you a dirty look. She's got this \"knowing old woman\" expression that looks out of place on her unlined face."
        
        lyd "\"Fine, keep your secrets.\""
        hide lydia with dissolve

        jump cobbler_end



    label cobbler_end:
        if cobblerfirst:
            scene brown with dissolve
            pause 1.5
            "It's been a big day. You'll go to the cornerstore tomorrow."

            scene brown with dissolve
            pause 3.0  
            jump cornerstore

        else:
            if cornerstorefirst:
                "What a weekend. It was good, but you're so tired... at least the bookstore will be quiet this week!"
                scene brown with dissolve
                pause 3.0
                jump farmers_market


    label cornerstore:
        stop sound fadeout 2.0
        "The cornerstore is mile away but it's a nice day, so you leave your bike behind and equip yourself with a couple of sturdy tote bags."
        
        "It's been a couple weeks since you've gone, so you're off to grab a bunch of snacks to supplement the usual groceries."

        "Little birds peck at scattered seeds and tiny crumbs on the sidewalk. The little fellows hop out of the way when you walk past."

        if milk_carton == True:
            "Outside the cornerstore you see a stack of familiar blue milk cartons."
            a excited "\"No way.\""
            "Looks like this is where she's been... closer than you thought!"
            pause 2.0

        stop music fadeout 1.0
        show bg cornerstore with dissolve
        play music cornerstore

        "You walk the aisles, picking treats off shelves. Your neighbor Timothy gives you a nod as he walks past you with a canvas tote bag over his shoulder. You nod back." 
        
        "Whenever you run into each other here he's always picking up an unbelievable quantity of whipped cream. You're sure that's what he got today, too."

        "He must really love the stuff."

        e neutral "\"Aya? Is that you?\""

        show erin happy at center, erin_size with dissolve

        "She's here. Like a breath of fresh air."

        a shocked "\"Erin!\""

        "You take in her apron and the box of candies she's holding tucked under one arm."

        a "\"So this is where you've been! You're... working here? How'd you get a job so fast?\""

        hide erin with dissolve

        e happy "\"Oh, I'm doing jobs here and there around town. But I'm renting a room from this store's owner.\""

        a neutral "\"Cindy, right? She's very sweet. I'm glad you found a place to stay, but why aren't you back home?\""

        e excited "\"I wasn't ready to go back yet. Besides... I still gotta help you find that spell, right?\""

        "Right... but that's not for another month. You thought she'd just come back when it's time, but apparently not."

        a happy "\"Ah, well... it's good to see you. I hope you've been well?\""

        "She steps past you and starts to unpack the box, restocking the shelf."

        "She's close enough that the light scent of citrus and apples wafts from her hair. It's a very bright and happy scent... it suits her."

        e rizzler "\"I have! So, you doing some shopping today? Or did you just come here to find me?\""

        a tsuntsun "\"I didn't know where to find you, really.\""
        
        a happy "\"Just here to pick some things up that I missed at the grocer.\""

        e happy "\"I'm glad our paths crossed, then! What are you doing later? I'm here 'til 7, but not busy tonight. We could hang out!\""

        "This seems like a hint. You're not doing anything, but you want to keep to yourself this weekend and recharge..."

        menu:
            "\"Having some downtime to myself tonight.\"":
                jump cornerstore_downtime
            
            "(Lie.) \"Magic stuff. Spirit things.\"":
                jump cornerstore_lie


    label cornerstore_downtime:
        a sad "\"So I'll be busy, sorry.\""

        "Erin tucks a loose strand of hair behind her ear and smiles up at you from where she squats next to a shelf."

        e excited "\"That's alright! Another time, then.\""

        jump cornerstore_cont

    label cornerstore_lie:

        "Erin nods sagely and smiles guilelessly up at me from where she squats next to a shelf."

        e happy "\"That sounds important, I don't want to intrude on that.\""

        "You feel a little bad for the lie."
        
        jump cornerstore_cont

    label cornerstore_cont:

        e excited "\"Well, I don't want to keep you from your shopping! You know where to find me now, so don't be a stranger, okay?\""

        e blush "\"I could come visit your bookstore after work!\""

        a blush "\"No! I mean, we'll be closed, sorry.\""

        "She nods and makes a wry smirk, but focuses on shelving the candies."

        a happy "\"Catch you later, Erin.\""

        "The rest of the shopping goes by quickly, though you do steal a few glances of Erin busying herself around the shop. She was certainly quite clumsy at your bookstore, but it looks like she's doing good work here."
        
        "Time to head home."
        window hide
        scene brown with dissolve
        jump cornerstore_end
        

    label cornerstore_end:

        if cornerstorefirst:     
            "You unpack the groceries and make yourself a cold lemonade."
            "You'll chill for the rest of today and make cobbler tomorrow."
            scene brown with dissolve
            jump cobbler

        else:
            if cobblerfirst:
                "You unpack the groceries and make myself a cold lemonade."
                "What a weekend. It was good, but you're so tired... at least the bookstore will be quiet this week!"
                scene brown with dissolve
                jump farmers_market


