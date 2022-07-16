######### Jada
label jadaFirstMeet:
    pcthink "I'm a bit hungry."
    pcthink "Let's have a look in the fridge."
    pcthink "I wonder if [m] and [e] are back already..."
    scene black with dissolve
    n "You open the door and..."
    scene hall jada crash with dissolve
    "Girl" "Owww..." with hpunch
    pc "Fuck!"
    scene hall jada after crash with dissolve
    pcthink "Huh? Who is she?"
    pc "Ugh! Are you okay?"
    "Girl" "Uhh... yeah... I-I guess."
    pc "Sorry, I didn't see you."
    "Girl" "No, I'm sorry, I didn't expect somebody coming out of this room."
    scene hall jada after crash smile with dissolve
    "Girl" "I'm [j] by the way. You're [e]'s big [bs], right?"
    pc "Yes, [pc]."
    j "Nice to meet you, [pc]."
    pc "Nice to meet you too, [j]... and what are you doing here?"
    j "I'm [e]'s classmate. I'm helping her out with homework from time to time."
    pc "Really?! That's nice... I bet it's not easy."
    j "It's fine. We're friends, after all."
    pcthink "Friends huh? I thought someone like [e] wouldn't have any..."
    pc "Cool. Well I don't want to keep you then."
    j "Hehe, thanks."
    j "Later [pc]."
    pc "Yeah, later."
    scene hall jada back with dissolve
    pcthink "Hm... [e]'s classmate? She looks older than [e]..."
    scene hall jada back2 with dissolve
    pcthink "...uff... what a gap!"
    scene hall jada look back with dissolve
    pause
    scene home_hall_idle with dissolve
    j "{size=-10}{i}Hey [e], you should have told me that your [bs] looks so cute!{/i}{/size}"
    pcthink "WTF! She clearly wanted me to hear that!"
    scene home_hall_entrance_idle with dissolve
    play music mainbgm fadein 1
    pcthink "Little minx!"
    jump mTellNotToDisturb


label flirtyJ:
    play music mainbgm fadein 1
    scene pcroomflirtyj1 with dissolve
    pcthink "Alright, time to ask [m] some serious questions..."
    play sound "audio/door-opening.ogg"
    scene pcroom flirtyj1surprise with hpunch
    j "Hey!{w=.5}{nw}"
    pc "Whoa what the!?"
    scene pcroom flirtyj1surprise2 with dissolve
    j "Did I scare you? Hehe..."
    pc "Damn [j]!"
    scene pcroom flirtyj1surprise3 with dissolve
    j "I'm going to leave..."
    play sound "audio/door-closing.ogg"
    scene pcroom flirtyj1surprise4 with dissolve
    pc "Okay, but... the exit isn't in my room you know."
    scene pcroom flirtyj1surprise5 with dissolve
    j "Hehe, I know that, stupid!"
    j "But I have a question to ask..."
    pcthink "Damn, I bet it's going to be something naughty again..."
    pc "Well what is it?"
    j "Hehe... are you..."
    scene pcroom flirtyj1surprise6_2 with dissolve
    j "...going to..."
    scene pcroom flirtyj1surprise8 with dissolve
    j "...break her heart again?!"
    pc "Eh... what?!"
    scene pcroom flirtyj1surprise7 with dissolve
    j "You know what I mean!"
    j "Are you going to stay!? In this house, in this town, in this country?"
    j "Or are you going to move away again and leave her alone a second time!"
    pc "Err... well..."
    pcthink "Damn I didn't expect that kind of question. What the hell..."
    pcthink "\"Leave her alone a second time\"?"
    pcthink "[e] must have told her that I left in the middle of night without telling anyone back then..."
    pcthink "Shit, I almost forgot that..."
    scene pcroom flirtyj1surprise6 with dissolve
    j "So? Don't you want to answer?"
    pc "Err.... Listen... I know I should have told her that I was leaving, but..."
    pc "...well I don't know how much you know about the circumstances..."
    j "Enough..."
    pc "Okay... you know, I felt terrible for months after I left."
    j "Good, at least you felt guilty..."
    pc "Well I can assure you that it's nothing that's ever going to happen again."
    pc "Even if I'm not going to stay in this house, I will stay in town and I'm not going to run out of the house in the middle of the night."
    j "Hum..."
    scene pcroom flirtyj1surprise7 with dissolve
    j "Okay, I believe you."
    scene pcroom flirtyj1surprise6_2 with dissolve
    j "But if you ever break her heart, I'm going to declare war!"
    pc "Err..."
    pc "War isn't a game."
    j "Hmm... are you sure life isn't a game, Soldier? Hehe."
    pc "Haha, that's {b}{i}sir{/i}{/b} to you."
    scene pcroom flirtyj1surprise9 with dissolve
    j "Hehe, nice try!"
    j "Anyway, I gotta go."
    scene pcroom flirtyj1surprise10 with dissolve
    j "Umm... sorry for the serious stuff, but she was really happy when you came back and I don't want to see her sad again..."
    pc "Yeah, understandable... neither do I."
    scene pcroom flirtyj1surpriseleave with dissolve
    j "Good, seeya tomorrow~!"
    pc "Seeya..."
    play sound "audio/door-closing.ogg"
    scene pcroom door close with dissolve
    pc "..."
    pcthink "Shit... Did me leaving have such an impact on her?"
    pcthink "I can't even imagine how [e] felt when I left..."
    pcthink "I think I should really talk to her..."
    pcthink "Damn, but first things first. I have to get some answers from [m]!"
    scene black with dissolve
    $ storyEvent = True
    $ SErachelPills3rd = True
    call screen map_home_hall_entrance
    
label JVREbirthday:
    if _in_replay:
        show screen endRep
    scene black with fade
    n "a while later" with dissolve
    stop music fadeout 2
    window hide
    pause 2
    "{color=#570058}Girl1{/color}" "AHN, AH, HA, HAA..."
    image vrporn3_30 = Movie(play="anim/porn_VR3_30.webm")
    scene vrporn3_30 with dissolve
    pause
    pcthink "Damn this is so hot!"
    "{color=#570058}Girl1{/color}" "HAA, HA, NHHH!"
    "{color=#cc5dcd}Girl2{/color}" "Yeees, fuck [himher], fuck [himher] \"Landlady\"!"
    pcthink "Ugh... when did they start doing this in porn?"
    "{color=#570058}Girl1{/color}" "Haa, Yes! Babe, I'm close!"
    image vrporn3_60 = Movie(play="anim/porn_VR3_60.webm")
    scene vrporn3_60 with dissolve
    pc "Shit, it's still hot!"
    "Voice" "Holy shit, it's {i}really{/i} hot!"
    "{color=#570058}Girl1{/color}" "HAA, HAA, HNAAH! YES! OH YES!"
    "{color=#cc5dcd}Girl2{/color}" "She's going to cum!"
    pc "Yeah babe, cum for me!"
    "Voice" "Yeah, cum for us!"
    pc "Eh?!"
    scene black with dissolve
    pc "What the!?"
    scene pcroomebd_jadavr1 with dissolve
    pc "[j!u]!"
    $ renpy.end_replay()
    play music mainbgm fadein 1
    scene pcroom ebd_jadavr2 with dissolve
    j "Oh, err... "
    scene pcroom ebd_jadavr3 with dissolve
    j "Hi!"
    pc "What the fuck? What are you doing here?"
    scene pcroom ebd_jadavr4_2 with dissolve
    j "It's [e]'s birthday? Silly..."
    pc "I mean, what are you doing in my room?"
    scene pcroom ebd_jadavr4 with dissolve
    j "Looking for you of course, what else would I do here?"
    pc "Wait... I locked the door, how did you get in?"
    scene pcroom ebd_jadavr4_2 with dissolve
    j "The balcony."
    pc "The balcony? ...seriously?"
    j "Yeah, [m] told me you're home. I knocked on your door, but you didn't react and I got curious so I let myself in."
    pc "...you're crazy, and that's actually quite rude, you know that?"
    scene pcroom ebd_jadavr4 with dissolve
    j "Hehe, that makes us the perfect couple, doesn't it?"
    pc "Err..."
    j "Hahaha, I'm joking... maybe, hehe."
    j "Anyway, I wanted to show you something I bought for today, but you have to promise not to tell anyone..."
    pc "What is it?"
    scene pcroom ebd_jadavr6 with dissolve
    j "Wait a sec..."
    pcthink "Damn, why must she always tease me like this..."
    scene pcroom ebd_jadavr6_2 with dissolve
    j "Tadaaa~"
    pc "Booze?"
    j "Shh... [m] mustn't hear about it!"
    pc "I'm sure [m] wouldn't mind. It's [e]'s birthday and she used to drink a lot herself back in the day..."
    scene pcroom ebd_jadavr6_3 with dissolve
    j "Oh you don't know?"
    pc "Don't know what?"
    scene pcroom ebd_jadavr8 with dissolve
    j "She is a freaking booze hater now."
    pc "What?! Really?"
    j "Yeah, she doesn't even use cough syrup, because it used to have alcohol in it."
    pc "Wow, I didn't know."
    pcthink "Now that she mentioned it, I haven't seen [m] drink any alcohol since I've been back..."
    j "That's why I'm telling you, hehe."
    pcthink "Looks like some things really changed..."
    pc "So, what's your plan?"
    j "Well, I'm sure [m] made her famous {size=-10}{i}boring{/i}{/size} fruit punch again."
    j "Don't get me wrong, it tastes awesome, but it's without alcohol and that's where this nice little bottle comes into play, hehe."
    pc "Don't you think she'll taste the difference?"
    j "Naah, this stuff doesn't really have its own taste, its just sweet and it fits the punch's flavor perfectly."
    pc "...and you want me to help you with that."
    j "Nah, I have a plan, hehe."
    pc "Somehow I have the feeling that this won't end well..."
    j "Awww, come on, don't be a spoilsport! No one will notice anything. I'll have everything under control."
    pc "Until they get drunk."
    j "Maybe, but by then it's too late anyway, hehe."
    pc "Why did you tell me about it if you don't need my help anyway?"
    j "Because it's more fun with a partner in crime and... I might need someone to drive me home later... hehe."
    pc "So THAT's the reason. You want me to stay sober..."
    scene pcroom ebd_jadavr7 with dissolve
    j "Well I could stay overnight if you're willing to share the bed, hehe."
    j "Buuuut I'm not sure how everyone would react when I come out of your room in the morning... naked... and sweaty... hehe."
    pcthink "Holy shit!"
    j "Talking of naked and sweaty, why don't you let me have a look through your headset?"
    scene black with fade
    j "Shit, these girls are HOT!"
    scene pcroom ebd_jadavr9 with dissolve
    pc "Uhuh..."
    pause
    pc "You like girls don't you?"
    j "Oh, how did you know, hehe."
    pc "It wasn't {i}really{/i} a question..."
    if pcgender == "man":
        j "But don't worry, I'm not exclusively into woman, hehe."
        scene pcroom ebd_jadavr9_1 with dissolve
        pc "Oh I {i}{b}really{/b}{/i} didn't notice that."
        j "Hehe."
    play sound "audio/knock-door1.ogg"
    n "*KNOCK* *KNOCK*"
    scene pcroom sitonchair door with dissolve
    m "[pc]? Why did you lock the door?"
    pcthink "Shit..."
    j "Uh-oh... should I hide under the bed?"
    scene pcroom ebd_jadavr9_2 with dissolve
    pc "Huh? No... why would you?"
    scene pcroom ebd_jadavr9_1 with dissolve
    j "Just asking, hehe."
    scene black with dissolve
    n "You quickly shut the laptop and open the door."
    scene pcroom ebd_rachel1 with dissolve
    m "[pc] what's the matter? Why did you..."
    scene pcroom ebd_rachel2 with dissolve
    m "Oh, [j], here you are..."
    j "Yeah... hey... hehe."
    m "..."
    pc "Err... what's up [m]?"
    scene pcroom ebd_rachel1 with dissolve
    m "Oh I... just wanted to ask if you could help me a bit with the decoration and maybe you want to try the punch?"
    j "{size=-15}I told ya...{/size}"
    pc "Uhh, yeah, why not..."
    scene black with fade
    
    jump ebdPreps
    
label ebdBringJadaHome:
    scene hall ebd jadaleaving1 with dissolve
    pc "You're leaving?"
    scene hall ebd jadaleaving2 with dissolve
    j "Yeah... I've screwed up enough for today..."
    pcthink "Wow, she's really down. I've never seen her like that..."
    pc "You're going to walk?"
    scene hall ebd jadaleaving3 with dissolve
    j "Yeah... it's still early in the evening, so I might catch a bus..."
    pc "It's a long way to the next bus stop."
    j "That's okay...a little walk might not be too bad..."
    menu:
        "Take her home":
            $ jlo +=1
            pc "Come on, I'll take you home."
            j "...really? Are you sure? After everything that happened?"
            pc "Yeah..."
            j "You're not going to lecture me? No \"I told you so\"?"
            pc "Would it change anything?"
            scene hall ebd jadaleaving2 with dissolve
            j "..."
            scene black with fade
            jump bringJadaHome
        "Don't take her home":
            pc "Yeah, some fresh air might be good for you..."
            j "You'll take care of them, will you?"
            pc "Of course."
            j "Okay... then... see you..."
            pc "Yeah, take care..."
            jump ebdEnd
    
