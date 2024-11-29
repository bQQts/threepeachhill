label pursuit:
    scene black with dissolve
    stop music fadeout 1.5
    play music "music/Quiet Village.flac" fadein 1.5

    # July 20

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

    "It's nearly time for peach picking to open up, but not quite yet!"

    "Since she spends all her time managing the business, she doesn't tend to do a lot of baking. I try to bring her things once in a while to check in."

    "I take my bike to her office, which is a small two-story building at the very foot of the orchard's hills. Wind chimes hang from the stoop, and the sign on the door says OPEN. When I swing the door open and step inside, I'm greeted by a couple of my neighbors sipping coffee in the lobby."
    
    scene black with dissolve
    show bg orchard with dissolve

    timothy "\"Well hey there! You lookin' for Joy, by any chance?\""

    a excited "\"Hey! Sure am.\""

    timothy "\"She's out in the trees today.\""

    a happy "\"Oh! No problem, I'll just drop this off upstairs.\""

    "The gentlemen wave in acknowledgement, and I take the stairs to the second floor, where the actual offices and the break room await my cobbler-laden picnic basket."

    "I borrow a sticky note from Joy's desk and jot down a note mentioning the cobbler, then put the cobbler in the break room fridge."

    "It's cozy, very lived-in for an administrative building. Joy's turned the downstairs into a social space with couches, bar counters, and plenty of plants so visitors and farmers alike have a place to relax out of the sun."

    "Upstairs, however, has the must and dust of decades of unchanging use. It's where the real business happens."

    "I'm fixing my hair in an old mirror in the break room when I hear Joy approach."

    joy "\"Aya! The boys told me someone was here for me, it's good to see you.\""

    a excited "\"It's good to see you too! I left you a note, there's peach cobbler in the fridge for you. Not too sweet.\""

    joy "\"That's awful kind of you, thanks for thinking of me. I'll be sure to bring it home with me tonight.\""

    a happy "\"Putting in a full work day?\""

    joy "\"The work never stops! And we're getting ready for picking season. How's the bookstore?\""

    a sad "\"Not so good, at least not lately. Having a hard time getting customers.\""

    joy "\"Sorry to hear that, have you thought about doing more social media marketing?\""

    a excited "\"Joy, you sound like such a youngster when you say stuff like that. But you know I'm not tech-savvy like that. And I don't know how that would work for a bookstore...\""

    joy "\"Ah, sorry, didn't mean to go straight into solutions-mode. Let me know if there's anything I can do to help, okay? And take care of yourself, honey. You focus too much on work.\""

    "She takes my hand and pats it comfortingly."

    a happy "\"I'll take care of myself. You eat that cobbler, okay? And give me notes!\""

    scene black with irisin
    pause 2.0
    scene bg bookstore with dissolve

    # title where it's "back at the bookstore"

    "I should call her."

    "I stare at the broken lightbulb in the dustbin."

    "I dial the number I had saved to my contacts after Erin left the shop that day."

    "It rings once... twice..."

    e neutral "\"*click* Hello?\""

    "She answered!!"

    "What do I say?! I didn't think this through!"

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

    "*ding*"

    "It\'s adorable. A little grey cat, barely more than a kitten, is napping in a milk carton lit by a perfect sunbeam."

    a excited "\"This is so cute! Where did you take this?\""

    e rizzler "\"Trade secret, I\'m afraid!\""

    a neutral "\"For what trade?\""

    e "\"It\'s a secret I\'ll trade for a kiss!\""

    a blush "\"A kiss, huh? How will I do that if I don\'t know where you are?\""

    "Erin giggles, the sound partly clipped by the phone\'s mic."

    e blush "\"I suppose you have a point. Darn.\""

    e happy "\"Wait, was there a reason you called me?\""


    menu:
        "I wanted to know if you stayed in town...":
            $ kind_points += 1
            jump cobbler_erin_stayed

        "I didn\'t really have a reason":
            jump cobbler_erin_no_reason


