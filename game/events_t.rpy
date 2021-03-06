######## Therapist 
label tIntroductionDay1:
    n "Hours later" with dissolve
    window hide
    pause 2
    play sound "audio/running-water.ogg" loop
    scene bathroompcwashhands with dissolve
    pcthink "...alright, back to the livingroom. At least [m] and [e] are back now, so it shouldn't be that boring anymore..."
    play sound "audio/running-water_end.ogg"
    scene bathroompcleave with dissolve
    stop music fadeout 2
    "Voice" "{size=-10}Good afternoon [e]. How are you today? Did you do everything I told you?{/size}"
    scene hall tfirst with dissolve
    pcthink "Huh? Who's this?"
    scene childroom tintroductionfirst with dissolve
    pc "Hey [e], and..."
    scene childroom tintroduction3rd with dissolve
    "Woman" "You must be [pc], I guess?"
    pc "Uh, yes and you are?"
    scene childroom tintroduction2nd with dissolve
    "Woman" "Oh? No one told you about me?"
    pc "No..."
    scene childroom tintroduction5 with dissolve
    "Woman" "I'm [e]'s therapist."
    scene childroom tintroduction9 with dissolve
    pcthink "Okay, no introduction then..."
    pc "She has her own therapist?"
    scene childroom tintroduction2nd with dissolve
    t1 "Of course."
    pc "..."
    pc "I see... I didn't know."
    t1 "Obviously."
    scene childroom tintroduction7 with dissolve
    pcthink "Why does she have such a hostile attitude?"
    pc "Yeah... uh, aren't you a bit young to be a therapist?"
    scene childroom tintroduction5 with dissolve
    t1 "I don't see what my age has to do with my work."
    scene childroom tintroduction9 with dissolve
    pc "...yeah. I guess age doesn't matter when you're good at your job..."
    scene childroom tintroduction5 with dissolve
    t1 "Of course, and I am!"
    pcthink "Wow, what a smug..."
    scene childroom tintroduction2nd with dissolve
    t1 "So, [m] told me that [e] is quite... fond of you?"
    scene childroom tintroduction6 with dissolve
    pc "Did she? Well I'm her [bs] after all."
    scene childroom tintroduction3rd with dissolve
    t1 "Hm, I see."
    scene childroom tintroduction4 with dissolve
    t1 "Well, I'd prefer it if you leave us alone until I'm finished with my work."
    scene childroom tintroduction8 with dissolve
    pcthink "Work? Is [e] nothing but work to her?"
    pc "Sure..."
    scene hall door with vpunch
    "She closes the door right in your face"
    pcthink "What the... what a bitch!"
    pcthink "Why did [m] hire someone like her to take care of [e]?!"
    pcthink "[e] didn't seem to be overly excited either... she almost looked like she wanted me to help her."
    scene hall_back_idle with dissolve
    pcthink "I have to talk to [m] about this."
    $ storyEvent = True
    $ SErachelPills2nd = True
    call screen map_hall_back
    jump endGame

label tLeavingDay1:
    n "As you are about to enter your room you hear [e]'s door open."
    scene hall door pcroom with dissolve
    t "{size=-10}...and don't forget to finish your tasks this time. I really don't feel like going through this every time I'm here!{/size}"
    scene hall tleave1 with dissolve
    t "..."
    scene hall tleave2_1 with dissolve
    pc "Done already?"
    scene hall tleave2 with dissolve
    t "Humph... It took way too long. Longer than usual."
    scene hall tleave2_1 with dissolve
    pc "Well... maybe it would have helped if you were a bit more... friendly!"
    pc "...just saying."
    scene hall tleave2_2 with dissolve
    t "Tch, it would have helped if you hadn't disturbed us at the beginning!"
    pc "What?! How the hell did I disturb you?! You barely entered her room!?"
    scene hall tleave2 with dissolve
    t "You did disturb {b}her{/b}, not me! You don't know much about people, do you?!"
    scene hall tleave2_1 with dissolve
    pc "{b}I{/b} don't know much about people?! You were the one who was unfriendly to start with, and by the way, you didn't even introduce yourself."
    pc "If that's the way you work then I know why [e] doesn't like you."
    scene hall tleave3 with dissolve
    t "I don't have time for this stupidity, you don't know anything about my work..."
    scene hall tleave toentrance with dissolve
    t "Just to make this clear, I'd prefer it if you'd not be here the next time I'm working with [e]!"
    pc "Yeah, go and I would prefer it if you'd never come back!"
    pcthink "Shit, maybe that was a bit too much. I hope [m] didn't hear that..."
    e "Hehehe."
    scene hall tleave elaugh with dissolve
    pc "Huh, [e]?"
    scene hall tleave elaugh2 with dissolve
    pause .5
    scene hall tleave egone with dissolve
    pc "Did she listen the whole time?"
    scene black with dissolve
    jump eOnLap
    
label talkTone:
    scene hall t enter1 with dissolve
    pause
    scene hall t enter1_2 with dissolve
    t "Oh..."
    pc "I'm happy to see you as well..."
    t "Pff, I didn't expect {i}you{/i} to open the door..."
    scene hall t enter1_3 with dissolve
    t "Anyway, I have work to do!"
    pcthink "What the fuck, is she serious?"
    scene hall t enter1_4 with dissolve
    pc "[e] is not home yet, same for [m]!"
    scene hall t enter1_5 with dissolve
    t "Not home? Why?"
    pc "I don't know, [m] just told me on the phone."
    t "Why didn't she call me?"
    pc "I guess she didn't see a need for it..."
    t "Tch... well I guess there won't be a session today then."
    pc "They will be here in a few minutes."
    t "Humph... fine, I'll wait then..."
    pcthink "Damn, she's so annoying..."
    t "I hope you know that time is money!"
    pcthink "What now, does she think I'm going to pay her?"
    pc "I'm not the one who's paying you..."
    t "Humph..."
    scene black with dissolve
    n "She goes to the living room and sits down at the dining table. You try your best to ignore her while she does the same."
    scene livingroom ttv2 with dissolve
    pc "..."
    extend "."
    extend "."
    extend "."
    scene livingroom ttv tsit2 with dissolve
    t "..."
    scene livingroom ttv2 with dissolve
    pc "..."
    scene livingroom ttv tsit1 with dissolve
    pause .5
    scene livingroom ttv tsit2 with dissolve
    pause
    scene livingroom ttv2 with dissolve
    pc "..."
    extend "."
    extend "."
    scene livingroom ttv tsit1 with dissolve
    pause .5
    scene livingroom ttv tsit3 with dissolve
    pcthink "What's up with her?"
    scene livingroom ttv2 with dissolve
    pc "..."
    t "..."
    scene livingroom ttv tsit lookwrite with dissolve
    pause
    scene livingroom ttv tsit write with dissolve
    pcthink "What the hell?"
    pc "Are you writing something about me?"
    t "..."
    pc "Hey, I'm talking to you!"
    t "...of course."
    pc "Of course?! What the hell?!"
    t "...I need to include all factors in [e]'s life for her therapy."
    pc "Factors? I'm not a fucking factor!"
    t "..."
    pc "Hey!"
    t "..."
    scene livingroom ttv2 with dissolve
    pcthink "Fuck this bitch. What the fuck is wrong with her?"
    pc "..."
    t "..."
    pc "You definitely have the wrong job..."
    t "...and why would you think so?"
    scene livingroom ttv tsit lookwrite with dissolve
    pc "As far as I know, a therapist should listen to people, but that's definitely not your best trait."
    t "..."
    scene livingroom ttv tsit write with dissolve
    t "Well, you're not my patient, so there is no reason to listen to your claptrap..."
    pc "You..."
    m "We are back!"
    scene livingroom ttv tsit mandeenter with dissolve
    pcthink "Damn, your luck [t]..."
    scene livingroom ttv tsit mandeenter2 with dissolve
    m "Hello [t], I'm sorry we're late. I hope you didn't wait long?"
    t "It's okay, but I have to charge for it."
    scene livingroom ttv tsit mandeenter4_2 with dissolve
    pc "What?! Are you serious? It was barely ten minutes if at all!"
    scene livingroom ttv tsit mandeenter4 with dissolve
    t "Time is money..."
    m "[pc], it's okay. It was my fault, so I'll happily pay for it."
    pc "Humph... well it's your money..."
    scene black with dissolve
    play music mainbgm fadein 1
    n "[e] comes closer and sits next to you on the couch. She tucks under your arm and rests her head on your shoulder."
    scene livingroom ttv tsit mandeenter5 with dissolve
    t "Well we should get started. Come on over [e]."
    scene livingroom ttv tsit mandeenter6 with dissolve
    n "[e] shrugs and draws herself closer to you."
    m "Oh [e], come on, you know [t] is a busy woman. You can cuddle with your [bs] later."
    n "She draws herself even closer."
    scene livingroom ttv tsit mandeenter7 with dissolve
    pause
    pc "What's wrong [e], don't tell me you don't like your therapist!"
    scene livingroom ttv tsit mandeenter8 with dissolve
    n "You look at [t] with a smile on your face while saying this."
    t "Tch..."
    m "[pc]..."
    scene livingroom ttv tsit mandeenter8_2 with dissolve
    pc "Anyway, we don't want [m] to pay more than necessary, do we, [e]?"
    n "You give her a wink."
    n "She smiles and gets up."
    scene livingroom ttv tsit mandeenter9 with dissolve
    pause .5
    n "[e] goes to her room, followed by [t] who turns back to you for a moment with an annoyed expression."
    scene black with dissolve
    pause .5
    scene livingroom ttv tsit m with dissolve
    m "Thank you, Hun."
    scene livingroom ttv tsit m2 with dissolve
    m "And I'm sorry, I should have told you about the session today."
    pc "Yeah, you should have. I hope you told [e] at least."
    scene livingroom ttv tsit m3 with dissolve
    m "Oh, [e] knows about her sessions with [t]. Better than me actually."
    pc "..."
    m "Could you do me a favor [pc]?"
    pc "What favor?"
    m "I... I know you don't like [t], but could you try to be a bit more friendly towards her?"
    pc "What? Why would I? She's been a bitch towards me from the first time we met!"
    m "Please, [pc]. She is all we have to help [e]..."
    pc "..."
    m "I told you she's the only one still willing to help her, so please? For [e]."
    pc "Humph... fine, I'll try, but I won't promise anything..."
    scene livingroom ttv tsit m3_1 with dissolve
    m "That's okay..."
    scene livingroom ttv tsit m3_2 with dissolve
    pcthink "Did she just look at my...?"
    m "Thanks, Hun. I really appreciate it."
    scene livingroom ttv tsit mkiss with dissolve
    pause
    scene livingroom ttv tsit m3_2 with dissolve
    pc "Uh... yeah, anytime..."
    scene livingroom ttv tsit m4 with dissolve
    m "Well, I don't want to disturb you any longer, so I'm going to prepare the cake for later."
    pc "...sure..."
    scene livingroom ttv_look with dissolve
    pcthink "What was that?"
    pcthink "She looked right into my eyes, almost as if she was expecting me to kiss her back like yesterday..."
    pcthink "Does she remember it?! Gawd, that would be awful!"
    pcthink "..."
    pcthink "...no I don't think so... she would have acted differently if that'd be the case..."
    pcthink "Maybe what happens when she takes the pills can still affect her, even if she doesn't remember it?"
    pcthink "...maybe it's affecting her subconsciously..."
    pcthink "Hum... I should have a look at the pills' description next time..."
    
    jump JVREbirthday
    
    
label coerceT1:
    if _in_replay:
        show screen endRep
    scene bathroomebdt2 with dissolve
    pc "Alright, that's enough!"
    t "Wha?!"
    scene bathroomebdtmolest1 with dissolve
    pc "I've had enough of your bitchy attitude now."
    scene bathroomebdtmolest3 with dissolve
    t "Tch! And what do you intend to do about it?"
    t "Are you going to punch me like your dad did with [m]?"
    pc "What?!"
    pc "What the fuck is wrong with you?!"
    pc "I'm not going to punch anyone, not even you!"
    pc "Why the hell would you think I would do that?"
    t "I don't know, tell me?!"
    pc "What the hell have I ever done to you, huh?!"
    t "Humph... more than enough..."
    scene bathroomebdtmolest2 with dissolve
    pcthink "Why is she... blushing?"
    pc "You were the one who was acting like a bitch from the first day we met!"
    t "..."
    pcthink "Don't tell me she's intimidated..."
    pc "I'm talking to you!"
    scene bathroomebdtmolest3 with dissolve
    t "I don't care!"
    scene bathroomebdtmolest2 with dissolve
    pcthink "No, she's definitely not intimidated... she's embarrassed!"
    pcthink "This smell..."
    scene bathroomebdtmolest3 with dissolve
    t "Stop staring at me and let me go!"
    pc "Are you going to stop being such a bitch to everybody then?"
    scene bathroomebdtmolest2 with dissolve
    pc "What the hell makes you even think I'd be like that piece of shit?!"
    t "Uhn..."
    n "You notice her twitching slightly for less than a second."
    pcthink "What's wrong with her?! I would have expected her to freak out and yell at me..."
    pcthink "...but it feels more like she's kind of embarrassed, almost... excited."
    t "..."
    pcthink "Damn, I know that smell..."
    pc "..."
    scene bathroomebdtmolestliftskirt0 with dissolve
    pcthink "...and I know exactly where it comes from..."
    pcthink "Could this really turn her on?"
    menu:
        "Touch between her legs.":
            pass
        "Don't.":
            $ tc = False
            scene bathroom ebd tmolest4_2 with dissolve
            t "...Fuck you! Let me go!"
            pc "I'm not even holding you anymore, but you're still here and blushing like a tomato..."
            t "A-Asshole!"
            scene black with dissolve
            n "She storms off."
            pc "..."
            pc "*Exhale*"
            scene bathroompcleave with dissolve
            pcthink "Phew... somehow I get the feeling that she expected me to do something to her..."
            pcthink "...haha, she looked cute blushing like that..."
            scene hall_back_idle with dissolve
            pcthink "Hum... well let's hope she didn't tell anyone..."
            jump ebd
    scene bathroomebdtmolestliftskirt with dissolve
    t "W-what are you doing? Don't touch me you pervert!"
    scene bathroomebdtmolesttouch with dissolve
    pcthink "Damn, she is extremely wet..."
    pc "Oh, but it feels like it's exactly what you want?"
    scene bathroom ebd tmolest4 with dissolve
    t "Uh... you.... No!"
    t "S-stop that!"
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .5
    scene bathroom ebd tmolest4_3 with dissolve
    t "Ahhnn..."
    pc "You say that, but do you mean it? You're completely wet down there."
    scene bathroom ebd tmolest4_2 with dissolve
    t "That's not true!"
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .5
    scene bathroom ebd tmolest4_3 with dissolve
    t "Hah.."
    pc "No? Don't tell me you've wet yourself."
    scene bathroom ebd tmolest4_2 with dissolve
    t "What?! N-no!! I'm.. haaah."
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .5
    pc "So you ARE wet!"
    scene bathroom ebd tmolest4_1 with dissolve
    t "Nnnh *gasp* ... I'm not...hnn... let me go!"
    pc "I'm not holding you."
    scene bathroom ebd tmolest4_3 with dissolve
    if pcgender == "man":
        t "Nghh... ahh asshole!"
    else:
        t "Nghh... ahh bitch!"
    t "Stop it! Haaanngh"
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .5
    scene bathroom ebd tmolest4_4 with dissolve
    t "Haa... aahnn... oh god, stop, please... aaahh!!"
    pc "Really? You want me to stop?"
    scene bathroom ebd tmolest4_3 with dissolve
    t "Ahnngh, y-yes, p-please, haaa..."
    pc "So you have some manners after all."
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroom ebd tmolest4_4 with dissolve
    t "Haaah..."
    scene bathroom ebd tmolest5 with dissolve
    pc "What's wrong? Are you going to cum?"
    t "Gnnhhh... n-no... ha...ha... aahnn..."
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestrub with dissolve
    pause .2
    scene bathroomebdtmolesttouch with dissolve
    pause .2
    scene bathroomebdtmolestsqueeze with dissolve
    t "NNnnnnnh"
    scene bathroom ebd tmolest4_cum with dissolve
    t "AAHhhhh..."
    scene bathroomebdtmolestsqueezecum with dissolve
    pause 1
    pc "Wow, you squirted all over the floor..."
    scene bathroom ebd tmolest4_4 with dissolve
    t "Haaa...haaa.... *gasp*"
    if pcgender == "man":
        t "You pig! Hahhh... H-how could you..."
    else:
        t "You dyke! Hahhh... H-how could you..."
    pc "Looks like you needed it quite urgently."
    scene bathroom ebd tmolest4_2 with dissolve
    t "...Fuck you!"
    scene black with dissolve
    n "She storms off."
    pc "..."
    pc "*Exhale*"
    pcthink "Phew... holy shit... I can't believe what I just did..."
    scene bathroompcleave with dissolve
    pcthink "...and she didn't even try to stop me..."
    scene hall_back_idle with dissolve
    pcthink "Shit, I hope she doesn't tell anyone..."
    $ renpy.end_replay()
    jump ebd
    