label bringJadaHome:
    if _in_replay:
        show screen endRep
    n "a bit later" with dissolve
    window hide
    pause 2
    scene bringjadahome with dissolve
    pc "Would you answer me a question, [j]?"
    j "Sure."
    pc "You and [e], err..."
    j "We are just friends, don't worry, hehe."
    scene bringjadahome1 with dissolve
    pc "Eh? That's not what I wanted to ask..."
    pcthink "...but it's good to know anyway."
    j "Oh, well. Errm... we do naughty stuff sometimes, hehe."
    pcthink "What the..."
    pc "That's not what I wanted to ask either!"
    j "No?"
    pc "No! I wanted to know if she talks to you!"
    j "Hum..."
    j "She... loves you, you know?"
    pc "What the fuck, [j]. Did you even listen?"
    scene bringjadahome1_1 with dissolve
    j "Yes..."
    pc "Ugh..."
    pcthink "She's avoiding the question... I wonder why."
    pc "She's my sister, you know that..."
    j "Hehe, don't act like that would be a big problem for you."
    pc "..."
    pc "It's obviously not a problem for you?"
    j "Me and [e] have known each other for a loooong time now, I got used to the idea, hehe."
    pc "She told you a lot about me, didn't she?"
    j "Yeah, it's almost like I knew you all my life."
    pc "..."
    j "You know, I think that even [m] knows about it."
    pc "I highly doubt that..."
    j "Oh I don't! Maybe she doesn't want to admit it to herself, but I'm sure she's well aware about [e]'s feelings for you."
    pcthink "If that was true, she would've never let [e] sleep in my bed..."
    j "Aaaaaanyway... do you plan to hit on [m], too?"
    pc "What?!"
    j "Haha, come on, she is hot as fuck! I know you've checked her out."
    j "I'd eat that sexy ass too, hehe. But sadly she isn't interested in me. You on the other hand..."
    pc "I don't think she looks at me {i}{b}that{/b}{/i} way."
    j "Hehe, who knows..."
    pc "..."
    pcthink "She wouldn't look at me that way... would she?"
    j "..."
    scene bringjadahome1_3 with dissolve
    j "...you know..."
    j "..."
    pc "What?"
    j "...I know I can't compete with [e]'s cuteness or [m]'s goddamn hot and sexy milfy...ness..."
    j "But I really like you, so... I might have to go the NTR route..."
    pc "NTR?"
    j "Uhuuh!"
    scene bringjadahome2 with dissolve
    pc "Wait, what?! You want to fuck someone in front of me???"
    j "PWHAHAHA! You should see your face right now! Haha..."
    pc "..."
    scene bringjadahome4 with dissolve
    j "At least now I know that you don't want to see me with somebody else, hehe."
    pc "..."
    j "..."
    scene bringjadahome3 with dissolve
    pc "Are you sure this is the right way?"
    j "Sure... just go on."
    pc "..."
    scene bringjadahome3 with vpunch
    j "Whuuups~"
    scene bringjadahome5 with dissolve
    pc "Whoa!"
    scene bringjadahome6 with dissolve
    j "You should've avoided that hole in the street."
    pc "There was no hole!"
    j "I'm sure there was, why else would I slip down here, hehe."
    scene bringjadahome7 with dissolve
    if pcgender == "woman":
        j "Oh, you have some dirt on your skirt. I'll rub it away for you."
    else:
        j "Oh, you have some dirt on your pants. I'll rub it away for you."
    scene bringjadahome3 with dissolve
    pc "Shit, [j], I can't reach the gearshift like this."
    j "Don't worry, the road won't change for miles."
    pc "So this is {i}{b}not{/b}{/i} the right way. Sneaky little minx!"
    j "Hehe."
    j "Looks like I have to use my mouth, the dirt is really persistent."
    if pcgender == "man":
        n "*zip*"
    pcthink "Damn..."
    scene uh-oh with fade
    pause 2
    pcthink "Haha, yeah, if this was a game, this would be the right spot for a cliffhanger."
    scene bringjadahome3 with dissolve
    pcthink "Weird, that I have to think about that right now..."
    j "Hmmh... look at this beauty. I wonder how it tastes..."
    pc "Just try it out, I bet you'll like it."
    jump bjhpov
    
label bjhpov:
    hide screen scrbjhtrd
    scene bjhmovpov with dissolve
    show screen scrbjhpov
    pause
    pc "Damn it [j], you're good at this!"
    j "Mhm..."
    pause
    j "Hhmm..."
    pause
    if pcgender == "woman":
        pc "Haaa... gawd..."
    else:
        pc "Gawd..."
    j "Hnn...like it?"
    pc "Shit, yes!"
    pause
    pc "Fuck, I'm not going to last long..."
    pause
    if pcgender == "woman":
        pc "MHhhh... this is too good..."
    else:
        pc "I'm going to cum soon..."
    scene bringjadahome3 with dissolve
    hide screen scrbjhpov
    jump bjhcum
    
label bjhtrd:
    hide screen scrbjhpov
    scene bjhmovtrd with dissolve
    show screen scrbjhtrd
    pause
    pc "Shit! Clean it thoroughly [j]."
    j "Mhh..."
    pause
    pc "Do you like the taste?"
    j "Mhhhm!"
    pcthink "She definitely knows what she's doing down there, holy shit..."
    pause
    if pcgender == "woman":
        pc "MHhhh... this is too good..."
    else:
        pc "I'm going to cum soon..."
    scene bringjadahome3 with dissolve
    hide screen scrbjhtrd
    jump bjhcum
    
label bjhcum:
    scene bringjadahome3 with flash
    pcthink "Fuck "
    scene bringjadahome3 with flash
    extend "fuck "
    scene bringjadahome3 with flash
    extend "fuck!"
    pc "Gaaawd!"
    scene bjh2_00 with dissolve
    if pcgender == "woman":
        j "*Slurp*"
    else:
        j "*Gulp*"
    j "Hehe..."
    pc "Gawd, [j]..."
    if pcgender == "man":
        scene bringjadahome6_cum with dissolve
    else:
        scene bringjadahome6 with dissolve
    j "I hope you liked it, I did! Hehe."
    pc "Hell no!"
    j "Huh?!"
    pc "...I loved it."
    if pcgender == "man":
        j "Hehe, dickhead..."
        pc "By the way, you have some milk there, Kitten."
        j "Meow..."
    else:
        j "Hehe, bitch..."
    scene black with dissolve
    $ renpy.end_replay()
    n "[j] cleans up and tells you the right way to her home, she leans her head on your shoulders for the rest of the ride.{p}After a while you arrive at her home."
    j "Here we are~"
    pc "Looks nice."
    scene ebd jadahome1 with dissolve
    j "Yeah it's... decent..."
    j "Sorry, I'd {i}{b}love{/b}{/i} to invite you to cum inside, hehe, but my mom is..."
    "Jada's Mom" "[j]! Where the fuck have you been?!"
    scene ebd jadahome2 with dissolve
    j "Ugh..."
    "Jada's Mom" "I've been waiting for you all day!"
    j "{size=-10}Shit, I'd hoped she'd be asleep already...{/size}"
    scene ebd jadahome3 with dissolve
    "Jada's Mom" "I'm talking to you [j]!"
    pcthink "Hum... I think I've seen her somewhere before..."
    scene ebd jadahome4 with dissolve
    j "Mom! I'm nineteen, I'm not going to tell you every time I go out! You never cared anyway!"
    pcthink "Nineteen? She's older than [e]?"
    "Jada's Mom" "Oh we'll see about that!"
    j "Ugh..."
    if pcgender == "woman":
        scene ebd jadahome5 with dissolve
        "Jada's Mom" "... seriously [j], when do you plan to get yourself a boyfriend?!"
        j "MOM! I'm never going to have a stupid boyfriend!"
        "Jada's Mom" "Tch... get your lazy ass inside and don't make me come out here again..."
    else:
        scene ebd jadahome5_2 with dissolve
        "Jada's Mom" "Oh? Don't tell me you {i}{b}finally{/b}{/i} got yourself a boyfriend?!"
        j "MOM!"
        "Jada's Mom" "What? I've already started to think that you're one of those lesbians..."
        j "There is nothing wrong with that!"
        "Jada's Mom" "Whatever, move your ass inside and don't make me come out here again..."
    scene ebd jadahome2 with dissolve
    j "..."
    j "I'm sorry... she's usually in bed already at this time, but since she lost her job a few days ago..."
    pcthink "Oh, she's... {b}was{/b} the receptionist from the hotel."
    pc "Don't worry about it."
    pc "Will you be alright?"
    scene ebd jadahome6 with dissolve
    j "Yeah... thanks."
    scene ebd jadahome7 with dissolve
    pause 1
    j "*smooch*"
    scene ebd jadahome6 with dissolve
    if pcgender == "woman":
        j "I hope you like {i}{b}your{/b}{/i} taste, hehe. I definitely did!"
    j "Anyway, good night."
    pc "Yeah good night."
    scene ebd jadahome8 with dissolve
    j "Oh and... have fun tomorrow."
    pc "Huh?! What do you mean?"
    scene ebd jadahome9 with dissolve
    j "Good niiiight~ hehe..."
    pcthink "Damn, why does she have to be such a tease..."
    scene black with fade
    n "You head back home..."
    jump ebdEnd
    