label cobbler_erin_stayed:

    a neutral "\"...or if you had gone back to the city.\""

    e neutral "\"Oh, you think I\'m a city kid, huh?\""

    a "\"Aren\'t you?\""

    e happy "\"I hate it there! I\'m still out here. I\'m sure we\'ll run into each other soon. You'll just have to figure out where I'm spending my time.\""

    e "\"Anyway, I gotta go! I\'ll text you later, bye!\""

    "*click*"

    "Okay, that was {i}definitely{/i} flirting, right?"

    scene black with irisin
    jump cobbler_end


label cobbler_erin_no_reason:

    e excited "\"Oh, okay! Well I\'m glad to hear from you anyway!\""

    e blush "\"Would you... like to get coffee sometime?\""

    a neutral "\"I\'m more of a tea drinker.\""

    "She sounds a little deflated when she responds."

    e gloom "\"Right, of course, that\'s alright. Well... I gotta get going, I\'ll text you later! Bye!\""

    "Wait... wait. Wait. Was she asking me out? WAIT."

    scene black with irisin
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

    scene black with dissolve
    jump cobbler_end



label lydia_chat:

    scene black
    show bg market with dissolve

    "Lydia is a cat spirit who tends a large garden near the post office. She has a little cottage that's perfect for just her, and she likes living alone."

    "In fact, she thrives by spending her time humming to budding flowers and sprouting vegetables, taking naps in her sun chair, and just being outside in general. But not in a sporty way, she's just kind of an outside cat."

    "I try to catch up with her regularly, but I'm a bit more of an indoorsy spirit. Still, it's good to have other spirits as friends nearby, especially at a time like this."

    "She might have a spell to fix broken lamps, which would save me a lot of time and effort."

    "I swing open the garden gate and look for her."

    "I find her weeding a garden box of catnip, looking blissed as all hell. She has a small, curvaceous figure and wears a painter's jumpsuit with thick yellow gardening gloves."

    "Her thick, calico colored hair is pulled back into a low ponytail, and a broad straw sunhat shades her head and shoulders. Holes are cut into the hat to leave room for her ears. Her spotted tail is adorned with a blue ribbon and a little gold bell that jingles lighty as her tail swings back and forth."

    "Lydia always looks like she's no older than 40, but I know she's much, much older. Spirits age slowly."

    a happy "\"I hope I'm not interrupting!\""

    "My tone is warm, and as I speak I sway my picnic basket in front of me."

    lyd "\"What have you brought me this time? I hope it isn't more pickles. You know how I hate pickles.\""

    a "\"Well, I know that now. I didn't know at the time! It was supposed to be a surprise.\""

    lyd "\"Surprise? More like jumpscare. Come on in, let's see what you have.\""

    "She peels off her gloves and tucks the heels of them into the back pocket of her jumpsuit."

    scene black
    show bg lydias with dissolve

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

label tell_lydia_about_erin:

menu:
    "She was clumsy" if picked_clumsy == False:
        $ picked_clumsy = True
        jump shes_clumsy

    "She was bold":
        $ kind_points += 1
        jump shes_bold

    "She was cute":
        $ kind_points += 1
        jump shes_cute

    "(Change the subject)":
        jump lydia_change_subject

label shes_clumsy:

    lyd "\"Well, obviously.\""

    lyd "\"Is that all?\""

    jump tell_lydia_about_erin


label shes_bold:

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
        a neutral "\"Right, sorry. I guess I did see her at the cornerstore...\""
        
        lyd "\"See? She's staying!\""

    "Lydia primly sips her tea. I know she's probably right, but I just don't know..."

    "I guess I'll just have to see what happens if I run into her."

    jump cobbler_end


label shes_cute:

    a blush "\"Really cute. Clumsy and cute.\""

    lyd "\"Oh my, does little Aya have a crush?\""

    a tsuntsun "\"I don't really have time for a crush...\""

    "Lydia snorts."

    lyd "\"All you have is time. You're just moldering away among those books. You're a cute girl, Aya, and you'd be extra cute with a cutie by your side.\""

    a excited "\"Lyd!! I barely know her!\""

    lyd "\"Just saying!\""

    "I grumble something into my teacup and she pretends to not hear me, ears swiveled away."

    jump cobbler_end


