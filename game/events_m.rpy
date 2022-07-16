########## Rachel
label rachelBathroomDay0:
    $ SErachelBathroomDay0 = False
    $ storyEvent = False
    scene bathroom rachel shower with dissolve
    pcthink "HOLY!!!"
    scene hallbathroomdoor
    pc "..."
    pcthink "Shit, that was [m]..."
    pcthink "..."
    pcthink "I don't think I have ever seen her like that... she's actually hot!"
    pcthink "Maybe I could..."
    pc "..."
    scene bathroom rachel shower2 with dissolve
    pause
    pcthink "Wow... that ass..."
    pause
    pcthink "I better leave now."
    scene hallbathroomdoor with dissolve
    pcthink "It would've been really embarrassing for both of us if she'd seen me."
    if pcgender == "woman":
        pcthink "On the other hand, she doesn't know I'm lesbian, so she might not even care... hehe."
    scene hall_back_idle with dissolve
    pcthink "Damn, I really need to use the bathroom..."
    pcthink "I guess I'll have to wait until she is done in there."
    scene black with dissolve
    n "1 Hour later" with dissolve
    play sound "audio/flush.ogg"
    pause 2
    scene bathroompcwashhands with dissolve
    play sound "audio/running-water.ogg" loop fadein 1
    pcthink "Phew that was too close..."
    if pcgender == "woman":
        scene bathroom pcfem mirror with dissolve
    pcthink "[m] really took her time in the shower."
    pcthink "..."
    play sound "audio/running-water_end.ogg"
    scene bathroompcleave with dissolve
    pcthink "It sounds like [m] is making breakfast, maybe I should help her..."
    scene hall_back_idle with dissolve
    pcthink "...or maybe not."
    scene home_hall_entrance_idle with dissolve
    pcthink "I mean, I still hate that bitch... right?"
    scene kitchen rachel doing breakfast with dissolve
    pcthink "Right? ..."
    scene kitchen rachel lookback2 with dissolve
    m "Good morning [pc]. Did you sleep well?"
    pc "Uh... no not really to be honest. I guess that's what you get from sleeping in a chair..."
    scene kitchen rachel breakfast3 with dissolve
    m "Oh no! I'm sorry, I wasn't sure if I should wake you up. You looked so tired yesterday."
    pcthink "Damn, doesn't she wear a bra?..."
    pc "Uhh... then it was you who put the blanket on me?"
    scene kitchen rachel breakfast4 with dissolve
    m "Yes, I hope that's okay?"
    pc "Yeah... thanks."
    $ actionsUsed = 1
    call dateTime from _call_dateTime_8
    menu:
        q "Ask if she needs help with the breakfast?"
        "Yes":
            m "Oh that's nice of you to ask. Thank you. I'm almost done anyway, but..."
            jump breakfastDay0
        "No":
            jump breakfastDay0
label breakfastDay0: 
    m "Could you do me a favor and wake up [e]? Breakfast will be ready in a minute and she tends to oversleep."
    pc "Yeah, sure."
    m "Thanks, Hun."
    scene black with dissolve
    n "..."
    scene home_hall_idle with dissolve
    pcthink "Okay, [e]'s room should be the last one on the right."
    scene hall door with dissolve
    pcthink "I guess I should knock..."
    menu:
        "Knock at the door":
            play sound "audio/knock-door1.ogg"
            n "*knock* *knock*"
            pc "Hey [e] are you awake?"
            pcthink "No answer"
            pcthink "Err... she doesn't talk, what did I expect?"
            pc "I'm coming in."
            jump childRoomDay0
        "Just open the door":
            $ mob +=1
            jump childRoomDay0
            
label rachelMorningKitchen:
    m "Good morning [pc]. Did you sleep well?"
    pc "Yeah, thanks."
    menu:
        n "Ask if she needs help?"
        "Yes":
            m "Oh that's nice of you to ask. Thank you."
            jump breakfast
        "No":
            jump breakfast
        
label breakfast: 
    m "Why don't you sit down, breakfast will be ready in a minute."

label mTellNotToDisturb:
    scene kitchen rachel fridge with dissolve
    m "Hey [pc]."
    scene kitchen rachel fridge2 with dissolve
    m "How was your day?"
    pc "Hey... Nothing special. I slept half the day."
    pcthink "Does she ever wear a bra?"
    m "Oh... Why didn't you go out?"
    pc "I was still a bit tired. The last night in the motel was kind of... short."
    m "Oh I see, then it's good you got a bit more sleep."
    pc "Yeah..."
    m "Um... well, did you need something?"
    pc "No, I just wanted to grab a snack."
    m "Oh okay. There's a lot in the fridge, grab whatever you like!"
    scene kitchen fridge closed with dissolve
    pc "Yeah, thanks."
    scene kitchen fridge open with dissolve
    window hide
    pause 1
    window show
    m "Oh [pc], there is one thing..."
    pc "Mhm?"
    pcthink "Hmm what should I take."
    m "I..."
    pc "Yeah?"
    m "I... I tend to... read some books in my room for one or two hours every afternoon and..."
    pcthink "...hmm... I can't decide..."
    m "... and I would prefer not to be disturbed at that time."
    m "So I hope that's no problem?"
    scene kitchenfridgeopentake with dissolve
    pc "Yeah, sure. No problem."
    m "Oh, okay. Thank you for understanding, Hun. I'll be in my room then."
    scene kitchen fridge closed with dissolve
    pc "Yeah, later..."
    pcthink "What was that all about? She seemed to be nervous..."
    scene black with dissolve
    pause 1
    n "A bit later" with dissolve
    window hide
    pause 2
    play sound "audio/running-water.ogg" loop
    scene bathroompcwashhands with dissolve
    pcthink "Damn that was sticky. I should have used a fork..."
    play sound "audio/running-water_end.ogg"
    scene bathroompcclosesink with dissolve
    pcthink "Huh? The tap is dripping..."
    scene bathroompcfiddle with dissolve
    n "You fiddle a bit with the tap and quickly find out that a loose joint is the reason for it leaking."
    pcthink "Alright, that's easy, I can fix that. All I need is a wrench."
    pcthink "I should ask [m] where the tools are."
    scene black with dissolve
    $ storyEvent = True
    $ SErachelPills1st = True
    $ actionsUsed = 1
    call dateTime from _call_dateTime_9
    scene hall_back_idle with dissolve
    call screen map_hall_back
    
label rachelPills1st:
    pcthink "Err... wait, didn't [m] tell me not to disturb her?"
    pcthink "Hmm..."
    pcthink "But on the other hand, if I'm going to fix her stuff, why would she complain?"
    pcthink "...but I should knock, just to be sure."
    menu:
        "Knock at the door":
            play sound "audio/knock-door1.ogg"
            n "*knock* *knock*"
            m "Come in."
            scene bedroom rachel lay onbed1 with dissolve
        "Just open the door":
            $ mob +=1
            scene bedroom rachel lay onbed0 with dissolve
            pause .5
            scene bedroom rachel lay onbed1 with dissolve
            m "Oh hey Hun. Come in."
    pc "Hey, [m]. I know you told me not to disturb you, but..."
    scene bedroom rachel lay onbed2 with dissolve
    m "Oh don't worry, Hun."
    pcthink "Huh? Looks like she doesn't mind."
    scene bedroom rachel sit onbed1 with dissolve
    m "What can I do for you?"
    pc "Do you have any tools? I need a wrench."
    m "Sure. Follow me, I'll show you where they are."
    pcthink "Wow, I would have expected her to be at least upset with me for disturbing her."
    scene black with dissolve
    n "You follow her to your room."
    scene pcroom searchfortools2 with dissolve
    m "There, these are all the tools we have."
    pc "Err... there aren't many..."
    scene pcroom searchfortools with dissolve
    m "What was it you needed again, a wrench?"
    pc "Yeah."
    scene pcroom searchfortools3 with dissolve
    pause 1
    scene pcroom searchfortools with dissolve
    m "What does it look like?"
    pc "A bit like a bone I guess."
    scene pcroom searchfortools4 with dissolve
    m "Hmm, I don't think we have a bone tool."
    pcthink "What's up with her, is she drunk? She's not that stupid..."
    pc "It's not a bone tool, it just looks a bit like a bone."
    scene pcroom searchfortools with dissolve
    m "Oh... sorry, Hun, but I don't think we have a tool that looks like a bone either."
    pc "Yeah... looks like it... not even a real pair of pliers."
    n "Suddenly your stomach begins to growl."
    m "Oh, are you still hungry? I'll make you something to eat."
    pc "No, it's okay, I'll just grab another snack later."
    pcthink "It's not even dinnertime and she wants to make me something to eat?!"
    m "Are you sure? I'll gladly do anything for you."
    pcthink "WTF!"
    pc "Uh... yeah, no, thanks, I'm fine!"
    m "Okay, but be sure to tell me if you need anything, Hun."
    pc "Yeah... sure, thanks."
    scene black with dissolve
    n "She goes back to her room."
    scene pcroom with dissolve
    pcthink "What the fuck was that?"
    pcthink "She would do anything for me? Did she really say that?"
    scene black with dissolve
    n "The rest of the day is quite uneventful and you go to bed early."
    stop music fadeout 2
    $ SErachelPills1st = False
    $ SEpcDay1Morning = True
    $ actionsUsed = 8
    call dateTime from _call_dateTime_10

label rachelPills2nd:
    if _in_replay:
        show screen endRep
    menu:
        "Knock at the door":
            play sound "audio/knock-door1.ogg"
            n "*knock* *knock*"
            m "Come in."
            scene bedroom rachel lay onbed1 with dissolve
        "Just open the door":
            $ mob +=1
            scene bedroom rachel lay onbed0 with dissolve
            pause .5
            scene bedroom rachel lay onbed1 with dissolve
            m "Oh hey Hun."
    pcthink "Shit, I forgot that she doesn't want to be disturbed in the afternoon."
    scene bedroom rachel sit onbed1 with dissolve
    pc "Uh, hey [m], sorry to disturb you again..."
    m "Oh you're not disturbing me, I'm always happy to see you."
    pcthink "Okay... she's being weird again."
    pc "Uh, yeah, but you told me not to disturb you in the afternoon."
    scene bedroom rachel sit onbed2 with dissolve
    m "Oh that? Don't worry about it, Hun. You know, I said it because I have to take these pills."
    pc "Pills?"
    m "Yes, they help me to get my head straight, but they also make me a bit woozy for an hour or so."
    pcthink "So that's why she's acting so weird."
    m "The doc said I should make sure to be alone or with only a few people I can really trust..."
    m "But I know I can trust you. You're my [pc] after all. Right, Hun?"
    pcthink "\"Her\" [pc]??"
    pc "Uh, yeah, of course you can trust me..."
    m "I knew it."
    pc "Err... anyway I wanted to ask you something..."
    m "Sure, what is it? You can ask me anything."
    pcthink "Wow, she's so overly friendly it's almost scary."
    pc "Uh... there is this therapist woman with [e] right now."
    m "[t]? Oh I forgot to tell you about her. I'm sooo sorry, Hun!"
    pcthink "Damn, these pills sure have an effect on her... I'll definitely need some time to get used to this..."
    pc "Don't worry about that, but don't you think she is a bit... unfriendly?"
    m "Do you think so?"
    pc "Absolutely..."
    pcthink "Not to mention that shes a bitch!"
    m "Hum... well she is still young and yes, she can be a bit strict, but don't worry Hun. She is really good at what she does."
    pc "And what exactly is she doing?"
    scene bedroom rachel sit onbed4 with dissolve
    m "I don't know the exact procedure, but she helps [e] and that's what counts for me."
    pc "[e] didn't seem to be overly excited..."
    scene bedroom rachel sit onbed2 with dissolve
    m "I know she doesn't like the sessions with her, but what should I do? There is no one else willing to help her anymore. Everyone gave up on her and [t] really wants to help."
    pcthink "And I bet she wants a lot of money for it..."
    pc "I didn't get the impression that she really cares for [e]..."
    m "Oh Hun, please don't judge her just by your first impression. I know you're worried about [e], but [t] really isn't that bad of a person. Give her a chance, okay?"
    pc "Well, if you say so..."
    m "Thank you, Hun, I knew you would understand."
    pcthink "I guess I need to find another Therapist myself..."
    m "Haahh... getting you back home was really the best decision I ever made."
    pc "Getting me back? What do you mean?"
    m "Oh, you know. After all that happened with your dad and then with [e], I almost lost the will to live..."
    pcthink "Seriously? And she's just casually telling me about it?"
    scene bedroom rachel sit onbed3 with dissolve
    m "...and after I realized how shitty I was to you, it got even worse... I almost destroyed your childhood and [e] lost her precious big [bs] because of me..."
    pc "Well I wasn't really a child anymore..."
    pcthink "...not that it makes it better..."
    m "I know, but still..."
    scene bedroom rachel sit onbed1 with dissolve
    if pcgender == "man":
        m "But now you're back. [e] is happy to have her big [bs] back and I'm happy to have a handsome young [pcgender] here I can count on and trust."
        pcthink "Handsome huh? Eh... wait..."
    else:
        m "But now you're back. [e] is happy to have her big [bs] back and I'm happy to have a beautiful young [pcgender] here I can count on and trust."
        pcthink "Beautiful huh? Eh... wait..."
    pc "So you're not actually letting me live here to help me out, but to help yourself!?"
    scene bedroom rachel sit onbed2 with dissolve
    m "Umm, yes, kind of."
    pcthink "Fuck I knew it! She was lying all the time!"
    m "But isn't it good for you, too?"
    pc "Huh?"
    m "After all, you don't have to pay any rent."
    pc "You know this is actually my house, right? You and... him were never married, so I could just throw you out at anytime."
    m "Of course I know that, Hun. But why would you do that now?"
    m "Aren't you happy to have your sister back? Or to have someone who makes you fresh meals every day, who washes your clothes and takes care of your needs?"
    pcthink "\"My needs\" huh? Hehe..."
    pcthink "...but damn, she's right. It's actually quite nice..."
    pcthink "I wonder if the pills are talking?"
    pc "I guess you're right, it helps us both."
    m "See? And if you ever need something, don't be afraid to ask me. I will do anything for you, whatever it is."
    pcthink "Fuck, she said it again..."
    pc "... Yeah... thanks, you told me already."
    m "Did I?"
    pc "Uhh... yes? Yesterday? In the afternoon! Don't you remember?"
    m "Yesterday, in the afternoon? Oh, I'm sorry sweetheart, I don't remember much of what I do when I take the pills."
    pc "Really? You just forget it?"
    m "Yes, I will most likely forget our conversation here, too."
    pcthink "Seriously? That's... interesting..."
    m "But please don't get this wrong Hun. Even if I forget it, everything I said was true and I really mean it!"
    pc "So you don't remember that I asked for tools yesterday?"
    m "Tools? No... why did you need them? Did I tell you where they are?"
    pc "Yeah, nevermind..."
    pcthink "Wait, this means she will forget everything that I say or that I do right in this moment?"
    pcthink "Maybe I could..."
    pc "And you don't remember that you showed me your tits?"
    pcthink "Fuck! That was stupid!"
    m "Umm, no. I don't think I ever remembered anything I did when I took the pills."
    m "But as I said, the effect only lasts for an hour or so. So when you need me to remember something, just tell me a bit later."
    pcthink "WTF, did she even realize what I just said?"
    pc "Err... are sure you heard what I said?"
    m "Yes, sure Hun."
    pcthink "Okaaayyy?"
    pc "Really?!"
    m "Yes, you said I showed you my tits."
    pcthink "The fuck!"
    pc "Do you remember me grabbing your tits?"
    pcthink "Fuck, don't overdo it, [pc]!"
    m "No I don't, I'm sorry Hun."
    pc "W!"
    pc "T!"
    pc "F!"
    pc "[m], do you even understand what I'm saying here?"
    m "Um... you said you grabbed my tits... Is something wrong, [pc]? Did I upset you somehow?"
    pc "Uh... no. It's alright..."
    pcthink "Holy shit! She doesn't even care. This is ridiculous!"
    pcthink "...maybe I could use this opportunity..."
    pcthink "I mean, she doesn't seem to mind... she is basically inviting me... isn't she?"
    m "Is everything alright, Hun?"
    pc "Errr... yeah..."
    pcthink "Damn, I just have to ask..."
    pc "So... you don't mind me grabbing your tits then?"
    m "Why would I, Hun?"
    pcthink "Fuck! Why did she have to say that..."
    pc "*Gulp* ...okay? Would you say the same if you hadn't taken the pills?"
    scene bedroom rachel sit onbed4 with dissolve
    m "Hum... I'm not sure..."
    scene bedroom rachel grabtits with dissolve
    m "...but it's okay, really, Hun."
    pcthink "Damn, she is serious..."
    pcthink "...should I...?"
    pcthink "Shit, she took the pills..."
    pcthink "But I'm not forcing her, right? She is basically begging me to touch her, right?"
    pcthink "After all she did to me, this is at least some kind of payback..."
    pcthink "Fuck, this is too alluring..."
    scene bedroomrachelpcgrabtits with dissolve
    pcthink "Damn, she really doesn't mind!"
    show brTitties with dissolve
    pcthink "They feel so soft!"
    pause
    m "Do you like them?"
    pc "Oh yes, I do!"
    m "That's good."
    pcthink "Gaawd I love these tits... I love these pills!"
    pause
    pcthink "These pills... shit, I don't know when she took them. They could wear off anytime."
    m "You can touch them whenever you want, sweetheart."
    pcthink "Shit!"
    hide brTitties
    scene bedroom rachel grabtits with dissolve
    pc "Yeah thanks, [m]."
    m "Anytime sweetheart. Do you want to see them?"
    pcthink "Holy Shit!"
    pc "*Gulp*"
    pc "Uh... I would love to see them, but no... maybe another time."
    pcthink "It's just too risky now."
    scene bedroom rachel sit onbed2 with dissolve
    m "Oh? Too bad I will most likely have forgotten about it by tomorrow."
    pcthink "That's exactly why."
    scene bedroom rachel sit onbed1 with dissolve
    m "You must remind me then, sweetheart."
    pc "Of course [m]! Later, [m]..."
    scene bedroom rachel sit onbed2 with dissolve
    m "Oh you are leaving?"
    pc "Yeah, uhh... I have something to do."
    m "Oh okay, see you later, [pc]."
    scene black with dissolve
    $ renpy.end_replay()
    pcthink "Damn, that was hot!"
    $ storyEvent = False
    $ SErachelPills2nd = False
    jump tLeavingDay1

