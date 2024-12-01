label farmers_market:
    # July 27
    # Introductory scene 
    # Screen that says a week passes
    # Farmers Market title screen
    scene brown with dissolve
    stop music fadeout 2.0
    pause 2.0
    show bg market with dissolve
    play music quiet_village fadein .5
    
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

    scene bg market
    stop music fadeout 3.0
    scene brown with dissolve
    pause 1.5
    show bg market with dissolve
    play music happy_village fadein 1.5 noloop
    pause 2.0

    "We walk through the market, trying food samples and looking at crafts and jewelry."

    "After a while, Erin takes a detour to the restrooms and leaves the bags with me. I decide to look around a bit, and one booth catches my eye."

    "It's a table with hair pins of all different styles. I find a brass pin with a cast sunflower at the end of it, and it's perfect for me."
    
    "I almost finish my shopping there, but then I see that one pin is part wood and part resin-cast. The resin looks like it has frozen big rainbow bubbles in time."

    "I hesitate for a moment, then buy both pins."

    "I head back to the spot where Erin left, and I'm waiting there when she returns."

    "I shove the bubble hair pin towards her."

    e blush "\"What's this?\""

    a blush "\"It's a hair pin. For you.\""

    "(Please don't make a big deal out of it.)"

    "Her eyes shine and she holds it to her chest."

    e "\"You didn't have to do that!\""

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

    a sad "\"So, that lamp...\"" 

    "I trail off, lost in the memory for a moment. My throat feels tight, my chest heavy."

    e gloom "\"I'm sorry about that. I really want to make it up to you.\""

    "Erin picks at a ragged cuticle, her eyes downcast."

    a shocked "\"Oh, I'm not bringing it up for you to keep apologizing!\""
    
    a neutral "\"No... I just felt like you should know why it was important to me. Important enough to try to go to the Lost Market, you know?\""

    "Erin looks sidelong at me, saying nothing. Just waiting, patient. I have her full attention."

    "I clear my throat a little and continue,"

    a happy "\"It was my mom's. She made it when I was really young. They kept it up on a high shelf so I wouldn't accidentally... break it.\""

    a "\"I didn't really appreciate that lamp 'til I was older. It grew on me, and turning it was like a reminder that mom's still around, lighting up the darkness.\""

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

    e neutral "\"What happened to her? Sorry, that's not really a polite question. You just sound so wistful, but not really sad?\""

    "I smile a little at her concern and pat her hand, drawing it down from my shoulder and clasping it between us. Her soft hand is warm and a little bit tacky from the humid summer air."

    a sad "\"One of her lovers was mortally wounded in an accident and had to return to The Other Side to recover, and she was so depressed about it.\""
    
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
    
    "(So, we're both aware of it. But neither of us is saying anything about it. And it's... nice. I suppose it isn't doing any harm.)"

    "I leave my hand in hers. We walk in silence, hand in hand, cicadas buzzing in the trees along the sidewalk."

    scene brown with irisin
    pause 2.0
    jump going_home_from_market


label going_home_from_market:

    show bg gate with dissolve

    "Erin walks me home, still carrying my bags from the market."

    a happy "\"Thank you, today was really nice!\""

    e happy "\"It's no trouble, I'm glad I was able to give you a hand.\""

    "I invite her in, kicking off my shoes at the front door and stepping into a cozy pair of slippers instead. She pauses to slide out of her sneakers and carries the bags in, looking around."

    hide bg gate with dissolve
    stop music fadeout 3
    pause 1.5
    show bg kitchen with dissolve
    play music romance fadein 1.5

    a "\"Please, make yourself at home.\""

    "I go to the fridge."

    a neutral "\"Water? Beer? Tea?\""

    e excited "\"Beer sounds amazing! Thanks.\""

    a happy "\"Of course!\""

    "We sit in companionable silence for a little bit, sipping at our drinks."

    e blush "\"I meant what I said that day, you know.\""

    a "\"Which day?\""

    e happy "\"When I said you're beautiful.\""

    a tsuntsun "\"O-oh! That day, right. Thank you. I'm flattered!\""

    "I hurriedly busy myself with putting things away and desperately try not to blush."

    e "\"I didn't say it to flatter you. I'm interested in you. And you like me too, right?\""

    "I nearly drop a cabbage. She says it so frankly, with no hesitation."

menu:
    "We're basically strangers.":
        jump home_stranger

    "How would you know who I'm into?":
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

    e gloom "\"I'm not a kid, don't look down on me. I'm... I'm 23.\""

    e neutral "\"But... sorry. you're right.\""

    a happy "\"No, you're right. You're not a kid. But you ARE very frank.\""

    "She giggles. It's REALLY cute."

    e "\"Well, I learned that if I don't use my words, people can't read my mind. So I just say what's on my mind instead of worrying about it.\""

    a neutral "\"That... seems reasonable, actually. Doesn't it get you into trouble?\""

    e happy "\"Sometimes. But most of the time, it's the opposite.\""

    "I crush my empty can and toss it into a recycling bin, then lean against a wall, arms crossed."

    e "\"So... about my question.\""

    a blush "\"Um, it's getting pretty late...\""

    e happy "\"Alright, I'll go then. Will you at least give it some thought? I'm not asking for a confession or anything, just that you give me a chance.\""

    a "\"No promises.\""

    e excited "\"Worth a try. Just so you know, I'm going to win you over.\""

    "I don't know what to say to that, but that seems okay with Erin."

    "When she leaves, I lock the door behind her and sit on my heels, one hand still on the door."

    a blush "\"She's so tenacious... And it's SO cute. What am I going to do?!\""

    "I bury my face in my hands, feeling heat flood my cheeks, my ears, down my neck."

    a "\"I think I'm doomed.\""

    "The words ring true even as I determine to steel myself."

    "I'm not going to fall for someone who's just passing through town. She's sticking around to pay back the debt she owes, no other reason."

    scene brown with dissolve
    stop music fadeout 2.0
    pause 3.0
    jump orchard