label tcoerce2:
    scene black with dissolve
    stop music fadeout 1
    n "You're about to get up, when suddenly..."
    play sound "audio/door-closing.ogg"
    scene pcroomcodingwork with hpunch
    n "*Slam*"
    pcthink "What the..."
    scene pcroom_codingwork_tenter
    pause 1
    pcthink "Her???"
    pc "What the fuck, can't you knock?"
    scene pcroom_codingwork_t1 with dissolve
    t "We have to talk!"
    pcthink "Shit! This is probably about  what happened in the bathroom at [e]'s birthday... I almost forgot about it after everything that happened..."
    t "I have a few questions."
    pc "Huh?"
    t "It's obvious that you play a big role in [e]'s condition, so I have to include you in my research..."
    pc "Errr... okay?"
    scene pcroom_codingwork_t2 with dissolve
    t "Good. Since you seem to be willing to cooperate, let's not waste time..."
    pcthink "I didn't even agree..."
    scene pcroom_codingwork_t3 with dissolve
    t "What was the last thing you did with her before you moved out?"
    scene black with dissolve
    n "She starts to ask questions without hesitation."
    n "You don't want to wake sleeping dogs, so you answer her questions as thoroughly as possible."
    n "Half an hour later..."
    scene pcroom_codingwork_t5 with dissolve
    t "I see... and did this happen more than once?"
    pc "No, it was just this one time..."
    pcthink "Damn, I didn't expect her to ask so many questions... when will she stop?!"
    t "Did she ever tell you that she wanted to marry you?"
    pc "What? What kind of question is that?"
    t "It's quite common for young girls to want to marry their parental figure."
    scene pcroom_codingwork_t6 with dissolve
    if pcgender == "man":
        pc "I'm not her dad!"
    else:
        pc "I'm not her mom!"
    scene pcroom_codingwork_t5 with dissolve
    t "That doesn't matter... did she or not?"
    scene pcroom_codingwork_t6 with dissolve
    pc "...ugh, yes, she did...."
    scene pcroom_codingwork_t5 with dissolve
    t "I see... did you agree?"
    scene pcroom_codingwork_t6 with dissolve
    pc "Why does it even matter? I mean, we were kids, it didn't mean anything!"
    scene pcroom_codingwork_t5 with dissolve
    t "Did you?"
    scene pcroom_codingwork_t6 with dissolve
    pcthink "Shit..."
    menu:
        "Yes.":
            $ efe -=1
            pc "Yes, but as I said, we were just kids!"
        "No":
            pc "Of course not! She didn't even understand what she was asking for at that time."
    scene pcroom_codingwork_t5 with dissolve
    t "I see... did you ever touch her or hold her so she cannot move?"
    pc "What?!"
    scene pcroom_codingwork_t7 with dissolve
    t "...or do you do that only to people you don't know?"
    pc "...the fuck! I {b}never{/b} touched her {b}that{/b} way!"
    t "...so you are just a pervert..."
    pc "I'm not a fucking pervert!"
    t "You obviously {b}are{/b} a pervert!"
    pc "Wait a minute, why am I the pervert here? You were the one who was completely wet..."
    if tc:
        pc "...and it didn't even take a minute for you to cum!"
    else:
        scene pcroom_codingwork_t7_2 with dissolve
        t "W-What are you talking about?"
        scene pcroom_codingwork_t7_3 with dissolve
        pc "Did you think I wouldn't notice that smell last time in the bathroom? It was more than obvious!"
    scene pcroom_codingwork_t8 with vpunch
    t "T-That had nothing to do with you!"
    scene pcroom_codingwork_t9 with dissolve
    if tc:
        pc "Ah yeah? So what was the reason for you cumming so quickly then?"
    else:
        pc "Ah yeah? Wait, don't tell me you did something to [e]!"
        t "W-what? No, of course not!!"
        pc "You better tell the truth!"
        t "I'd never do such a thing, I'm not like that!"
        pc "Hmph... well I guess that make me the only possible reason, doesn't it?"
        t "N-no! I..."
    t "It was just..."
    t "..."
    pc "I'm listening."
    scene pcroom_codingwork_t9_2 with dissolve
    t "Fuck you, it won't ever happen again!"
    pc "No?"
    t "No!"
    menu:
        "Check if she's telling the truth.":
            pass
        "I don't care.":
            pc "Well, whatever, I guess question time is over..."
            if pcgender == "man":
                t "Humph, asshole!"
            else:
                t "Humph, bitch!"
            scene pcroom_codingwork_trun with dissolve
            n "She storms off like a fury."
            play sound "audio/door-opening.ogg"
            scene pcroom_aftercodingwork with hpunch
            play sound "audio/door-closing.ogg"
            pause 1
            pc "Jeez..."
            jump afterTcoerce2
label tcoerce2_r:
    if _in_replay:
        show screen endRep
    if tc:
        pc "Heh, so by your logic, you wouldn't cum again if I touch you?"
        $ tc = 3
    else:
        pc "Heh, so by your logic, you can't be wet right now, right?"
        $ tc = 2
    scene pcroom_codingwork_t9 with dissolve
    t "O-Of course! I..."
    scene pcroom_codingwork_t10 with dissolve
    pc "Alright, why don't we try and see if that's the truth."
    scene pcroom_codingwork_t11 with dissolve
    t "N-No, I didn't mean..."
    pc "No? Yes? What? Can't decide?"
    scene pcroom_codingwork_t12 with dissolve
    t "T-That's not... aahhhn..."
    scene pcroomcodingworkt13 with dissolve
    pc "Well look at that, it seems like you've been waiting for it."
    t "Hnn...no... fuck you! Leave me alone!"
    scene pcroomcodingworkt14_1 with dissolve
    pc "And if not?"
    scene pcroomcodingworkt14_3 with dissolve
    t "I'll scream!"
    scene pcroomcodingworkt15_1 with dissolve
    t "Ahnn..."
    scene pcroom_codingwork_t12_3 with dissolve
    pc "Do it! Stop me if you want."
    scene pcroomcodingworkt15_2 with dissolve
    t "Unnh... f-fuck you! Stop it!"
    scene pcroomcodingworkt15_1 with dissolve
    t "Hnghh..."
    pc "You really need this, don't you?"
    scene pcroom_codingwork_t12_3 with dissolve
    if pcgender == "man":
        t "Hnn... no... Pig!"
    else:
        t "Hnn... no... Dyke!"
    scene pcroomcodingworkt15_2 with dissolve
    pc "Oh I think you do and you know it!"
    scene pcroomcodingworkt15_1 with dissolve
    t "Ahnnn... no... you're forcing me, pervert."
    scene pcroomcodingworkt15_2 with dissolve
    scene pcroomcodingworkt15_1 with dissolve
    t "Haaahh... nnnhh"
    pc "You could just push me away and leave, you know?"
    scene pcroomcodingworkt15_2 with dissolve
    scene pcroomcodingworkt15_1 with dissolve
    t "Ahh... ha... haa..."
    if pcgender == "man":
        t "You... aahh... asshole!"
    else:
        t "You... aahh... bitch!"
    scene pcroomcodingworkt15_2 with dissolve
    scene pcroomcodingworkt15_1 with dissolve
    t "Haahn... nnnnnh..."
    scene pcroom_codingwork_t12_3_3 with dissolve
    t "AAAhhnnn..."
    pc "Well that was quick."
    scene pcroom_codingwork_t12_2 with dissolve
    t "*pant*"
    pc "What a squirter you are, and so needy."
    scene pcroomcodingworktcum with dissolve
    t "Hnnn... *pant*"
    pc "You should thank me you know..."
    scene pcroom_codingwork_t12_3 with dissolve
    t "W-what?! *gasp*"
    pc "I'm sure you heard me."
    t "W-why would I do that!? You molested me..."
    pc "I made you cum, and you clearly needed that."
    t "T-thats not..."
    pc "Thank me!"
    t "...no!"
    pc "Thank me, or leave!"
    scene pcroom_codingwork_t12_2_2 with dissolve
    t "..."
    scene pcroom_codingwork_t12_2 with dissolve
    t "Ugh... Thank you..."
    pc "Good girl!"
    t "..."
    pc "So, you wanted to leave, didn't you?"
    scene pcroom_codingwork_t12_3 with dissolve
    pause .5
    scene pcroom_codingwork_t12_3_2 with dissolve
    if pcgender == "man":
        t "Humph, asshole! Pig!"
    else:
        t "Humph, bitch! Dyke!"
    scene pcroom_codingwork_trun with dissolve
    n "She storms off like a fury."
    play sound "audio/door-opening.ogg"
    scene pcroom_aftercodingwork with hpunch
    play sound "audio/door-closing.ogg"
    pause 1
    pcthink "Wow..."
    pcthink "What a little sub... and so feisty..."
    $ renpy.end_replay()
    jump afterTcoerce2
    
    
label coerceT3:
    #achievement
    $achievement.grant("Achievement_katfull")
    init: 
        $achievement.register("Achievement_katfull")
    $achievement.sync()
    ###########
    if _in_replay:
        show screen endRep
    scene hall_d6_kat3 with dissolve
    t "Huh?"
    pc "We should talk."
    scene hall_d6_kat4 with dissolve
    t "Whaa?!"
    play sound "audio/door-closing.ogg"
    scene pcroom_tcoerce3_1 with dissolve
    t "A-Again?"
    scene pcroom_tcoerce3_1_2 with dissolve
    t "Humph... Why don't you just leave me alone, pervert!"
    pc "Why would I?"
    t "Tch!"
    pc "I saw you in the city today, you know..."
    t "Oh really? I'm surprised you didn't try to molest me there too..."
    pc "I didn't want to interfere."
    t "Don't act like you have any manners. I bet you were just shy because it was out in the open..."
    pc "Nah, it just looked like you had enough to do with your boyfriend."
    scene pcroom_tcoerce3_1_1
    pause 1
    scene pcroom_tcoerce3_1_3 with dissolve
    t "I-I don't have a boyfriend..."
    pc "Yeah, I guess that's true by now... and I bet he won't try to \"molest\" you again."
    scene pcroom_tcoerce3_1_1 with dissolve
    t "W-What are you talking about?!"
    pc "You could have knocked me out, too..."
    scene pcroom_tcoerce3_1_3 with dissolve
    pc "...but you didn't even try..."
    t "I..."
    t "It's not like..."
    pc "Get on your knees!"
    scene pcroom_tcoerce3_1_1 with dissolve
    t "W-what?"
    pc "You heard me."
    scene pcroom_tcoerce3_1_2 with dissolve
    t "N-No, why would I?!"
    pc "Because it's time for you to give something back!"
    t "What are you talking about?"
    pc "You know what I'm talking about."
    scene pcroom_tcoerce3_1_4 with dissolve
    t "..."
    if tc and tc == 3:
        pc "It's been two times already... you've had your fun and I've never asked for anything in return."
    else:
        pc "I've caught you two times already... you've been dripping wet!"
    scene pcroom_tcoerce3_1_1 with dissolve
    t "T-That's not what was happening!"
    if tc:
        pc "No? I didn't make you cum?"
    else:
        $ tc = True
        pc "I don't even need to see it to know that you're wet right now!"
    scene pcroom_tcoerce3_1_3 with dissolve
    t "That's not..."
    pc "Stop being selfish and get on your knees."
    scene pcroom_tcoerce3_1_4 with dissolve
    t "I..."
    pc "Do it!"
    scene pcroom_tcoerce3_1_5 with dissolve
    t "..."
    scene pcroom_tcoerce3_2 with dissolve
    pcthink "Shit, she's really doing it!"
    pause .5
    scene pcroom_tcoerce3_3_1 with dissolve
    pc "Well..."
    scene pcroom_tcoerce3_3_2 with dissolve
    pc "You know what to do."
    t "Unn..."
    scene tbj1 with dissolve
    pause 1
    scene tbj_01 with dissolve
    pause
    pc "Not bad, [t], not bad..."
    if pcgender == "man":
        t "Unn... asshole..."
        pc "Hum, maybe not good enough."
        scene tbj2 with dissolve
        scene tbj_02 with dissolve
        t "*Gag*"
    else:
        t "Unn... bitch..."
        pc "Hum, maybe not good enough."
        scene tbj2 with dissolve
        scene tbj_02 with dissolve
        t "Mmph..."
    pause
    pc "So, how do you like giving something back for a change?"
    t "Gmrrgh!"
    pause
    scene pcroom_tcoerce3talk with dissolve
    t "Ghaaah...haah... I... hate you!"
    pc "Yeah, why don't you go back to it..."
    scene tbj_01 with dissolve
    t "Unn..."
    pause
    pc "Deeper."
    scene tbj_02 with dissolve
    t "Ugh..."
    pc "That's better."
    pause
    pcthink "Damn, she's actually really good at this..."
    pc "Uhh..."
    pcthink "...and despite her attitude, she's really giving it her all!"
    pc "Shit, I'm gonna...!"
    scene tbj2_15 with flash
    pause 1
    scene tbj2_25 with flash
    scene tbj2_25 with flash
    pause 1
    pc "Gaawwd..."
    if pcgender == "man":
        scene pcroom_tcoerce3_acum with dissolve
    t "*Cough*"
    pc "Well that wasn't too bad, I hope you enjoyed it as much as I did."
    scene pcroom_tcoerce3_acum2 with dissolve
    t "*Gulp* ...fuck you!"
    scene pcroom_tcoerce3_acum3 with dissolve
    pc "Still the same attitude, eh?"
    pc "Well, seeya next time, then."
    scene pcroom_tcoerce3_acum4 with dissolve
    t "..."
    $ renpy.end_replay()
    scene pcroom_tcoerce3_acum5 with dissolve
    t "Humph..."
    play sound "audio/door-closing.ogg"
    scene pcroom_tcoerce3_aleft with dissolve
    pause .5
    pcthink "Okay...?"
    pcthink "What was that? No drama, no harassing me, no complaints?"
    pcthink "She just left without a word..."
    pc "Hum..."
    pcthink "Well, at least it was fun. I wonder how far this will go in the future..."
    jump d6_gotobed
    