label stuffArrivesDay3Door:
    scene hall stuffarrives rclosedoor with dissolve
    m "Yes, thank you, good bye..."
    pcthink "Damn that ass!"
    scene hall stuffarrives rachel with dissolve
    m "Oh hey Hun, good morning. I accepted your stuff, I hope that's okay?"
    pc "Yeah, sure, thanks [m]."
    scene hall stuffarrives rachel1 with dissolve
    m "It's not much though, is this really all of it?"
    pc "Yeah, I sold most of my stuff before I moved."
    scene hall stuffarrives rachel2 with dissolve
    m "Really? Why did you do that?"
    pc "I guess because it's a new start in a not so new city, so I wanted to buy some new furniture as well..."
    m "I see..."
    m "Well, I'm going to prepare breakfast, just holler if you need help with anything."
    pc "Yeah, thanks."
    scene hall stuffarrives boxes with dissolve
    pcthink "Damn, what happened to the boxes..."
    pcthink "I hope they didn't break anything."
    pcthink "Let's take the box with my computer and the other \"essentials for surviving\" stuff first, hehe."
    scene hall stuffarrives carry box with dissolve
    n "You grab the first box and take it to your room."
    scene black with dissolve
    pcthink "Alright, let's have a look."
    scene pcroomstuffarrivesunboxing with dissolve
    pcthink "Looks good so far..."
    scene pcroom stuffarrives lappytest with dissolve
    pcthink "Nice, I can finally use my computer again!"
    pcthink "Okay, I'll just carry the rest of the boxes to my room as well and head for breakfast afterwards."
    scene pcroom stuffarrives leaveroom with dissolve
    pcthink "And when [e] and [m] are gone, it's time to relax and have a good 'ol porn session! Hehe."
    scene hall stuffarrives boxes with dissolve
    pcthink "Hum... now that I think about it, I could use something more relaxing to wear..."
    pcthink "Which box did I put that shirt in again?"
    scene black with dissolve
    n "You rummage through the boxes for a while."
    n "A few minutes later you find the box with your clothes and carry it to your room."
    jump ellieVR
    
label rachelStuckInTraffic:
    scene pcroomlappyf95 with dissolve
    pc "Haha, oh em gee! Some people really need to get a real life."
    scene pcroom boxes with dissolve
    pcthink "Speaking of real life... I should finish unpacking..."
    n "*Mobile rings*"
    scene pcroomphonegetefromschool with dissolve
    pc "Who's that now..."
    scene pcroomphoneanswer with dissolve
    pc "Yeah?"
    m "{i}Hey, [pc]. It's [m].{/i}"
    pc "Huh?! Hey [m]..."
    pcthink "When did I give her my number?"
    m "{i}Can you do me a favor [pc]?{/i}"
    pc "Sure... what is it?"
    m "{i}I'm stuck in traffic, could you pick [e] up at school? She must be waiting already.{/i}"
    pc "Yeah, sure. Did you call her?"
    m "{i}No, I tried to reach [j], but she didn't respond.{/i}"
    pc "Why didn't you call [e]?"
    m "{i}She doesn't have a mobile.{/i}"
    pc "Huh? Why?"
    m "{i}She wouldn't know how to use it. She's not really good with electronics.{/i}"
    pc "Err... Are you sure about that?"
    m "{i}Yes, we had a laptop once, but she didn't even know how to start it and one day it was broken...{/i}"
    pcthink "Well that's interesting, she knew how to get my computer working {b}with{/b} the VR headset and that's not the easiest thing to do..."
    m "{i}...do you remember how to get to the school?{/i}"
    pc "Which one is it?"
    m "{i}Sunroad High, the same one you went to.{/i}"
    pc "Oh, okay, yeah I remember..."
    m "{i}Okay, thank you so much, Hun. See you later then.{/i}"
    pc "Yeah, later..."
    scene pcroomcloselappygete with dissolve
    pcthink "Thats interesting..."
    pcthink "Why would [e] pretend to be bad with electronics?"
    pcthink "Anyway, I better hurry!"
    $ storyEvent = True
    $ SEGetEFromSchool = True
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance



label rachelElliesBDayReminder:
    $ weekDay = 4
    m "Just to make sure, you know what day tomorrow is, right?"
    pc "Uhh... tomorrow is [wday]..."
    m "That's not what I meant [pc]."
    pcthink "Err... shit, tomorrow must be some kind of special day..."
    pcthink "Okay let me think... today is [dtoday], so tomorrow is the..."
    pcthink "...[day].. damn time flies by..."
    scene pcroom rachelenter jandeleft7 with dissolve
    m "Did you forget it?"
    pc "Uhh... n-no... uh I guess tomorrow is..."
    pcthink "Shit...[day] of [month]... [day] of [month]..."
    pcthink "...wait, this date... there was something... something special..."
    pc "Eh... [e]'s birthday?"
    scene pcroom rachelenter jandeleft4 with dissolve
    m "Oh, you remember. Thats so nice, I wasn't sure."
    pc "Ehehe, of course I wouldn't forget that... hehe..."
    scene pcroom rachelenter jandeleft6 with dissolve
    m "Good, it would be quite embarrassing if you don't have a present for the most important day of a young woman's life..."
    pcthink "*gulp* ...a present... fuck! Of course I don't have a present."
    pc "Err... yeah, that's true hehe..."
    pcthink "Fuck, she knows it!"
    m "Right? I mean you only become 18 once in your life..."
    pc "Absolutely..."
    pc "Wait, what? 18?!"
    scene pcroom rachelenter jandeleft8 with dissolve
    m "Uh.. yes? Don't tell me you don't know how old your sister is."
    pc "I... uh..."
    m "Oh, dear."
    pcthink "How can [e] be 18? She looks so much younger than that!"
    m "Well, I guess I can't really blame you. You were probably blinded by her looks. I know she's a bit underdeveloped for her age."
    pcthink "Shit! Why didn't I read the signs. [j] looks way older than [e] and they are classmates. And then [e] is way too flirty and... sexual... for how young she looks..."
    scene pcroom rachelenter jandeleft6 with dissolve
    m "Maybe you should buy {b}another{/b} present for her tomorrow morning?"
    pc "Yeah... I guess I should do that..."
    scene pcroom rachelenter jandeleft9 with dissolve
    m "I'm taking her on a small shopping trip tomorrow morning... well... when she wakes up..."
    m "She tends to oversleep on weekends, so you'll have a bit of time."
    pc "That's good, thanks [m]."
    m "Anytime, Hun."
    m "Well... I'm going to my room then... you... do remember what that means... right?"
    pc "Yeah, don't disturb..."
    scene pcroom rachel beforekisscheek with dissolve
    m "Right... Thank you, Hun!"
    scene pcroom rachel kisscheek1 with dissolve
    pcthink "Whoa, what the...?!"
    scene pcroom rachel kisscheek2 with dissolve
    pause 1
    scene pcroom rachel afterkisscheek with dissolve
    pcthink "... a kiss on the cheek!?"
    scene pcroom rachel afterkisscheek2 with dissolve
    pcthink "What the hell, she's never done that before!"
    scene pcroom rachel afterkisscheek3 with dissolve
    pc "..."
    scene pcroom rachel afterkisscheekleft with dissolve
    pcthink "Damn...I can still smell her perfume..."
    pc "..."
    stop music fadeout 2
    pcthink "Wait! ...is she playing with me?!"
    pcthink "She never would've kissed me back then..."
    pcthink "...and these clothes... she must know what kind of effect they have!"
    pcthink "...what kind of fucked up game is this???"
    pcthink "...and why? She won't gain anything from it..."
    pcthink "Damn..."
    pcthink "She's going to take the pills again... Maybe I can get her to tell me what she's up to..."
    pcthink "...but I can't just storm into her room, I should at least wait a bit until the pills take effect."
    scene pcroom beforesitonchair2box with dissolve
    pcthink "Alright, I'll just unpack the rest and sit down for a bit..."
    scene black with dissolve
    pc "..."
    scene pcroomsitonchair2box with dissolve
    pcthink "[e]'s birthday... Why would she tell me about it if she's just playing with me? Is [e] really going to turn 18 tomorrow?"
    pcthink "Shit, I don't get it... am I imagining things?"
    pcthink "Anyway I have to find a present for [e]. It's better to have one even if I don't need it..."
    pcthink "But what should I buy for her?"
    pc "Humph..."
    scene black with dissolve
    n "30 minutes later" with dissolve
    window hide
    pause 2
    
    jump flirtyJ
    
label rachelPills3rd:
    scene home_hall_entrance_idle
    stop music fadeout 2
    menu:
        "Knock at the door":
            play sound "audio/knock-door1.ogg"
            n "*knock* *knock*"
            m "O-Oh... one second..."
            n "You can hear some rustling from within the room."
            pause 3
            pcthink "What's going on in there?"
            m "Come in."
            play sound "audio/door-opening.ogg"
            scene bedroom rachelmast_emberrast with dissolve
            m "Oh, hi, Hun. Do you need something?"
            jump rachelPills3rd2
        "Storm in":
            #achievement
            $achievement.grant("Achievement_knock")
            init: 
                $achievement.register("Achievement_knock")
            $achievement.sync()
            ###########
            $ mob +=1
            play sound "audio/door-opening.ogg"
            scene bedroom rachelmast1 with hpunch
            pc "[m] I have to... What the!?"
            scene bedroom rachelmast2 with dissolve
            m "WHAA!! ...[pc]!?"
            pc "Err... I... err, sorry I just... wanted to ask you something."
            m "Y-Yes, sure... um..."
            m "...can you turn around for a second?"
            pc "S-Sure..."
            scene bedroom rachelmast lookaway with dissolve
            pcthink "Damn this is embarrassing."
            m "You should have knocked, Hun."
            pc "Yeah, I know I..."
            pcthink "Wait a second, didn't she take the pills? Why am I embarrassed, this is perfect!"
            scene bedroom rachelmast5 with dissolve
            m "Well, this is a bit embarrassing isn't it? I'm sorry, Hun."
            pcthink "Damn, she's hot!"
            scene bedroom rachelmast5_2 with dissolve
            m "H-Hun, aren't you supposed to look away?"
            pc "Why? Don't you like me looking at you?"
            scene bedroom rachelmast6 with dissolve
            m "Um... I..."
            m "I guess I don't mind..."
            pcthink "Ha! It works! ...now you'll tell me everything!"
            scene bedroom rachelmast_emberrast with dissolve
            m "Okay, Hun. Um... let's just forget about this little... incident. Okay?"
            pc "Yeah, sure..."
            pcthink "...ly not, hehe."
            m "So... what can I do for you, Hun?"
            pc "Err..."
            pcthink "Shit, what did I want here again?"
            pcthink "Ah, right."
            jump rachelPills3rd2
            