label d6_wayBackHome:
    $ go_home = False
    scene black with fade
    n "On your way back home."
    scene pre_kandbf with dissolve
    pcthink "Damn, I should've taken the long way, who knew that the old shortcut doesn't exist anymore..."
    scene pre_kandbf2 with dissolve
    t "{size=-10}LEAVE ME ALONE!{/size}"
    pcthink "Huh? Wasn't that [t]'s voice?"
    stop music fadeout 2
    scene kandbf_pre_kick1 with dissolve
    "Man" "Come on [t], don't be like that. I've been waiting for so long and you still won't let me even touch you?"
    pcthink "Wow, someone like her has a boyfriend?"
    scene kandbf_pre_kick0 with dissolve
    t "I told you, I'm not ready yet!"
    pcthink "Ha, no wonder she gets off so fast..."
    scene kandbf_pre_kick2 with dissolve
    "Man" "Come on [t], I don't want to wait any longer."
    t "I don't care! Don't touch me!"
    "Man" "What the fuck [t], we've been together for 2 months!"
    t "Stop touching me, I'm warning you!"
    "Man" "You're warning me? Are you serious? What are you going to do, huh?!"
    pcthink "Looks like it's getting ugly... maybe I should help her..."
    scene kandbf_pre_kick with dissolve
    t "How about this!!!"
    scene kandbf_kick with dissolve
    t "Haaaaya!" with hpunch
    pcthink "Holy fuck!"
    t "How do you like that, asshole!"
    play sound "audio/honk.ogg"
    n "*Honk* *Honk*"
    play sound "audio/bike.ogg"
    scene after_kandbf with dissolve
    pc "Huh?{w=1}{nw}"
    scene after_kandbf2 with dissolve
    pcthink "What the?!{w=1}{nw}"
    play audio "audio/jbrake.ogg"
    scene jbikebrake at brakeshake with dissolve
    pause 1
    pc "Whoa!"
    pc "What the fuck! Are you crazy?!"
    scene after_kandbf4 with dissolve
    j "Haha, got you!"
    pc "[j]! What the..."
    t "{size=-10}...and don't you dare talk to me ever again, asshole!{/size}"
    scene kandbf_after_kick with dissolve
    pause 1
    pcthink "Damn, she could have easily knocked me out when I touched her... why didn't she?"
    j "What's going on there?"
    scene after_kandbf5 with dissolve
    pc "Err... just a guy who got his ass kicked by his girlfriend."
    scene after_kandbf6 with dissolve
    j "Really? Haha. I like the girlfriend already!"
    pc "What are you doing here, [j], and what about the bike? Don't tell me it's yours."
    j "This? Oh, no, it's not mine..."
    pc "You didn't steal it, did you?"
    j "Of course not! What do you think of me?"
    j "It's from my mom's ex, I... borrowed it, hehe."
    pc "Borrowed... why do I get the feeling that he doesn't know you borrowed it?"
    j "I totally don't know, hehe. Anyway, need a ride?"
    scene after_kandbf7 with dissolve
    j "And I totally don't mean that suggestively... hehe."
    pc "I'm not sure I'd want to sit on that bike with you as a rider, also I don't have a helmet, and we're in the middle of the city, if the cops see us..."
    scene after_kandbf6 with dissolve
    j "Nah, don't worry, I'll only take backstreets, nobody will see us."
    pc "I don't know, [j]. I've already had some trouble with the cops lately..."
    j "Awww, come on, you can take my helmet if you want. Don't be a pussy!"
    pc "I'm not a fucking pussy, and it won't fit anyway."
    scene after_kandbf7 with dissolve
    j "It won't fit a fucking pussy? Are you sure about that? Meow!"
    pc "That's not what I... shit, forget it."
    scene after_kandbf6 with dissolve
    j "Hehe, come on, let's ride!"
    pc "Yeah, yeah, fine..."
    if jlo >= 1:
        scene after_kandbf8 with dissolve
        pc "Huh?"
        menu:
            "Kiss her":
                image after_kandbf8_2 = "/jpg/after_kandbf8_2.jpg"
                $ pov1 = "after_kandbf8_2"
                $ pov2 = "jkiss"
                scene after_kandbf8_2 with dissolve
                $ povstart = True
                show screen povscreen(pov1)
                pause
                scene afterkbf9 with dissolve
                hide screen povscreen with dissolve
                hide screen povbutton with dissolve
                $ jlo += 1
            "Don't kiss her":
                pass
    stop music
    scene afterkbf9 with dissolve
    pc "Alright, let's go."
    j "You better grab my waist... tightly, hehe."
    pc "You do have a license, don't you, [j]?"
    scene afterkbf10 with dissolve
    j "Hold tight!"
    play sound "audio/bike-go.ogg"
    pc "Fuck!"
    scene black with fade
    play music "audio/FlowingNoise.mp3" fadein 2
    play sound "audio/motorcycle-ride.ogg" loop fadein 2
    scene jada_ride0 with dissolve
    j "{b}So, how was it?{/b}"
    pc "{b}How was what?{/b}"
    j "{b}Awww, come on, you know what I mean!{/b}"
    pc "{b}No, I don't...{/b}"
    j "{b}Last night of course, dumbass.{/b}"
    pc "{b}Last night?{/b}"
    pcthink "Could she mean...?"
    j "{b}Don't tell me [e] didn't do it!?{/b}"
    pcthink "Shit, it wasn't a dream? Holy fuck!!!"
    scene jada_ride2 with dissolve
    j "{b}Come on, tell me, tell me! Did she do it? Did she not?{/b}"
    pc "{b}Err... well, she did...{/b}"
    j "{b}Really?! Haha, how was it? Did she fuck up? Eh... I mean... you know what I mean, hehe.{/b}"
    pc "{b}No, it was...{/b}"
    pc "{b}Wait! Did you pressure her into doing this?{/b}"
    j "{b}Huh? Why would I do that?{/b}"
    pc "{b}[j], I'm serious. Did you, or did you not pressure her?{/b}"
    j "{b}I did not! I even told her to wait a bit longer, but she didn't want to listen...{/b}"
    pc "..."
    j "{b}She actually wanted to do it on her birthday already, but you know what happened...{/b}"
    pc "Yeah... sorry..."
    j "{b}Huh?{/b}"
    pc "{b}...nevermind.{/b}"
    pcthink "Shit! I had sex with my... not sister..."
    pcthink "Yeah right, she isn't my sister, not even my stepsister, lucky me I guess, haha..."
    if visit_e_d6 == True:
        $ visit_e_d6 = False
        scene jada_ride1 with dissolve
        pc "{b}By the way, I didn't see you at the school earlier today...{/b}"
        j "{b}Oh, did you come to see me? Did you miss me that much? Hehe.{/b}"
        pc "{b}I was just nearby and thought I'd say hi...{/b}"
        j "{b}Uh-huuuuh...{/b}"
        j "I bet you just wanted to see [e]..."
        pc "..."
        pc "{b}So?{/b}"
        j "{b}So what?{/b}"
        pc "{b}Did you skip classes?{/b}"
        j "{b}What if I did? Would you be mad at me for being a bad girl? Hehe.{/b}"
        pc "{b}I guess that would be a bit hypocritical...{/b}"
        j "{b}Hehe, yeah...{/b}"
        pc "{b}It's still bad behaviour, especially in front of [e]...{/b}"
        j "..."
        pc "{b}Look, I'm not going to lecture you, but do me a favour...{/b}"
        j "I didn't skip classes..."
        pc "{b}Huh?{/b}"
        j "{b}I got suspended...{/b}"
        pc "{b}Why?{/b}"
        j "{b}Ughhh, because that idiot teacher can't distinguish a calculator from a smartphone!{/b}"
        pc "{b}Seriously?{/b}"
        j "{b}Yeah, she thought I was texting, and wanted me to hand over my phone, so I told her to get some new glasses... and...{/b}"
        pc "{b}And?{/b}"
        j "Well..."
        pc "{b}Come on, you can tell me!{/b}"
        j "{b}She answered that her glasses are fine so...{/b}"
        j "{b}I said that if her glasses are fine, then she needed more proteins for her eyes, so she should go and suck some dicks...{/b}"
        pc "{b}No way! You really said that?{/b}"
        j "{b}Yeah... I guess... but only because I was really mad at that moment...{/b}"
        pc "{b}Hahaha, that's hilarious, I bet she freaked out!{/b}"
        j "{b}Well... yeah, that's why I got suspended...{/b}"
    stop music fadeout 2
    stop sound fadeout 1
    scene black with fade
    scene d6_comehome_j2 with dissolve
    play music mainbgm fadein 2
    j "Here we are~"
    scene d6_comehome_j1 with dissolve
    pc "Yeah, thanks for the ride."
    scene d6_comehome_j2 with dissolve
    j "Anytime, just ask if you want to {b}rrriiide{/b} again, hehe."
    pc "Ha... yeah, but maybe without \"borrowing\" a motorcycle next time..."
    j "Heh, alright."
    pc "Anyway, you better get the bike back to its owner..."
    scene d6_comehome_j3 with dissolve
    j "Guess you're right..."
    pc "...and you should really ask next time..."
    j "Yeah..."
    j "I guess mom will also know about the expulsion by now."
    pc "I guess she won't be too happy..."
    j "Yeah..."
    pc "Well that's what you get for being a naughty girl."
    scene d6_comehome_j1 with dissolve
    j "..."
    pc "Hey, don't be down in the mouth, okay? And maybe think before you act, next time."
    scene d6_comehome_j3_2 with dissolve
    j "Okay... {i}[md]!{/i}"
    pc "Hah, you wish... bye, [j]."
    if jlo >= 2:
        scene d6_comehome_jkiss with dissolve
    j "Hehe, bye~"
    scene d6_comehome_j4 with dissolve
    pause .5
    scene black with dissolve
    play sound "audio/bike-go.ogg"
    jump d6_backhomeRachel
    
label d6_gotobed:
    scene black with fade
    n "Later..."
    scene pcroom_d6_j_arrive0 with dissolve
    pcthink "YAAAWWN... damn, it's getting late... I should stop and go to bed..."
    play sound "audio/knock-window.ogg"
    n "*Knock* *Knock* *Knock*"
    scene pcroom_d6_j_arrive0door with dissolve
    pcthink "Huh? That was not coming from the door!?"
    play sound "audio/knock-window.ogg"
    n "*Knock* *Knock*"
    scene pcroom_d6_j_arrive1 with dissolve
    pcthink "[j]?!"
    scene pcroom_d6_j_arrive2 with dissolve
    j "Uh... hey, [pc]..."
    pc "What are you doing here, [j], it's the middle of the night!"
    j "Yeah, I know..."
    j "Um... I have a little problem..."
    pc "Don't tell me you got kicked out."
    j "Well... kinda..."
    pc "Kinda?"
    scene pcroom_d6_j_arrive3 with dissolve
    j "I had an argument with my mom because of the stuff in school..."
    j "...and the bike..."
    pc "Damn..."
    j "Mom was drunk and yelled at me... then I yelled back and..."
    j "..."
    if jlo < 2:
        j "I texted [e] and asked her if I can stay the night... she told me to come through your room... I hope you don't mind..."
        pc "Well, I don't mind, but I'm not so sure about [m]..."
        scene pcroom_d6_j_arrive6 with dissolve
        j "Don't worry, I'll be gone tomorrow morning before she notices anything."
        pc "Well then, be sure to make no noise when you go to [e]'s room."
        scene pcroom_d6_j_arrive7 with dissolve
        j "I will, thanks!"
        scene pcroom_d6_j_arrive8 with dissolve
        pcthink "Humph... this girl..."
        pcthink "Anyway, time to go to bed..."
        jump d6_night
    j "Can I stay here for the night?"
    pc "I'm not sure if this is a good idea..."
    scene pcroom_d6_j_arrive4 with dissolve
    j "Pleeeaaase, I promise to be a good girl!"
    pcthink "Damn, what a little minx... but I really don't know if this is a good idea."
    pcthink "I guess [e] would be okay with [j] staying overnight, but [m] would probably not like it..."
    scene pcroom_d6_j_arrive2 with dissolve
    j "I promise I'll be gone before anybody notices anything."
    pcthink "Hum... on the other hand, what she doesn't know, won't hurt her..."
    menu:
        "Alright, I guess it's okay for one night.":
            pass
        "No, better not.":
            $ jlo = 0
            j "Awww, come on..."
            pc "Sorry..."
            j "I guess I'll have to stay with [e] then..."
            scene pcroom_d6_j_arrive6 with dissolve
            j "But don't worry, I'll be gone tomorrow morning before [m] notices anything."
            scene pcroom_d6_j_arrive7 with dissolve
            j "Nightieee~!"
            scene pcroom_d6_j_arrive8 with dissolve
            pcthink "Humph... this girl..."
            pcthink "Anyway, not my problem... time to go to bed..."
            jump d6_night
    scene pcroom_d6_j_arrive5 with dissolve
    j "Yay, thanks!"
    scene pcroom_d6_j_arrive6 with dissolve
    j "I'll be a nice roommate, hehe."
    scene pcroom_d6_j1 with dissolve
    pc "Do you want the couch, or the bed?"
    scene pcroom_d6_j2 with dissolve
    j "Wow, did you really just ask that?"
    if pcgender == "woman":
        pc "Hey, I'm a gentle...woman..."
    else:
        pc "Hey, I'm a gentleman!"
    scene pcroom_d6_j3 at brakeshake with dissolve
    j "Haha, I really didn't expect that... but thanks for asking..."
    scene pcroom_d6_j4 with dissolve
    j "..."
    pc "Are you alright?"
    scene pcroom_d6_j5 with dissolve
    j "Yeah... it's just the situation with mom... it sucks..."
    scene pcroom_d6_j6 with dissolve
    pc "Weeeeell... I could say I told you so... but I'm not going to be like that *smirk*"
    scene pcroom_d6_j7 with dissolve
    j "Yeah... I guess I should have listened to you..."
    extend "[md], hehe."
    pc "Haha, you should have!"
    scene pcroom_d6_j8 with dissolve
    j "Umm... [pc]?"
    pc "Yeah?"
    j "Do you mind if I call you..."
    scene pcroom_d6_j9 with dissolve
    j "[md]?"
    pc "Uh..."
    menu:
        "I'm not really into that.": 
            j "Awww please, [md], please!!"
            menu:
                "Okay, fine. If you want it so badly.":
                    $ pcmd = md
                    jump jmdyes
                "No, I don't think so.":
                    $ pcmd = str(mrms) + " " + str(pc)
                    scene pcroom_d6_j11 with dissolve
                    j "Awww... okay..."
                    extend " [pc]."
                    pc "Does it make a difference?"
                    scene pcroom_d6_j11_2 at my_shake with dissolve
                    j "Hum..."
                    scene pcroom_d6_j12 with hpunch
                    j "I guess I can live with that."
                    scene pcroom_d6_j13 with dissolve
                    pause .5
                    jump d6_gotobed_withj
        "I actually like that!":
            $ pcmd = md
            jump jmdyes
            
    label jmdyes:
        $ jlo += 1
        scene pcroom_d6_j10 with dissolve
        j "Really? You don't mind?"
        pc "Yeah, why not."
        scene pcroom_d6_j10_2 with dissolve
        j "Thank you..."
        scene pcroom_d6_j12 at my_shake with dissolve
        j "...[md]!"
        scene pcroom_d6_j13 with dissolve
        pause .5
        jump d6_gotobed_withj