label d7_city:
    scene d7_city1 with dissolve
    pc "..."
    pcthink "Hum... it's been over a week already that I'm back..."
    pcthink "... and nothing really went like planned..."
    scene d7_city2 with dissolve
    pcthink "But is it really a bad thing? A lot of crazy stuff happened since..."
    pc "...Huh, is that [t]?"
    scene d7_city3 with dissolve
    pcthink "Yeah, looking at the way she walks... that's clearly her attitude..."
    pcthink "What's up with her anyway, I don't get that woman."
    scene d7_city4 with dissolve
    pcthink "Looks like that grumpy guy has the morning shift..."
    scene d7_city5 with dissolve
    pc "Hum... maybe I should follow [t]? This might be a good opportunity to learn a bit more about her."
    menu:
        "Follow her.":
            $ followedt = True
            scene d7_city6 with dissolve
            pcthink "Yeah, let's see where this goes. Maybe I can even have a normal talk with her..................oh who am I kidding..."
            scene black with slowdissolve
        "I need coffee!!!":
            "Naw, fuck that, I need coffee!"
            scene black with slowdissolve
            scene coffeehouse_d6_aran2 with dissolve
            pcthink "Ahhhh..."
            scene coffeehouse_d6_aran with dissolve
            pcthink "That's better..."
            pcthink "..."
            scene black with fade
            jump d7_home
    n "A few minutes later..."
    scene d7_city7 with dissolve
    pcthink "Damn where is she going?"
    pcthink "I doubt that someone like her would have her office in such an area... or even just a client..."
    scene d7_city8 with dissolve
    pcthink "Wait... isn't this the old dopehead corner?"
    pcthink "Don't tell me she's..."
    scene d7_city9 with dissolve
    pcthink "Shit... really, [t]?"
    scene d7_city10 with dissolve
    pause
    scene d7_city_pg1 with dissolve
    pcthink "A playground?"
    scene d7_city_pg2 with dissolve
    pcthink "That definitely wasn't here when I visited this area the last time..."
    pcthink "But it doesn't look new either..."
    scene d7_city_pg3 with dissolve
    if pcgender == "man":
        "Girl" "Hey uncle, can you help me?"
    else:
        "Girl" "Hey auntie, can you help me?"
    pc "Huh? What's up?"
    pcthink "...and where the hell is [t]?!"
    scene d7_city_pg4 with dissolve
    "Girl" "Over here!"
    pc "Hey have you seen..."
    scene d7_city_pg5 with dissolve
    t "HAAYYYA!"
    scene d7_city_pg6f with dissolve
    pause .2
    scene d7_city_pg7_2 with hpunch
    pc "WHOA!"
    scene d7_city_pg8 with dissolve
    t "Y-You?!"
    pc "Shit! What the hell, [t]?! That was too close!"
    scene d7_city_pg9 with dissolve
    "Girl" "Whoa, Katie! That was awesome!!"
    scene d7_city_pg10 with dissolve
    t "I told you not to call me Katie!"
    "Girl" "Shorryyy Katie!"
    scene d7_city_pg11 with dissolve
    "Girl" "Lalala~"
    t "Humph..."
    scene d7_city_pg12 with dissolve
    t "Why are you following me?!"
    pc "I'm not following you, I just wanted to visit an old place..."
    scene d7_city_pg13 with dissolve
    t "Tsk, do you even remember this place?"
    pc "Yeah, of course, it's the old dopehead corner."
    pcthink "Shit, maybe I should have pretended not knowing this place..."
    t "Is that all?"
    pc "What do you mean?"
    scene d7_city_pg14 with dissolve
    t "Tsk! Idiot!"
    scene d7_city_pg14 with dissolve
    pcthink "What the hell?"
    scene d7_city_pg15 with dissolve
    pc "Jeez, why am I an idiot now... what the fuck is wrong with you?!"
    scene d7_city_pg16 with dissolve
    t "With me? Are you serious?"
    t "You are the druglord here..."
    pc "What??"
    scene d7_city_pg17 with dissolve
    t "And you are the one molesting innocent people... and you're the one who doesn't remember anything!"
    pc "Druglord? Remembering? What the fuck are you talking about?! I never sold drugs!"
    scene d7_city_pg18 with dissolve
    t "Humpf... just leave me alone!"
    scene d7_city_pg19 with dissolve
    pcthink "Holy shit... what's going on? What is she talking about?"
    pcthink "Did [m] tell her stories about me?"
    pcthink "But why would she tell lies?"
    pc "Hum... alright, I'll take the bait, now what's this all about... \"Katie\"?!"
    scene d7_city_pg20 with dissolve
    t "DON'T CALL ME KATIE!"
    scene d7_city_pg19 with dissolve
    pc "Haha..."
    pcthink "Wait... Katie.........."
    scene black with slowdissolve
    stop music fadeout 2
    scene dream_01 with fade
    n "Years ago."
    scene black with dissolve
    scene d7_city_pgt1 with dissolve
    pcthink "Almost there..."
    if pcgender == "man":
        pcthink "I wonder if this little slut will come too, hehe."
    else:
        pcthink "I wonder if this little cutie will come too, hehe."
    "Voice" "DON'T CALL ME KATIE!"
    play music "audio/LightSteps.mp3" fadein 1
    pcthink "Huh?"
    scene d7_city_pgt2 with dissolve
    pcthink "Shit, it's those guys..."
    pcthink "But who's the girl?"
    "Guy 1" "You know this bitch?"
    "Guy 2" "Yeah, she's in the same class as my little sister."
    "Guy 1" "Hehe, what is a little girl like you doing in a place like this?"
    "Guy 2" "I bet she's here for a fix."
    t "N-No, I just..."
    "Guy 1" "She can have a fix from my dick!"
    "Guy 2" "Haha, is that what you want Katie? Do you want a dose of dick?"
    t "N-No! Let me go!"
    "Guy 1" "Why not have some fun first, hehe."
    "Guy 2" "Come on Katie, just a little suck!"
    t "No!"
    pcthink "Jeez, these idiots..."
    scene d7_city_pgt3 with dissolve
    pc "Hey, is that all you can do? Scaring little girls?"
    "Guy 1" "YOU!"
    "Guy 2" "Get lost, [pc], this is none of your business!"
    pc "You know, I just thought that you guys must be really desperate. Can't find a girl who actually wants to suck your dick, huh?"
    if pcgender == "man":
        "Guy 2" "What did you just say? Desperate for some beating?"
        pc "Yeah, sure, like last time? Bigmouth?"
        scene d7_city_pgt4 with dissolve
        "Guy 1" "There are two of us now, motherfucker!"
        "Guy 2" "We'll beat the shit out of you, asshole!"
    else:
        "Guy 2" "What did you... how about {b}you{/b} suck my dick, bitch?!"
        pc "You wish!"
        scene d7_city_pgt4 with dissolve
        "Guy 2" "I'll make you beg for it!"
        pc "Good luck with that!"
    scene black with fade
    play sound "audio/punch_fight2.ogg"
    scene black with vpunch
    pause 1
    scene black with hpunch
    scene black with vpunch
    pause 1
    scene black with hpunch
    pause 1
    scene d7_city_pgt5 with dissolve
    pc "...and don't come back!"
    scene d7_city_pgt5_2 with dissolve
    pcthink "Ugh... shit, they almost got me..."
    t "Are you alright?"
    scene d7_city_pgt6 with dissolve
    t "You're bleeding."
    scene d7_city_pgt7 with dissolve
    pc "Yeah, I'm good, it's probably fatal, but that's okay."
    scene d7_city_pgt10 with dissolve
    t "What?!"
    pc "Haha, I'm joking, it's just a scratch. How about you?"
    scene d7_city_pgt8 with dissolve
    t "I'm fine... thank you."
    pc "I haven't seen you here before, are you new?"
    scene d7_city_pgt9 with dissolve
    t "No I..."
    pc "Oh, I see, you really wanted a fix..."
    scene d7_city_pgt10 with dissolve
    t "N-No,  I'm just late, and I wanted to take a shortcut home!"
    pc "Well, you better hurry then, and I'd suggest to avoid this \"shortcut\" from now on."
    pc "It's probably best if you never come back to this place..."
    scene d7_city_pgt11 with dissolve
    t "I won't..."
    stop music fadeout 2
    scene d7_city_pg19 with slowdissolve
    play music mainbgm fadein 1
    pcthink "That little girl... it was her."
    pcthink "Shit, how am I supposed to remember that, I've only met her once, and it's so long ago..."
    t "..."
    pc "Alright..."
    scene d7_city_pg21 with dissolve
    pc "First of all, I never sold drugs! I was just hanging around here from time to time."
    scene d7_city_pg22 with dissolve
    t "Sure..."
    scene d7_city_pg21 with dissolve
    pc "Second, what the hell are {b}you{/b} doing here? Didn't I tell you to never come back to this place?"
    scene d7_city_pg23 with dissolve
    t "..."
    scene d7_city_pg24 with dissolve
    t "So you {b}do{/b} remember..."
    pc "I do... now."
    t "..."
    pc "So?"
    scene d7_city_pg23 with dissolve
    t "So what?!"
    pc "What are you doing here... Katie."
    scene d7_city_pg24 with dissolve
    t "Humph..."
    scene d7_city_pg25 with dissolve
    t "..."
    scene d7_city_pg26 with dissolve
    t "She's the daughter of a client... well, a client of my mentor..."
    scene d7_city_pg25_2 with dissolve
    pc "Your mentor?"
    t "He died two years ago, right before my qualification..."
    pc "Sorry to hear that."
    scene d7_city_pg27 with dissolve
    "Girl" "WOOHOOO!"
    scene d7_city_pg25_2 with dissolve
    pc "So you took his clients over?"
    t "No... I..."
    scene d7_city_pg27_2 with dissolve
    t "He took me with him a few times during my training..."
    t "Her mother died years ago and her dad was constantly drunk..."
    pc "Sounds quite familiar..."
    t "She started to show signs of a mental illness, and my mentor took care of the case."
    t "During that time they took her away from her father and she got adopted by a childless couple, but her new dad died shortly after in an accident..."
    scene d7_city_pg26 with dissolve
    pc "Shit... how did she take it?"
    t "Not so well, unsurprisingly..."
    scene d7_city_pg27 with dissolve
    "Girl" "WOOOO!"
    scene d7_city_pg25_3 with dissolve
    t "Her second mom didn't have enough money to keep the house, so they had to move..."
    t "My mentor accompanied her through all that, and so did I."
    scene d7_city_pg25_4 with dissolve
    pc "I see... but it looks like you made it. She looks healthy and happy."
    scene d7_city_pg25_5 with dissolve
    t "Appearances are often deceptive, you should know that better then anybody else..."
    scene d7_city_pg25_4 with dissolve
    pc "What's that supposed to mean? Are you trying to insult me?"
    t "..."
    scene d7_city_pg28 with dissolve
    "Girl" "Katieeeee! Can you push me?!"
    scene d7_city_pg28_2 with dissolve
    t "..."
    scene d7_city_pg29 with dissolve
    pc "Hey I'm talking to you!"
    scene d7_city_pg30 with dissolve
    t "I know..."
    scene d7_city_pg31 with dissolve
    pcthink "...did she just smile?"
    pcthink "I've never seen her smile before..."
    n "BZZZZzzzzzz!"
    scene d7_city_pg32 with dissolve
    pcthink "Ugh... what does [m] want now?"
    scene d7_city_pg33_2 with dissolve
    pc "Yeah?"
    m "Hey, it's me, [m]."
    pc "Yeah, I know. What's up, [m]?"
    m "I wanted to ask... could you do me a favor, [pc]?"
    scene d7_city_pg33 with dissolve
    pc "What favor?"
    pcthink "[t] really cares for that girl... almost like a mother..."
    m "I ordered 10 packs of toilet paper last week and forgot that they'll arrive today. Could you go to the store and get them for me?"
    scene d7_city_pg33_2 with dissolve
    pcthink "Maybe it's a bit of a therapy for [t] as well..."
    pc "Yeah, I can do that... wait, 10 packs??? Why?!"
    m "They said something about a shortage on TV, so I thought it might be better to have a few in stock."
    pc "But... 10 packs?!"
    m "Can you get them for me?"
    scene d7_city_pg33 with dissolve
    pc "Ugh... fine..."
    m "Thank you, Hun!"
    scene d7_city_pg34 with dissolve
    pcthink "10 packs of toilet paper..."
    scene d7_city_pg33_2 with dissolve
    pc "..."
    pcthink "Looks like both of them are having fun."
    scene d7_city_pg33 with dissolve
    "Girl" "WOOHOOO!"
    pc "..."
    pcthink "I guess I'll just leave..."
    scene black with fade
    n "Nothing special happens on your way back home...\n"
    extend "...except from people staring at you in disbelief when they notice all the toilet paper."
    
    jump d7_evening
    