label rachelPills3rd2:
    pcthink "Okay, here we go..."
    pc "[m], why are you playing games with me?"
    scene bedroom rachelmast_emberrast2 with dissolve
    m "G-Games? What are you talking about?"
    pc "You know what I'm talking about. You kissed me on the cheek!"
    m "Oh, that... I'm sorry, did you dislike it?"
    pc "Err no, that's not the point..."
    pc "You would never have kissed me back then! You've even avoided coming close to me. And now?"
    pc "The clothes you're wearing and the perfume and your god damn overacted friendliness. That's not you! You're just playing with me! I know it!"
    m "Um I..."
    m "I'm sorry, Hun."
    pcthink "Ha! Looks like I hit the nail on the head!"
    m "I didn't expect to trigger so much emotion with just a kiss..."
    pc "Huh?!"
    m "I just wanted to show some affection."
    pc "Bullshit... you're lying!"
    m "I'm not playing games with you [pc]..."
    m "Is it wrong that I want to feel sexy sometimes?"
    m "Is it bad that I want to have a better relationship with you? To make up for everything I did to you?"
    pcthink "Damn, that's really not like her... she has changed a lot..."
    pcthink "Wait, what if she's still playing with me? What if she didn't take the pills this time?"
    pcthink "Only one way to find out..."
    pc "Quick, show me your tits [m]!"
    m "M-My tits?"
    pc "Yes, do it!"
    scene bedroom rachelmast titties1 with dissolve
    m "O-Okay, Hun..."
    pcthink "...shit."
    scene bedroom rachelmast titties3 with dissolve
    pcthink "Looks like I was wrong..."
    m "Is everything okay, Hun?"
    pc "...yeah..."
    pcthink "Shit, I really thought she was just playing with..."
    m "Don't you like them?"
    pc "Hm? No err... I mean yeah, I do like them."
    m "Thank you, Hun."
    if pcgender == "man":
        pcthink "Damn, she was really just trying to be nice and I've been a total ass..."
    else:
        pcthink "Damn, she was really just trying to be nice and I've been a total bitch..."
    m "[pc]?"
    pc "Yes?"
    m "Did you dislike me kissing you that much?"
    pc "Erm... No, that's not it... I just thought..."
    pc "I actually liked it."
    #scene bedroom rachelmast_emberrast with dissolve
    m "Really?"
    pc "Yeah..."
    #scene bedroom rachelmast4 with dissolve
    m "...so I could do it again?"
    pc "Sure..."
    scene bedroom rachelmast titties getup with dissolve
    pcthink "Wait, now? Like this?"
    scene bedroom rachelmast titties getupclose with dissolve
    pcthink "She must still be under the influence of the pills."
    scene bedroom rachelmast titties kiss1 with dissolve
    pcthink "Gawd, these lips... I want to..."
    scene bedroom rachelmast titties kiss2 with dissolve
    m "Mmm?"
    scene bedroom rachelmast titties kiss3 with dissolve
    pause
    pcthink "She isn't even trying to resist..."
    pause
    scene bedroom rachelmast titties kiss4 with dissolve
    m "Haa... [pc]."
    pc "Sorry, [m]. I couldn't help it."
    scene bedroom rachelmast titties kiss5 with dissolve
    m "Oh don't worry, Hun. You're a good kisser."
    pc "Haha, thanks. You too, [m]."
    pc "Well, I better leave now, so you can go on with what you were doing before I came in."
    pcthink "...before I do something stupid again..."
    m "Okay, Hun. I'll call you when dinner is ready."
    pc "Yeah, thanks [m]."
    pc "Oh and... think about me while you do what you do."
    m "Sure, I will, Hun."
    scene black with dissolve
    pcthink "Hehe, this was actually a nice idea. If she still thinks about me when the pills wear off, it could have a nice effect."
    $ storyEvent = False
    $ SErachelPills3rd = False
    jump hallPCtalktoEllie

label ebdRachelToBed:
    scene livingroom ebd all rtobed6 with dissolve
    m "Uhh... I'm shorry [pc]... *hic*"
    pc "Don't worry about it..."
    scene livingroom ebd all rtobed6_3 with dissolve
    m "I'm really the worsht... firsht deshtroying your child...*hic*...hood... and now [e]'s birthday..."
    pc "..."
    m "Pleeeeash forgive me, [pc]!"
    pc "Calm down [m], you'll feel better tomorrow..."
    scene livingroom ebd all rtobed7 with dissolve
    m "Ugh... yesh..."
    m "I'm... shorry... *hic*"
    m "I'll just shleep a bit and everyshing will be f-fine tomorrow..."
    scene livingroom ebd all rtobed8 with dissolve
    m "Can you give me the pillsh [pc]?"
    pc "I don't think it's a good idea to take them when you feel bad already..."
    scene livingroom ebd all rtobed9 with dissolve
    m "Ugh... don't worry... they will make me feel better *hic* ...ugh..."
    scene livingroom ebd all rtobed10 with dissolve
    pcthink "Shit, I should have a look at the instructions first..."
    pcthink "\"{b}CAUTION: Never{/b} take more than 1 pill per day. {b}Never{/b} use in combination with alcohol. Avoid human interactions for 1 to 2 hours if possible. Only take this medicine in a secure place (e.g. Home). Medicine can cause dizziness, nausea, temporary amnesia, temporary decreased cognitive ability...\""
    pcthink "Geez, that's heavy stuff..."
    scene livingroom ebd all rtobed9 with dissolve
    pc "Sorry [m], but I can't let you take them right now."
    m "Wh... why not? *hic*"
    pc "It's too dangerous."
    m "There ish nothing dangerous about the pillsh..."
    pc "There {b}is{/b} [m], and I think it's better if I keep them for now. You can have them back tomorrow."
    scene livingroom ebd all rtobed11 with dissolve
    m "Oh come oooonn... I really need one right now. *hic*"
    pc "No!"
    m "Whyyy? I neeeed one! Gimmme one!!!"
    pcthink "Damn it..."
    menu:
        "Tell her about the alcohol":
            pc "[m] you're drunk, there was alcohol in the fruit-punch..."
            pc "I won't let you take these pills in combination with alcohol."
            m "..."
            m "Ugh... I had a feeling... *hic*"
            m "..."
            m "Did you pour it in the punch bowl?"
            pc "No it wasn't me..."
            m "..."
            m "Shank you for telling me... *hic*"
        "Don't tell her":
            $ mob +=1
            pc "Not today [m]."
            m "Pleeeeash..." 
    scene livingroom ebd all rtobed12 with dissolve
    pc "Good night [m]..."
    m "Ugh..."
    scene black with dissolve
    jump ebd2
    
label bathroomRAfterEBD:
    play sound "audio/door-opening.ogg"
    scene bathroom rachel_afterebd1 with hpunch
    pc "Whoa shit!"
    m "Ugh..."
    scene bathroom rachel_afterebd2 with dissolve
    m "Huh?"
    scene bathroom rachel_afterebd1 with dissolve
    m "[pc]..."
    pc "God dammit, [m]! Why can't anybody in this house lock the door when they use the bathroom?!"
    scene bathroom rachel_afterebd2 with dissolve
    m "I-I'm sorry [pc]... I... I must have forgotten... I don't feel so well today..."
    scene bathroom rachel_afterebd1 with dissolve
    pcthink "Of course, she drank so much yesterday, she must have the worst hangover..."
    pc "Uh... [m]?"
    m "Yes..."
    pc "You know that you're naked?"
    m "Yes..."
    scene bathroom rachel_afterebd2 with dissolve
    m "Uhh...I mean..."
    scene bathroom rachel_afterebd3 with dissolve
    m "S-sorry [pc]..."
    m "Can you give me just a minute to finish and I'll make us some breakfast..."
    pc "Errr... yeah... sure..."
    pc "Do you want me to wake [e]?"
    m "Uhn... no... It's Sunday, let her sleep..."
    pc "Okay... I'll wait in the living room then."
    m "Okay, I'll hurry..."
    pcthink "Damn, [m] must be the hottest milf on the planet!"
    scene black with fade
    n "A bit later." with dissolve
    window hide
    pause 2
    scene livingroom morning aebd with dissolve
    pause 1
    pc "...not hungry?"
    scene livingroom morning aebd0 with dissolve
    m "I... no... I don't think it's going to stay inside..."
    scene livingroom morning aebd with dissolve
    pc "..."
    scene livingroom morning aebd4 with dissolve
    m "[pc]"
    pc "Yeah?"
    scene livingroom morning aebd3 with dissolve
    m "What happened yesterday?"
    pc "You don't remember?"
    scene livingroom morning aebd4 with dissolve
    m "..."
    m "I didn't do anything stupid, did I?"
    pc "Nothing I can think of..."
    pcthink "As if I know what she thinks is stupid..."
    pc "Aside from tripping over me."
    scene livingroom morning aebd3 with dissolve
    m "..."
    scene livingroom morning aebd2 with dissolve
    m "...I did?"
    scene livingroom morning aebd3 with dissolve
    pc "Yeah..."
    scene livingroom morning aebd4 with dissolve
    m "I hope you didn't get hurt?"
    pc "No I'm fine..."
    m "Good..."
    pc "..."
    pc "Erm... [m], isn't that the same dress you were wearing yesterday at the party?"
    scene livingroom morning aebd3 with dissolve
    m "Is it?"
    pc "Yeah..."
    scene livingroom morning aebd2 with dissolve
    m "Oh, yes, of course, I bought it for the party... I must have just grabbed it today in the morning without looking..."
    pc "Okay..."
    pcthink "I'd expect it to be quite hard to get into that dress, especially with a hangover..."
    scene livingroom morning aebd3 with dissolve
    m "So what are you going to do today? Any plans?"
    pc "Well I was thinking about checking my new workplace out, I've never been there and I don't want to be late tomorrow."
    m "Oh, right, tomorrow is your first day, isn't it?"
    pc "Yeah."
    m "Well it's a good idea then and very diligent of you."
    pc "I guess... what about you?"
    m "Oh I think I'm just going to do the household chores..."
    m "By the way, thank you for clearing the table yesterday."
    pc "Yeah, no prob..."
    pcthink "How did she know it was me if she doesn't remember anything?"
    scene black with fade
    "A few minutes and an awkward conversation later..."
    scene hall door pcroom with dissolve
    pcthink "Damn, that was awkward..."
    scene pcroom_enter_eafterebd with dissolve
    pcthink "I can't remember [m] ever being like that after she drank..."
    pc "..."
    scene pcroom_enter_eafterebd2 with dissolve
    pcthink "[e] is still sleeping..."
    pcthink "Hum... I didn't have the chance to give her the present yesterday..."
    pcthink "...maybe I could surprise her with it when she wakes up..."
    scene black with dissolve
    n "You grab the mobile phone from its hideout."
    pcthink "Okay, the battery is fully charged... now the card..."
    scene pcroom_enter_eafterebd3 with dissolve
    pcthink "Heh... that'll be a nice surprise when she wakes up..."
    pcthink "...at least I hope so..."
    pcthink "Hum... anyway, I don't want to wake her up, so I guess I'm going to check out the office..."
    scene black with fade
    $ SERachelBRAfterEBD = False
    $ SEAfterEBD = False
    $ SEWork = 1
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance
    
label rachelsaffair:
    scene backhome_rachel_phone with dissolve
    pcthink "Finally home.. gawd, I need to get out of these wet clothes..."
    m "{size=-10}No, that's something completely different...{/size}"
    scene backhome_rachel_phone1 with dissolve
    pcthink "Sounds like [m] is talking to someone on the phone..."
    scene backhome_rachel_phone_topcroom with dissolve
    pcthink "Anyway...I have to thank [oc] properly some day... he helped me out so many times, even though I hated him back then..."
    scene hall door pcroom with dissolve
    m "{size=-10}...yes, but when [pc]s Dad found out that I was involved with someone else... well, you know what happened.{/size}"
    pcthink "Huh?! Wait!"
    scene bedroom rachel phone1 with dissolve
    m "...I don't want to... I cant ever have this happen again..."
    pcthink "This means she really cheated on the old man?"
    m "..."
    m "...No... no I don't."
    m "..."
    m "...of course not. It was just that one time, but I already knew it was a bad decision. I just wanted to... feel something... anything at all."
    pcthink "Well I can't blame her for that. The old man didn't even try to show any affection towards her..."
    m "...no. He tried to avoid me after I got pregnant."
    pcthink "Yeah, the old man started to freak out more and more the year [m] got pregnant. I can still remember that..."
    m "Yes, the timing fits..."
    pcthink "...timing?"
    m "...no I don't think so..."
    pcthink "What timing?"
    m "Why would I tell him? In the end he was just another asshole."
    pcthink "What the hell? Does this mean she got pregnant from the other man?!"
    m "Yes, sure..."
    pcthink "This can't be true! Why would she..."
    m "Uhuh..."
    pcthink "Damn, of course she wouldn't tell anyone... the old man would have killed her if he knew..."
    m "Yes..."
    pcthink "Wait... does this mean..."
    m "I... I don't know..."
    pcthink "...[e] isn't my sister?"
    m "...I'm really unsure..."
    pcthink "I... can't believe it..."
    pcthink "Why didn't she tell me?"
    m "Yes, I do, but..."
    pcthink "She could have at least told me now that I'm back..."
    pcthink "All this talk about her having changed, and yet, she's still lying to me..."
    m "Yes [heshe] is, but it feels so wrong... I feel really bad about it and to be honest, I think [heshe] really cares a lot for [e]."
    pcthink "She feels bad about what?!"
    m "I don't know if I should do this anymore."
    pcthink "What the hell is she talking about?"
    m "I know, but still..."
    m "..."
    m "Oh no you don't!"
    m "..."
    m "Come on, please!? You can't do that!"
    m "..."
    m "...fine... I... I'll think about it, okay?"
    m "..."
    m "No, I'm sorry, but I think we shouldn't meet for now... I don't want [himher] to notice anything until... until I'm ready for it."
    m "..."
    m "Yes, thank you for understanding, precious."
    pcthink "Precious?!"
    m "Alright, I should hang up, [heshe] could be back soon."
    pcthink "Fuck, I really want to confront her right now... but maybe it's better if she doesn't know that I know about all that... yet."
    pcthink "I better pretend I've just gotten home..."
    m "Thank you... You too. Bye..."
    scene black with dissolve
    n "You open and close the front door and make sure to make enough noise so that [m] can hear it."
    scene backhome_rachel_phone with dissolve
    pcthink "Alright, that should do..."
    scene backhome_rachel_phone2 with dissolve
    m "Oh hey, welcome home, hun. How..."
    scene backhome_rachel_phone3 with dissolve
    m "Oh no, you're completely soaked!"
    pcthink "Yeah, play innocent, [m]..."
    pc "I ran into a shower... I'm going to change clothes now..."
    m "Yes, good, I don't want you to catch a cold. Do you want me to make you a tea or something?"
    scene hall door pcroom with dissolve
    pc "No thanks."
    play sound "audio/door-opening.ogg"
    scene black with dissolve
    play sound "audio/door-closing.ogg"
    scene pcroom with dissolve
    pcthink "Shit, I have to find out what she's up to..."
    pcthink "Ugh... but I should change first..."
    scene black with slowdissolve
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    m "Have you finished changing, Hun?"
    pc "Yeah, come in..."
    play sound "audio/door-opening.ogg"
    scene pcroom_rachel_affair1 with dissolve
    m "Is everything alright? Do you need something, Hun?"
    pc "No I'm fine..."
    m "Alright... well I'm going to make dinner now, is there something you’d like in particular?"
    pc "No..."
    scene pcroom_rachel_affair2 with dissolve
    m "Oh... okay..."
    pc "..."
    m "..."
    scene pcroom_rachel_affair1 with dissolve
    m "Well, could you tell [e] that dinner will be ready soon?"
    pc "Sure..."
    m "Okay... thanks, Hun..."
    play sound "audio/door-closing.ogg"
    scene pcroom_rachel_affair3 with dissolve
    pc "..."
    pcthink "Damn it! I almost started to trust her..."
    pcthink "Alright, [m], you won't fool me any longer, I'll be really cautious from now on!"
    pcthink "..."
    pcthink "Ugh... well, let's see what [e] is doing. At least I can trust her... hopefully..."
    
    jump eKitten
    