label d6_gotobed_withj:
    if pcgender == "woman":
        $ persistent.pcmdf = pcmd
    else:
        $ persistent.pcmdm = pcmd
    if _in_replay:
        show screen endRep
    scene pcroomd6jkiss with dissolve
    pause
    scene pcroom_d6_j13 with dissolve
    j "Hmmmm..."
    pc "By the way, [j]..."
    scene pcroomd6jkiss1 with dissolve
    pc "...could it be that you're not wearing anything under that jacket?"
    scene pcroomd6jkiss2 with dissolve
    j "Yeah... I was in the middle of changing when my mom started yelling at me... I just grabbed what wasn't in the washer already and left..."
    scene pcroom_d6_jakiss_3 with dissolve
    pc "Oh [j], oh [j]... what did I tell you about thinking before acting?"
    j "I know, I know, but..." 
    scene pcroom_d6_jakiss_4 with dissolve
    j "I'm sure my [pcmd] will warm me up, so I won't catch a cold, hehe."
    scene pcroomd6jkiss5 with dissolve
    pc "Well of course I'll do that for you..."
    scene jtits00 with dissolve
    show jtits
    pause 1
    j "Nhhhh..."
    pause
    pc "It's getting quite hot in here, don't you think?"
    scene pcroomd6jmc_undress with dissolve
    j "Hehe, let's do something about it."
    scene pcroomd6jmc_undress2 with dissolve
    pause 1
    scene black with dissolve
    scene pcroom_d6_j_mc_undress3 with dissolve
    j "I think I'm feeling a bit warmer now."
    scene pcroom_d6_j_mc_undress4 with dissolve
    j "Maybe I should lose some more..."
    scene pcroom_d6_j_mc_undress5 with dissolve
    pc "Sounds like a good idea."
    scene pcroom_d6_j_mc_undress6 with dissolve
    pause .5
    pcthink "Damn!"
    menu:
        "Grab her ass.":
            scene pcroomd6jmc_undress7 with dissolve
            j "I hope you don't mind if I just drop my pants to the ground..."
            scene pcroomd6jmc_undress8 with dissolve
            j "Your room is waaaay too tidy... whoa!"
            scene pcroom_d6_j_mc_undress9 with hpunch
            pause
    scene pcroomd6j_fp1 with dissolve
    j "Naughty..."
    scene pcroomd6j_fp2 with dissolve
    pc "Aren't you the one making my room messy? Naughty girl..."
    scene pcroomd6j_fp3 with dissolve
    j "Oh, I'm soooo sorry, [pcmd]."
    scene pcroomd6j_fp4 with dissolve
    pc "Tsk, tsk, I don't believe you, and I think you need a little punishment."
    scene pcroomd6j_fp5 with dissolve
    show pcroomd6jfp5
    j "Nnnnhh, yes, please, [pcmd]!"
    pause
    scene pcroomd6j_fp6 with dissolve
    pc "Well, I think that's enough punishment for now."
    scene pcroomd6j_fp7 with dissolve
    j "Awww, already?"
    pc "Do you want me to do all the work alone?"
    scene pcroomd6j_fp8 with dissolve
    j "Oh, so this is work for you?"
    scene pcroomd6j_fp9 with dissolve
    j "I guess I should help you then, hehe!"
    pc "Absolutely, young lady!"
    scene pcroom_d6_j_fp10 with dissolve
    j "Okay..."
    scene pcroomd6j_fp11 with dissolve
    j "...let's get rid of these!"
    scene pcroomd6j_fp12 with dissolve
    j "...and now..."
    scene pcroomd6j_fp13 with dissolve
    pause 1
    scene pcroomd6j_fp14 with dissolve
    j "Hmm..."
    if pcgender == "man":
        scene pcroom_d6_j_fp15 with dissolve
        pause .5
        scene pcroom_d6_j_fp15_2 with dissolve
        pause 1
        scene pcroom_d6_j_fp15_3 with dissolve
        j "Hmph..."
    scene d6_jbj1 with dissolve
    show d6jl1
    $ pov1 = "d6jl1"
    $ pov2 = "d6jl2"
    $ campov = False
    $ povstart = True
    show screen povscreen(pov1)
    pause
    scene d6jl3 with dissolve
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    j "Hmmm..."
    pause
    scene black with dissolve
    scene pcroomd6j_fp16 with dissolve
    if pcgender == "man":
        j "Hum... I think I need to work a bit harder."
        pc "Haha, go for it!"
        j "Hehe."
    else:
        j "Would you mind sharing the \"work\", [pcmd]?"
        pc "Well, I guess you earned that much."
        j "Yay!"
    scene pcroom_d6_j_fp17 with dissolve
    j "Let me just..."
    if pcgender == "man":
        scene pcroom_d6_j_fp17_2 with dissolve
        show d6jfinsert
        pause 3.4
        scene pcroom_d6_j_fp17_3 with dissolve
    scene d6_jf1 with dissolve
    show d6jf1
    pause .5
    j "Unnn... yes!"
    pause
    j "Oww gawd, this feels great!"
    pc "Gawd, yes!"
    scene d6_jf2 with dissolve
    show d6_jf2
    $ pov1 = "d6jf2"
    $ pov2 = "d6jf3"
    $ campov = False
    show screen povscreen(pov1)
    pause 
    j "Ohnn... gawd!"
    show d6jf5
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    $ pov1 = "d6jf5"
    $ pov2 = "d6jf4"
    $ campov = False
    show screen povscreen(pov1)
    j "Hnnn! Haaaa!"
    if pcgender == "man":
        j "So warm..."
        j "...so big..."
    else:
        j "So hot!"
    pause
    pc "Gaaawd, [j]!"
    j "Yes, yes, yes, [pcmd]!"
    j "Fuck me, fuck me!"
    if pcgender == "man":
        j "Cum inside me!"
        j "Fill me up, [pcmd]!"
    pc "Holy sh..."
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    scene pcroomd6jfuckend1 with flash
    j "{cps=15}{size=+10}HAAAAAAAH...{/size}{/cps}" with vpunch
    scene pcroomd6jfuckend1_2 with dissolve
    pause .5
    j "Ohh... shit..."
    scene pcroomd6jfuckend2 with dissolve
    j "Sorry, that was probably a liiiitle bit loud."
    pc "Ha, let's just hope that no one heard that."
    j "Yeah, haha..."
    if pcgender == "woman":
        j "Phew... that was more exhausting than I thought, hehe."
        pc "Well, maybe because scissoring usually works a little bit different."
        j "I know... I just wanted to be creative!"
        pc "Haha, well that's what you get."
        j "Pff... bitch!"
        pc "What was that, little girl?"
        j "Uhh... sorry [pcmd]..."
        pc "I guess you need some more punishment, hm?"
    if pcgender == "man":
        pc "Maybe we should close the balcony door..."
        scene pcroom_d6_jfuckend2 with dissolve
        j "Ooooor... we could go another round to keep us warm?"
        pc "Hum, I guess that's an alternative. Let's do it!"
    j "Hehe, yay..."
    $ renpy.end_replay()
    scene black with fade
    stop music fadeout 2
    $ storyEvent = False
    $ visit_cafe_d6 = False
    $ visit_work_d6 = False
    $ actionsUsed = 8
    call dateTime from _call_dateTime_20
    jump d7_wakeup
    
label d7_motel:
    n "BZZZzzzzzz"
    scene d8jcall1 with dissolve
    pcthink "Hm? Jada..."
    pcthink "How is her number saved on my phone?"
    scene d8jcall2 with dissolve
    pc "Yeah?"
    j "Hey, [pcmd]!"
    pc "Hey, what's up, [j]?"
    j "Umm... I'd like to ask you a favor..."
    pc "A favor? If it has something to do with toilet paper, forget it."
    j "Huh? Toilet paper?"
    scene d8jcall3 with dissolve
    pc "Nah, forget about it... what do you need?"
    j "Well... I got a little problem..."
    pc "Uh-huh... what did you do this time, [j]?"
    j "It wasn't my fault, honestly!"
    pc "Ugh... what happened?"
    j "...Mom kicked me out..."
    scene d8jcall2 with dissolve
    pc "She did what?"
    j "I tried to apologize... but she started arguing again, and..."
    scene d8jcall3 with dissolve
    pc "Oh dear..."
    j "..."
    pcthink "She sounds really down... understandably..."
    pc "Do you have somewhere to stay?"
    j "I actually do, yes."
    pc "Really!?"
    j "Yes, I got a small apartment where I can stay... That's why I'm calling."
    pc "Oh you got an apartment? That's awesome!"
    j "Yeah... but I could use a bit of help here..."
    pc "I guess so, where is it?"
    j "No. 2 Salt Street."
    pcthink "Hum, that rings a bell..."
    pc "Okay, give me about half an hour and I'll be there."
    j "Really? You'll come over?"
    pc "Yeah, of course."
    j "Yay, thanks!"
    pc "By the way, you don't happen to know how your number got onto my phone?"
    j "No idea... hehe."
    pc "[j]..."
    scene black with fade
    n "About half an hour later..."
    scene d7_motel with dissolve
    pcthink "Okay, so this is the address..."
    pcthink "As I though, I know this place!"
    pcthink "This used to be a cheap motel, now it looks even cheaper..."
    pcthink "I can't believe they made apartments out of those small rooms."
    scene d7_motel2 with dissolve
    pcthink "...and of course the cops are here... this place doesn't seem to have changed for the better."
    scene d7_motel3 with dissolve
    pcthink "Well, maybe the apartments are good at least..."
    pcthink "Huh? What's this?"
    scene d7_motel_construction with dissolve
    pause 1
    pcthink "What the hell?"
    "Girl" "Yeah how lazy is that?"
    scene d7_motel4 with dissolve
    pc "Huh?"
    "Girl" "Yes, can you believe it? They're so bad!"
    play sound "audio/door-opening.ogg"
    pcthink "Oh she's talking on the phone..."
    j "Hey, [pc]!"
    scene d7_motel_jada with dissolve
    pc "Oh hey, [j]!"
    j "Come in!"
    scene d7_motel_jada2 with dissolve
    j "Welcome to my apartment, hehe..."
    scene d7_motel_jada3 with dissolve
    j "Just don't look... well, anywhere, and better not touch anything without wearing gloves, haha."
    pcthink "Uhh... well I didn't have high hopes after seeing the building, but this is..."
    scene d7_motel_jada4 with dissolve
    j "I know, I know, it's a shithole, but that's why you're here, right? I bet we can make it... bearable at least."
    pc "Are you sure, [j]? I mean, what's up with the junk and all?"
    scene d7_motel_jada3 with dissolve
    j "Yeah, the apartment was used as a storage place and the landlord told me that no one had entered it since... I don't know... world war two maybe."
    pc "Haha, definitely looks like it!"
    scene d7_motel_jada4 with dissolve
    j "You know... it's not like I have a choice. I don't have any money and he's only letting me live here because he knew my dad... and maybe because he's a little perv."
    pc "Ugh... that doesn't make it better..."
    scene d7_motel_jada5 with dissolve
    pc "What about the kitchen, is it usable?"
    scene d7_motel_jada5_2 with dissolve
    j "Have a look."
    scene black with dissolve
    scene d7_motel_jada6 with dissolve
    pc "Okay, this is... ugh... at least the fridge seems to be working..."
    j "Yeah, surprising isn't it? I just plugged it in and it ran."
    scene d7_motel_jada7 with dissolve
    j "I was too scared to open it yet, though..."
    pc "What the fuck!?"
    pc "A toilet in the kitchen?!"
    scene d7_motel_jada8 with dissolve
    j "Yeah... I know it's not ideal, but..."
    pc "[j], that's the epitome of worst things to have in the kitchen!"
    scene d7_motel_jada9 with dissolve
    j "But at least I can shower..."
    scene d7_motel_jada7 with dissolve
    pc "There's a shower too?"
    j "Yeah..."
    scene d7_motel_jada10 with dissolve
    pc "Jeez..."
    scene d7_motel_jada11 with dissolve
    pc "Where do you sleep? In the closet?"
    scene d7_motel_jada11_2 with dissolve
    j "..."
    scene d7_motel_jada12 with dissolve
    pc "Uff... [j]..."
    j "So..."
    scene d7_motel_jada13 with dissolve
    j "Will you help me?"
    menu:
        "Yes...":
            pass
        "Of course!":
            pass
    pc "...you know what?"
    scene d7_motel_jada13_2 with dissolve
    j "What?"
    pc "I'll ask [m] if you can live with us for a while."
    scene d7_motel_jada14 with dissolve
    j "W-what?! Really?!"
    pc "Yeah, why not."
    scene d7_motel_jada15 with dissolve
    j "Wow! Thanks, but... I doubt that she will say yes..."
    pc "Well, she kinda has to, it's not her house you know..."
    scene d7_motel_jada16 with dissolve
    j "It's not?"
    pc "No, it's my old man's house and he's dead, so..."
    scene d7_motel_jada16_2 with dissolve
    j "Oh right, they weren't married."
    pc "Yeah."
    scene d7_motel_jada17 with dissolve
    j "But I think I'd feel bad, living there if she doesn't want me to..."
    pc "Don't worry, she knows how hard it is to get an apartment at the moment. I bet she doesn't mind."
    scene d7_motel_jada18 with dissolve
    j "You don't need to do this, you know."
    pc "But I will. I wouldn't want anyone to live in this shithole, especially not with an old perv nearby."
    scene d7_motel_jada19 with dissolve
    if jlo == 0:
        j "Hehe, yeah, I'd rather be the perv."
        pc "Haha, I thought so."
        scene d7_motel_jada23_2 with dissolve
        j "So, can you help me clean up a bit... just in case?"
        pc "Sure. [m] is still at work anyway..."
        scene black with fade
        scene d8_motel_cleaning1 with dissolve
        j "Phew, that was more then expected... sorry for that."
        scene d8_motel_cleaning3 with dissolve
        pc "No prob, at least we passed some time."
        scene d8_motel_cleaning2 with dissolve
        j "Yeah, [e] and [m] should be home by now."
        scene d8_motel_cleaning4 with dissolve
        pc "Yeah, so I better make my way home. I'll let you know if you can come over."
        scene d8_motel_cleaning2 with dissolve
        j "Cool, I can't wait, hehe."
        scene d8_motel_cleaning4 with dissolve
        pc "Alright, later then."
        scene d8_motel_cleaning5 with dissolve
        j "Later!"
        scene black with fade
        jump d8_rachel_talk
    j "Hehe, yeah I already have my old perv."
    pc "Huh? Who are you talking about?"
    scene d7_motel_jada20 with dissolve
    j "You of course!"
    pc "Me?! I'm not a perv! ...well maybe a bit, but I'm not old!"
    scene d7_motel_jada21 with dissolve
    j "No, but I hope you will perv on me frequently, hehe ...and you're older than me."
    pc "I'm not {b}that{/b} old!"
    pc "Heh, but the other part sounds like something I could be interested in."
    scene d7_motel_jada22 with dissolve
    j "Hehe... oh..."