label lydia_change_subject:

    "I don't really want to talk about Erin..."

    a tsuntsun "\"She's just some girl, I don't have much to say about her.\""

    "Which is more or less true. I don't like the way Lydia looks at me, though. She's got this \"knowing old woman\" expression that looks out of place on her unlined face."

    jump cobbler_end



label cobbler_end:
    if cobblerfirst:
        "It's been a big day. I'll go to the cornerstore tomorrow."

        scene black with dissolve 
        jump cornerstore

    else:
        if cornerstorefirst:
            "What a weekend. It was good, but I'm so tired... at least the bookstore will be quiet this week!"
            scene black with dissolve
            jump farmers_market


label cornerstore:
    "The cornerstore is on the far side of town but it's a nice day, so I leave my bike behind and equip myself with a couple of sturdy tote bags."
    
    "It's been a couple weeks since I've gone, so I'll probably grab a bunch of snacks and drinks to supplement the usual groceries."

    "Some tiny birds peck at seeds and tiny crumbs scattered on the sidewalk, and the little fellows hop out of the way when I walk past."

    if milk_carton == True:
        "Outside the cornerstore I see a stack of familiar blue milk cartons."
        a "\"No way.\""
        "I guess this is where she's been... closer than I thought!"

    show bg cornerstore with dissolve

    "I nod at a couple people in the cornerstore. I don't know them by name, but I broadly recognize them as locals."

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

    "Right... in a month!"

    a happy "\"Ah, well... it's good to see you. I hope you've been well?\""

    "She steps past me and starts to unpack the box, restocking the shelf."

    "She stepped close enough that the scent of citrus and apples wafted from her hair. It's a very bright and happy scent, and it suits her."

    e rizzler "\"I have! So, you doing some shopping today? Or did you just come here to find me?\""

    a tsuntsun "\"I didn't know where to find you, really. Just here to pick some things up that I missed at the grocer.\""

    e happy "\"Nice! What are you doing after? I'm here 'til 7, but not busy after. We could hang out!\""

    "This seems like a hint. I'm not doing anything, but I want to keep to myself this weekend and recharge..."

    menu:
        "Having some downtime to myself tonight.":
            jump cornerstore_downtime
        
        "(Lie.) Magic stuff. Spirit things.":
            jump cornerstore_lie


label cornerstore_downtime:
    a sad "\"So I'll be busy, sorry.\""

    "She tucks a loose strand of hair behind her ear and smiles up at me from where she squats next to a shelf."

    e excited "\"That's alright! Another time, then.\""

    jump cornerstore_cont

label cornerstore_lie:

    "Erin nods sagely and smiles guilelessly up at me from where she squats next to a shelf."

    e happy "\"That sounds important, I don't want to intrude on that.\""

    "I feel a little bad for the lie. She really took that at face value."
    
    jump cornerstore_cont

label cornerstore_cont:

    e excited "\"Well, I don't want to keep you from your shopping! You know where to find me now, so don't be a stranger, okay?\""

    e blush "\"I could come visit your bookstore after work!\""

    a blush "\"No! I mean, we'll be closed, sorry.\""

    "She nods and makes a wry smirk, but focuses on shelving the candies."

    a happy "\"Catch you later, Erin.\""

    "The rest of my shopping goes by quickly, though I do steal a few glances of Erin busying herself around the shop. She was certainly quite clumsy at my shop, but it looks like she's doing good work here."

    jump cornerstore_end


label cornerstore_end:

    if cornerstorefirst:
        "It's been a big day. I'll make cobbler tomorrow."
        scene black with dissolve
        jump cobbler

    else:
        if cobblerfirst:
            "What a weekend. It was good, but I'm so tired... at least the bookstore will be quiet this week!"
            scene black with dissolve
            jump farmers_market