label rachelGivePills:
    "Later..."
    play sound "audio/knock-door1.ogg"
    "*Knock* *Knock*"
    m "It's me..."
    pc "Yeah, come in."
    scene pcroom_rachel_affair2 with dissolve
    m "Um... [pc]?"
    pc "Yeah, what's up?"
    scene pcroom_rachel_givepills1 with dissolve
    m "Um... did you... perhaps..."
    pc "..."
    m "Did you maybe... um..."
    pcthink "What's wrong with her?"
    menu:
        "Push her to talk.":
            pc "Come on, what's wrong, [m]? Just spit it out already."
            $ mob += 1
        "Wait.":
            pc "..."
    scene pcroom_rachel_affair2 with dissolve
    m "Uh... I'm sorry, did you... um... for whatever reason... take my pills?"
    pcthink "Ugh... shit, the pills... I totally forgot about them..."
    scene pcroom_rachel_givepills2 with dissolve
    m "I-I mean, I'm not saying that I suspect you did, but... I-I can't find them anywhere and... I promise, I won't be mad or anything... it's just..."
    pc "I have them."
    scene pcroom_rachel_givepills6 with dissolve
    m "Y-You do?!"
    pc "Yeah. Sorry, I forgot about it."
    scene pcroom_rachel_givepills5 with dissolve
    m "...can you... give them back then?"
    pcthink "Why doesn't she ask why I have them?"
    pcthink "Wouldn't she be curious, if she really doesn't remember?"
    pcthink "Damn, she's playing with me again..."
    m "I-I really need them, Hun."
    pcthink "Hum... that might even be true, but..."
    pc "Did you ever try a day without them?"
    scene pcroom_rachel_givepills6 with dissolve
    m "N-No... please... just give them back, okay, Hun?"
    pc "Why didn't you get a new bottle if you need them so urgently?"
    scene pcroom_rachel_givepills8 with dissolve
    m "I-I can't, they are still experimental I can't get them in a pharmacy, they are rationed to prevent overdoses as well."
    pc "What?! Why do you use experimental drugs?"
    m "Because I was asked by my doctor, and because they help." 
    pc "Jeez.. [m]... and what if you lose them?"
    m "I can make a request, but since they are experimental, they need to get manufactured first and then get shipped, so they need at least a week until they arrive."
    pcthink "Hum... maybe I could use this as an opportunity... I know she's hiding something from me and if she really has something planned, I'd at least have something up my sleeve..."
    pcthink "On the other hand, if I'm wrong... ugh..."
    menu:
        "Give her the bottle.":
            scene pcroomrachelgivepillsbottle with dissolve
            pc "Here, take it, but you really should try to stop using them."
            scene pcroom_rachel_givepillsall with dissolve
            m "Thanks, Hun. I'll try."
        "Give her one pill.":
            $ rpills = True
            pc "Well, that sounds like it might be better if I keep them, so you won't lose them again."
            scene pcroom_rachel_givepills3 with dissolve
            m "Lose? Um... I... I won't lose them again, don't worry, Hun!"
            pc "Better safe than sorry, don't you think?"
            scene pcroomrachelgivepillssingle with dissolve
            pc "Here, I'll give you one per day from now on."
            pcthink "Heh, no matter if she knows that I took them from her yesterday or not. If she wants to keep up her masquerade, she has no other choice than to accept."
            scene pcroom_rachel_givepillshave1_1 with dissolve
            pc "Don't worry, I'll keep track of them for you."
            scene pcroom_rachel_givepillshave1 with dissolve
            m "...okay... thank you, Hun..."
            pcthink "HA! I knew it!"
    m "Good night, Hun."
    pc "Yeah, good night, [m]..."
    scene black with fade
    jump homeday4night

label afterTcoerce2:
    if tc == 2 or tc == 3:
        scene pcroomaftercodingwork2 with dissolve
        pcthink "...who would have guessed, hehe."
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    scene pcroom_aftercodingwork with dissolve
    m "[pc]?"
    if tc == 2 or tc == 3:
        scene pcroomaftercodingwork2 with dissolve
    pcthink "Shit..."
    if tc == 2 or tc == 3:
        scene pcroom_aftercodingwork3_fem with dissolve
        pause .7
        scene pcroom_aftertcoerced2 with dissolve
    pc "Yeah?"
    scene pcroom_aftertcoerced2_rachel0 with dissolve
    m "What happened?"
    pc "Err, well she was asking stupid questions... I guess she didn't like my answers."
    scene pcroom_aftertcoerced2_rachel with dissolve
    m "[pc], you promised to be nicer to her!"
    pc "I tried, okay? I really tried, but then she started to be all bitchy again..."
    scene pcroom_aftertcoerced2_rachel2 with dissolve
    m "Hum, at least you tried... anyway, can we talk a bit?"
    pc "Sure, what about?"
    if rpills:
        scene pcroomaftertcoerced2rachelpills with dissolve
        pc "Oh, you want the pills, don't you?"
        scene pcroom_aftertcoerced2_rachel2 with dissolve
        m "No... I mean, yes, but that's not what I wanted to talk about..."
        pc "Okay...?"
    play sound "audio/door-closing.ogg"
    scene pcroom_aftertcoerced2_rachel3 with dissolve
    m "Why don't we sit down?"
    pc "Sure..."
    scene pcroom_atc2_rachel_sit4 with dissolve
    m "So..."
    scene pcroom_atc2_rachel_sit1 with dissolve
    m "How is work going?"
    scene pcroom_atc2_rachel_sit2 with dissolve
    pc "Okay, I guess..."
    scene pcroom_atc2_rachel_sit4 with dissolve
    m "Okay..."
    pc "..."
    scene pcroom_atc2_rachel_sit3 with dissolve
    m "Well, I wanted to talk about..."
    m "..."
    m "You and [e]..."
    pcthink "Oh right, the kiss, I totally forgot about that..."
    m "Um... I know you've always been close... and that's totally fine..."
    pcthink "Is she going to moralize me?"
    scene pcroom_atc2_rachel_sit4 with dissolve
    m "...but, I think that [e] might..."
    m "Well... [e] might think more of it..."
    pcthink "She isn't my sister, not even my stepsister, but [m] still acts like she is..."
    scene pcroom_atc2_rachel_sit3 with dissolve
    m "Maybe you didn't even realize it... and, I'm not mad or anything, but still... she's your sister..."
    stop music fadeout 2
    pc "Tch..."
    scene pcroom_atc2_rachel_sit4_2 with dissolve
    m "Huh?"
    pc "Are you fucking serious, [m]?"
    m "W-What...?!"
    pc "How long are you going to play this game? Do you think I don't know what's going on?"
    m "W-What do you mean? I-I'm not playing any games!"
    pc "Even {b}if{/b} she was my sister, she's old enough to know what she's doing."
    m "\"W-was\"?"
    pc "STOP playing dumb, [m]! I know all about your affair!"
    scene pcroom_atc2_rachel_sit5 with dissolve
    m "Y-You know?! But..."
    pc "I was really stupid to think that you might really have changed!"
    scene pcroom_atc2_rachel_sit6 with dissolve
    pc "But you're still lying to me!"
    m "..."
    pc "This won't happen again, you can't fool me anymore, [m]!"
    m "..."
    m "...I..."
    scene pcroom_atc2_rachel_run with dissolve
    m "I'm sorry..."
    play sound "audio/door-opening.ogg"
    scene pcroom_atc2_rachel_run2 with dissolve
    play sound "audio/door-closing.ogg"
    pause .5
    pc "..."
    pcthink "...and there's the second woman running out of my room today..."
    pcthink "I didn't expect her to burst into tears... I guess I lost my temper quite a bit..."
    pcthink "...or was it just another act from her?"
    pcthink "Anyway, the cat is out of the bag now..."
    pcthink "Maybe she will even start telling the truth from now on."
    pcthink "..."
    pcthink "Damn, I feel a bit bad for her... if she's just acting, then she's really good at it..."
    scene black with fade
    jump porn_vr_4
    
label d6_backhomeRachel:
    scene d6_backhome1 with dissolve
    pcthink "Ugh... great..."
    m "Was that [j] on a motorcycle?"
    pc "Yeah..."
    scene d6_backhome1_2 with dissolve
    m "I didn't know she had a license."
    pc "..."
    scene d6_backhome2 with dissolve
    m "Umm... [pc]?"
    pc "Yes..."
    m "I... can we talk?"
    pcthink "Ugh... shit, I don't really want to deal with her right now..."
    m "Please...?"
    pcthink "...I guess I should have expected her to want to talk after what happened yesterday..."
    m "Listen, I... I'm... I-I know I should have told you about the affair, but..."
    m "Can we please go inside and talk?"
    pcthink "Looks like she might even be honest this time..."
    pc "Fine..."
    m "Thank you..."
    scene black with dissolve
    stop music fadeout 2
    n "You follow her to her room. She closes the door behind you."
    scene bedroom_d6_backhome with dissolve
    play sound "audio/door-closing.ogg"
    pc "Humph... don't want [e] to hear about it?"
    scene bedroom_d6_backhome1 with dissolve
    m "[t] is here too, I don't want to disturb the therapy..."
    pc "Humph..."
    m "...and..."
    m "...yes, [e] also doesn't know about the affair, so..."
    pc "Tch, I don't believe it, you really are the worst..."
    m "But she..."
    scene bedroom_d6_backhome2 with dissolve
    m "... don't you think she had enough to deal with in her life?"
    m "Would it be any better if she knew about it?"
    pcthink "Shit, she has a point..."
    scene bedroom_d6_backhome1 with dissolve
    m "I'm really sorry I didn't tell you about it, but it's such a long time ago and you've just come back..."
    pc "You could have told me before I left..."
    m "I... I could've, yes... but we..."
    scene bedroom_d6_backhome2 with dissolve
    m "...we didn't really have the best relationship back then, did we?"
    pcthink "Another good point... but!"
    pc "But you did tell other people about it, didn't you?!"
    m "I..."
    m "...yes..."
    pc "Did... the old man know about it?"
    scene bedroom_d6_backhome1 with dissolve
    m "Hell no! He would have killed me!"
    pcthink "That might even be true... literally..."
    scene bedroom_d6_backhome2 with dissolve
    m "He... suspected something, but he never knew for sure..."
    m "He... tried to make me tell him the truth... several times... but I knew if I had told him..."
    pc "Yeah, I can even remember that..."
    scene bedroom_d6_backhome1 with dissolve
    m "You can?"
    pc "Yeah... my memory about that time is a bit foggy... I almost forgot about all this... but everything seems to be coming back bit by bit since I've been back..."
    scene bedroom_d6_backhome2 with dissolve
    m "I'm... so sorry..."
    scene bedroom_d6_backhome1 with dissolve
    m "Can I ask you a question?"
    pc "...yeah."
    m "Why did you say that [e] isn't your sister?"
    pcthink "Huh? What's that all about now? Didn't she just admit it?"
    scene bedroom_d6_backhome2 with dissolve
    m "I mean... I know you've been mad at me, and that you probably wanted to hurt me..."
    m "Or maybe it's because you've... developed some feelings for her, feelings one shouldn't have for [hisher] sister..."
    m "...but saying something like that isn't fair towards her..."
    pcthink "What the fuck?!"
    pc "What the hell, [m]? You just admitted that she isn't my sister yourself!"
    scene bedroom_d6_backhome1 with dissolve
    m "What? What are you talking about?"
    pc "You had an affair with another man! You got pregnant by that man!"
    m "What? No!!!"
    extend " No no no, Hun, that's not true! I didn't even sleep with him once!"
    pc "Bullshit! Do you think I'd believe that?"
    m "But it's true! I was way too scared about what would happen if your dad found out. I wanted to... but I never did."
    pc "That's..."
    pcthink "Fuck... am I supposed to believe this?"
    pcthink "This even makes sense considering the situation she was in..."
    scene bedroom_d6_backhome1 with dissolve
    m "Don't worry, Hun, she really is your sister... well, half sister, but still..."
    pcthink "Shit..."
    scene bedroom_d6_backhome2 with dissolve
    m "I'm sorry for the confusion, I really should have cleared things up with you way earlier..."
    pcthink "But she {b}did{/b} say that [e] is from the other man on the phone... didn't she?"
    
    scene bedroom rachel phone1memory with fade
    m "...no. He tried to avoid me after I got pregnant."
    m "Yes, the timing fits..."
    m "...no I don't think so..."
    m "Why would I tell him? In the end he was just another asshole."
    pcthink "Shit, this could actually mean that this guy just {b}thought{/b} he was the father, but he wasn't, and [m] never told him..."
    pcthink "But it could also mean that he {b}was{/b} the father, and she never told him... damn it!"
    scene bedroom_d6_backhome2 with dissolve
    m "I hope you can forgive me one more time..."
    pcthink "Why is everything so complicated when it comes to [m]?"
    m "I promise I'll be honest from now on and I will make it up to you..."
    pcthink "Why can't she just be the same bitch she was when I left?"
    scene bedroom_d6_backhome1 with dissolve
    m "Are you... okay, Hun?"
    pcthink "Damn it, I'll ask her again when she took the pills, and no distractions this time, no tits, no ass, no nothing, I need some answers!"
    m "Hun?"
    pc "Eh, yeah, I'm okay!"
    pc "I was just a bit surprised by our... misunderstanding... but it's good that you cleared things up."
    scene bedroom_d6_backhome3 with dissolve
    m "Yes it is... I think I feel better now, too."
    pc "Well, I still have a bit of work to do, so I better get started."
    m "Okay, thank you for listening to me."
    pc "Anytime..."
    if rpills:
        pc "Oh by the way, do you need your medicine, [m]?"
        m "Yes, please... I didn't take it yesterday..."
        pc "Alright, I'll get you a pill. I'll be right back."
        m "Thank you, Hun, that's really nice of you."
        pcthink "..."
    scene black with fade
    jump d6_backhome
    
label d6_rachel_pills:
    play music mainbgm fadein 1
    n "A while later."
    scene pcroom_rpills3_0 with dissolve
    pcthink "I guess that's enough for today..."
    pc "..."
    pcthink "Oh shit! I wanted to pump [m] for information!"
    pcthink "...hehe, pump [m]..."
    pcthink "Ugh, shit, I should focus on the questions!"
    pcthink "I better hurry, before it's too late..."
    scene black with fade
    scene bedroom_rpills3_0 with hpunch
    pc "[m] I... uff..."
    scene bedroom_rpills3_0_2 with dissolve
    m "Oh hey, Hun. Can I help you with anything?"
    pc "Damn, err... I mean, I... just wanted to make sure that you took your medicine..."
    m "Oh, of course, thank you for caring so much."
    if rpills:
        m "...and thank you for taking care of the pills, that's really nice of you, Hun."
    pc "What are you doing there by the way?"
    scene bedroom_rpills3_0_3 with dissolve
    m "I..."
    m "Hum... I don't remember..."
    pc "You don't remember?"
    scene bedroom_rpills3_0_2 with dissolve
    m "Umm... no, I'm sorry..."
    pc "Looks like you were searching for something."
    m "Searching?"
    pcthink "Alright, there's no doubt she took the pills..."
    scene bedroom_rpills3_0_3 with dissolve
    m "OH, right, yes. I was searching for the paternity test!"
    pc "Paternity test?"
    scene bedroom_rpills3_0_2 with dissolve
    m "I wanted to show it to you."
    pc "What paternity test?"
    m "Your dad demanded one after I got pregnant with [e]..."
    pcthink "A paternity test... of course he wanted that..."
    scene bedroom_rpills3_0 with dissolve
    m "...but I can't find it anywhere..."
    pc "Damn!"
    m "Did you say something?"
    pc "Err... no, nothing, haha."
    pcthink "Shit... I'd love to feel that ass..."
    pcthink "Wait a minute... she took the pills so..."
