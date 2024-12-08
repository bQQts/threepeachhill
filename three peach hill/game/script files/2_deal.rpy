label chapter_two:   ## 2. The Deal - Erin makes a pact with a spirit, and is surprisingly cool with it
    $ chapter_num = 2
    label deal:

        e neutral "\"It was an accident, but I broke it. So I should fix it.\""

        "She says it with conviction. I let go of her and cross my arms."

        a gloom "\"And how are you going to fix it? By picking up broken glass with your bare hands?\""

        e blush "She blushes."

        e happy "\"Let me pay you for it, then.\""

        a gloom "\"It's not something I can replace that easily.\""

        e "\"Humor me, how much?\""

        "I snort and give her a number. Her eyes bulge."

        e shocked "\"I-I, uh, I can't pay that now but let me write you an IOU. And, um... I can leave something as collateral... does that work...?\""

        a happy "\"First, what's your name?\""

        e excited "\"Oh, right. I'm Erin. Erin Prammale! And you are...?\""

        a "\"You can call me Aya.\""

        "I step gingerly past the lamp to grab the broom and dustpan from an alcove next to the front door and hand her the implements."

        a excited "\"You could start by sweeping up all these pieces. Try not to miss any! I actually do have an idea for how we could fix it, but we'll need as many of the pieces as possible.\""

        e neutral "Erin looks doubtful."

        e neutral "\"Really...?\""
        hide brokenlamp with dissolve
        scene brown with dissolve
        pause 1.0
        show bg bookstore with dissolve

    if lamp_freeze_outcome == True:

        jump lamp_freeze_bandage

    else:        

        jump deal_cont

    label lamp_freeze_bandage:

        a neutral "\"Oh, first we should clean up that cut before it gets any worse.\""

        e gloom "\"Thank you, I'm sorry for the trouble.\""

        "I turn off the neon OPEN sign at the front door, grabbing a dry erase marker to scribble out a note that says \"Back at 12:45\", which I stick to the front door."

        "We quickly wash our hands at the bathroom sink and return to the front counter. I reach under it and pull out a first aid kit, removing iodine, gauze, tweezers, and a small bandage."

        "She winces as I press the iodine-soaked gauze into the wound but does not pull away. It only takes a minute to finish treating and bandaging the cut."

        a sad "\"This shouldn't leave a scar, just be sure to keep it clean and dry.\""

        e blush "\"Thank you, Aya.\""

        "For some reason, I really like the sound of my name from her lips."

        "(What am I thinking?)"
    
        "I shake my head to clear the thought from my mind, and clear my throat softly."

        a tsuntsun "\"Okay. Let's get that glass cleaned up before any more visitors come in. I'll... move the peaches, too.\""

        jump deal_cont

    label deal_cont:
        
        "I pop into the back to find a bucket."

        a neutral "\"Put the pieces in this. I'm going to go look something up.\""

        "As Erin collects the pieces, I go get the address book from the front counter and start flipping through it. \"Book\" is a generous descriptor for this mishmash."
            
        "It's a huge leather binder that's been stuffed full of additional sheaves of paper, parchment, newspaper ad clippings, and even some pressed leaves inscribed with nearly illegible writings."

        "These are notes, contacts, fliers, and advertisements from all manner of local business, both human and spirit. My parents added their notes when they took over the shop, and I've added a few of my own over the years."

        "(There must be somebody in here who could fix the lamp.)"

        play sound "sound/PageTurn.flac"
        pause 0.8
        queue sound "sound/PageTurn.flac" volume 0.7
        #queue sound "sound/Glass Sweep.flac" volume 0.7
        queue sound "sound/PageTurn.flac" volume 0.4
        "The bookshop's vibey music is accented by the sounds of pages flipping and glass pieces clinking as we work away."

        e neutral "\"Hey, Aya?\""

        "(There! I've got it!)"
        
        "I pin a no-longer-sticky sticky note with an index finger so the little fan doesn't blow it away while I write in thick marker on a blank page from a nearby notebook. I reply distractedly,"

        a neutral "\"Yeah?\""

        "Erin walks over, setting the bucket of lamp pieces on the countertop. She brushes a few loose strands of hair from her face, tucking them behind her ears, then bends to the counter to prop her weight up on her elbows."

        e gloom "\"Whatever solution you're thinking of had better be magic, because I don't know anyone who could put together all those tiny pieces in a way that fits right. It's pretty busted.\""

        "Her voice is hesitant and full of regret."

        a sad "\"Well, you're right about that.\""

        #play sound "Marker.flac"
        "I finish writing the last few words and sign the bottom of the page with a flourish before sliding the sheet over to Erin."

        show unsigned contract with dissolve

        "She peers at the page, brows furrowed cutely in concentration."

        e neutral "\"What's this? Is this... a contract?\""

        "My mouth curls into a tiny smile, and my tone is light when I explain."

        a neutral "\"It's just something simple. Sign it with your name and it will mean you can accompany me to the Lost Market.\""
        
        a happy "\"We should be able to find a spell that fixes lamps there, and I don't intend to be the one who pays for it.\""

        "Erin gulps."

        e shocked "\"What do I have to pay with? Is it... do I have to pay with, like, blood? Or years off my life? Or my firstborn child? Or—"

        "I interrupt before her imagination takes her farther into a spiral."

        a excited "\"No, no, nothing like that. Just regular money. Most spirits in the modern era use human currency to keep things simple,\""
        
        a "\"...though it's possible to find the odd esoteric spirit who wants weird ingredients, favors, or labor as their exchange rate.\""
        
        a gloom "\"But whatever the cost, nothing is ever free.\""

        e neutral "\"So you want me to go with you to the spirit world?"

        a neutral "\"It's not really the Other Side, which is what you're referring to. It's more of a liminal space between the two worlds.\""
        
        a "\"It's easy to travel between worlds through the market as long as you've made a deal before you go. If you don't... the Lost Market keeps you until you do.\""

        "I see the worried look on her face."

        a excited "\"Which won't be a problem, since we'll have a deal in place already!\""

        e blush "\"O-okay! Will the spell cost the... the same amount you listed earlier? Because I don't think I can pay that...\""

        a "\"Gods, no. It'll cost enough, and you'll be able to cover it. It's a magic thing.\""

        "She waggles a finger at me."

        e gloom "\"You don't know just how broke I am. I'm a college student.\""

        "My ear twitches and I shrug."

        a happy "\"It'll be fine! Anyway, if you're that broke you should probably pay better attention to your surroundings so you don't accidentally break peoples' stuff.\""

        "I'm mostly joking. We both know it wasn't really her fault. She takes it in stride."

        "She reads the contract very carefully, and I feel a sense of approval about the care she's taking. Always know what you're signing up for."

        "She might be a bit clumsy, but she's not a fool. After a couple of minutes, she nods and sets the paper down."

        e excited "\"So when do we go?\""

        "I tap a finger against the countertop and think it over."

        a shocked "\"We should be able to go on the night of the autumn equinox. That's when it's pretty much guaranteed to show up. Any other time can be kind of hit or miss."

        e neutral "\"That's like, next month, right?\""

        a neutral "\"Yes, {color=#F87B4E}the evening of the 22nd{/color}. That a problem?\""

        "She pulls out her phone, presumably to check her calendar, and bites her lip. It's more distracting than I care to admit."

        e happy "\"It could be... but I said I'd fix your lamp, and that's a promise. I'll make it work. Can I borrow your pen?\""

        "I wordlessly pass her the marker, which has a plastic spoon taped to it. She takes it and signs the bottom of the page."

        show signed contract with dissolve

        pause 1

        ## in a future version it would be cool to have art/simple animation of the contract going golden
        play sound "sound/Magic Spell Push.flac" volume 0.5
        hide unsigned contract with dissolve
        "With a whoosh, heatless golden flames trace the lines of ink and the page disappears."

        hide signed contract with dissolve

        "If we were on The Other Side, we'd be able to see the little red ribbon of promise that now connects us. But we're here, so we can't."

        "Erin startles."

        e shocked "\"What was that?\""

        "The surprise on a human's face when they see everyday magic never really gets old."

        a blush "\"It's not a trick or anything, that's just the pact being made! It links us. Think of it as a little magical insurance that automatically happens when spirits make agreements.\""
        
        a neutral "\"Basically, if you decide to bail, there will be a karmic consequence. This isn't a big pact, so even if you do decide to bail it won't be too drastic. But I still suggest you try to keep your word.\""

        "She nods and makes a note in her phone."

        e happy "\"Alright, that makes sense. Then... I guess I'll see you around? Oh wait, let me give you my number.\""

        "I expect her to jot it down on the paper, but she confidently takes my wrist and writes the number there, the marker tickling my skin. She grins."

        e rizzler "\"So you don't lose it!\""

        "I blush furiously."

        "Erin rocks back on her heels and does a little spin, walking lightly to the door. Hand poised to open it, she looks back over her shoulder at me."

        e excited "\"Bye, gorgeous!\""

        "My heart skips a beat and I hesitate, not sure if she means that in an I-love-women way or a complimenting-between-girlies way."
        
        "She notices the heat warming my cheeks. Before I can say anything in response, she ducks out of the store, giggling."

        a tsuntsun "\"Wh... what...!\""

        scene brown with irisin
        jump pursuit