label farmers_market:
    # July 27
    # Introductory scene 
    # Screen that says a week passes
    # Farmers Market title screen
    show bg market with dissolve
    
    "The smell of food wafts across the town on a light breeze that carries away the remnants of summer's humidity."

    "As I walk down the street toward the town's central plaza, I hear the hum of small generators and the bustling of people a couple blocks away."

    "The farmers market is in full swing for harvest season."

    "There are vendors selling early peaches from Joy's orchard, while others sell the last of the season's blackberries. The usual veggie stands have a bounty of fresh treasures."
    
    "A honey merchant has paired up with a woodworker who's selling wooden wands and bread bowls to go with the honey."

    "There are rows of unique, handcrafted wares from merchants in the surrounding regions who've come to this town to peddle their wares at this farmers market."

    "There's even a fox spirit selling lucky talismans. They're real magic, though the workings are quite small; it's better not to swing the balance of things too far in any direction."

    "The first event of the season is always a big one."

    "I pick up some veggies, a cup of cold lemonade, and buy a loaf of bread from a baker who drove 3 hours to be here."

    "After a good lap around the produce side of the market, my bags are getting heavy. I head to a flower stand I've bought from in the past in search of marigold and sunflowers."

    "I hear her voice before I see her."

    e happy "\"Coming right up! Let me get those bagged for you.\""

    "A customer hands Erin a bouquet of daisies and she turns around to place it in a water-sealed paper bag."

    "She's smiling when she returns the bouquet to the customer, then sees me and waves."

    e excited "\"Aya! Are you here to get flowers??\""

    a happy "\"Yeah, but I'm still deciding what to get.\""

    e happy "\"I helped unload everything, I could probably give you some ideas! What would you think about this little bouquet of lavender and larkspur?\""

    menu:
        "Should I get my usual marigold and sunflowers, or go for the lavender and larkspur like Erin suggests?"

        "Marigold and sunflowers":
            jump farmers_market_marigold

        "Lavender and larkspur":
            $ kind_points += 1
            jump farmers_market_lavender

    label farmers_market_marigold:

        a "\"Thanks, but I think I'll get my usual. A bouquet each of marigold and sunflowers, please.\""

        e "\"Oooh how pretty! I love that, I'll bag those for you.\""

        jump farmers_market_cont

    label farmers_market_lavender:

        a "\"That's a good suggestion, I'll take the lavender and larkspur.\""

        "She beams at me and nearly bounces to fetch a bouquet of purple and blue sprigs."

        e blush "\"Here, this is my favorite one from this morning! Do you like it??\""

        a excited "\"I love it.\""

        jump farmers_market_cont