label d6_rachel_pills_r:
    if _in_replay:
        show screen endRep
    scene bedroom_rpills3_0 with dissolve
    pc "[m]?"
    m "Yes, Hun?"
    pc "*Cough* You have a great ass!"
    m "Why thank you, Hun! That's so nice of you to say."
    pcthink "Damn..."
    scene bedroom_rpills3_1 with dissolve
    pcthink "I could just grab her ass and she wouldn't even complain!"
    scene bedroom_rpills3_2 with dissolve
    pcthink "Shit, okay let's go for it..."
    scene bedroom_rpills3_3 with dissolve
    m "Wha?"
    m "What are you doing, Hun."
    pc "Just testing if it feels as good as it looks."
    m "O-Okay... does it?"
    pcthink "Damn..."
    pc "Oh yes, it does!"
    scene bedroom_rpills3_4 with dissolve
    pc "You don't mind, do you?"
    m "No of course not, Hun. I was just surprised."
    scene bedroom_rpills3_5 with dissolve
    m "Nnnhh..."
    pcthink "Gaawwwd, she's even moaning!"
    pc "Do you like that, [m]?"
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    m "Hnn... yes, it's been such a long time since somebody touched me there."
    pc "I guess..."
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    m "Haa..."
    pc "What about your \"precious\" from the phone call yesterday?"
    pcthink "I guess it doesn't matter if I mention her now, [m] will forget about it anyway as soon as the pills wear off."
    m "Oh, you heard that?"
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    pc "Yeah, I heard a few words..."
    m "Nnnhh... she hasn't touched me that way in a long time..."
    pc "She?"
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    m "Yes, haah..."
    pc "You're dating a woman? Really?"
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    m "Y-Yes... nnhh."
    m "N-No..."
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    pc "What now, [m]? Are you, or are you not dating a woman?"
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    m "It's... hnnn... not like that..."
    pc "Did you have sex with her, [m]?"
    scene bedroom_rpills3_5_2 with dissolve
    pause .2
    scene bedroom_rpills3_5 with dissolve
    m "Hhhnn... it's just that... we both were so lonely..."
    pcthink "She's avoiding answering directly..."
    pcthink "Wait, does that mean..."
    scene bedroom_rpills3_stop with vpunch
    pcthink "Fuck!!"
    m "Huh? Is something wrong, Hun?"
    pc "Err.. no, don't worry... When did you say you took the pills again?"
    m "Umm... about an hour ago, maybe a bit more... why do you ask?"
    pcthink "Fuck! The pills could wear off any time! I'm lucky they haven't, yet!"
    pc "Just curious... Anyway, I'll let you go back to your search now."
    scene bedroom_rpills3_stop3 with dissolve
    m "Oh, you don't want to go on, Hun?"
    pcthink "Shit, I'd love to..."
    pc "Sorry, but I have... things to do."
    m "Oh, okay..."
    $ renpy.end_replay()
    pcthink "Damn it, I wish I'd came earlier..."
    pcthink "That reminds me..."
    pc "Why don't you finish yourself off while thinking about me, [m]?"
    scene bedroom_rpills3_stop4 with dissolve
    m "Oh, that's a good idea, thank you, Hun."
    pcthink "Hehe..."
    pc "Anytime, later, [m]."
    m "Bye, Hun..."
    scene black with dissolve
    pcthink "Damn... now I'm horny as fuck... and I didn't even ask her everything... AGAIN!"
    scene backhome_rachel_phone_topcroom with dissolve
    pcthink "I really need to focus on the questions next time..."
    play sound "audio/door-closing.ogg"
    scene hall door pcroom with dissolve
    pcthink "Huh?"
    scene hall_d6_kat with dissolve
    pcthink "Hum..."
    if tc:
        pcthink "Well, maybe I can at least do something about my horniness..."
    scene hall_d6_kat2 with dissolve
    pcthink "She's blushing..."
    menu:
        "Grab her arm.":
            jump coerceT3
        "Let her be.":
            pcthink "Nah, better not..."
            jump d6_gotobed
                
                
label d8_rachel_talk:
    n "Back home."
    play sound "audio/door-opening.ogg"
    pause 2
    scene d8_backhome1 with dissolve
    m "Oh hey, Hun."
    pcthink "perfect timing..."
    scene d8_backhome2 with dissolve
    pc "Hey, [m]... can we talk for a bit?"
    scene d8_backhome3 with dissolve
    m "Sure, what about?"
    scene d8_backhome4 with dissolve
    if rpills:
        m "Oh, could you give me one of the pills prior to that? I forgot about it yesterday and have been feeling bad all day."
        pc "Yeah, sure..."
        scene black with dissolve
        scene d8_backhome5 with dissolve
        m "Thank you..."
        scene d8_backhome5_2 with dissolve
        pause 1
        scene d8_backhome6 with dissolve
        m "So what did you want to talk about?"
        scene d8_backhome7 with dissolve
    else:
        m "Oh will it take long? I just took one of the pills."
        scene d8_backhome4_2 with dissolve
        m "...and I still have to do the dishes..."
        pc "No, it shouldn't take that long."
        scene d8_backhome7 with dissolve
        m "Okay, so what did you want to talk about?"
    pc "Well... about [j]..."
    scene d8_backhome9 with dissolve
    m "Oh... right..."
    if jlo > 1 or jpushed:
        scene d8_backhome10 with dissolve
        m "I... I'm honestly a bit surprised..."
        scene d8_backhome10_2 with dissolve
        if pcgender == "woman":
            m "I didn't know that you're... I mean..."
            pc "...lesbian?"
            scene d8_backhome10_3 with dissolve
            m "Um... yes, I mean, you could have told me."
            scene d8_backhome10_2 with dissolve
            pc "Really now? I thought it was kinda obvious, [m]..."
            m "Well I... I didn't want to make assumptions..."
            scene d8_backhome10_3 with dissolve
            m "...but don't get me wrong, I'm absolutely fine with you being... uhm..."
            m "A lesbian..."
            scene d8_backhome11 with dissolve
            m "I'm sorry, Hun. I was just surprised... that's all."
            pc "..."
            m "Uhm... so, about [j], are you sure about... her?"
        scene d8_backhome11_2 with dissolve
        m "I mean, I have nothing against her, but she's..."
        scene d8_backhome11_3 with dissolve
        m "Well, I don't think she's the right person for you..."
        pc "[m], this is not about me and her."
        scene d8_backhome11_4 with dissolve
        m "It's not?"
        pc "No..."
        pc "Alright, the reason why she was sleeping here was that..."
    scene d8_backhome12 with dissolve
    pc "...she had an argument with her mom."
    scene d8_backhome12_2 with dissolve
    m "Oh..."
    scene d8_backhome13 with dissolve
    pc "Yeah, so she went back today to try and clear things up, but in the end it got worse..."
    pc "She got kicked out and now she has nowhere to stay..."
    scene d8_backhome14 with dissolve
    m "Oh no..."
    pc "Yeah, so I was thinking that we could let her stay here for a while..."
    scene d8_backhome15 with dissolve
    m "W-What?"
    pc "Well, at least until things settled down a bit, or until she found somewhere else to stay."
    scene d8_backhome16 with dissolve
    m "No... no, that's a bad idea, [pc]."
    scene d8_backhome16_2 with dissolve
    pc "Why is it a bad idea? It would be only for a few days..."
    scene d8_backhome17 with dissolve
    m "[pc], you know her, she means trouble. I'm fine with her coming over for a visit every now and then, but living here... no."
    pc "It would be just for a few days."
    m "No, [pc]!"
    pc "Seriously, what's the problem with having her here for a few days, it's not like she'd be living here forever..."
    scene d8_backhome17_2 with dissolve
    m "Humph, I said no, [pc], that's my final answer!"
    pc "But..."
    scene d8_backhome18 with dissolve
    m "...did you even talk to [e]? They might be friends, but maybe she doesn't want [j] to be here all the time! Maybe she doesn't want to..."
    m "...to..."
    scene d8_backhome19 with dissolve
    m "I-It's enough that you and [e] are sleeping together, I... I just can't stomach anymore!"
    pc "What?"
    scene d8_backhome20 with dissolve
    m "...the answer is no, [pc]."
    pcthink "Shit... I didn't expect that reaction..."
    pcthink "If I throw the \"it's my house\" card now, things might get out of hand..."
    pcthink "I better talk to her again when the pills set in..."
    pcthink "She's right though, I should've talked to [e] first. I doubt that she'd have anything against [j] living here, but better safe than sorry..."
    pcthink "Well, there's a bit of time until the pills set in, so..."
    scene black with fade
    jump d8_etalk

label d8_rachel_pills:
    pcthink "Alright, let's see how it works out."
    menu:
        "Knock.":
            play sound "audio/knock-door1.ogg"
            n "*Knock* *Knock*"
            pc "{cps=15}...{/cps}"
            pcthink "Hum... no reaction..."
            menu:
                "Knock again.":
                    "Just when you're about to knock again..."
                    m "Come in..."
        "Just go in.":
            pass
    play sound "audio/door-opening.ogg"
    scene d7_rpills with dissolve
    pcthink "Huh? She's just lying there..."
    m "..."
    pc "..."
    pc "[m]?"
    scene d7_rpills2 with dissolve
    m "Hm? Oh, [pc]..."
    scene d7_rpills2_2 with dissolve
    pc "What are you doing?"
    scene d7_rpills3 with dissolve
    m "I'm just laying..."
    scene d7_rpills4 with dissolve
    pc "I can see that, but why? What's the matter, [m]?"
    scene d7_rpills5 with dissolve
    m "Oh I... umm..."
    scene d7_rpills9 with dissolve
    m "I don't remember..."
    pcthink "Seriously?"
    scene d7_rpills7 with dissolve
    m "Do you need something, Hun?"
    pc "Yeah well... We need to talk about [j]."
    scene d7_rpills10 with dissolve
    m "Oh I'm sorry, Hun, I know you want her to stay here."
    pc "Yeah, do you remember when you invited me to stay here?"
    scene d7_rpills8 with dissolve
    m "Of course! And I'm really happy that you decided to stay!"
    pc "Yeah... I was searching for an apartment, but ended up in a filthy motel."
    m "Yes, I know."
    pc "There was not a single apartment available and the motel was the worst!"
    pc "So I had nowhere to go..."
    scene d7_rpills11 with dissolve
    m "Hmm..."
    scene d7_rpills10 with dissolve
    m "Is that why you accepted to move in again?"
    pc "Well, yeah, basically..."
    scene d7_rpills12 with dissolve
    m "Oh, it's okay. I didn't really expect you to accept the offer, but I'm glad you did."
    pc "Really? You didn't expect me to accept? Why did you offer it then?"
    scene d7_rpills13 with dissolve
    m "Oh I just had to... I want to make up for everything, and I just had to have you close!"
    pc "Have me close? What do you mean?"
    scene d7_rpills10 with dissolve
    m "Uhm... well, I want to be close to you, Hun."
    pc "Err..."
    scene d7_rpills10_2 with dissolve
    pcthink "Shit, is she flirting with me?"
    pcthink "Nah, that can't be what she meant..."
    pc "Anyway, what I'm trying to tell you is that I had no other choice, but to live here."
    pc "Otherwise I would've had to live under a bridge."
    scene d7_rpills13 with dissolve
    m "Oh, but you're always welcome here, Hun."
    pc "Yeah, but the same goes for [j] now. She might end up under a bridge if we don't help her..."
    scene d7_rpills7 with dissolve
    m "That would be bad, but I'm sure it won't happen."
    pc "Maybe, but what if?! Also, she's [e]'s best friend... her only friend as far as I can tell."
    pc "Would you really want such a fate for [e]'s BFF?"
    scene d7_rpills10 with dissolve
    m "Of course not, but [e] has you now..."
    scene d7_rpills13 with dissolve
    m "She's so happy since you're back! I haven't seen her smile so much in years!"
    pc "Really? But you don't want her to be close to me?"
    scene d7_rpills11 with dissolve
    m "Umm... well... that's something else..."
    pcthink "Uhh, this gives me another idea."
    pc "Wouldn't it be good for her to be as close to me as possible?"
    scene d7_rpills10 with dissolve
    m "Umm... I guess that makes sense... but still..."
    pc "Come on [m], don't you want the best for her?"
    m "Of course, but I'm not sure it really is the best for her..."
    m "I'll have to think about it..."
    pcthink "Humph, shit... well anyway..."
    pc "But don't you think that losing her best friend would be bad for her, even with me being here?" 
    scene d7_rpills9 with dissolve
    m "That's true I guess..."
    pc "And you being part of the reason wouldn't make it better right?"
    scene d7_rpills11 with dissolve
    m "Yes... but..."
    pc "And did you know that [j] really likes you? She looks up to you, you know."
    scene d7_rpills10 with dissolve
    m "Does she?"
    pc "Of course!"
    scene d7_rpills11 with dissolve
    m "I thought she was just a horny teen..."
    pc "She's an adult, [m]."
    scene d7_rpills10 with dissolve
    m "But she doesn't really show it..."
    pc "She does when she's with me..."
    pcthink "...sometimes..."
    pc "Maybe she's just nervous around you. I mean, everyone gets a bit nervous around someone [heshe]'s attracted to..."
    m "Do you think so?"
    pc "Yeah, of course."
    m "But aren't you together with her?"
    if jlo >= 2:
        pc "Yeah, but I don't mind."
        pcthink "You won't remember anyway, hehe."
    else:
        pc "Huh? No not really..."
    pc "Didn't you have something going on with the woman on the phone? How old is she?"
    scene d7_rpills14 with dissolve
    m "Huh? How did you know?"
    pc "You didn't answer my question, [m]."
    scene d7_rpills10 with dissolve
    m "Umm, well she is a bit older than me..."
    pc "So I guess it must be flattering to have a young woman like [j] being attracted to you as well..."
    scene d7_rpills11 with dissolve
    m "I... I guess..."
    scene d7_rpills10 with dissolve
    m "...yes, it is!"
    pc "Wouldn't it be nice to know there is someone home who really admires you?"
    scene d7_rpills11 with dissolve
    m "Yes..."
    pc "So why don't you let her live here, just for a while?"
    scene d7_rpills10 with dissolve
    m "Umm... maybe..."
    pc "Maybe?"
    m "...maybe you're right..."
    pcthink "YES!"
    pc "You won't regret it, I promise."
    m "But what if she makes trouble?"
    pc "Don't worry, I'll take care that won't happen."
    m "Okay... I trust you, Hun."
    pcthink "Damn, that went better than expected. Now I only have make sure she'll remember it somehow..."
    scene d7_rpills11 with dissolve
    m "To think someone that young would be interested in me..."
    pc "Is it really that surprising to you?"
    scene d7_rpills10 with dissolve
    m "Yes... I didn't think I'd be attractive to someone her age... or yours..."
    pc "Why though? You're an attractive woman, [m]."
    scene d7_rpills14 with dissolve
    m "Do you really think so? Am I not too old?"
    pc "You aren't old, [m], and yes, you are very attractive!"
    scene d7_rpills13 with dissolve
    m "Oh thank you, Hun! I wasn't sure about..."
    scene d7_rpills11 with dissolve
    m "..."
    scene d7_rpills10 with dissolve
    m "Can I ask you a question, Hun?"
    pc "Sure."
    scene d7_rpills11 with dissolve
    m "Umm... How do you think a person who has done wrongs in the past should approach a person she really likes, someone she really wants to be close to, but who she hurt in the past?"
    pc "Eh...?"
    pcthink "Is she talking about... me?"
    menu:
        pc "I think you should..."
        "Be honest and show your feelings.":
            $ mob -= 3
            scene d7_rpills8 with dissolve
        "Listen to [himher] and focus on what [heshe] wants!":
            $ mob += 3
            scene d7_rpills12 with dissolve
        "Don't approach [himher]!":
            $ mend = True
            scene d7_rpills10 with dissolve
    pause 1
    scene d7_rpills7 with dissolve
    m "That's good to know... thank you, Hun."
    pc "No prob..."
    pc "Err... back to topic... you will let [j] stay, right?"
    scene d7_rpills13 with dissolve
    m "Oh, yes of course, but you'll have to remind me later!"
    pc "Yeah, I will!"
    pcthink "Shit, I hope that isn't necessary..."
    pc "But you should really think about all the reasons I told you, why you want her to stay here."
    scene d7_rpills11 with dissolve
    m "Yes, you're right."
    pcthink "Damn, I really hope that helps her remember when the pills wear off..."
    scene d7_rpills10 with dissolve
    m "By the way, Hun, how did you know about the phone call?"
    pc "Oh err... well, I just overheard a bit of it when I came home that day. I didn't hear much though..."
    scene d7_rpills11 with dissolve
    m "Oh, okay..."
    pc "Who is she by the way?"
    scene d7_rpills7 with dissolve
    m "Oh you know her..."
    pc "What?!"
    play sound "audio/doorbell.ogg"
    n "*Doorbell rings*"
    pc "Shit... what do you mean I know her?"
    play sound "audio/doorbell.ogg"
    n "*Doorbell rings*"
    m "Well she is..."
    play sound "audio/doorbell.ogg"
    pause .5
    play audio "audio/doorbell.ogg"
    pause .5
    play sound "audio/doorbell.ogg"
    n "*Doorbell {cps=30}riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiings*{/cps}"
    scene d7_rpills15 with dissolve
    m "Shouldn't we open the door?"
    pc "Just tell me who..."
    play sound "audio/doorbell_cut.ogg" loop
    pause .5
    play audio "audio/doorbell.ogg"
    n "*{cps=30}Rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnngggggggggggggggggggggggg{/cps}*"
    n "{cps=30}*Ring* *Ring* *Riiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiing*{/cps}"
    scene d7_rpills16 with vpunch
    pc "Fuck! This is annoying!"
    scene black with dissolve
    n "{cps=30}*Riiiiiiiiiiiiiiiiiiiiiiing*{/cps}"
    pcthink "Gawd damn, who ever this is...!"
    stop sound
    play sound "audio/door-opening.ogg"
    scene d8_hall_j1 with dissolve
    pc "[j]!?"
    scene d8_hall_j2 with dissolve
    j "Hey!"
    pc "What the fuck are you doing here?"
    scene d8_hall_j3 with dissolve
    j "Yeah I'm happy to see you too..."
    pc "Ugh... shit, sorry... I was just... really busy you know..."
    scene d8_hall_j4 with dissolve
    j "Sorry... I didn't mean to distract you, but I couldn't bear waiting any longer, hehe."
    pc "Eh... yeah..."
    scene d8_hall_j5 with dissolve
    j "Can I come in? I'll be a nice girl, sit down somewhere and be quiet... promise."
    scene d8_hall_j6 with dissolve
    m "Oh hey [j]."
    scene d8_hall_j7 with dissolve
    j "Hi, [m]!"
    scene d8_hall_j8 with dissolve
    m "Funny that you're here. We've just talked about you and your living situation."
    j "Oh did you? Hehe."
    scene d8_hall_j9 with dissolve
    m "Yes, and we've decided that you can stay here for as long as you want!"
    j "Really?"
    pcthink "For as long as she wants?"
    j "That's awesome!!!"
    j "Thank you so much, [m]!"
    if jlo > 1:
        scene d8_hall_j9_2 with dissolve
        j "Thank you so much... {size=-10}[pcmd]{/size}!"
    scene d8_hall_j10 with dissolve
    m "You're welcome, [j], just make yourself at home."
    j "Thank you, I will! Hehe."
    scene d8_hall_j11 with dissolve
    j "{size=-10}She took the pills didn't she?{/size}"
    pc "{size=-10}You know about the pills?{/size}"
    scene d8_hall_j12 with dissolve
    j "{size=-10}I've seen her taking them and I've noticed her being a bit weird some times after that.{/size}"
    scene d8_hall_j13 with dissolve
    j "Oh hey, [e]. Guess who's your new room mate, hehe."
    scene d8_hall_j14 with dissolve
    e "HN!"
    
    jump d8_eveningWJada
    
