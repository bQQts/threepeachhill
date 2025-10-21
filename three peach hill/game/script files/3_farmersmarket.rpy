label chapter_three_b:
    $ chapter_num = 3
    label farmers_market:
        pause 1.5
        show date_animated_ch3B with dissolve  # July 27
        pause 2.5
        hide date_animated_ch3B with Dissolve(2)


        # Screen that says a week passes ## wait I'm not sure if its a week from the 20th or a week from the 27th....... D:
        # Farmers Market title screen

        scene brown with dissolve
        stop music fadeout 2.0
        show bg market with dissolve
        play music quiet_village fadein .5
        
       
        "As you approach the town's central plaza your ears prick up at the hum of generators and the murmur of a small crowd."
        
        "Your foxen senses catch the scent of baked goods, hot cider, and herbs on the light breeze that carries away the last bit of the summer day's humidity."

        "The farmers market is in full swing for harvest season."

        "Orchard vendors sell more of the early season peaches; other stalls sell the last of the season's blackberries. The usual veggie stands have a bounty of fresh treasures--corn, broccoli, peppers, radishes."
        
        "A beekeeper has paired up with a woodworker to selling wooden wands and bread bowls alongside clover and wildflower honeys."

        "Rows of tents offer unique, handcrafted goods from merchants in the surrounding regions who've come to this town to peddle their wares."

        "There's even another fox spirit selling lucky talismans. The talismans are real magic, though the workings are quite small; it's better not to swing the karmic balance too far in any direction unless you really know what you're doing."

        "The first farmers market of the season is always a big one. You love to see the same faces year after year. It's a good time to meet new merchants, too."

        "You pick up some veggies, a cup of black coffee, and buy a loaf of bread from a baker who drove 3 hours to be here. It's divine."

        "Your bags are much heavier after a good lap around the produce side of the market. You head to a flower stand you've bought from in the past in search of your usual marigold and sunflowers. Your favorites."

        pause 2.0

        "You hear her voice before you see her."

        e happy "\"Coming right up! Let me get those bagged for you.\""

        "A customer hands Erin a bouquet of daisies and she turns around to place it in a water-sealed paper bag."

        "She's smiling when she returns the bouquet to the customer, then sees you and waves."

        e excited "\"Aya! Are you here to get flowers??\""

        a happy "\"I sure am. I didn't expect to see you here!\""

        e happy "\"It's a part time gig! I helped unload everything. I could probably give you some ideas on what looked the prettiest today! What would you think about this little bouquet of lavender and larkspur?\""

        menu:
            "Your arms are quite full, you should really only get one bouquet. Which to choose, though?"

            "Marigold and sunflowers":
                jump farmers_market_marigold

            "Lavender and larkspur":
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
                jump farmers_market_lavender

        label farmers_market_marigold:

            a "\"Thanks, but I think I'll get my usual. A bouquet each of marigold and sunflowers, please.\""

            e "\"Oooh how pretty! I love that, I'll bag those for you.\""

            jump farmers_market_cont

        label farmers_market_lavender:

            a "\"That's a good suggestion, I'll take the lavender and larkspur.\""

            "She beams at you and nearly bounces to fetch a bouquet of purple and blue sprigs."

            e blush "\"Here, this is my favorite one from this morning! Do you like it??\""

            a excited "\"I love it.\""

            jump farmers_market_cont

    label farmers_market_cont:

        "Erin bags the flowers and waves over the flower merchant, your old friend Jeff, so you can pay for them."

        show jeff at right with dissolve:
            subpixel True
            zoom 0.7
            yoffset -300

        jeff "\"Oh, hello there Aya!\""

        e neutral "\"You know Aya?\""

        jeff "\"Kiddo, you forget I've been selling here for ages. Aya's a long time customer, she comes by almost every weekend during the market season!\""

        e happy "\"Oh, duh! Aya, you must really like flowers!\""

        "You chuckle. Jeff gives the two of you a knowing look."

        jeff "\"You know, Erin, if you'd like to call it a day here I'm sure Aya would be happy to show you around the rest of the market.\""

        "He winks at you on the sly."

        a neutral "\"Oh no, Jeff, if you need the extra help I really don't want to pull her away. I was just stopping by to get flowers—\""

        jeff "\"Nonsense, we'll be just fine. She was a huge help unloading everything this morning, but we can take it from here. Kiddo, let me pay you now so you have some change for the rest of the market.\""

        e excited "\"Really?! Thank you! This is great!!\""

        "She unties her apron and lays it over the back of a folding chair behind the sales table, slings her book bag over her shoulder, then comes around to join you."

        e happy "\"Won't you show me around the market? I bet you know where all the good stuff is!\""

        a tsuntsun "\"I suppose...\""

        "Jeff comes back with an envelope for Erin and a big grin for you both."

        jeff "\"You two take care, now!\""

        a happy "\"Thanks, old man. Likewise!\""

        hide jeff with dissolve

        pause 0.5

        "You tuck the flowers into the larger of your tote bags and heft them so the straps rest more comfortably on your shoulders."

        "Erin notices the motion and offers a hand."

        e neutral "\"Let me carry your bags, okay? You must be tired from carrying them around all day.\""

        "You start to protest, but she insists, and you end up giving her the two smaller totes while you wrangle the largest one with the flowers."

        scene bg market
        stop music fadeout 3.0
        scene brown with dissolve
        pause 1.5
        show bg market with dissolve
        play music happy_village fadein 1.5 noloop
        pause 2.0

        "You walk through the crafts and goods side of the market, trying food samples and looking at homemade wares and curated jewelry."

        "After a while, Erin takes a detour to the restrooms and leaves the bags with you. You decide to look around a bit, and one booth catches your eye."

        "It's a table with hair pins of all different styles. You find a brass pin with a cast sunflower at the end of it. It's just your style."
        
        "You almost check out then, but see that one pin is part wood and part resin-cast. The resin looks like it's frozen big rainbow bubbles in time."

        a neutral "(Erin likes to wear her hair up...)"

        ##Could add a choice here to buy both or just Aya's pin

        "You hesitate for a moment, then buy both pins."

        "You head back to the spot where Erin left so you'll be waiting there when she returns."

        "You're just in time. She emerges and bounces toward you. She holds a hand out for the bags and you shove the bubble hair pin towards her."

        e excited "\"What's this?\""

        a blush "\"It's a hair pin. For you.\""

        a "(Please don't make a big deal out of it.)"

        "Her eyes shine and she holds it to her chest."

        e blush "\"You didn't have to do that!\""

        a tsuntsun "\"It's just a hair pin, don't mention it.\""

        e excited "\"Well, thank you! It's so cute!!!\""

        "She tucks it away safely in her book bag and we continue walking around the market."

        scene brown with dissolve
        pause 2.0
        jump lamp_talk

    label lamp_talk:
        show bg market with dissolve
        stop music fadeout 3.0
        pause 1.0
        queue music quiet_village fadein 0.5

        a sad "\"So, I wanted to tell you more about that lamp...\"" 

        "You trail off, lost in the memory for a moment. Your throat feels tight, your chest heavy."

        e gloom "\"I'm sorry about that. I really want to make it up to you.\""

        "Erin picks at a ragged cuticle, her eyes downcast."

        a shocked "\"Oh, I'm not bringing it up for you to keep apologizing!\""
        
        a neutral "\"No... I just felt like you should know why it was important to me. Important enough to try to go to the Lost Market, you know?\""

        "Erin looks sidelong at you, saying nothing. Just waiting, patient. You have her full attention."

        "You clear my throat softly and continue,"

        a happy "\"It was my mom's. She made it when I was really young. They kept it up on a high shelf so I wouldn't accidentally... break it.\""

        a "\"I didn't really appreciate that lamp 'til I was older. It grew on me, and turning it on each day was like a reminder that mom's still around, lighting up the darkness.\""

        a "\"It's special to me.\""


        if lamp_check == True:
            jump lamp_talk_apology
        else:
            jump lamp_cont

    label lamp_talk_apology:
        a sad "\"I'm sorry I didn't check to see if you were okay first, that was kinda shitty of me. It's just... it was another piece of her gone, just like that.\""

        jump lamp_cont

    label lamp_cont:
        "Erin gently rests her free hand on my shoulder."

        e neutral "\"What happened to her? Sorry, I guess that's not really a polite question! You don't have to answer...\""

        "You smile a little at her concern and pat her hand, drawing it down from your shoulder and clasping it between you. It's warm and strong. An artist's hand."

        a sad "\"One of her lovers was mortally wounded in an accident and had to return to The Other Side to recover, and she was so depressed about it.\""
        
        a "\"Dad encouraged her to go back to The Other Side to be with her lover, and when she eventually went, he went with her.\""

        e sad "\"Is that like... dying? Going to The Other Side?\""

        "You shake your head."

        a happy "\"No, it's more like... going to a faraway place that's hard to travel to, and harder to return from. They could come back, but time moves differently there.\""

        a neutral "\"Sometimes it goes faster, sometimes much slower. So they could show back up here at any time, really. Or it could be decades. There isn't a good way to know.\""

        "Erin tilts her head to the side, contemplating the new information."

        e neutral "\"Do you miss them?\""

        "Tears prickle at your eyes."

        a sad "\"I do. I can't wait to see them again, but I'm nowhere near ready to go to The Other Side myself. I'm enjoying this mortal life.\""

        "You realize then that you're still holding her hand and loosen your grip as if to pull away, but she keeps holding on and gives you a little squeeze."
        
        a tsuntsun "(So forward, but it's... nice. I suppose a little hand holding isn't doing any harm.)"

        "You leave your hand in hers. You walk in silence, hand in hand, cicadas buzzing in the trees along the sidewalk."

        scene brown with irisin
        pause 2.0
        jump going_home_from_market


    label going_home_from_market:

        show bg gate with dissolve

        "Erin walks you the rest of the way home, laden with your bags from the market."

        "Somehow she wheedled you into giving up the remaining bag."

        e happy "\"Can I have some more kettle corn?\""
        
        "You pop a piece in her mouth."
        e happy "\"More!!!\""

        "You grin and keep feeding her pieces until she can't talk."

        "She looks like a chipmunk. A cute little chipmunk loaded up with even more snacks for her winter stash..."

        "She giggles at your expression and a piece falls out of her mouth."

        e happy "\"Mmggghh!!!\""

        "So. Freaking. Cute."

        "You let her munch away at the kettle corn for a bit until it seems like she can talk again."

        a blush "\"Today was really lovely. Thanks for carrying my bags...\""

        e happy "\"Today was AMAZING!!! And it's no trouble, I'm glad I was able to give you a hand!\""

        "You invite her in, kicking off your shoes at the front door and stepping into a cozy pair of slippers instead. She follows suit and pauses to kick off her sneakers, then carries the bags in, looking around with wide eyes."

        hide bg gate with dissolve
        stop music fadeout 3
        pause 1.5
        show bg kitchen with dissolve
        play music romance fadein 1.5

        "Your home is old and loved, the result of generations of care and curation. The walnut tables and shelves glisten with wood oil--you just polished everything last week."

        "Paintings and pictures of family members in various settings dot the walls. You smile when Erin notices a favorite of yours--a picture of your parents and their mates in their youth sprawled on a picnic blanket beneath a blossoming spring cherry tree."

        a "\"Please, make yourself at home.\""

        "You go to the fridge. Erin must be thirsty after all that pack-muling... and all the kettle corn!"

        a neutral "\"Would you like something to drink? Water, beer, tea...?\""

        e excited "\"Water first, please, but after that a beer would hit the spot!\""

        a happy "\"Of course!\""

        menu:
            "You need a drink, too."

            "Water, no ice. Ice water gives you hiccups.":
                jump kitchen_drinks

            "A cold beer. You should let loose!":
                jump kitchen_beer

            "Tea. Earl Grey sounds great right now.":
                jump kitchen_tea

        label kitchen_water:
            "So refreshing."
            jump kitchen_drinks

        label kitchen_beer:
            "You can't let Erin crack a cold one alone, right?"
            jump kitchen_drinks

        label kitchen_tea:
            "Your hot water machine is ready and waiting--no kettle necessary. Truly, you live in luxury."

    label kitchen_drinks:
        "You sit in companionable silence across the kitchen table, sipping at your drinks."

        "You trace a finger across the carved inlay on the edge of the table. The florals and whorls are so pretty."

        "Erin is so pretty."

        "You look up at her and she's already watching you. She takes a sip of her beer and sets it down, resting her elbows on the table and propping her chin up on an open hand."

        e blush "\"I meant what I said that day, you know.\""

        a "\"Which day do you mean?\""

        e excited "\"That first day. When I called you gorgeous.\""

        "Your heart flutters."

        a tsuntsun "\"O-oh! That day, right. Thank you. I'm flattered!\""

        "You stand up and hurriedly busy yourself with putting things away, desperately trying not to blush."

        e happy "\"Aya... I didn't say it to flatter you. I'm interested in you. And you like me too, right?\""

        "You nearly drop the cabbage you were unloading from the market tote. She says it so frankly, with no hesitation."

    menu:
        "But you hardly know me... (Dodge her flirt)":
            jump home_stranger

        "How would you know who I'm into?~ (Flirt back)":
            jump younger_women


    label home_stranger:
        "It's too much, too soon. She doesn't know you well enough to really like you."

        a neutral "\"We're basically strangers.\""

        "Strangers who held hands at the market."

        "But Erin is not thrown by your weak attempt at evasion."

        e  excited "\"It doesn't have to stay that way, you know. I want to learn more.\""

        a happy "\"Oh...\""
        "That makes you happy, but you're not sure what to do."

        "You run out of things to mess with and clasp your hands to keep from fidgeting."
        jump home_deflect

    label younger_women:
        e excited "\"I just feel it!\""

        a blush "\"And what if I said I'm not into younger women?\""

        e rizzler "\"Then I'll just never tell you my age! Who knows, maybe I'm older than you!\""

        a "\"Silly.\""

        e "\"C'mon, I'm serious! We obviously have chemistry.\""

        "She's so cute that you almost tell her you've been crushing on her, too. But..."

        jump home_deflect


    label home_deflect:

        "You just need a little more time."

        menu:
            "She's waiting for an answer. You need to buy yourself more time. Time to think, time to feel out your feelings, time to make sure you know what you want. You don't want to hurt this sweet girl's feelings."

            "\"You're very frank, you know that?\"":
                jump frank

            "\"I-I don't want a summer fling...\"":
                jump fling

            "\"Uh, it's getting late...\"":
                jump getting_late

        label frank:
            a happy "\"VERY frank.\""

            "She giggles. It's REALLY cute."

            e "\"Well, I learned that if I don't use my words, people can't read my mind. So I just say what's on my mind instead of worrying about it.\""

            a "(That's so charming...)"

            a neutral "\"Doesn't it get you into trouble?\""

            e happy "\"Sometimes. But most of the time, it's the opposite.\""

            e "\"Soooo...?\""

            a "\"I'm not ready to think about that right now, to be honest.\""

        label fling:
            a blush "\"It's just not my thing.\""

            e neutral "\"That's okay! We could--\""

            "You interrupt her gently."

            a neutral "\"Erin, give me some time, okay?\""


        label getting_late:
            e happy "\"No worries! I would hate to overstay.\"" 

            jump give_her_a_chance
        
    label give_her_a_chance:

        e happy "\"Will you at least give it some thought? I'm not asking for a confession or anything, just that you give me a chance.\""

        a neutral "\"No promises.\""

        a blush "\"But just to be clear, I'm not saying no...\""

        e excited "\"Worth a try. Just so you know, I'm going to win you over.\""

        "You don't know what to say to that, but that seems okay with Erin."

        "When she leaves, you lock the door behind her and crouch to sit on your heels, one hand still on the door."

        a blush "\"She's so tenacious... And it's SO cute. What am I going to do?!\""

        "You bury your face in your hands, feeling heat flood your cheeks, your ears, down your neck."

        a "\"I like her.\""

        "The words ring true even as you determine to steel yourself."

        "You're not going to fall for someone who's just passing through town. She's sticking around to pay back the debt she owes, no other reason. You need to get her out of your head."

        scene brown with dissolve
        stop music fadeout 2.0
        pause 3.0
        jump orchard