########## Ellie
label elliePCRoomSleepDay0:
    scene pcroom ellie sleep with dissolve 
    pcthink "What?! [e]?"
    pcthink "Why is she sleeping in my bed?"
    menu:
        "get closer":
            scene pcroom ellie sleep far with dissolve 
            pause
    menu:
        "get closer":
            scene pcroom ellie sleep mid with dissolve 
            pause
    pcthink "She looks so cute when she's sleeping..."
    menu:
        "get really close":
            scene pcroom ellie sleep close with dissolve
            pause
    menu:
        "Wake her up":
            pc "Hey sleepyhead, wake up!"
            scene pcroom ellie close eyes open with dissolve
            pause
            jump ellieWakeup
        "Just look":
            window hide
            pause
            scene pcroom ellie close eyes open with dissolve
            pcthink "Ugh... shit..."
            pc "Uhh..."
            jump ellieWakeup
        
label ellieWakeup:
    pc "Good morning [e]..."
    pc "You know this is my bed... right?"
    scene pcroom ellie getup with dissolve
    pause .5
    scene pcroom ellie getup attack with hpunch
    e "Hisss..."
    pc "WHOA WTF!!!"
    scene pcroom ellie getup after attack with dissolve
    e "Khehehe..."
    pc "Gosh, [e]! I almost had a heart attack!"
    e "..."
    pc "Anyway, [m] says breakfast is almost finished, so you better get up..."
    scene black with dissolve
    n "She takes her time to get up and leaves the room."
    pcthink "Damn, she got me with that surprise attack..."
    pcthink "Usually I was the one always trying to scare her when we were younger." 
    pcthink "Sometimes I scared her so much that she started to cry... I always felt so sorry when that happened..."
    pcthink "...and I was even more sorry when [m] noticed what I did..."
    $ SEsearchforsis = False
    $ storyEvent = False
    jump kitchenBreakfastDay0
    
label eOnLap:
    play music mainbgm fadein 1
    n "A while later" with dissolve
    window hide
    pause 2    
    scene pcroomsitonchair2 with dissolve
    pcthink "Damn, I wanted to play with myself a bit after touching [m]s tits, but this stupid therapist bitch totally destroyed the mood..."
    pcthink "But the pills [m] takes... I wonder how far I could go..."
    scene pcroom sitonchair door opens with dissolve
    n "The door to your room opens."
    pc "Huh?"
    scene pcroom sitonchair eenter with dissolve
    pc "Hey [e], whats up?"
    scene pcroom sitonchair eshy with dissolve
    pause
    pc "What's wrong? Why are you being shy now?"
    scene pcroom sitonchair esurprised with dissolve
    pause 0.5
    scene pcroom sitonchair esmilebeforejump with dissolve
    pause 0.5
    scene pcroom sitonchair eonlap with hpunch
    pc "Whoa!"
    scene pcroom sitonchair eonlap2 with dissolve
    e "Khehe..."
    pcthink "Okay, definitely not shy!"
    scene pcroom sitonchair eonlap with dissolve
    e "..."
    pc "..."
    pc "This [t] is quite annoying, huh?"
    scene pcroom sitonchair elookaway with dissolve
    e "..."
    pc "..."
    pc "Yeah, I don't like her either..."
    scene pcroom sitonchair ehug with dissolve
    pcthink "Awww..."
    scene pcroomsitonchairehug3 with dissolve
    pc "Come here..."
    e "Hmmm..."
    pc "I missed you, sis..."
    scene pcroom sitonchair estare with dissolve
    pause
    pc "???"
    scene pcroom sitonchair kiss with dissolve
    pause 1
    scene pcroom sitonchair ehug3 with dissolve
    pcthink "Wow, I guess she missed me, too."
    pause
    scene black with dissolve
    n "She rests on your lap for a while. Both of you keep quiet until [m] calls for dinner."
    jump dinnerDay2
      
label eNightTwo:
    if _in_replay:
        show screen endRep
    n "Night" with dissolve
    window hide
    pause 2
    scene pcroomday2night1 with dissolve
    pc "..."
    pcthink "I wonder if [e] is going to sneak over again..."
    pcthink "I can't remember a day she didn't at least try to sleep over back when we were kids."
    pcthink "It all started after Dad's death..."
    pc "..."
    pcthink "...it's a bit weird that she is still doing it..."
    pcthink "...but it's also kind of cute, hehe."
    n "You can hear the door handle being moved slowly."
    scene pcroomday2night1_1 with dissolve
    pc "Hm?"
    pcthink "I guess there is my answer..."
    pcthink "Ha! Time for a revenge attack."
    scene black with dissolve
    n "You pretend to be asleep."
    n "[e] moves slowly, trying to make no noises. As she reaches your bed, she climbs into it and gives you a soft poke."
    pcthink "That poke was so soft, she was definitely not trying to wake me up."
    n "[e] fiddles a bit with the blanket, you assume that she is trying to get under it without waking you up."
    pcthink "Alright, this is my chance for a surprise attack!"
    scene pcroomday2night2 with dissolve
    pcthink "What the... she isn't trying to get under the blanket! She is staring at my crotch!"
    pcthink "Shit, I didn't expect this..."
    scene pcroom day2 night3 with dissolve
    pc "Gotcha!"
    scene pcroom day2 night ehide with dissolve
    e "*Squeak*"
    pause 1
    pc "Haha, too bad I'm wearing shorts this time, eh [e]?"
    pc "Naughty little sis, did you do that yesterday too?"
    scene pcroom day2 night epeek with dissolve
    n "She shakes her head fiercely, still hiding behind the blanket."
    pcthink "Damn, she's so cute..."
    scene pcroom day2 night ehug0 with hpunch
    pc "Whoa!"
    scene pcroomday2nightehug with dissolve
    pause
    pc "..."
    e "..."
    pc "You know, as the older one of us I should mention that this is quite inappropriate..."
    scene pcroom day2 night esleep with dissolve
    pause
    pc "...but who cares, right?"
    pcthink "She obviously doesn't..."
    pc "..."
    if not steamy:
        pcthink "Damn, I can feel her pussy lips on my leg..."
        pcthink "It almost feels like she isn't wearing anything under her pyjamas..."
        pcthink "Wait!"
        pcthink "She {b}isn't{/b} wearing anything under her pyjamas!"
        pcthink "Fuck... is she wet?"
        e "Hnn..."
        n "You notice that she very subtly grinds on your leg."
        image egrind = Movie(play="anim/esleep_anim2.webm")
        scene egrind with dissolve
        pcthink "What the hell, is she doing this on purpose?"
        pcthink "Gawd, Sis, don't do this to me! I'm horny enough already..."
        if pcgender == "man":
            pcthink "I'm getting the hardest boner ever!"
        pcthink "Shit I have to think about something else..."
        pcthink "Err... Lions... Rats... Little Cats... Catgirls... Fuck!"
        scene black with dissolve
        n "After a while of struggling you manage to fall asleep."
    $ renpy.end_replay()
    $ actionsUsed = 15
    call dateTime from _call_dateTime_6
    