label d9_backhome:
    scene d9_backhome with dissolve
    pcthink "Finally back home..."
    pcthink "It's late afternoon already..."
    scene d9_backhome2 with dissolve
    m "Oh hey, hun."
    pc "Hey, [m]."
    if mmom == "Mom":
        pc "Err... [mmom]..."
    scene d9_backhome3 with dissolve
    m "Why didn't you tell me that you're going to the city? We could've taken you with us."
    pc "It wasn't really planned, I got a call from the rental company and decided to head over there."
    scene d9_backhome4 with dissolve
    m "The... rental company?"
    pc "Yeah, I'll finally get my money back for the burned down apartment."
    scene d9_backhome5 with dissolve
    m "Oh, I see, that's good news!"
    pc "Yeah, one less thing to worry about."
    m "Good, good."
    scene d9_backhome6 with dissolve
    pc "..."
    if rpills:
        scene d9_backhome7_2 with dissolve
        m "Oh by the way, would you give me one of the pills?"
        pc "Yeah, sure..."
        scene d9backhome8 with dissolve
        m "Thanks."
    scene d9_backhome9 with dissolve
    m "Well, I'm... I'll be in my room for a while until it's time to make dinner..."
    play sound "audio/door-opening.ogg"
    scene d9_backhome10 with dissolve
    pc "Yeah, later, [m]."
    play sound "audio/door-closing.ogg"
    scene d9_backhome11 with dissolve
    pcthink "Well... that was weird..."
    pcthink "...did something change about her?"
    pcthink "Hum..."
    scene black with dissolve
    scene d9_pcroom_backhome0 with dissolve
    pcthink "Alright, what am I going to do for the rest of the day..."
    pcthink "I don't really want to do any work anymore today, so..."
    pcthink "Right, I should talk to [m], I need to know who the person was she was talking to on the phone..."
    pcthink "She said I know her, but who could it be?"
    scene d9pcroombackhome with dissolve
    pcthink "Well, I'll find out, but I have to wait until the pills start working..."
    scene d9_pcroom_backhome2 with dissolve
    pcthink "I guess I could have a look at what [e] and [j] are up to... but first I need to use the bathroom."
    scene black with dissolve
    play sound "audio/door-opening.ogg"
    jump d9_backhome_j
    
label d10shower:
    play sound "audio/shower.mp3" loop
    pcthink "I'm having a lot of these dreams lately..."
    scene d10shower01 with dissolve
    pcthink "Coming back here seems to trigger a lot of the old memories..."
    if pcgender == "woman":
        scene d10shower01_2 with dissolve
    pcthink "Not that I've forgotten anything..."
    pcthink "I'd just wish they'd stay buried in the back of my head, where they used to be over the last few years... I don't want to remember that shit..."
    scene d10shower02 with dissolve
    pcthink "Huh?"
    scene d10shower03 with dissolve
    pcthink "Shit, that's [m], isn't it? Damn, I forgot to lock the door again..."
    pcthink "Is she... I don't think she's noticed that I've seen her..."
    scene d10shower04 with dissolve
    pcthink "Wow, I think she was checking me out..."
    scene black with slowdissolve
    play sound "audio/shower_end.mp3"
    n "You finish up and head for breakfast."
    scene d10breakfast01 with dissolve
    pcthink "Hum, looks like breakfast for two?"
    pcthink "Ah, it's the weekend. [e] won't get up for a while... and I guess [j] likes to sleep in as well."
    m "Good morning, Hun."
    scene d10breakfast02 with dissolve
    m "Are you done in the bathroom?"
    pc "Morning, yeah..."
    scene d10breakfast03 with dissolve
    m "[e] and [j] will probably not get up soon, but I've made us some breakfast."
    if mob >= 5:
        m "I hope you don't mind, I thought you might be hungry."
    elif mob <= 0:
        m "I believe it's something you liked."
    scene d10breakfast04 with dissolve
    m "Why don't you sit down? I'll be there in a minute."
    pc "Sure, thanks."
    play music mainbgm fadein 1
    scene black with dissolve
    scene d10breakfast05 with dissolve
    pcthink "Isn't that..."
    scene d10breakfast06 with dissolve
    pcthink "Oh wow, french toast with syrup {b}and{/b} an omelette, that's two of my favorite foods!"
    pcthink "Is it coincidence, or did she really remember that I like this stuff?"
    pcthink "Well, whatever the case, it looks tasty and I haven't had any of it in a while!"
    scene black with dissolve
    n "You start eating until after a few minutes [m] comes back."
    scene d10breakfast07 with dissolve
    m "Do you like it?"
    pcthink "Holy! Damn..."
    pc "Yeah, it looks great."
    scene d10breakfast08 with dissolve
    m "Looks?"
    pc "Err... oh you mean the food!"
    scene d10breakfast09 with dissolve
    m "Yes, what did you think?"
    scene d10breakfast10 with dissolve
    pcthink "Damn, she looks really good this morning!"
    pc "Err..."
    if not mend:
        menu:
            "Tell her that she looks great.":
                if mob >= 5:
                    $ mob +=1
                else:
                    $ mob -=1
                pc "Well, to be honest, I was talking about you... you look great."
                scene d10breakfast11 with dissolve
                m "R-Really? But I'm not even wearing any makeup."
                pc "Yeah, I don't think you need any makeup at all, especially not in that outfit."
                scene d10breakfast12 with dissolve
                m "Oh, thank you! I was actually just going for a little workout after breakfast."
            "The weather! The weather looks to be great!":
                pc "I mean the weather, it looks to be a great day today."
                scene d10breakfast09 with dissolve
                m "Right? That's why I decided to do a little workout after breakfast."
        if mob >= 5:
            scene d10breakfast14 with dissolve
            m "You could... you could join me... if you want, maybe you'd enjoy it... I could even make some snacks if you like."
        else:
            scene d10breakfast13 with dissolve
            m "You should join me, I'm sure you'd enjoy a little workout."
        pc "Hmm... well, I guess it won't hurt."
        pcthink "Also, seeing more of her in that outfit..." 
        scene d10breakfast12_2 with dissolve
        m "Great! I'll get some snacks and an extra bottle of water for you after breakfast."
        scene black with slowdissolve
        n "You eat up and once [m] is ready, both of you head outside for a workout. After a bit of stretching, you start jogging."
    else:
        pc "The weather, it looks to be a great day today."
        scene d10breakfast12 with dissolve
        m "Right? That's why I decided to do a little workout after breakfast."
        pc "I see."
        scene black with fade
        n "The conversation slows down, so you eat up and go back to your room while [m] goes out to do her workout."
        jump d10pcroom
        


