label orchard:
    scene black
    show bg bookstore with dissolve

    # August 3

    "Another week goes by and I manage to avoid running into Erin. She's texted me more pictures of the gray cat outside of the cornerstore, but I haven't replied."

    "She's really persistent, though, and dripping with optimism. But I feel like she can probably tell that something's off."

    "The whole thing—trying to smother my feelings, avoiding her—it's got me in a sour mood. So, today I'm going out."

    "Three Peach Hill is an orchard known for its stunning peach trees. Like the name implies, it spans rolling hills."
    
    hide bg bookstore with dissolve
    show bg orchard with dissolve

    "The team of farmers who tend the orchard under Head Orchardist Joy have been quite busy as many of the trees are ready for harvest."

    "I see Joy directing a couple farmers who are helping load her truck with an order of peaches and I wave to her as I park my bicycle alongside the orchard's front office building. She waves back with a big grin."

    "Yesterday she had posted a picture of the first ripe peaches dangling from trees on social media with the caption, \"Peach picking is open! Come by to fill a cart or basket!\""

    "I couldn't make it out here yesterday, but it's a nice Saturday and I have the whole day free. So here I am, on my way to fill a cart of peaches. The pie I'm gonna make out of these is going to be legendary."

    "The farmers at the orchard point me toward the hill where the peaches are available for the public to pick."

    "I'm walking up the hill when I hear her voice, and my heart beats a little faster."

    "Erin is here of all places, on today of all days. Just my luck."

    "Her oversized shirt and messy bun are so cute on her. She wipes her brow with the back of a work-gloved hand, laughing at something a girl in a VOLUNTEER vest said. I keep walking, hoping she doesn't notice me."

    e happy "\"Aya,\""

    "Erin calls out to me, jogging to catch up to me as I {i}very subtly{/i} pick up my pace."

    e excited "\"Hi!\""

    a gloom "\"Hi.\"" 

    "The word came out crabbier than I meant it to."

    "But... I'm trying to avoid her! Surely she'll get the memo if I'm brusque with her. Right? So maybe crabby isn't a bad thing!"

    e neutral "\"Wait!\"" 

    "She catches my hand and I lurch as she tugs my arm gently but firmly. I yank my arm back, and she lets go. The lack of resistance throws me off balance, and I stumble."

    a sad "\"What do you want?\""

    e sad "\"It's just, it seems like you've been avoiding me—or maybe I'm just reading into it?\""

    a "\"...\""

    "I sigh."

    a neutral "\"I have been.\""

    e neutral "\"I didn't do anything, though.\""
    
    a sad "\"That's true... but... I just wanted some space.\""

    e sad "\"Was I being too much?\""

    a blush "\"No! No, I...\""
    
    e rizzler "\"Wait... wait, were you possibly avoiding me because youuuu like me back?\""

    "I flush hot red."

    e excited "\"Oh my gods! You like me!\""

    "She covers a grin with her hand and giggles."

    a tsuntsun "\"What! No! That's absurd!\""

    e gloom "\"Your face says otherwise, but fine. Explain it to me, then. What are you running from?\""

    "She looks a bit hurt, and my heart aches at the sight."
    
    "But... I really don't want to get involved in something temporary. Whether or not I like her, I need to do this."

menu:
    "I've got to put an end to this before something starts."

    "Shut this down hard":
        jump shut_this_down

    "Let her down gently" if kind_points >= 2:
        jump let_her_down_gently

label shut_this_down:
    a "\"I don't want to waste my time.\""

    "...is what I said. It's partly true, I am worried. But what I mean, and what I can't tell her, is that I'm afraid she might be what I want. And I don't want it to hurt when she leaves."

    "Erin's eyes mist with tears."

    e sad "\"Wasting time? What do you mean? Is there something wrong with me?\""

    "I wince."

    a sad "\"W-we're just not a good fit. You're not... you're not... actually, it's not really about you.\""

    "She stiffens."

    e neutral "\"So you're just afraid.\""

    "Without another word, she turns and walks away."

    "She's right."

    scene black with dissolve
    pause 2.0
    jump the_rain



label let_her_down_gently:

    a blush "\"I'm not really available right now... I'm, uh, looking for something specific.\""

    e neutral "\"I could be what you want. Just tell me who to be and I'll be that.\""

    "That sentence hurts my heart."

    a tsunstsun "\"No, I'm not going to tell you who to be! That would be horrible.\""

    e gloom "\"But you don't like who I am and I don't know why.\""

    "{i}I do like you. Gods, I do. But you have school, you're bound to leave, and I don't think you'll come back out here when you're done.{/i}"

    a gloom "\"I... don't have a good answer.\""

    e shocked "\"You're just afraid, aren't you?\""

    "She almost yells the words. Then she shoves her hands into her shorts pockets and strides away, back down the hill."

    "She's right."
    
    scene black with dissolve
    pause 2.0
    jump the_rain