label ellieVR:
    scene pcroom ellievr with dissolve
    pc "Huh? [e]?"
    pcthink "Damn, she is sneaky!"
    pc "Hey, [e]!"
    pc "..."
    pcthink "She hasn't even noticed me..."
    pcthink "Looks like she's having fun in the VR world."
    pcthink "I guess she has never experienced anything like it before."
    scene pcroom ellievr2 with dissolve
    pc "..."
    scene pcroom ellievr3 with dissolve
    pcthink "I'm a bit impressed she could set it up so quickly..."
    pcthink "Well, I guess I just let her be..."
    scene pcroom ellievr grab2 with dissolve
    pcthink "Whoa!"
    scene pcroom ellievr grab with dissolve
    pause 0.1
    scene pcroom ellievr grab2 with dissolve
    pcthink "What the..."
    scene pcroom ellievr grab with dissolve
    pause 0.1
    scene pcroom ellievr grab2 with dissolve
    pcthink "What is she doing?"
    scene pcroom ellievr pclookatlappy with dissolve
    pause
    scene pcroomellievrporn with dissolve
    pcthink "What the fuck!? VR porn?!"
    pcthink "She's watching VR porn?!"
    pc "Shit!"
    scene black with dissolve
    n "You quickly turn around and take the HMD from her head."
    scene prcoomellievrgrabhmd with dissolve
    e "Whaa?!"
    scene pcroom ellievr grabhmd2 with dissolve
    pc "What the fuck [e]! Who the hell told you that you could use my stuff??"
    pc "This isn't yours!"
    scene black with dissolve
    n "She runs out of the room."
    scene pcroomellievrpccloselappy with dissolve
    pcthink "Damn... She looked kinda scared..."
    pcthink "...did I overdo it?"
    scene pcroom ellievr pccloselappy2 with dissolve
    pcthink "Shit, why didn't she just play a Game or watch one of the animated Movies?"
    pcthink "Why did she have to watch porn?!"
    pc "Fuck!"
    pc "..."
    scene pcroom ellievr pccloselappy3 with dissolve
    pcthink "Maybe I should have a look for her."
    pcthink "But she did use my stuff without even asking..."
    pc "Ugh, fuck!"
    pcthink "Of course she didn't ask, she doesn't speak... dammit."
    scene pcroom ecarring box with dissolve
    e "Uaahhh..."
    pc "Huh?"
    pc "..."
    scene pcroom ecarring boxpctake with dissolve
    e "Eh?"
    scene pcroom pctakebox with dissolve
    pc "Thanks [e]."
    scene pcroom pcput box with dissolve
    pause
    scene pcroom esorry with dissolve
    e "..."
    scene pcroom esorry2 with dissolve
    pc "*Sigh*"
    pc "...Sorry [e]. I didn't mean to yell at you..."
    e "..."
    pc "Listen, you can use my stuff if you want, but at least give me a hint, okay?"
    scene pcroom esorry3 with dissolve
    pcthink "So I have the chance to hide my porn collection..."
    scene black with dissolve
    n "You and [e] get the rest of the boxes into your room and head to the livingroom for breakfast afterwards."
    n "After [e] and [m] left, you start to unpack the rest your stuff."
    n "Hours later" with dissolve
    window hide
    pause 2
    $ actionsUsed = 6
    call dateTime from _call_dateTime_7
    jump rachelStuckInTraffic

label childroomPCtalktoEllie:
    scene childroom ellierelax with dissolve
    pc "Hey, [e]."
    scene childroom ellierelax look with dissolve
    pcthink "Huh? She looks sad..."
    scene childroom ellierelax look2 with dissolve
    pcthink "Or not?"
    scene childroom ellierelax look3 with dissolve
    pcthink "...must have been my imagination..."
    scene childroom ellierelax look4 with dissolve
    pcthink "...Anyway..."
    pc "... we didn't have the chance to talk since I've come back, so I thought now might be a good time?"
    scene childroom ellierelax look5 with dissolve
    pc "Hey, don't worry, there is nothing to be concerned about, okay?"
    scene childroom ellierelax look6 with dissolve
    pause .1
    scene childroom ellierelax look6_2 with dissolve
    pause .1
    scene childroom ellierelax look6 with dissolve
    pc "Heh, right..."
    scene childroom ellierelaxpc with dissolve
    pc "So... errm... how are you [e]?"
    scene childroom ellierelaxpc2 with dissolve
    e "..."
    pc "Eh... well you know... about when I left back then..."
    pc "Err... I'm sorry [e]... I know I should have told you that I was leaving, and I promise that it's not going to happen again..."
    pc "I mean... I might not stay here, but..."
    scene childroom ellierelaxpc3 with dissolve
    e "Eh?!"
    scene childroom ellierelaxpc4 with hpunch
    e "HNN!!"
    pc "H-Hey, I won't leave, don't worry..."
    scene childroom ellierelaxpc5 with dissolve
    pc "What I meant is, even if I'm not going to stay here in the house, I'm not going to leave the city."
    pc "{b}If{/b} I'm going to move out again, you're going to be the first one to know, and you can come visit me whenever you want..."
    pc "Well... actually, I demand that you are going to come visit me every day, hehe."
    scene childroom ellierelaxpc6 with dissolve
    e "Khehe..."
    scene black with fade
    n "[e] hugs you again as if she doesn't want to let you go anymore. You assure her that you're not going to disappear again. She doesn't answer, but you can tell that she is happy.{p}After a while [m] calls for dinner..."
    jump pcroomnight3