label d7_motel_r:
    if _in_replay:
        show screen endRep
    scene d7_motel_jada23 with dissolve
    pc "Oh? What's wrong?"
    scene d7_motel_jada23_2 with dissolve
    j "I guess that means we won't have make-up sex after some hard work today..."
    pc "Huh?"
    if not jpushed:
        pc "Did we have something to make up for?"
        scene d7_motel_jada23_3 with dissolve
        j "Hehe, no but I've heard old people need a reason to have sex."
        pc "Pfff, I'm not..."
        pc "Ugh, whatever, come here you little bitch!"
        scene d7_motel_jada24 with dissolve
        j "Hehe! Uhhh, [pcmd]!"
    else:
        pc "Uhh, yeah, right. I'm sorry for pushing you out of the bed."
        pc "I was just panicking at that moment."
        scene d7_motel_jada23_3 with dissolve
        j "Well... you could \"make-up\" for it... [pcmd]."
        pc "Hum, I guess I should make sure you didn't get any bruises or scratches, so I better check you thoroughly."
        scene d7_motel_jada24 with dissolve
        j "Hehe, yes, [pcmd]!"
    if pcgender == "man":
        scene black with slowdissolve
    else:
        scene d7_motel_jada24_2 with dissolve
        j "Oh wait! I've got something!"
        pc "Huh? What?"
        scene d7_motel_jada24 with dissolve
        j "You'll see, hehe."
        scene d7_jmotelstrapon0 with dissolve
        j "I'll be right back!"
        scene d7_jmotelstrapon0_1 with dissolve
        pause .5
        n "*Ruffle* *Ruffle*"
        pause .5
        pc "..."
        scene d7_jmotelstrapon1 with dissolve
        j "Back!"
        pc "So? What is it?"
        scene d7_jmotelstrapon2 with dissolve
        j "Tadaaaa~"
        pc "A strap-on?"
        j "Yeah, awesome isn't it?"
        scene d7_jmotelstrapon3 with dissolve
        j "It even has this little one here, hehe."
        pc "Wow..."
        scene d7_jmotelstrapon4 with dissolve
        j "I thought that... maybe you want to try it out on me?"
        pc "Uhh..."
        menu:
            "I'm not sure honestly...":
                scene d7_jmotelstrapon4_2 with dissolve
                j "Awwww, come on, I've never tried it out... I really want you to bang me like a dirty little girl!"
                j "Don't make me put my puppy pout face on, [pcmd]... you'll regret it, I swear!"
                pc "Haha, okay, okay you won. I can't win against a puppy pout face of a cute girl!"
                scene d7_jmotelstrapon4 with dissolve
                j "Hehe, yay~!"
            "Yeah, sure!":
                scene d7_jmotelstrapon4 with dissolve
                j "Hehe, finally! I've had it for so long, but never really got to try it out."
                j "Pound me like a dirty little girl, [pcmd]!"
                pc "Haha, you bet!"
        scene black with slowdissolve
        
    scene jmotelf200 with dissolve
    show jmotelf245
    $ pov1 = "jmotelf"
    $ pov2 = "jmotelf2"
    $ campov = False
    $ povstart = True
    show screen povscreen(pov1)
    pause
    j "Hnnn, yes, [pcmd]!"
    pause
    j "Faster, [pcmd]! Pound me like a dirty little girl! Haaa..."
    show jmotelf245
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    $ pov1 = "jmotelf45"
    $ pov2 = "jmotelf245"
    show screen povscreen(pov1)
    pause
    j "Nhhhnnnn, [pcmd]! Haaa! Hnaaa!"
    j "Ohhh gawd, howw gaawd!"
    if pcgender == "man":
        j "Fill me, fill my belly with your cum, [pcmd]!"
    scene d7motelfend with dissolve
    hide screen povscreen with dissolve
    hide screen povbutton with dissolve
    j "I'm... Nnnnnhaaaaa!" with flash
    scene d7motelfend with dissolve
    j "Haaaaa~haaa!" with flash
    scene d7motelfend2 with dissolve
    j "Ha... ha... *pant*"
    if pcgender == "man":
        scene d7_motel_fendcum2 with dissolve
        j "...soooo much..."
    scene black with slowdissolve
    scene d7_motel_afterf with dissolve
    j "..."
    pc "..."
    j "Hnn..."
    scene d7_motel_afterf2 with dissolve
    j "I don't know why, but sex with you feels kinda special..."
    scene d7_motel_afterf with dissolve
    pc "Does it?"
    scene d7_motel_afterf2 with dissolve
    j "Yeah!"
    scene d7_motel_afterf with dissolve
    pc "Well... thanks..."
    scene d7_motel_afterf3 with dissolve
    if pcgender == "woman":
        j "You have to tell me your secret, hehe."
        pc "Uhh... there is no secret."
        scene d7_motel_afterf4 with dissolve
        j "Pff, you just don't want to tell me!"
        pc "Hmm... maaaaybe."
        scene d7_motel_afterf5 with dissolve
        j "Bitch! Hehe."
    else:
        j "I bet you had a quadzillion girls to practice your secret technique, hehe."
        pc "Hmm... maaaaybe."
        scene d7_motel_afterf5 with dissolve
        j "Dick! Hehe."
    scene d7_motel_afterf with dissolve
    pc "..."
    j "..."
    scene d7_motel_afterf2 with dissolve
    j "Are you sure you don't want to take a shower?"
    scene d7_motel_afterf with dissolve
    pc "Yeah, definitely not in this shower... I'll take a shower when I'm back home."
    scene d7_motel_afterf2 with dissolve
    j "Hum... too bad."
    scene d7_motel_afterf with dissolve
    pc "Speaking of which, I should go... it's getting late."
    scene d7_motel_afterf2 with dissolve
    j "Aww, that's even worse..."
    scene d7_motel_afterf with dissolve
    pc "Haha yeah, but hey maybe we can shower together regularly soon."
    scene d7_motel_afterf5 with dissolve
    j "Uhh, that sounds nice! Maybe [e] and [m] can join us, hehe."
    pc "Haha, dirty girl."
    scene d7_motel_afterf7 with dissolve
    j "Hehe, you made me dirty!"
    j "... I guess I should try the shower..."
    pc "Just watch out that you aren't getting even dirtier in that thing."
    j "Hehe, I will..."
    if pcgender == "man":
        scene d7_motel_afterf6 with dissolve
        j "But I think I'll just leave your \"dirt\" where it is for a little longer..."
        j "...maybe even play with it... hehe."
        pc "You dirty little minx!"
        scene d7_motel_afterf7 with dissolve
        j "You made me, [pcmd]..."
    $ renpy.end_replay()
    scene black with fade
    n "As you leave the apartment..."
    scene d7_motel_leave1 with dissolve
    "Girl" "Yes, I could hear it all, she was like \"yes [pcmd], give it to me [pcmd]\", haha."
    pcthink "Oh shit..."
    "Girl" "[heshe!c] must be really good..."
    play sound "audio/door-closing.ogg"
    scene d7_motel_leave2 with dissolve
    "Girl" "Ah, err..."
    scene d7_motel_leave3 with dissolve
    "Girl" "... t-that's what happens in the movie I told you about earlier... haha."
    scene d7_motel_leave2 with dissolve
    pause .2
    scene d7_motel_leave3 with dissolve
    "Girl" "Yes..."
    pc "..."
    scene black with fade
    
    jump d8_rachel_talk
    
label d9_morning_wakeup:
    $ d9_wakeup = True
    scene black with dissolve
    play sound "audio/impact.ogg"
    n "*Boink*" with hpunch
    scene pcroom_wakeup2
    scene pcroom_wakeup with dissolve
    pcthink "Huh?"
    j "Ouch ouch ouch! Fuck!"
    scene d9_pcroom_morning01 with dissolve
    pc "[j]?!"
    j "Awww damn it!"
    n "You can't help but giggle seeing [j] jumping on one foot holding the other."
    scene d9_pcroom_morning02 with dissolve
    j "Hey, that's not funny!"
    pc "Haha, that's what you get for sneaking into someone else's bedroom."
    scene d9_pcroom_morning03 with dissolve
    j "I didn't sneak... you were just sleeping like a log."
    pc "Suuuuure...and you think I'd believe that, hm?"
    scene d9_pcroom_morning04 with dissolve
    j "You better believe it!"
    scene d9_pcroom_morning05 with dissolve
    j "[m] is making breakfast and [e] is still asleep, so I thought I'd wake you up."
    pc "By kicking my bed?"
    j "Haaaa-Haaaa!"
    scene d9_pcroom_morning06 with dissolve
    j "You know that [e] was trying to sneak over tonight?"
    pc "Like usual..."
    scene d9_pcroom_morning07 with dissolve
    j "Yeah I know, she really likes to sleep with... err next to you, hehe."
    pcthink "Little minx..."
    scene d9_pcroom_morning06 with dissolve
    if jlo > 2:
        j "you know..."
        pc "What?"
        scene d9_pcroom_morning08 with dissolve
        j "I was expecting you to come over and molest us in our sleep."
        pc "Huh?! What do you think I am? Some kind of dirty pervert?"
        j "Maybe, hehe."
        pc "I think you might've played too many adult games."
        j "Mmmmmaybe..."
        scene d9_pcroom_morning09 with dissolve
        j "But [pcmd], I wouldn't mind if you molest me in my sleep, and I bet [e] wouldn't mind either, hehe."
        pc "Jeez, you better stop that, or I'll have to punish you for being so naughty."
        scene d9_pcroom_morning10 with dissolve
        j "Oh, but I wouldn't mind if you punish me [pcmd]..."
        pc "I guess that means I'll have to give you some extra punishment then, huh?."
        j "Hmmmm... please [pcmd]."
        pc "Well shit, we better stop here, I bet that either [m] or [e] will come looking for us if we don't get up."
        scene d9_pcroom_morning11 with dissolve
        j "Awwww but I want my punishment..."
        pc "Heh, you're not supposed to want it, but don't worry, you'll get your punishment later."
        scene d9_pcroom_morning10 with dissolve
        j "Hehe, I hope so, [pcmd]."
        scene d9_pcroom_morningjkiss with dissolve
        j "*Smooch*"
    else:
        pause 1
    scene d9_pcroom_morning07 with dissolve
    j "Well, I guess I'll let you get up then... that is... unless you want me to help, hehe."
    pc "I'm good, thanks."
    j "Too bad."
    scene d9_pcroom_morning12 with dissolve
    j "Well, see you in a bit."
    scene black with slowdissolve
    queue sound ["audio/shower_start.mp3", "audio/shower.mp3"]
    n "You get up, go to the bathroom and take a shower..."
    jump d9_ebathroom
    
label d9_backhome_j:
    scene d9_j_bathroom01 with dissolve
    pc "Whoops, sorry I..."
    scene d9_j_bathroom02 with dissolve
    j "Oh hey, [pcmd]!"
    scene d9_j_bathroom03 with dissolve
    j "What do you think?"
    pc "Oh you've been to a hairdresser?"
    scene d9_j_bathroom04 with dissolve
    j "Yeah, I talked [m] into it, hehe."
    pc "Looks good, I like the color."
    scene d9_j_bathroom05 with dissolve
    j "Thanks, I was hoping you'd like it."
    pc "Wait, did [m] get a new haircut too?"
    scene d9_j_bathroom04 with dissolve
    j "More like a new styling, but it looks great, you should see her!"
    pcthink "Shit, that's why she looked different..."
    scene d9_j_bathroom05 with dissolve
    j "So, were you looking for me, or do you want to use the bathroom?"
    pc "Err, the latter actually..."
    j "Too bad..."
    scene d9_j_bathroom06 with dissolve
    j "Well, go ahead! Don't mind me."
    pc "Are you sure?"
    scene d9_j_bathroom07 with dissolve
    j "Mhm..."
    scene d9_j_bathroom08 with dissolve
    pc "Well, if you don't mind, I won't mind either.."
    scene black with dissolve
    scene d9jbathroom09 with dissolve
    j "Hm~hm~hm~..."
    pcthink "Looks like someone is quite happy about her new hair style..."
    if jlo > 2:
        jump d9_backhome_j_fun
    else:
        scene d9_j_bathroom10 with dissolve
        j "Hmm..."
        pc "Hey, what are you looking at?"
        scene d9_j_bathroom10_2 with dissolve
        j "Umm... nothing? Hehe, sorry, I couldn't help it."
        pc "Yeah, and I bet it was totally {b}not{/b} intentional..."
        scene d9_j_bathroom10_3 with dissolve
        j "Who knows, hehe."
        pc "[j]..."
        scene d9_j_bathroom10_4 with dissolve
        j "Oh come on, did you really expect me to not look?"
        pc "Well, I guess you're right, I should've expected it, knowing you..."
        scene d9_j_bathroom10_4_up with dissolve
        j "Yes you should have."
        jump d9_backhome_j_end