label farmers_market_cont:

    "Erin bags the flowers and waves over the flower merchant so I can pay for them."

    jeff "Oh, hello there Aya!"

    e neutral "\"You know Aya?\""

    jeff "\"Kiddo, you forget I've been selling here for ages. Aya's a long time customer, she tends to come by almost every weekend during the market season!\""

    e happy "\"Oh!\""

    "I chuckle at her blush."

    jeff "\"You know, Erin, if you'd like to call it a day here I'm sure Aya would be happy to show you around the rest of the market.\""

    "He winks at me on the sly."

    a neutral "\"Oh, Jeff, if you need the extra help I really don't want to pull her away, I was just stopping by to get flowers—\""

    jeff "\"Nonsense, we'll be just fine. She was a huge help unloading everything this morning, we can take it from here. Kiddo, let me pay you now so you have some change for the rest of the market.\""

    e excited "\"Really?! Thank you! This is great!!\""

    "She unties her apron and lays it over the back of a folding chair behind the sales table, slings her book bag over her shoulder, then comes around to join me."

    e happy "\"Will you show me around the market? I bet you know where all the good stuff is!\""

    a tsuntsun "\"I suppose...\""

    "Jeff comes back with an envelope for Erin."

    jeff "\"You two take care, now!\""

    a happy "\"Thank you, old man. Likewise!\""

    "I tuck the flowers into the larger of my tote bags and heft them so the straps rest more comfortably on my shoulders."

    "Erin notices the motion and offers a hand."

    e neutral "\"Let me carry your bags, okay? You must be tired from carrying them around all day.\""

    "I start to protest, but she insists, and I end up giving her the two smaller totes while I hang on to the largest one with the flowers."

    "We walk through the market, trying food samples and looking at crafts and jewelry."

    "After a while, Erin takes a detour to the restrooms and leaves the bags with me. I decide to look around a bit, and one booth catches my eye."

    "It's a table with hair pins of all different styles. I find a brass pin with a cast sunflower at the end of it, and it's perfect for me."
    
    "I almost finish my shopping there, but then I see that one pin is part wood and part resin-cast. The resin looks like it has frozen big rainbow bubbles in time."

    "I hesitate for a moment, then buy both pins."

    "I head back to the spot where Erin left, and I'm waiting there when she returns."

    "I shove the bubble hair pin towards her."

    e blush "\"What's this?\""

    a blush "\"It's a hair pin. For you.\""

    "Please don't make a big deal out of it."

    "Her eyes shine and she holds it to her chest."

    e "\"You didn't have to do that!\""

    a tsuntsun "\"It's just a hair pin, don't mention it.\""

    e excited "\"Well, thank you! It's so cute!!!\""

    "She tucks it away safely in her book bag and we continue walking around the market."

    jump lamp_talk

label lamp_talk:
    a sad "\"That lamp...\"" 

    "I trail off, lost in the memory for a moment. My throat feels tight, my chest heavy."

    e gloom "\"I'm sorry about that, I really am.\""

    "Erin picks at a ragged cuticle, her eyes downcast."

    a shocked "\"Oh, I'm not bringing it up for you to keep apologizing. No... I just felt like you should know why it was important to me. Important enough to make that pact, you know?\""

    "Erin looks at me directly, saying nothing. Just waiting, attentive and patient. Fully present with an intensity you don't see often."

    "I clear my throat a little and continue,"

    a neutral "\"It was my mom's. She made it when I was young enough that I could only see it from afar, to minimize the risk of me breaking it.\""

    if lamp_check == True:
        jump lamp_talk_apology
    else:
        jump lamp_cont

label lamp_talk_apology:
    a sad "\"I'm sorry I didn't check to see if you were okay first, that was shitty of me. It's just... it was another piece of her gone, just like that.\""

    jump lamp_cont

label lamp_cont:
    "Erin gently rests her free hand on my shoulder."

    e neutral "\"What happened to her? Sorry, I guess that's not really a polite question. You just sound so wistful, but not really sad?\""

    "The questioning lilt at the end of her sentence made the statement into a question of its own."

    "I smile a little at her concern and pat her hand, drawing it down from my shoulder and clasping it between us. Her soft hand is warm and a little bit tacky from the humid summer air."

    a neutral "\"One of her lovers was mortally wounded in an accident and had to return to The Other Side to recover, and she was so depressed about it.\""
    
    a "\"Dad encouraged her to go back to The Other Side to be with her lover, and when she eventually went, he went with her.\""

    e sad "\"Is that like... dying? Going to The Other Side?\""

    "I shake my head."

    a happy "\"No, it's more like... going to a faraway place that's hard to travel to, and harder to return from. They could come back, but time moves differently there.\""
    
    a neutral "\"Sometimes it goes faster, sometimes much slower. So they could show back up here at any time, really. Or it could be decades. There isn't a good way to know.\""

    "Erin tilts her head to the side, contemplating the new information."

    e neutral "\"Do you miss them?\""

    "I feel my eyes start to mist up and blink the tears back."

    a sad "\"I do. I can't wait to see them again, but I'm nowhere near ready to go to The Other Side myself. I'm enjoying this mortal life.\""

    "I realize I'm still holding her hand and loosen my grip as if to pull away, but she keeps holding on and gives my hand a little squeeze."
    
    "So, we're both aware of it. But neither of us is saying anything about it. And it's... nice. I suppose it isn't doing any harm."

    "I leave my hand in hers. We walk in silence, hand in hand, cicadas buzzing in the trees along the sidewalk."

    scene black with irisin
    jump going_home_from_market


