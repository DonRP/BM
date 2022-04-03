######### MC
label day0Morning:
    play music mainbgm fadein 1
    scene pcroomsleeponchairwakeup1 with dissolve
    pc "YAAAHHWN..."
    pcthink "Gawd, I needed that sleep..."
    scene pcroomsleeponchairwakeup2 with dissolve
    pcthink "Huh?! Who put the blanket on me?"
    pcthink "...and took my shoes off?"
    scene pcroomsleeponchairwakeup3 with dissolve
    scene pcroomsleeponchairwakeup3_2 with hpunch
    pcthink "Uhh ouch, my back..."
    scene pcroomsleeponchairwakeup3 with dissolve
    pcthink "Argh... wasn't the best idea to fall asleep in a chair!"
    scene black with dissolve
    n "You struggle to get up from the chair, but eventually make it."
    scene pcroom with dissolve
    pcthink "Ugh... So this is how old people feel."
    pcthink "I better try not to sit in that chair again when I'm tired..."
    pc "..."
    pcthink "...back home after all these years..."
    pcthink "I'll have to have a look for [e] later..."
    pcthink "But first things first. I really need to use the bathroom!"
    $ SErachelBathroomDay0 = True
    $ storyEvent = True
    jump hall

label childRoomDay0:
    scene childroom front with dissolve
    pc "Hey [e], [m] told me to..."
    pcthink "Huh? She's not here?"
    pc "..."
    pcthink "Maybe she is in the bathroom?"
    scene hallbathroomdoor with dissolve
    pcthink "Hmm... the door is not locked and there is nothing to hear."
    scene bathroom with dissolve
    pcthink "No one here..."
    scene hall_back_idle with dissolve
    pcthink "Okay, that's weird... did I miss her?"
    pcthink "Maybe in the Livingroom?"
    scene livingroom with dissolve
    pcthink "Nope, not here either... where is she?"
    $ SEsearchforsis = True
    $ storyEvent = True
    $ actionsUsed = 1
    call dateTime from _call_dateTime_4
    scene home_hall_idle with dissolve
    call screen map_home_hall

label kitchenBreakfastDay0:
    n "A bit later" with dissolve
    window hide
    pause 2
    scene livingroom diningtable eandm with dissolve
    m "Oh, so you only need to go to work every few days?"
    pc "Yeah, you could say I'm an employed freelancer."
    pcthink "What's up with [e]?"
    m "Sounds interesting, but does this job really pay that well?"
    pc "The pay is okay, I manage..."
    pcthink "...actually more than okay, but why would I tell her that..."
    m "Well, if you like your job, who am I to judge. But if you ever need something, just tell me, okay?"
    pcthink "Not gonna happen..."
    pc "Don't worry, I won't need anything."
    m "Alright..."
    scene livingroom diningtable elookatm with dissolve
    m "[e], don't you want to eat something?"
    scene livingroom diningtable eeat with dissolve
    m "Alright, I'm going to make myself ready for work."
    scene livingroom diningtable ellie eat with dissolve
    m "[e] eat up, okay?"
    scene livingroom dinigtable ellie look with dissolve
    pcthink "Ugh... she's doing it again..."
    pause
    pc "Err... what's up [e]?"
    e "..."
    pcthink "Damn, she doesn't talk. I keep forgetting that..."
    pc "..."
    e "..."
    pc "Uh, hey I'm sorry I didn't recognize you back in the city..."
    e "..."
    pcthink "This is awkward..."
    pcthink "Why is she staring at me like this?!"
    pcthink "It's almost creepy..."
    scene livingroom dinigtable ellie surprised with dissolve
    m "[e], get ready for school, we need to leave in five minutes!"
    scene livingroom dinigtable with dissolve
    scene black with dissolve
    n "She jumps up immediately and leaves the room."
    pcthink "Phew... thanks [m]..."
    n "A few minutes later" with dissolve
    window hide
    pause 2
    scene pcroomsitonchair2 with dissolve
    pcthink "Damn I don't know how to handle the situation with [e]..."
    pcthink "But at least she doesn't seem to be mad at me..."
    pcthink "Maybe I shouldn't think too much about it."
    pcthink "I mean, she's just a normal girl...right?"
    pcthink "Aside from not talking..."
    pcthink "...and staring at me like a creep..."
    pcthink "...and sleeping in my bed..."
    pcthink "Ugh... don't think about it, she's just a normal girl! No sweat!"
    play sound "audio/knock-door1.ogg"
    n "*KNOCK* *KNOCK"
    scene pcroom sitonchair door mande with dissolve
    m "We are leaving, will you manage?"
    pc "Yeah, sure."
    pcthink "Damn, [e] looks like she's trying to seduce someone..."
    m "Food is in the fridge, take whatever you want, okay?"
    pc "Yeah, okay. Thanks."
    m "See you later, Hun."
    pc "Later..."
    scene pcroom sitonchair door with dissolve
    pcthink "What's up with that \"Hun\" thing of hers? She never called me that back then..."
    scene black with dissolve
    pcthink "Anyway, time to relax..."
    scene pcroomsitonchair2 with dissolve
    $ actionsUsed = 1
    call dateTime from _call_dateTime_3
    jump whatToDoHome
    
label pcDream1:
    n "You lay down in your bed."
    scene pcroomlaydown with dissolve
    pcthink "It feels so weird to be back..."
    pcthink "...seeing [e] and [m] again..."
    pcthink "[e] surely has grown up, but... actually I thought she should be a bit older by now."
    pcthink "How old is she anyway?"
    pcthink "Uhh..."
    pcthink "Shit, I can't remember..."
    pcthink "..."
    pcthink "...and [m]... did she really change?"
    pcthink "Something is bugging me about her... I don't trust her."
    pcthink "I bet she's... *yaaawn* ...hiding something..."
    scene black with dissolve
    stop music fadeout 2
    n "You close your eyes and fall asleep."
    pause 3
    n "In your dreams" with dissolve
    play music "audio/BadDream.mp3"
    scene dream_01 at dream with dissolve
    m "Welcome home [e]."
    e "Hello, Mommy."
    m "Wait a minute, show me your face..."
    e "Um, it's nothing, Mommy. I just..."
    m "[bpc]! WHAT DID YOU DO TO HER?!"
    pc "Huh? I didn't do anything!"
    e "No. Mommy, it wasn't..."
    m "Shut up [e]! [pc] what the hell?!"
    pc "I-I didn't do anything, I swear! There were some guys bullying her and I..."
    m "SHUT UP!"
    m "I don't want to hear any excuses from you! You stupid [ds] of an asshole!"
    e "Mommy, please, [heshe] helped me!"
    m "Go to your room [pc]! I don't want to see you leave your room until you go to school tomorrow!"
    pc "..."
    stop music fadeout 2
    scene pcroomwakeup with dissolve
    pc "Uhh..."
    pcthink "Shit... the memories keep coming back..."
    scene pcroomwakeup1 with dissolve
    pcthink "I wish I could just keep them locked somewhere in the back of my brain."
    pcthink "..."
    pcthink "Damn, it really doesn't help to wallow in self-pity..."
    pcthink "I better get up and do something useful..."
    pcthink "...well, or whatever."
    $ actionsUsed = 5
    call dateTime from _call_dateTime_5
    scene pcroom with dissolve
    jump jadaFirstMeet
    

label wakeupDay1:
    $ SEpcDay1Morning = False
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    m "[pc], are you awake?"
    pc "..."
    play sound "audio/knock-door2.ogg"
    n "*Knock* *Knock* *Knock*"
    m "[pc]?"
    pc "Uhhh..."
    scene pcroomwakeup with dissolve
    pc "Uhnnn... yeah..."
    scene pcroomwakeuprachel1st with dissolve
    m "I can't find [e], do you..."
    scene pcroomwakeuprachel2nd with dissolve
    m "What the?! [pc]?"
    pc "Huh?"
    scene black with dissolve
    n "You turn around."
    scene pcroomwakeupellie1st with dissolve
    pause 0.5
    scene pcroomwakeupfall with hpunch
    pc "WHOA!!!"
    scene pcroomwakeupellielookdownsurprise with dissolve
    pc "What the hell are you doing here, [e]?!"
    m "Hahaha..."
    scene pcroom wakeup rachel laugh with dissolve
    play music mainbgm fadein 1
    m "I guess you didn't know she was here either."
    m "Looks like someone wanted to cuddle a bit with her big [bs]."
    scene pcroomwakeupellielookatrachel with dissolve
    m "But, [e], you really shouldn't sneak into your [bs]'s room like this."
    scene pcroomwakeupellielookdown with dissolve
    pause 0
    scene pcroomwakeupelliegetup with dissolve
    pause 0.5
    scene pcroomwakeupelliejumplanding with dissolve
    n "[e] jumps over you and leaves the room."
    scene pcroom wakeup pcleanup with dissolve
    if pcgender == "man":
        m "By the way, you should start wearing some pants in bed."
    else:
        m "By the way, you should start wearing pyjamas in bed."
    pc "Huh?!"
    scene pcroomwakeupexposed with dissolve
    pause 0.8
    scene pcroomwakeupexposedhide with vpunch
    pc "FUCK!"
    m "Hahaha, don't worry, Hun. I have seen that before... even though, you've obviously become a [pcgender]..."
    scene pcroom wakeup pcleanup with dissolve
    pc "Yeah, could you leave the room please!"
    m "Hahaha, of course, I'm sorry honey."
    scene pcroom wakeup pcleanup doorclosed with dissolve
    pcthink "Shit! I was so surprised by [e] that I didn't think about sleeping naked..."
    pcthink "That was embarassing..."
    if pcgender == "man":
        pcthink "Especially with that morning wood..."
        pcthink "Wait, did [e] see that too?"
    pcthink "Damn it..."
    scene black with dissolve
    n "You get dressed and take a quick shower."
    n "After breakfast, [m] and [e] leave for work and school.{p}You go back to your room."
    n "After a while" with dissolve
    window hide
    pause 2
    scene pcroomsitonchair with dissolve
    pcthink "Damn it's so boring..."
    pc "..."
    pcthink "Maybe I should look for an apartment again..."
    pc "..."
    pcthink "It's nice to see [e] again, but I don't want to stay here with [m]..."
    pc "..."
    pcthink "I can still visit them from time to time..."
    pc "..."
    pcthink "Damn it..."
    pcthink "Tomorrow my stuff comes...maybe I'll wait until then, so I can at least use my computer instead of the phone for that..."
    pcthink "...yeah I guess that's a good idea..."
    pc "..."
    menu:
        "Watch TV in the living room":
            scene black with dissolve
            n "You go over to the living room and zap around the channels..."
            scene livingroom_tv with dissolve
            pause
            pcthink "Commercials."
            pcthink "Commercials..."
            pcthink "Yaawn..."
            scene black with dissolve
            jump tIntroductionDay1
    

label dinnerDay2:
    scene livingroom diningtable dinner1 with dissolve
    m "So... I know it's just your second day back home, but how do you feel about it? Have you settled in a bit already?"
    pc "Err... it's still a bit weird to be honest."
    scene livingroom diningtable dinner2 with dissolve
    m "Oh, I'm sure you will come to like it here after a while."
    pcthink "After a while? For how long does she expect me to stay?"
    scene livingroom diningtable dinner rdown with dissolve
    m "I..."
    m "..."
    scene livingroom diningtable dinner eup with dissolve
    pcthink "Huh?"
    m "I know you don't have many good memories in this house..."
    scene livingroom diningtable dinner eup rsmile with dissolve
    m "But I'm sure that will change from now on!"
    pc "Eh... yeah... maybe..."
    pcthink "Damn I think she really means it... I'm not sure that it's possible though."
    scene livingroom diningtable dinner1 with dissolve
    m "Anyway, it must be boring being alone here half of the day?"
    pc "Yeah, kinda."
    scene livingroom diningtable dinner5 with dissolve
    m "When did you say your stuff comes?"
    scene livingroom diningtable dinner4_1 with dissolve
    pc "...should be delivered by tomorrow. I don't know the exact time though."
    scene livingroom diningtable dinner4_2 with dissolve
    m "Have you been able to change your address?"
    scene livingroom diningtable dinner2_2 with dissolve
    pc "Yeah, I sent them the new address via email."
    m "Good. That makes it easier at least."
    scene black with dissolve
    n "You continue to chatter with [m] while [e] occasionally makes faces at you."
    jump eNightTwo
    
label stuffArrivesDay3:
    play sound "audio/doorbell.ogg"
    n "You hear the doorbell ring."
    scene pcroomwakeup with dissolve
    pc "Uhhh..."
    scene pcroomwakeup1 with dissolve
    pc "YAAAAWN..."
    scene pcroomwakeuplookfore with dissolve
    pcthink "Looks like [e] is up already..."
    pc "..."
    pcthink "Wha... shit, the door. It must be my stuff being delivered!"
    scene black with dissolve
    n "You get up quickly, throw some clothes on and hurry to the front door."
    jump stuffArrivesDay3Door

label getEfromSchool1:
    scene black with dissolve
    n "A bit later" with dissolve
    stop music fadeout 2
    scene school first arrival with dissolve
    pcthink "Alright, there is the school..."
    n "Suddenly you hear a voice from behind you."
    "Voice" "Hey! Stop right there!"
    pcthink "Huh?"
    play music "audio/LightSteps.mp3" fadein 1
    scene school cop1 with dissolve
    pcthink "Oh no... not this guy again..."
    scene school cop2 with dissolve
    "Cop" "Hey... *pant* ...I said... *pant* ... stop right there!"
    pc "I'm just standing here Officer..."
    "Cop" "You... *pant* ... shit..."
    pc "A little out of shape Officer?"
    scene school cop3 with dissolve
    "Cop" "You better shut it... *pant* ...smart ass."
    scene school cop4 with dissolve
    "Cop" "Just so you know... I know about you... I have seen your files!"
    pc "..."
    scene school cop6 with dissolve
    "Cop" "What?! Surprised?"
    scene school cop5 with dissolve
    "Cop" "It wasn't easy to get them *gasp* and my colleagues even told me to let it go, but I'm not a lazy bum like they are."
    "Cop" "The case might be closed, but I know you have skeletons in your closet!"
    pcthink "Shit!"
    scene school cop6 with dissolve
    "Cop" "I'll be keeping an eye on you!"
    pc "Well, I hope you have fun with that. I have things to do..."
    "Cop" "I'm watching you!"
    scene school first arrival with dissolve
    pc "Yeah... bye..."
    pcthink "Damn, this guy is annoying... I hope he doesn't become a problem..."
    stop music fadeout 2
    scene school1 with dissolve
    pcthink "Hum... the school didn't change a bit. It looks exactly like when I left..."
    play music mainbgm fadein 1
    scene school1 jada with dissolve
    j "{size=-10}...and you really should have told me how hot [heshe] is{/size}."
    pcthink "Isn't that [j]?"
    play music mainbgm fadein 1
    scene school1 jada1_2 with dissolve
    j "Speaking of the devil, look who's here!"
    scene school elli1 jada2 with dissolve
    e "Eh?"
    pc "Hey girls."
    scene school elli1 with dissolve
    j "{b}[e]!{/b}"
    scene school elli2 with dissolve
    j "Can't you at least wait until you're home before you hump your big [bs]?"
    pcthink "What the?! Hump me?"
    scene school elli3 with dissolve
    pause
    scene school jada tease with dissolve
    j "So... what's up [pc]? Did you miss your {i}cute little sister{/i} soo much that you have to come visit her?"
    pcthink "What the fuck?"
    j "Or... did you {i}cum{/i} for me?"
    scene school jada tease ejealous with dissolve
    e "Hnnn!!!"
    j "Hehe, calm down [e], I'm just teasing."
    pcthink "Damn, this girl is such a minx!"
    scene school jande look with dissolve
    pc "Actually, [m] called me to pick up [e]. She is stuck in traffic and can't make it."
    pc "She tried to call you by the way."
    scene school jande look2 with dissolve
    j "Did she?"
    scene school jande look away with dissolve
    j "I didn't notice. Oh but my phone is on vibrate, hehe."
    pc "Uh-huh..."
    scene school jande look away back1 with dissolve
    j "Well, shall we go then?"
    pc "You're coming with us?"
    j "Of course!"
    scene school jande look away back2 with dissolve
    j "Someone has to make sure that a specific young lady doesn't get herself into trouble."
    pc "Eh... Not that I mind you coming with us, but I'm sure I can handle that."
    j "No you can't."
    pc "What? Why is that?"
    scene school jande leave with dissolve
    j "Because you're the source of the problem, silly."
    pc "Err... okay?"
    j "Well, come on. Let's go!"
    e "Mhm!"
    pc "Yeah..."
    scene black with dissolve
    n "You take the two back home."
    $ actionsUsed = 7
    call dateTime from _call_dateTime_11
    jump afterGetEFromSchool