label d9_backhome_j_fun:
        if _in_replay:
            show screen endRep
        scene d9_j_bathroom10 with dissolve
        j "You know, I was just thinking..."
        scene d9_j_bathroom11 with dissolve
        j "Maybe you want me to help?"
        pc "Uhh... help with what exactly?"
        scene d9_j_bathroom12 with dissolve
        j "Cleaning, hehe."
        pc "Cleaning what?"
        j "You, with my mouth, hehe."
        pc "Dirty girl..."
        scene d9_jlick with dissolve
        j "Oh that's entirely your fault, [pcmd]!"
        pc "Heh, go ahead then."
        if pcgender == "man":
            scene d9jbjlick with dissolve
            pause 2.5
            scene d9jbj01 with dissolve
            pause
            pc "I think you need to go a bit deeper to clean it properly."
            j "Hnnn..."
            $ pov1 = "d9jbj02"
            $ pov2 = "d9jbj02side"
            $ povstart = True
            show screen povscreen(pov1)
            pause
            pc "Shit, yeah, that's it!"
            hide screen povscreen with dissolve
            hide screen povbutton with dissolve
            scene d9_jsuck2_00 with dissolve
            show d9jbj03
            pause
            show d9jbjcum
            pc "Shit, shit, shit!"
            scene d9_jsuc_swallow1 with dissolve
            j "*Slurp*"
            scene d9_jsuc_swallow2 with dissolve
            j "Mhh..."
            scene d9jbathroom13 with dissolve
        else:
            scene d9_jlick_01_0 with dissolve
            j "Hmm... yummy!"
            pc "Go on babygirl."
            j "At once, [pcmd]!"
            scene d9_jlick2_00 with dissolve
            show d9jlick1
            pause
            pc "Hnn... you're such a dirty girl, [j]!"
            scene d9_jlick_00 with dissolve
            j "Hehe."
            show d9jlick2
            pause
            scene d9_jlick3_00 with dissolve
            pc "Oh shit, don't stop, babygirl."
            show d9jlick3
            pause
            pc "Oh shit, oh shit, oh shit!"
            #
            pc "I'm... cumming! Haa!" with flash
            pc "Haaa!" with flash
            pc "Haa!" with flash
        scene d9jbathroom13 with dissolve
        j "Thank you, [pcmd], that was delicious!"
        pc "Shit, [j], I could get used to that."
        j "Me too, [pcmd], hehe."
        $ renpy.end_replay()
        scene d9_j_bathroom14 with dissolve
        pc "Huh, that's it? You don't want me to return the favor?"
        j "Oh I'm good, I just had a bit fun myself, hehe."
        pc "I see... so..."
        jump d9_backhome_j_end
label d9_backhome_j_end:
    scene d9jbathroom_flush with dissolve
    pause .5
    play sound "audio/flush.ogg"
    scene d9_j_bathroom10_5 with dissolve
    pc "You're going to stay in the bathroom?"
    j "Yeah, maybe you and [e] should spend some time alone, too."
    scene d9_j_bathroom15 with dissolve
    pc "Hmm... how considerate..."
    j "Right?"
    scene black with dissolve
    jump d9_pcroom_e01
        
label d9_jhall:
    scene d9_jhall with dissolve
    pcthink "Alright, time to get some answers!"
    play sound "audio/door-opening.ogg"
    scene d9_jhall00 with dissolve
    j "Thanks, [m]! Hehe."
    pcthink "What the..."
    play sound "audio/door-closing.ogg"
    scene d9_jhall01 with dissolve
    j "Oh hey, [pc]."
    pc "What are you doing here, [j]? Didn't [m] tell you she doesn't want to get disturbed when she takes the pills?"
    scene d9_jhall02 with dissolve
    j "Uhh... no?"
    j "I was just having a nice little chit-chat with her..."
    pc "Uh-huh... just a chit-chat..."
    scene d9_jhall03 with dissolve
    j "So I guess you didn't just want to enter the room, right?"
    pc "Uhh, I was just walking by."
    scene d9_jhall04 with dissolve
    j "Suuuure, hehe."
    scene d9_jhall04_2 with dissolve
    pc "Hey, what do you think of me!?"
    scene d9_jhall04_3 with dissolve
    j "Only the best {size=-15}and naughtiest{/size} things, hehe."
    scene d9_jhall04_2 with dissolve
    pc "Eh..."
    scene d9_jhall04 with dissolve
    j "Where's [e] by the way?"
    pc "She's waiting in my room."
    j "Okay, any plans for the rest of the day?"
    pc "No, not really."
    scene d9_jhall05 with dissolve
    j "Why don't we watch a movie or something?"
    pcthink "Shit, if I go into [m]'s room now she'll know something's fishy..."
    pc "Yeah, why not."
    scene black with slowdissolve
    
jump d9_backhome_pcroom

label d10pcroombeforekh:
    if d10mshowervisit:
        scene d10pcroom01 with slowdissolve
        pcthink "Damnit, that was unsatisfying..."
        scene d10pcroom02 with dissolve
        pause .5
        scene d10pcroom03 with vpunch
        pc "..."
        pcthink "I guess I could just watch some porn..."
    else:
        scene d10pcroom01 with dissolve
        pcthink "Well, I guess I'll have some alone time now..."
        scene d10pcroom02 with dissolve
        pause .5
        scene d10pcroom03 with vpunch
        pcthink "Hmm, I guess I could check my mail and stuff..."
    scene d10pcroom05 with dissolve
    pause 1
    scene d10pcroom06 with dissolve
    pcthink "Oh damn, I have to deliver the project tomorrow... shit!"
    scene d10pcroom07 with dissolve
    pcthink "Guess I better finish it before it's too late..."
    scene black with fade
    scene d10pcroom08 with slowdissolve
    pcthink "Alright, this does actually look good!"
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    scene d10pcroom09 with dissolve
    j "Hey."
    pc "Hey, [j]."
    scene d10pcroom10 with dissolve
    pc "Are they still having their session?"
    j "Yeah..."
    scene d10pcroom11 with dissolve
    j "Whatcha doing?"
    pc "Working."
    scene d10pcroom12 with dissolve
    j "Working? On a sunday?"
    scene d10pcroom13 with dissolve
    pc "Yeah, I totally forgot that I have to deliver a project tomorrow..."
    scene d10pcroom12 with dissolve
    j "Uh-huh, workaholic."
    pc "I'm not a workaholic, there's not much else to do anyway."
    scene d10pcroom14 with dissolve
    j "You could've spent time with me!"
    scene d10pcroom15 with dissolve
    pc "I just told you that I have to deliver it tomorrow, didn't I?"
    scene d10pcroom16 with dissolve
    j "Show me!"
    scene d10pcroom17 with dissolve
    pc "There's not much to see, it's just a lot of code and the UI won't work until it's implemented in the main system."
    scene d10pcroom18 with dissolve
    j "Uh... okay..."
    scene d10pcroom19 with dissolve
    pc "Heh, I've just finished working on it anyway."
    scene d10pcroom20 with dissolve
    j "Nice, so we can play a game!"
    pc "What game?"
    scene d10pcroom21 with dissolve
    j "I have some ideas."
    pc "Wait, you are talking about a computer game... right?"
    scene d10pcroom22 with dissolve
    j "Maaaaaybe, hehe."
    scene d10pcroom23 with dissolve
    pc "Heh, I see you're already playing games with me."
    scene d10pcroom24 with dissolve
    j "Am I? Oh, but isn't life a game anyway?"
    scene d10pcroom23 with dissolve
    pc "But what kind of game would it be then? An adventure? An action game?"
    scene d10pcroom25 with dissolve
    j "Hmm, maybe it is..."
    scene d10pcroom24 with dissolve
    j "Maybe it's a dating sim, or a visual novel."
    pc "A romance game?"
    j "Ohh, maybe? Hehe."
    scene d10pcroom26 with dissolve
    pc "Or it turns out to be a horror game..."
    scene d10pcroom27 with dissolve
    j "Let's hope not!"
    pc "Yeah..."
    scene d10pcroom28 with dissolve
    j "Hey, maybe it's a porn game, haha. I {b}bet{/b} it's a porn game!"
    pc "Heh, maybe."
    scene d10pcroom29 with dissolve
    j "Hmm... if we're in a game, why not ask the player?"
    scene d10pcroom30 with dissolve
    pc "Haha, sure!"
    scene d10pcroom31 with dissolve
    j "Hey, Player, what kind of game are we in?"
    scene d10pcroom32 with dissolve
    pc "Err... why do you ask me?"
    scene d10pcroom33 with dissolve
    j "I'm not asking you, I'm asking the player! You're obviously the MC."
    pc "What? Why me? Why not you, or [e]?"
    j "Because you're the one who gets all the girls."
    scene d10pcroom30 with dissolve
    pc "Huh? You think so?"
    scene d10pcroom33 with dissolve
    j "Obviously! All the girls have at least a crush on you!"
    scene d10pcroom30 with dissolve
    pc "And who is \"all the girls\"?"
    scene d10pcroom34 with dissolve
    j "Oh come on, it's everyone in this house! Even visitors! You seem to have some kind of magic attraction, like the MC in porn VN's."
    pc "Err... aren't those MC's usually weird creeps?"
    scene d10pcroom35 with dissolve
    j "Yeah, haha."
    pc "Well thanks for calling me a creep then..."
    scene d10pcroom36 with dissolve
    j "Awww, I didn't mean it {b}that{/b} way!"
    if pcgender == "man":
        pc "Also, don't they usually have a huge horse cock?"
        scene d10pcroom35 with dissolve
        if jlo >= 1:
            j "Yeah, usually... maybe the dev prefers small cocks?"
            pc "Hey!"
            scene d10pcroom37 with dissolve
            j "Haha, I mean small compared to a horse cock."
            scene d10pcroom35 with dissolve
            j "You're still above average... honestly it's quite impressive and I love it!"
            pc "Well, thanks, I'm glad you like it."
            scene d10pcroom33 with dissolve
            j "It's not the only thing I like about you..."
            pc "Is that so? Tell me more."
        else:
            j "You don't have one?"
            pc "Obviously not! It's... normal."
            scene d10pcroom38 with dissolve
            j "Hmm, too bad, it must be something else then..."
            pc "Maybe my good looks or being an awesome person all around..."
            scene d10pcroom37 with dissolve
            j "Haha, maybe."
    else:
        pc "Also, aren't they usually male and have a huge horse cock?"
        scene d10pcroom35 with dissolve
        j "There are some games with incredibly good looking female MC's."
        pc "Is that a compliment?"
        scene d10pcroom33 with dissolve
        j "Well... you aren't one of these corrupted bimbo sluts who get fucked by several men and/or monsters at the same time, sooo..."
        pc "Ewww, [j], you definitely play too many of those type of games!"
        scene d10pcroom37 with dissolve
        j "Haha, maybe!"
        if jlo >= 2:
            scene d10pcroom33 with dissolve
            j "But honestly I wouldn't even mind if you had a horse cock as long as you're still the same awesome looking, jaw dropping, hot girl, hehe."
            pc "Wow, you definitely need to work on your compliments, but uhh... thanks..."
    scene d10pcroom39 with dissolve
    j "..."
    scene d10pcroom40 with dissolve
    pc "Hm? what's wrong, [j]?"
    j "..."
    pc "[j]?"
    scene d10pcroom41 with dissolve
    j "Hm? Oh, nothing... it's nothing."
    pc "Are you sure?"
    scene d10pcroom42 with dissolve
    j "Yeah, sure, I'm fine..."
    scene d10pcroom43 with dissolve
    j "...I think I'll check if they're done with the session."
    pc "Okay...?"
    scene d10pcroom44 with dissolve
    j "Later!"
    scene d10pcroom04 with dissolve
    pcthink "What was that? She went from super-happy to ultra-sad within a second..."
    pcthink "Damn, what the hell is wrong with the women in this house?!"
    pc "..."
    if hlo == 3:
        jump d10hcall
    else:
        jump d10takekathome
    
label d11jbeforl:
    scene d11beforel01 with dissolve
    pcthink "Hmm... looks good, no errors..."
    j "Bye, later, [e]!"
    scene d11beforel02 with dissolve
    j "Hey, whatcha doing?"
    scene d11beforel01 with dissolve
    pc "I was just checking the code one last time."
    scene d11beforel03 with dissolve
    j "Didn't you do that yesterday?"
    pc "Yeah, just making sure."
    scene d11beforel04 with dissolve
    j "You should spend some time with me instead, hehe."
    scene d11beforel05 with dissolve
    pc "I can't. I need to go to work today and I also have some papers I need to get to the rental company."
    scene d11beforel06 with dissolve
    j "Aww, what am I supposed to do then, all by myself?"
    scene d11beforel07 with dissolve
    pc "Sorry, [j], I'd give you my laptop, but I need it for work."
    if jlo >= 2:
        jump d11jbeforlsex
    else:
        jump d11jbeforll