label d10outdoor:
    scene black with slowdissolve
    scene d10outdoor01 with dissolve
    pcthink "Phew... I'm really off form... unlike [m]..."
    scene d10outdoor02 with dissolve
    pcthink "No wonder she looks like that! Damn, I doubt that I can keep up with her much longer..."
    scene d10outdoor03 with dissolve
    m "Phew! How about a little break?"
    pc "Yeah."
    pcthink "Thank god!"
    scene d10outdoor04 with dissolve
    m "I must say I'm a bit surprised. I didn't think you'd keep up."
    scene d10outdoor05 with dissolve
    pc "Thanks."
    scene d10outdoor06 with dissolve
    pc "Well, I'm definitely not in {b}top{/b} form, that's for sure..."
    scene d10outdoor07 with dissolve
    pc "As opposed to you it seems."
    scene d10outdoor08 with dissolve
    m "Well, I used to do it every day for a while, but it's hard to stay motivated."
    m "I think the last time I went for a workout was two months ago, and even then it had been quite a while..."
    scene d10outdoor08_2 with dissolve
    menu:
        "You should keep doing workouts.":
            $ mob +=1
            pc "It'll help you stay fit and healthy."
            scene d10outdoor08 with dissolve
            m "Yes, you're right, I should really do it more often..."
            if mob >=5:
                scene d10outdoor09 with dissolve
                m "Would you..."
                scene d10outdoor10 with dissolve
                m "It would be nice to have somebody to help me stay motivated..."
            else:
                scene d10outdoor11 with dissolve
                m "You should join me once in a while, it'll help me to stay motivated and it's good for you, too."
            pc "Sure, I can help you with that."
            m "Thanks, Hun."
        "You don't need that workout you look great anyway!":
            $ mob -=1
            scene d10outdoor11 with dissolve
            m "Oh... thanks, Hun... but the same goes for you, you look really good."
            pc "Heh, thanks."
    scene d10outdoor12 with dissolve
    m "Oh, I hope you don't think I asked you to come with me because I think you need it."
    scene d10outdoor13 with dissolve
    pc "You didn't?"
    scene d10outdoor14 with dissolve
    m "N-No, of course not, you're perfectly fine!"
    scene d10outdoor15 with dissolve
    m "Actually, I think you've become a really attractive [pcgender]."
    scene d10outdoor16 with dissolve
    pc "..."
    pc "Do I still remind you of the old man?"
    pcthink "Damn, why did I have to remember that now..."
    scene d10outdoor17 with dissolve
    m "No, not in the slightest!"
    scene d10outdoor18 with dissolve
    m "You've never actually reminded me of him..."
    scene d10outdoor19 with dissolve
    pc "..."
    scene d10outdoor18 with dissolve
    m "...I..."
    m "...I'm sorry..."
    scene d10outdoor19 with dissolve
    pc "..."
    pcthink "Shit..."
    scene d10outdoor20 with dissolve
    pc "Shall we go on with the workout?"
    scene d10outdoor21 with dissolve
    m "Yes, thank you."
    scene black with slowdissolve
    n "You head on for a while in silence, but after a few minutes you run out of steam again."
    scene d10outdoor22 with slowdissolve
    n "You're not sure if [m] noticed you're out of breath, but as you come across an old pavilion she stops and quietly heads into it."
    scene d10outdoor23 with dissolve
    m "Let's take a short break and then head back, shall we?"
    scene d10outdoor24 with dissolve
    pc "Yeah... good idea..."
    scene d10outdoor25 with dissolve
    pc "Phew..."
    scene d10outdoor26 with dissolve
    m "Do you remember this place?"
    pc "Hm?"
    scene d10outdoor27 with dissolve
    pc "Now that you mention it... yeah I think I've been here before."
    scene d10outdoor26 with dissolve
    m "We've been here a few times when I was pregnant with [e]."
    scene d10outdoor27_2 with dissolve
    m "Until your dad came home early from work one day..."
    scene d10outdoor28 with dissolve
    m "He was furious at the fact that I wasn't home to make dinner."
    m "..."
    pc "I think I remember that part, too."
    scene d10outdoor27_2 with dissolve
    m "Your mom used to take care of everything in the house before she died, so he expected me to do the same..."
    m "...but whatever I did, it wasn't good enough..."
    scene d10outdoor29 with dissolve
    m "I don't have a problem with being a housewife you know..."
    scene d10outdoor30 with dissolve
    m "It's just..."
    scene d10outdoor31 with dissolve
    m "..."
    scene d10outdoor32 with dissolve
    m "It would just be nice to get something back every once in a while."
    scene d10outdoor33 with dissolve
    pcthink "Odd... did she switch from past to future tense on purpose?"
    m "..."
    scene d10outdoor34 with dissolve
    m "God I'm exhausted!"
    scene d10outdoor35 with dissolve
    m "The pavilion has seen better times as well..."
    scene d10outdoor36 with dissolve
    pc "..."
    if mob >= 5:
        scene d10outdoor37 with dissolve
        m "Do you mind if I lean on you for a while?"
        pc "I don't..."
        scene d10outdoor38 with dissolve
    if mob <5:
        scene d10outdoor35 with dissolve
        m "..."
        scene d10outdoor38 with dissolve
        pcthink "Whoa!"
        scene d10outdoor41 with dissolve
        m "You don't mind, do you? I just need to lean back for a short while."
        #scene d10outdoor38 with dissolve
        pc "No, it's fine..."
        scene d10outdoor38 with dissolve
    m "Thanks..."
    scene d10outdoor41 with dissolve
    m "...and thanks for listening, Hun..."
    scene d10outdoor40 with dissolve
    pc "Well..."
    pc "It's... kind of weird to hear your side of the story..."
    scene d10outdoor41 with dissolve
    m "My side?"
    pc "Yeah... well, I guess I've always just seen it from my perspective..."
    scene d10outdoor40 with dissolve
    pc "Much of the time before his death is... I don't know... foggy..."
    pc "I didn't understand much of what happened back then..."
    scene d10outdoor41 with dissolve
    m "Understandably, you were just a child."
    scene d10outdoor40 with dissolve
    pc "He always made it look like he didn't do anything bad, like it was never his fault."
    pc "\"[m] did something stupid again.\", \"[m] stumbled again.\", \"[m] is just weepy again.\""
    pcthink "Thinking about it... I think I knew somewhere deep in the back of my head, that he was lying, but..."
    pcthink "I guess I didn't want to accept it..."
    pc "As you said, I was just a child and he was my dad... why would he lie to me all the time..."
    scene d10outdoor38 with dissolve
    m "..."
    pc "Then, after that day... after his death... I started to realize how much you hated him... and me..."
    scene d10outdoor42 with dissolve
    m "Oh, I didn't!"
    scene d10outdoor43 with dissolve
    m "I didn't hate you... it's just..."
    m "I was so frustrated..."
    m "Yes, I hated him and he was gone... and you..."
    m "You were still there... his [ds]..."
    m "The [ds] of the woman he always compared me with, the [ds] of the man that caused me so much pain..."
    m "He made me feel like everything I did was wrong and stupid..."
    m "I was..."
    m "...I was just 18 when we came together and when he was gone I was... broken..."
    m "I wanted to get back at him... somehow... anyhow..."
    pc "...and then you started drinking..."
    scene d10outdoor45 with dissolve
    m "I'm so sorry, [pc]."
    scene d10outdoor43 with dissolve
    m "Being drunk is no excuse for being... the way I was towards you..."
    pc "..."
    m "I won't ask you to forgive me... but if you give me a chance..."
    scene d10outdoor46 with dissolve
    m "I'll do anything... Honey..."
    pcthink "...anything...?"
    if jlo >= 2:
        scene d10outdoor45 with dissolve
        m "...say..."
        scene d10outdoor43 with dissolve
        m "You and [j]..."
        m "...is it serious?"
        scene d10outdoor44 with dissolve
        pc "Me and [j]? ...well..."
        pc "I'm not sure to be honest."
        scene d10outdoor45 with dissolve
        m "She seems to be quite... open."
        scene d10outdoor44 with dissolve
        pc "Yeah, I'm sure she wouldn't mind being in my place right now."
        scene d10outdoor45 with dissolve
        m "You mean... with me?"
        scene d10outdoor43 with dissolve
        m "I... I'm not sure I could be that open..."
        if harem:
            pc "Well, she's still my girlfriend..."
            pcthink "I guess?"
            pc "...she wouldn't do anything I'm not okay with."
            pcthink "I hope..."
        else:
            pc "Nobody said you'd have to."
        m "I see..."
        pc "..."
        scene d10outdoor46 with dissolve
        m "[pc] I..."
    scene d10outdoor47 with dissolve
    pause
    scene d10outdoor48 with dissolve
    pcthink "Whoa!"
    scene d10outdoor49 with dissolve
    pause
    scene d10outdoor50 with dissolve
    pause
    pcthink "Well that was unexpected..."
    scene d10outdoor51 with dissolve
    m "*sniff* *Sniff*"
    scene d10outdoor52 with dissolve
    m "Phew, we'll need to take a shower when we're back home."
    pc "*Sniff* ...ugh... true."
    scene d10outdoor53 with dissolve
    if mob >=5:
        m "You can go first if you like."
    else:
        m "But I'll go first!"
    pc "Sure... we don't want to risk seeing each other naked under the shower, right?"
    scene d10outdoor54 with dissolve
    m "Was that sarcasm?"
    scene d10outdoor55 with dissolve
    pc "Well, we've seen each other naked already..."
    scene d10outdoor56 with dissolve
    m "H-Huh?"
    pc "I noticed you this morning."
    scene d10outdoor57 with dissolve
    m "Oh I'm sorry, I thought you didn't see me... I... I didn't want to disturb you."
    scene d10outdoor58 with dissolve
    menu:
        "Tell her to come in next time.":
            $ mob +=1
            pc "You should come in next time, we've seen each other naked already anyway."
            scene d10outdoor57 with dissolve
            if mob >= 5:
                m "O-Oh, are sure you don't mind?"
                pc "Yeah, it really doesn't bother me."
                m "O-okay... I'll try to remember..."
            else:
                m "Oh, well if you don't mind... I guess I could do that."
                m "I mean, since we have seen each other naked already..."
                pc "Yeah."
        "Ask her if she would mind you seeing her under the shower again.":
            pc "Would you mind me seeing you under the shower?"
            scene d10outdoor57 with dissolve
            m "Oh I... I mean... I guess I'd be okay with that..."
        "Tease her.":
            $ mob -=1
            pc "Peeping on people under the shower is not nice you know."
            scene d10outdoor59 with dissolve
            m "I-I didn't, I was just surprised, I didn't know what to do for a second!"
            pc "So surprised that you kept staring at my naked, wet body..."
            m "I-I... it wasn't..."
            pc "Maybe I should turn around next time so you can see more of me."
            scene d10outdoor60_2 with dissolve
            m "Oh stop making fun of me, [pc]!"
            scene d10outdoor60 with dissolve
            pc "Haha, just teasing."
    scene d10outdoor61 with dissolve
    m "Oh, by the way I think we should head back, [e] and [j] will probably wake up soon."
    scene d10outdoor62 with dissolve
    pc "Hm?"
    scene d10outdoor61 with dissolve
    pcthink "She changed the subject so suddenly..."
    scene d10outdoor44 with dissolve
    pc "Yeah, let's go then."
    scene black with fade
    n "You make your way back home at a slow pace, occasionally engaging in some small talk followed by awkward moments of silence."
    n "[m] seems to feel relieved when you arrive home, you can't help but feel the same..."
    play sound "audio/door-closing.ogg"
    scene d10ao01 with dissolve
    m "*Yaaaaawn*"
    scene d10ao02 with dissolve
    m "...I can't wait to get under the shower..."
    play sound "audio/door-opening.ogg"
    j "There you are!"
    scene d10ao03 with dissolve
    m "Oh good morning, [j]."
    pcthink "What the hell did she do in my room?"
    play sound "audio/door-closing.ogg"
    scene d10ao04 with dissolve
    j "Mornin', where have you been?"
    scene d10ao05 with dissolve
    m "We did a little morning workout."
    scene d10ao06 with dissolve
    j "Morning workout, huh? Hehe..."
    m "Ugh... [j]."
    scene d10ao07 with dissolve
    j "Come on, [pc], I need to show you something!"
    scene d10ao08 with dissolve
    pc "Huh? What's the matter?"
    scene d10ao09 with dissolve
    j "Just come, it's a surprise, you'll see!"
    scene d10ao10 with dissolve
    m "Well, I guess I'll be using the shower first, then."
    pc "Yeah, sure."
    scene d10ao11 with dissolve
    pc "Damn, [j], what are you up to?"
    j "You'll love it, promise!"
    scene black with slowdissolve
jump d10eshow

label d10shower2:
    if _in_replay:
        show screen endRep
    pcthink "Well, I guess I can at least take a shower now..."
    pcthink "I wonder if [m] is done already, maybe I should check."
    if not _in_replay:
        menu:
            "Check.":
                scene black with dissolve
                play sound "audio/shower.mp3" volume .4 loop fadein 1
                scene d10kataes07 with dissolve
                pcthink "Sounds like she's still under the shower..."
                menu:
                    "Go in.":
                        pcthink "Yeah, she's fine with it, right?"
                        if mob >= 5:
                            pcthink "And even if not..."
                        $ d10mshowervisit = True
                    "Don't. (Go back to your room)":
                        pcthink "Yeah, who wants to see a hot and naked milf..."
                        stop sound fadeout 1
                        jump d10pcroombeforekh
            "Go back to your room.":
                stop sound fadeout 1
                jump d10pcroombeforekh
    stop sound
    play sound "audio/shower.mp3" loop
    scene d10rshower01 with dissolve
    pcthink "Damn she's hot!"
    scene d10rshower02 with dissolve
    pcthink "Phew!"
    scene d10rshower03 with dissolve
    m "O-Oh...[pc]..."
    scene d10rshower04 with dissolve
    pcthink "Now we'll see if she's really okay with it..."
    scene d10rshower05 with dissolve
    m "..."
    scene d10rshower06 with dissolve
    pcthink "Wow... I guess she is..."
    scene d10rshower07 with dissolve
    pcthink "Well, time to join her."
    scene black with dissolve
    scene d10rshower08 with dissolve
    pc "..."
    scene d10rshower09 with dissolve
    pcthink "Looks like she's a bit unsure..."
    scene d10rshower09_2 with dissolve
    pause
    scene d10rshower10 with dissolve
    pause
    scene d10rshower11 with dissolve
    m "Are you... sure this is what you want, [pc]?"
    scene d10rshower12 with dissolve
    pc "I am..."
    scene d10rshower13 with dissolve
    m "Mhmm..."
    scene d10rshower14 with dissolve
    pause .5
    scene d10rshower14_2 with dissolve
    pause .5
    scene d10rshower14 with dissolve
    pause .5
    scene d10rshower15 with dissolve
    m "Hnnn..."
    scene d10rshower16 with dissolve
    m "[pc]..."
    if pcgender == "woman":
        scene d10rshower17 with dissolve
    else:
        scene d10rshower17_m with dissolve
    pause
    scene d10rshower18 with dissolve
    pause .5
    scene d10rshower19 with dissolve
    pause .5
    m "Nnnh..."
    scene d10rshower20 with dissolve
    m "N-No, [pc]..."
    scene d10rshower21 with dissolve
    pc "What's wrong?"
    scene d10rshower22 with dissolve
    m "I... the others could hear us."
    scene d10rshower23 with dissolve
    pc "We just have to be quiet."
    scene d10rshower24 with dissolve
    m "I-I... can't..."
    pc "Why, what's wrong, [m]?"
    scene d10rshower25 with dissolve
    m "That was [t] at the door, right?"
    pc "Yeah, why?"
    m "So we have two visitors, [t] and [j]..."
    scene d10rshower26 with dissolve
    m "I-I just don't feel comfortable... like that..."
    scene d10rshower25_2 with dissolve
    pc "[t] and [e] are busy with their session."
    scene d10rshower25 with dissolve
    m "Which means [j] has nothing to do... you know her..."
    scene d10rshower27 with dissolve
    m "We can still wash each other if you like."
    pc "Hmph... fine..."
    scene black with slowdissolve
    $ renpy.end_replay()
    n "Highly disappointed, you help [m] wash herself and she returns the favor, cautiously avoiding every sensitive spot."
    if pcgender == "man":
        n "She also completely ignores that you have a boner..."
    stop sound fadeout 2
    scene black with dissolve
    n "A little bit later." with slowdissolve
    jump d10pcroombeforekh
    
label d12rachel:
    n "An hour later."
    scene d12morning05 with dissolve
    pcthink "Phew, finally. What a toil..."
    pcthink "That thing is huge, it would've been a lot easier with a helping hand..."
    pcthink "But the image is great!"
    pcthink "I'm glad the old socket was still there behind the painting, it's in the perfect spot to hide the cable."
    if not mend:
        pcthink "I almost expected it to be..."
        play sound "audio/door-closing_muffled.ogg"
        pause .5
        scene d12morning06 with dissolve
        pcthink "Huh?"
        pcthink "That was the front door..."
        scene black with dissolve
        play sound "audio/door-opening.ogg"
        scene d12morning03 with dissolve
        pc "Hmm..."
        scene d12morning07 with dissolve
        pc "..."
        scene d12morning08 with dissolve
        pause
        scene d12morning03 with dissolve
        pc "Anybody here?"
        m "{size=-10}Oh, sorry, it's just me.{/size}"
        scene d11evhall04 with dissolve
        pc "[m]?"
        m "{size=-10}Yes, give me a minute...{/size}"
        pc "Alright..."
        scene black with dissolve
        pcthink "I guess she forgot something..."
        play sound "audio/door-closing.ogg"
        scene d12morning09 with dissolve
    else:
        scene d12morning14 with dissolve
    pcthink "Alright..."
    scene d12morning10 with dissolve
    pcthink "What do I do with the packaging..."
    pcthink "It's probably better to not throw it away, yet..."
    pcthink "Maybe there's room for it in the shed."
    if not mend:
        jump d12rachels
    else:
        play sound "audio/knock-door1.ogg"
        pc "Hm?"
        scene d12morning11 with dissolve
        pc "Come in."
        play sound "audio/door-opening.ogg"
        scene d12morning11_2 with dissolve
        m "Hey, Hun. Sorry, I..."
        scene d12morning11_3 with dissolve
        m "O-Oh, you got yourself a new TV?"
        scene d12morning11_4 with dissolve
        pc "Err... yeah, just finished setting it up."
        scene d12morning11_5 with dissolve
        m "Oh, well... anyway, I just forgot some papers for work, I have to leave again already."
        scene d12morning11_6 with dissolve
        pc "Yeah, I thought it must be something like that."
        scene d12morning11_7 with dissolve
        m "Alright, I need to hurry, see you later, Hun, and sorry for the trouble."
        pc "No problem, see you later."
        scene black with dissolve
        play sound "audio/door-closing.ogg"
        scene d12morning10 with dissolve
    
    jump d12shed
        
