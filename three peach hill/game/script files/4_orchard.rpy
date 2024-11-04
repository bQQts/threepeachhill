label orchard:
    "Another week goes by and I manage to avoid running into Erin. It's been good for me, I'm able to keep my head on straight."

    "Today I'm going out."

    "Three Peach Hill is an orchard known for its stunning peach trees. Like the name implies, it spans rolling hills. The team of farmers who tend the orchard under Head Orchardist Joy have been quite busy, as the peaches are in season and many of the trees have produced fruit ripe enough to pick."

    "Joy and I have been friends for almost our whole lives. I see her loading her truck with an order of peaches and wave to her as I park my bicycle alongside the orchard's shop. She rolls her shoulders in a languorous stretch and waves back with a big grin."

    "Yesterday she had posted a picture of the first ripe peaches dangling from trees on social media with the caption, \"Peach picking is open! Come by to fill a cart or basket!\""

    "I couldn't make it out here yesterday, but it's a nice Saturday and I had the whole day free. So here I am, on my way to fill a cart of peaches. The pie I'm gonna make out of these is going to be legendary."

    "The farmers at the orchard point me toward the hill where the peaches are available for the public to pick."

    "I'm walking there when I hear her voice."

    "What is Erin doing here?"

    "I see her APPEARANCE XX. She wipes her brow with the back of a work-gloved hand, laughing at something another farmer said. I keep walking."

    e "\"Aya,\""

    "Erin calls out to me, jogging to catch up to me as I pick up my pace."

    e "\"Hi!\""

    a "\"I'm a little busy today." 

    "My words come out crabbier than I mean them."

    e "\"Wait!\"" 

    "She catches my hand and I lurch as she tugs my arm firmly. I throw my body to the side to yank my arm back, but she lets go. The lack of resistance throws me off balance, and I stumble."

    a "\"What are you doing?\""

    e "\"You've been avoiding me—\""

    a "\"Maybe, so what if I have?\""

    e "\"Wait... wait, is it because you like me? You like me!\""

    a "\"I'm not falling for a punk! You don't even know if that's why I may or may not have avoided you.\""

    e "\"Fine, then explain it to me. What are you running from?\""

    "She looks so hurt, and my heart aches at the sight. But if I don't shut this down now, she's almost certainly going to keep trying."

menu:
    "Shut this down":
        jump shut_this_down

    "Let her down gently" if kind_points >= 2:
        jump let_her_down_gently

label shut_this_down:
    a "\"I don't want to waste my time.\""

    "...is what I said. It's partly true, I am worried. But what I mean, and what I can't tell her, is that I'm afraid she might be what I want. And I don't want it to hurt when she leaves."

    "Erin's eyes mist with tears."

    e "\"Wasting time? What do you mean? Is there something wrong with me?\""

    "I wince."

    a "\"W-we're just not a good fit. You're not... you're not... actually, it's not really about you."

    "She stiffens."

    e "\"So you're just afraid.\""

    "Without another word, she turns and walks away."

    "She's right."

    jump the_rain



label let_her_down_gently:
    a "\"I'm not really available right now... I'm, uh, looking for something specific.\""

    e "\"Let me be what you want, then. Just tell me who to be and I'll be that.\""

    "That sentence hurts my heart."

    a "\"No, I'm not going to tell you who to be! That would be horrible.\""

    e "\"But you don't like who I am and I don't know why.\""

    "I do like you. Gods, I do. But I'm scared that you'll leave. You have school, you're bound to leave, and I don't think you'll come back out here when you're done."

    a "\"I... don't have a good answer.\""

    e "\"You're just afraid, aren't you?\""

    "She almost yells the words. Then she shoves her hands into her pockets and strides away, back down the hill."

    "She's right."
    
    jump the_rain