label afterGetEFromSchool:
    $ storyEvent = False
    $ SEGetEFromSchool = False
    n "After your arrival you let them do their thing and you go to your room."
    play music mainbgm fadein 1
    scene pcroom finish unpacking with dissolve
    pcthink "Damn these girls are crazy..."
    pc "..."
    pcthink "Alright, I guess it's time to unpack the rest of my stuff."
    play sound "audio/door-opening.ogg"
    j "Hey!"
    scene pcroom jadaenter with dissolve
    pc "Uh, hey [j], what's up?"
    j "Do you need help?"
    pc "Err... no, I..."
    scene pcroom jadaenter2 with dissolve
    j "Fuuuuck, you have a VR headset too?"
    scene pcroom finish unpacking with dissolve
    pc "...yeah..."
    scene pcroom jadaenter epeek with dissolve
    j "Awesome!"
    scene pcroom jadaenter epeek2 with dissolve
    j "Oh hey [e], let's help [pc] \"unpack\", hehe."
    e "Hn!"
    n "[e] nods."
    pcthink "Damn [j]. Luckily [e] didn't get the joke..."
    scene pcroom jandehelpunpackstart with dissolve
    j "Okay, let's start with the boxes over here."
    pc "Err..."
    pcthink "Well I guess I have no say in this..."
    scene black with dissolve
    n "A few minutes later." with dissolve
    window hide
    pause 2
        
    if pcgender == "man":
        scene pcroom ereadytosmackdatass with dissolve
        pcthink "Damn, [j] is stretching her ass at me all the time..."
        scene pcroom ereadytosmackdatass2 with dissolve
        pcthink "...this can't be coincidence."
        scene pcroom esmackdatass1 with dissolve
        pc"Huh?{w=1}{nw}"
        play sound "audio/slap2.ogg"
        scene pcroom esmackdatass2 at my_shake with flash
        j "Whaa! Naughty..."
        scene pcroom aftersmack1 with dissolve
        j "[e]?"
        scene pcroom aftersmack2_2 with dissolve
        pc "Uh..."
        scene pcroom aftersmack2 with dissolve
        j "Oh come on [e], don't be so selfish. I'm not going to take him away from you!"
        scene pcroom aftersmack3 with dissolve
        pcthink "Take me away from her?"
        scene pcroom aftersmack5 with dissolve
        j "...but he's still a man and men like to get a little peek from time to time, right [pc]?"
        scene pcroom aftersmack4 with dissolve
        pc "Err..."
        jump haremChoice
    else:
        scene pcroom jandehelpunpack bra with dissolve
        j "Oh wow, look at this [e]."
        e "Hehe."
        pcthink "What the..."
        pc "Hey what are you doing with my underwear?"
        scene pcroom jandehelpunpack bra2 with dissolve
        j "Oh come on, what's the matter? It's sexy. I bet you look hot in it."
        scene pcroom jandehelpunpack bra3 with dissolve
        j "Where is the other piece? I wanna try it on!"
        pcthink "Jeez, that girl..."
        pc "It won't fit anyway, it's obviously not your size."
        scene pcroom jandehelpunpack bra5 with dissolve
        j "Whoops, yeah. I almost forgot that I don't have such a purrfect and sexy body..."
        scene pcroom jandehelpunpack bra6 with dissolve
        j "Too bad, I guess {b}you{/b} have to show us how it looks then, hehe."
        pcthink "Damn girl, was this your plan?"
        scene pcroom jandehelpunpack beformolest3 with dissolve
        j "Come on [pc], show us your sexy curves! I'm sure [e] wants to see them too."
        pcthink "Yeah I'm sure about that, judging by what happened last night..."
        scene pcroom jandehelpunpack beformolest3_2 with dissolve
        j "Come on, come on, don't be shy."
        scene pcroom jandehelpunpack jtitties with dissolve
        j "Here I'll show you my titties too!"
        scene pcroom jandehelpunpack jtittieshide with vpunch
        e "HNNGH!"
        pcthink "What the..."
        j "Come on [e], you've seen them a lot too, don't act so prudishly..."
        pcthink "A lot?"
        scene pcroom jandehelpunpack afterjtitties with dissolve
        j "Ooooh I get it, it's because mine are bigger than yours, right? Don't worry, I bet she will like yours too."
        e "HNN!!!"
        j "Jeez... calm down [e]! It's not like I'm going to take her away from you..."
        jump haremChoice
    
label haremChoice:
    scene pcroom aftersmack4_2 with dissolve
    j "...and by the way, didn't we agree to always share everything?"
    pcthink "Shit... this girl is so fucking naughty..."
    scene pcroom aftersmack4 with dissolve
    j "I bet [heshe] wouldn't mind if we did share, hehe... right [pc]?"
    pc "Eh...?"
    pcthink "Did she just imply a threesome? WTF! How am I supposed to answer to that?"
    pcthink "Damn, if this would be one these adult games, this would probably be the harem choice..."
    menu:
        "{i}(Damn, I love the idea...){/i}":
            $ harem = True
            pc "Err... well I guess I wouldn't mind..."
            scene pcroom aftersmack4_2 with dissolve
            j "See [e]?"
        "{i}(There is no way I would ever do that!){/i}":
            pc "Hell no! I'm not going to get shared with anyone!"
            j "Oh... I expected a different answer..."
    play sound "audio/door-opening.ogg"
    n "Suddenly the door to your room opens."
    scene pcroom jandehelpunpack rachelenter with dissolve
    m "Hey Hun, I'm sorry for the hassle. I really didn't expect to be so late."
    scene pcroom jandehelpunpack rachelenter2 with dissolve
    pc "Yeah, don't worry about it."
    j "Hey [m]!"
    scene pcroom jandehelpunpack rachelenter3 with dissolve
    m "Oh hey [j], I thought I heard your voice. I didn't expect you today."
    scene pcroom jandehelpunpack rachelenter_j with dissolve
    j "Yeah, we have a... school project to work on..."
    scene pcroom jandehelpunpack rachelenter3 with dissolve
    m "I see, well then, it's better you start working on it, don't you think?"
    scene pcroom jandehelpunpack rachelenter_j with dissolve
    j "Yeah, sure."
    scene pcroom jandehelpunpack rachelenter_j2 with dissolve
    j "Come on [e], let's go!"
    e "Hn!"
    scene pcroom rachelenter jandeleave with dissolve
    j "Oh I love that shirt by the way [m]. It looks really hot on you!"
    m "Why thank you!"
    scene pcroom rachelenter jandeleave2 with dissolve
    j "I wonder if you're wearing it for someone special, hehe."
    m "Wh... well don't you two have something to do?"
    j "Of course... {size=-10}Run [e]!{/size}"
    e "Khehehe..."
    if harem:
        #achievement
        $achievement.grant("Achievement_harem")
        init: 
            $achievement.register("Achievement_harem")
        $achievement.sync()
        ###########
    pcthink "Damn, did [j] just stare at [m]s tits?!"
    scene pcroom rachelenter jandeleft with dissolve
    play sound "audio/door_close.ogg"
    m "Humph..."
    pcthink "Why is she closing the door?"
    scene pcroom rachelenter jandeleft2 with dissolve
    m "I'm sorry, I didn't know about [j]. I hope she didn't cause you any trouble?"
    pc "Not at all..."
    scene pcroom rachelenter jandeleft3 with dissolve
    m "Oh that's good, I know she can be a bit ...feisty."
    pcthink "...what an understatement..."
    scene pcroom rachelenter jandeleft4 with dissolve
    m "Anyway, are you hungry? I'll make dinner if you want?"
    pc "No, I'm fine, thanks."
    scene pcroom rachelenter jandeleft5 with dissolve
    m "Okay... Oh by the way..."
    jump rachelElliesBDayReminder
    
label hallPCtalktoEllie:
    n "You go back to your room."
    play music mainbgm fadein 1
    scene pcroomsitonchair2 with dissolve
    pcthink "Okay, I guess it's time for some VR porn, hehe..."
    pcthink "Err, Shit. I wanted to talk to [e] too..."
    pcthink "...but I'm actually quite a bit horny now..."
    menu:
        "She will come over tonight anyway... gimme porn!":
            scene pcroomvrfun with dissolve
            pcthink "Yeah, it's better to clear my mind before she comes over again tonight."
            scene porn-vr1 with fade
            pc "Hey Ladies, did you miss me?"
            scene porn-vr1_2 with dissolve
            pause .1
            scene porn-vr1_3 with dissolve
            "Girls" "Heeey, elder unrelated roommate..."
            scene porn-vr1_4 with dissolve
            pcthink "Err what the..."
            pause
            scene black with fade
            jump pcroomnight3
        "I should really talk to her now!":
            $ efe -= 1
            pcthink "Yeah, I really shouldn't wait any longer. I haven't talked to her alone once, since I've been back..."
            scene black with fade
            n "You go to her room."
            jump childroomPCtalktoEllie
    
label pcroomnight3:
    n "Nothing special happens for the rest of the day."
    scene black with fade
    n "Later that Night." with dissolve
    window hide
    pause 2
    scene pcroomday2night1 with dissolve
    pc "Yaawn..."
    pcthink "It's late... I guess [e] should be coming over soon..."
    pc "..."
    extend "."
    extend "."
    scene pcroomday2night1_1 with dissolve
    m "{size=-10}[e]? What are you doing up so late? Trying to sneak into your [bs]'s bed again?{/size}"
    pcthink "Huh? [m] is still awake?"
    m "{size=-10}You should really let [himher] sleep [e]...{/size}"
    e "{size=-10}...{/size}"
    m "{size=-10}Listen [e], I know you're really happy that [pc] is back, but [heshe] just moved in and we both don't know if [heshe] intends to stay...{/size}"
    m "{size=-10}...also, [heshe]'s been away for a long time, we basically don't know anything about [himher]. Plus, do you even know if [heshe] is okay with you sleeping in [hisher] bed?{/size}"
    pcthink "Damn, are you serious [m]?"
    m "{size=-10}Come on [e], go back to your room. If [heshe]'s going to stay, you'll have enough opportunities to cuddle with [himher] in the future...{/size}"
    pcthink "..."
    pcthink "Well... I guess I'm going to sleep alone tonight..."
    stop music fadeout 2
    scene black with fade
    play music "audio/BadDream.mp3"
    scene dream_01 at dream with dissolve
    m "[bpc], WHAT THE HELL?!"
    m "Don't tell me you got yourself into a fight AGAIN?!"
    pc "..."
    m "Just what the hell is wrong with you? Why must you constantly embarrass me?"
    m "Can't you be a normal [boygirl] once in your life?"
    pc "..."
    m "Oh I guess that's a bit too much to ask with a Dad like yours..."
    m "I swear, if I get a call from your school or the police again, you'll regret ever being born!"
    pc "..."
    m "DON'T JUST STAND THERE LIKE THE FOOL YOU ARE, YOU'RE DRIPPING BLOOD ALL OVER THE FLOOR, GO TO THE BATHROOM AND WASH YOUR FACE!"
    pc "..."
    m "...and don't forget to wipe the blood off the floor when you're done..."
    pc "..."
    stop music fadeout 2
    scene black with dissolve
    $ storyEvent = True
    $ actionsUsed = 8
    call dateTime from _call_dateTime_12
    
label wakeupDay3:
    scene pcroomwakeup with dissolve
    pcthink "Uhh... not again..."
    scene pcroomwakeup1 with dissolve
    pcthink "..."
    pcthink "...she didn't even care I was hurt..."
    pcthink "Fuck you [m], I'm not going to forgive you so easily!"
    pcthink "..."
    pcthink "At least [e] was worried about me..."
    pcthink "I can't even count how many times she stitched me together after I got into a fight."
    pcthink "She was still so young, but she tried to cheer me up so many times..."
    pcthink "I think she knew that I was just angry..."
    pcthink "Angry at [m], angry at the old man, angry at everything and everyone..."
    pcthink "..."
    pcthink "Well I better find the perfect present for her birthday. I have a lot to make up for and only a few hours time."
    scene black with dissolve
    n "You take a quick shower and make yourself ready to go into the city."
    play music mainbgm fadein 1
    scene hall_back_idle with dissolve
    pcthink "Alright, time to go."
    $ SEsisBDayPresent = True
    $ doonce = True
    call screen map_hall_back
    
    
label pcCityDay3:
    scene city2 with dissolve
    pcthink "Okay, where should I start..."
    pcthink "Uhh... shit, I don't even know what [e] likes... I should have asked [m] or [j]..."
    pcthink "Hum..."
    pcthink "Wasn't there a cafe somewhere here? I can't think straight without a good coffee in the morning..."
    scene black with dissolve
    n "You look around for the cafe until you find it."
    scene coffeehouse2_1 with dissolve
    "Dude" "Yeah?"
    pcthink "Wasn't there a girl working here last time?"
    pc "The biggest cup of the strongest coffee you have."
    "Dude" "Sure..."
    pcthink "This guy looks kind of funny in the uniform..."
    scene coffeehouse2_1_2 with dissolve
    "Dude" "Here you go..."
    pc "Thanks, keep the change."
    "Dude" "Thanks."
    scene coffeehouse2_2 with dissolve
    "Girl" "{size=-10}Yeah, bye!{/size}"
    pcthink "That's the barista from last time."
    scene coffeehouse2_3 with dissolve
    "Girl" "Oh, you."
    pc "Me?"
    pcthink "Looks like she's remembering me as well."
    scene coffeehouse2_4 with dissolve
    "Girl" "Ah sorry, haha. You looked really tired last time, that's why I remember you, haha."
    pc "Yeah that sounds like me... I hope I didn't look too scary?"
    "Girl" "Haha no, not at all. Err... how is your friend?"
    pc "Friend?"
    "Girl" "The older woman..."
    "Girl" "Oh that sounds mean. I didn't mean that she looks old or something, haha. She's a regular."
    "Girl" "...but she looked really sad when she left the other day. I hope she's alright?"
    pc "I guess you mean [m]...  yeah she's fine."
    "Girl" "Did you break up with her?"
    pc "Break up? Hell no! She's not my girlfriend."
    "Dude" "Hey [h], stop chattering, I want to go home!"
    scene coffeehouse2_4_2 with dissolve
    "Girl" "Ugh... Looks like I have to start my shift."
    pc "Yeah, too bad."
    scene coffeehouse2_4 with dissolve
    "Girl" "I'm [h] by the way."
    menu:
        "Introduce yourself.":
            $ hlo += 1
            pc "[pc], nice to meet you."
            h "Nice to meet you too. I hope you visit us more often from now on, we have the best coffee in town and the cutest barista too, haha."
            pc "That's two really good reasons to come back. Especially the last one."
            h "Hehe, thanks."
            "Dude" "[h]!"
            scene coffeehouse2_4_3 with dissolve
            h "Yes, stop crying baby boy!"
            scene coffeehouse2_5 with dissolve
            h "Well, I have to go. See you soon~"
            pc "Yeah, seeya."
            scene black with dissolve
            pcthink "Wow, she seemed kind of nervous at first... because of me?"
            pcthink "Cute..."
        "Say good bye and leave.":
            scene coffeehouse2_5 with dissolve
            pc "Yeah, well I have to go now. Bye..."
            scene black with dissolve
    n "You leave the cafe and walk down the street, starting to think about what kind of present [e] would really like to have."
    n "You wander from window to window, enter some shops, look at jewelry, plushies, clothes and several other things."
    pcthink "..."
    pcthink "Hum... looked better from far away."
    pcthink "..."
    pcthink "No... this won't do as well..."
    pcthink "..."
    pcthink "No..."
    pcthink "...no..."
    pcthink "Nope, this looks cheap..."
    pcthink "..."
    pcthink "Ugh... who buys this shit?"
    pcthink "..."
    n "Several shops and after what feels like hours you start to get exhausted."
    pcthink "Damn! Why is it so hard to find a good present..."
    n "You decide to enter one last shop and take a break after that. You enter the shop without looking at what they actually sell."
    scene phoneshop1 with dissolve
    pcthink "A phone shop?"
    pcthink "Well I won't find anything here..."
    pcthink "Or...?"
    pcthink "Hum... [m] said [e] wouldn't know how to use it, but I highly doubt that."
    pcthink "I don't know any girl her age who doesn't want to have a mobile phone."
    pcthink "Plus I don't think she has the money to buy a good one herself..."
    pcthink "Yeah, I bet she would be happy to have one, even if she's only using it to send messages and listen to music."
    pcthink "But I can't buy just {b}some{/b} phone, it has to be a good one. Maybe a Lie-Phone, or the new Moogle phone?"
    pcthink "...and some cute accessories too. Girls her age love this kind of stuff... I think..."
    scene black with dissolve
    n "You buy a stupidly expensive mobile phone and some cute accessories.{p}Then you make your way back home."
    scene black with fade
    scene re_home with dissolve
    pc "I'm back..."
    pcthink "...looks like [m] and [e] aren't back yet."
    scene black with dissolve
    n "You hide the mobile in your room and after a while waiting for [m] and [e] to return you decide to spend some time watching TV."
    scene livingroom ttv with dissolve
    "Reporter" "...building that burned down a few days ago."
    "Reporter" "The man responsible for the fire stated that he wanted to protect his wife from becoming corrupted by another man."
    "Reporter" "Police told us that the man believes that some unspecified person is using a magical serum to bend his wife's and other women's will."
    scene livingroom ttv2 with dissolve
    "Reporter" "He was sent to a mental hospital..."
    pcthink "Jeez, this guy must have played too many porn games..."
    pcthink "Anyway I... huh?"
    n "*Mobile phone rings*"
    scene livingroomttvrachelcall1 with dissolve
    pcthink "[m]... what does she want now?"
    scene livingroomttvrachelcall2 with dissolve
    pc "Yes..."
    m "Hey [pc], it's [m]."
    pc "Yeah, I know."
    m "I'm sorry, we are running a bit late, if [t] shows up, could you tell her that we will be home soon?"
    pc "The therapist? Did you seriously invite her to [e]'s birthday?"
    m "No it's..."
    m "It's... a session."
    pc "What? That's even worse!"
    m "[pc], please. I know you don't like her, but these sessions are important for [e] and [t] doesn't have much time, so we have to take what we can get."
    pc "Geez, [m] this is awful..."
    m "I know, I'm sorry..."
    pc "You should be sorry for [e], it's her birthday!"
    m "Will you tell her [pc]? Please?"
    pc "Humph... yeah fine..."
    m "Thank you, Hun. We'll be home soon."
    scene livingroom ttv2 with dissolve
    pcthink "I can't believe it, she's ruining [e]'s birthday..."
    play sound "audio/doorbell.ogg"
    stop music fadeout 2
    n "*Doorbell rings*"
    pcthink "Ugh... speak of the devil..."
    scene black with dissolve
    n "You get up and open the door."
    jump talkTone
    