label going_home_from_market:

    show bg gate with dissolve

    "Erin walks me home, still carrying my bags from the market."

    a happy "\"Thank you, today was really nice!\""

    e happy "\"It's no trouble, I'm glad I was able to give you a hand.\""

    "I invite her in, kicking off my shoes at the front door and stepping into a cozy pair of slippers instead. She pauses to slide out of her sneakers and carries the bags in, looking around."

    hide bg gate with dissolve
    stop music fadeout 1.5
    show bg kitchen with dissolve
    play music "Romance LoFi.flac" fadein 1.5

    a "\"Please, make yourself at home.\""

    "I go to the fridge."

    a neutral "\"Water? Beer? Tea?\""

    e excited "\"Beer sounds amazing! Thanks.\""

    a happy "\"Of course!\""

    "We sit in companionable silence for a little bit, nursing our drinks."

    e blush "\"I meant what I said that day, you know.\""

    a "\"Which day?\""

    e happy "\"When I said you're beautiful.\""

    a tsuntsun "\"O-oh! That day, right. Thank you. I'm flattered!\""

    "I hurriedly busy myself with putting things away and desperately try not to blush."

    e "\"I didn't say it to flatter you. I'm interested in you.\""

    "I nearly drop a cabbage. She says it so frankly, with no hesitation."

menu:
    "We're basically strangers.":
        jump home_stranger

    "How do you know I'm into you?":
        jump younger_women


label home_stranger:
    a neutral "\"You hardly know me.\""

    e  excited "\"It doesn't have to stay that way, you know. I want to learn more.\""

    a happy "\"Hmm.\""

    "I run out of things to mess with so I clasp my hands to keep from fidgeting."
    jump home_push

label younger_women:
    a blush "\"What if I said I'm not into younger women?\""

    e rizzler "\"Then I'll just never tell you my age!\""

    a "\"Silly.\""

    e "\"I'm serious! We obviously have chemistry.\""
    jump home_push


label home_push:

    "I sigh, blushing, and down the rest of my beer."

    a tsuntsun "\"Pushing me about this is not going to do you any favors, kid.\""

    e gloom "\"I'm not a kid, don't look down on me. I'm 23.\""

    e neutral "\"But... sorry. you're right.\""

    a happy "\"No, you're right. You're not a kid. But you're very frank for your age.\""

    "She chuckles at that. It's REALLY cute."

    e "\"Well, I learned that if I don't use my words, people can't read my mind. So I just say what's on my mind instead of worrying about it.\""

    a neutral "\"That... seems reasonable, actually. Doesn't it get you into trouble?\""

    e happy "\"Sometimes. But most of the time, it's the opposite.\""

    "I crush my empty can and toss it into a recycling bin, then lean against a wall, arms crossed."

    a blush "\"It's getting pretty late...\""

    e happy "\"I'll go then. Will you at least give it some thought? I'm not asking for a confession or anything, just that you give me a chance.\""

    a "\"No promises.\""

    e excited "\"Worth a try. Just so you know, I'm going to win you over.\""

    "I don't know what to say to that, but that seems okay with Erin."

    "When she leaves, I lock the door behind her and sit on my heels, one hand still on the door."

    a blush "\"She's so tenacious... And it's SO cute. What am I going to do?!\""

    "I bury my face in my hands, feeling heat flood my cheeks, my ears, down my neck."

    a "\"I think I'm doomed.\""

    "The words ring true even as I determine to steel myself."

    "I'm not going to fall for someone who's just passing through town. She's sticking around to pay back the debt she owes, no other reason."

    scene black with dissolve
    pause 3.0
    jump orchard