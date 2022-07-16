label intro_day2:
    scene black
    n "At night" with dissolve
    window hide
    pause 2
    n "..."
    play music "audio/BadDream.mp3"
    scene dream_01 at dream with dissolve
    "Loud Voice" "I HAVE SEEN IT! DON'T YOU DARE LIE TO ME AGAIN!" with vpunch
    "Female Voice" "I'm not lying, I didn't do anything. He was just talking to me!"
    "Loud Voice" "I FUCKIN' TOLD YOU WHAT'S GOIN TO HAPPEN, YOU FUCKIN' SLUT!"
    "Female Voice" "No, please. I swear I didn't..."
    "Loud Voice" "SHUT THE FUCK UP, SLUT!"
    play sound "audio/slap1.ogg"
    "*SLAP*" with hpunch
    "Female Voice" "Ahh... n-no, p-please..."
    play sound "audio/slap1.ogg"
    "*SLAP*" with hpunch
    "*wimpering*"
    "Female Voice" "Please..."
    "Loud Voice" "I TOLD YOU TO SHUT UP SLUT!"
    play sound "audio/slap3.ogg"
    "*SMACK*" with hpunch
    "Female Voice" "ACK"
    "*wimpering*"
    "Female Voice" "I'm sorry... I'm sorry..."
    "Loud Voice" "Yeah, you better be... now, suck it!"
    "*wimpering*"
    "Loud Voice" "I TOLD YOU TO SUCK!"
    "Female Voice" "Yes, yes, I'm sorry..."
    "Female Voice" "Unn..."
    play sound "audio/knock-door1.ogg"
    n "*KNOCK* *KNOCK*"
    pc "D-Dad? What's going on, why are you screaming?"
    "Loud Voice" "FUCK!"
    play sound "audio/door-opening.ogg"
    n "The door opens slightly."
    "Dad" "Hey, it's okay. [m] and I just had a small argument. Nothing special. Go to bed [boygirl]."
    pc "Um... Dad, [m] is bleeding..."
    "Dad" "It's okay, she was too stupid to watch where she was going and stumbled over something."
    "Dad" "It's just a scratch, she's fine. Go to bed now."
    pc "Oh... okay."
    play sound "audio/door-closing.ogg"
    n "He closes the door."
    n "..."
    "Dad" "{size=-10}Are you happy now? You woke [himher] up with your stupid screaming!{/size}"
    m "{size=-10}...I'm sorry...{/size}"
    "Dad" "{size=-10}Stupid bitch. Turn around!{/size}"
    if uVersion == 0:
        m "{size=-10}B-but I'm not on the pill, you know that!?{/size}"
    else:
        m "{size=-10}P-Please, it still hurts...{/size}"
    "Dad" "SHUT UP! I don't fucking care!"
    n "*wimpering*"
    n "..."
    stop music fadeout 2
    scene hotelroomwakeup with dissolve
    pc "Shit..."
    scene hotelroomwakeup2 with dissolve
    pcthink "Damn, that was a heavy dream..."
    pcthink "..."
    pcthink "Did that really happen?"
    pcthink "...why am I remembering this shit now..."
    pcthink "..."
    pcthink "...I guess she really treated me better than that asshole treated her..."
    pcthink ".."
    pcthink "..."
    pcthink "...."
    pcthink "But still... I can't forgive her..."
    pcthink ".."
    pcthink "..."
    pcthink "...."
    pcthink "I need a shower..."
    scene black with slowdissolve
    play music "audio/memory.mp3" fadein 2
    n "A few minutes later." with dissolve
    window hide
    pause 3
    n "You hear the phone in your room ringing."
    scene hotelroom roomphone1 with dissolve
    pc "Yeah?"
    "Voice" "Hello [mrms] [pcsure], this is the reception desk. We have a call from a woman named [m], who wants to talk to you."
    if introrachel:
        pcthink "[m]?! What does she want now?"
    else:
        pcthink "[m]?! How the fuck did she get the number?"
    "Voice" "Do you accept the call [mrms] [pcsure]?"
    menu:
        "No way, and tell her to never call again!":
            "Voice" "O-Oh... okay, I will tell her..."
            scene hotelroom roomphone3 with dissolve
            play sound "audio/hangup.ogg"
            pcthink "Fucking hell, I can't believe it. Why can't she just let me be..."
            jump intro_day2_2
        "...yeah.":
            pass
    "Voice" "Okay, one moment please..."
    n "..."
    m "[pc], are you there?"
    pc "...yes."
    m "..."
    if introrachel:
        m "[pc] I'm sorry for yesterday, I shouldn't have left so suddenly, but I..."
        scene hotelroom roomphone2 with dissolve
        pc "Don't worry about it."
        pcthink "Shit, why am I being nice to her?"
        m "Really?! Thanks [pc]."
        m "But still, I didn't even pay my bill. Did you..."
        pc "Yeah, I paid it..."
        m "Thank you, Hun. I'll make it up to you."
        pcthink "Did she just call me \"Hun\"?"
        pc "..."
        m "So, do you have a new apartment already?"
    else:
        $ introrachel = True
        m "I... wanted to say sorry for yesterday, I shouldn't have blindsided you like that..."
        pc "..."
        m "Our little meeting probably brought back a lot of bad memories..."
        pc "..."
        m "..."
        pc "Is that all?"
        m "Uhm... I... Oh I wanted to ask, do you have a new apartment already?"
    pc "No I don't..."
    m "It's a shame, I've heard the burnt down building had really nice apartments."
    pc "Wait! How do you know that I had my apartment there?"
    m "Um... you did? I didn't know. The fire was on TV. Didn't you see it?"
    pc "Uh... no, I didn't watch TV lately."
    pcthink "I guess that makes sense... She can't really know that it was my apartment that burned down."
    m "Well, I was thinking... If you need somewhere to stay... you could have your old room..."
    pcthink "What the fuck???"
    m "..."
    m "If you want."
    pcthink "Does she really think I would want to live with her again?"
    pc "I won't need it."
    m "Oh okay, I thought so. I just wanted to let you know."
    pc "Yeah, thanks..."
    m "...I bet your sister would have been happy to see you again."
    pc "Ellie..."
    m "Oh, so you still remember her name?"
    pc "Very funny, [m]."
    m "I'm sorry, [pc]."
    if uVersion == 1:
        pc "...and by the way she is not my sister..." 
        m "Hum... Of course not, but you always treated each other like brother and sister..."
        pcthink "Yeah, I guess we where really close back then..."
    m "She was really sad when you left, you know."
    pc "..."
    pc "...and whose fault was that?"
    m "..."
    pc "Is there something else you wanted to talk about?"
    m "N-No, I... just wanted to apologize for yesterday and tell you that you're welcome home anytime."
    pc "Yeah, thanks. See ya [m]."
    m "Goodbye [pc]."
    scene hotelroom roomphone3 with dissolve
    play sound "audio/hangup.ogg"
    n "*Click*"
    pc "Humph... as if I would ever go back there..."
    pc "..."
    pcthink "[e]..."
    pcthink "I wonder how she's been."
    pcthink "She was so young back then."
    pcthink "She must be an adult now... uhh... I think..."
    pcthink "Shit, how old is she?"
    pc "Argh, I don't remember..."