label d11jbeforlsex:
    if _in_replay:
        show screen endRep
    scene d11beforel08 with dissolve
    j "Do you really have to go immediately, [pcmd]?"
    pc "Damn, don't look at me with those puppy eyes... I guess I have a bit of time..."
    scene d11beforel09 with dissolve
    j "Yay! I'll make it worth it, hehe."
    scene d11beforel10 with dissolve
    j "Let me put this away for you, so I can show you something, [pcmd]."
    scene d11beforel11 with dissolve
    if pcgender == "woman":
        pc "Hmh... go ahead, show me that cute little bum."
    else:
        pc "Hmh... go ahead, show me that sexy little ass."
    scene d11beforel12 with dissolve
    j "Of course, [pcmd]!"
    pc "No panties... naughty little girl."
    j "I thought I wouldn't need them today."
    scene d11beforel13 with dissolve
    pc "I see... too bad I don't have much time today."
    j "We still have the whole week though!"
    pc "Looks like it'll be a busy week."
    j "Hehe..."
    if pcgender == "woman":
        scene d11beforelff01 with dissolve
        pc "Come here, naughty little girl!"
        scene d11beforelff02 with dissolve
        j "Uhh, let me try something, [pcmd]."
        scene d11beforelff03 with dissolve
        pc "Hmm?"
        scene d11beforelff04 with dissolve
        j "Hey there!"
        pc "Wow, I didn't know you're this flexible."
        scene d11beforelff05 with dissolve
        j "Mmmmh, just need to get rid of these pants!"
        scene d11beforelff06 with dissolve
        j "Ready for some fun?"
        pc "Haha, crazy girl, go on."
        if pcgender == "woman":
            scene d11beforelff07 with dissolve
            j "Hmmm... yummie!"
            pc "Gawd, [j]!"
            j "Mmph... don't you want to lick my pussy, too, [pcmd]?"
            pc "Oh you bet!"
    scene black with dissolve
    $ pov1 = "d11jf1"
    $ pov2 = "d11jf2"
    $ povstart = True
    show screen povscreen(pov1)
    j "Haaa, yes, [pcmd]! Nhhh!"
    pause
    j "Hnnn, gawd!"
    if harem and jlo >= 2:
        j "Did you... haaa... like our little threesome yesterday, [pcmd]?"
        pc "Of course I did!"
        j "Nnnnh... I wish we could do it every night, nhaaa!"
        pc "Maybe one day..."
        j "Yes! Gawd..."
    j "We need to get [m] to allow us to sleep with you!"
    pc "Gawd, that would be great!"
    j "Maybe she'll even join us..."
    pc "Ha, I doubt that."
    j "Just imagine... haaah... all four of us having fun every night..."
    pc "You'd like that, wouldn't you?"
    j "Oh yes, [pcmd]!"
    if pcgender == "man":
        j "Imagine you fucking [e] right in front of her!"
    else:
        j "Imagine you and [e] licking each other right in front of her!"
    pc "Damn..."
    j "Hnnn..."
    pc "And what would you do?"
    j "Whatever you like me to do, [pcmd]."
    j "I could lick [e]'s other hole, or I could... hnnnn... lick [m]'s wet pussy... I could make out with her while you go down on all of us..."
    if pcgender =="man":
        j "You could fuck all our holes, one after the other... GAWD, [pcmd], you could fill each one of us with your juicy, hot cum!"
    pc "Jeez, [j], you're such a dirty little girl."
    j "Yes, [pcmd]!"
    if pcgender == "man":
        j "Hnnn... you can fill all my dirty little holes, [pcmd]!"
        menu:
            "Switch to her ass.":
                $ jass = True
                $ pov1 = "jfan1"
                $ pov2 = "jfan2"
                hide screen povscreen with dissolve
                hide screen povbutton with dissolve
                if campov:
                    show screen povscreen(pov2)
                else:
                    show screen povscreen(pov1)
                j "Oh gawd, yes, [pcmd]!"
                pcthink "So tight!"
            "Don't.":
                pass
    j "We could, haaaah... have sex all day... hnnnn!"
    pc "Gawd, damnit, [j]."
    j "Fuck! ....haaa... everywhere!"
    pc "Damn, that's so hot!"
    j "Hnnnn, yes, [pcmd]!"
    j "Oh gaaawd, I'm close, [pcmd]!"
    pc "Me too..."
    j "OH [pcmd], [pcmd]!"
    pc "Fuck!" with flash
    if pcgender == "woman":
        j "Gimme your juicy cum, [pcmd]!"
    else:
        j "Fill me up, [pcmd], I want to feel your hot cum inside me, [pcmd]!"
    pc "Shit!" with flash
    extend  " Shit!" with flash
    if pcgender == "woman":
        hide screen povscreen
        hide screen povbutton
        scene d11beforelffa with flash
        extend " Shit!" with vpunch
        scene black with slowdissolve
    else:
        hide screen povscreen
        hide screen povbutton
        scene d11fjcum with flash
        extend " Shit!" with vpunch
        scene black with slowdissolve
    if campov:
        scene d11jcum2 with dissolve
    else:
        scene d11jcum1 with dissolve
    j "Shiiit, that was great!"
    pc "Damn, you're crazy [j], but yes, it was."
    j "Haha."
    if pcgender == "man":
        scene black with dissolve
        scene d11beforelmf_clean02 with dissolve
        j "One more thing..."
        pc "Hm?"
        scene d11beforelmf_clean with dissolve
        j "Hmmmm..."
        pcthink "Damn, this girl is so naughty... I could almost go again, but I need to go..."
        scene d11beforelmf_clean02 with dissolve
        j "All clean!"
    pc "Alright, it was fun, but I really should get going now."
    j "Awww, already?"
    pc "Yeah, I don't know how long it'll take at work and I still need to get those papers to the rental company..."
    $ renpy.end_replay()
label d11jbeforll:
    j "Do you mind if I tag along?"
    pc "I don't, but I can't take you with me to my workplace."
    j "That's okay, I'll just do some window shopping."
    pc "Alright then."
    scene black with slowdissolve
    n "You head out and once you reach town you and [j] part ways."
    $ go_home = False
    $ gotowork = True
    scene bm-map with dissolve
    call screen wmap with dissolve
    
label d11stepladder:
    scene black with fade
    play sound "audio/door-opening.ogg"
    scene d11backhomej01 with dissolve
    pc "Hey, [j]. Whatcha doing?"
    j "Oh hey, the light bulb is..."
    scene d11backhomej02
    j "WHAA!"
    play sound "audio/drop.ogg"
    scene d11backhomej03 with hpunch
    pause .5
    scene d11backhomej04_2 with dissolve
    pc "Oh shit, are you alright?"
    j "Ouch... yeah I'm fine..."
    scene d11backhomej04 with dissolve
    pc "Did the {b}step{/b}-ladder molest you?"
    scene d11backhomej05 with dissolve
    j "Huh?"
    scene d11backhomej06 with dissolve
    j "W-What are you doing, step-ladder?"
    scene d11backhomej07 with dissolve
    pc "Haha!"
    scene d11backhomej08 with dissolve
    pc "You should've waited for me to fix it."
    if pcgender == "woman":
        scene d11backhomej09 with dissolve
        j "Why? Do you think I can't do that on my own?"
        scene d11backhomej10 with dissolve
        pc "No, but I'm taller than you, and I used to live alone for a long time, so I'm used to fixing stuff like that myself."
        scene d11backhomej11 with dissolve
        j "I'm not a helpless little girl you know..."
        if jlo >= 3:
            scene d11backhomej12 with dissolve
            j "...that is, unless [pcmd] wants me to be one... hehe."
            scene d11backhomej13 with dissolve
            pc "Heh, naughty little girl..."
        scene d11backhomej13 with dissolve
        pc "You know that's not what I meant."
        j "Yeah..."
    else:
        scene d11backhomej09 with dissolve
        j "Why? Do you think a woman can't fix stuff?"
        scene d11backhomej10 with dissolve
        pc "No, but if I'd think like that, you'd have just proven the point, haha."
        scene d11backhomej11 with dissolve
        j "Pffff, dick! It's your fault that I fell off the ladder!"
        scene d11backhomej11_2 with dissolve
        pc "Haha, I know, I know, just teasing."
        pc "But still, I'm taller than you, and I used to live alone for a long time, so I'm used to fixing stuff myself."
        scene d11backhomej14 with dissolve
        j "I bet you're just one of those guys who thinks a woman can't do anything on their own and should stay in the kitchen..."
        pc "What?!"
        scene d11backhomej15 with dissolve
        j "PFFWHAHAHAHA! You should see your face right now, haha!"
        pc "You dirty little..."
        if jlo >= 3:
            scene d11backhomej16 with dissolve
            j "Hehe, I've been a baaad girl, haven't I, [pcmd]?"
            pc "Oh yes, you have!"
            scene d11backhomej17 with dissolve
            j "Maybe you should spank me as punishment...[pcmd]..."
            scene d11backhomej18 with dissolve
            pc "I'd say that would be appropriate, little girl. You almost got me there..."
        scene d11backhomej19 with dissolve
        j "Hehe, don't worry, I don't care about that kinda stuff."
        scene d11backhomej20 with dissolve
        pc "And you shouldn't, I'm just trying to help."
    if jlo >= 3:
        scene d11backhomej21 with dissolve
        j "Hmm... thinking about it... yeah, why don't you fix it, I might as well enjoy the view, hehe."
        scene d11backhomej22 with dissolve
        pc "Huh? Oh well, of course you do..."
        j "Hehe."
    else:
        scene d11backhomej21 with dissolve
        j "Well, go ahead, I wont stop you."
    scene black with slowdissolve
    n "You change the bulb while [j] stabilizes you even though you tell her that you won't fall off the ladder. It's quite obvious that she isn't doing it to secure you from falling..."
    scene black with dissolve
    scene d11backhomej23 with dissolve
    pc "Alright, that takes care of that..."
    scene d11backhomej24 with dissolve
    pc "Uhh... where did you find the ladder by the way, [j]?"
    scene d11backhomej25 with dissolve
    j "In the shed."
    pc "Shed? Oh... right, there's a shed outside, I forgot..."
    scene d11backhomej26 with dissolve
    j "I'll take it back."
    pc "Okay."
    scene black with slowdissolve
    n "You go to your room."
    jump d11bhpcroom
    