label childroomESleepDay3:
    scene hall door with dissolve
    pcthink "Hum... [m] said that [e] usually oversleeps on weekends."
    menu:
        "Look for her.":
            pcthink "Just to see if she's okay..."
            scene childroom ellie sleep1 with dissolve
            pcthink "There she is, sleeping peacefully..."
            menu:
                "Get closer.":
                    $ efe -= 1
                    scene childroom ellie sleep2 with dissolve
                    pcthink "Damn she's so cute..."
                    pause
                    pcthink "I can't believe she still sleeps with that old teddy..."
                    pcthink "I can still remember the day my Mom gave it to me..."
                    pause
                    pcthink "Anyway, no time to revel in the past, I have to buy a present!"
                    jump leaveDay3
                "Leave.":
                    pcthink "I guess I better hurry to find an awesome present for her."
                    jump leaveDay3
        "Don't look for her.":
            jump leaveDay3
label leaveDay3:
    $ doonce2 = True
    scene hall_back_idle with dissolve
    call screen map_hall_back
    
    
label ebdLookForE:
    m "...and then [pc] jumped up and ran after him."
    scene livingroom ebd_ tjm1 with dissolve
    j "Haha."
    m "At first I wasn't even sure what happened, but when I saw [e] crying, I knew *hic*"
    scene livingroom ebd_ tjm2 with dissolve
    if pcgender == "woman":
        j "[pc] the heroine, hehe."
    else:
        j "[pc] the hero, hehe."
    m "Haha, yes [heshe] was always like that when it came to [e]..."
    scene livingroom ebd_ tjm3 with dissolve
    if pcgender == "woman":
        t "I wonder how much is left of that heroine nowadays."
    else:
        t "I wonder how much is left of that hero nowadays."
    pc "..."
    m "*hic*"
    scene livingroom ebd_ tjm4 with dissolve
    t "Are you sure there is no alcohol in the punch [m]?"
    scene livingroom ebd_ tjm5 with dissolve
    m "Yes, of course, I'm sure..."
    scene livingroom ebd_ tjm4 with dissolve
    t "I have to admit, I feel a bit dizzy..."
    scene livingroom ebd_ tjm5 with dissolve
    m "Hum... now that you mention it, I'm feeling a bit weird myself..."
    scene livingroom ebd_ tjm6 with dissolve
    j "Maybe it's the weather, it's really hot today, hehe."
    scene livingroom ebd_ tjm7 with dissolve
    t "I doubt that."
    scene livingroom ebd_ tjm5 with dissolve
    m "Oh I hope it's not the fruit. I made extra sure they were fresh..."
    scene livingroom ebd_ tjm6 with dissolve
    j "I feel good and the punch tastes as awesome as always [m]."
    m "Thanks, [j]."
    scene livingroom ebd_ tjm8 with dissolve
    m "How about you [pc]?"
    pc "I didn't notice anything and it tastes really good."
    scene livingroom ebd_ tjm9 with dissolve
    m "Thanks, Hun."
    pcthink "Damn, I hope this doesn't backfire..."
    scene livingroom ebd_ tjm10 with dissolve
    j "I wonder why [e] is taking so long..."
    m "Hum, right. I'll have a look for her."
    scene livingroom ebd_ tjm11 with dissolve
    j "Oh, why don't you let [pc] have a look. You've done so much for [e] today, you should sit down and enjoy the punch, hehe."
    scene livingroom ebd_ tjm11 with dissolve
    pc "Yeah, let me look for her..."
    scene livingroom ebd_ tjm12 with dissolve
    m "Oh... sure [pc]."
    scene livingroom ebd_leave with dissolve
    j "Another glass [m]?"
    m "Umm... sure, why not?"
    scene home_hall_idle with dissolve
    pcthink "Shit, I hope [j] doesn't overdo it..."
    scene hall door with dissolve
    pc "[e], it's me..."
    pc "I'm coming in."
    scene childroom ebd1 with dissolve
    pcthink "Huh? What's going on with her?"
    pc "What's up [e]? Everybody is waiting for you?"
    scene childroom ebd2 with dissolve
    pcthink "Is she crying?"
    scene childroom ebd3 with dissolve
    pc "Hey, what's wrong? For a second I thought you where crying..."
    scene childroom ebd4 with dissolve
    e "..."
    scene childroom ebd5 with dissolve
    pcthink "Damn, I bet it's [t]'s fault! That bitch!"
    pcthink "Hum..."
    pc "*Hop*"
    scene childroom ebd6 with vpunch
    pause
    pc "Come on [e], whatever happened, forget about it. It's your birthday and you should be happy."
    scene childroom ebd7 with dissolve
    e "..."
    pc "Come on, there is a lot of cake waiting for you and of course some neat presents. I bet you'll love them."
    scene childroom ebd8 with dissolve
    e "..."
    pc "Hey, I spent {i}ages{/i} to find a good present for you, so if you don't get up and attend your own birthday party I'm sure I'll start crying like a baby."
    scene childroom ebd9 with dissolve
    e "..."
    scene black with dissolve
    n "She gets up, goes to the wardrobe and looks at you meaningfully."
    scene childroom ebd10 with dissolve
    pc "Oh, yeah, I get it. I'll let you change..."
    scene childroom ebd11 with dissolve
    pcthink "Alright, let's hope the rest of this \"party\" is going to work out better..."
    scene hallbathroomdoor with dissolve
    pcthink "Just a quick visit to the toilet..."
    play sound "audio/door-opening.ogg"
    stop music fadeout 2
    scene bathroom ebd1 with dissolve
    pc "Whoa... sorry..."
    scene hall_back_idle with dissolve
    pcthink "Shit, why didn't she lock the door?"
    t "{size=-10}Pervert...{/size}"
    pcthink "..."
    extend "."
    extend "."
    extend "."
    extend "keep."
    extend "calm."
    extend "[pc]."
    t "{size=-10}Would you shut the door already or are you going to peep on me forever?{/size}"
    pcthink "FUCK!"
    jump coerceT1
    