label intro_day2_2:
    pcthink "Anyway, I still need a new apartment so I better start looking again."
    stop music fadeout 2
    scene black with dissolve
    n "You spend some time looking for a new apartment."
    pcthink "Damn, I can't believe there are no fucking apartments available in this town..."
    pc "Shit..."
    pcthink "I guess I'd better rent the room for a little while longer."
    n "You head down to the reception."
    scene hotel reception1 with dissolve
    pause
    scene hotel reception2 with dissolve
    pc "Hey I'd like to have the room for a bit longer."
    scene hotel reception3 with dissolve
    "Receptionist" "Oh, hello [mrms] [pcsure], I'm sorry, but that's not possible at the moment. We are awaiting a group of guests that arrive tomorrow."
    pc "Okay, no problem. I'm not picky, I'd take any other room."
    "Receptionist" "Sorry [mrms] [pcsure], but in fact, all rooms are booked..."
    pc "What?! Every single room?"
    "Receptionist" "Yes, there is an international trade fair over the next few weeks, so we are awaiting many guests."
    pc "Ugh... shit. But I really need a room."
    "Receptionist" "I'm sorry, [mrms] [pcsure]. I guess you have to book a room somewhere else, but it's most likely that all of the major hotels are fully booked."
    "Receptionist" "You could try some of the smaller motels around town. Maybe some of them still have rooms."
    pc "Yeah, I guess a motel will do..."
    scene black with dissolve
    n "The moment you're about to leave, a man looking like a manager shows up and starts to argue with the receptionist."
    scene hotel reception manager2 with dissolve
    "Manager" "[r], what the hell!? How many times do I have to tell you that you have to wear a bra?"
    r "I-I'm sorry, sir."
    scene hotel reception manager1 with dissolve
    "Manager" "You're sorry?! [r] you shouldn't be sorry, you should be ashamed!"
    "Manager" "We have standards in this hotel, [r]! Your shameful behavior already got the attention of some of our guests. That's not acceptable."
    r "I'm sorry, sir. I-It's just that the technician still didn't fix the AC and it's so hot in here."
    "Manager" "That's no excuse for dressing like a whore!"
    pcthink "Whoa, that's a bit harsh..."
    r "I'm sorry, sir..."
    "Manager" "I'm tired of your excuses, [r]. I've had enough of this now. Get your stuff and leave."
    r "B-but sir! Please, I-I need the money, you can't just throw me out!?"
    "Manager" "Don't make a scene now, it's your own fault, I've given you enough warnings!"
    r "I'm sorry..."
    "Manager" "I'll send George over to take care of the reception and I expect you to be gone in half an hour at the latest!"
    scene hotel reception manager3 with dissolve
    r "Yes, sir..."
    pcthink "Damn, seems like I'm not the only one having a bad day..."
    scene black with dissolve
    n "You head back to your room."
    pcthink "Maybe I should've said something..."
    pcthink "..."
    n "You pick up your smartphone and browse through the internet, looking for motels in town."
    pcthink "... damn she was right. Almost everything is fully booked..."
    n "After a while you book a room in one of the few available motels."
    pcthink "Not much choice here... I hope it's not a shit-hole."
    scene black with dissolve
    
    jump intro_day3