label d9_tcoffee:
    $ seentd9 = True
    scene d9_tcoffee with dissolve
    if hlo == 3:
        pcthink "Hmm, [h] isn't working today, but a coffee to go would be nice..."
    else:
        pcthink "Hmm a coffee to go would be nice..."
    scene d9_tcoffee02 with dissolve
    pcthink "Oh look who we got here..."
    scene d9_tcoffee03 with dissolve
    pcthink "She hasn't noticed me yet..."
    scene d9_tcoffee04 with dissolve
    pcthink "...maybe I could tease her a bit."
    scene d9tcoffee05 with dissolve
    pc "Hey, Katie."
    scene d9_tcoffee06 with dissolve
    t "HAAA?!"
    scene d9_tcoffee07 with dissolve
    t "Y-you!"
    pc "What's up, Katie."
    scene d9_tcoffee08 with dissolve
    t "Hmph..."
    t "{size=-10}S-Stop touching me...{/size}"
    pc "I'm just hugging you."
    scene d9_tcoffee09 with dissolve
    t "{size=-10}Stop it! Seriously, everyone can see us!{/size}"
    scene d9_tcoffee10 with dissolve
    pc "...and? What's the problem with that?"
    scene d9_tcoffee11 with dissolve
    t "Hmph... Idiot!"
    pcthink "Wow, she really has a stick up her ass... but that could be fun thinking about it."
    scene d9tcoffee12 with dissolve
    pc "One to go."
    scene d9_tcoffee13 with dissolve
    pcthink "Is she waiting for me?"
    pcthink "Guess she wants to talk about something..."
    scene d9tcoffee14 with dissolve
    pc "Thanks."
    scene d9_tcoffee15 with dissolve
    pc "Let's go, Katie."
    scene d9_tcoffee16 with dissolve
    t "Stop calling me..."
    scene d9_tcoffee17 with dissolve
    t "Ugh, whatever... I have an appointment!"
    scene d9_tcoffee18 with dissolve
    pc "Yeah, looks like we're heading in the same direction."
    scene d9_tcoffee19 with dissolve
    t "..."
    pc "Haha, you're cute when you're angry."
    scene d9_tcoffee20 with dissolve
    t "Shut up..."
    scene d9_tcoffee21 with dissolve
    pc "Haha."
    t "..."
    scene d9_tcoffee22 with dissolve
    pc "Are you going to see [e] today?"
    scene d9_tcoffee23 with dissolve
    t "No, but tomorrow..."
    scene d9_tcoffee24 with dissolve
    pc "Again on sunday?"
    t "Every sunday."
    scene d9_tcoffee25 with dissolve
    pcthink "Jeez, I seem to be surrounded by workaholics..."
    pc "Do you ever take a day off?"
    t "Yes..."
    t "..."
    scene d9_tcoffee26_0 with dissolve
    pc "..."
    pc "Alright, stop!"
    scene d9_tcoffee26 with dissolve
    t "Huh?"
    scene d9tcoffee27 with dissolve
    pc "Give me your hand!"
    scene d9tcoffee28 with dissolve
    t "What? Why?!"
    pc "Just give me your hand already..."
    t "..."
    scene d9tcoffee29 with dissolve
    pause
    pc "The other one."
    scene d9tcoffee30 with dissolve
    t "Hmph..."
    scene d9tcoffee31 with dissolve
    pause .5
    scene d9tcoffee32 with dissolve
    pc "Good girl."
    scene d9tcoffee33 with dissolve
    pc "Now let's go..."
    t "W-what are you doing?!"
    scene d9tcoffee34 with dissolve
    pc "Holding your hand obviously..."
    scene d9_tcoffee35 with dissolve
    t "B-but why? Why would you do that?!"
    pc "Maybe to tease you."
    scene d9_tcoffee36 with dissolve
    t "I-Idiot! Let me go!"
    pc "Don't you have an appointment, we better get going."
    scene d9_tcoffee37 with dissolve
    t "I-Idiot..."
    pc "Yeah, yeah, let's go..."
    scene black with slowdissolve
    scene d9tcoffee38 with dissolve
    pc "So... do you have any idea of what's going on with [e]?"
    scene d9_tcoffee39 with dissolve
    t "...hmm?"
    if pcgender == "man":
        pcthink "Damn, she looks cute when the sun shines on her face like that..."
    else:
        pcthink "Wow, she looks beautiful..."
    pcthink "...and she's still blushing red like a tomato."
    pc "I said, do you have any idea of what's going on with [e]?"
    scene d9_tcoffee40 with dissolve
    t "No..."
    scene d9tcoffee41 with dissolve
    pcthink "But she didn't let go of my hand..."
    pcthink "...well not that I would let her, hehe."
    scene d9_tcoffee42 with dissolve
    pc "Wait, what do you mean \"no\"?"
    t "I mean I won't tell you..."
    pc "Huh? What do you mean you won't tell me?"
    scene d9_tcoffee43 with dissolve
    t "Medical discretion."
    pc "Oh come on, I'm her [bs]."
    scene d9_tcoffee44 with dissolve
    t "That doesn't mean I'm relieved from medical discretion."
    scene d9_tcoffee45 with dissolve
    pc "Yeah believe it or not, I know a bit about that stuff. [e] doesn't talk so I doubt she told you to keep whatever you know a secret, that means you're actually allowed to talk about it with close relatives."
    scene d9_tcoffee46 with dissolve
    t "The keyword is \"close\"..."
    scene d9_tcoffee47 with dissolve
    pc "What? You don't think we're close?"
    scene d9_tcoffee48 with dissolve
    t "I don't know..."
    pc "Come on, of course we are close. I'd even say we're closer than ever before!"
    scene d9_tcoffee49 with dissolve
    t "Uh-huh..."
    scene d9_tcoffee50 with dissolve
    t "This is my stop by the way, so I guess we separate here..."
    scene d9_tcoffee51 with dissolve
    pcthink "Ugh, is she playing with me? I bet she expects me to try and force her to tell me what I want to know..."
    pc "So you're not going to tell me anything..."
    scene d9_tcoffee52 with dissolve
    t "No."
    scene d9_tcoffee52_2 with dissolve
    pcthink "As I thought, but I'm not going to play her little game..."
    pc "Fine, see you tomorrow then."
    scene d9_tcoffee53 with dissolve
    t "Huh?"
    scene d9_tcoffee54 with dissolve
    pcthink "Heh, looks like I was right. Now I'm just going to leave."
    t "There's nothing..."
    scene d9_tcoffee55 with dissolve
    pc "Hm? Did you say something?"
    t "..."
    scene d9_tcoffee56 with dissolve
    t "...she is a perfectly normal young woman."
    pc "What do you mean by that?"
    scene d9_tcoffee57 with dissolve
    t "She's just stubborn..."
    scene d9_tcoffee58 with dissolve
    pc "..."
    pcthink "What the hell is that supposed to mean?"
    #achievement
    $achievement.grant("Achievement_kathh")
    init: 
        $achievement.register("Achievement_kathh")
    $achievement.sync()
    ###########
    scene black with slowdissolve
    call screen wmap
    