label ebdPreps:
    m "This, and that... oh could you take the plate, Hun?"
    pc "Sure..."
    scene livingroom ebd preps1 with dissolve
    m "Alright, that's it, everything is ready. Now we only need to wait for [e]."
    pc "Is no one else coming?"
    scene livingroom ebd preps2 with dissolve
    m "Well..."
    scene livingroom ebd preps3 with dissolve
    m "[e] doesn't have many friends because of... how she is."
    m "...and aunt Jenna died a few years back..."
    pc "Jenna is dead?"
    scene livingroom ebd preps4 with dissolve
    m "Yes... that's one of the things I wrote you in the letter I sent you..."
    m "I'm sorry, Hun."
    pc "Uhh... yeah, forget it..."
    pcthink "Damn, I liked aunt Jenna..."
    scene livingroom ebd preps5 with dissolve
    m "Anyway, why don't you sit down and I'll go get the punchbowl?"
    scene livingroom ebd preps6 with dissolve
    j "I've got it already."
    scene livingroom ebd_jadabowl with dissolve
    m "Oh, thanks [j]."
    j "Anytime~"
    scene livingroom ebd preps jandr with dissolve
    pcthink "Geez..."
    scene livingroom ebd_tenter with dissolve
    m "Oh [t], did you finish for today?"
    scene livingroom ebd_tenter1 with dissolve
    t "Yes, obviously."
    m "Nice, why don't you come and sit down with us for a while?"
    scene livingroom ebd_tenter2 with dissolve
    pcthink "No.fucking.way!"
    pcthink "Looks like [j] thinks the same."
    m "You should try my punch."
    scene livingroom ebd_tenter2_2 with dissolve
    t "Sorry, I don't have time and I still have to drive."
    m "Oh, don't worry, there is no alcohol in it."
    t "No I..."
    scene livingroom ebd_tenter3 with dissolve
    j "Oh you HAVE to try it, I'm sure you've never had punch as good as [m]'s! Hehe."
    pcthink "What the fuck [j]?"
    scene livingroom ebd_tenter4 with dissolve
    m "Why thank you [j]. See [t]? Come on, I'm sure your work can wait for a few minutes."
    scene livingroom ebd_tenter5 with dissolve
    t "..."
    t "Humph... fine, but just one glass."
    scene black with fade
    
    jump ebdLookForE
    
label ebd:
    scene livingroom ebd all start with dissolve
    m "Oh [pc], do you know what got into [t]?"
    pc "Err... no, why? What happened?"
    m "She came into the room, blushing bright red like a tomato, grabbed her bag and left..."
    scene livingroom ebd all start1 with dissolve
    j "Yeah, all she said was \"[pc], the perv molested me while I was in the bathroom.\" Hehe."
    pc "W-WHAT?!"
    m "[j]! That's not funny."
    j "Hehe, sorry."
    if tc:
        pcthink "Gawd! She was just joking... damn you [j], I almost died."
    scene livingroom ebd all start2 with dissolve
    m "All [t] said, was that she has to leave and before I could say anything she was gone..."
    pc "Strange..."
    m "Right?"
    m "Anyway, what's up with [e]? Will she be ready soon?"
    pc "Yeah, she's changing right now."
    scene livingroom ebd all start3 with dissolve
    j "Oh, so you molested her instead?"
    scene livingroom ebd all start4 with dissolve
    m "[j]!"
    scene livingroom ebd all start5 with dissolve
    j "Yeah, sorry [m], you're right, I shouldn't say things like that..."
    scene livingroom ebd all start5_2 with dissolve
    j "...It's not like [pc] {b}{i}needs{/i}{/b} to molest her anyway, hehe."
    scene livingroom ebd all start6 with dissolve
    m "Ugh... you're hopeless [j]."
    pc "..."
    scene black with dissolve
    n "A little bit later." with dissolve
    play music mainbgm fadein 1
    window hide
    pause 2
    j "...and then you saw the burning apartment building?"
    scene livingroom ebd all start3 with dissolve
    pc "Yeah."
    j "Crazy..."
    scene livingroom ebd all start2 with dissolve
    m "I'm so sorry, Hun. But at least you are here with us now. *hic*"
    scene livingroom ebd all start3 with dissolve
    j "Yeah, without the fire we would've never met, so cheers to the crazy dude who..."
    scene livingroom ebd all start6_2 with dissolve
    m "There you are, we've been waiting for you [e]... Oh you look beautiful!"
    scene livingroom ebd all1 with dissolve
    j "Wow, [e], you look luscious!"
    scene livingroom ebd all1_2 with dissolve
    m "I guess now we know what took her so long."
    j "Hehe."
    e "..."
    m "..."
    pc "..."
    scene livingroom ebd all2 with dissolve
    j "Hey, say something [pc]!"
    pc "Err..."
    pc "Sorry, I had to collect my jaw from the floor first, you look stunning [e]."
    scene livingroom ebd all2_2 with dissolve
    e "..."
    m "Well then, why don't you come over here and sit down with us, [e]..."
    scene black with fade
    j "...WHAHAHA, [heshe] really fell out of the bed?"
    scene livingroom ebd all3 with dissolve
    m "Yes, it was really funny *hic*"
    m "And guess what, [heshe] was sleeping completely naked, haha."
    j "NO WAY!"
    m "It's true, right [pc]?"
    scene livingroom ebd all4 with dissolve
    j "Aww, I would've loved to see that! Hehe."
    scene livingroom ebd all5 with dissolve
    m "Oh by the way, don't you want to give [e] your presents?"
    scene livingroom ebd all8 with dissolve
    j "I already gave her mine yesterday."
    scene livingroom ebd all6 with dissolve
    m "Really, what is it?"
    scene livingroom ebd all8 with dissolve
    j "Just some nice clothes and... a secret, hehe."
    scene livingroom ebd all6 with dissolve
    m "A shecret eh? *hic*"
    scene livingroom ebd all4 with dissolve
    j "What did you get her [pc]?"
    pc "Oh I have a..."
    pcthink "Shit, I can't give it to her in front of [m]. She still thinks [e] has no idea how electronics work..."
    scene livingroom ebd all7 with dissolve
    m "Well?"
    pc "Err... well, haha, it's a secret too..."
    m "Huh? Why do you all have secret presentsh... did I miss the joke here? *hic*"
    scene livingroom ebd all8 with dissolve
    j "Naaw, don't worry, we just don't want to destroy the surprise, hehe."
    scene livingroom ebd all6 with dissolve
    m "Oh... okay... *hic*"
    scene black with fade
    m "...and then I deshided to *hic... shtop drinking and shange my life... it wash the besht deshision I've ever made..."
    scene livingroom ebd all9 with dissolve
    m "Oh nooo, the besht deshision wash to get [pc] back... *hic*"
    j "Yeah, that was a great decision, hehe."
    m "Ugh..."
    scene livingroom ebd all rtobed1 with dissolve
    m "I shink I need to pee..."
    scene livingroom ebd all rtobed2 with hpunch
    pc "Whoa!"
    m "Whups..."
    e "Hehe."
    pc "Are you okay [m]?"
    m "S-shorry, [pc]..."
    m "Ugh... I don't feel sho well..."
    pcthink "Shit, she definitely had enough punch for today..."
    pc "Maybe you should lie down for a while."
    m "...but it's [e]'sh birthday... *hic*"
    pc "Doesn't help if you feel bad [m]."
    m "Uhh... everything is shpinning..."
    scene livingroom ebd all rtobed4 with dissolve
    j "You should help her to the bedroom, [pc]. Hehe."
    scene livingroom ebd all rtobed5 with dissolve
    m "But I don't want to go to bed yet... *hic*"
    pc "Come on [m], I'll help you..."
    m "Ugh... okay... i-if I must..."
    
    jump ebdRachelToBed
    
label ebd2:
    scene livingroom ebd all rtobed13 with dissolve
    j "Wow, I've never seen [m] {b}this{/b} drunk before!"
    e "Heh..."
    scene livingroom ebd all etobed with dissolve
    pc "Well I did... several times..."
    pcthink "...and she was completely different this time..."
    j "She will be alright... right?"
    pc "Yeah..."
    j "Great! Now let's start the {i}real{/i} party, right [e]? Hehe..."
    scene livingroom ebd all etobed1_1 with dissolve
    e "..."
    j "[e]?"
    e "...ehh..."
    scene livingroom ebd all etobed1_2 with hpunch
    pause 1
    e "..."
    j "Awww damn it..."
    pc "Looks like the party is over before it even started..."
    j "AAAAaaaawwww... stupid [j]!"
    j "..."
    j "I'm sorry..."
    j "I wanted this to be something special for [e] and now everything is fucked..."
    pc "Well, you tried... and I guess this is a birthday she will remember..."
    j "If she remembers anything at all..."
    j "..."
    pc "I'm going to take her to bed..."
    j "Yeah..."
    scene livingroom ebd all etobed3 with dissolve
    pcthink "I guess I was right..."
    pcthink "...it didn't turn out well..."
    scene black with dissolve
    pause 1
    scene childroom ebd all etobed2 with dissolve
    pc "Good night [e]."
    e "Hnn..."
    scene black with dissolve
    jump ebdBringJadaHome

label ebdEnd:
    stop music fadeout 2
    scene black with dissolve
    pcthink "Well, back home..."
    scene ebd backhome with dissolve
    pcthink "Home..."
    pcthink "I've never felt at home in this house..."
    scene ebd backhome2 with dissolve
    pcthink "Hum... I guess [m] isn't going to clear the table anytime soon..."
    pcthink "At least there's no huge pile of junk to clean up like after a normal party..."
    scene black with dissolve
    n "You clear the table and decide to go to bed."
    scene pcroom night with dissolve
    pcthink "What a \"party\"..."
    pcthink "That must have been the worst birthday party ever..."
    pcthink "Poor [e], I hope she{w=1.0}{nw}"
    play sound "audio/door-opening.ogg"
    scene pcroom ebd night1 with vpunch
    pc "Whoa [e]!"
    scene pcroom ebd night2 with dissolve
    e "Uhhh..."
    scene pcroom ebd night3 with dissolve
    pcthink "Wow she's really drunk..."
    scene pcroom ebd night4 with hpunch
    pause
    pc "[e]?"
    e "*snore*"
    pc "..."
    pc "Oh well... good night [e]..."
    $ storyEvent = True
    $ SEAfterEBD = True
    $ SEsisBDayPresent = False
    $ actionsUsed = 15
    $ livingHomeDays = 3
    call dateTime from _call_dateTime_13
    
label afterEBD:
    $ SEAfterEBD = False
    $ SERachelBRAfterEBD = True
    play music mainbgm fadein 1
    pc "*Yaaawn*"
    scene pcroom afterebd1 with dissolve
    pc "..."
    scene pcroomafterebd2 with dissolve
    pause 5
    pcthink "[e]..."
    pcthink "When did she become so attached to me?"
    pcthink "She's was always a bit clingy when we were younger, but this is... different..."
    pcthink "Could she really be in love with me, like [j] said?"
    pcthink "...with her own [bs]?"
    pcthink "..."
    pcthink "...and why doesn't she talk?"
    pcthink "Or does she?"
    pcthink "Could she be talking to [j]?"
    pcthink "I'd understand it if she doesn't want to talk to [m]... or that therabitch..."
    pcthink "...but why wouldn't she want to talk to me?"
    pcthink "What the hell happened after I moved out?!"
    scene pcroomafterebd2_2 with dissolve
    pause .5
    e "Hnnn..."
    pcthink "Damn..."
    pause 5
    pcthink "Well, time to get up. I need to use the bathroom."
    scene pcroom afterebd3 with dissolve
    pcthink "I guess I'll let her sleep..."
    scene pcroom rachel afterkisscheekleft with dissolve
    pcthink "I hope [m] isn't up already..."
    scene home_hall_idle with dissolve
    call screen map_home_hall
    