label eKitten:
    scene hall door with dissolve
    pcthink "I hope she doesn't have a hangover as bad as [m]..."
    "Voice" "{size=-10}Nya!{/size}"
    pcthink "Huh? What was that?"
    "Voice" "{size=-10}Nya nya nya...{/size}"
    pcthink "Is that [e]?"
    e "{size=-10}Nyaaa...{/size}"
    pcthink "Well that's interesting..."
    pcthink "I guess it's time for a..."
    scene childroom kitty1 with dissolve
    play sound "audio/door-opening.ogg"
    pc "SURPRISE ATTACK!" with hpunch
    scene childroom kitty3 with hpunch
    e "{cps=20}NYAAAAAA!!{/cps}"
    pc "Haha, gotya!"
    e "HNN!"
    scene childroom kitty4 with dissolve
    pc "Hey, cute outfit! Is this your present from [j]?"
    e "?!"
    scene childroom kitty5 with dissolve
    pc "So that's why you where making these cute anime cat noises..."
    scene childroom kitty6 with dissolve
    pc "Come on, do it again."
    e "..."
    pc "Haha, no need to be embarrassed [e], I've heard you anyway and it was actually really cute."
    e "..."
    pc "Come on [e], or do I have to tickle your cat ears?"
    scene childroom kitty9 with dissolve
    e "Nnn..."
    pc "...or maybe the tail?"
    scene childroom kitty7 with dissolve
    e "Nnn!"
    scene childroomkitty10 with dissolve
    pc "You won't escape me!"
    scene childroomkitty11 with vpunch
    e "NYAAA!!"
    pause 1
    pc "What the?!"
    e "NNNNaaah..."
    pcthink "Don't tell me this is..."
    scene childroom kitty12 with dissolve
    pcthink "Shit..."
    pc "...a plug?!"
    scene childroom kitty13 with dissolve
    pcthink "So that's what [j] meant with the \"secret\" present yesterday... who would have guessed..."
    pc "That's fucking naughty... haha."
    scene childroom kitty14 with dissolve
    e "HN!"
    pc "Whoa, hey. Wait a minute!"
    scene childroom kitty15 with dissolve
    pc "If you want it back, I want you to say \"Nya\" for me."
    scene childroom kitty15_2 with dissolve
    e "...NYAA!!"
    scene childroom kitty16 with dissolve
    pc "Fuuuck!" with hpunch
    scene childroom kitty17 with dissolve
    pc "Holy kitty attack..."
    scene childroom kitty18 with dissolve
    e "Khehe..."
    scene childroom kitty19 with dissolve
    e "Eh!"
    pc "Haha, nope!"
    scene childroom kitty20 with dissolve
    e "Hn!"
    pc "Come on, one more time..."
    scene childroom kitty22 with dissolve
    e "..."
    scene childroom kitty23 with dissolve
    e "...nya?"
    scene childroom kitty22 with dissolve
    pc "... cuuute~"
    scene childroom kitty24 with dissolve
    e "Hehe..."
    e "Nyaaaa..."
    pcthink "She's so cute..."
    e "..."
    scene childroom kitty25 with dissolve
    pcthink "So cute..."
    e "..."
    pc "..."
    pcthink "Damn it!"
    pcthink "She's not my sister, so who cares..."
    scene childroomkitty26 with dissolve
    pc "I don't care..."
    scene childroomkitty27 with dissolve
    pause 1
    scene childroomkitty28 with dissolve
    e "Unn..."
    pause 3
    scene childroomkitty27 with dissolve
    $renpy.pause(1)
    scene childroomkitty29 with hpunch
    e "Nyahaha!"
    pc "Whoa, hey, that's not fair!"
    scene childroom kitty30 with dissolve
    e "Khehehe."
    scene childroom kitty31 with dissolve
    pause 1
    pc "Little cheater!"
    #
    pause 1
    #
    pc "Alright, you better get changed now, [m] asked me to get you for dinner, and I'm not sure how she would react if you show up like this..."
    e "...nya."
    pc "I'll see you in a bit then."
    scene childroom ebd11 with dissolve
    pcthink "Damn, what a surprise..."
    scene hall_back_idle with dissolve
    pcthink "But I guess I should have expected something like this with a friend like [j]."
    pcthink "Shit, [e] is even naughtier than I thought..."
    scene black with fade
    jump dinnerDay4Home

label makedinnerwithE:
    pcthink "I guess I'm not the only one who expected dinner to be ready..."
    pc "Hey [e]."
    scene kitchen_e_searchforfood2 with dissolve
    e "Huh?"
    scene kitchen_e_searchforfood2_2 with dissolve
    pause 1
    scene kitchen_e_searchforfood_kiss with dissolve
    $ pov1 = "kitchen_e_searchforfood_kiss"
    $ pov2 = "kitchenesearchforfoodkissmc"
    show screen povscreen(pov1)
    e "*Smootch*"
    scene kitchen_e_searchforfood5 with dissolve
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    pc "Looks like we have to make dinner today."
    scene kitchen_e_searchforfood4 with dissolve
    pc "Err... yeah, I guess [m] isn't going to make dinner today..."
    scene kitchen_e_searchforfood3 with dissolve
    pc "Sorry, that's my fault. I had an argument with her a bit earlier today..."
    pc "Anyway..."
    pc "What do you think, should we cook something together?"
    scene kitchen_e_searchforfood3_2 with dissolve
    e "Hn!"
    scene black with slowdissolve
    play music mainbgm fadein 1
    n "You check the available food and decide to make some noodles."
    scene kitchen_e_cook1 with dissolve
    pcthink "Damn, that's a lot to eat..."
    pc "How is it?"
    scene kitchen_e_cook2 with dissolve
    e "Uhuh!"
    pc "Alright, let's eat then."
    scene black with slowdissolve
    pause 1
    scene kitchen_e_eat2 with dissolve
    pc "Phew, quite spicy..."
    scene kitchen_e_eat with dissolve
    pc "...don't you think, [e]?"
    pc "PWAHAHA, do you need a bib, [e]?"
    scene kitcheneeat_mc with dissolve
    pc "The sauce is all over your face..."
    scene kitcheneeat_mc2 with hpunch
    pc "Whoa!"
    scene kitcheneeat_mc3 with dissolve
    pc "Hey, what if I wanted to eat that?"
    scene kitcheneeat_smile with dissolve
    e "Tee-hee."
    scene black with slowdissolve
    pause .5
    scene kitcheneeat_empty with dissolve
    pcthink "Phew... I'm full..."
    scene kitcheneeat_refill with dissolve
    pc "[e], you still want more?"
    scene kitcheneeat_refill2 with dissolve
    e "Uh-uh..."
    scene kitcheneeat_refill3 with dissolve
    pcthink "Oh, she's going to give it to [m]?"
    scene kitcheneeat_refill4 with dissolve
    m "{size=-10}[e], what are you...?! Oh...{/size}"
    pcthink "Hum, I didn't expect [e] to be so caring about her mother..."
    m "{size=-10}Thank you, but I'm not hungry.{/size}"
    play sound "audio/door_close.ogg"
    n "You can hear the door to [m]'s room closing."
    pcthink "Hah, looks like [e] doesn't accept a no as an answer..."
    scene black with dissolve
    stop music fadeout 2
    n "You wait a few minutes for [e] to come back, but she doesn't. After a while you go back to your room and spend the rest of the evening watching some funny videos and finally decide to go to bed..."
    jump eHumpNight5
    