label d10takekathome:
    n "You hear someone knocking at the front door."
    scene d10pcroom04 with dissolve
    pcthink "Hm? Who the hell would knock instead of using the doorbell?"
    pcthink "Let's have a look."
    scene d10hallbth01 with dissolve
    m "Oh, [t], did you forget something?"
    pcthink "[t], huh? I didn't notice she's left already..."
    t "My car won't start and I have an appointment, would you take me home? I'll get the car by tomorrow..."
    scene d10hallbth02 with dissolve
    m "Oh, that's... unfortunate..."
    scene d10hallbth03 with dissolve
    if mob >=5:
        m "Oh, hey, Hun, would you be so kind and take [t] home, I'm awaiting an urgent call."
    else:
        m "Oh, [pc], could you take [t] home? I'm awaiting a call."
    scene d10hallbth04 with dissolve
    t "I-I would honestly prefer it if you would take me back home, [m]."
    scene d10hallbth05 with dissolve
    m "Come on, [t], I know you don't like each other much, but this might be a good opportunity to reconcile with each other."
    scene d10hallbth06 with dissolve
    t "..."
    pcthink "...I wonder what she's thinking."
    scene d10hallbth07 with dissolve
    m "I... take that as a yes?"
    scene d10hallbth08 with dissolve
    t "Hmph... fine."
    scene d10hallbth09 with dissolve
    t "But as I said, I have an appointment."
    scene d10hallbth10 with dissolve
    m "I'm sure [pc] will make sure to get you home in time."
    scene d10hallbth11 with dissolve
    m "Right, Hun?"
    scene d10hallbth12 with dissolve
    t "That's not...ugh..."
    scene d10hallbth13 with dissolve
    pc "I haven't even agreed yet..."
    if mob >=5 or mend:
        scene d10hallbth14 with dissolve
        m "Oh, please do me that favor, Hun..."
    else:
        scene d10hallbth15 with dissolve
        m "Thank you, Hun."
        pc "Eh..."
    pc "Ugh... fine."
    scene d10hallbth16 with dissolve
    m "Thanks."
    if not mend:
        scene d10hallbth17 with dissolve
        n "*smooch*"
    if not mend:
        scene d10hallbth18_ with dissolve
    pc "..."
    scene d10hallbth18 with dissolve
    t "Hmph."
    pc "Welp, let's go..."
    scene black with slowdissolve
    n "You get into the car, [t] tells you the directions, but otherwise keeps silent."
    n "After a few minutes you reach the town center."
    play sound "audio/driving.ogg" fadein 1
    scene d10bth01 with slowdissolve
    pc "..."
    scene d10bth02 with dissolve
    t "..."
    pcthink "She didn't say a word since we set off..."
    scene d10bth03 with dissolve
    pc "So...what about that appointment you mentioned?"
    scene d10bth04 with dissolve
    t "What about it?"
    scene d10bth05 with dissolve
    pc "What's so important about it that you can't move it?"
    scene d10bth06 with dissolve
    t "I don't think that's any of your business..."
    scene d10bth07 with dissolve
    pc "Humph... being bitchy again, huh?"
    scene d10bth08 with dissolve
    t "Tch, just take me home, I don't care what you think about me!"
    scene d10bth09 with dissolve
    pc "Seriously, I just wanted to start a conversation..."
    scene d10bth10 with dissolve
    t "..."
    pc "..."
    scene d10bth11 with dissolve
    t "...I'm going to see a patient..."
    scene d10bth12 with dissolve
    if followedt:
        pc "The girl?"
        t "Yes..."
    pc "I see..."
    scene d10bth13 with dissolve
    t "..."
    pc "..."
    pc "You know what I don't get?"
    t "What?"
    scene d10bth14 with dissolve
    pc "How somebody like you... I mean you aren't really the most sensitive person, so..."
    pc "Why did you become a shrink?"
    scene d10bth15 with dissolve
    t "Psychotherapist..."
    scene d10bth16 with dissolve
    pc "Yeah..."
    scene d10bth31 with dissolve
    t "..."
    scene d10bth18_ with dissolve
    t "There was... This person I met when I was younger..."
    t "That person was... not... really..."
    scene d10bth19 with dissolve
    if followedt:
        pc "Come on now, if you're talking about me, just say it..."
    else:
        pc "What now, are you struggling to talk about your own past, Miss \"Psychotherapist\"?"
    scene d10bth20 with dissolve
    t "Hmph..."
    t "Well, you probably can't imagine how it is growing up with parents only interested in their jobs..."
    scene d10bth with dissolve
    pc "I guess you probably know what my parents did for a living."
    scene d10bth22 with dissolve
    t "My mother was a bank manager, my dad an equity analyst."
    t "They didn't really expect me to follow in their footsteps, but..."
    scene d10bth23 with dissolve
    t "They had expectations..."
    t "So I spent most of my childhood learning..."
    scene d10bth24 with dissolve
    t "I wasn't allowed to have many friends... I didn't have much free time... so I didn't have many interactions with other people..."
    scene d10bth25 with dissolve
    pc "So you got curious."
    scene d10bth26 with dissolve
    t "No."
    t "Do you want me to tell the story or do you want to make your own assumptions?"
    scene d10bth27 with dissolve
    pc "Tch... go on..."
    scene d10bth28 with dissolve
    t "...I went to a private school and..."
    t "I thought the other kids were stupid... they were busy being kids and I spent my time reading books or learning, so it's kind of true I guess..."
    scene d10bth29 with dissolve
    pc "Depends on how you look at it."
    scene d10bth30 with dissolve
    t "...maybe."
    scene d10bth31 with dissolve
    t "Anyway, I knew there are foul people in the world, my parents warned me about them, I read about them in books, et cetera..."
    t "And one day... due to some unfortunate events... I met some of them..."
    scene d10bth32 with dissolve
    pc "What happened?"
    scene d10bth33 with dissolve
    t "I was reading a book in the library that hooked me for a bit too long, so I was late to get back home and despite the fact that it was well known place where all sorts of scum hang out I decided to take a shortcut that I knew I should've avoided..."
    scene d10bth34 with dissolve
    if followedt:
        pcthink "Is she talking about the dopehead corner?"
    t "I thought I'd just quickly rush through, but of course it didn't go well..."
    scene d10bth35 with dissolve
    t "That was the first time I've ever met such people and it made me curious about how such people work..."
    pc "..."
    scene d10bth36 with dissolve
    t "..."
    scene d10bth37 with dissolve
    pc "Err..."
    pc "That's it?"
    scene d10bth38 with dissolve
    t "Yes."
    scene d10bth39 with dissolve
    pc "Oh come on, you don't want me to make assumptions, but won't tell the whole story? That's bullshit..."
    t "Uch..."
    scene d10bth40 with dissolve
    t "The person I was talking about earlier saved me despite being scum themselves at the time and I got curious why... that's why I started looking into psychology... that's why I started taking kick-boxing classes... that's why I took the case of a young girl that..."
    scene d10bth41 with dissolve
    t "..."
    if followedt:
        pc "...are you telling me that you've become a shrink because of me?"
        scene d10bth42 with dissolve
        t "Psychotherapist."
        scene d10bth43 with dissolve
        pc "Yeah, fine, Katie."
        scene d10bth44 with dissolve
        t "Uch, fuck you, too!"
    else:
        pcthink "Hmm...where have I heard that story before..."
        scene d10bth42 with dissolve
        pc "A young girl that...?"
        scene d10bth44 with dissolve
        t "..."
        pc "Are you talking about [e]?"
        t "..."
    scene d10bth45 with dissolve
    t "Over there..."
    pc "Hm?"
    scene d10bth46 with dissolve
    t "The white house at the junction, that's where I live."
    scene d10bth47 with dissolve
    pc "Oh, right."
    scene d10bth48 with dissolve
    t "Oh no..."
    scene d10bth49 with dissolve
    pc "Isn't that your ex?"
    scene d10bth50 with dissolve
    t "Can you do me a favor?"
    stop sound fadeout 2
    scene d10bth51 with dissolve
    pc "Depends..."
    scene d10bth52 with dissolve
    t "I... just follow me to the entrance... I don't want to waste time with him."
    scene d10bth53 with dissolve
    pc "Hmm... guess that would mean you owe me one."
    scene d10bth54 with dissolve
    t "Uch... what do you want..."
    scene d10bth54_2 with dissolve
    pc "I don't know...yet."
    scene d10bth55 with dissolve
    t "Fine, whatever, just... help me!"
    scene d10bth56 with dissolve
    play sound "audio/traffic.ogg"
    "Guy" "[t], I was waiting for you."
    scene d10bth57 with dissolve
    t "Didn't I tell you that I don't want to see you again?"
    scene d10bth58 with dissolve
    "Guy" "But I wanted to apologize."
    scene d10bth59 with dissolve
    t "I don't care, I don't want to see you anymore..."
    scene d10bth60 with dissolve
    pc "I think you'd better leave, dude."
    scene d10bth61 with dissolve
    "Guy" "Who's that?"
    if pcgender == "man":
        "Guy" "Don't tell me he's..."
        scene d10bth62 with dissolve
        t "He's..."
        scene d10bth63 with dissolve
        t "...my new boyfriend..."
    else:
        scene d10bth62 with dissolve
        t "She's..."
        scene d10bth63 with dissolve
        t "...my new girlfriend..."
    pcthink "Heh.."
    scene d10bth64 with dissolve
    "Guy" "W-What?"
    if pcgender == "woman":
        "Guy" "A-Are you lesbian now?!"
        t "Looks like it, doesn't it?"
    "Guy" "B-But... but..."
    scene d10bth65 with dissolve
    "Guy" "T-That's NTR!!!"
    scene d10bth66 with dissolve
    pcthink "Oh geez..."
    t "It's what?"
    scene d10bth67 with dissolve
    pc "It's not NTR, you're {b}not{/b} together anymore!"
    scene d10bth68 with dissolve
    "Guy" "Y-You can't do this to me, [t]."
    scene d10bth69 with dissolve
    t "Ugh, whatever, let's just get inside... Love..."
    pcthink "Wow, did she really just call me Love?"
    scene d10bth70 with dissolve
    pc "Damn, that was quite heartless, Katie, even for you."
    scene d10bth71 with dissolve
    t "It will be easier for him to accept it that way..."
    scene d10bth72 with dissolve
    t "...and stop calling me Katie!"
    scene d10bth73 with dissolve
    if followedt:
        pcthink "But that wouldn't be as much fun..."
    play sound "audio/charger_leave.ogg"
    pause 1
    scene d10bth74 with dissolve
    t "Thank god..."
    scene d10bth75 with dissolve
    if not tc:
        t "I almost expected him to start making a scene..."
        scene d10bth76 with dissolve
        t "Uhh... well, thanks I guess..."
        scene d10bth77 with dissolve
        t "Bye..."
        pause 1
        play sound "audio/door-closing.ogg"
        scene d10bth77_2 with dissolve
        pc "What?!"
        pcthink "Ugh... bitch!"
    else:
        t "..."
        scene d10bth76 with dissolve
        t "I almost expected him to start making a scene..."
        scene d10bth77 with dissolve
        pcthink "Hum... she left the door open..."
        pcthink "I guess that's an invitation."
        scene black with slowdissolve
        scene kathouse01 with dissolve
        pc "Soooo, Katie..."
        t "Uch..."
        scene kathouse02 with dissolve
        t "Do you always enter somebody's home without being invited?"
        scene kathouse03 with dissolve
        pc "You left the door open."
        scene kathouse04 with dissolve
        t "That doesn't mean you can just enter!"
        scene kathouse05 with dissolve
        pc "Yeah, yeah, why don't you just stop the bullshit for a while..."
        scene kathouse06 with dissolve
        t "W-What?"
        scene kathouse07 with dissolve
        pc "Nice little house by the way, is it yours?"
        t "Yes..."
        scene kathouse08 with dissolve
        pc "I wouldn't have thought that a psychotherapist makes that much money."
        scene kathouse09 with dissolve
        t "It's... my parents bought it..."
        pcthink "What a surprise..."
        scene kathouse10 with dissolve
        t "They bought it for me after I finished my psychotherapist training."
        scene kathouse11 with dissolve
        pc "..."
        scene kathouse12 with dissolve
        pc "They must've been proud."
        scene kathouse13 with dissolve
        t "..."
        scene kathouse14 with dissolve
        t "It was more like a \"We don't like what you do, but we've bought this house for you, so you can move out.\""
        scene kathouse15 with dissolve
        pc "Ouch... are you sure that's what it meant?"
        scene kathouse16 with dissolve
        t "..."
        scene kathouse17 with dissolve
        t "They've been like that from the moment they realized I won't follow the route they had planned for me."
        scene kathouse18 with dissolve
        pc "I see, the typical \"parents want to shape their children's future\" story..."
        scene kathouse19 with dissolve
        t "Don't act like you know about my childhood!"
        pcthink "And here we go again..." 
        scene kathouse20 with dissolve
        t "God, why am I even telling you all this?"
        pcthink "I guess I better do something before she goes all tsundere again..."
        pc "Well..."
        scene kathouse21 with dissolve
        if pcgender == "man":
            pc "Now that I'm officially your boyfriend..."
        else:
            pc "Now that I'm officially your girlfriend..."
        scene kathouse22 with dissolve
        t "Oh no, that's not..."
        scene kathouse23 with dissolve
        pc "...I think it's only fair that you tell me a bit more about you."
        scene kathouse24 with dissolve
        t "Ugh..."
        scene kathouse25 with dissolve
        t "I have an appointment..."
        scene kathouse27 with dissolve
        pc "When?"
        scene kathouse26 with dissolve
        t "What does it matter?"
        scene kathouse28 with dissolve
        pc "Just answer."
        scene kathouse29 with dissolve
        t "...in about an hour..."
        scene kathouse30 with dissolve
        pc "So enough time."
        scene kathouse31 with dissolve
        t "I still have to get there..."
        scene kathouse30 with dissolve
        pc "I brought you here, I'll bring you there."
        scene kathouse32 with dissolve
        t "I'm not..."
        scene kathouse33 with dissolve
        t "Ah..."
        scene kathouse34 with dissolve
        pause .5
        scene kathouse34_2 with dissolve
        pause
        scene kathouse35 with hpunch
        t "I-I still need to change clothes..."
        scene kathouse36 with dissolve
        pc "I thought you have an appointment and not a date."
        t "It's not a date, I just need new..."
        scene kathouse37 with dissolve
        pc "New what? Panties?"
        t "Shut up!"
        pcthink "Heh, this is going to be fun..."
        stop music fadeout 2
        scene black with fade
        n "You follow her upstairs."
        scene kathouse38 with dissolve
        pcthink "Hm, fancy... her parents must've made some good money..."
        scene kathouse39 with dissolve
        t "Uhn..."
        pcthink "Not bad..."
        scene kathouse40 with dissolve
        pcthink "I wonder if she paid for anything in this house by herself..."
        scene kathouse41 with dissolve
        pc "Phew..."
        if pcgender == "man":
            pc "Nice ass!"
        else:
            pc "Look at those curves!"
        scene kathouse42 with vpunch
        t "WHAA!"
        scene kathouse43 with dissolve
        t "P-Pervert!"
        pc "Maybe you should start closing doors if you don't want people to enter."
        scene kathouse44 with dissolve
        t "H-How should I know that you're such a pervert?"
        pc "Pervert? Just admit that you wanted me to come in."
        scene kathouse45 with dissolve
        t "Why would I want that, not everyone is such a pervert like you!"
        pc "Like me? I'm not the one who's getting off of getting molested."
        t "I'm not! I-I... I'm just sensitive!"
        scene kathouse46 with dissolve
        pc "Sensitive my ass, you're just a spoiled brat!"
        t "I'm not a brat!"
        pc "Not a brat, huh?"
        scene kathouse47 with dissolve
        t "Whaa!"
        scene kathouse48 with dissolve
        t "What are you doing?"
        scene kathouse49 with vpunch
        t "Ah!"
        scene kathouse53 with dissolve
        pc "I'm going to give you what you need."
        t "L-Let me go, pervert!"
        scene kathouse50 with dissolve
        pc "Not yet, princess!"
        play sound "audio/slap1.ogg"
        scene kathouse51 with hpunch
        scene kathouse52 with dissolve
        t "Whaaa!"
        t "A-Are you crazy?"
        scene kathouse50 with dissolve
        pc "I could ask you the same question!"
        play sound "audio/slap1.ogg"
        scene kathouse51 with hpunch
        scene kathouse52 with dissolve
        t "Ahhh!"
        pc "Bet you've never been spanked before, right?"
        scene kathouse50 with dissolve
        pause .1
        play sound "audio/slap1.ogg"
        scene kathouse51 with hpunch
        scene kathouse52 with dissolve
        t "Ahh!"
        scene kathouse53 with dissolve
        t "Don't act like you know anything about me!"
        scene kathouse50_2 with dissolve
        pc "Oh but I know..."
        play sound "audio/slap3.ogg"
        scene kathouse51_2 with hpunch
        scene kathouse52_2 with dissolve
        t "Nnnaah!"
        scene kathouse54 with dissolve
        pc "...what you like."
        scene kathouse55 with dissolve
        t "Hnnn... don't..."
        scene kathouse54 with dissolve
        scene kathouse55 with dissolve
        t "Mmmmh..."
        pc "Don't, what?"
        t "S-Stop doing that!"
        scene kathouse50_2 with dissolve
        pc "So you want me to go back to..."
        play sound "audio/slap3.ogg"
        scene kathouse51_2 with hpunch
        pc "this!{w=0.5}{nw}"
        scene kathouse52_2 with dissolve
        t "Ahhh!"
        t "N-No, stop that!"
        pc "You want me to do the other thing then?"
        t "..."
        scene kathouse50_2 with dissolve
        pc "I'm listening."
        play sound "audio/slap1.ogg"
        scene kathouse51_2 with hpunch
        scene kathouse52_2 with dissolve
        t "AAhh, YES! Yes..."
        pc "Yes, what?"
        t "...yes... go on..."
        pc "With what?"
        t "Hnn... fuck you..."
        pc "Hm? I can't hear you."
        t "Hmph... t-touching!"
        scene kathouse50_2 with dissolve
        pause .5
        play sound "audio/slap3.ogg"
        scene kathouse51_2 with hpunch
        scene kathouse52_2 with dissolve
        t "AHH, you can touch me, you can touch me!"
        pc "Say please."
        t "W-What!?"
        scene kathouse50_2 with dissolve
        pause .5
        play sound "audio/slap3.ogg"
        scene kathouse51_2 with hpunch
        scene kathouse52_2 with dissolve
        scene kathouse53 with dissolve
        t "Haa! Please touch me..."
        scene kathouse54 with dissolve
        pc "Good girl."
        scene kathouse55 with dissolve
        scene kathouse54 with dissolve
        t "Hnnn!"
        scene kathouse55 with dissolve
        scene kathouse54 with dissolve
        pc "You really like that, don't you?"
        scene kathouse55 with dissolve
        scene kathouse54 with dissolve
        t "Nnn... fuck you!"
        scene kathouse56 with dissolve
        pc "I think that's enough for now."
        scene kathouse57 with dissolve
        t "H-Huh?"
        scene kathouse58 with dissolve
        pc "Look at the mess you made on my fingers."
        scene kathouse59 with dissolve
        pc "Here."
        t "T-That's your own fault..."
        pc "What was that?"
        t "..."
        pc "Clean it."
        t "..."
        scene kathouse60 with dissolve
        t "Unh..."
        scene kathouse61_2 with dissolve
        pc "Look at me."
        scene kathouse61 with dissolve
        pc "Good girl."
        scene kathouse61_3 with dissolve
        pause .2
        scene kathouse61 with dissolve
        pause .2
        scene kathouse61_3 with dissolve
        pause .2
        scene kathouse61 with dissolve
        pause .2
        scene kathouse61_2 with dissolve
        pc "Good."
        scene kathouse62 with dissolve
        pc "Now get up."
        scene kathouse63 with dissolve
        t "..."
        scene kathouse64 with dissolve
        pc "Come on, or do you want more spanking?"
        scene kathouse65 with dissolve
        t "..."
        scene kathouse66 with dissolve
        pc "Look at me."
        scene kathouse67 with dissolve
        t "..."
        scene kathouse68 with dissolve
        pc "You have some nice little titties, you know that?"
        scene kathouse69 with dissolve
        t "Humph, they aren't \"little\"!"
        scene kathouse70 with dissolve
        pc "Haha, show me."
        scene kathouse71 with dissolve
        t "Humph..."
        pc "Cute!"
        menu lookatkat:
            "(Look down.)" if not lookatkat or lookatkat == 6 or lookatkat == 3 and lookatkatcount != 10 and lookatkatcount != 20:
                scene kathouse72 with dissolve
                pause
                $ lookatkat = 1
                $ lookatkatcount +=1
                jump lookatkat
            "(Look down.)" if lookatkat == 4 or lookatkat == 7 and lookatkatcount != 10 and lookatkatcount != 20:
                scene kathouse74 with dissolve
                pause
                $ lookatkat = 2
                $ lookatkatcount +=1
                jump lookatkat
            "(Look up.)" if lookatkat == 1 or lookatkat == 8 and lookatkatcount != 10 and lookatkatcount != 20:
                scene kathouse71 with dissolve
                pause
                $ lookatkat = 3
                $ lookatkatcount +=1
                jump lookatkat
            "(Look up.)" if lookatkat == 5 or lookatkat == 2 and lookatkatcount != 10 and lookatkatcount != 20:
                scene kathouse73 with dissolve
                pause
                $ lookatkat = 4
                $ lookatkatcount +=1
                jump lookatkat
            "(Tell her to turn around.)" if lookatkat == 1 or lookatkat == 8 and lookatkatcount != 10 and lookatkatcount != 20:
                scene kathouse71 with dissolve
                pc "Turn around, Katie."
                t "*grumble*"
                scene kathouse74 with dissolve
                pause
                $ lookatkatcount +=1
                $ lookatkat = 5
                jump lookatkat
            "(Tell her to turn around.)" if lookatkat == 4 or lookatkat == 7 and lookatkatcount != 10 and lookatkatcount != 20:
                pc "Turn around."
                scene kathouse71 with dissolve
                pause
                $ lookatkat = 6
                $ lookatkatcount +=1
                jump lookatkat
            "(Tell her to turn around.)" if lookatkat == 6 or lookatkat == 3 and lookatkatcount != 10 and lookatkatcount != 20:
                pc "Turn around."
                scene kathouse73 with dissolve
                pause
                $ lookatkat = 7
                $ lookatkatcount +=1
                jump lookatkat
            "(Tell her to turn around.)" if lookatkat == 2 or lookatkat == 5 and lookatkatcount != 10 and lookatkatcount != 20:
                pc "Turn around."
                scene kathouse72 with dissolve
                pause
                $ lookatkat = 8
                $ lookatkatcount +=1
                jump lookatkat
            
            "(Tell her to bend over.) {i}{color=#f00}advance scene{/color}{/i}" if lookatkat == 2 or lookatkat == 5:
                pc "Bend over, let me see that ass, Katie."
                t "..."
                scene kathouse75 with dissolve
                pause
                if pcgender == "woman":
                    pc "Damn, do you ever complain?"
                else:
                    pc "Damn, what a nice ass."
                t "..."
                pc "A little more."
                scene kathouse76 with dissolve
                pc "Good girl."
                scene kathouse77 with dissolve
                pause .5
                scene kathouse78 with dissolve
                t "Nhh!"
                scene kathouse78_2 with dissolve
                pause .2
                scene kathouse78 with dissolve
                t "Haaa..."
                pause .2
                scene kathouse78_2 with dissolve
                pause .2
                scene kathouse78 with dissolve
                t "Nhh... I..."
                pc "Yes?"
                pause .2
                scene kathouse78_2 with dissolve
                pause .2
                scene kathouse78 with dissolve
                t "I-I..."
        if lookatkatcount == 10:
            t "Can you stop staring at me and just do something already?"
            pc "Heh, so eager."
            $ lookatkatcount = 11
            jump lookatkat
        if lookatkatcount == 20:
            t "Alright, that's... that's enough!"
            pc "Haha, fine."
            if lookatkat == 2 or lookatkat == 5 or lookatkat == 4 or lookatkat == 7:
                scene kathouse73 with dissolve
            else:
                pc "Turn around one last time."
                scene kathouse73 with dissolve
                t "Humph..."
        scene kathouse80 with dissolve
        pc "Let's get a little bit more personal then!"
        scene kathouse81 with hpunch
        t "Whaa!"
        scene kathouse82_1 with dissolve
        t "I-Idiot!"
        pc "What? Are you afraid of being close to your [boygirl]friend?"
        scene kathouse82 with dissolve
        t "N-No, that's..."
        t "I..."
        scene kathouse83 with hpunch
        t "STOP IT!"
        pc "Whoa, what the hell?! What's wrong now?"
        scene kathouse84 with dissolve
        t "I..."
        t "I know about you and [e]..."
        pc "Huh?"
        if jlo >= 2:
            scene kathouse85 with dissolve
            t "...and [j]."
            pc "What?!"
        scene kathouse86 with dissolve
        t "I..."
        t "I'm not going to be the fifth wheel!"
        pc "How do you even know about that?"
        scene kathouse85 with dissolve
        t "By doing my job."
        pc "Yeah, I doubt that anyone would've told you."
        scene kathouse86 with dissolve
        t "I'm not blind, and you also just confirmed it!"
        pc "Ugh, shit... that was sneaky."
        scene kathouse87 with dissolve
        t "I... I don't know what you're planning, but I'm not going to be part of it!"
        pc "Planning? I'm not planning anything."
        t "Hmph, sounds like you..."
        pc "Ah right, because I'm \"stupid scum\", right?"
        t "..."
        pc "...and for \"not taking part\" you just moaned a lot!"
        t "I-I was just curious how far you would go!"
        pc "Suuuure, and I was just curious how far {b}you{/b} would go..."
        scene kathouse88 with dissolve
        t "T-That's bullshit!"
        scene kathouse89 with dissolve
        pc "Just be honest, you like it!"
        scene kathouse86 with dissolve
        t "Why would I?"
        pc "I'm not stupid, [t], I might not be a shrink like you, but I can see when someone is enjoying herself."
        scene kathouse88 with dissolve
        t "I was just acting!"
        scene kathouse89 with dissolve
        pc "As if... I'm sorry to tell you, but you're really bad at acting."
        scene kathouse86 with dissolve
        t "Ugh... did you ever think about how [e] would feel about this, if she finds out?"
        if harem:
            pc "She'd be okay with it."
            scene kathouse87 with dissolve
            t "..."
            t "I highly doubt that!"
            pc "You could ask her."
            t "Hmph..."
            scene kathouse86 with dissolve
            t "I told you I'm not going to be the fifth wheel!"
            scene kathouse87 with dissolve
            pc "And who says that you're going to be the fifth wheel?"
            scene kathouse88 with dissolve
            t "What else am I going to be then?"
            scene kathouse87 with dissolve
            t "... uch... I don't even want to know..."
        else:
            scene kathouse87 with dissolve
        pc "It's not that I could do anything with [e] officially ever... and she knows that as well..."
        if jlo >= 2:
            pc "...and [j]... well it's [j], you know her better than I do, do you really think she'd be interested in something serious? She wants to have fun."
        pc "You on the other hand got exactly what you wanted, isn't that true?"
        scene kathouse84 with dissolve
        t "Uch..."
        scene kathouse90 with dissolve
        pc "..."
        scene kathouse91 with dissolve
        pc "What are you doing?"
        scene kathouse92 with dissolve
        t "I still have an appointment..."
        scene kathouse93 with dissolve
        t "...and not much time left."
        scene kathouse94 with dissolve
        pc "..."
        scene kathouse95 with dissolve
        pc "I told you I'm going to bring you."
        scene kathouse96 with dissolve
        t "That doesn't make any difference..."
        scene kathouse97 with dissolve
        t "...and I'm going to take the bus..."
        scene kathouse98 with dissolve
        pc "Jeez, are you serious now?!"
        scene kathouse99 with dissolve
        t "I am."
        scene kathouse100 with dissolve
        t "Close the door when you leave."
        scene kathouse101 with dissolve
        play sound "audio/door-opening.ogg"
        play sound "audio/door-closing.ogg"
        pc "The fuck..."
        pcthink "?"
        pcthink "Right, she probably expects me to go after her like in a fury..."
        pcthink "Heh, not gonna happen!"
        pcthink "..."
        pcthink "...I doubt she'd trust me enough to leave me alone in her house{cps=2}........{/cps} right?"
        pcthink "..."
        pcthink "Shit!"
        scene black with dissolve
        n "You head down to see if she really left..."
        play sound "audio/traffic.ogg" loop
        scene kathouse102 with dissolve
        pcthink "Damnit!"
        pcthink "I can't believe that just happened..."
    scene black with fade 
    n "You get in the car and drive back home." with slowdissolve
    if hlo == 3:
        n "Stopping on a red traffic light, you notice that you got a message on your phone..."
        jump d10hdate
    jump d10johnson
        