label d12rachels:
    if _in_replay:
        show screen endRep
    if mob >= 5:
        play sound "audio/knock-door1.ogg"
        pc "Hm?"
        scene d12morning11 with dissolve
        pc "Come in."
    play sound "audio/door-opening.ogg"
    if mob <= 5:
        pause .5
    scene d12morning12 with dissolve
    pcthink "Holy shit!"
    scene d12morning13 with dissolve
    m "O-Oh, you got yourself a new TV?"
    scene d12morning14 with dissolve
    play sound "audio/door-closing.ogg"
    pc "Err... yeah, just finished setting it up."
    scene d12morning15 with dissolve
    m "It's so big..."
    scene d12morning16 with dissolve
    pc "Err... what's with this outfit, and shouldn't you be at work?"
    scene d12morning17 with dissolve
    if mob >= 5:
        m "Oh, sorry, I... I thought I'd take a day off... I hope you don't mind... what do you think?"
    else:
        m "Oh, right... I took a day off... what do you think?"
    scene d12morning21 with dissolve
    pc "About the outfit?"
    scene d12morning21_2 with dissolve
    m "Yes."
    scene d12morning18 with dissolve
    pc "It's... incredibly hot."
    scene d12morning19 with dissolve
    m "Thank, you, I was hoping you'd like it."
    scene d12morning20 with dissolve
    m "To be honest, I wasn't even sure if it still fits."
    scene d12morning21 with dissolve
    pc "It fits perfectly."
    m "Thanks, Hun."
    scene d12morning22 with dissolve
    m "You know..."
    if d10mshowervisit:
        m "...I thought that, since we're alone now..."
        if mob >= 5:
            m "... maybe... maybe you wanted to go on where we stopped last time under the shower?"
        elif mob <= 0:
            m "...I think we should go on where we stopped last time under the shower."
        else:
            m "I... we could go on where we stopped last time under the shower."
    else:
        m "I was thinking, maybe we should spend some time together..."
        if mob >= 5:
            m "... we could... I mean, we can do whatever you want..."
        elif mob <= 0:
            m "...get to know each other a little bit... closer."
        else:
            m "I mean... just if you want."
    scene d12morning23 with dissolve
    pcthink "Shit, why do I get the feeling that this is all a bit sudden?"
    pc "Err... [mmom], don't get me wrong, but... what's going on all of a sudden, are you sure this is what you want?"
    scene d12morning24 with dissolve
    m "Huh? Y-Yes, of course, why do you ask?"
    pc "I don't know, it's just a bit unexpected."
    pc "I mean, I'm sure you know what's going on..."
    m "..."
    scene d12morning25 with dissolve
    m "Yes..."
    if harem:
        if jlo >= 3:
            m "I... I know I can't stop [j] from being the naughty girls she is..."
            m "...and I can understand that you like her."
        if tc:
            m "I honestly didn't expect [t] to... I thought she'd be a bit more professional..."
            if pcgender == "man":
                m "I don't blame her though, you're a handsome man."
            else:
                m "I don't blame her though, you're a beautiful woman."
        if jlo >= 3 and tc:
            m "I can't believe she's okay with you being with multiple girls though..."
        scene d12morning26 with dissolve
        m "[e]..."
        m "I honestly don't know what to think..."
        m "The only thing I know is that I..."
        scene d12morning27 with dissolve
        m "That I'm willing to try... whatever you have in mind..."
        scene d12morning28 with dissolve
        pc "Whatever I have in mind?"
        scene d12morning27 with dissolve
        m "Yes, I... I don't know how far I'm ready to go, yet... but..."
        if mob >=5:
            m "I'd do almost anything... for you... if you let me."
        else:
            m "I'll try..."
    else:
        if jlo >= 3:
            m "I... I know that [j] is your girlfriend..."
            m "...and I can understand that you like her."
        if tc:
            m "I honestly didn't expect [t] to... who would've thought she'd want to be your girlfriend."
        if jlo >= 3 and tc:
            m "You should probably talk to them and make a decision."
        scene d12morning26 with dissolve
        m "[e]..."
        m "I honestly don't know what to think... I'm not even entirely sure what's going on, but I try not to think about it..."
        m "What I did think about is that..."
        scene d12morning27 with dissolve
        m "I know I'm not the youngest anymore, I know we have a bad past, and that it's all my fault..."
        m "...but as long as there is a chance... I want to use it, and accept whatever you decide... for who you decide..."
    scene d12morning28 with dissolve
    pc "Are you really sure that's what you want?"
    scene d12morning27 with dissolve
    m "Yes, I'm ready to jump over the fence..."
    scene d12morning28 with dissolve
    pc "Well, that's... I don't know what to say, I honestly didn't expect that."
    m "..."
    scene d12morning29 with dissolve
    m "Oh, I... I guess I've destroyed the mood now... I'm sorry, Hun."
    menu:
        "Kiss her.":
            scene d12morning30 with dissolve
            pc "You didn't."
            scene d12morning31 with dissolve
            pause .5
            scene d12morning32 with dissolve
            pause
            scene d12morning32_2 with dissolve
            pause
            if mob <= 0:
                scene d12morning32_3 with dissolve
                m "Nhh..."
            scene black with dissolve
            scene d12morning35 with dissolve
            m "So, do you want to see what's under my outfit?"
            pc "I'd love to."
            scene black with dissolve
            play audio "audio/clothing-rustle-c2.ogg"
            pause 1
        "Rip her clothes off.":
            pc "Shit, come here, [mmom]!"
            scene d12morning33 with dissolve
            m "Whaa!?"
            scene d12morning33_2 with dissolve
            pause .5
            scene d12morning33_3 with dissolve
            m "I guess not."
            scene d12morning33_4 with dissolve
            pc "Not with this outfit... let's see what's under there."
            scene black with dissolve
            play audio "audio/clothing-rustle-c2.ogg"
            pause 1
    scene d12morning34 with dissolve
    pc "Damn, what a sight."
    if pcgender == "woman":
        pc "You have such a beautiful body, [mmom]!"
        m "Thank you, Hun, but so do you!"
    scene d12morning35 with dissolve
    if mob <= 0:
        m "Let's go to the bed, Hun."
    elif mob >= 5:
        m "Can we use the bed, Hun?"
    else:
        m "Shall we go over to the bed?"
    pc "Sure."
    scene black with slowdissolve
    m "What are you looking at?"
    scene d12morning36 with dissolve
    pc "I'm looking at an incredibly hot woman."
    scene d12morning37 with dissolve
    m "Oh, thanks, Hun."
    scene d12morning38 with dissolve
    pc "Alright, let's go on."
    if pcgender == "man":
        scene d12morning39 with dissolve
        pc "Mh-hm."
        scene d12morning40 with dissolve
        pause 1
        scene d12morning41 with dissolve
        pause 1
        scene d12mfm1_00 with dissolve
        pause 1
        $ pov1 = "d12mfm1"
        $ pov2 = "d12mfm2"
        $ povstart = True
        $ campov = False
        show screen povscreen(pov1)
        pause
    else:
        scene d12mff2 with dissolve
        pause 5
        scene black with dissolve
        scene d12mff3_179 with dissolve
    m "Haah... it's been so long..."
    pc "How about this then?"
    if pcgender == "man":
        hide screen povscreen with dissolve
        hide screen povbutton
        $ pov1 = "d12mfm3"
        $ pov2 = "d12mfm4"
        $ povstart = True
        show screen povscreen(pov1)
    scene d12mf with dissolve
    m "Hnn! Oh god, yes, Hun..."
    pause
    m "Nnnh, haaa..."
    pcthink "She's getting close!"
    m "Mmhh, hmmm..."
    scene d12morning42
    hide screen povscreen with hpunch
    hide screen povbutton
    m "Haaa... ahhh!"
    scene d12morning43 with dissolve
    m "Haaah... god... that felt so good... Hun..."
    pc "And we've just started."
    m "Haah... oh, I'm ready for more... don't let me stop you."
    if pcgender == "woman":
        scene d12morning44 with dissolve
        pc "Let's try this then..."
    scene black with dissolve
    scene d12mf2 with dissolve
    m "Ahh... haaa..."
    pcthink "Damn, what a view!"
    m "Oh god, yes!"
    pause
    if pcgender == "woman":
        $ pov1 = "d12mff6"
        $ pov2 = "d12mff7"
        $ povstart = True
        show screen povscreen(pov1)
    m "Hnn... nnhh..."
    if pcgender == "man":
        if mob >=5:
            m "Will... hnnn... will you come inside me?"
            pc "Do you want that?"
            m "Hnnn... I... don't know... haaa... I don't mind... haaa..."
            m "I-I'm on the pill anyway... hnnn..."
        else:
            m "Mhhh... you can... ahnn... come inside me, if you want...hnnn..."
            pc "Are you sure?"
            m "I'm on the pill anyway... haaah..."
        pc "Damn, I think even if I wanted to hold back, I wouldn't be able to..."
        pc "Hngh!"
        scene d12mfm5cum with hpunch
        pause 2
        m "Ahh... haah...{w=1}{nw}"
        scene d12morning46_m with slowdissolve
        pcthink "Shit, that felt good!"
        scene black with slowdissolve
    if pcgender == "woman":
        m "You're so... mmhh... beautiful... haa..."
        scene black
        hide screen povscreen with slowdissolve
        hide screen povbutton
        m "Mhaaa... haaa!" with hpunch
        m "Oh god, Hun..."
    pc "Ready for another round, [mmom]?"
    m "Of course, Hun!"
    scene d12morning47 with slowdissolve
    pause 2
    scene black with slowdissolve
    scene d12morning48 with dissolve
    pause 3
    scene black with slowdissolve
    n "Hours later..."
    scene d12morning50 with slowdissolve
    m "Hmmm... I really needed that..."
    scene d12morning51 with dissolve
    pc "Glad I was able to help out."
    scene d12morning52 with dissolve
    m "Oh, don't sell yourself short, Hun. I'm glad we finally did it."
    scene d12morning53 with dissolve
    pc "I just hope it wasn't a one time thing."
    scene d12morning51_3 with dissolve
    m "We can do it as much as you like, Hun."
    scene d12morning51_4 with dissolve
    if d10mshowervisit:
        pc "Well, you were very reluctant under the shower."
        scene d12morning51_3 with dissolve
        m "Oh... but that was only because we weren't alone at the time."
    else:
        pc "Well, you've never been like this before."
        scene d12morning51_3 with dissolve
        m "But that's because we were never alone."
        scene d12morning51_4 with dissolve
        pc "Well, we had some time alone before."
        scene d12morning51_5 with dissolve
        m "Yes, but... there has always been someone around the house..."
    scene d12morning51_4 with dissolve
    pc "There'll be someone around most of the time, but honestly, I don't care about that."
    scene d12morning51_5 with dissolve
    m "I..."
    scene d12morning51_3 with dissolve
    m "I'm sorry... I know I should be more open about it... It's just that... what if they hear us?"
    scene d12morning51_4 with dissolve
    pc "Who cares, they'll find out anyway."
    scene d12morning51_6 with dissolve
    m "..."
    scene d12morning51_3 with dissolve
    m "You're right... it won't work if I don't jump over my own fence. I'll do it!"
    scene d12morning51_4 with dissolve
    pc "Are you sure?"
    scene d12morning51_3 with dissolve
    m "Yes, I'll be more open from now on, a good relationship needs good sex. Otherwise it won't last long."
    scene d12morning51_4 with dissolve
    pc "That's true..."
    pc "So you won't mind if I come over to your bedroom later?"
    scene d12morning51_3 with dissolve
    m "Of course I don't mind... we'll just have to be more quiet."
    scene d12morning51_4 with dissolve
    pc "Heh, I don't mind if they hear us."
    scene d12morning51_3 with dissolve
    m "Oh, I bet you don't..."
    scene d12morning51_4 with dissolve
    if harem and jlo >=3:
        pc "And I bet [j] would enjoy hearing us."
        scene d12morning51_5 with dissolve
        m "Oh... that..."
        scene d12morning51_7 with dissolve
        m "Do you think she'd..."
        scene d12morning51_8 with dissolve
        pc "She'd probably want to join us."
        scene d12morning51_6 with dissolve
        m "..."
        scene d12morning51_5 with dissolve
        m "Do you..."
        scene d12morning51_6 with dissolve
        m "..."
        scene d12morning51_7 with dissolve
        m "I-I don't know if I can do that..."
        if pcgender == "man":
            scene d12morning51_8 with dissolve
            pc "You had sex with a woman before..."
            scene d12morning51_5 with dissolve
            m "Yes... yes, but..."
        if mob >=5:
            scene d12morning51_8 with dissolve
            pc "Didn't you say you'd do anything for me?"
            scene d12morning51_5 with dissolve
            m "Yes... yes... I..."
            scene d12morning51_3 with dissolve
            m "I promise, I'll try, but please give me a bit time, Hun."
            scene d12morning51_4 with dissolve
            pc "Sure, but don't take too much time."
            scene d12morning51_3 with dissolve
            m "I won't, I promise."
        else:
            scene d12morning51_3 with dissolve
            m "Maybe if I'm in the right mood..."
            scene d12morning51_4 with dissolve
            pc "We don't need to push it."
            scene d12morning51_3 with dissolve
            m "Thanks, Hun."
        scene d12morning51_5 with dissolve
        m "Maybe I should wait to take my meds before you come..."
        scene d12morning51_8 with dissolve
        pc "Eh, you'd forget we had sex the moment the effect wears off."
        scene d12morning51_7 with dissolve
        m "But I'd still feel it, and I'd probably be more open to... things, while the effect lasts."
        scene d12morning51_8 with dissolve
        pc "Yeah, but I want you to be more open in general."
        scene d12morning51_3 with dissolve
        m "Oh, I know, and I'll try..."
        scene d12morning51_4 with dissolve
        pc "That's all I want."
    else:
        pc "Haha."
    m "..."
    scene d12morning51_5 with dissolve
    m "I'm glad we can finally look behind the past..."
    m "...maybe even forget about it."
    scene d12morning51_6 with dissolve
    pc "..."
    play sound "audio/clothing-rustle-c3.ogg"
    scene d12morning54 with dissolve
    m "Oh, I should get ready. I need to pick up the girls."
    scene d12morning55_2 with dissolve
    pc "Yeah, right, it's probably time..."
    scene d12morning55 with dissolve
    m "Sorry, Hun. See you later."
    scene d12morning56 with dissolve
    m "*smooch*"
    scene d12morning57 with dissolve
    pc "Later, [mmom]."
    scene d12morning58 with dissolve
    pcthink "..."
    $ renpy.end_replay()
    play sound "audio/door-closing.ogg"
    scene d12morning59 with dissolve
    pcthink "...what a day..."
    scene black with dissolve
    scene d12morning60 with dissolve
    
    jump d12shed