label eHumpNight5:
    play music "audio/BadDream.mp3"
    scene dream_01 at dream with dissolve
    n "At night" with dissolve
    m "[bpc] WHERE IS MY WINE?" with hpunch
    pc "Huh? How would I know?"
    m "I KNOW YOU HAVE IT! GIVE IT BACK YOU LITTLE BASTARD!"
    pc "I don't have your stupid wine..."
    m "Oh, so the bottle just disappeared from the kitchen table by itself? DO YOU THINK I'M STUPID?!"
    pc "You mean the bottle you drank before the last one?"
    m "What?!"
    pc "Maybe you should drink a little bit less, then you might actually remember how much you drank..."
    m "What did you just say?"
    m "Do you think I don't know how much I drink?!"
    pc "Obviously..."
    m "Oh, you will regret saying this! Come here, take your pants off!"
    stop music fadeout 2
    pcthink "W-What?"
    if pcgender == "man":
        m "As a punishment, I will suck your cock!"
    else:
        m "As a punishment, I will lick your pussy!"
    pcthink "What the...!"
    m "SHUT UP! You'll regret everything you said once I have... *hmmmph* *slurp*"
label eHumpNight5_r:
    if _in_replay:
        show screen endRep
    pcthink "What the fuck!"
    e "Hmmm... *slurp* *slurp*"
    pcthink "Shit, what's going on?!"
    m "*Slurp*"
    pc "Damn, this feels good..."
    e "Hn..."
    pcthink "W-Wait, what?"
    scene pcroomebjfirst with slowdissolve
    pcthink "What the hell?"
    scene pcroomebjfirst2 with dissolve
    pause .5
    pc "[e]?!"
    scene pcroomebjfirst3 with dissolve
    scene pcroomebjfirst4 with dissolve
    pause .5
    pc "What are you doing [e]?"
    scene pcroomebjfirst5 with dissolve
    e "Hehe."
    scene ebj000 with dissolve
    scene ebj01
    pause 1
    pcthink "Am I still dreaming?"
    pause
    pcthink "Shit this is..."
    menu:
        "Shit this is..."
        "...so wrong, I need to stop her!":
            pc "[e] stop it! We can't do this!"
            scene pcroomebjfirst60 with dissolve
            e "Eh?!"
            pc "I'm sorry, [e], but that's... just wrong..."
            scene pcroomebjfirst6sad with dissolve
            pc "Can't we just..."
            scene pcroomebjfirst6sadrun with hpunch
            e "*Sniff*"
            pc "[e]?!"
            jump gameOverE
        "...so hot, I can't believe she's doing this!":
            $ efe -= 1
    pcthink "I would've never expected her to do something like this!"
    pause
    if pcgender == "man":
        pcthink "She's clearly inexperienced, but damn..."
    else:
        pcthink "Wow, she's really good with her tongue..."
    e "*Slurp*"
    scene pcroomehump1 with dissolve
    pc "Huh?"
    scene pcroomehump2 with dissolve
    pcthink "Shit..."
    if pcgender == "man":
        pc "Are you sure about this, [e]?"
        scene pcroomehump3 with dissolve
        e "Hn!"
        scene pcroom_ehump4 with dissolve
        pause .5
        scene pcroom_ehump3_2 with dissolve
        e "Haaahn..."
        scene pcroom_ehump3_3 with dissolve
        pc "Shit, [e]..."
        pcthink "She just shoved it in..."
    else:
        scene pcroomehump3 with dissolve
        pause 1
    scene pcroom_ehump4 with dissolve
    e "Nnn..."
    scene es01 with dissolve
    $ pov1 = "es01"
    $ pov2 = "es_02"
    show screen povscreen(pov1)
    pause
    pcthink "Gaaawd..."
    if pcgender == "man":
        extend " so tight!"
    else:
        extend " [e]..."
    e "Nnnh..."
    pause
    pc "Damn, [e], this feels incredible!"
    e "Hnn... nhnn..."
    pause
    pc "Shit, I'm going to cum, [e]!"
    e "Hnnn... haah..." with flash
    scene pcroom_ehump_cum with flash
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    e "Nnnhaaah!" with flash
    scene pcroom_ehump3_4 with dissolve
    e "Haa..."
    scene ebj_ac_00 with hpunch
    e "*Pant*"
    scene ebj_ac with dissolve
    n "[e] collapses on top of you, she hugs you tightly and softly kisses your neck a few times while still panting heavily."
    if pcgender == "man":
        pcthink "Damn, I came right inside her..."
        pause 1
        pcthink "..."
        pcthink "Doesn't she want me to pull out?"
    n "You hug her and softly stroke her back for a while until both of you fall asleep."
    $ renpy.end_replay()
    scene black with slowdissolve
    $ storyEvent = False
    $ actionsUsed = 15
    call dateTime from _call_dateTime_16
    
label eschool_d6:
    $ efe -= 1
    scene school_e_random1 with dissolve
    pcthink "Looks like it's break time..."
    scene school_e_random2 with dissolve
    pcthink "Not many pupils out here... but it's hot today, so... huh?!"
    scene school_e_random3 with dissolve
    pcthink "[e]? She's alone?"
    scene school_e_random4 with dissolve
    pc "Hey, [e]!"
    scene school_e_random5 with dissolve
    pause 1
    scene school_e_random6 with dissolve
    pc "Hey, I'm going for a walk and thought I'd come by and have a look if I see you."
    scene school_e_random9 with dissolve
    play sound "audio/schoolbell.mp3"
    e "*Smooch*"
    scene school_e_random8 with dissolve
    pc "Too bad, looks like the break is over already..."
    scene school_e_random9 with dissolve
    pause 1
    scene school_e_random7_2 with dissolve
    pc "See you at home, [e]."
    scene school_e_random10 with dissolve
    pcthink "Well, time to move on..."
    scene black with dissolve
    $ visit_e_d6 = True
    call screen wmap
    
