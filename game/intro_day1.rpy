label intro_day1:
    scene black with fade
    n "Next Day" with dissolve
    n "You're woken up by the sound of your mobile phone."
    scene hotelroomwakeup with dissolve
    pc "Uhh..."
    scene hotelroomwakeup2 with dissolve
    pc "What time is it?"
    scene hotelroomwakeupphone1 with dissolve
    pc "Who the hell is calling so early..."
    scene hotelroomwakeupphone2 with dissolve
    pc "Yeah?"
    "Voice" "Hello [mrms] [pcsure], this is Maggy Shelter. I'm sorry but I have bad news for you."
    pcthink "Ah, Maggy, the office secretary from the rental company."
    pcthink "She's obviously about to tell me about the apartment. She doesn't know I was there..."
    pc "Hey Maggy. I know about the fire already."
    "Maggy" "You know that the apartment burned down?"
    pc "Yeah, I arrived yesterday and wanted to have a look at the apartment."
    "Maggy" "Oh no, that must have been a shock to you."
    pc "It was quite a surprise..."
    "Maggy" "I'm so sorry [mrms] [pcsure]. Do you have somewhere else to stay?"
    pc "Yeah, I have a hotel room for a few days until my stuff arrives."
    "Maggy" "That's good to hear."
    pc "So... what about a replacement? Are there any other apartments?"
    "Maggy" "No, I'm sorry [mrms] [pcsure], there are no apartments free at the moment."
    "Maggy" "There is not much I can do, but you can be sure to get your money back and I promise to call you as soon as we have another apartment for you."
    pc "That's nice and all, but I can't go back to my old flat and I cannot live in a hotel forever. Don't you know anywhere else I could get an apartment, Maggy?"
    "Maggy" "..."
    "Maggy" "I... I might... but I have to make a few calls first."
    pc "Great! Thanks Maggy. Really!"
    "Maggy" "Don't celebrate just yet. I can't promise anything. I'll try my best, but you should also have a look around for yourself [mrms] [pcsure]."
    pc "Of course, but at least you've given me some hope."
    "Maggy" "Okay then, I will call you as soon as I know something [mrms] [pcsure]."
    pc "Thanks Maggy, and call me [pc]."
    "Maggy" "Good bye [mrms].... ahem, [pc]."
    pc "Bye Maggy."
    pcthink "Damn that girl has a nice voice..."
    pcthink "I wonder what she looks like."
    pcthink "Anyway, she's right. I better get up and have look for another apartment myself."
    scene black with dissolve
    play music mainbgm fadein 1
    n "You get up, take a quick shower and spend a few hours browsing the web for an apartment."
    n "You make some phone calls for interesting apartment offers, but have no luck."
    pc "Damn, is every apartment in this town gone?!" 
    n "You try a few more times with no luck."
    n "The moment you're about to give up, you get another call."
    pcthink "Huh? Must be Maggy again..."
    scene hotelroomphoneclothed2 with dissolve
    pc "Hey Maggy. Please tell me something positive."
    "Maggy" "Hey [mrms]..[pc]. Yes I might have something for you, but you have to hurry."
    "Maggy" "It's an apartment in a nice part of town and it won't take long before it's gone again."
    scene hotelroomphoneclothed1 with dissolve
    pc "Great! Thanks Maggy. You just saved my day!"
    "Maggy" "Haha, glad to help."
    scene black with dissolve
    n "You save the address Maggy gives you in your smartphone and immediately go on your way after saying your goodbyes."
    stop music fadeout 2
    scene black with dissolve
    n "Half an hour later" with dissolve
    scene sold apartment1 with dissolve
    pcthink "Okay, this is the address... looks okay I guess... hmm, I like the annex."
    scene sold apartment2 with dissolve
    pcthink "Shit, this doesn't look good..."
    scene sold apartment3_2 with dissolve
    pc "Uh, hey I'm here for the apartment."
    scene sold apartment3 with dissolve
    "Broker" "I'm sorry [mrms].."
    scene sold apartment3_2 with dissolve
    pc "[pcsure]."
    scene sold apartment3 with dissolve
    "Broker" "[pcsure]? Hum... I don't remember your name, did we have an appointment?"
    scene sold apartment3_2 with dissolve
    pc "No, a friend gave me the address."
    scene sold apartment4 with dissolve
    if pcgender == "man":
        "Guy" "You're too late, man."
    else:
        "Guy" "You're too late. It's sold!"
    scene sold apartment3 with dissolve
    "Broker" "Well I'm sorry [mrms] [pcsure]. This lovely couple here just closed the deal on this apartment."
    pcthink "Shit, this sucks... all the haste for nothing."
    pcthink "Looks like I have to continue searching..."
    scene black with dissolve
    play music mainbgm fadein 1
    pcthink "Well I guess I'll head back to the hotel..."
    pc "*stomach rumble*"
    pcthink "...or get a snack first."
    n "On your way back you stop for a small snack."
    scene getsnack with dissolve
    pause
    "Random Guy" "Oh and don't forget the other Ramen, and the Negi."
    "Girl" "Of course!"
    pcthink "..."
    scene getsnack rachel with dissolve
    pcthink "What the... is that... [m]?"
    pcthink "Fuck!"
    stop music fadeout 2
    play music "audio/lightsteps.mp3" fadein 3
    scene getsnack rachel2 with dissolve
    pcthink "This can't be fucking true!"
    pcthink "The day got even worse just by seeing her... The one person I never wanted to see again. One of the reasons why I left this town."
    pcthink "I’ll just pretend I haven’t seen her and leave right now..."
    pcthink "I might lose it and slap her right in the face if I stay..."
    scene black with dissolve
    n "You quickly turn in the opposite direction and hope she doesn't recognise you after all these years."
    m "[pc]? Is that you?" with vpunch
    pcthink "Fuck..."
    scene getsnack leave rachel1 with dissolve
    pc "Uh... hey [m]."
    m "Oh my god, It's really you, isn't it?!"
    scene getsnack leave rachel7 with dissolve
    m "You didn't just pretend you didn't see me, did you?"
    pc "Uhh, well..."
    scene getsnack leave rachel2 with dissolve
    m "Ahaha! It's okay [pc]..."
    m "I don't blame you."
    pcthink "Why is she so friendly?"
    m "To be honest, I didn't expect to see you ever again."
    pc "..."
    pcthink "I would’ve preferred it that way..."
    scene getsnack leave rachel3 with dissolve
    m "I guess it must be fate then."
    pcthink "Or bad luck. I seem to have a lot of it lately..."
    m "What brings you back? Are you visiting some old friends?"
    pc "A new job..."
    m "Really?! Here in town?"
    pc "Yeah..."
    pcthink "Shit, why did I tell her about that..."
    m "Wow, that's great news!"
    pcthink "...and why is she acting like she is happy to see me?"
    m "I guess we'll meet more often then."
    pcthink "God please no!"
    pc "..."
    m "..."
    scene getsnack leave rachel4 with dissolve
    m "Listen... I know you must still be mad at me, but..."
    pcthink "Mad? I fucking hate this bitch!"
    m "Things have changed... I have changed..."
    pcthink "Yeah, as if..."
    scene getsnack leave rachel5 with dissolve
    m "I really wanted to talk to you and apologize for... well, everything."
    pcthink "Fuck..."
    pc "Are you serious? Now? After all these years?"
    scene getsnack leave rachel4 with dissolve
    m "I know, I know..."
    scene getsnack leave rachel6 with dissolve
    m "I sent you a letter a while ago, but you probably never read it... did you?"
    pc "A letter?"
    pcthink "Now that she mentions it, I got a letter a few years ago... and burned it instantly when I saw her name on it..."
    pcthink "I still don't know how she got my address. I stayed away from every social media platform. Deleted every account she might have known about and still, she somehow managed to find my real life address..."
    pc "Yeah, I didn't read it..."
    scene getsnack leave rachel5 with dissolve
    m "But you can't tell me I didn't try, right?"
    pcthink "As if a letter would change anything."
    m "..."
    pc "..."
    scene getsnack leave rachel6 with dissolve
    m "Umm... well, I have a bit of time right now. Don't you think we could have a cup of coffee together and talk a bit at least... after all this time..."
    pcthink "Tch, seriously?..."
    pc "Sorry, I don't have the time right now..."
    m "Really? Or do you just not want to talk to me?"
    pcthink "Ugh...she's so... different."
    pcthink "...is she just acting?"
    m "...hm?"
    pcthink  "There is definitely something different about her..."
    m "I mean, it's okay if you don't want to... I would understand."
    menu:
        "Go with her.":
            pass
        "Just leave.":
            $ introrachel = False
            scene black with dissolve
            stop music fadeout 2
            n "You turn around and leave."
            pcthink "Fuck that bitch..."
            scene black with slowdissolve
            jump intro_day1_2
    pc "Ugh... okay, fine... I guess I have a few minutes..."
    scene getsnack leave rachel7 with dissolve
    m "Great!"
    m "There is a nice small café over there. I bet you'll love it."
    scene black with dissolve
    stop music fadeout 2
    pcthink "Damn, I hope I won't regret it..."
    n "A bit later" with dissolve
    play music "audio/memory.mp3" fadein 3
    pause 2
    scene coffeehouse rachel0 with dissolve
    m "...and you moved all the way back just for that job?"
    pc "Yeah..."
    scene coffeehouse rachel1 with dissolve
    m "Well I mean, getting more money and having a lot more free time is good..."
    scene coffeehouse rachel0 with dissolve
    m "...but I don't know. I don't think I could do that, leaving everything behind..."
    m "But I guess it's easier when you have done it once before..."
    scene coffeehouse rachel1 with dissolve
    pc "..."
    pc "[m], why did you really want to talk to me?"
    scene coffeehouse rachel0_1 with dissolve
    m "Well, we haven't seen each other for a while have we?"
    scene coffeehouse rachel1_1 with dissolve
    pc "Come on [m], I know that's not the real reason."
    scene coffeehouse rachel2 with dissolve
    m "..."
    m "[pc] I..."
    scene coffeehouse rachel3 with dissolve
    m "I meant it when I said I'm sorry."
    pc "Yeah, sure..."
    scene coffeehouse rachel3_2 with dissolve
    m "Listen [pc], I know I wasn't the best mom you could think of..."
    pc "You are NOT my mom. Not even my stepmom. You're just some woman who used to live with my dad, you weren't even married." with hpunch
    scene coffeehouse rachel2 with dissolve
    m "Yes, that's true, but still... "
    scene coffeehouse rachel4 with dissolve
    m "I was supposed to take care of you, raise you, be your second mother..."
    scene coffeehouse rachel4_2 with dissolve
    m "And I failed miserably."
    pc "Tch... That's a BIG understatement."
    scene coffeehouse rachel2 with dissolve
    m "..."
    pc "..."
    scene coffeehouse rachel4 with dissolve
    m "You know what your dad did to me, don't you?!"
    pc "..."
    m "I know he kept you away from it, but you must have noticed!"
    scene coffeehouse rachel4_2 with dissolve
    pc "... that... doesn't give you the right to treat me the same way..."
    scene coffeehouse rachel3 with dissolve
    m "Oh no, I didn't! What your dad did, was way beyond that!"
    scene coffeehouse rachel5 with dissolve
    m "But still..."
    m "You are right..."
    m "I hated you because you were his [ds]... and... that was wrong."
    scene coffeehouse rachel4 with dissolve
    m "You were never like him..."
    pc "..."
    m "..."
    m "I... better leave now..."
    scene coffeehouse rachelrun with hpunch
    m "I'm sorry [pc]..."
    scene coffeehouse rachel6 with dissolve
    n "She runs off with tears in her eyes."
    pc ".."
    pc "..."
    pc "...."
    pc "Fuck!"
    pcthink "Why do {i}I{/i} feel bad now?!"
    pcthink "She's the one who treated me like shit back then..."
    scene coffeehouse rachel7 with dissolve
    pc "..."
    scene black with dissolve
    stop music fadeout 2
    n "You pay the bill for both of you and head back to the hotel."

label intro_day1_2:
    scene hotelroom with dissolve
    pcthink "Damn what a fucked up day..."
    pcthink "I'm starting to regret my decision to come back..."
    pcthink "...hopefully I'll have more luck tomorrow..."
    pcthink "It's getting dark already..."
    pcthink "I think I'm going to take a shower and just go to bed for now..."
    scene black with dissolve
    n "You take a shower and go to bed, still thinking about today's events."
    
    jump intro_day2