label officeFirst:
    scene black with fade
    n "On your way to the office it starts to rain."
    pcthink "Shit, lucky me!"
    n "You can see a woman running towards the entrance of the building in which you suspect the office to be located."
    scene job intro with dissolve
    pc "Hey! Hey you!"
    scene job intro1 with dissolve
    "Woman" "Y-yes?!"
    pc "Is this Atomic Aeronautics?"
    "Woman" "Y-yes!"
    pc "I'm [pc]... [pc] [pcsure]."
    "Woman" "[pc] [pcsure]?"
    pc "Yes, I'm starting work here tomorrow!"
    "Woman" "O-oh, that's you... please, let's go inside!"
    scene black with dissolve
    "You follow her."
    scene job intro2 with dissolve
    pc "Finally out of the rain..."
    "Woman" "Why are you here?"
    pc "Huh?"
    "Woman" "I-I mean, you're starting tomorrow, why are you here today?"
    pc "Well... it's been a while since I left town, and I don't know this area, so I thought it might be a good idea to have a look before I start."
    "Woman" "I see."
    pc "I could ask you the same question by the way. It's Sunday, what are you doing here?"
    "Woman" "I... C.J... the boss asked me to bring in some papers."
    pc "He's here, too?"
    "Woman" "Yes, like almost every Sunday."
    pcthink "WTF, he must be a workaholic..."
    pc "Every Sunday?"
    scene job intro3 with dissolve
    "Woman" "Yes... I can tell him that you are here."
    pc "Yeah, why not. Can I have a look around?"
    "Woman" "Uhm... I can show you a bit, why don't you follow me."
    pc "Yeah, sure. What's your name by the way?"
    "Woman" "Stephanie..."
    pc "Well, nice to meet you, Stephanie."
    scene black with dissolve
    pause 1
    scene job intro4 with dissolve
    st "This is the fabrication and testing hall."
    scene job intro5 with dissolve
    pc "Whoa, I didn't know that you're actually building stuff here..."
    st "This is the company headquarters, all our prototypes are built and tested here."
    pc "That's really impressive."
    scene black with dissolve
    pause 1
    scene job intro6 with dissolve
    pc "Damn, this building is larger than I'd expected it to be..."
    scene black with dissolve
    pause 1
    st "C.J, I have the papers you asked for."
    boss "Oh good, thanks, [st]."
    st "There is something else..."
    scene boss_buro1 with dissolve
    st "Our new employee..."
    scene boss_buro2 with dissolve
    boss "Oh, I see, you must be [pc]. I didn't expect you today."
    pc "Err... yeah, I actually just wanted to have a look at the office, but then it started to rain and Stephanie was nice enough to let me in."
    boss "Anyway, nice to meet you."
    scene boss_buro3 with dissolve
    boss "[st], why don't you go and get yourself and [pc] a towel to get dry with."
    st "Yes, [boss]."
    scene boss_buro4 with dissolve
    boss "You should have called me, I'd have let you in."
    pc "I didn't know you're here."
    scene boss_buro5 with dissolve
    boss "Ha! I'm always here. My wife is happy when I leave her alone and I'm happy when I don't have to see her... A drink?"
    pc "Err... no, thanks."
    boss "Well I'll take one."
    scene boss_buro6 with dissolve
    boss "Actually, it's good that you're here today, so we can go through all the details while it's quiet."
    boss "I guess [st] showed you around a bit?"
    pc "Yeah, it's quite impressive."
    boss "Ha! That's nothing. We're just doing the rough tasks here, but I've seen your work, now {b}that's{/b} impressive. You're a true artist."
    pc "Thanks, I do my best."
    scene boss_buro7 with dissolve
    boss "That's why I hired you. Now let's sit down, there are a few things I need from you asap!"
    scene black with fade
    n "After a quick introduction he tells you about a new project he's planning, and your role in it. It turns out that there is not much time left, you only have one week from start to finish for your part of the project."
    n "A while later."
    scene boss_buro8 with dissolve
    boss "...and if you need anything, be sure to call or just come by. Even if I'm not here, [st] is always there to help."
    pc "Sure. By the way, is she your secretary?"
    boss "Yes and no. She's actually more than just a secretary. In fact, she could handle the company on her own if she'd just be a bit more confident, but that woman is way too shy, I tell ya..."
    pc "Yeah, I've noticed that."
    boss "Don't worry, she'll open up to you over time. That's just the way she is."
    pc "I hope so... errm... can I ask you a personal question?"
    boss "There is nothing going on between us, so if you're interested in her, just go for it."
    pc "Eh... haha, actually I was wondering what C.J. stands for?"
    boss "My name?"
    pc "Yeah, it's always just C.J. in every paper I've seen so far."
    boss "Colin-James Olafsson is the name, and yes, I have some Viking ancestry. One of them even sailed with the children of Eirik the Red."
    pc "Wow, that's interesting!"
    boss "Anyway, I won't keep you any longer. We both have a lot of work to do. See ya next week."
    pc "Yeah, goodbye."
    scene black with fade
    n "On your way back home."
    "*Ding*"
    scene city7ephoto1 with dissolve
    pcthink "Huh?"
    pcthink "A message from [e]? HA! I knew it!"
    scene city7ephoto2 with dissolve
    pcthink "Heh... cute dress..."
    pcthink "Is that her tongue sticking out?"
    scene epic at ephone with dissolve
    pcthink "Yep, it is... damn she's so cute."
    stop music fadeout 1
    play sound "audio/collide.ogg"
    scene city_8_cop1 with vpunch
    "Cop" "Ouuch!"
    pc "Fuck!"
    play music "audio/LightSteps.mp3" fadein 1
    scene city_8_cop2 with dissolve
    "Cop" "YOU!"
    pc "Oh, no..."
    pcthink "Not this guy again..."
    scene city_8_cop3 with dissolve
    "Cop" "So-so, not watching where we're going, are we?"
    pc "I doubt that {b}you{/b} were looking, idiot..."
    pcthink "Shit, I shouldn't have said that!"
    scene city_8_cop4 with dissolve
    "Cop" "What was that? Insulting an officer? W-wait... you ran into me, that was obviously an attack! Ha! Now I got you!"
    pc "What? That's bullshit and you know it!"
    scene city_8_cop5 with dissolve
    "Cop" "Hands where I can see them, turn around, asshole!"
    pcthink "Fuck... what an idiot..."
    scene black with fade
    stop music fadeout 2
    
    scene holdingcell_1 with dissolve
    pcthink "Damn... I had hoped to never see this cell again..."
    pcthink "Fuck that goddamn wannabe Sherlock! What the fuck is his problem anyway!"
    scene holdingcell2 with dissolve
    pcthink "..."
    scene holdingcell_1 with dissolve
    pcthink "How many times have I seen this cell from the inside?"
    pcthink "Shit, I hope they let me go soon, I don't want to spend the night here..."
    scene holdingcell3 with dissolve
    pcthink "..."
    scene holdingcell_1 with dissolve
    pcthink "Especially not in wet clothes..."
    scene holdingcell4 with dissolve
    pcthink "...what's up with her?"
    scene holdingcell_1 with dissolve
    pcthink "Damn, I hope [m] and [e] don't find out I'm in here."
    scene holdingcell_5 with dissolve
    if pcgender == "man":
        "Prostitute" "Hey there, handsome. I haven't seen you here before."
    else:
        "Prostitute" "Hey there, beautiful. I haven't seen you here before."
    scene holdingcell6 with dissolve
    pc "Ugh... yeah, you're a few years late..."
    "Prostitute" "Huh? What do you mean, honey?"
    pc "...forget it."
    scene holdingcell7 with dissolve
    pause .5
    "Prostitute" "But it's never too late to have a bit fun, don't you think, sexy?"
    pause .5
    pc "We are in a holding cell already, do you want to get in even more trouble?"
    "Prostitute" "No risk, no fun."
    scene holdingcell8 with dissolve
    "Prostitute" "Come on, sexy, I'll make it worth your time!"
    oc_ "Apart you two!"
    scene holdingcell9 with dissolve
    "Prostitute" "Ughh, shit!"
    oc_ "Sam, aren't you in enough trouble already?"
    scene holdingcell10 with dissolve
    "Prostitute" "Fuck off, old man, you're not my dad!"
    oc_ "And you're lucky that I'm not..."
    "Prostitute" "Pfft..."
    oc_ "Wait a minute..."
    oc_ "[pc]?"
    scene holdingcell_cop1 with dissolve
    pc "Huh?"
    pcthink "Is that... Johnson?!"
    scene holdingcell_cop2 with dissolve
    oc "What the hell are {b}you{/b} doing here? I thought I'd never see you again?!"
    pc "Yeah, likewise..."
    oc "Come on, you know what I mean. When did you come back?"
    pc "About a week ago..."
    oc "A week?!"
    oc "A fuckin' week and you're in a cell already?"
    pc "Hey, it's not my fault this time. I've changed a lot since back then."
    pcthink "Wow, that sounds like [m]..."
    oc "...and you think I believe that? Seriously, you should know better, [pc]."
    pc "It's true. There is this idiot... shit, I mean a co-worker of yours who is on me constantly, for whatever weird reason..."
    oc "Who?"
    pc "I don't know his name. He wasn't here back then... He's quite short, clumsy, {i}out of shape{/i}... and he thinks he's the new white \"Shaft\" or something..."
    oc "...[w]."
    oc "So that's why he wanted to have access to the old files."
    pc "Seriously, what's his problem?"
    oc "..."
    scene holdingcell_cop3 with dissolve
    oc "Come on, let's get you outta here."
    scene black with dissolve
    "You follow him to his office where he quickly fills out all the necessary paperwork."
    scene police_office1 with dissolve
    oc "Alright, that's it, you're free to go. Make sure that's the last time I have to see you here!"
    scene police_office5 with dissolve
    pc "If it was up to me I wouldn't be here in the first place... but seriously, thanks."
    scene police_office2 with dissolve
    w "Oi! What the..."
    oc "Ugh... bad timing..."
    w "Johnson, what's going on here? What are you doing with my prisoner?"
    scene police_office3 with dissolve
    oc "First of all, [heshe] is not {b}your{/b} prisoner..."
    oc "Secondly, you know as much as I do, that your accusations won't stand a chance in court. You should be happy that I'm doing the paperwork."
    scene police_office4 with dissolve
    w "T-that's... that's harassment! Y-you only want to bully me!"
    oc "Sure, [w]... why don't you go back on the streets and watch the traffic..."
    w "{b}You{/b}... I know that you're in cahoots over something... That one closed case, it's obvious that you're hiding something and I'm going to prove it!"
    w "Say goodbye to your pension, Johnson!"
    scene police_office4_2 with dissolve
    oc "Jeez..."
    pc "That doesn't sound good... this guy has some serious issues..."
    scene police_office5 with dissolve
    oc "Don't worry about him, nobody here takes him seriously, and the case was closed a long time ago."
    pc "I don't want you to get into trouble because of me."
    oc "Better worry about yourself. Make sure that I don't have to see you again before my retirement."
    pc "Heh, can't be long, old man."
    oc "Ha...{w=1} Ha...{w=1} Now move ya ass outta here!"
    pc "I'm gone already... thanks, Johnson..."
    scene black with fade
    n "Your way back home is quite unspectacular, but you can't help but to think about how many times [oc] saved your ass when you were younger..."
    n "A bit later."
    jump rachelsaffair
    
label dinnerDay4Home:
    play music mainbgm fadein 1
    scene dinner_day4home_3 with dissolve
    m "So, how was your day, Hun? You've been away longer than I thought you would be."
    pc "Uh, yeah nothing special... I met my new boss and we had a long conversation about work..."
    scene dinner_day4home with dissolve
    m "Oh really? He was there on a Sunday?"
    pc "Yeah, I was surprised as well."
    m "Now I understand why you took so long."
    pcthink "Why would she be interested in how long I'm away? I didn't even mention how long I'd be gone..."
    scene dinner_day4home_2 with dissolve
    m "Oh but, he doesn't expect you to work on weekends, too, does he?"
    pc "No... as I said, I'm only expected to be there a few days per week."
    pc "In fact, since we settled everything today, I don't even need to go there next week, but will start working from here tomorrow."
    scene dinner_day4home with dissolve
    m "Oh, that's nice. But don't forget to take enough breaks in between."
    pc "Yeah, sure, I'm not a workaholic, [m]..."
    scene dinner_day4home_3 with dissolve
    m "That's good to hear."
    pcthink "Jeez, is she just acting or does she really want me to stay home..."
    scene dinner_day4home2 with dissolve
    pcthink "...and why would she want me to be here?"
    scene dinner_day4home2_2 with dissolve
    e "..."
    pcthink "Cute..."
    scene black with fade
    jump rachelGivePills
    
label homeday4night:
    n "At night..."
    scene pcroom night with dissolve
    pcthink "Shit, maybe I should have used the opportunity to ask [m] some more questions when she was under the influence of the pills..."
    pcthink "..."
    pcthink "...maybe tomorrow..."
    pcthink "..."
    pcthink "Hum... it's really late..."
    pcthink "[e] should be here by now..."
    pcthink "..."
    scene pcroom_homenight4 with dissolve
    pcthink "I wonder if she's embarrassed about what happened in her room earlier today..."
    scene pcroom night with dissolve
    pcthink "Nah... I don't think so..."
    pcthink "She wasn't really shy about it, and she {b}did{/b} return the kiss after all..."
    pcthink "It's probably [m] who told her to stay in her room again, even though... I haven't heard her talking to [e]..."
    scene pcroom_homenight4 with dissolve
    pcthink "..."
    scene pcroom night with dissolve
    pcthink "Anyway, I better get some sleep..."
    stop music fadeout 2
    scene black with fade
    play sound "audio/BadDream.mp3" loop
    scene dream_01 at dream with dissolve
    m "[bpc]! WHAT THE HELL DID YOU DO THIS TIME?" with hpunch
    oc "Calm down, [m]. It doesn't help to yell at [himher]."
    m "WHAT DO YOU KNOW? YOU DON'T HAVE TO LIVE WITH THIS..."
    oc "CALM DOWN!"
    m "Humph... fine..."
    m "So what did [heshe] do this time?"
    oc "[m], you're not making this any better! Sit down and think about who you're talking to!"
    m "..."
    m "I'm sorry, [oc]... [heshe]'s just..."
    m "I just can't stand [himher] any longer..."
    stop sound fadeout 2
    $ SERachelBRAfterEBD = False
    $ SEAfterEBD = False
    $ actionsUsed = 15
    call dateTime from _call_dateTime_1

label d5morning:
    scene pcroom afterebd1 with dissolve
    pc "Yaaawn..."
    pc "..."
    pcthink "Damn dreams..."
    pcthink "...I think that day was the last time I got into a fight with those two assholes from school again..."
    pcthink "I broke the nose of one of them and hit the other one with a cane."
    pcthink "...I can't say I regret it, but it was really dumb..."
    pcthink "Without [oc] I would've ended up in jail..."
    if pcgender == "man":
        pcthink "I guess I wasn't the nicest guy around that time..."
    else:
        pcthink "I guess I wasn't the nicest girl around that time..."
    pcthink "..."
    scene pcroomwakeuplookfore with dissolve
    pcthink "[e] didn't come over..."
    pcthink "Hum..."
    scene black with dissolve
    n "You get up and make yourself ready for breakfast."
    scene breakfast_day5 with dissolve
    pc "..."
    pcthink "[e] didn't look at me once yet..."
    e "..."
    pc "Is everything alright, [e]?"
    pause .5
    scene breakfast_day5_1 with dissolve
    e "Hn..."
    pause .5
    scene breakfast_day5_2 with dissolve
    pause
    scene black with dissolve
    n "A bit later..."
    scene breakfast_day5leaving1 with dissolve
    m "We are leaving, I've made you some extra food for the day, it's in the fridge."
    pc "Thanks, [m]."
    m "If you need something else, whatever it might be, don't hesitate and give me a call, okay, Hun?"
    pc "Sure."
    scene breakfast_day5leaving2 with dissolve
    pcthink "Why is she so nice to me today? Huh? ...what's up with [e]?!"
    scene breakfast_day5leaving3 with dissolve
    pcthink "Huh?"
    scene breakfast_day5leaving4 with hpunch
    pc "Whoa!"
    pause
    scene breakfast_day5leaving5 with dissolve
    pcthink "Wow, [e]..."
    scene breakfast_day5leaving6 with dissolve
    e "..."
    pc "Heh... you should probably go, or you'll be late... We can talk later, okay?"
    e "Hn!"
    scene breakfast_day5leaving8 with dissolve
    pcthink "Wow, that came out of nowhere..."
    scene breakfast_day5leaving9 with dissolve
    pcthink "Err... Looks like I'm not the only one who's surprised."
    m "..."
    scene breakfast_day5leaving10 with dissolve
    pcthink "Phew... [m] didn't say a word, but that look on her face... I wonder what she was thinking."
    scene black with dissolve
    $ actionsUsed = 1
    call dateTime from _call_dateTime_14
    play music mainbgm fadein 1
    scene pcroom with dissolve
    pcthink "Anyway, I should probably start working on the project for [boss], I have a lot to do and I don't have that much time..."
    scene black with fade
    n "You spend the rest of the morning and afternoon working on the project, only taking short breaks to go to the bathroom or get some snacks from the kitchen."
    scene pcroomcodingwork with dissolve
    pcthink "Ugh, this won't work either..."
    pcthink "Damn, where is the error?"
    pcthink "...gaaawd, I need a break..."
    scene pcroomcodingwork2 with dissolve
    pcthink "I think I've heard [e] and [m] coming back a while ago and it sounded like there was someone else as well..."
    scene pcroomcodingwork with dissolve
    pcthink "Maybe I should just stop for today..."
    jump tcoerce2
    
label porn_vr_4:
    n "A while later..."
    pause .5
    "Voice" "Mphh... mphhh..."
    if _in_replay:
        show screen endRep
    scene porn_vr4 with dissolve
    pause 1
    pcthink "Gawd, I love these girls!"
    if pcgender == "woman":
        pcthink "Too bad there's no girl on girl action..."
    pause
    "Girl 2" "Are you about to cum babe?"
    pcthink "Hehe, yeah spray that load all over them!"
    pause 1
    scene pornvr4_end with slowdissolve
    pause
    pc "What!? Are you fucking serious? That's even worse than in porn games..."
    scene pcroomafterpornvr4_1 with dissolve
    pcthink "Fuck..."
    pcthink "...that was... unsatisfying..."
    $ renpy.end_replay()
    pc "..."
    pcthink "Hum... shit, isn't it dinner time already?"
    pcthink "I guess I'll have a look..."
    scene pcroom_aftercodingwork with dissolve
    pcthink "It's funny how quick I got used to [m] making dinner every evening... or breakfast..."
    play sound "audio/door-opening.ogg"
    scene kitchen_e_searchforfood0 with dissolve
    pcthink "Huh? Isn't [m] making dinner today?"
    scene kitchen_e_searchforfood1 with dissolve
    pcthink "[e]?"
jump makedinnerwithE
    