label d7_evening_e:
    scene pcroom_d7_coding with dissolve
    pcthink "Hum..."
    pcthink "Alright, I think I'll stop for today... I've made some progress at least..."
    pc "..."
    pcthink "Hum... maybe I'll watch some VR porn..."
    pcthink "Oh wait, I still need some answers from [m], I should go ask her out first!"
    if rpills:
        pcthink "Wait, did I give her a pill today?"
    play sound "audio/door_close.ogg"
    pc "Huh?"
    scene d7_pcroom_kitty1 with dissolve
    pc "Oh hey, err..."
    pcthink "That catgirl costume again."
    pc "... Kitten."
    scene d7_pcroom_kitty2 with dissolve
    e "Nya!!"
    scene d7_pcroomkitty3 with vpunch
    pc "Wha..."
    scene black with dissolve
    pc "Umph!"
    scene d7_pcroomkitty4 with dissolve
    pcthink "I guess I won't ask [m] any questions today..."
    pause
    scene d7_pcroom_kitty5 with dissolve
    pc "You really like to assault me out of nowhere, don't you, [e]?"
    e "Khehe!"
    scene d7_pcroom_kitty6 with dissolve
    pc "Hm?"
    scene d7_pcroom_kitty7_2 with dissolve
    pause 1
    scene d7_pcroom_kitty7 with dissolve
    pc "Do you want to use it?"
    scene d7_pcroom_kitty8 with dissolve
    e "HN!"
    scene d7_pcroom_kitty10 with dissolve
    pc "Okay..."
    pc "But no porn!"
    scene d7_pcroom_kitty9 with dissolve
    e "Unh..."
    pc "Arf... fine, you're old enough anyway..."
    scene d7_pcroom_kitty11 with dissolve
    e "Khehehe."
    scene black with dissolve
    scene d7_pcroom_kitty12 with dissolve
    e "Whoooo!"
    if pcgender == "man":
        pcthink "Damn, she really likes these lesbian scenes."
    else:
        pcthink "Damn, she's really into that stuff."
    scene d7_pcroom_kitty13 with dissolve
    pcthink "Hum, isn't that the scene where the camera suddenly shakes for a few seconds?"
    scene d7_pcroom_kitty14 with dissolve
    e "Ugh uhhh..."
    pcthink "Yep, it is."
    scene d7_pcroom_kitty15 with dissolve
    pc "Whoa, hold tight, [e]!" with hpunch
    scene d7_pcroom_kitty16 with dissolve
    e "Uhhh..."
    pc "Haha, looks like it was a bit too much."
    scene d7_pcroom_kitty17 with dissolve
    e "Unnnh..."
    pc "Don't worry, it'll stop in a few seconds."
    scene black with fade
    n "After a while..."
    scene d7_pcroom_kitty18 with dissolve
    pcthink "Hum... she's fallen asleep..."
    scene d7pcroomkitty18_2 with dissolve
    pcthink "Looks like it hit her a bit harder then I'd have expected..."
    e "{size=-10}Hnnn...{/size}"
    pc "...Cutie..."
    pcthink "I guess I should take her to bed..."
    menu:
        "Her bed.":
            $ d72esbed = True
            scene black with dissolve
            scene d7_cr_kitty19 with dissolve
            pcthink "...she's so cute..."
            pause
            scene d7_cr_kitty19_2 with dissolve
        "Your bed.":
            scene d7_pcroom_kitty19 with dissolve
            pcthink "...she's so cute..."
            pause
            scene d7_pcroom_kitty19_2 with dissolve
    pcthink "Well, I guess I should get some sleep too..."
    pc "Good night, sweetie..."
    scene black with fade
    $ storyEvent = False
    $ SEd7walk = False
    $ actionsUsed = 13
    call dateTime from _call_dateTime_19

label d8_etalk:
    scene d8_e_talk1 with dissolve
    pc "Hey [e], there's something we should talk about."
    scene d8_e_talk2 with dissolve
    pc "I'm sure [j] told you about her situation..."
    e "Hn!"
    scene d8_e_talk2_2 with dissolve
    pc "Good... well I was thinking that... maybe she could live here for a while... with us."
    e "HN!"
    scene d8_e_talk3 with dissolve
    pc "Oh she told you about it already?"
    e "Nhn!"
    pc "Ha, of course she did."
    scene d8_e_talk4 with dissolve
    pc "Well, I told her I'll ask [m], but I'm also asking you. I don't want her to live here if you're not okay with it..."
    pc "I know you're friends, but I also know that she can be a bit annoying at times, so if you don't want her to live here, you can tell me."
    pc "So, what do you think, should we let her live with us for a while?"
    scene d8_e_talk4_2 with dissolve
    scene d8_e_talk4 with dissolve
    e "Nnn!"
    pc "Err... just to make sure, you're okay with her staying here?"
    e "HNNN!"
    scene d8_e_talk4_2 with dissolve
    scene d8_e_talk4 with dissolve
    scene d8_e_talk4_2 with dissolve
    scene d8_e_talk4 with dissolve
    n "She nods in a very exaggerated way to make sure that you really get it."
    pc "Haha, okay I get!"
    scene d8_e_talk5 with dissolve
    e "Khehe."
    pc "So now we only have to convince [m]... which might not be so easy..."
    pc "You don't happen to know anything that could convince her?"
    scene d8_e_talk6 with dissolve
    e "Hum..."
    scene d8_e_talk5 with dissolve
    scene d8_e_talk_kiss with dissolve
    e "Mwhaa"
    scene d8_e_talk5 with dissolve
    pc "Wait a minute, that gives me an idea..."
    pc "I think I should go talk to [m] now, thanks [e]."
    e "Khehe."
    scene black with fade
    jump d8_rachel_pills
    
