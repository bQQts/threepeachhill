label pursuit:
"The rest of the week is much less eventful. The air is as humid as ever. The cicadas continue to play their summer soundtrack. Finally, the weekend comes calling."

menu:
    "I make cobbler for the neighbors":
        jump cobbler

    "I make a trip to the cornerstore to pick up drinks and groceries":
        jump cornerstore

label cobbler:

    "Fortunately, the peaches had sustained no damage at all during The Incident, and I'm able to whip up a couple of test cobblers."

    "The local peaches aren't quite in season yet, so these are just some of the early bloomers that my friend at the orchard set aside for me."

    "The cobblers aren't bad. They're not as sweet as I had hoped they'd be, but that makes sense since peach season starts next month."
    
    "I should have accounted for the difference and adjusted my recipe, but this is good practice for the real thing!"

    "I divide the cobblers into plastic food storage bins to give to the neighbors. Some of my older friends are the opposite of sweet-tooths and will probably love this."

    # Couple of neighbor interactions, maybe this is a choice where you can pick who to go to?
    # A regular day
    # Thinking about what Erin is up to
    # Some interesting choice
    jump farmersmarket

label cornerstore:
    "TBD"
    # Another week goes by
    # Run into Erin at the cornerstore
    # Erin's working to make some extra cash while she's in town, she's staying at an Airbnb for now
    jump farmersmarket

label farmersmarket:
    "TBD"
    # Erin is working for the florist doing odd jobs
    # Aya buys some flowers and Erin talks to the florist and gets permission to call it a day, so she joins Aya and carries her bag for her
    # They get vegetables, fresh bread, and Aya picks out something cute for Erin
    jump Lamp_Talk

label Lamp_Talk:
    a "\"That lamp...\"" 

    "I trail off, lost in the memory for a moment. My throat feels tight, my chest heavy."

    e "\"I'm sorry about that, I really am.\""

    "Erin picks at a ragged cuticle, her eyes downcast."

    a "\"Oh, I'm not bringing it up for you to keep apologizing. No... I just felt like you should know why it was important to me. Important enough to make that pact, you know?\""

    "Erin looks at me directly, saying nothing. Just waiting, attentive and patient. Fully present with an intensity you don't see often."

    "I clear my throat a little and continue,"

    a "\"It was my mom's. She made it when I was young enough that I could only see it from afar, to minimize the risk of me breaking it.\""

    # IF WENT LAMP
    a "\"I'm sorry I didn't check to see if you were okay first, that was shitty of me. It's just... it was another piece of her gone, just like that.\""

    jump Lamp_Cont

label Lamp_Cont:
    "Erin gently rests her free hand on my shoulder."

    e "\"What happened to her? Sorry, I guess that's not really a polite question. You just sound so wistful, but not really sad?\""

    "The questioning lilt at the end of her sentence made the statement into a question of its own."

    "I smile a little at her concern and pat her hand, drawing it down from my shoulder and clasping it between us. Her soft hand is warm and a little bit tacky from the humid summer air."

    a "\"One of her lovers was mortally wounded in an accident and had to return to The Other Side to recover, and she was so depressed about it.\""
    
    a "\"Dad encouraged her to go back to The Other Side to be with her lover, and when she eventually went, he went with her.\""

    e "\"Is that like... dying? Going to The Other Side?\""

    "I shake my head."

    a "\"No, it's more like... going to a faraway place that's hard to travel to, and harder to return from. They could come back, but time moves differently there.\""
    
    a "\"Sometimes it goes faster, sometimes much slower. So they could show back up here at any time, really. Or it could be decades. There isn't a good way to know.\""

    "Erin tilts her head to the side, contemplating the new information."

    e "\"Do you miss them?\""

    "I feel my eyes start to mist up and blink the tears back."

    a "\"I do. I can't wait to see them again, but I'm nowhere near ready to go to The Other Side myself. I'm enjoying this mortal life.\""

    "I realize I'm still holding her hand and loosen my grip as if to pull away, but she keeps holding on and gives my hand a little squeeze."
    
    "So, we're both aware of it. But neither of us is saying anything about it. And it's... nice. I suppose it isn't doing any harm."

    "I leave my hand in hers. We walk in silence, hand in hand, cicadas buzzing in the trees along the sidewalk."

    jump going_home_from_market


label going_home_from_market:

    "Erin walks me home, carrying my bags from the market."

    a "\"Thank you, today was really nice!\""

    e "\"It's no trouble, I'm glad I was able to give you a hand.\""

    "I invite her in, kicking off my shoes at the front door and stepping into a cozy pair of slippers instead. She pauses to slide out of her sneakers and carries the bags in, looking around."

    a "\"Please, make yourself at home.\""

    "I go to the fridge."

    a "\"Water? Beer?\""

    e "\"Beer sounds amazing! Thanks.\""

    a "\"Of course!\""

    "We sit in companionable silence for a little bit, nursing our drinks."

    e "\"I meant what I said that day, you know.\""

    a "\"Which day? \""

    e "\"When I said you're beautiful.\""

    a "\"O-oh! That day, right. Thank you. I'm flattered!\""

    "I hurriedly busy myself with putting things away and desperately try not to blush."

    e "\"I didn't say it to flatter you. I'm interested in you.\""

    "I nearly drop a cabbage. She says it so frankly, with no hesitation."

menu:
    "We're basically strangers.":
        jump home_stranger

    "How do you know I'm into you?":
        jump younger_women


label home_stranger:
    a "\"You hardly know me.\""

    e "\"It doesn't have to stay that way, you know. I want to learn more.\""

    a "\"Hmm.\""

    "I run out of things to mess with so I clasp my hands to keep from fidgeting."
    jump home_push

label younger_women:
    a "\"What if I said I'm not into younger women?\""

    e "\"Then I'll just never tell you my age!\""

    a "\"Silly.\""

    e "\"I'm serious! We obviously have chemistry.\""
    jump home_push


label home_push:

    "I sigh, blushing, and down the rest of my beer."

    a "\"Pushing me about this is not going to do you any favors, kid.\""

    e "\"I'm not a kid, don't look down on me. I'm 23.\""

    e "\"But... sorry. you're right.\""

    a "\"No, you're right. You're not a kid. But you're very frank for your age.\""

    "She chuckles at that. It's REALLY cute."

    e "\"Well, I learned that if I don't use my words, people can't read my mind. So I just say what's on my mind instead of worrying about it.\""

    a "\"That... seems reasonable, actually. Doesn't it get you into trouble?\""

    e "\"Sometimes. But most of the time, it's the opposite.\""

    "I crush my empty can and toss it into a recycling bin, then lean against a wall, arms crossed."

    a "\"It's getting pretty late...\""

    e "\"I'll go then. Will you at least give it some thought? I'm not asking for a confession or anything, just that you give me a chance.\""

    a "\"No promises.\""

    e "\"Worth a try. Just so you know, I'm going to keep pursuing you.\""

    "I don't know what to say to that, but that seems okay with Erin."

    "When she leaves, I lock the door behind her and sit on my heels, one hand still on the door."

    a "\"She's so tenacious... And it's SO cute. What am I going to do?!\""

    "I bury my face in my hands, feeling heat flood my cheeks, my ears, down my neck."

    a "\"I think I'm doomed.\""

    "The words ring true even as I determine to steel myself."

    "I'm not going to fall for someone who's just passing through town. She's sticking around to pay back the debt she owes, no other reason."

    jump orchard