label d6morning:
    play music mainbgm fadein 1
    pc "YAAAAWN..."
    scene pcroomwakeupd6 with slowdissolve
    pause .5
    pc "..."
    pcthink "[e] is gone again..."
    pause 1
    pc "..."
    scene pcroom_d6_wakeup2 with hpunch
    pc "Wait!"
    pcthink "Did that really happen last night?"
    pcthink "...did we really...?"
    pc "..."
    pcthink "T-that's impossible, she's my little sister..."
    pcthink "Err, I mean, she's not, but still..."
    scene pcroomwakeupd6 with slowdissolve
    pcthink "...and wouldn't she be here if we..."
    pcthink "Wait, what time is it?"
    scene pcroom_d6_wakeup3 with dissolve
    pause .5
    pcthink "Ugh, shit, I overslept... dammit!"
    pcthink "I better get up, I still have a lot of work to do..."
    scene black with slowdissolve
    n "You get up, make yourself ready and start working on the project again for a while."
    scene pcroomcodingwork with slowdissolve
    pcthink "There we go... this should work nicely..."
    pc "Ugh...yaaawn..."
    pcthink "I could use a break..."
    pcthink "Maybe I should take a walk... get some fresh air... get a coffee..."
    if hnumber:
        pcthink "...coffee... I could visit the girl... [h] at the cafe."
        scene coffeehouse_h_number_memory with dissolve
        pcthink "Oh right, she gave me her number, I totally forgot about that!"
        #
        pcthink "Hum... should I call her?"
        menu:
            "Call her?"
            "Call her!":
                scene pcroom_d6_callh with dissolve
                pcthink "Yeah, she's cute... and..."
                pcthink "... she seems to be the only normal girl I've met since I'm back home..."
                scene pcroom_d6_callh2 with dissolve
                pcthink "I'm going to call her, let's see where this is going."
                play sound "audio/call.ogg" loop
                pc "..."
                stop sound
                h "Yes?"
                pc "Hey, it's me, [pc], the one from the..."
                h "Oh, hey, [pc]! Hi! How are you?! How have you been?"
                pc "Err, I'm good, how are you?"
                h "Good, I'm really good, I've been waiting for... for you to show up at the cafe again, haha."
                pc "Well I was about to go for a walk and get a coffee, are you there?"
                h "Yes! Of course! Oh you mean at the cafe, right? Haha."
                pc "Yeah. Aren't you working today?"
                h "I-I am, haha. Of course, I'll be there, just come over whenever you want!"
                pc "Whenever I want?"
                h "Yes, sure! Ehm... I mean, during working hours of course, haha... I mean... yes working hours... haha."
                pc "Heh, alright, I'll be there soon, reserve a table for me."
                if pcgender == "man":
                    h "Of course, sir! Haha."
                else:
                    h "Of course, ma'am! Haha."
                pc "Haha, later, [h]."
                h "Later, [pc]."
                #
                n "You wait for a second before hanging up, and you're sure that she didn't hang up before you."
                #
                pcthink "Damn, she's cute."
                $ hlo = 3
            "Nah, not now.":
                pcthink "Nah, I just want to get a coffee..."
    pcthink "Alright, let's go!"
    scene home_hall_entrance_idle with dissolve
    $ actionsUsed = 7
    call dateTime from _call_dateTime_15
    $ storyEvent = True
    call screen map_home_hall_entrance

label d6_backhome:
    scene backhome_rachel_phone_topcroom with dissolve
    pcthink "Alright..."
    scene pcroom_d6_inc with dissolve
    pcthink "Time to get back to work... well, at least for a bit, we don't want to overdo it."
    play sound "audio/lightswitch.ogg"
    scene pcroom_d6_inc1 with dissolve
    pcthink "Huh? Why is my computer on?"
    pcthink "Didn't I shut it down?"
    scene pcroom_d6_inc2 with dissolve
    pcthink "What the..."
    pcthink "Did I...?"
    pcthink "No I didn't search for this!"
    pcthink "Did [e] use my computer again?!"
    pcthink "Incest, huh?"
    pcthink "Interesting..."
    pcthink "A little bit late now though..."
    pc "..."
    scene black with fade
    jump d6_rachel_pills

label d6_night:
    
    $ storyEvent = False
    $ visit_cafe_d6 = False
    $ visit_work_d6 = False
    $ actionsUsed = 8
    call dateTime from _call_dateTime_17
    jump d7_wakeup
    
label d7_wakeup:
    pause 1
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    if jlo >= 2:
        scene pcroomd7wakeup_j1 with slowdissolve
        pc "Uh..."
        scene pcroomd7wakeup_j2 with dissolve
        j "Unn..."
        scene pcroomd7wakeup_j3 with dissolve
        m "{size=-10}[e], are you there? Come on, we need to get going soon!{/size}"
        j "Oh shit!"
        play sound "audio/knock-door2.ogg"
        n "*Knock* *Knock* *Knock*"
        scene pcroom_d7_wakeup_j4 with dissolve
        j "We totally overslept."
        pc "Yeah, damn it!"
        m "{size=-10}[pc]?{/size}"
        play sound "audio/knock-door1.ogg"
        n " *Knock* *Knock*"
        scene pcroom_d7_wakeup_j5 with dissolve
        m "{size=-10}I'm coming in!{/size}"
        j "Now we have a problem..."
        e "Unn..."
        pc "Huh?"
        scene pcroom_d7_wakeup_j6 with dissolve
        pc "What the?! [e]?" with hpunch
        pcthink "Shit, shit, shit, this is bad! I need to do something!"
        scene pcroomd7wakeup_j7 with dissolve
        menu:
            "Push [j] out of the bed.":
                $ mob += 1
                $ jlo -= 1
                $ efe += 1
                $ jpushed = True
                play sound "audio/door-opening.ogg"
                scene pcroomd7wakeup_j9_2 with vpunch
                j "WHAA!"
                play sound "audio/drop.ogg"
                scene pcroom_d7_wakeup_j11_2_1 with dissolve
                m "What the!?"
                j "Auu..."
                m "[j]?!"
                scene pcroom_d7_wakeup_j11_2_2 with dissolve
                e "NN!"
                scene pcroom_d7_wakeup_j11_2_3 with dissolve
                m "[e]?!"
                pcthink "Oh shit, that was stupid!"
                scene black with fade
            "Hide [e] under the blanket.":
                $ jlo += 1
                scene pcroomd7wakeup_j9 with dissolve
                pcthink "Right, I can't hide both of em!"
                e "Ehh?!"
                pc "{size=-10}Hush, [e]!{/size}"
                j "WHAAA!"
                play sound "audio/door-opening.ogg"
                scene pcroom_d7_wakeup_j10 with dissolve
                pcthink "Oh shit, I forgot that [j] is naked."
                scene pcroom_d7_wakeup_j11 with dissolve
                m "[j]?!"
                j "Uhh... morning [m]... hehe..."
                m "What on earth is going on here?"
                pc "Err... this is not what it's... uhh..."
                pcthink "Shit!"
                pc "Well it {b}{i}is{/i}{/b} what it looks like..."
                m "Why didn't you tell me?!"
                j "Sorry, that's my fault..."
                m "Uhm..."
                pcthink "Shit, I hope she didn't see [e]!"
                m "You... you haven't seen [e], have you?"
                pcthink "Phew..."
                pc "Err... no... no I haven't..."
                scene pcroom_d7_wakeup_j12 with dissolve
                j "I think I've heard her opening her door a while ago."
                scene pcroom_d7_wakeup_j12_2 with dissolve
                m "Umm... okay..."
                pc "..."
                j "Hehe..."
                m "Does she... know about..."
                m "...this?"
                j "Umm... yeah, I told her, hehe."
                m "...okay..."
                j "..."
                m "Uhh... right, well I... I'll make some breakfast..."
                play sound "audio/door_close.ogg"
                scene pcroom_d7_wakeup_j13 with dissolve
                pause 1
                scene pcroom_d7_wakeup_j14 with dissolve
                j "[e], you better hurry!"
                scene pcroom_d7_wakeup_j15 with dissolve
                e "Hn!"
                scene black with dissolve
                n "[e] jumps up and quickly runs out the balcony."
                scene pcroom_d7_wakeup_j16 with dissolve
                pc "Huh? [e], wait!"
                scene pcroom_d7_wakeup_j16_jump with dissolve
                pc "..."
                pc "Damn, I hope [m] doesn't see her like this..."
                scene pcroom_d7_wakeup_j17 with dissolve
                j "..."
                scene black with fade
    else:
        m "Are you awake, Hun?"
        pc "...ugh... Yeah, I'm awake..."
        #
        m "Good morning, Hun."
        pc "...what's up, [m]?"
        if mob > 4:
            m "Oh, I thought I might ask if you want some breakfast? I hope that's okay? Did I wake you up, Hun?"
        else:
            m "Well, breakfast is ready, and you have some work to do, right?"
        pc "Uhn... I'm coming..."
        m "Alright~"
        #
        pcthink "Damn... she's almost acting as if she's my real mother..."
        scene black with fade
            
    jump d7_breakfast
    
label d7_breakfast:
    $ actionsUsed = 2
    call dateTime() from _call_dateTime_18
    if jlo == 0:
        scene d7_breakfast3_3 with dissolve
        pcthink "Looks like [j] is gone already..."
        m "So, what are your plans today, Hun?"
        pc "Err... work, I guess..."
        m "Oh, I bet you're making good progress?"
        pc "Yeah, kind of."
        m "That's good to hear."
        scene black with dissolve
        n "You continue to make  small talk for a bit until [m] and [e] get ready to leave..."
    else:
        scene d7_breakfast4 with dissolve
        pc "..."
        m "..."
        j "..."
        if jpushed:
            pcthink "Shit, nobody is saying anything..."
            pcthink "Looks like I really fucked up..."
            pcthink "Everybody seems to be mad at me..."
            pc "..."
            pc "So, uh..."
            menu:
                "Tell them you're sorry.":
                    $ jlo += 1
                    $ efe -= 1
                    pc "...about what happened..."
                "Talk about the weather.":
                    $ mob += 1
                    pc "Looks like it's going to be a nice day today..."
                    if mob < 3:
                        scene d7_breakfast with dissolve
                        m "Humph... don't you think you should apologize to someone?"
                    else:
                        scene d7_breakfast2_2 with dissolve
                        j "Pff, is that all you have to say?"
            scene d7_breakfast with dissolve
            m "That was not nice, [pc]."
            scene d7_breakfast2_2 with dissolve
            j "Yeah, that really hurt."
            pc "I'm sorry... I was surprised and just reacted..."
            j "...humpf... so it was \"just\" a reaction, huh?"
            pc "Yes, it wasn't on purpose!"
            j "Humph..."
        else:
            scene d7_breakfast5 with dissolve
            j "So uhh... I hope you don't mind me having spent the night here, [m]."
            m "..."
            scene d7_breakfast6 with dissolve
            m "Well... you should have asked me first."
            scene d7_breakfast5 with dissolve
            j "I know, but... it was kinda unexpected."
            scene d7_breakfast7 with dissolve
            m "Unexpected?"
            j "Yeah, hehe."
            m "..."
            scene d7_breakfast8 with dissolve
            pcthink "Hum... looks like [j] doesn't want to tell her what really happened..."
            scene d7_breakfast5 with dissolve
            j "But I'll stay at home tonight, so [pc]'s bed will be free, hehe."
            pcthink "Uh-Oh..."
            scene d7_breakfast2 with dissolve
            j "[e] can have her big [bs] all for herself again, or maybe even..."
            scene d7_breakfast3_2 with hpunch
            m "[j]!"
            m "That's is not funny!"
            j "Sorry..."
            pcthink "I knew it..."
            scene black with fade
    n "A little bit later."
    play music mainbgm fadein 1
    scene d7_breakfast9 with dissolve
    pcthink "Well... everybody is gone..."
    pcthink "..."
    pcthink "Hum, I guess I should get some work done..."
    scene black with fade
    n "An hour later."
    scene pcroom_d7_coding with dissolve
    pc "..."
    extend "."
    extend "."
    extend "."
    pcthink "Naaaaaaaaw... I can't think... not a single line of code done..."
    pcthink "I'm tired, I'm bored... I can't work like this."
    pcthink "I need to do something else..."
    pc "..."
    pcthink "I'll go for a walk..."
    $ SEd7walk = True
    jump entrance

label d7_evening:
    scene d7_bathroom_tp with fade
    pcthink "Damn, that was embarrassing... everyone was staring at me..."
    pcthink "I don't get it, why would you ever need so much toilet paper?"
    pc "..."
    pcthink "Anyway, I better get some work done now..."
    scene black with fade
    
label d7_home:
    n "Later..."
    scene pcroom_d7_coding with dissolve
    pcthink "Alright, that's better. At least {b}some{/b} progress..."
    if SEWork == 2:
        scene pcroom_d7_codingcj with dissolve
        pcthink "Huh?"
        scene cjd0
        pause
        scene cjd0_1
        pause
        scene cjd1
        pause
        scene cjd2
        pause
        pcthink "Oh shit! It's the boss!"
        scene cjd3
        pause
        scene cjd4
        pause
        scene cjd5
        pause
        scene cjd6
        pause
        scene cjd7
        pause
        scene cjd8
        pause
        scene cjd9
        pause
        scene cjd10
        pause
        scene cjd11
        pause
        pc "..."
        extend "."
        extend "."
        extend "."
        scene cjd12
        pause
        scene cjd13
        pause
        scene cjd14
        pause
        scene cjd15
        pause
        scene cjd16
        pause
        scene cjd17
        pause
        scene cjd18
        pause
        scene cjd19
        pause
        scene cjd20
        pause
        scene cjd21
        pause
        scene cjd22
        pause
        if stl > 0:
            scene cjd23
            pause
            scene cjd24
            pause
            scene cjd25
            pause
            scene cjd26
            pause
            scene cjd27
            pause
            scene cjd28
            pause
            scene cjd29
            pause
            scene cjd30
            pause
            scene cjd31
            pause
            scene cjd32
            pause
            scene cjd33
            pause
        else:
            scene cjd23_2
            pause
            scene cjd24_2
            pause
            scene cjd30_2
            pause
            scene cjd31_2
            pause
            scene cjd32_2
            pause
            scene cjd33_2
            pause

        pcthink "So [st] told him about my visit... I wonder why they were talking about me."
    jump d7_evening_e
    
label d8_morning:
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    scene d8_wakeup1 with dissolve
    pc "Uhh..."
    scene d8_wakeup3 with dissolve
    m "Time to get up, [e]..."
    scene d8_wakeup_e with dissolve
    e "Uhnn..."
    if d72esbed:
        pcthink "...of course she snuck over again..."
    scene d8_wakeup3 with dissolve
    if mob < 3:
        m "... and [pc] as well."
    else:
        m "... do you want to have breakfast with us, [pc]?"
    pc "*YAAAWN*... yeah..."
    pcthink "... [m] really {b}has{/b} changed..."
    scene black with fade
    scene d8_breakfast with dissolve
    n "You and [m] engage in some small talk again, you can't help but wonder if this is how a normal family would have their breakfast..."
    scene black with fade
    m "See you later, Hun."
    pc "Later..."
    pc "..."
    scene d7_breakfast9 with dissolve
    pcthink "Shit... I'm almost starting to enjoy the time here..."
    pcthink "[m] really changed, but I'm sure she's still hiding something from me."
    pc "..."
    pcthink "I wonder why she didn't mention anything about [e] sleeping in my bed again..."
    pcthink "Maybe she's starting to accept it?"
    pcthink "...or she just gave up trying..."
    scene d7_breakfast10 with dissolve
    pcthink "Well, whatever, I have work to do..."
    scene black with fade
    n "A few hours later..."
    
    jump d7_motel
    