label d11tfirst:
    scene d11katvisit02 with dissolve
    t "We need to talk..."
    play sound "audio/door-closing.ogg"
    scene d11katvisit03 with dissolve
    j "Oh it's just you, [t]. Aren't you a little early?"
    scene d11katvisit04 with dissolve
    if harem and jlo > 3:
        if pcgender == "man":
            t "I need to talk to your boyfriend, [j]... alone."
        else:
            t "I need to talk to your girlfriend, [j]... alone."
    else:
        t "I need to talk to [pc]... alone."
    scene d11katvisit05 with dissolve
    j "Err... Okay, sure."
    scene d11katvisit06 with dissolve
    j "Just don't do anything I wouldn't do."
    scene d11katvisit07 with dissolve
    t "I presume that's not much..."
    scene d11katvisit08 with dissolve
    pc "What's this all about now?"
    scene d11katvisit09 with dissolve
    t "Let's go to your room, I don't want to talk in the hallway."
    scene d11katvisit10 with dissolve
    pcthink "Hmm, I wonder what she wants..."
    scene d11katvisit11 with dissolve
    pcthink "Probably about yesterday."
    scene d11katvisit12 with dissolve
    t "Are you going to keep standing there?"
    if tc:
        pc "Eh... no I was just admiring your rear."
        scene d11katvisit13 with dissolve
        t "Uch..."
    else:
        pc "Eh... no..."
        scene d11katvisit13 with dissolve
        pause .7
    play sound "audio/door-closing.ogg"
    scene d11katvisit14 with dissolve
    pc "There's nobody home anyway, aside from me and [j], but I'm sure you knew that already..."
    scene d11katvisit15 with dissolve
    pc "So, why did you come so early and why do we need to be alone?"
    if tc:
        scene d11katvisit16 with dissolve
        t "..."
        scene d11katvisit15 with dissolve
    ##################
    t "It's about your past, your families past... and before you ask, I need to talk about it for [e]'s therapy."
    pc "Okay... what exactly do you need to know?"
    t "..."
    t "I know your dad was abusive towards [m]..."
    pc "..."
    t "I know he was never really abusive towards you, is that correct?"
    pc "Why do you ask if you know about it anyway?"
    t "Because I've only heard one side of the story... or one and a half so to speak."
    pc "One and a half?"
    scene d11katvisit15_2 with dissolve
    t "Not important, what's important is your answer."
    scene d11katvisit17 with dissolve
    pc "Hmph... sit down..."
    scene d11katvisit18 with dissolve
    pc "He wasn't... abusive..."
    scene d11katvisit19 with dissolve
    pc "Not to me, not like he was with [m]..."
    pc "He was still an asshole, though, thinking I wouldn't notice anything."
    scene d11katvisit19_2 with dissolve
    t "So you knew how he was treating [m]?"
    scene d11katvisit19_1 with dissolve
    pc "Well, I wouldn't say I knew... I was a kid, I knew something was wrong, but I didn't understand it."
    scene d11katvisit19_2 with dissolve
    t "Weren't you in your teens before he died?"
    scene d11katvisit19_1 with dissolve
    pc "Yes, but that doesn't mean I fully understood it."
    scene d11katvisit19_3 with dissolve
    t "You didn't understand that your dad was beating her?"
    pc "Listen, before my mom died, he was a totally normal guy, I think he was even a good dad from what I remember, and even after he met [m], everything was fine at first..."
    scene d11katvisit19_1 with dissolve
    pc "So as a kid I had no reason to not believe him when he said [m] was clumsy and hurt herself by accident..."
    t "..."
    pc "I basically grew up with it, so I simply thought it was her fault, that it was just the way she is. I only really understood what was going on when I grew older."
    scene d11katvisit19_4 with dissolve
    t "..."
    scene d11katvisit19_5 with dissolve
    t "I guess she didn't make it any easier either..."
    scene d11katvisit19_4 with dissolve
    pc "That's for sure..."
    pc "After his death... when she started... being like that..."
    pc "I even started thinking that she was always like that, that it was her fault that my dad became... the man he was before his death..."
    t "..."
    pc "..."
    scene d11katvisit19_5 with dissolve
    t "Did he..."
    scene d11katvisit19_2 with dissolve
    t "Did he ever touch [e]?"
    scene d11katvisit19_1 with dissolve
    pc "..."
    pc "He was actually quite nice towards her until he died..."
    scene d11katvisit19_3 with dissolve
    t "That doesn't answer my question."
    scene d11katvisit19_1_2 with dissolve
    pc "..."
    pc "I think he felt guilty for what he did to [m], so he kinda tried to make up for it by being nice to [e]..."
    scene d11katvisit19_2 with dissolve
    t "Is that your {i}analysis{/i}?"
    scene d11katvisit19_1 with dissolve
    pc "It's what I think. He treated her nicer than me, and he treated me nicer than [m]."
    scene d11katvisit19_3 with dissolve
    t "Have you been jealous of her? Of how he treated her?"
    scene d11katvisit19_1 with dissolve
    pc "Jealous of [e]? No..."
    scene d11katvisit19_6 with dissolve
    t "..."
    pc "Well... maybe a little bit, but I can't remember being really jealous."
    scene d11katvisit19_2 with dissolve
    t "Do you remember how he died?"
    pc "...really now?"
    pc "I'm sure you heard it from [m], I'm even sure you've read the official documents, don't you have any other questions? Also, sit down!"
    scene d11katvisit19_5 with dissolve
    t "Hmph..."
    t "..."
    scene d11katvisit19_2 with dissolve
    t "Do you intend to stay here?"
    scene d11katvisit19_1 with dissolve
    pc "What do you mean?"
    scene d11katvisit19_2 with dissolve
    t "Will you stay in this house, in this town, or do you intent to move away again."
    scene d11katvisit19_1 with dissolve
    pc "Funny, [j] asked me the same question a few days ago..."
    scene d11katvisit20 with dissolve
    t "And?"
    scene d11katvisit21 with dissolve
    pc "Well... why don't you sit down already."
    scene d11katvisit22 with dissolve
    t "I'm good, just answer."
    scene d11katvisit23 with dissolve
    pc "Hmph... suit yourself."
    pc "The agreement with [m] was to live here until I find a new apartment."
    scene d11katvisit24 with dissolve
    t "That doesn't answer my question."
    pc "Why do you even ask?"
    scene d11katvisit25 with dissolve
    t "It might as well be important for [e]'s therapy."
    scene d11katvisit26 with dissolve
    pc "For [e] huh? Are you sure it isn't something {b}you{/b} just want to know?"
    scene d11katvisit27 with dissolve
    t "Why would I? Also, I've told you about me yesterday, don't you think it's only fair to return the favor?"
    scene d11katvisit26 with dissolve
    pc "The favor? Aren't you the one who owes me a favor? And that aside, you didn't really tell me much anyway... I've told you a lot more just now."
    scene d11katvisit28 with dissolve
    t "Not much?!"
    #scene d11katvisit26 with dissolve
    pc "Well, most of it was you beating around the bush..."
    scene d11katvisit25 with dissolve
    t "I'm sorry I haven't had such a bad childhood as you had, but do you think that makes it easy for me to talk about that?"
    scene d11katvisit26 with dissolve
    pc "Well... probably not..."
    pc "Oh well... I guess I can tell you that I wasn't sure about [m] at first..."
    scene d11katvisit28 with dissolve
    t "Whether or not she really changed?" 
    pc "Yeah, I wouldn't stay any longer than I have to, if she hadn't changed."
    scene d11katvisit29 with dissolve
    t "Did you think she was lying?"
    scene d11katvisit30 with dissolve
    pc "Yes, to be honest. It's not like people just suddenly change, and trust doesn't come over night."
    scene d11katvisit31 with dissolve
    t "That's for sure, but I can tell you, she regrets what happened in the past, and she's not the same woman anymore."
    scene d11katvisit32 with dissolve
    pc "...and you know that because? Are you [m]'s therapist now, too?"
    scene d11katvisit33 with dissolve
    t "My mentor was her therapist, I have access to all of his documents, and even though her therapy ended a long time ago, we still talk from time to time."
    scene d11katvisit34 with dissolve
    pc "Your mentor was her therapist?"
    scene d11katvisit35 with dissolve
    t "Yes, didn't I tell you about that?"
    scene d11katvisit36 with dissolve
    pc "No you didn't, and it would've been nice to get that information a little earlier."
    scene d11katvisit37 with dissolve
    t "Well, my bad, I guess."
    scene d11katvisit38 with dissolve
    pc "Yeah, I can tell you're incredibly sorry..."
    scene d11katvisit39 with dissolve
    t "You should be happy I even told you about it, because technically it falls under medical discretion."
    scene d11katvisit40 with dissolve
    pc "Yeah, yeah. Technically you should sit down if you want to have a serious conversation."
    scene d11katvisit41 with dissolve
    t "Technically, you still didn't answer my question."
    scene d11katvisit42 with dissolve
    pc "Will you sit down if I answer your question?"
    scene d11katvisit43 with dissolve
    t "Maybe."
    scene d11katvisit44 with dissolve
    pcthink "Jeez..."
    pc "Alright, I'm really not in the mood for that shit today, so yeah, I'll probably stay, but even if I decide to move, I'll stay in town and in touch."
    scene d11katvisit45 with dissolve
    t "Huh..."
    pc "..."
    scene d11katvisit46 with dissolve
    pc "You didn't expect that answer, huh?"
    scene d11katvisit47 with dissolve
    t "I... didn't expect anything..."
    scene d11katvisit48 with dissolve
    pc "Will you sit down now?"
    scene d11katvisit49 with dissolve
    t "Actually... I don't have any more questions..."
    if tc:
        jump d11tfirsts
    else:
        pc "Huh?! You came this early, just to ask a few questions?"
        scene d11katvisit50_e1 with dissolve
        t "Well, I didn't know if you'd cooperate."
        scene d11katvisit50_e2 with dissolve
        pc "Sure, now it's my fault, huh?"
        scene d11katvisit50_e3 with dissolve
        t "Well, I got what I came here for, I'll be waiting in the living room. Have fun with your little stalker over there..."
        pc "Huh?"
        scene d11katvisit166_ with dissolve
        pc "[j]?"
        scene d11katvisit167 with dissolve
        j "..."
        scene d11katvisit168 with dissolve
        play audio "audio/door-opening.ogg"
        pause .5
        scene d11katvisit50_e4 with dissolve
        play audio "audio/door-closing.ogg"
        pause .5
        pcthink "Ugh, god damn..."
        scene black with slowdissolve
        
    jump d11evening
    