label d9_ebathroom:
    play sound "audio/shower_end.mp3"
    scene d9morningbr01 with dissolve
    pcthink "...time to get out."
    play sound "audio/door_close.ogg"
    pause .5
    scene d9_morning_br02 with dissolve
    pcthink "Hm? [e]?"
    scene d9_morning_br02_2 with dissolve
    e "..."
    scene d9_morning_br03 with dissolve
    pcthink "Doesn't she notice me?"
    scene d9_morning_e with dissolve
    menu:
        "(Make a noise)":
            pc "Ahem!"
            scene d9_morning_br05 with dissolve
            e "Eh?"
            pc "Good morning [e]..."
        "(Wait)":
            play sound "audio/epee.ogg"
            pause 19
            pc "Erm..."
            stop sound
            scene d9_morning_br05 with dissolve
            e "Eh?"
            pc "Morning [e], I was wondering when you'd notice me, haha."
    scene d9_morning_br06 with dissolve
    pause 1
    scene d9_morning_br07 with dissolve
    e "*Smooch*"
    scene d9_morning_br08 with dissolve
    pause 1
    play sound "audio/door_close.ogg"
    scene d9_morning_br09 with dissolve
    pcthink "Wow, she was still half asleep..."
    scene d9morningbr10 with dissolve
    pcthink "Anyway, let's get ready for the day."
    scene black with fade
    n "You get dressed and go to the living room where the others have already started their breakfast."
    jump d9_breakfast
    
label d9_pcroom_e01:
    play sound "audio/door_close.ogg"
    if _in_replay:
        show screen endRep
    pcthink "Alright, I guess I should look for..."
    scene d9_pcroom_backhome_e01 with dissolve
    pcthink "Huh? What the..."
    pc "[e]?"
    pcthink "What's she doing?"
    scene d9_pcroom_backhome_e02 with dissolve
    pc "[e] are you alright?"
    pause
    pcthink "Oh, I get it, she's trying to prank me again."
    scene d9pcroombackhomee03 with dissolve
    pcthink "But not this time!"
    play sound "audio/slap1.ogg"
    scene d9pcroombackhomee04 with hpunch
    n "*SMACK*"
    scene d9_pcroom_backhome_e05 with dissolve
    e "WHAAA!"
    scene d9_pcroom_backhome_e06 with dissolve
    pc "Haha, gotya!"
    e "HNN!"
    pc "What? Are you mad that I didn't fall for your little prank? You won't get me so easy anymore."
    scene d9_pcroom_backhome_e07 with dissolve
    e "Mmmmm!"
    pc "Haha, you're cute."
    scene d9_pcroom_backhome_e08 with dissolve
    pc "By the way, why are you wearing my shirt?"
    scene d9_pcroom_backhome_e08_2 with dissolve
    e "..."
    pc "Speak up young lady, or I'll have to..."
    scene d9pcroombackhomee09
    pc "Tickle you until you submit!" with hpunch
    scene d9_pcroom_backhome_e10 with dissolve
    e "Wha..."
    scene d9_pcroom_backhome_e11 with vpunch
    e "Hahahahaha!"
    pc "WHOA!"
    play sound "audio/drop.ogg"
    scene d9pcroombackhomee12 with hpunch
    pc "Ouch..."
    scene d9_pcroom_backhome_e12_2 with dissolve
    e "Hnn..."
    scene d9_pcroom_backhome_e13 with vpunch
    pcthink "Uff, she's heavier than she looks."
    scene d9_pcroom_backhome_e14 with dissolve
    e "Mmmmh..."
    scene d9_pcroom_backhome_e15 with dissolve
    pc "Cutie..."
    scene d9_pcroom_backhome_e16 with dissolve
    pc "Eh?"
    scene d9_pcroom_backhome_e17 with dissolve
    pause .5
    scene black with dissolve
    scene d9_pcroom_backhome_e18 with dissolve
    pcthink "Oh damn!"
    scene black with dissolve
    scene d9_pcroom_backhome_e19 with dissolve
    pc "Cute and hot!"
    scene d9_egrind_060 with dissolve
    show d9egrind
    if jlo > 2:
        pcthink "Shit, first [j] and now [e] too?"
    pause
    if jlo > 2 and pcgender == "man":
        pcthink "Damn, okay, I'm rock hard again just from her grinding on it..."
    elif pcgender == "man":
        pcthink "Damn, I'm rock hard just from her grinding on it..."
    if pcgender == "woman":
        pc "Hmm, you're so beautiful, [e]."
        e "Khehe..."
    scene d9_pcroom_backhome_e21 with dissolve
    pause 1
    scene black with dissolve
    scene d9_pcroom_backhome_e22 with dissolve
    e "..."
    scene black with dissolve
    scene d9_pcroom_backhome_e23 with dissolve
    pause 1
    scene black with dissolve
    scene d9_pcroom_backhome_e24 with dissolve
    pcthink "Oh I know where this is going."
    pc "Give me that cute pussy!"
    scene d9_pcroom_backhome_e25 with dissolve
    pause .5
    pc "Look who's all excited already."
    e "*Smooch* kehehe."
    if pcgender == "man":
        n "[e] kisses the head of your dick and starts to suck it."
    else:
        n "[e] kisses your already moist slit and starts to lick your clit."
    pcthink "Alright, time to taste that honey I guess."
    show d9elicksuck
    pause
    e "Hnnnn..."
    pcthink "Wait, what's this taste?"
    e "...nnnh."
    pcthink "This tastes like..."
    scene d9pcroombackhomee26 with dissolve
    pc "[e] did you smear honey onto your pussy?"
    e "Mhmm..."
    pc "Haha, you're crazy!"
    e "Khehehe!"
    show d9elicksuck
    pcthink "Did she plan this together with [j]?"
    if jlo > 2:
        if pcgender == "man":
            pcthink "But if [j] knew about it, why did she want to go down on me first?"
        else:
            pcthink "Naughty girls!"
    pause
    $ pov1 = "d9elicksuck1"
    $ pov2 = "d9elicksuck2"
    show screen povscreen(pov1)
    pcthink "Damn, now she's giving it her all..."
    
    pc "Oh shit, this feels great [e]!"
    e "Hnnn... nnnnhnn!"
    pause
    e "Nnnnh... hnnn!"
    pcthink "Oh damn, oh shit!"
    if pcgender == "woman":
        scene d9elick_00
        show d9elick4
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    if pcgender == "man":
        scene d9_pcroom_eride_switch1 with dissolve
        pcthink "Shit, what is she..."
        scene d9_eride with dissolve
        pcthink "Now she wants to ride me? Shit, I already almost came!"
        scene d9_eride01_00 with dissolve
        $ pov1 = "d9eride1"
        $ pov2 = "d9eride2"
        show screen povscreen(pov1)
        pause
        e "Nhhh... haaa..."
        pcthink "Damn, I'm so close..."
        scene d9_eride03_00 with dissolve
        $ pov1 = "d9eride3"
        $ pov2 = "d9eride4"
        if campov:
            show screen povscreen(pov2)
        else:
            show screen povscreen(pov1)
        pause
    pc "Oh god, oh god... I'm gonna..."
    e "HAAAA!" with flash
    if pcgender == "man":
        if campov:
            scene d9_eride04_cum with dissolve
        else:
            scene d9_eride03_cum with dissolve
        hide screen povscreen
        hide screen povbutton
    e "Hnaaa, haaa, haaaaa!" with flash
    if efe <= 2 and jlo >= 4:
        scene d9_eride_cum_face
        pause .1
    if pcgender == "man":
        if campov:
            scene d9_eride04_cum with flash
            scene d9_eride04_cum with flash
        else:
            scene d9_eride03_cum with flash
            scene d9_eride03_cum with flash
        pc "Fuck..."
        scene black with fade
    else:
        scene d9_elick_cum with flash
        pc "Hnnaaa..."
        scene black with fade
    e "*pant*..."
    extend "*pant*"
    pc "Damn..."
    scene d9eend1 with slowdissolve
    e "..."
    pc "..."
    pc "I can still taste that honey..."
    scene d9eend2 with dissolve
    e "Kehehehe..."
    scene d9eend3 with dissolve
    e "*Smooch*"
    scene black with slowdissolve
    $ renpy.end_replay()
    n "You cuddle for a while until you remember that you wanted to question [m] about that woman you're supposed to know."
    pc "I'll be right back, [e]."
    e "Mhmm."
    jump d9_jhall
    