label d8_eveningWJada:
    scene d8_hall_j15 with dissolve
    pcthink "Hum, I just hope [m] remembers when the pills wear off..."
    pcthink "Maybe I should keep everyone together until the pills wear off. She {b}{i}has{/i}{/b} to remember when I don't give her the chance to think about anything else..."
    scene d8_hall_j16 with dissolve
    pc "Hey, how about we celebrate this with a... err... with something, haha."
    scene d8_hall_j17 with dissolve
    j "Yeah, why not, hehe."
    scene d8_hall_j18 with dissolve
    m "Oh, that's a great idea, I'll make us some drinks!"
    scene d8_hall_j19 with dissolve
    j "Uhh..."
    scene d8_hall_j20 with dissolve
    j "...but better nothing alcoholic... hehe...heh..."
    scene d8_hall_j19 with dissolve
    m "Huh? Of course not, you know that we won't have alcohol in this house, honey."
    scene d8_hall_j21 with dissolve
    j "Uhh... yeah, hehe..."
    scene d8_hall_j22 with dissolve
    j "{size=-10}Did she just call me honey?{/size}"
    pc "{size=-10}Yeah, it sounded like it...{/size}"
    j "Weird..."
    scene black with fade
    scene d8_lr01 with dissolve
    j "...and then she was like \"What the hell was that?!\", haha."
    scene d8_lr04 with dissolve
    pc "Damn, that must have looked funny."
    scene d8_lr01 with dissolve
    j "Yeah it did! Haha."
    scene d8_lr04 with dissolve
    pc "You better not do that here though, as funny as it sounds..."
    scene d8_lr03 with dissolve
    j "Don't worry, I promise I won't cause you any trouble."
    scene d8_lr04 with dissolve
    pc "Good, otherwise I'd have to send you back to that creepy old perv."
    scene d8_lr03 with dissolve
    j "...and we don't want that, hehe."
    scene d8_lr05 with dissolve
    j "Thanks again by the way, [m]. It's really nice of you to let me stay here..."
    scene d8_lr02 with dissolve
    m "..."
    pc "[m]?!"
    scene d8_lr06 with dissolve
    m "Hm?"
    pcthink "Shit, looks like the pills are going to wear off..."
    pc "[j] said thank you for letting her stay."
    scene d8_lr07 with dissolve
    m "Letting her..."
    scene d8_lr08 with dissolve
    j "Yeah, thanks, [m]. You're a life saver!"
    pcthink "I better try to remind her about the talk we had..."
    scene d8_lr09 with dissolve
    pc "Yeah, now [e] has her BFF here, and err... we \"have her close\" ..."
    pc "Err...to keep an eye on her!"
    scene d8_lr10 with dissolve
    j "Hey, I'm sitting right here you know."
    pc "Of course I know."
    e "Khehehe."
    scene d8_lr11 with dissolve
    j "Aww, stop laughing [e], they will probably monitor us 24/7!"
    pc "Haha, every second."
    scene d8_lr12 with dissolve
    if pcgender == "man":
        j "Dick!"
    else:
        j "Bitch!"
    pc "Haha."
    scene d8_lr13 with dissolve
    m "[j], I don't want to hear any swear words in this house, so if you want to stay here for a while, you better stop that!"
    scene d8_lr14 with dissolve
    j "Uhh... sorry, no swear words anymore..."
    pcthink "Phew, looks like it worked..."
    scene black with fade
    n "Later..."
    e "HNNN!"
    pc "Right! Go right!"
    j "I know!"
    scene d8_jvr01 with dissolve
    e "NN!"
    pc "Watch out, behind you!"
    scene d8_jvr02 with dissolve
    j "Fuuuuuck!"
    j "Aww damn it, I almost got her..."
    pc "Welp..."
    scene d8_jvr03 with dissolve
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    if mob > 6:
        #scene d8_jvr04_0 with dissolve
        pc "..."
        pc "Yes?"
    scene d8_jvr04 with dissolve
    m "Hey, are you having fun?"
    scene d8_jvr04_2 with dissolve
    j "Naaaw... I just lost..."
    m "That's... well..."
    scene d8_jvr05_2 with dissolve
    m "Anyway, [pc], I'm going to bed and I just wanted to make sure that..."
    if mob < 3:
        m "...well, I'm sure it isn't necessary, but I wanted to remind you that [e] has her own room and I expect [j] to sleep in [e]'s room, too."
    else:
        m "Umm... well, I... I just wanted to remind you that this is {b}{i}your{/i}{/b} room, [e] has her own room and bed and [j] is her best friend so..."
        m "I..."
    m "I just wanted to make sure that you all remember that."
    pcthink "Jeez, is she serious now?"
    j "Oh don't worry [m]..."
    scene d8_jvr06_2 with dissolve
    j "Of course we remember that..."
    scene d8_jvr06 with dissolve
    j "[e] and I will of course sleep in [e]'s room."
    pc "Huh?"
    e "Eh?"
    m "Oh really?!"
    scene d8_jvr06_2 with dissolve
    j "Of course, and I'll make sure that everyone stays in their respective beds."
    scene d8_jvr06_0 with dissolve
    m "That's, umm... well thanks [j]..."
    pcthink "Wow, [j] really wants to make a good impression..."
    m "Okay then... have a good night everyone..."
    j "Good night, [m]."
    scene d8_jvr07 with dissolve
    j "Well, I guess that means we should go to bed, huh, [e]?"
    scene d8_jvr09 with dissolve
    e "Unh..."
    scene d8_jvr09_2 with dissolve
    j "Oh come on [e], I don't want to get kicked out again!"
    scene d8_jvr08 with dissolve
    pc "Well, I guess she's right, let's play along, okay?"
    scene d8_jvr09_2 with dissolve
    pause 1
    scene d8_jvr10 with dissolve
    pause 1
    n "You expect a simple goodnight kiss, but right when your lips meet, you can feel [e]'s tongue sliding into your mouth..."
    scene ekiss_00 with dissolve
    show d8jvrekiss
    pause
    scene d8_jvr11 with dissolve
    j "Hehe, cute!"
    if not harem or jlo < 2:
        j "Good night, [pc]."
        pc "Night, [j], night, [e]."
    elif not harem and jlo > 1:
        scene d8_jvr12 with dissolve
        j "Night..."
        scene d8_jvr13 with dissolve
        j "{size=-15}[pcmd]{/size}."
        n "*Smooch*"
        scene d8_jvr15 with dissolve
        pc "Night, [j]..."
        scene d8_jvr16 with dissolve
        pc "Heh, night, sweetie."
        scene d8_jvr14 with dissolve
        e "Hn!"
    else:
        scene d8_jvr12 with dissolve
        j "Good night, [pcmd]..."
        scene jkiss_00 with dissolve
        show d8jvrjkiss
        pause
        scene d8_jvr12 with dissolve
        pc "Heh... good night, babygirl."
        scene d8_jvr14 with dissolve
        pc "Night, sweetie."
        e "Khehe!"
    scene black with slowdissolve
    n "A bit later..."
    scene pcroomday2night1 with dissolve
    j "{size=-10}Hahaha... yes!{/size}"
    n "You can hear [j]'s voice through the wall."
    j "{size=-10}Do you think...{/size}"
    pcthink "Looks like [e] and [j] are still awake..."
    j "{size=-10}Haha, nooo, I'll help you, but that's too...{/size}"
    j "{size=-10}...yes!{/size}"
    j "{size=-10}...really like [himher]!{/size}"
    pcthink "Damn, I can't understand all of it."
    j "{size=-10}...really sure about it?{/size}"
    n "From this point on you can only hear some whispering, but can't understand a word."
    pcthink "Hum... I wonder what they were talking about..."
    stop music fadeout 2
    scene black with fade
    #dream
    
label d9_wakeup:
    play sound "audio/BadDream.mp3" loop
    scene dream_01 at dream with dissolve
    n "*Sniff*"
    n "*Wimper*"
    pc "Huh? What's wrong, [m]?"
    m "*Sniff* ...oh..."
    m "I'm sorry, [pc], it's nothing..."
    pc "Where's Dad?"
    m "*Sniff* ...he didn't tell you?"
    pc "Uh-uh."
    m "He got suspended and is attending the hearing... [oc] just picked him up..."
    pc "Why did he get suspended?"
    m "*Sniff* ...I don't know, he didn't tell me... he was probably drunk again..."
    pc "Does that mean he will be home more often from now on?"
    m "*Sniff* ...yes..."
    m "[oc] said that your Dad will probably stay home for a while from now on..."
    pc "Did [oc] get suspended too?"
    m "No, but he has to attend the hearing too."
    stop sound fadeout 2
    $ storyEvent = True
    scene black with fade
    
    $ actionsUsed = 15
    call dateTime from _call_dateTime_21
    
label d9_breakfast:
    play music mainbgm fadein 1
    scene d9_breakfast0 with dissolve
    pc "Morning everyone."
    m "Good morning, hun."
    scene d9_breakfast01_2 with dissolve
    m "Nice shirt."
    pc "Thanks..."
    scene d9_breakfast01 with dissolve
    m "Oh by the way [j], I didn't see you bring any of your stuff yesterday?"
    scene d9_breakfast02 with dissolve
    j "Yeah, most of it is still in the apartment..."
    scene d9_breakfast03 with dissolve
    m "I see, you should get it here soon if you plan to stay for a bit longer..."
    scene d9_breakfast02 with dissolve
    j "Yeah..."
    scene d9_breakfast11 with dissolve
    m "It will surely help to make you feel at home."
    scene d9_breakfast04 with dissolve
    j "Oh thanks, I feel at home already, I mean, the only place I've ever had a breakfast like this is here."
    scene d9_breakfast03 with dissolve
    m "Really? You don't eat breakfast together with your mom?"
    scene d9_breakfast10 with dissolve
    j "No, but I always liked it when I was staying here overnight. It feels like... having a real family."
    scene d9_breakfast03 with dissolve
    m "I didn't know that it meant so much to you..."
    scene d9_breakfast02 with dissolve
    j "It kinda makes me feel like having a real family..."
    pcthink "Damn, I know how she feels..."
    scene d9_breakfast05 with dissolve
    j "By the way, [pc], did you ever call [m] Mom?"
    pc "Eh?"
    scene d9_breakfast06 with dissolve
    m "[j] you know that I'm not [hisher] mom."
    e "Khehehe."
    scene d9_breakfast07 with dissolve
    m "...I mean... I wouldn't mind..."
    pc "Err..."
    scene d9_breakfast08 with dissolve
    menu:
        "Call her Mom.":
            $ mmom = "Mom"
            pc "Well, I guess I could..."
            scene d9_breakfast08_3 with dissolve
            m "Oh, but you don't need to if you feel uncomfortable about it."
            pc "Nah, it's okay..."
            pc "..."
            pc "...[mmom]."
            scene d9_breakfast08_2 with dissolve
            m "..."
            scene d9_breakfast08 with dissolve
            m "Umm..."
            scene d9_breakfast11 with dissolve
            m "A-Anyway... [j]. Me and [e] will go shopping and pick up some groceries after breakfast, why don't you come with us so we can get your stuff on our way back?"
            scene d9_breakfast10 with dissolve
            j "Yeah, why not."
        "Change the topic.":
            scene d9_breakfast09_2 with dissolve
            pc "...well about your stuff in the apartment, [j]..."
            j "Hm?"
            scene d9_breakfast11 with dissolve
            m "Right, you can come and help me and [e] with the groceries after breakfast, we can get your stuff on our way back."
            scene d9_breakfast12 with dissolve
            j "Uhh..."
            scene d9_breakfast13 with dissolve
            j "...well, okay."
            pcthink "Hmm... I have the feeling that she had some other plans..."
    scene black with dissolve
    n "After everyone is done eating you're surprised to see [j] helping with the dishes instantly."
    pcthink "Hum... she's full of surprises..."
    n "Since there's nothing left to do, you decide go back to your room and do some work..."
    scene black with fade
    
    scene d9_pcroom_work1 with dissolve
    pc "..."
    extend "."
    extend "."
    extend "."
    pcthink "Hum... that's weird..."
    pcthink "...something doesn't fit..."
    m "[pc]?"
    scene d9_pcroom_work0_0 with dissolve
    pc "Hm?"
    scene d9_pcroom_work0_1 with dissolve
    m "Didn't you hear me knocking?"
    scene d9_pcroom_work0_0 with dissolve
    pc "Uh... no, what's up?"
    scene d9_pcroom_work0_2 with dissolve
    m "We're leaving, do you need anything from the city?"
    scene d9_pcroom_work0_3 with dissolve
    pc "Hm? Ah, no... nothing."
    scene d9_pcroom_work0_2 with dissolve
    m "Okay, see you later then."
    scene d9_pcroom_work0_0 with dissolve
    pc "Yeah, later..."
    pc "[mmom]."
    if mmom == "Mom":
        scene d9_pcroom_work0_3 with dissolve
        pause .9
    play sound "audio/door_close.ogg"
    scene d9_pcroom_work0 with dissolve
    pause .5
    if mmom == "Mom":
        pcthink "Ugh... calling her mom feels really weird..."
        pcthink "Why am I even doing this... I don't trust her god dammit..."
        scene d9_pcroom_work1 with dissolve
        pcthink "Shit... better get back to work... I don't want to think about stuff like that..."
    scene d9_pcroom_work1 with dissolve
    pc "Hum..."
    pcthink "...there seems to be something missing..."
    pcthink "Hum..."
    extend "."
    extend "."
    extend "."
    scene d9pcroomwork3 with dissolve
    pause .5
    scene d9pcroomwork2 with dissolve
    pause .5
    scene d9_pcroom_work1 with dissolve
    pc "..."
    st "...yes?"
    pcthink "As I thought, she's working at the weekend again..."
    pc "Hey, [st], I'm just working on the project, but I think I'm missing some files, could you check the files you sent me?"
    st "Uhm... yes, give me a minute..."
    pc "Okay, thanks."
    pc "..."
    extend "."
    extend "."
    extend "."
    st "This... might be a problem..."
    pc "What do you mean?"
    st "It looks like [boss] forgot to include the latest data, but I'll have to check some older files to make sure, there's definitely something missing though."
    pc "Okay... sounds like it'll take a while?"
    st "Yes..."
    pc "Hum... okay, well it looks like I'll have an actual weekend then."
    st "Sorry... I'll send them to you as soon as I can."
    pc "Yeah no sweat, it's the weekend we shouldn't be working in the first place..."
    st "..."
    pc "Thinking about it, I don't have much else to do, so maybe I'll come over later."
    st "..."
    st "Okay."
    pc "Well... maybe later then."
    st "L-later..."
    scene d9pcroomwork4 with dissolve
    pause .5
    scene d9pcroomwork3 with dissolve
    pause .5
    scene d9_pcroom_work1 with dissolve
    pcthink "Hum... I don't get that woman..."
    pcthink "Anyway, what am I going to do now?"
    n "*BZZZZZ*"
    scene d9pcroomwork23 with dissolve
    pcthink "Huh? Did she forget anything?"
    scene d9_pcroom_work1 with dissolve
    pc "What's up [st], did you forget anything?"
    ma "Hello, this is [ma] Shelter."
    pc "Ma..."
    pcthink "Oh right, the office secretary from the rental company."
    pc "Sorry I thought you were my co-worker, I just talked to her."
    ma "No problem, do you want me to call again another time?"
    pc "No, it's okay, [ma], what do you need?"
    ma "I have some good and some bad news for you, which one would you like to hear first?"
    menu:
        "The good news.":
            ma "We are ready to refund your deposit for the apartment, all I need is your signature on a few documents."
            pc "Okay, so what's the bad news then?"
            ma "I still don't have any news on another apartment."
            pc "Well, that's no big problem for now, I have somewhere to stay for a while."
            ma "Good to hear."
            ma "Do you want me to send you the documents via email?"
            jump d9_leavehome
        "The bad news.":
            ma "I still don't have any news on another apartment."
            pc "Well, that's no big problem for now, I have somewhere to stay for a while."
            ma "Oh, that's good to hear."
            pc "So what's the good news?"
            ma "We are ready to refund your deposit for the apartment, all I need is your signature on a few documents."
            pc "Good, can you send them over?"
            ma "Sure."
            ma "Do you want me to send them via email?"
            jump d9_leavehome
            
label d9_leavehome:
    pc "I sadly don't have a printer here..."
    ma "Oh, well I can send them by post, but you could also come over during business hours, our office is in the same city."
    pc "Okay, I could come over Monday, what's the address?"
    ma "It's... well, actually..."
    pc "Hmm?"
    ma "We usually don't accept customers on sunday, but I wanted to do some overtime anyway, so you could come over after closing time if you want."
    pc "Hmm, yeah sounds good, I was thinking about going to the city anyway."
    ma "Okay, the address is..."
    scene black with dissolve
    n "You note the address and even though it's still a lot of time until closing time, you get ready to leave..."
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance
    