label d11tfirsts:
    if _in_replay:
        show screen endRep
    scene d11katvisit50 with dissolve
    pc "..."
    scene d11katvisit51 with dissolve
    pc "Come here."
    scene d11katvisit52 with dissolve
    t "W-Why?"
    scene d11katvisit53 with dissolve
    pc "[t]..."
    scene d11katvisit54 with dissolve
    t "..."
    scene d11katvisit55 with dissolve
    pause .7
    scene black with dissolve
    scene d11katvisit56 with dissolve
    pause .7
    t "Why are you doing this..."
    scene d11katvisit57 with dissolve
    t "I told you I'm not going to be the fifth wheel."
    pc "And I told you, you're not going to be the fifth wheel, or the third wheel, or whatever you want to call it."
    scene d11katvisit58 with dissolve
    pc "Look, I don't know what you're really looking for, and I'm not even sure you know it yourself..."
    scene d11katvisit59 with dissolve
    t "I..."
    pc "{b}BUT{/b} we both know that whatever there is between us, we both enjoy it, and that's the important part."
    pc "If you want more than that, then I'm willing to try, but ultimately, that's your decision. You just have to make up your mind."
    scene d11katvisit60 with dissolve
    if pcgender == "man":
        t "Why do you even think I'd be interested in someone like you?"
        scene d11katvisit61 with dissolve
        pc "Someone like me, huh? If you think {b}that{/b} bad of me, then I wonder why you're sitting on my lap."
    else:
        t "Why do you even think I'd be interested in someone like you? Or a women at all."
        scene d11katvisit61 with dissolve
        pc "If you'd think {b}that{/b} bad of me, then I wonder why you're sitting on my lap."
    scene d11katvisit62 with dissolve
    t "T-That's just... because you made me."
    scene d11katvisit63 with dissolve
    pc "As I said..."
    scene d11katvisit64 with dissolve
    pc "You just have to make up your mind."
    scene d11katvisit65 with dissolve
    t "..."
    scene d11katvisit66 with dissolve
    pc "..."
    pc "You know... I have a theory."
    scene d11katvisit67 with dissolve
    t "A theory?"
    pc "Yeah, hug me."
    scene d11katvisit68 with dissolve
    t "W-What? Why?!"
    scene d11katvisit69 with dissolve
    pc "Just hug me."
    scene d11katvisit70 with dissolve
    t "No? Why would I?"
    pc "To disprove my theory."
    scene d11katvisit71 with dissolve
    t "I don't even know what theory!"
    scene d11katvisit72 with dissolve
    pc "Well, you're quite cold to other people..."
    scene d11katvisit73 with dissolve
    t "I'm not cold!"
    scene d11katvisit74 with dissolve
    pc "...and you basically told me that your parents were cold as well."
    scene d11katvisit75 with dissolve
    t "I never said that they were cold!"
    scene d11katvisit76 with dissolve
    pc "No, not directly, but indirectly."
    pc "You said they were very strict, and you had to study all the time, so I don't think your childhood was really the warmest either."
    scene d11katvisit79 with dissolve
    t "It was very warm!"
    scene d11katvisit76 with dissolve
    pc "Sure... did your parents cuddle with you regularly? Did you get many hugs from from them?"
    scene d11katvisit77 with dissolve
    t "Don't act like you're the therapist now!"
    scene d11katvisit78 with dissolve
    pc "Am I wrong?"
    scene d11katvisit80 with dissolve
    t "..."
    scene d11katvisit81 with dissolve
    pc "Just one hug to disprove my theory."
    scene d11katvisit80 with dissolve
    t "..."
    scene d11katvisit82 with vpunch
    pause .3
    scene d11katvisit83 with dissolve
    t "There... happy now?"
    scene d11katvisit84 with dissolve
    pc "What?! That wasn't a hug, you just bumped into me."
    scene d11katvisit85 with dissolve
    t "Of course, it was a hug, what are you talking about?"
    scene d11katvisit86 with dissolve
    pc "A hug doesn't just take a millisecond."
    scene d11katvisit85 with dissolve
    t "It was more than a millisecond!"
    scene d11katvisit86 with dissolve
    pc "Yeah, slightly..."
    scene d11katvisit87 with dissolve
    t "Ugh... fine..."
    scene d11katvisit82 with vpunch
    t "..."
    $ campov = False
    $ pov1 = "d11katvisit82"
    $ pov2 = "d11katvisit88"
    $ povstart = True
    show screen povscreen(pov1)
    pause
    t "Is that long enough now, or how long do we need to do this to disprove your stupid theory?"
    pc "As long as it takes."
    t "As long as {b}what{/b} takes?"
    pc "Does it make you feel so uncomfortable? You're not even really hugging me?"
    t "I {b}am{/b} hugging you!"
    pc "So, is it comfortable?"
    t "I... it's awkward..."
    pc "That's just because you're thinking too much about it, you need to relax."
    t "Easy for you to say..."
    pc "Well, I guess I'll need to help you relax, then."
    t "What are you..."
    scene d11katvisit82
    hide screen povscreen with dissolve
    hide screen povbutton
    scene d11katvisit89 with dissolve
    pause .3
    scene d11katvisit90 with hpunch
    t "Whaaa!"
    pc "Just relax and keep hugging me."
    t "T-That's not going to help me relax!"
    pc "Try it."
    t "Ugh..."
    scene d11katvisit91 with dissolve
    t "Just hurry up."
    pc "As you wish."
    scene d11katvisit92a with dissolve
    t "Nh-hnn..."
    pause
    pc "Are you relaxing?"
    t "I-I told you it's not going to hn...help."
    pc "Are you even trying?"
    t "You try mhh... relaxing while being molested."
    pc "I'm just caressing you."
    t "Call it how you want, I...nhh don't care."
    pc "Hmm... I guess we should try something else then."
    scene d11katvisit93 with dissolve
    t "What's the point anyway?"
    scene d11katvisit94 with dissolve
    pc "As I said, to get you to relax."
    scene d11katvisit95 with dissolve
    t "As if..."
    scene d11katvisit94 with dissolve
    pc "Take your top off."
    scene d11katvisit96 with dissolve
    t "Tch... and how would that help?"
    scene d11katvisit97 with dissolve
    pc "You obviously have no idea how to relax, so just do what I'm saying, [t]."
    scene d11katvisit98 with dissolve
    t "Pff..."
    scene d11katvisit99 with dissolve
    t "..."
    extend "."
    extend "."
    extend "."
    scene d11katvisit100 with dissolve
    pause .7
    play sound "audio/clothing-rustle-c1.ogg"
    scene d11katvisit101 with dissolve
    play sound "audio/clothing-rustle-c2.ogg"
    pause 1
    play sound "audio/clothing-rustle-c3.ogg"
    scene d11katvisit102 with dissolve
    pause 1
    scene d11katvisit103 with dissolve
    pc "That's better, isn't it?"
    scene d11katvisit104a with dissolve
    t "You really can't think of anything else, can you?"
    if pcgender == "woman":
        t "...dyke."
    scene d11katvisit105 with dissolve
    pc "I'm just trying to prove or disprove my theory."
    scene d11katvisit106 with dissolve
    t "Hmph..."
    scene d11katvisit104a with dissolve
    if pcgender == "woman":
        pc "Also, calling me a dyke won't hide the fact that you're interested in women..."
    pc "We've done this several times already, and you're still turning red like a tomato."
    t "T-That's not true..."
    pc "Do you want me to take a photo to show you?"
    t "N-No, don't you dare take a photo of me!"
    if pcgender == "man":
        pc "You should really be a bit more comfortable with your boyfriend."
    else:
        pc "You should really be a bit more comfortable with your girlfriend."
    t "That's not even...{w=0.5}{nw}"
    scene d11katvisit107 with dissolve
    pc "Come, turn around."
    scene d11katvisit108 with dissolve
    t "What are you..."
    scene d11katvisit109 with dissolve
    pc "Trying to make it more comfortable for you."
    scene d11katvisit110 with dissolve
    t "Oh..."
    pc "It'll help you relax."
    scene d11katvisit111 with dissolve
    t "Hmph, just stop acting as if you're doing it for me."
    scene d11katvisit113ma2 with dissolve
    pc "You think I'm doing this for myself?"
    t "Of course you do."
    scene d11katvisit114 with dissolve
    pc "Oh really? Well I guess there's no point in going on then..."
    scene d11katvisit112 with dissolve
    t "You... you're just going to stop now?"
    pc "Yeah, unless you want me to go on."
    scene d11katvisit115 with dissolve
    t "Hmph..."
    extend "."
    extend "."
    scene d11katvisit116 with dissolve
    t "..."
    scene d11katvisit117 with dissolve
    t "Fine..."
    scene d11katvisit118 with dissolve
    pc "Fine what?"
    scene d11katvisit119 with dissolve
    t "I'm going to play your stupid game..."
    pc "My stupid game?"
    scene d11katvisit120 with dissolve
    t "..."
    scene d11katvisit121 with dissolve
    pc "Hm?"
    scene d11katvisit122 with dissolve
    t "Just take it off already..."
    scene d11katvisit123 with dissolve
    pc "You mean my pants? Didn't you just say..."
    scene d11katvisit124 with dissolve
    t "Just do it already."
    pc "Well, if you insist..."
    scene black with dissolve
    play sound "audio/clothing-rustle-c2.ogg"
    pause 1
    play sound "audio/clothing-rustle-c3.ogg"
    pause 1
    scene d11katvisit125 with dissolve
    pc "There we go."
    scene d11katvisit126 with dissolve
    t "..."
    scene d11katvisit127 with dissolve
    pause .7
    play sound "audio/clothing-rustle-c4.ogg"
    scene d11katvisit128 with dissolve
    pause .5
    scene d11katvisit129 with dissolve
    t "..."
    if pcgender == "man":
        scene d11katvisithj1_00 with dissolve
        scene khj2bj with dissolve
        pause 30.2
        scene d11katvisithj11_1_00
        $ campov = False
        $ pov1 = "khj10_1"
        $ pov2 = "khj10_2"
        $ povstart = True
        show screen povscreen(pov1)
        pause
        pc "Not bad, [t]... not bad."
        $ pov1 = "khj11_1"
        $ pov2 = "khj11_2"
        hide screen povscreen
        hide screen povbutton
        if campov:
            show screen povscreen(pov2)
        else:
            show screen povscreen(pov1)
        pause 5.9
        $ pov1 = "khj14_1"
        $ pov2 = "khj14_2"
        hide screen povscreen
        hide screen povbutton
        if campov:
            show screen povscreen(pov2)
        else:
            show screen povscreen(pov1)
        pause
        pcthink "Damn, this looks uncomfortable..."
        pcthink "...and it doesn't feel that great either..."
    else:
        scene kli1 with dissolve
        pause
        scene kli2 with dissolve
        pause 5.2
        $ campov = False
        $ pov1 = "kli3"
        $ pov2 = "kli4"
        $ povstart = True
        show screen povscreen(pov1)
        pc "Hmm, not bad, [t], not bad..."
        pause
    scene d11katvisit130
    hide screen povscreen with dissolve
    hide screen povbutton
    pc "Alright, [t], get up."
    scene d11katvisit131 with dissolve
    t "W-Why?! Did I do something wrong?"
    scene d11katvisit132 with dissolve
    pc "Just do what I said."
    scene d11katvisit133 with dissolve
    t "You didn't even cum, yet..."
    pc "As I said, it's not about me."
    scene d11katvisit134 with dissolve
    t "Fine... what do you want now?"
    scene d11katvisit135 with dissolve
    pc "Take your pants off."
    scene d11katvisit136 with dissolve
    t "..."
    scene black with dissolve
    play sound "audio/clothing-rustle-c2.ogg"
    scene d11katvisit137 with dissolve
    pause .7
    scene d11katvisit138 with dissolve
    play sound "audio/clothing-rustle-c3.ogg"
    pause 1
    scene d11katvisit139 with dissolve
    t "What now?"
    scene d11katvisit140 with dissolve
    if pcgender == "man":
        pc "Sit on my lap."
        scene d11katvisit141 with dissolve
        t "W-What?! I'm not going to sit on your dick!"
        scene d11katvisit142 with dissolve
        pc "You just had it in your mouth, what's the problem with sitting on it?"
        scene d11katvisit143 with dissolve
        t "That's something different..."
        pc "Are you scared it could accidentally enter the wrong hole?"
        t "It could accidentally enter any hole!"
        scene d11katvisit144 with dissolve
        pc "Heh... come here."
    
        scene black with dissolve
        scene d11katvisit145 with dissolve
        pc "See? It's not that... hard, right?"
        t "..."
        scene d11katvisit146 with dissolve
        pc "Alright, why don't you grind on it?"
        t "Just grind?"
        pc "Just grind."
        scene d11katvisit147 with dissolve
        t "Okay..."
        scene kgrind1 with dissolve
        t "Like this?"
        pc "Yeah."
        $ campov = False
        $ pov1 = "kgrind1"
        $ pov2 = "kgrind3"
        $ povstart = True
        show screen povscreen(pov1)
        pause
        t "Nh..."
        pc "Are you comfortable?"
        t "Hnn... what kind of question is that?!"
        pc "Hey, I'm just making sure it's feeling good for you."
        t "It's... okay..."
        pc "Come on, [t]."
        t "Ugh... it's, nhh... it's good..."
        pc "Do you like it, or not?"
        t "C-Can you shut up?"
        pc "Being bitchy again, huh?"
        t "I'm not bitchy!"
        pc "Alright, a little bit higher, [t]."
        t "..."
        scene d11katvisit148_1_00
        hide screen povscreen with dissolve
        hide screen povbutton
        scene kinsert1 with dissolve
        pause .5
        t "Like this?"
        pc "Higher."
        scene kinsert2 with dissolve
        pause .5
        pc "A little more."
        t "N-Nhhn..."
        scene kinsert3 with dissolve
        pause 1
        t "Haah!"
        pc "Oh, looks like it almost slipped in... accidentally."
        scene d11katvisit152 with dissolve
        t "A-Accidentally? As if you didn't plan to do this."
        scene d11katvisit153 with dissolve
        pc "Heh, it was totally by accident, but... what are we going to do about it?"
        scene d11katvisit154 with dissolve
        t "Hmrph..."
        scene d11katvisit155 with dissolve
        t "..."
        scene d11katvisit156 with dissolve
        t "Nh..."
        scene kinsert4 with dissolve
        pause .5
        t "Haah..."
        scene d11katvisit160_000_i with dissolve
        pcthink "Wow, I didn't expect her to just slide it in."
        scene d11katvisit161 with dissolve
        pc "Looks like you accidentally slid down, [t]."
        scene d11katvisit162 with dissolve
        t "Humph..."
        pc "*Smirks* go on."
        scene d11katvisit157 with dissolve
        t "..."
        scene d11katvisit161 with dissolve
        pause .5
        $ campov = False
        $ pov1 = "kf1"
        $ pov2 = "kf3"
        $ povstart = True
        show screen povscreen(pov1) with dissolve
        t "N-Nhh..."
        pause
        scene kf2
        hide screen povscreen with dissolve
        hide screen povbutton
        pc "Are you finally relaxing?"
        t "If...hnnhh... you want to call it that..."
        pc "It's just that you should be a bit more comfortable with your boyfriend."
        t "Nhhh... maybe..."
        pc "No objections to the boyfriend part?"
        t "N-Nhnn..."
        $ campov = False
        show screen povscreen(pov1) with dissolve
        pause
        
        scene d11katvisit163
        hide screen povscreen with dissolve
        hide screen povbutton
    else:
        pc "Come closer, let me get a nice, close look between your sexy legs."
        t "..."
        scene black with dissolve
        scene d11katvisit145_f with dissolve
        t "I-I don't know if that's a good idea..."
        scene d11katvisit146_f with dissolve
        pc "Don't worry, I'll hold you."
        scene d11katvisit162_f with dissolve
        t "Nh..."
        scene d11katvisit147_f with dissolve
        pause .5
        pc "Mhm, Looks tasty."
        t "Just make sure you won't let me fall."
        scene d11katvisit162_f with dissolve
        pc "Do you really think I'd let my girlfriend fall?"
        t "..."
        pc "No objections to the girlfriend part?"
        scene d11katvisit163_f with dissolve
    pause .3
    scene d11katvisit164 with dissolve
    t "Huh?"
    scene d11katvisit165 with hpunch
    t "WHAAH!"
    if jlo < 3:
        $ renpy.end_replay()
    pc "What the!?"
    stop music fadeout 2
    scene d11katvisit166_ with dissolve
    pc "[j]?"
    scene d11katvisit167 with dissolve
    j "..."
    scene d11katvisit168 with dissolve
    t "God..."
    scene d11katvisit169 with dissolve
    t "I can't believe this, I..."
    scene d11katvisit170 with hpunch
    j "AU!"
    scene d11katvisit168 with dissolve
    pc "Shit..."
    scene d11katvisit171 with dissolve
    pc "I better have a look."
    t "Yes."
    scene black with dissolve
    play music mainbgm fadein 1
    scene d11katvisit172 with dissolve
    j "Damn..."
    scene d11katvisit173_0 with dissolve
    pc "What happened, are you okay?"
    scene d11katvisit173 with dissolve
    j "I'm okay, I just slipped from the railing..."
    pc "Well, that's what you get for peeping."
    scene d11katvisit174 with dissolve
    j "Hey, you were making weird noises, I was just checking..."
    scene d11katvisit174_ with dissolve
    pc "Yeah, sure... weird noises, huh..."
    scene d11katvisit175 with dissolve
    pc "Come on, you can go through my room."
    scene d11katvisit176 with dissolve
    t "..."
    scene d11katvisit177 with dissolve
    pause
    scene d11katvisit178 with dissolve
    j "Uhh... sorry for the interruption..."
    scene d11katvisit179 with dissolve
    t "Shouldn't you be mad or something?"
    scene d11katvisit180 with dissolve
    j "Uhh... should I?"
    if jlo >= 3:
        scene d11katvisit181 with dissolve
        if pcgender == "man":
            t "He's your boyfriend!"
        else:
            t "She's your girlfriend!"
        scene d11katvisit182 with dissolve
        j "And yours, too, right?"
    scene d11katvisit183 with dissolve
    pc "How long have you been watching?"
    scene d11katvisit184 with dissolve
    j "Uhh..."
    scene d11katvisit185 with dissolve
    if jlo >= 3:
        t "How can you be okay with that?!"
        scene d11katvisit186 with dissolve
        pc "I told you she'd be fine with it, didn't I?"
    else:
        t "How can you be okay with that?! [e] is your best friend!"
        scene d11katvisit186 with dissolve
        pc "I told you [e] would be fine with it, didn't I?"
    scene d11katvisit187 with dissolve
    t "Uch, you're both weird..."
    if jlo >= 3:
        scene d11katvisit188 with dissolve
        j "Hey."
        scene d11katvisit189_0 with dissolve
        j "How would you know that I'm fine with it?"
        scene d11katvisit189 with dissolve
        pc "Well, you basically said it yourself, on my second day here, after I got you and [e] from school, remember?"
        scene d11katvisit190 with dissolve
        j "Oh..."
        scene d11katvisit191 with dissolve
        j "Uh, hey, [t], you really don't need to put your clothes back on, I'll leave you two alone if you want."
    else:
        scene d11katvisit191 with dissolve
        j "Uh, hey, [t], you really don't need to put your clothes back on, I'll leave you two alone..."
    scene d11katvisit192 with dissolve
    t "No thanks, I'll just be leaving."
    scene d11katvisit193 with dissolve
    j "Aww, come on, don't leave. I'm sorry, okay?"
    scene d11katvisit194 with dissolve
    t "You two can do what ever you want, but I don't need to be part of it."
    scene d11katvisit195 with dissolve
    t "Just do me a favor and don't tell anyone what you've seen today..."
    scene d11katvisit196 with dissolve
    j "Of course not..."
    scene d11katvisit197 with dissolve
    j "I mean..."
    j "Uhh..."
    scene d11katvisit198 with dissolve
    j "That means you owe me something, right?"
    scene d11katvisit199 with dissolve
    if jlo >= 3:
        t "Ugh, you two really are a perfect match!"
    else:
        t "Ugh, you two would make a perfect couple!"
    scene d11katvisit200 with dissolve
    j "Hehe."
    scene d11katvisit201 with dissolve
    t "What do you want?"
    scene d11katvisit202 with dissolve
    j "Hey, don't be mad, I just want you to stay. You have an appointment with [e] anyway, don't you?"
    scene d11katvisit203 with dissolve
    t "Hmph... fine."
    scene d11katvisit204 with dissolve
    t "...but I'm just going to sit and wait until [e] is home for her therapy..."
    scene d11katvisit205 with dissolve
    pause 2
    scene d11katvisit206 with dissolve
    j "..."
    scene d11katvisit207 with dissolve
    j "Well, okay."
    scene d11katvisit208 with dissolve
    t "..."
    scene d11katvisit209 with dissolve
    j "What are you standing there like a lost sheep, come, sit between us!"
    scene d11katvisit210 with dissolve
    t "Ugh..."
    scene d11katvisit211 with dissolve
    if jlo >= 3:
        pause .5
        scene d11katvisit212 with dissolve
        j "Nothing better than cuddling with your girlfriendssss, right?"
        scene d11katvisit213 with dissolve
        pc "Heh, right."
        scene d11katvisit214 with dissolve
        pc "Wouldn't you say, too, [t]?"
    else:
        j "..."
    scene d11katvisit215 with dissolve
    t "*grml*"
    scene d11katvisit216 with dissolve
    pc "Come on, [t]."
    scene d11katvisit217 with dissolve
    pc "Shit happens sometimes, right?"
    scene d11katvisit218 with dissolve
    t "..."
    scene d11katvisit219 with dissolve
    if pcgender == "man":
        j "Come on, [t], there's nothing wrong with having fun with your boyfriend."
    else:
        j "Come on, [t], there's nothing wrong with having fun with your girlfriend."
    if jlo >= 3:
        scene d11katvisit220 with dissolve
        pc "Err..."
    j "I won't tell anybody, promise."
    if jlo >= 3:
        pcthink "Damn, [j] is such a naughty little..."
    play sound "audio/door-closing_muffled.ogg"
    pause .3
    scene d11katvisit221 with dissolve
    pc "Sounds like [m] and [e] are back."
    scene d11katvisit222 with dissolve
    t "Good, time to do my job."
    scene d11katvisit223 with dissolve
    if jlo >= 3:
        pause .5
        scene d11katvisit223_2 with dissolve
        j "She has a really nice ass in those pants."
        t "Hmph..."
        play sound "audio/door-opening.ogg"
        scene d11katvisit224 with dissolve
        play sound "audio/door-closing.ogg"
        pause .5
        j "No wonder you like her."
        scene d11katvisit225 with dissolve
        j "Too bad [e] and [m] just came back home."
        scene d11katvisit226 with dissolve
        pc "I doubt that them coming home changed much."
        scene d11katvisit227 with dissolve
        j "Aww, sorry, I'll be more careful next time."
        scene d11katvisit228 with dissolve
        pc "More careful? You shouldn't peep in the first place."
        scene d11katvisit229 with dissolve
        j "Hrm..."
        pc "Seriously, [j]."
        scene d11katvisit230 with dissolve
        j "Sorry, I won't do it again."
        scene d11katvisit231 with dissolve
        pc "I hope so, otherwise I'll have to punish you, young lady."
        scene d11katvisit232 with dissolve
        j "Hehe, don't tempt me, [pcmd]."
        scene d11katvisit233 with dissolve
        pc "But seriously, [j], don't do it again, unless you know everyone is fine with it."
        scene d11katvisit234 with dissolve
        j "I won't, promise."
    else:
        j "She has a really nice ass in those pants."
        t "Hmph..."
        play sound "audio/door-opening.ogg"
        scene d11katvisit224_2 with dissolve
        play sound "audio/door-closing.ogg"
        j "No wonder you like her."
        j "Too bad [e] and [m] just came back home."
        scene d11katvisit224_3 with dissolve
        pc "I doubt that them coming home changed much."
        scene d11katvisit224_4 with dissolve
        j "Sorry, I guess I..."
    play sound "audio/door-opening.ogg"
    pause .5
    scene d11katvisit235 with dissolve
    j "Hey, [e], welcome back."
    scene d11katvisit236 with dissolve
    t "Come on, [e], I don't have much time..."
    scene d11katvisit237 with dissolve
    t "Ugh, are you still..."
    scene d11katvisit238 with dissolve
    e "Huh?"
    scene d11katvisit239 with dissolve
    m "Hey, what's going..."
    scene d11katvisit240
    m "O-Oh... err..."
    scene d11katvisit241 with dissolve
    m "Come on, [e], [t] is waiting for you."
    e "Whaa..."
    if jlo < 3:
        scene d11katvisit224_5 with dissolve
        pc "Shit, I better put my pants on."
        j "Yeah... sorry..."
        scene d11katvisit224_6 with dissolve
        j "...I'll go see if [m] needs help with anything..."
        pc "Sure..."
    else:
        scene d11katvisit242 with dissolve
        pc "Shit, I better put my pants on."
        j "yeah... too bad..."
        scene d11katvisit243 with dissolve
        pc "Well, at least they didn't see me and [t]."
        scene d11katvisit244 with dissolve
        j "Hehe, yeah, that might've ended up worse than it did."
        scene d11katvisit245 with dissolve
        pc "Yeah..."
        j "Too bad [m] isn't okay with us, yet, this could've ended up in a nice little orgy."
        scene d11katvisit246 with dissolve
        pc "Damn, [j]..."
        scene d11katvisit247 with dissolve
        j "What?"
        scene d11katvisit248 with dissolve
        pc "What do mean by \"yet\" by the way?"
        scene d11katvisit249 with dissolve
        j "Well, we obviously need to convince her to join your little harem, right?"
        scene d11katvisit250 with dissolve
        pc "My harem? Why do I get the feeling that that's more like what {b}you{/b} want?"
        scene d11katvisit251 with dissolve
        j "Nah, that'd be too much work for me..."
        scene d11katvisit252 with dissolve
        pc "Oh, so you let me do all the hard work."
        scene d11katvisit253 with dissolve
        j "Hey, I'm trying to help you! Also, it's not only hard, but also juicy, isn't it?"
        scene d11katvisit254 with dissolve
        pc "Heh, well, kind of."
        scene d11katvisit255 with dissolve
        j "See? And it's not like I'm not doing my part, hehe."
        $ renpy.end_replay()
        scene d11katvisit256 with dissolve
        pc "Yeah... and you really are okay with that?"
        scene d11katvisit257 with dissolve
        j "Yeah, sure, I mean..."
        scene d11katvisit258 with dissolve
        j "..."
        scene d11katvisit259 with dissolve
        pc "[j]?"
        scene d11katvisit260 with dissolve
        j "Err... yeah, haha."
        scene d11katvisit261 with dissolve
        j "Absolutely!"
        scene d11katvisit262 with dissolve
        pc "..."
        scene d11katvisit263 with dissolve
        j "..."
        scene d11katvisit263_2 with dissolve
        j "Well..."
        scene d11katvisit264 with dissolve
        j "...I'll go see if [m] needs help with anything..."
        scene d11katvisit265 with dissolve
        j "..."
        scene d11katvisit266 with dissolve
        play sound "audio/door-closing.ogg"
        pause .5
        pcthink "Is she lying?"
        pcthink "But why would she say she's okay with it, if she's not okay with it?"
    scene black with slowdissolve

    jump d11evening