label d10eshow:
    play sound "audio/door-opening.ogg"
    scene d10eshow01 with dissolve
    pc "Hm? Where's [e]?"
    e "NYAAAAA!"
    scene d10eshow02 with dissolve
    pc "Wh...{w=.5}{nw}"
    scene black with hpunch
    pc "Whoa!"
    j "Haha, I don't remember that being part of the plan, [e]."
    scene d10eshow03 with dissolve
    e "Khehehe!"
    pc "Damn... what are you guys up to?"
    scene d10eshow04 with dissolve
    j "[e] wasn't sure what to wear today, so we decided to let you decide."
    j "Though, I'm not so sure if that's still the plan, hehe."
    scene d10eshow05 with dissolve
    e "Eh..."
    scene black with dissolve
    n "[e] gets up and you place yourself on the bed next to your old teddy bear..."
    scene d10eshow06 with slowdissolve
    n "Seeing the old teddy again makes you think about old times before your mom died..." with dissolve
    pc "..." with dissolve
    j "Hey, [e]..."
    scene d10eshow07 with dissolve
    j "...hurry up, [pc] is getting bored already!"
    scene d10eshow08_2 with dissolve
    pc "Huh? No I was just thinking about something..."
    scene d10eshow08_1 with dissolve
    j "Maybe you need to shake your ass a bit to get [hisher] attention, hehe."
    scene d10eshow09_1 with dissolve
    pause .5
    scene d10eshow09_2 with dissolve
    pause .5
    scene d10eshow09_1 with dissolve
    pause .5
    scene d10eshow09_2 with dissolve
    pause .1
    scene d10eshow08_1 with dissolve
    pc "Haha, yes, I'm fully focused now!"
    e "Khehe."
    j "Now hurry up, [e] before [heshe] loses concentration again!"
    e "Hn!"
    scene black with slowdissolve
    scene d10eshow12 with dissolve
    j "Oh come on [e], that looks almost like your normal outfit!"
    menu:
        "Looks great, I like it.":
            $ of12 = True
        "Nah, your normal outfit looks better.":
            pass
    j "Show [himher] the next outfit, [e]."
    e "Hn!"
    scene black with slowdissolve
    scene d10eshow11 with dissolve
    j "Uhh, I like that one!"
    menu:
        "Hot!":
            $ of11 = True
        "Nah, that's too goth style.":
            pass
    j "Okay, next one, [e]."
    scene black with slowdissolve
    scene d10eshow10 with dissolve
    j "Cuuuuute~"
    menu:
        "Looks great, but isn't that a little bit too much for everyday use?":
            $ of10 = 1
        "Luscious! I love it!":
            j "I knew it, hehe!"
            $ of10 = 2
        "Nah, your normal outfit looks better.":
            pass
    j "Next one, [e]."
    scene black with slowdissolve
    scene d10eshow13 with dissolve
    j "Haha, we should do a cosplay together one time, [e]."
    j "Next one."
    scene black with slowdissolve
    play sound "audio/doorbell.ogg"
    scene d10eshow14 with dissolve
    j "Aww, who's that now..."
    scene d10eshow15 with dissolve
    pc "Damn, [m] is probably still under the shower..."
    scene d10eshow16 with dissolve
    pc "Guess, I should open the door then. Why don't you choose the next outfit until I'm back?"
    scene d10eshow17 with dissolve
    pc "By the way, I like this outfit most, [e]."
    e "Khehe."
    scene black with slowdissolve
    pause .5
    play sound "audio/door-opening.ogg"
    scene d10kataes01 with dissolve
    pc "Oh... [t]..."
    pc "Right, you got a session with [e], right?"
    scene d10kataes02 with dissolve
    t "..."
    scene d10kataes03 with dissolve
    pc "Erm..."
    scene d10kataes04 with dissolve
    pc "Yeah it's nice to see you, too, why don't you just come in..."
    scene d10kataes05 with dissolve
    pc "..."
    pc "Jeez, what's up with her again..."
    scene d10kataes06 with dissolve
    if seentd9:
        pcthink "And here I thought she'd be a bit more... reasonable after yesterday..."
        pcthink "She's like the prototype of a tsundere in manga..."
        pcthink "I wonder if she ever reads manga."
    pc "..."
    pcthink "Oh shit, I hope [e] got dressed in time!"
    pcthink "..."
    if not mend:
        jump d10shower2
    else:
        jump d10pcroombeforekh