label d9_backhome_pcroom:
    n "A while later..."
    scene d9_movie00 with dissolve
    pause
    scene d9_movie01 with dissolve
    j "The movie is better than I thought, if only the screen was bigger..."
    scene d9_movie02 with dissolve
    j "How come you don't have a TV?"
    scene d9_movie03 with dissolve
    pc "I had one, but it broke when I was packing my stuff before moving."
    scene d9_movie04 with dissolve
    j "Oh shit, that sucks, you really should get a new one."
    scene d9_movie05 with dissolve
    pc "Yeah, you're right..."
    scene d9_movie06 with dissolve
    j "Hey, looks like he's going to bang the princess, hehe."
    pcthink "[j]... always naughty..."
    scene black with fade
    j "Night, [pcmd]."
    pc "Night you two."
    scene d9end01 with dissolve
    pcthink "Well, I guess I'm going to bed too..."
    scene d9_end02 with dissolve
    pcthink "I better file the papers somewhere before I forget about it..."
    scene d9_end03 with dissolve
    pcthink "What's this? That's not my name..."
    pcthink "Did she hand me the wrong papers?"
    pcthink "Shit, I better call her tomorrow..."
    pcthink "Oh damn, I don't have her number."
    if hlo == 3:
        scene d9end04 with dissolve
        pcthink "Huh? [h] tried to call me?!"
        pcthink "Oh shit, I wanted to text her..."
        pcthink "Wait, tomorrow is the date!"
        pcthink "Dammit, I totally forgot about that."
        scene d9_end05 with dissolve
        pcthink "Alright, I'll call her, I hope she's still awake..."
        play sound "audio/call.ogg" loop
        pause 3
        pcthink "Maybe I should send her a message instead..."
        stop sound
        h "Yes, yes, I'm awake! Ah... I mean... hi [pc]!"
        pc "Oh shit, did I wake you up? I'm sorry..."
        h "Nono, I'm totally awake, it's fine, really!"
        pcthink "Damn, she's cute."
        scene d9_end06 with dissolve
        pc "I just saw that you tried to call me and thought I'd call back."
        h "Oh, haha, I was just... uhm... since you didn't text me..."
        scene d9_end07 with dissolve
        pc "Yeah, sorry about that, it was a really busy week. Lots of stuff happened."
        scene d9_end08 with dissolve
        h "It did for sure!"
        h "So do you still want to go on a date tomorrow?"
        pc "Yes, of course!"
        h "{size=-20}Yes!{/size}... ahem... good, but uhm... the lock down basically disrupted all my plans..."
        pc "Lock down?"
        h "You didn't get the news yet? All public areas like restaurants, bars and so on are closed from tomorrow on."
        pc "What?! Why?"
        h "Uhh... you don't watch TV?"
        pc "Not much lately..."
        h "You've really been busy, haven't you?"
        pc "Yeah... sorry."
        h "It's okay, it's nice that you didn't forget about me."
        scene d9_end09 with dissolve
        pc "How could I forget such a cute girl."
        h "Haha, thanks!"
        pc "So where do you want to go tomorrow if everything's closed?"
        h "Oh I have an idea already, but I won't tell, hehe."
        pc "Oh come on, that's mean."
        h "Hehe... well, there is a nice place I'd like to go."
        pc "Where is it?"
        h "Hmm... I'll tell you this much: It's a quiet and beautiful place."
        pc "Quiet and beautiful, huh?"
        h "Yes, I think you'll like it."
        pc "I bet!"
        if pcgender == "man":
            pc "Do I need a coat and tie?"
        else:
            pc "Do I need a fancy dress?"
        h "Haha, no! You'll look good anyway..."
        pc "Now you're making me blush."
        h "Hehe... {size=-20}*yaaaaawn*{/size}"
        pc "Well, I can't wait, but I better let you sleep now."
        h "Oh I'm not tired, really!"
        pc "Heh, we'll have a lot of time to talk tomorrow, and you know what?"
        h "What?"
        pc "It will be even better, because we can see each other."
        h "Haha, right! And maybe even..."
        h "Touch... haha!"
        pc "Haha, you're cute! Good night and sweet dreams, [h]!"
        h "You too! Sweet dreams, [pc]! See you tomorrow!"
        pc "See you tomorrow, [h]!"
        scene d9end10 with dissolve
        pcthink "Wow, she's so cute..."
        scene d9_end11 with dissolve
        pcthink "I'm curious where she wants to go tomorrow..."
    else:
        pcthink "I guess I'll have to go to her office again..."
    pcthink "Anyway, time to sleep."
    stop music fadeout 2
    scene black with fade


label d9dream:
    play sound "audio/BadDream.mp3" loop
    scene dream_01 at dream with dissolve
    "Voice" "*Sniff*"
    n "You can hear a weeping noise."
    pc "Dad?"
    "Dad" "Oh hey, [pc]... *sniff*"
    n "He wipes tears from his eyes. You can see him holding a photo of your mom in his hands."
    "Dad" "You're back early..."
    pc "Are you crying, Dad?"
    "Dad" "No... *sniff* ...must've gotten something in my eye..."
    pc "..."
    "Dad" "Do you miss your mom, [pc]?"
    pc "Yes..."
    "Dad" "Hm... you should forget about her..."
    pc "I don't want to forget her!"
    "Dad" "But it's better for you... for both of us..."
    "Dad" "...and do yourself a favor and never fall in love..."
    pc "..."
    n "He puts the photo of your mom into a drawer."
    pc "Don't you love [m], Dad?"
    "Dad" "[m]?! Pff..."
    "Dad" "That b... she doesn't even know how to cook a proper meal, let alone how to suck a..."
    "Dad" "Uch... damn it..."
    "Dad" "Just always remember that she's not your mom, even if she tries to be... she's useless and she'll never be your mom!"
    pc "...okay..."
    "Dad" "Now go back to your room or go out and play or whatever you do..."
    pc "Okay..."
    n "You're about to leave the room..."
    "Dad" "[pc]?"
    pc "Yes, Dad?"
    "Dad" "I'm sorry that I..."
    "Dad" "...sometimes..."
    "Dad" "..."
    "Dad" "Never mind, just go..."
    stop sound fadeout 2
    $ actionsUsed = 15
    call dateTime from _call_dateTime_22
label d10wakeup:
    scene pcroom_wakeup01 with dissolve
    pc "Uhh..."
    pc "{cps=10}...{/cps}"
    pcthink "These dreams..."
    pcthink "...I hate them..."
    pcthink "..."
    pcthink "I think that was the only time ever I saw the old man crying..."
    pcthink "He didn't even cry at Mom's funeral..."
    pcthink "..."
    pcthink "Shit, time to get up."
    scene black with dissolve
    n "You get up and take a shower."
    
    jump d10shower
label d10pcroom:
    pcthink "Alright, what to do now... hmm..."
    play sound "audio/knock-door1.ogg"
    scene d10beforeeshow01 with dissolve
    j "Morning!"
    pc "Mornin' [j], what's up?"
    j "Follow me, I want to show you something!"
    pc "Huh? What is it?"
    scene d10beforeeshow02 with dissolve
    j "Just come, it's a surprise!"
    pc "Eh... fine..."
    scene black with dissolve
    n "You follow her to [e]'s room."
    jump d10eshow

label d10johnson:
    stop music
    play sound "audio/door-opening.ogg"
    scene d10ahd01 with dissolve
    pc "Huh?"
    scene d10ahd02 with dissolve
    pc "What's going on here? [oc]?!"
    scene d10ahd03 with dissolve
    m "Oh [pc], there was this policeman here while you were gone..."
    scene d10ahd04 with dissolve
    oc "Looks like [w] still doesn't want to give up."
    scene d10ahd05 with dissolve
    pc "[w]? Oh no, not that guy again."
    scene d10ahd06 with dissolve
    j "You know that guy?"
    pc "Sadly, yes. What happened, what did he want?"
    j "He was asking weird questions and acted like we're all gangsters..."
    scene d10ahd07 with dissolve
    oc "[m] called me after he was gone."
    scene d10ahd08 with dissolve
    m "I didn't know what to do, I was confused and scared."
    scene d10ahd09 with dissolve
    oc "It's okay, [m], he can't do anything."
    scene d10ahd10 with dissolve
    pc "Jeez, [oc], isn't there anything you can do to stop him? Do we have to get an injunction?"
    scene d10ahd11 with dissolve
    oc "It's not that easy, especially not with all the shit you've done in the past."
    scene d10ahd12 with dissolve
    pc "Oh come on, [oc], it's been years now."
    scene d10ahd11 with dissolve
    oc "Yeah, but not long enough to be removed from your file, if there's anything he can link to you, any old case, even if it's just a suspicion, he has all the rights to go after it."
    scene d10ahd12 with dissolve
    pc "Shit! So we can't do anything?"
    scene d10ahd11 with dissolve
    oc "Nobody really takes him seriously and I told the chief about your case, so as long as [w] doesn't find any hard evidence for something, he won't be able to do much more than asking questions and be as annoying as always."
    scene d10ahd13 with dissolve
    m "Will he come back?"
    scene d10ahd14 with dissolve
    oc "Possibly, but you can safely ignore him. He knows he can't do anything without getting himself into trouble."
    scene d10ahd15 with dissolve
    oc "Just don't do anything he can use as pretence."
    scene d10ahd16 with dissolve
    m "Of course not!"
    scene d10ahd17 with dissolve
    oc "That was more or less directed at [pc]..."
    scene d10ahd18 with dissolve
    oc "...and [j]."
    scene d10ahd19 with dissolve
    pc "Wait, you know each other?"
    scene d10ahd20 with dissolve
    j "Eh...haha..."
    scene d10ahd21 with dissolve
    oc "Let's just say I wasn't surprised to find her here..."
    scene d10ahd22 with dissolve
    m "[j], I didn't know you had trouble with the law?"
    scene d10ahd23 with dissolve
    j "It was an accident, I swear!"
    scene d10ahd24 with dissolve
    oc "Don't worry about it, [m], she's just a little trouble maker, I'm sure [pc] can handle her."
    j "Huh?"
    scene d10ahd25 with dissolve
    oc "Anyway, my wife is waiting, so I better take my leave. Call me if there's any trouble again."
    scene d10ahd26 with dissolve
    m "Thanks, [oc], give her my regards."
    scene d10ahd27 with dissolve
    oc "Sure."
    scene d10ahd28 with dissolve
    oc "...and you stay clear of trouble."
    pc "Eh? Sure, I'll try my best."
    scene d10ahd29 with dissolve
    oc "{size=-10}...and take good care of [j], she needs someone like you to look after her.{/size}"
    scene d10ahd30 with dissolve
    pc "I know, thanks, [oc]."
    scene d10ahd31 with dissolve
    play sound "audio/door_close.ogg"
    pc "..."
    scene d10ahd32 with dissolve
    m "So, I think there's something we should talk about, [j]... but first..."
    scene d10ahd33 with dissolve
    m "...who is that [w] guy, [pc]?"
    scene black with slowdissolve
    n "You explain the situation, how you met [w] on your very first day at the burning apartment and all the other occasions when you bumped into each other. How he suspected you to be a criminal for no reason..."
    scene d10ahd34 with dissolve
    m "My god, I hope he doesn't dig too deep..."
    scene d10ahd35 with dissolve
    e "Nh!"
    scene d10ahd36 with dissolve
    pc "As [oc] said, he can't do anything as long as we don't give him a reason."
    scene d10ahd37 with dissolve
    j "What an annoying guy."
    scene d10ahd38 with dissolve
    m "Oh right, isn't there something you wanted to tell us, [j]? How did you and [oc] come to know each other?"
    scene d10ahd39 with dissolve
    j "Eh... it's nothing, really!"
    scene d10ahd40 with dissolve
    m "[j], if you want to live with us, then you should at least be honest !"
    if mob > 5:
        scene d10ahd41 with dissolve
        m "I mean..."
        scene d10ahd42 with dissolve
        m "Don't you agree, [pc]?"
        pc "Hm? Well, yeah, she's right, [j]."
    scene d10ahd40_x with dissolve
    j "Hmph... fine..."
    pcthink "This is probably going to be about the bike she took from her mom's ex..."
    scene black with slowdissolve
    n "As expected, [j] talks about the motorcycle, but then she goes on about the argument she had with her Mom, explaining that it wasn't the first time, then about what happened in school and even bits and pieces about things that happened in the past."
    n "All in all it's nothing too dramatic, but it seems like she just needed a little push to go all out. She talks about her childhood, how she's never seen her real Dad, how most of her Mom's boyfriends were assholes or didn't care about her..."
    n "After roughly an hour..."
    scene d10ahd43 with dissolve
    j "..."
    m "..."
    scene d10ahd44 with dissolve
    e "..."
    pc "Err..."
    scene d10ahd45 with dissolve
    pc "Well, now that you're here with us, you don't have to worry about that anymore."
    scene d10ahd46 with dissolve
    m "Absolutely, let the past be the past and focus on the future."
    scene d10ahd47 with dissolve
    j "Eh, sorry, I didn't mean to tell my whole life story!"
    pc "Sometimes things have to be said."
    scene d10ahd48 with dissolve
    j "Maybe, but it feels like I've been talking all evening..."
    scene d10ahd49 with dissolve
    m "Oh, right. I should make dinner."
    scene d10ahd50 with dissolve
    j "I-I'll help!"
    m "You don't need to, [j]."
    j "But I want to..."
    scene d10ahd51 with dissolve
    pc "*Smirk*"
    scene black with slowdissolve
    scene d10ahd52 with dissolve
    pc "Haha, the new Housekeeper update is funny!"
    if pcgender == "woman":
        pcthink "Too bad it's male MC only..."
    scene d10ahd53 with dissolve
    pc "Hey [e], you should have a look at this!"
    e "..."
    if not of10 == 2:
        pc "...or just stay there and look cute."
    else:
        pc "...or just stay there looking sexy."
    scene d10ahd54 with dissolve
    e "Khehehe."
    pc "...hmm..."
    pc "You know, I think [j] is right, I really should get a new TV."
    scene d10ahd53 with dissolve
    e "Hn!"
    pc "By the way, why don't you have your own TV?"
    e "Hm..."
    pc "...and why does [m] think you're bad with electronics?"
    scene d10ahd55 with dissolve
    e "Uhh..."
    play sound "audio/knock-door1.ogg"
    play sound "audio/door-opening.ogg"
    scene d10ahd56 with dissolve
    j "Time to stop drooling over each other, dinner is readyyyyy~!"
    scene black with slowdissolve
    n "You go have dinner and it tastes surprisingly well, even though you half expected it to be a disaster since [j] helped with it." with dissolve
    n "It's quite late already, so everyone quickly goes to bed after dinner, you decide do the same."
    scene black with slowdissolve
    
label d10night:
    if harem and jlo >= 2:
        jump d10nightsex
    else:
        scene black with fade
        $ d11morning = True
        $ actionsUsed = 15
        call dateTime from _call_dateTime_24
        jump d11wakeup
label d10nightsex:
    if _in_replay:
        show screen endRep
    "Voice" "Wakey wakey." with slowdissolve
    pc "Uhh... is it morning already?"
    "Voice" "No, Silly, it's still night!"
    "Voice" "Khehehe."
    scene d10night02 with slowdissolve
    pc "Huh?!"
    scene d10night01 with dissolve
    pc "[j]!?"
    scene d10night03 with dissolve
    pc "[e], what are you..."
    pc "Aren't you supposed to sleep in your bed?"
    scene d10night04 with dissolve
    e "..."
    j "Well, we're not sleeping..."
    scene d10night05 with dissolve
    j "We're just here to say good night, hehe."
    pc "I see..."
    scene d10night06 with dissolve
    pause
    scene d10night07 with dissolve
    pause
    scene d10night08 with dissolve
    e "*Smootch*"
    scene d10night09 with dissolve
    pc "Oh, I think I like where this is going!"
    scene d10night10 with dissolve
    j "So, are we allowed to stay a little longer, [pcmd]?"
    pc "How could I possibly say no."
    j "Hmm, thank you, [pcmd]."
    scene d10night11 with dissolve
    j "*Smootch*"
    scene d10night12 with dissolve
    j "*Smootch*"
    e "*Smootch*"
    scene d10night13 with dissolve
    pcthink "Damn, this is so hot!"
    scene d10night14 with dissolve
    show d10nightsx with dissolve
    pause
    show d10nightsx2 with dissolve
    pause 1
    show d10nightsx3 with dissolve
    pause
    show d10nightsx4 with dissolve
    pause 1
    show d10nightsx5 with dissolve
    pause 1.5
    scene d10night15 with dissolve
    j "You or me?"
    scene d10night16 with dissolve
    e "Hn!"
    scene d10night17 with dissolve
    j "You decide."
    if pcgender == "woman":
        pc "Decide what?"
        scene d10night17_2 with dissolve
        j "Whose pussy you want to lick, hehe."
        pc "Oh, I see."
    scene d10night18 with dissolve
    pc "Why not both?"
    scene d10night17 with dissolve
    j "You can't do us both at the same time."
    scene d10night18 with dissolve
    pc "Ha! Are you sure about that?"
    scene d10night17 with dissolve
    if pcgender == "woman":
        j "Haha, okay, who do you want to taste first then?"
    else:
        j "Haha, but who gets your dick first?"
    scene d10night18 with dissolve
    pc "Tough question."
    menu d10nightfun:
        "[e].":
            scene d10night19 with dissolve
            j "Awww..."
            if pcgender == "man":
                scene d10night20_m with dissolve
                e "Mmm..."
                scene d10night21_m with dissolve
                e "...nnnaah."
                scene d10night22_m with dissolve
                pause

                jump d10nfe
            else:
                jump d10nle
        "[j].":
            scene d10night19_1 with dissolve
            j "Yay!"
            if pcgender == "man":
                jump d10nfj
            else:
                scene d10night25 with dissolve
                j "But leave me some pussy, okay, [e]?"
                e "Kehehe."
                jump d10nlj