label d12shed:
    pcthink "Alright, let's get the packaging to the shed..."
    scene black with slowdissolve
    n "You take the empty packaging to the shed."
    scene d12morningshed1 with dissolve
    pc "Shit..."
    pcthink "What a mess, everything's just put somewhere without any system..."
    pcthink "...I guess I'll have to make some room."
    scene black with slowdissolve
    scene d12morningshed2 with dissolve
    pcthink "Look at that, the old toolbox still exists. [mmom] must've forgotten about it."
    scene d12morningshed3 with dissolve
    pcthink "Eh... almost all of the tools are missing... oh well..."
    scene black with slowdissolve
    pause .7
    pcthink "There we go!"
    scene d12morningshed_done with dissolve
    pcthink "...Now there's more space even with the packaging in it."
    pcthink "Maybe I should tell the girls to not make it all messy again..."
    pcthink "..."
    pcthink "Hmm, time to head back in, I still have to fix some stuff for work..."
    scene black with slowdissolve
    scene d12morningjada01 with dissolve
    pause .7
    scene d12morningjada02 with dissolve
    pc "[j]?!"
    scene d12morningjada03 with dissolve
    j "Oh, there you are!"
    scene d12morningjada04 with dissolve
    play audio "audio/door-closing.ogg"
    pc "What are you doing here? Shouldn't you be at school?"
    scene d12morningjada05 with dissolve
    j "Err... well, yeah... you know... the thing is..."
    scene d12morningjada06 with dissolve
    pc "Don't tell me you got kicked out again."
    scene d12morningjada07 with dissolve
    j "I-It wasn't my fault!"
    scene d12morningjada08 with dissolve
    pc "Seriously, [j]."
    scene d12morningjada09 with dissolve
    j "Honestly, it really wasn't my fault, not this time!"
    scene d12morningjada10 with dissolve
    pc "Are you sure about that?"
    scene d12morningjada11 with dissolve
    j "Yes, a thousand percent!"
    scene d12morningjada12 with dissolve
    j "She was asking questions and always picked me to answer them, knowing very well that I can't answer them all..."
    scene d12morningjada13 with dissolve
    pc "And?"
    j "...I kept calm, and I answered what I was able to answer."
    scene d12morningjada14 with dissolve
    pc "So, what's the problem?"
    scene d12morningjada15 with dissolve
    j "She kept asking and asking..."
    scene d12morningjada16 with dissolve
    j "...and when I was struggling to answer, she made comments implying that I'm stupid!"
    scene d12morningjada17 with dissolve
    pc "And you called her names in response?"
    scene d12morningjada18 with dissolve
    j "No, I stopped answering."
    scene d12morningjada19 with dissolve
    pc "You stopped?"
    scene d12morningjada20 with dissolve
    j "Yes, I kept quiet."
    scene d12morningjada21 with dissolve
    pc "And she didn't like that."
    scene d12morningjada22 with dissolve
    j "She kicked me out for not taking part in classes..."
    pc "Really now?!"
    scene d12morningjada23 with dissolve
    j "Yes, even though I was answering all of her stupid questions before... as good as I could..."
    scene d12morningjada24 with dissolve
    pc "You didn't say anything offensive?"
    scene d12morningjada25 with dissolve
    j "No, nothing! I've been really nice!"
    scene d12morningjada26 with dissolve
    pc "{b}You{/b}'ve been nice?"
    scene d12morningjada27 with dissolve
    j "Yes, I've been acting of course, but I didn't say anything offensive. I didn't even hint at anything that could've been taken as offense..."
    scene d12morningjada28 with dissolve
    pc "I guess she wanted to get back at you."
    scene d12morningjada29 with dissolve
    j "Yes, that bitch just wanted to find a reason to kick me out."
    scene d12morningjada30 with dissolve
    pc "Did you apologize for last time?"
    scene d12morningjada31 with dissolve
    j "N-no?!"
    scene d12morningjada32 with dissolve
    pc "Maybe you should've done that."
    scene d12morningjada33 with dissolve
    j "Awwwww, I just hate her!!!"
    scene d12morningjada34 with dissolve
    pc "I know it sucks, [j], but you need to play along if you want to get a degree."
    j "Mmmh..."
    scene d12morningjada35 with dissolve
    j "I won't get a job anyway, even if I get a degree. My grades suck..."
    scene d12morningjada36 with dissolve
    pc "Hey, don't just give up, my grades sucked as well, and look at me now."
    j "..."
    scene d12morningjada37 with dissolve
    j "You know what?"
    pc "What?"
    scene d12morningjada38 with dissolve
    if jlo >=3:
        j "I'll just be your personal little whore, hehe."
        scene d12morningjada39 with dissolve
        pc "What?!"
        scene d12morningjada40 with dissolve
        j "Well, [e] will probably get a nice job, she has better grades than me, so she won't be home half the day."
        if not mend:
            j "[m] already has a job, so she also won't be home most of the time."
        if tc:
            j "...and [t] has a job as well, and one day her therapy sessions with [e] will end."
        scene d12morningjada41 with dissolve
        j "So, logically, I'll be the only one available for most of the day."
        scene d12morningjada42 with dissolve
        if pcgender == "man":
            j "I said it already, but you can fuck me whenever you want, and I'll suck your dick whenever you want."
            scene d12morningjada43 with dissolve
            j "I can suck it while you're working... I'll be sitting under the table, naked and suck it all day, like in some of those VN's, hehe."
            scene d12morningjada44 with dissolve
            j "And of course you can fill me with your seed all day, [pcmd]."
        else:
            j "I said it already, we can have sex whenever you want, and I'll lick your pussy whenever you want."
            scene d12morningjada43 with dissolve
            j "I can lick it while you're working... I'll be sitting under the table, naked, licking it and make you cum all day, like in some of those VN's, hehe."
            scene d12morningjada44 with dissolve
            j "And of course you can lick me too whenever you want, play with my body however you want, [pcmd]."
        pc "Damn it, [j]."
        
    else:
        j "I can be your personal maid!"
        scene d12morningjada39 with dissolve
        pc "What?!"
        scene d12morningjada40 with dissolve
        j "I'll bring you coffee in the morning, snacks in the afternoon..."
        scene d12morningjada43 with dissolve
        j "I'll make lunch for you... I'll clean the room for you... I can assist you in any way you want."
    scene d12morningjada45 with dissolve
    pc "Is that what you want to do with your life?"
    scene d12morningjada46 with dissolve
    j "Definitely, you know I like it here, I honestly think it would be nice!"
    scene d12morningjada47 with dissolve
    pc "Oh [j]..."
    scene d12morningjada48 with dissolve
    j "I mean it, I'd like that!"
    if jlo >=3:
        scene d12morningjada49 with dissolve
        pc "And you're sure you really want to be a whore?"
        scene d12morningjada50 with dissolve
        j "No, I don't want to be a whore! I want to be {b}your{/b} whore. Your personal one, and only yours, [pcmd]!"
    scene d12morningjada49 with dissolve
    pc "Hmm... Well, I'll think about it, under one condition."
    scene d12morningjada51 with dissolve
    j "Yay! I'll do it, whatever it is!"
    scene d12morningjada52 with dissolve
    pc "You'll apologize and get your degree."
    scene d12morningjada53 with dissolve
    j "Awww........"
    pc "That's the condition."
    scene d12morningjada54 with dissolve
    j "Fine... if I must..."
    scene d12morningjada55 with dissolve
    pc "I mean it, [j]."
    scene d12morningjada56 with dissolve
    j "Understood... I'll..."
    scene d12morningjada57 with dissolve
    j "I'll do it, promise."
    scene d12morningjada58 with dissolve
    pc "..."
    j "..."
    scene d12morningjada59 with dissolve
    j "So..."
    scene d12morningjada60 with dissolve
    j "...did you have fun with [m]?"
    if not mend:
        scene d12morningjada61 with dissolve
        pc "Huh? How do you..."
        scene d12morningjada62 with dissolve
        j "So you did! It worked! How was it?"
        scene d12morningjada61 with dissolve
        pc "Err... it was... wait, what worked?"
        scene d12morningjada63 with dissolve
        j "Uhh... nothing?"
        pc "[j]?"
        scene d12morningjada64 with dissolve
        j "What?"
        scene d12morningjada65 with dissolve
        pc "Did you suggest something to her while she was under the influence of the pills?"
        scene d12morningjada35 with dissolve
        j "I-I just told her that, if she wants to be closer to you, she has to leap over her own fence."
        scene d12morningjada36 with dissolve
        pc "That's all?"
        scene d12morningjada64 with dissolve
        j "Yes, I mean, it's obvious that she likes you, isn't it? She was just too scared to do something about it. It's not like I told her to do something naughty........ {size=-15}not directly{/size}."
        scene d12morningjada58 with dissolve
        pc "[j]."
        scene d12morningjada57 with dissolve
        j "Awww... I just told her that she has a great body and you'd probably like to see it, I didn't tell her to have sex with you..."
        scene d12morningjada58 with dissolve
        pc "Damn it, [j]..."
        scene d12morningjada57 with dissolve
        j "I-I just told her the truth, it's what you both wanted, and you both enjoyed it, didn't you?"
        scene d12morningjada58 with dissolve
        menu:
            "You're right, it helped.":
                scene d12morningjada60 with dissolve
                j "Right?! I actually wanted to suggest a lot more, but I wasn't sure if you'd be okay with that."
                scene d12morningjada61 with dissolve
                menu:
                    "You could've just asked me.":
                        scene d12morningjada64 with dissolve
                        j "But I wanted it to be a surprise... sorry."
                        scene d12morningjada66 with dissolve
                        pc "It was definitely unexpected."
                        scene d12morningjada60 with dissolve
                        j "Hehe, plan succeeded!"
                        if harem and jlo >= 3:
                            scene d12morningjada62 with dissolve
                            j "Sooo... now that your little harem is growing..."
                            j "Maybe we could use the pills to convince her to sleep in your bed with us, hehe."
                            scene d12morningjada61 with dissolve
                            menu:
                                "We better not play games with her mind.":
                                    scene d12morningjada59 with dissolve
                                    j "Oh... right, yeah, that might be a bad idea."
                                    scene d12morningjada58 with dissolve
                                    pc "We can try to convince her without the pills."
                                    scene d12morningjada56 with dissolve
                                    j "Yeah, but I doubt she'll ever agree..."
                                    scene d12morningjada58 with dissolve
                                    pc "Maybe she wont, but we'll have to accept it."
                                    scene d12morningjada59 with dissolve
                                    j "Yeah, I'd prefer it if she'd join us, but it's fine if she doesn't."
                                    scene d12morningjada67 with dissolve
                                "Sounds like a plan!":
                                    $ mindplayer = True
                                    scene d12morningjada51 with dissolve
                                    j "Yes! We'll have orgies every night, [pcmd]! I can't wait!"
                                    scene d12morningjada52 with dissolve
                                    pc "Heh, that might take some time."
                                    scene d12morningjada46 with dissolve
                                    j "Maybe, but I can wait!"
                                    scene d12morningjada47 with dissolve
                        elif not harem and jlo >= 3:
                            scene d12morningjada47 with dissolve
                            pc "You're aware that she's going to compete with you?"
                            scene d12morningjada46 with dissolve
                            j "Yeah..."
                            scene d12morningjada47 with dissolve
                        elif not harem and jlo <3:
                            scene d12morningjada61 with dissolve
                            pc "But you better don't do that again, [j]. Playing with peoples mind can be dangerous."
                            scene d12morningjada59 with dissolve
                            j "Yeah, you're right, maybe I shouldn't have done it at all..."
                            scene d12morningjada58 with dissolve
                            pc "Maybe, but now it's too late."
                            scene d12morningjada56 with dissolve
                            j "Yeah... damn it, I hope it wasn't a mistake..."
                            scene d12morningjada58 with dissolve
                            pc "Probably not, but don't risk it."
                            scene d12morningjada57 with dissolve
                            j "Right, now I'm feeling bad... I won't do it ever again!"
                            scene d12morningjada58 with dissolve
                    "You better not do that again.":
                        scene d12morningjada64 with dissolve
                        j "Awww, but it helped..."
                        scene d12morningjada58 with dissolve
                        pc "Playing with peoples mind can be dangerous, [j]."
                        scene d12morningjada56 with dissolve
                        j "Yeah, you're right, maybe I shouldn't have done it at all..."
                        scene d12morningjada55 with dissolve
                        pc "Maybe, but now it's too late."
                        scene d12morningjada57 with dissolve
                        j "Yeah... damn it, I hope it wasn't a mistake..."
                        scene d12morningjada58 with dissolve
                        pc "Probably not, but don't risk it."
                        scene d12morningjada59 with dissolve
                        j "Right, now I'm feeling bad... I won't do it ever again!"
                        scene d12morningjada58 with dissolve
            "That's not right.":
                pc "She trusts you, [j], and you betrayed her trust."
                scene d12morningjada57 with dissolve
                j "But I just wanted to help!"
                scene d12morningjada58 with dissolve
                pc "It's the wrong way, [j]!"
                scene d12morningjada56 with dissolve
                j "Awww, I'm sorry... I really just wanted to help..."
                j "Why do I always mess everything up..."
                scene d12morningjada55 with dissolve
                pc "Because you don't think before you act, and you really should start doing that if you don't want to lose everyone and everything that means something to you."
                pc "Shit, [oc] told me exactly the same once... and you know what?"
                scene d12morningjada57 with dissolve
                j "...What?"
                scene d12morningjada58 with dissolve
                pc "He was right, but I wasn't ready to see it, yet."
                scene d12morningjada59 with dissolve
                j "I know it's true... but I only ever realize it when it's too late..."
    else:
        scene d12morningjada61 with dissolve
        pc "Huh? What are you talking about?"
        scene d12morningjada62 with dissolve
        j "I saw her leaving when I came back."
        scene d12morningjada61 with dissolve
        pc "You saw her leaving? She left almost an hour ago."
        scene d12morningjada60 with dissolve
        j "I was walking, so it took me a while to get here."
        scene d12morningjada61 with dissolve
        pc "Why didn't you take the bus?"
        scene d12morningjada64 with dissolve
        j "I missed it by a few minutes..."
        scene d12morningjada66 with dissolve
        pc "Damn, you walked all the way from school?"
        scene d12morningjada68 with dissolve
        j "Yeah... it feels like my feet are almost falling off..."
        scene d12morningjada66 with dissolve
        pc "Well, at least you can relax now."
        scene d12morningjada64 with dissolve
        j "Yeah, finally..."
        scene d12morningjada60 with dissolve
        j "So, how was it?"
        scene d12morningjada61 with dissolve
        pc "How was what?"
        scene d12morningjada50 with dissolve
        j "You and [m]?"
        scene d12morningjada61 with dissolve
        pc "There was nothing, she just forgot something, she got it, and went back to work."
        scene d12morningjada48 with dissolve
        j "Really?"
        scene d12morningjada49 with dissolve
        pc "Yes, really."
        scene d12morningjada64 with dissolve
        j "Oh... how boring..."
        scene d12morningjada66 with dissolve
        pc "Do you want me to get something going with her?"
        if harem and jlo >=3:
            scene d12morningjada60 with dissolve
            j "Of course, more girls for your harem!"
            scene d12morningjada61 with dissolve
        elif harem and jlo <3:
            scene d12morningjada60 with dissolve
            j "Of course, you'd make a great couple, and [e] would be happy as well!"
            scene d12morningjada61 with dissolve
            pc "You think it would make [e] happy?"
            j "Mh-hm."
        elif not harem and jlo >=3:
            scene d12morningjada60 with dissolve
            j "Why not? I don't mind, [e] would be happy, and maybe I can watch you two in the future, hehe."
            scene d12morningjada61 with dissolve
            pc "You think [e] would like me to be with [m]?"
            scene d12morningjada60 with dissolve
            j "Yeah, sure..."
            scene d12morningjada61 with dissolve
    pc "..."
    pcthink "[j] is really a weird one... sometimes I'm not even sure if she's being honest or not..."
    scene d12morningjada36 with dissolve
    j "..."
    pc "Hm?"
    scene d12morningjada69 with dissolve
    j "Aaaaawww, I can't do this anymore..."
    pc "Huh? What? What are you talking about?"
    scene d12morningjada70 with dissolve
    j "..."
    pc "[j]?"
    scene d12morningjada71 with dissolve
    j "...dammit... shit..."
    pc "What the hell is wrong, [j]?!"
    scene d12morningjada72 with dissolve
    j "It's... I think..."
    pcthink "What's wrong with her now?"
    scene d12morningjada73 with dissolve
    j "I like you, okay? And it's because of [e]... I just can't..."
    play sound "audio/door-opening.ogg"
    "voice" "{size=+15}[j]!{/size}" with hpunch
    scene d12morningjada74 with dissolve
    pc "[e]?!"

$ renpy.run_action(QuickSave())
scene black with dissolve
pause .5
jump endGame