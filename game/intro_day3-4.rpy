label intro_day3:

    n "Next morning in the motel" with dissolve
    window hide
    pause 2
    scene motelroom with dissolve
    pcthink "Wow, this really {b}is{/b} a shit-hole..."
    pcthink "Ugh... do they ever clean this room?"
    pcthink "Well, it's just for a few days... hopefully..."
    pcthink "I guess I'm going to find a nice inn with wifi to look for an apartment. I don't want to spend too much time here..."
    scene black with dissolve
    n "You head out and spend the rest of the day searching for an apartment again."
    n "As it gets dark you decide to head back to the motel and watch tv."
    scene motel_static with dissolve
    play sound "audio/tv-static.ogg" loop
    pcthink "Damn the signal sucks..."
    pcthink "...like the rest of this motel..."
    pcthink "Argh, fuck it, I'm going to bed..."
    stop sound fadeout 2
    scene black with dissolve
    n "At night" with dissolve
    window hide
    pause 2
    play sound "audio/motel_sex.ogg"
    n "*creak*{w=1}{nw}" with hpunch
    n "*creak*{w=1}{nw}" with hpunch
    n "*creak*{w=1}{nw}" with hpunch
    scene motelbedroomnight with dissolve
    pcthink "Ughh, what's this..."
    n "*creak*{w=1}{nw}" with hpunch
    n "*creak*{w=1}{nw}" with hpunch
    "Voice" "{size=-10}Ahh, yes!{/size}"
    n "*creak*{w=1}{nw}" with hpunch
    n "*creak*{w=1}{nw}" with hpunch
    n "*creak*{w=1}{nw}" with hpunch
    "Voice" "{size=-10}Ahnn, babe!!{/size}"
    pcthink "Sounds like someone is having fun..."
    scene black with dissolve
    n "You turn around and try to sleep"
    n "*creak*{w=1}{nw}" with hpunch
    n "*creak*{w=1}{nw}" with hpunch
    pc "..."
    stop sound
    n "Hours later" with dissolve
    window hide
    pause 2
    play sound "audio/bass.ogg" loop
    scene motelbedroomnight2 with dissolve
    n "*rumble*{w=0.5}{nw}" with vpunch
    n "*rumble*{w=0.5}{nw}" with vpunch
    n "*rumble*{w=0.5}{nw}" with vpunch
    pc "..."
    n "*rumble*{w=0.5}{nw}" with vpunch
    n "*rumble*{w=0.5}{nw}" with vpunch
    n "*rumble*{w=0.5}{nw}" with vpunch
    pcthink "...are you serious..."
    n "*rumble*{w=0.5}{nw}" with vpunch
    n "*rumble*{w=0.5}{nw}" with vpunch
    n "*rumble*{w=0.5}{nw}" with vpunch
    pc "GOD DAMMIT!"
    pc "Fuck it, I'm outta here!"
    stop sound
    scene black with dissolve
    play music "audio/memory.mp3" fadein 1
    n "A bit later" with dissolve
    play sound "audio/shop-chime.ogg"
    pause 2
    scene coffeehouse waitress with dissolve
    "Waitress" "Here you go."
    pc "Thanks... Keep the change."
    "Waitress" "Thanks!"
    play sound "audio/shop-chime.ogg"
    scene coffeehouseentrancecup with dissolve
    n "*slurp*"
    pcthink "Ahhhh, that's what I needed right now..."
    pc "*YAAAWN*"
    pcthink "I'm so fucking tired..."
    scene coffeehouse cup2 with dissolve
    pc "..."
    pcthink "Damn I need an apartment..."
    pcthink "Or at least a better motel..."
    pcthink "I'm not going to spend another night in there."
    pcthink "Shit..."
    scene coffeehouse cup3 with dissolve
    if introrachel:
        pcthink "Even home with [m] would be better than that..."
        pcthink "Ugh... what am I thinking?!"
    "Voice" "[pc]?"
    pc "Huh?!"
    scene coffeehouse entrance rachel1 with dissolve
    pc "...[m]?!"
    pc "What the fuck?! Are you following me?"
    m "Why would I do that?"
    pc "..."
    scene coffeehouse entrance rachel2 with dissolve
    m "God, [pc], you look awful. What happened?"
    pc "..."
    pc "Bad night..."
    if introrachel:
        m "Oh my... do you want a coffee? I still owe you one."
        scene coffeehouseentrancerachel3 with dissolve
        pc "I'm good."
        scene coffeehouse entrance rachel2 with dissolve
        m "But you don't really look like you are!"
        pc "..."
        pcthink "Shit!"
        pc "[m]?"
        m "Yes?"
        pc "Does your offer still hold?"
        m "Hm? You mean your old room?"
        pc "Yeah..."
        scene coffeehouse entrance rachel1 with dissolve
        m "Of course! Do you want to take it?"
        pc "Yeah... I guess."
    else:
        m "Oh my... do you want a coffee?"
        scene coffeehouseentrancerachel3 with dissolve
        pc "I'm good."
        scene coffeehouse entrance rachel2 with dissolve
        m "But you don't really look like you are!"
        pc "..."
        pcthink "Shit!"
        pc "I still have no apartment and all the hotels are booked because of some kind of trade fair or something..."
        m "I've heard about the trade fair... but, where did you spend the night?"
        pc "In some cheap motel... if you want to call it like that..."
        m "Was it that bad?"
        pc "Worse..."
        m "Well..."
        m "I mean... your old room is unused..."
        pc "..."
        m "I wouldn't mind if you'd take it for a few days..."
        pcthink "Shit... no way..."
        m "I know you probably don't want to come back... but it's better than any motel... and it's free of course."
        pcthink "Damn it... anything would be better than that motel... and she really seems to have changed..."
        pcthink "...just a few days won't kill me I guess, it can't get much worse anyway..."
        pc "I guess... I guess I take it."
        scene coffeehouse entrance rachel1 with dissolve
    m "Really? Great! When do you want to move in?"
    pc "Uh... as soon as possible, preferably today."
    scene coffeehouse entrance rachel4 with dissolve
    m "Today?"
    pc "Is that a problem?"
    m "N-No... not really. I just didn't expect it so soon."
    scene coffeehouse entrance rachel1 with dissolve
    m "Umm, I'll be home in about six hours. Do you remember how to get there?"
    pc "Yeah..."
    m "Okay, great! Do you need help with anything? Do you want me to pick you up?"
    pc "No, I'll just come over later."
    m "Oh, okay, good."
    m "Well, I guess I'll see you later then."
    pc "Yeah... thanks, [m]."
    m "You're welcome, Hun."
    scene black with dissolve
    stop music fadeout 2
    pc "..."
    pcthink "God, am I really going to move in there again?"
    scene black with dissolve
    n "Later that day." with dissolve
    play music mainbgm fadein 1
    window hide
    pause 2
    n "You arrive at your old home and spend a few moments thinking about the past."
    n "Still doubting your decision to come back, you eventually knock at the door."
    play sound "audio/knock-door1.ogg"
    n "*Knock* *knock*"
    n "Almost instantly the door opens."
    scene home welcome rachel entrance1 with dissolve
    m "Heyyy, look who found [hisher] way home."
    scene home welcome rachel entrance1 hug with dissolve
    m "Welcome back [pc]."
    pcthink "What the..."
    pc "Uh... thanks."
    scene home welcome rachel entrance2 with dissolve
    m "Huh? [pc], where is all your stuff? Don't tell me you changed your mind!?"
    pc "No, that's not it. Most of my stuff will be shipped in a few days. I have all I need in my bag."
    scene home welcome rachel entrance3 with dissolve
    m "Just a bag? Wow, I wouldn't survive a day with just a bag."
    if pcgender == "man":
        pc "Guess sometimes clichés are true..."
    else:
        pc "Guess that's normal for most women... I'm just not like that."
    scene home welcome rachel ellie entrance with dissolve
    m "Haha, true!"
    pc "Huh?"
    scene home welcome rachel ellie entrance1 with dissolve
    pc "Is that..."
    m "Hm?"
    m "Oh, hey [e]. Look who's here!"
    scene home welcome ellie closeup2 with dissolve
    pcthink "Isn't this..."
    scene 2walk close memory with dissolve
    pause
    scene home welcome ellie closeup2 with dissolve
    pcthink "Fuck, that was her!?"
    pcthink "...and I didn't recognize her, shit!"
    scene home welcome rachel ellie entrance2 with dissolve
    m "Why don't you come closer [e]?"
    scene home welcome rachel ellie entrance3 with dissolve
    m "...and there she goes."
    scene home welcome rachel entrance ellie gone with dissolve
    m "I guess I should have told you..."
    pc "Huh? Told me what?"
    scene home welcome rachel entrance3 with dissolve
    m "Um.. well, why don't you come in? Let's sit down in the living room and I'll tell you everything."
    pc "..."
    scene black with dissolve
    stop music fadeout 2
    n "You follow her to the living room and take a seat."
    n "Hesitantly she starts to explain what happened after you moved out years ago."
    n "Apparently [e] was really sad and couldn't understand why you left all of a sudden."
    n "A few months later, [e] went missing for a few days and was found at night, walking through the city like a ghost."
    n "Despite the fact that [e] was unharmed physically, something had happened to her mind."
    n "She was unresponsive and didn't even recognize her mother at first."
    n "No one knows what happened that day and since then, she has never spoken a word to anybody."
    scene livingroom rachel talk1 with dissolve
    pc "..."
    pc "Wow, that's... fucked..."
    pc "I'm sorry, I didn't know..."
    scene livingroom rachel talk2 with dissolve
    m "How could you?"
    pc "..."
    pc "I thought she's a totally normal girl..."
    m "Well, she is a normal girl. She's just not talking and..."
    pc "And? There is more?"
    scene livingroom rachel talk1 with dissolve
    m "...sometimes it is like she is in another world, but aside from that, she is like any other girl her age."
    pc "In another world?"
    scene livingroom rachel talk1 with dissolve
    m "Yes, um... how can I explain it..."
    scene livingroom rachel talk2 with dissolve
    m "Sometimes she is totally absorbed in something she's doing, sometimes so much that she doesn't respond, or even notice that somebody is talking to her."
    pc "Maybe she is just ignoring you?"
    m "No, that's not it. She completely blocks everything out in such moments."
    pc "..."
    pc "Damn, if I had known..."
    m "You couldn't have..."
    m "...and even if you knew, there is nothing you possibly could have done to help her. In fact, by now I know that nobody can."
    pc "What do you mean?"
    m "Well, over the years I've talked to many doctors, went to many psychologists..."
    scene livingroom rachel talk1 with dissolve
    m "Nobody could help her and nobody knows what's causing her condition."
    pc "..."
    pc "I can't believe this. There must be something I can do..."
    scene livingroom rachel talk3 with dissolve
    m "Maybe it'll help her to know that you are back, but I don't think she will ever come back to her normal self."
    pc "I see... you've given up on her already..."
    scene livingroom rachel talk2 with dissolve
    m "No, that's not it, [pc]. But she has been like this for years now and I just don't know what else I can do anymore..."
    scene livingroom rachel talk1 with dissolve
    pc "..."
    m "..."
    pcthink "I guess she really did try a lot to help [e]. She's her daughter after all and she was always a good mom to her... at least..."
    scene livingroom rachel talk3 with dissolve
    m "Anyway, I hope you will still be staying with us, after hearing all this. Will you?"
    pc "Sure... at least until I find a new apartment."
    scene livingroom rachel talk4 with dissolve
    m "That's good. Thank you [pc]. I wasn't sure..."
    pcthink "Why is she thanking me for this?"
    pc "Knowing this, I have even more reasons to stay now..."
    m "..."
    m "So..."
    m "I have prepared your old room for you, but I fear there is not much of your old stuff left. We used it as a guest room after you moved out."
    pc "That's no problem. I didn't expect much to be left anyway."
    pcthink "She probably threw everything on the junk pile right after I was out of the door..."
    m "Well then, why don't you make yourself at home and we'll see each other at dinner? I guess you have a lot to think about right now."
    pc "Sure..."
    pcthink "Thats actually true..."
    scene black with dissolve
    pcthink "I wonder what my room looks like right now."
    pcthink "Actually the whole house looks a lot different."
    scene pcroom with dissolve
    pcthink "Whoa, she didn't lie, there is not much left..."
    pcthink "I don't see anything that belongs to me here. The room looks completely different."
    pcthink "Even the couch is new."
    scene black with dissolve
    scene pcroomsitonchair with dissolve
    n "You sit down on the chair and exhale."
    n "Your eyes are getting heavy immediately."
    scene pcroomsitonchairtired1 with dissolve
    pcthink "Shit, I didn't realize that I'm so tired."
    pcthink "But it's no wonder since I didn't get much sleep last night."
    scene pcroomsitonchairtired2 with dissolve
    pc "..."
    pcthink "...what happened to [e] gives me the creeps..."
    scene pcroomsitonchairtired3 with dissolve
    pcthink "If I'd just been there..."
    scene black with dissolve
    n "You fall asleep."
    scene black with dissolve
    n "Home Day 0" with dissolve
    #achievement
    $achievement.grant("Achievement_home")
    init: 
        $achievement.register("Achievement_home")
    $achievement.sync()
    ###########
    window hide
    pause 2
    jump day0Morning