label d10nle:
    pc "Come here, [e]."
    scene d10night29_7 with dissolve
    j "I'll take that yummy pussy then."
    scene d10night29_8 with dissolve
    pause 1
    scene d10night29_9 with dissolve
    pause .5
    $ pov1 = "d10night30_2"
    $ pov2 = "d10night30_3"
    $ campov = False
    show screen povscreen(pov1) with dissolve
    pause
    j "Mhhh... I love how you taste, [pcmd]!"
    pc "Nhhh, and I love how you work your tongue!"
    j "Just don't come too early, you two!"
    e "Hnnn... hn!"
    pc "I can't guarantee for anything if you go on like this, [j]."
    j "Hehe... mphh... I love... mhh... your pussy, [pcmd]."
    j "I just... mhh... can't hold back!"
    menu md10nle:
        set menuset
        "Switch to [j].":
            pc "[j] come over here, I want to taste you as well!"
            j "Yay!"
            scene d10night31 with dissolve
            hide screen povscreen
            hide screen povbutton
            j "Here I cum, [pcmd]!"
            pc "Heh, not yet!"
            jump d10nlj
        "Go on, [e].":
            e "Nhh... nhhh..."
            j "[e]... mhh... hold on... mphh."
            e "Nhh... haaa..."
            j "Hold on, [e], hold on..."
            scene ej3somenightlecum1
            hide screen povscreen with dissolve
            hide screen povbutton with hpunch
            e "Haaaa!"
            scene ej3somenightlecum2 with dissolve
            e "Haaa..."
            j "Dammit, [e]."
            jump md10nle
        "Cum.":
            jump d10nend
label d10nlj:
    scene d10night26 with dissolve
    j "..."
    scene d10night29_3 with dissolve
    pause .5
    $ pov1 = "d10night30a"
    $ pov2 = "d10night30_4"
    $ campov = False
    show screen povscreen(pov1) with dissolve
    pause
    j "Hnnn... I just... gnnnh... love your tongue... haaa...!"
    j "Do you... hnn... like how I taste, [pcmd]?"
    pc "I love it!"
    j "Hnn... yes, [pcmd], right there."
    menu md10nlj:
        set menuset
        "Switch to [e].":
            scene d10night29_4
            hide screen povscreen with dissolve
            hide screen povbutton with dissolve
            j "Your turn, [e]!"
            e "Hn!"
            jump d10nle
        "Go on, [j].":
            e "Mhhh..."
            j "Gaawd... [pcmd]... nhh... I love it... hnnn."
            j "Hold on, hold on... fuck!"
            scene ej3somenightljcum1
            hide screen povscreen
            hide screen povbutton with hpunch
            j "Haaaa!"
            scene ej3somenightljcum2 with dissolve
            j "Haaa... your tongue feels amazing, [pcmd]."
            jump md10nlj
        "Cum.":
            jump d10nend
label d10nfe:
    scene d10night23_m with dissolve
    e "Hnn..."
    scene d10na1m with dissolve
    e "Nhhhaa..."
    pause
    scene d10night25_m with dissolve
    j "..."
    scene d10night27_m with dissolve
    pause
    scene d10na2m_00 with dissolve
    j "Go on, [e]."
    $ pov1 = "d10na2m"
    $ pov2 = "d10na3m"
    show screen povscreen(pov1)
    pause
    scene d10na2m_00
    hide screen povscreen
    hide screen povbutton
    scene d10na2m45 with dissolve
    e "Haa... haaa..."
    j "Damn, [e], don't go too fast yet!"
    scene d10night27_m with dissolve
    j "I want some fun, too..."
    scene d10night28_m with dissolve
    j "If you don't mind, [pcmd]."
    pc "Get get over here, Babygirl!"
    j "Yay!"
    scene d10night29_m with dissolve
    j "I hope you don't mind, [e]."
    scene d10night29_2 with dissolve
    e "..."
    scene d10night29_3 with dissolve
    pause .5
    $ pov1 = "d10night30a"
    $ pov2 = "d10night30m"
    $ campov = False
    show screen povscreen(pov1) with dissolve
    pause
    j "Hnn... how are you holding up, [e]?"
    e "Nhhh!...hnnn..."
    pause
    j "Ohhh, damn, [pcmd]... this feels great!"
    e "Hnn... nnhhh..."
    j "Nhhh... yes, there... haaaa!"
    e "Haaa... nnhhh..."
    pcthink "Shit, [e] is tightening up..."
    menu md10nfe:
        set menuset
        "Switch to fuck [j].":
            scene d10night29_4
            hide screen povscreen with dissolve
            hide screen povbutton with dissolve
            j "Now's my turn, [e]."
            e "Hn!"
            jump d10nfj
        "Go on, [j].":
            e "Nhh... nhhh..."
            j "Gaawd... [e]... nhh... hold on... hnnn."
            e "Nhh... haaa..."
            j "Hold on, hold on... fuck!"
            scene ej3somenightljcum1
            hide screen povscreen with dissolve
            hide screen povbutton with hpunch
            e "Haaaa!"
            scene ej3somenightljcum2 with dissolve
            e "Haaa..."
            jump md10nfe
        "Cum.":
            jump d10nend
label d10nfj:
    scene d10night29_5 with dissolve
    j "Right there."
    scene d10night29_6 with dissolve
    j "Haa... yes!"
    pc "[e] come here."
    scene d10night29_7 with dissolve
    e "Hn..."
    scene d10night29_8 with dissolve
    pause 1
    scene d10night29_9 with dissolve
    pause .5
    $ pov1 = "d10night30_2"
    $ pov2 = "d10nightfjm1"
    $ campov = False
    show screen povscreen(pov1) with dissolve
    pause
    e "Hnnn... nhnnn!"
    j "Ohh gaaaawd, [pcmd], I love your dick!"
    j "Shit, hnn... [pcmd]."
    e "Nhhh..."
    j "[pcmd], [pcmd]!"
    menu md10nfj:
        set menuset
        "Switch to fuck [e].":
            hide screen povscreen with dissolve
            hide screen povbutton with dissolve
            jump d10nfe
        "Go on, [e].":
            e "Nhh... nhhh..."
            j "Gaawd... [e]... nhh... hold on... hnnn."
            e "Nhh... haaa..."
            j "Hold on, hold on... fuck!"
            scene ej3somenightlecum1
            hide screen povscreen with dissolve
            hide screen povbutton with hpunch
            e "Haaaa!"
            scene ej3somenightlecum2 with dissolve
            e "Haaa..."
            jump md10nfj
        "Cum.":
            jump d10nend
label d10nend:
    pc "I'm getting close!"
    scene black with dissolve
    hide screen povscreen with dissolve
    hide screen povbutton
    j "[e], I think it's time for the grand finale."
    e "Hn!"
    pc "Hey, why did you stop?"
    scene d10night30 with dissolve
    j "Like we agreed?"
    e "Mh-hm!"
    scene d10night31 with dissolve
    j "Come on, get up, [pcmd]."
    pc "Huh?"
    if pcgender == "man":
        pc "What are you up to?"
        j "The grant finale! You on top of [e]."
        pc "Hmm... sounds good."
        scene black with dissolve
        pc "Let's try this."
        j "Mmh... looks sexy! I'll watch!"
        $ pov1 = "d10nightfe3"
        $ pov2 = "d10nightfe2"
        $ campov = False
        show screen povscreen(pov1) with dissolve
        j "Damn, this looks so hot!"
        pause
        j "You like it, [e]?"
        e "Hn!... nnhh..."
        j "Haha, obvious."
        pause
        scene ej3somenight1_i1
        hide screen povscreen with dissolve
        hide screen povbutton with dissolve
        pc "Hm?"
        scene ej3somenight1_i2 with dissolve
        j "..."
        pc "Heh, come closer..."
        $ pov1 = "d10nightfe4"
        $ pov2 = "d10nightfe5"
        $ campov = False
        show screen povscreen(pov1) with dissolve
        j "Hnn, yes, [pcmd]!"
        pause
        scene d10nightfe6
        hide screen povscreen with dissolve
        hide screen povbutton with dissolve
        pc "Damn, I'm close, [e], are you ready?"
        e "Hnn!"
        j "Oh, [pcmd], I'm close, too!"
        e "Hnnn... hnnnn..."
        scene d10nightfe7 with dissolve
        pc "Shit!"
        j "Nhhh... fill her, [pcmd]! Fill her with your hot, juicy cum!"
        e "Hnnn... nhaaa..." with flash
        j "Fill your little sister's baby room with your seed, [pcmd]!"
        pc "Holy shit!" with flash
        scene ej3somenightfcum1 with hpunch
        e "Haaaaa!"
        scene ej3somenightfcum1 with flash
        scene ej3somenightfcum1 with hpunch
        pc "Gawd!"
        scene ej3somenightfcum1 with flash
        scene ej3somenightfcum1 with hpunch
        pc "Damn..."
        scene black with slowdissolve
        scene ej3somenightfcum2 with slowdissolve
        pc "...phew..."
        j "Mmmh, [pcmd] that was awesome!"
        scene black with slowdissolve
    else:
        scene d10night32 with dissolve
        pc "What are you up to?"
        scene d10night33 with dissolve
        j "You'll love it, promise!"
        scene d10night34 with dissolve
        pc "Now I'm curious."
        scene ej3somenight3_00 with dissolve
        pc "Oh, I think I know..."
        $ pov1 = "d10nightle1"
        $ pov2 = "d10nightle2"
        $ campov = False
        show screen povscreen(pov1) with dissolve
        pause
        j "Do you like it, [pcmd]?"
        if campov:
            scene ej3somenight6f_000
            $ pov1 = "d10nightle4"
            $ pov2 = "d10nightle3"
        else:
            scene ej3somenight5f_000
            $ pov1 = "d10nightle3"
            $ pov2 = "d10nightle4"
        hide screen povscreen with dissolve
        hide screen povbutton with dissolve
        show screen povscreen(pov1)
        pc "Hmmm... suck on my clit, [e]."
        e "Mhhh..."
        pc "How could I not like it, with two beautiful, hot girls..."
        pause
        j "Mhh... do you like...mphh... getting eaten out by your... mhhh... little girls, [pcmd]?"
        pc "It feels great, girls!"
        j "Mhhh... your skin is so smooth..."
        e "Mnhh..."
        j "Do you want to cum into your little sister's mouth, [pcmd]!"
        pc "Damn..."
        j "Look at her...mhhh... right between your legs... mmph... tasting your juicy, wet pussy..."
        pc "Damn, you look so sexy down there..."
        j "Let us taste all your yummy pussy juice... mmphh..."
        pc "Shit..." with flash
        j "Cum for us, [pcmd], mhh... cum for us!"
        pc "Oh fuck! Don't stop, don't stop!" with flash
        j "Yes, [pcmd], cum for us!"
        hide screen povscreen
        hide screen povbutton
        scene ej3somenightlcum1 with hpunch
        pc "FUCK!"
        scene ej3somenightlcum2 with dissolve
        e "*Lick*"
        scene ej3somenightlcum3 with dissolve
        e "*Smooch*"
    scene black with slowdissolve
    j "Gaaawd, we need to do this again some day."
    pc "Yeah."
    scene d10night35 with dissolve
    j "How about tomorrow night?"
    pc "Haha, sure."
    j "And the night after tomorrow?"
    e "Khehehe."
    pc "How about every night?"
    j "Hehe, oh [pcmd], you're so naughty..."
    pc "Hey, it's you two who came over to keep me from sleeping."
    j "You didn't seem to mind it much."
    pc "Speaking of which, maybe you two should go back to your room, [e] needs to get up early for school, right [e]?"
    scene d10night36 with dissolve
    e "*Snooze*"
    pc "Damn..."
    scene d10night35 with dissolve
    j "I guess we're going to sleep here tonight."
    pc "Well, let's hope [m] doesn't notice anything."
    scene d10night37 with dissolve
    j "We really need to make her change her mind, so she's okay with us sleeping here instead of [e]'s room."
    pc "Maybe she'll change her mind in the future."
    scene d10night38 with dissolve
    j "I'm sure you can convince her, hehe."
    pc "Maybe... wait, was that some kind of suggestion again?"
    scene d10night39 with dissolve
    j "Hehe, good night, [pcmd]."
    pc "Oh well, whatever... Night, [j]..."
    scene black with fade
    $ renpy.end_replay()
    $ d11morning = True
    $ actionsUsed = 15
    call dateTime() from _call_dateTime_23
        
        
label d11wakeup:
    play sound "audio/knock-door1.ogg"
    m "[pc], do you want to eat breakfast with us?"
    scene pcroom_wakeup with slowdissolve
    pc "YAAAAAaaaawn..."
    scene pcroom_wakeup_lright with dissolve
    if harem and jlo >= 2:
        pcthink "Looks like they got up in time..."
    else:
        pcthink "Looks like [e] didn't come over again..."
    play sound "audio/knock-door1.ogg"
    m "[pc]?"
    scene pcroom_wakeup_lleft with dissolve
    pc "Yeah, I'm coming..."
    scene black with fade
    n "You get up, take a quick shower and then join the others for breakfast. [j] and [m] seem to have been engaged in a conversation for a while..."
    play music mainbgm fadein 1
    scene d11breakfast02 with slowdissolve
    j "...and then it all went down from there..."
    scene d11breakfast01 with dissolve
    m "I see... say, [j], for how long are you suspended from school again?"
    scene d11breakfast02 with dissolve
    j "This week still."
    scene d11breakfast03 with dissolve
    m "I see, any plans for today?"
    scene d11breakfast04 with dissolve
    j "Uhh... no, not really."
    scene d11breakfast05 with dissolve
    m "Do you have any plans for the future? Maybe you could look for a job, it's not that long anymore until school is out."
    scene d11breakfast06 with dissolve
    j "I... don't know. I will probably end up as a waitress anyway..."
    scene d11breakfast07 with dissolve
    m "You don't have any plans for the future?"
    scene d11breakfast08 with dissolve
    j "It's not like I have much to chose from."
    pc "I didn't know what to do either."
    scene d11breakfast09 with dissolve
    j "Hm?"
    pc "After school... I didn't have a degree, I had no idea what to do, nor did I care at the time... and look at me now, I'm basically self-employed and do what I like."
    scene d11breakfast10 with dissolve
    m "You don't have a degree?"
    scene d11breakfast11 with dissolve
    pc "I didn't, you know how I left... I got my degree a few years later, but until then I still had many different jobs."
    pc "I'm not saying that a degree doesn't matter, it does, but just because you don't have a degree doesn't mean you can't do anything. There are still a lot of opportunities in life."
    scene d11breakfast12 with dissolve
    m "I see..."
    pc "..."
    scene d11breakfast13 with dissolve
    m "So, what are your plans for today?"
    scene d11breakfast14 with dissolve
    pc "Today is the deadline for the project I was working on, so I'll have to present it at work today."
    scene d11breakfast13 with dissolve
    m "I see, sounds like it'll be a busy day for you."
    scene d11breakfast14 with dissolve
    pc "Yeah, probably..."
    scene black with fade
    n "After breakfast, [e] and [m] get ready to leave for the day. To everyone's surprise, [j] demands to take care of the dishes... you decide to look through the project one more time before you leave for town."
jump d11jbeforl

label d11bhpcroom:
    scene d11bhpcroom01 with dissolve
    pcthink "Hmm... what to do now..."
    pcthink "..."
    pcthink "Maybe I should look for a good TV to buy..."
    pcthink "I mean, it looks like I'll stay..."
    pcthink "Right?"
    pcthink "..."
    scene d11bhpcroom02 with dissolve
    pcthink "Damn, my life really took a 180 over the last two weeks..."
    play sound "audio/door-opening.ogg"
    scene d11bhpcroom03 with dissolve
    j "Whatcha doing?"
    scene d11bhpcroom04 with dissolve
    pc "I was just about to look for a TV online."
    scene d11bhpcroom05 with dissolve
    j "Finally! That's great! Can I help?"
    pc "Sure..."
    play sound "audio/doorbell.ogg"
    n "*Doorbell rings*"
    scene d11bhpcroom06 with dissolve
    pc "Hm?"
    j "Are you waiting for somebody?"
    pc "No, not that I remember..."
    scene d11bhpcroom07 with dissolve
    j "Oh no, I hope it's not that weird cop again..."
    
$ renpy.run_action(QuickSave())
scene black with dissolve
pause .5
jump endGame