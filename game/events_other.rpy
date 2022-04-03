label cafeBeforeOffice:
    pc "Hey, [h]!"
    scene coffeehouse3_1 with dissolve
    if hlo > 0:
        h "Oh, hey, [pc]! Back so soon? Haha."
        pc "Yeah, something seems to draw me back here... or maybe someone."
        h "Haha, I wonder who that might be?"
        pc "I have no clue. *Smirk*"
        scene coffeehouse3_2 with dissolve
        h "I just hope you didn't expect my hairy, grumpy co-worker today."
        pc "Ugh... No way!"
        scene coffeehouse3_1 with dissolve
        h "Haha!"
    else:
        h "Oh, hey it's you again!"
        pc "Yeah, sorry about yesterday, I had to run."
        h "Haha, don't worry, my shift started anyway."
        pc "[pc]..."
        h "Huh?"
        pc "That's my name."
        h "Oh! Yes! Nice to meet you, [pc]. My name is [h], and yes I know I told you already, haha."
        pc "Heh... nice to meet you, too, [h]... again."
    scene coffeehouse3_2 with dissolve
    h "So~ how can I make your day better?"
    pc "Well, I have some ideas, but I'll take a coffee for now."
    scene coffeehouse3_1 with dissolve
    h "Haha, sure, why don't you sit down and I'll bring it over to you in a minute."
    pc "Yeah, thanks."
    scene black with dissolve
    pause 1
    scene coffeehouse3_3 with dissolve
    h "Here we go~"
    h "A special coffee on the house!"
    pc "On the house? Thanks, that looks interesting, what is it?"
    h "Haha, it's coffee, don't worry, it's not poisoned."
    pc "Oh that sounds fishy."
    h "Haha, try it, I bet you'll love it!"
    scene black with dissolve
    pause 1
    scene coffeehouse3_4 with dissolve
    h "So you haven't been here for six years?"
    pc "Yeah."
    h "Wow, I bet you've seen a lot of the world. I've never left town."
    pc "You've never been somewhere else? Not even on holidays?"
    h "No, sadly... I'm a bit jealous I must say. Haha."
    pc "What about class trips, excursions and the like?"
    h "My family is a bit antiquated, they didn't let me leave the country, not even for a week."
    pc "But you don't even need to leave the country to discover interesting places and they can't keep you forever."
    h "I know, but I'm a bit too scared to travel alone, haha."
    scene coffeehouse3_5 with dissolve
    if pcgender == "man":
        h "...but I'm still hoping that someday a gallant hero comes by and..."
    else:
        h "...but I'm still hoping that someday a gallant hero{size=-15}{i}ine{/i}{/size} comes by and..."
    scene coffeehouse3_4_2 with dissolve
    h "Ahaha... welp, I guess I'm a bit old fashioned myself, haha."
    play sound "audio/shop-chime.ogg"
    scene coffeehouse3_6 with dissolve
    pc "Haha, there's nothing wrong with that and I'd love to show you a few places some day, but right now it looks like work is calling you..."
    scene coffeehouse3_7 with dissolve
    h "Aww, too bad, but that would be awesome!"
    scene coffeehouse3_9 with dissolve
    pause 1
    pcthink "Shit, it looks like it's going to start to raining soon, I guess I should be leaving."
    scene coffeehouse3_9_1 with dissolve
    pc "See you soon, [h], I've got to go."
    scene coffeehouse3_9_2 with dissolve
    if pcgender == "man":
        h "Ah-Ohh... please wait, sir!"
    else:
        h "Ah-Ohh... please wait, ma'am!"
    pc "Huh?"
    scene coffeehouse3_10 with dissolve
    if pcgender == "man":
        h "Didn't you want to have the bill, sir?"
    else:
        h "Here's the bill, ma'am?"
    pc "The bill? I thought the coffee was on the..."
    h "*Cough*"
    scene coffeehouse3_11 with dissolve
    pause 2
    pc "Ohh! Yeah, the bill, I almost forgot about it... thanks."
    scene coffeehouse3_12 with dissolve
    if pcgender == "man":
        h "Anytime, sir. Have a good day~"
    else:
        h "Anytime, ma'am. Have a good day~"
    pc "Thanks, you too. Bye~"
    scene coffeehouse3_9_2 with dissolve
    pcthink "Wow... I guess it was the right decision to come here."
    scene city_6 with dissolve
    pcthink "Well, let's see what the office looks like..."
    $ hlo += 1
    $ hnumber = True
    jump officeFirst
    
label cafe_d6:
    if hlo == 3:
        play sound "audio/shop-chime.ogg"
        scene coffeehouse_d6 with dissolve
        pcthink "Huh? isn't that the guy from the other shift?"
        scene coffeehouse_d6_2 with dissolve
        "Guy" "Humph..."
        pcthink "Hum?"
        scene coffeehouse_d6_h1 with dissolve
        h "Oh hey, [pc]!"
        pc "Hey, [h]."
        scene coffeehouse_d6_h2 with dissolve
        h "You're early, haha. Just take a seat, I'll be there in a minute."
        pc "Alright."
        scene coffeehouse_d6_h3 with slowdissolve
        h "...and here's your mocha!"
        "Woman" "Thanks [h]."
        h "Enjoy~"
        scene coffeehouse_d6_h4 with dissolve
        h "I'll be right there, [pc]."
        pc "No rush."
        scene coffeehouse_d6_h5 with fade
        h "Here we go, [h] special on the house, haha."
        pc "Thanks, [h]. Why don't you sit down for a while?"
        h "Yes, of course!"
        scene coffeehouse_d6_h6 with dissolve
        pc "Say, was that your co-worker leaving a bit earlier?"
        h "Ehh... yeah, haha. He forgot something and came back for it."
        pc "Oh, okay..."
        scene coffeehouse_d6_h7 with dissolve
        h "Sooo... how was your day? I mean, how {b}is{/b} your day... I mean how are you today, haha!"
        pc "Haha, I'm good, how about you? You seem happy today."
        scene coffeehouse_d6_h8 with dissolve
        h "Oh I... just happen to have some nice customers today."
        pc "Really? Someone special?"
        scene coffeehouse_d6_h9 with dissolve
        h "Maaaaybe... haha."
        scene coffeehouse_d6_h8 with dissolve
        pc "Do I know him?"
        if pcgender == "woman":
            h "Why do you think that it's a \"him\"?"
        scene coffeehouse_d6_h10_2 with dissolve
        "Woman" "Hey, [h], is [heshe] the reason why you're working on your day off?"
        scene coffeehouse_d6_h10 with dissolve
        h "Ehh...hahah, I have no idea what you're talking about, Jenny..."
        "Woman" "No? Didn't you just storm in here 10 minutes ago, and begged Jason to take his shift?"
        scene coffeehouse_d6_h10_3 with dissolve
        h "Whaa, nonono, you got it all wrong!"
        scene coffeehouse_d6_h10_2 with dissolve
        "Woman" "She even put perfume on while coming half changed out of the locker room."
        scene coffeehouse_d6_h11 with hpunch
        h "I-I'll be right back..."
        scene coffeehouse_d6_h13 with dissolve
        h "*Whisper*"
        scene coffeehouse_d6_h12 with dissolve
        pc "..."
        scene coffeehouse_d6_h14 with dissolve
        pcthink "Damn, I can't understand what they're talking about..."
        scene coffeehouse_d6_h15 with dissolve
        pcthink "But it's really cute that she spends her day off working just because of me."
        scene coffeehouse_d6_h16 with dissolve
        h "Hehe..."
        scene coffeehouse_d6_h17 with dissolve
        h "They were just joking of course, haha."
        pc "Sure... *smirk*"
        scene coffeehouse_d6_h18 with dissolve
        h "Ugh... this is so embarrassing..."
        pc "Haha, don't worry, I think it's cute."
        scene coffeehouse_d6_h19 with dissolve
        h "Unn... really?"
        pc "I do."
        h "..."
        pc "How about we meet somewhere else next time, so you don't have to beg your co-worker to change the shift last minute?"
        scene coffeehouse_d6_h20 with dissolve
        h "You mean like... a date?"
        pc "I mean a date, yes."
        scene coffeehouse_d6_h6 with dissolve
        h "Haha, yes! I'd love to!"
        pc "Great, when do you have time? This weekend?"
        scene coffeehouse_d6_h21 with dissolve
        h "Anytime!"
        scene coffeehouse_d6_h7 with dissolve
        h "I mean... when I'm not working of course, haha."
        pc "Alright, so, this weekend?"
        scene coffeehouse_d6_h6 with dissolve
        h "Yes!"
        pc "Oh wait... aren't you working over the weekend?"
        h "Ehh... oh yes... but I can take a day off, since I'm working today anyway, haha."
        pc "No need to take a day off for me, when is your next regular day off?"
        h  "Oh but I don't mind, really. My next regular day off is not until next week."
        pc "Hum... you really don't mind?"
        h "No, really!"
        pc "Alright, this weekend it is then."
        h "Yay, haha!"
        pc "Is there anywhere you want to go?"
        h "Where ever you want to go."
        pc "Well, I'll be honest, the city changed a lot since I moved away, so I'm not sure I'll pick the best place."
        h "Oh, right..."
        h "Leave it to me then, I'll find something!"
        pc "Okay, sounds good."
        play sound "audio/shop-chime.ogg"
        scene coffeehouse_d6_h22 with dissolve
        pc "Looks like you got some customers."
        scene coffeehouse_d6_h24 with dissolve
        h "Oh, yeah, I'll be right back."
        scene coffeehouse_d6_h25 with dissolve
        pc "Yeah, I won't run away."
        scene black with dissolve
        pc "*Slurp*"
        play sound "audio/shop-chime.ogg"
        scene coffeehouse_d6_h26 with fade
        h "Alright, all customers satisfied, haha."
        pc "Looks like you have to satisfy one more..."
        scene coffeehouse_d6_h27 with dissolve
        h "Ugh... alright, one minute~"
        pc "I'll be here."
        scene coffeehouse_d6_h28 with dissolve
        pc "*Slurp*"
        scene black with fade
        play sound "audio/shop-chime.ogg"
        scene coffeehouse_d6_h29 with dissolve
        pcthink "Even more customers..."
        scene black with fade
        scene coffeehouse_d6_h30 with dissolve
        pc "..."
        scene black with fade
        play sound "audio/shop-chime.ogg"
        scene coffeehouse_d6_h32 with dissolve
        pc "...and another one..."
        scene coffeehouse_d6_h31 with dissolve
        pc "Hum..."
        scene coffeehouse_d6_h32 with dissolve
        pcthink "Damn, the customer onrush doesn't seem to stop..."
        scene coffeehouse_d6_h33 with dissolve
        pcthink "I bet she feels guilty for making me wait for so long..."
        scene coffeehouse_d6_h31 with dissolve
        pc "..."
        pcthink "Shit, I guess it's time to leave."
        scene coffeehouse_d6_h34 with dissolve
        pc "Hey [h], I'm leaving, do you mind if I text you later?"
        scene coffeehouse_d6_h35 with dissolve
        h "Of course!"
        h "Ah, I mean, no of course I don't mind, haha!"
        pc "Haha, okay later then."
        h "Later, [pc]~"
    else:
        pcthink "Alright, time for coffee..."
        scene coffeehouse_d6_aran with dissolve
        pc "..."
        pcthink "Maybe I should have brought the notebook..."
        pc "..."
        pcthink "Well, time to finish the coffee and go on..."
    $ gotocafe = False
    scene black with fade
    $ visit_cafe_d6 = True
    call screen wmap


label job_d6:
    $ SEWork = 2
    scene job_d6_1 with dissolve
    pcthink "Look who's there..."
    st "...and then you can bring the new components to the testing area."
    "Guy" "Okay."
    scene job_d6_2 with dissolve
    pc "Hey, [st]."
    scene job_d6_3 with dissolve
    st "Huh? What are you doing here?"
    scene job_d6_4 with dissolve
    pc "Yeah, it's good to see you, too..."
    st "Shouldn't you be working on the project? Do you need additional information?"
    pcthink "Jeez, is it all work to her? I guess I'll have to approach her a little bit differently if I want to get on good terms with her..."
    scene job_d6_5 with dissolve
    pc "I'm just having a break, and I thought I'd come over and see if there's anything new regarding the project."
    scene job_d6_6 with dissolve
    st "That's...commendable... but the project didn't change, and [boss] is on a business trip until next week."
    scene job_d6_5 with dissolve
    pc "Oh, he didn't tell me."
    scene job_d6_6 with dissolve
    st "He told me to give you any additional information you might need in the meantime."
    scene job_d6_5 with dissolve
    pc "I see..."
    scene job_d6_6 with dissolve
    st "Well if you don't need anything... I have a lot to do, and I'm sure you do, too."
    scene job_d6_5 with dissolve
    pcthink "This might be a good chance..."
    menu:
        "Ask if she needs help.":
            $ stl += 1
            pcthink "I should try to find out what she's going to do first, just asking if she needs help won't get me anywhere..."
            pc "I really don't want to be a pain, but I'm curious about how everything works here, so... what exactly do you do?"
            scene job_d6_6 with dissolve
            st "Well... I'm [boss]'s secretary..."
            scene job_d6_5 with dissolve
            pc "Yeah, he told me as much, but he also told me that you do way more than just being an ordinary secretary."
            scene job_d6_6 with dissolve
            st "What do you mean? I'm just doing my job!"
            scene job_d6_5 with dissolve
            pc "He didn't tell me exactly what he meant, that's why I'm asking..."
            scene job_d6_6 with dissolve
            st "Hum... I have no idea what he meant by that."
            scene job_d6_5 with dissolve
            pc "Weird... what kind of work are you going to do now?"
            scene job_d6_6 with dissolve
            st "Nothing special, I'll just manage the archive, but I have a lot of paperwork and other things to do as well today."
            scene job_d6_5 with dissolve
            pc "Manage the archive?"
            scene job_d6_6 with dissolve
            st "...sorting, and typing values into the computer..."
            pcthink "Ha! Perfect!"
            scene job_d6_5 with dissolve
            pc "Oh that sounds tedious... do you need help?"
            scene job_d6_6 with dissolve
            st "It is, but it's my job. Your job is something else."
            scene job_d6_5 with dissolve
            pc "True, but as I said, I'm having a break right now, and I made a little breakthrough yesterday, so I can afford to spend time on something else."
            scene job_d6_6 with dissolve
            st "That's... nice, but I know the archive better than anyone else, and I'll be faster without any distraction."
            scene job_d6_5 with dissolve
            pcthink "So I'm distracting her, huh?"
            pc "Didn't you say you have to type values into the computer?"
            scene job_d6_6 with dissolve
            st "Yes..."
            scene job_d6_5 with dissolve
            pc "Well typing values into the computer basically is my job, so if I do the typing, we'd be done way faster then when you do it on your own."
            scene job_d6_7 with dissolve
            st "That... might be true..."
            pc "...and you'll have more time for other important things, right?"
            st "... that's also true..."
            scene job_d6_8 with dissolve
            st "Alright, you can help me, but please don't touch anything, the archive is messy enough already."
            scene job_d6_9 with dissolve
            pc "Sure..."
            scene job_d6_sort1 with fade
            st "As you can see, the archive is quite a mess, we moved all the files from the old archive and I'm still sorting things out."
            pc "Looks like a lot of work. I guess you really could use a helping hand."
            scene job_d6_sort2 with dissolve
            st "As I said, it's my job."
            scene job_d6_sort3 with dissolve
            st "There is the computer, please have a seat and let us begin."
            pc "Sure..."
            scene black with fade
            n "A while later..."
            scene job_d6_sort5 with dissolve
            st "G55... same value..."
            pc "Uh-huh..."
            st "G56... same value..."
            pc "Of course..."
            pcthink "Maybe this wasn't the best idea..."
            st "G57... same value..."
            pc "Yeah..."
            pcthink "Gaaawd, why did I ask to help her?! This is so annoying..."
            st "Ugh... the box is a bit stuck..."
            scene job_d6_sort6 with dissolve
            pcthink "Wow, but that's a nice view..."
            st "F49..."
            scene job_d6_sort7 with dissolve
            st "Where are you?"
            pc "Sh... "
            scene job_d6_sort8 with dissolve
            st "Are you staring at my..."
            pc "Err, no, of course not!"
            pcthink "Shit, she has caught me, who am I trying to kid."
            st "Pervert!"
            pc "I'm sorry, it was an accident I swear! It's just that... err... you're... you're beautiful?!"
            pcthink "Shit, I hope that works!"
            st "B-B-Beauti..."
            scene job_d6_sort9 with dissolve
            st "Whaaa~"
            scene job_d6_sort10 with dissolve
            pcthink "Ohhh sheet!"
            scene job_d6_sort11 with hpunch
            st "Au..."
            pc "Uhh..."
            pause 2
            scene job_d6_sort12 with vpunch
            st "I'm sorry, I'm sorry!"
            scene job_d6_sort13 with dissolve
            st "I'm really sorry, it wasn't on purpose, I just stumbled!"
            pcthink "Phew, lucky me, now the tables turned."
            pc "Heh, it's okay, nobody died."
            scene job_d6_sort14 with dissolve
            st "...I...I...I..."
            pc "Are you okay?"
            pcthink "Damn, how flustered she is..."
            st "...I will do the rest of the work on my own, thank you for your help..."
            pc "Err..."
            st "Good bye..."
            pc "Hey, this really wasn't..."
            st "Please leave..."
            pc "..."
            pcthink "Shit... I guess it doesn't matter what I say right now, she seems to have completely shut herself off..."
            pc "Alright, I'll leave... but hey, we both are alright, nothing bad happened, right?"
            st "..."
            scene job_d6_sort15 with dissolve
            pcthink "Shit, this didn't work out like expected!"
            scene job_d6_sort16 with dissolve
            pc "Bye, [st]..."
            st "..."
            pcthink "Damn..."
        "Leave":
            pcthink "Or it might annoy her... I better leave."
            pc "You're right, have a good day, [st]."
    $ gotowork = False
    scene black with fade
    $ visit_work_d6 = True
    call screen wmap

label porngirls:
    $ gotowork = False
    scene d9_city01 with dissolve
    pcthink "Let's see if anybody else is working today at the company."
    pcthink "It wouldn't surprise me if [st] is the only one working today..."
    scene d9_city02 with dissolve
    if stl == 1:
        pcthink "I just hope she forgot about what happened last time and that she's a bit more relaxed today..."
    else:
        pcthink "I wonder if [boss] is still on that business trip... [st] seems to be a bit more relaxed around him..."
    scene d9_city03 with dissolve
    pcthink "Huh?"
    scene d9_city04 with dissolve
    pcthink "Have I seen her before?"
    play sound "audio/drop.ogg"
    scene d9_city05 with dissolve
    "{color=#570058}Girl1{/color}" "Ouch!" with hpunch
    scene d9_city06 with dissolve
    pc "Whoa, shit!"
    scene d9_city07 with dissolve
    "{color=#cc5dcd}Girl2{/color}" "What the fuck!? Can't you watch out?"
    pc "Sorry I was distracted!"
    "{color=#cc5dcd}Girl2{/color}" "Obviously, Idiot!"
    pc "Hey, she didn't watch out either!"
    "{color=#570058}Girl1{/color}" "Unn..."
    scene d9_city06 with dissolve
    pause .5
    scene d9_city08 with dissolve
    menu:
        "Help her up.":
            $ pgirls = True
            scene d9_city09 with dissolve
            pc "Sorry, I was lost in thought..."
            scene d9_city10 with dissolve
            "{color=#570058}Girl1{/color}" "It's okay, I didn't watch out either."
            pc "Are you okay?"
            "{color=#570058}Girl1{/color}" "Yes, I'm good, thanks."
            scene d9_city11 with dissolve
            "{color=#cc5dcd}Girl2{/color}" "Come on [em], don't waste time with [himher]!"
            scene d9_city12 with dissolve
            em "Sorry, we're in a hurry."
            scene d9_city13 with dissolve
            "{color=#cc5dcd}Girl2{/color}" "What an idiot..."
            em "Hey, it's not [hisher] fault, [jess]..."
            pcthink "Hmm... where did I see them before?"
            #achievement
            $achievement.grant("Achievement_pg21")
            init: 
                $achievement.register("Achievement_pg21")
            $achievement.sync()
            ###########
        "Ignore them.":
            if pcgender == "man":
                scene d9_city14 with dissolve
                "{color=#cc5dcd}Girl2{/color}" "What an idiot!"
                pc "Bitch!"
            else:
                scene d9_city14 with dissolve
                "{color=#cc5dcd}Girl2{/color}" "What a bitch!"
                scene d9_city13 with dissolve
                pc "Thanks, same to you too..."
    scene black with fade
    scene d9_job01 with dissolve
    pcthink "Alright, I guess I should have a look if [boss] is here, too..."
    scene black with dissolve
    pause .5
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    boss "Yes!"
    play sound "audio/door-opening.ogg"
    scene d9_job03 with dissolve
    boss "Heyyyy, [pc], what brings you here?"
    scene d9_job04 with dissolve
    pc "Hey, [boss], I need some files that seem to be missing from the project, so I thought I'd come by."
    scene d9_job05 with dissolve
    boss "Missing files huh? What exactly is missing?"
    scene d9_job04 with dissolve
    pc "I'm not exactly sure, but I called [st] and she seems to have some ideas."
    if stl > 0:
        scene d9_job06 with dissolve
        boss "Oh? So that's why..."
        pc "Huh?"
    scene d9_job05 with dissolve
    if stl == 0:
        boss "I see..."
    boss "She's in the archive, sorting stuff. Tell her to get me a coffee when she's done, would'ya?"
    scene d9_job04 with dissolve
    pc "Sure, I'll tell her."
    scene black with dissolve
    pcthink "He seems to be the typical \"I don't care as long as stuff works\" kind of guy..."
    scene d9_job08 with dissolve
    pcthink "I wonder what happens if one day \"stuff\" doesn't work..."
    scene black with dissolve
    scene d9_job09 with dissolve
    pcthink "Hmm looks like she's still not done sorting stuff..."
    scene d9_job10 with dissolve
    pc "Hey, [st]!"
    scene d9_job11 with hpunch
    st "WHAAA!"
    scene d9job12 with dissolve
    pc "Haha, it's just me, sorry I didn't mean to scare you."
    scene d9job13 with dissolve
    st "[pc]?!"
    scene d9_job14 with dissolve
    st "Oh right..."
    scene d9job15 with dissolve
    st "I found the missing files and saved them on a usb-stick."
    scene d9job16 with dissolve
    pc "Wow, thanks, you're quick."
    scene d9job17 with dissolve
    pc "I thought I'd have to search for it."
    if stl > 0:
        pc "Hmm? You look kinda different today..."
        scene d9_job18 with dissolve
        st "I-I don't know what you mean."
        pc "I'm sure there's something different about you..."
        menu:
            "Must be her clothes.":
                $ stl = 0
                pc "Must be the clothes then..."
                scene d9job17 with dissolve
                st "..."
                scene d9_job21 with dissolve
                st "I still have a lot to do..."
                pc "Uhh... well okay, I'll leave you to your work then..."
                st "..."
                scene d9_job25 with dissolve
                pc "Damn, I don't get that woman..."
                scene black with slowdissolve
                call screen wmap
            "(Joke) It's the hair!":
                pc "You changed your hairstyle, didn't you?"
                scene d9job17 with dissolve
                st "..."
                pc "Haha, don't look at me like that, I'm joking!"
            "Make-up and glasses.":
                pass
        #achievement
        $achievement.grant("Achievement_stmakeup")
        init: 
            $achievement.register("Achievement_stmakeup")
        $achievement.sync()
        ###########
        $ stl +=1
        pc "You're not wearing your glasses and put some make-up on."
        scene d9_job19 with dissolve
        st "O-oh you noticed?"
        pc "Of course, you look great!"
        scene d9_job20 with dissolve
        st "..."
        scene d9_job21 with dissolve
        st "I-I still have a lot to do..."
        scene d9_job22 with dissolve
        pc "I can help you if you want."
        scene d9_job23 with dissolve
        st "I-I'm almost done anyway!"
        scene d9_job24 with dissolve
        st "...but thanks..."
        scene d9_job22 with dissolve
        pc "Alright, I'll leave you to your work then, thanks again, [st]."
        scene d9_job21 with dissolve
        st "Anytime."
        scene d9_job25 with dissolve
        pcthink "Wow, she can be really cute."
        scene d9_job26 with dissolve
        scene d9_job27 with dissolve
        pcthink "Heh..."
        pc "Bye, [st]."
        st "...bye."
        scene black with slowdissolve
        call screen wmap
    else:
        scene d9_job21 with dissolve
        st "I found it while going through some other data, it was a lucky coincidence..."
        pc "I see, well thanks, [st]."
        st "..."
        pc "Alright, I'll leave you to your work then, thanks again, [st]."
        st "Anytime."
        scene d9_job25 with dissolve
        pcthink "Alright, time to leave..."
        scene black with slowdissolve
        call screen wmap

label maggy1:
    $ go_home = True
    play sound "audio/knock-door1.ogg"
    n "*Knock* *Knock*"
    ma "Yes?"
    play sound "audio/door-opening.ogg"
    scene maggy_office1 with dissolve
    ma "Oh, you must be [pc], welcome, sit down please, I'll be ready in a minute."
    pc "Yeah, thanks."
    scene maggy_office2 with dissolve
    pcthink "Hum, she's older than I thought."
    pcthink "Still a nice butt, though!"
    scene maggy_office3 with dissolve
    ma "I'm sorry, we had a database crash right after I called you, so it's all haywire now."
    pc "Damn, that's awful, but no worries, I have time."
    scene maggy_office4 with dissolve
    ma "Can I get you something? A coffee maybe? Or something else?"
    pc "Thanks, I'm good."
    scene maggy_office5 with dissolve
    ma "Okay, well..."
    n "*Rrrrring*"
    scene maggy_office6 with dissolve
    pause .5
    n "*Rrrrring*"
    scene maggy_office7 with dissolve
    ma "I'm sorry, one second."
    scene maggy_office8 with dissolve
    ma "Yes?"
    scene maggy_office9 with dissolve
    pcthink "Looks like she's had a tough day."
    scene maggy_office10 with dissolve
    ma "No, I'm sorry, I know you need these files, but this has to wait until Monday. The database is still..."
    pcthink "I bet {b}she{/b} could use a coffee right now..."
    scene maggy_office11 with dissolve
    pcthink "Or maybe something a bit more relaxing."
    ma "Thank you for your understanding, bye..."
    play sound "audio/hangup.ogg"
    scene maggy_office12 with dissolve
    ma "I'm really sorry, I hope that was the last one for today..."
    scene maggy_office12_2 with dissolve
    pc "Isn't worktime over already?"
    scene maggy_office12 with dissolve
    ma "Yes, but with the current situation..."
    scene maggy_office12_2 with dissolve
    pc "I see..."
    pcthink "Maybe I should try to cheer her up and see where things go."
    menu:
        "(Yeah, she's hot, so let's try!)":
            $ datemaggy = True
            pc "You know, thinking about it, I guess I could use a drink."
            scene maggy_office13 with dissolve
            ma "Sure, what can I get you? A coffee?"
            pc "I was thinking of something a bit more..."
            scene maggy_office11 with dissolve
            pc "Relaxing..."
            scene maggy_office14 with dissolve
            ma "Hm?"
            scene maggy_office15 with dissolve
            ma "Ooooh... haha, right, I guess a glass won't hurt after a day like today"
            scene maggy_office16 with dissolve
            ma "Shall we go over to the seating area?"
            pc "Sure!"
            scene black with slowdissolve
            scene maggy_office18 with dissolve
            pc "...and that's basically what happened."
            scene maggy_office17 with dissolve
            ma "So you moved back to your old house because there was no other apartment available?"
            scene maggy_office19 with dissolve
            pc "Yeah."
            scene maggy_office17 with dissolve
            ma "That's good, isn't it? I'd like to spend more time with my family as well."
            scene maggy_office18 with dissolve
            pc "Family... well [m] is {b}{i}not{/i}{/b} my mom, and [e]..."
            scene maggy_office17 with dissolve
            ma "But they're still family, aren't they? Did you ever call [m] mom?"
            scene maggy_office18 with dissolve
            pc "Err, well..."
            scene maggy_office17 with dissolve
            ma "Or are you more interested in... {i}other{/i} things regarding her?"
            pc "What?!"
            ma "Oh sorry, I shouldn't ask questions like that... let's change the subject, shall we?"
            scene maggy_office19 with dissolve
            pc "Yeah... there are more interesting topics than that..."
            scene maggy_office18 with dissolve
            pc "..."
            scene maggy_office17_2 with dissolve
            ma "So, how do you like the city, is it still like you remember it?"
            scene maggy_office19_2 with dissolve
            pc "It has changed a lot since back then... but it's okay I guess."
            scene maggy_office17_2 with dissolve
            ma "Did you meet any old friends?"
            scene maggy_office18_2 with dissolve
            pc "Friends? No, not really..."
            scene maggy_office17_2 with dissolve
            ma "That's too bad, but I bet someone like you will find new friends easily."
            scene maggy_office19_2 with dissolve
            pc "Someone like me?"
            scene maggy_office17_2 with dissolve
            ma "Well... you seem to be a nice person, you're young and..."
            scene maggy_office19_2 with dissolve
            pc "...and?"
            scene maggy_office17_2 with dissolve
            ma "Well..."
            scene maggy_office18_2 with dissolve
            pause .5
            scene maggy_office17_2 with dissolve
            ma "You're a good looking [pcgender]..."
            if pcgender == "man":
                ma "I bet a lot of girls are hitting on you, I know I would if I were a bit younger."
            else:
                ma "I bet a lot of guys are hitting on you, maybe even some girls..."
                pc "I'm not into guys."
                ma "Oh? Well that's interesting... if I were a bit younger..."
            pc "Oh come on, you're not old, and you're a beautiful woman!"
            ma "Oh? Is that so?"
            scene maggy_office18_2 with dissolve
            pc "Absolutely."
            scene maggy_office20 with dissolve
            ma "Why thank you!"
            scene maggy_office22 with dissolve
            n "*Rrrrring*"
            ma "Oh goddamnit!"
            scene maggy_office21 with dissolve
            ma "One second I'll just cut off whoever it is and activate the voice mail..."
            pc "Mhm, good..."
            scene maggy_office23 with dissolve
            pcthink "Heh, looks like this will be a good afternoon."
            scene maggy_office24 with dissolve
            ma "Really? Now?"
            scene maggy_office25 with dissolve
            ma "Uhh... yes, of course!"
            pcthink "...or not?"
            play sound "audio/hangup.ogg"
            scene maggy_office26 with dissolve
            ma "That was my boss, he's going to come over to get some papers..."
            scene maggy_office27 with dissolve
            pc "Damn, guess that means I'll have to go?"
            scene maggy_office27_2 with dissolve
            ma "Yes, I'm sorry. We have a few minutes so we can get your papers done at least."
            scene maggy_office28 with dissolve
            pc "Well, let's get it done then..."
        "(Nah, I better let her be, I'm not interested anyway.)":
            scene maggy_office12_2 with dissolve
            pc "Well I don't want to keep you busy for too long..."
    scene maggy_office29 with dissolve
    ma "Right, sorry, I just need your signature on some papers to make the transaction..."
    scene black with dissolve
    n "You quickly go through the papers without taking much note of the content and sign them all."
    scene maggy_office30 with dissolve
    ma "Okay, here are your copies to keep."
    pc "Thanks, [ma]."
    scene maggy_office31 with dissolve
    ma "Sorry for the hassle."
    pc "No problem, it's not your fault anyway."
    scene black with dissolve
    n "You say good bye, leave the building and make your way back home..."
    scene black with dissolve
jump d9_backhome

label d10hcall:
    n "*Phone rings*"
    scene d10hannacalls01 with dissolve
    pcthink "[h]?"
    pcthink "Oh... right, today is the date!"
    scene d10hannacalls02 with dissolve
    pc "Hey, Hanna!"
    h "Hey! Good morning, I mean, evening! Err... good day! Haha."
    pc "Haha, what's up Hanna, ready for the date later today?"
    h "Yes!"
    h "I mean, not yet, but I will!"
    pc "Nice, will you tell me where we're going to go now?"
    h "Hm..."
    h "No, not yet, haha."
    scene d10hannacalls03 with dissolve
    pc "Come on, how will I know where to meet you?"
    h "That's why I'm calling, do you know the old Galvin Pier at the Toluca Lake?"
    pc "Yeah, sure, I live on the other side of the lake."
    h "Really?! You live at the lake?"
    pc "Yeah, well, currently at least."
    h "Wow! Isn't that, like, really expensive?"
    pc "I guess, but I don't have to pay anything at the moment."
    h "Oh really? Lucky you! I wish I could afford even the smallest flat."
    pc "You still live with your parents?"
    h "Yes... I want to move out, but I can't afford it..."
    pc "That sucks, I guess the pay at the cafe isn't the best, huh?"
    h "It's okay, but it's only a part time job and I don't have the time for a second job yet."
    pc "Yet?"
    h "Yes, I won't have time until I graduate from university."
    pc "Oh, what are you studying?"
    h "Environmental science."
    pc "Nice, are you going for a Bachelors or a Masters?"
    h "I'm not sure yet..."
    pc "Well, you can always switch anyway, which field are you going for?"
    h "Uhm... Geoscience... I think..."
    pc "First year?"
    h "Yes... I'm... I'm still not really sure what I want to do..."
    pcthink "I get the feeling it wasn't her decision to study..."
    pc "Well, you still have a lot of time and changing the field isn't really uncommon."
    h "You think that'd be okay?"
    pc "Sure, why not?"
    h "..."
    scene d10hannacalls04 with dissolve
    pc "Anyway, back to the date..."
    h "Right! Uhm... the pier, shall we meet there?"
    pc "Sure, do you want me to bring anything?"
    h "No-no, I got everything!"
    pc "Are you sure? I really don't mind."
    h "No it's fine, really, you don't need to worry about anything!"
    pc "Okay, if you're sure."
    h "Sooooo... at six in the afternoon?"
    pc "Let me check my calender... hmm... yeah, six sounds good."
    h "No other girls to date?"
    pc "Not at six, no."
    h "Haha, don't you dare!"
    pc "Haha, just joking."
    h "Oh, ehh..."
    h "I mean... it's not that I... we aren't a couple... right? I mean, I-I'm not demanding anything! So... you could... theoretically... if you wanted to... as long as..."
    h "{size=-15}Oh, damn it, [h]! What are you doing!{/size}"
    pc "Haha, you know I can hear you, right?"
    h "Wha... {size=-15}damn{/size}, I'm sorry! I'm just... it's just... I-I tend to talk too much... sometimes... and sometimes I just say stupid things when I'm nervous..."
    pc "No need to be sorry, I think it's cute, but there's really no reason to be nervous."
    h "Sorry..."
    pc "It's fine, really, we aren't even on a date yet."
    h "I know... it's stupid, isn't it?"
    pc "Haha, kind of, but also not really."
    h "Huh?"
    pc "Everyone does or says something stupid every once in a while, especially when they're nervous. I'm no different."
    h "I guess that's true..."
    pc "..."
    h "..."
    scene d10hannacalls03 with dissolve
    pc "So, what's your plan for the date, does it involve skinny dipping?"
    h "W-What?"
    pc "Haha, joking, just joking."
    h "Haha, you're naughty!"
    pc "Just a little bit."
    h "Haha, well, maybe..."
    pc "Maybe?"
    h "...nothing, haha."
    pc "Maybe nothing?"
    h "Maybe nothing, haha."
    pc "Heh."
    h "Okay, I-I think I should uhh, prepare everything for later now."
    pc "Alright, six in the afternoon then?"
    h "Yes! At the Galvin Pier."
    pc "Looking forward to it."
    h "Thanks, I mean, me too!"
    pc "Heh, okay, later then."
    h "Later... nice talking to ya!"
    pc "Yeah, same, bye, [h]!"
    h "Bye, [pc]!"
    
    jump d10takekathome
    
label d10hdate:
    scene d10beforedate1 with dissolve
    pcthink "Oh, [h] sent a picture."
    show hphoto with dissolve
    pause
    pcthink "Wow, she looks great!"
    scene d10beforedate2 with dissolve
    pause
    pcthink "I should  probably head home and get ready for the date."
    scene d10beforedate3 with dissolve
    pause
    pcthink "Shit, I better hurry."
    scene d10beforedate4 with dissolve
    pause
    stop sound fadeout 2
    scene black with slowdissolve
    n "You rush back home, quickly change into something presentable, then make your way to the pier where [h] is already waiting." with dissolve
    play music mainbgm fadein 1
    scene d10date01 with dissolve
    pc "There she is, I hope I'm not too late."
    scene d10date02 with dissolve
    h "Oh, hey there!"
    scene d10date03 with dissolve
    pc "Hey, sorry for making you wait for so long."
    scene d10date04 with dissolve
    h "Oh, I didn't wait long, barely a few minutes!"
    scene d10date04_2 with dissolve
    if pcgender == "woman":
        pc "Wow, you look beautiful! I love that dress!"
    else:
        pc "Wow, you look great, [h]!"
    scene d10date05 with dissolve
    h "Thanks! You look great as well!"
    pc "What's in the backpack?"
    scene d10date06_ with dissolve
    h "That's..."
    scene d10date07_ with dissolve
    h "Restaurant \"La Hanna\"."
    pc "Oh, you have a whole restaurant in your backpack?"
    h "Well, just the kitchen, haha."
    scene d10date08_ with dissolve
    h "The restaurant is here, at the pier."
    scene d10date09_ with dissolve
    pc "Oh, I see, can you lead me to the tables then, Madam?"
    scene d10date10_ with dissolve
    if pcgender == "woman":
        h "Of course, Madam, please follow me."
    else:
        h "Of course, Monsieur, please follow me."
    pc "With pleasure."
    h "Haha."
    scene black with dissolve
    scene d10date06 with dissolve
    pc "So here's the spot?"
    h "Mh-hmm, you like it?"
    scene d10date07 with dissolve
    pc "Yeah, but why not the pier itself? There's also a bench over there."
    h "The pier is broken and I like it here, it's a little bit more... private."
    scene d10date07_2 with dissolve
    pc "Fair enough, I'll have a seat then."
    if pcgender == "woman":
        h "I'll take your order in a minute, Madam."
    else:
        h "I'll take your order in a minute, Monsieur."
    pc "Heh, take your time, my Lady."
    scene d10date08 with dissolve
    pcthink "She really thought of everything..."
    scene d10date09 with dissolve
    h "Ready to take your order!"
    pc "I take the waitress, please."
    h "Haha, you can't just skip the dinner part."
    pc "Alright, fine, dinner first then."
    h "Haha..."
    scene black with slowdissolve
    
    #achievement
    $achievement.grant("Achievement_hdate")
    init: 
        $achievement.register("Achievement_hdate")
    $achievement.sync()
    ###########
    
    scene d10date10 with dissolve
    pc "You said your parents were quite strict, right?"
    scene d10date11 with dissolve
    h "Yes, sadly..."
    scene d10date10 with dissolve
    pc "Do they know that you..."
    scene d10date11 with dissolve
    if pcgender == "woman":
        h "That I like women?"
    else:
        h "That I'm on a date right now?"
    scene d10date10 with dissolve
    pc "Yeah..."
    scene d10date11 with dissolve
    h "None of their business, I have my own life and they'll have to accept it."
    scene d10date10 with dissolve
    pc "Heh, little rebel, huh?"
    scene d10date11 with dissolve
    h "Haha."
    scene d10date10 with dissolve
    pc "Didn't you say that you still live with your parents?"
    scene d10date11_2 with dissolve
    h "Uh-huh."
    scene d10date10 with dissolve
    pc "Must be difficult, especially with the job and university..."
    scene d10date11 with dissolve
    h "It's not always easy, but they give me my own space..."
    h "The only thing that really sucks is that I have to do the laundry and dinner every time, especially when I had a hard day at work."
    h "...like last time when we were talking about the date."
    scene d10date11_2 with dissolve
    pc "You have to do the laundry and dinner every time?"
    scene d10date11_3 with dissolve
    h "Uh-huh."
    pc "What are your parents doing then?"
    scene d10date11 with dissolve
    h "Dad has a fulltime job and Mom takes care of the boys."
    scene d10date10 with dissolve
    pc "The boys?"
    scene d10date11 with dissolve
    h "My little brothers, I have three of them, one pair of twins and a baby boy."
    scene d10date10 with dissolve
    pc "Wow, okay that's probably not easy for her as well, but still..."
    scene d10date11 with dissolve
    h "Mom keeps saying I have to do it to become a good wife for my future husband."
    scene d10date10 with dissolve
    pc "Sounds like an excuse..."
    scene d10date11 with dissolve
    h "No, she really thinks that way."
    scene d10date11_2 with dissolve
    pc "Really?!"
    scene d10date11 with dissolve
    h "Haha, I told you they're oldschool, didn't I?"
    scene d10date10 with dissolve
    pc "True..."
    scene black with slowdissolve
    n "You keep on chatting for a while until you notice that she started shivering slightly. You also notice goosebumps on her skin."
    scene d10date12 with dissolve
    pc "Are you cold?"
    scene d10date13 with dissolve
    h "N-No, no I'm good, haha, just the wind..."
    scene d10date14 with dissolve
    pc "It's getting a bit chilly."
    scene d10date15 with dissolve
    h "A little bit."
    scene d10date16 with dissolve
    pc "Why don't you come over here."
    scene d10date17 with dissolve
    h "..."
    scene d10date21 with dissolve
    pc "Better?"
    scene d10date22 with dissolve
    h "A lot!"
    scene d10date18 with dissolve
    h "Thank you."
    scene d10date21 with dissolve
    pc "It's totally my pleasure."
    scene d10date18 with dissolve
    h "Haha, pervert!"
    scene d10date21 with dissolve
    pc "Hey, I'm just being nice!"
    scene d10date22 with dissolve
    h "And I like it..."
    scene d10date21 with dissolve
    pc "So you call me a pervert but still like it..."
    scene d10date22 with dissolve
    h "Haha, I guess that makes me a pervert, too."
    scene d10date21 with dissolve
    pc "Yep, absolutely!"
    scene d10date22 with dissolve
    h "Haha."
    scene d10date21 with dissolve
    pc "..."
    scene d10date19 with dissolve
    pause
    scene d10date29 with dissolve
    h "..."
    scene d10date23 with dissolve
    scene d10date24 with dissolve
    pause
    scene black with slowdissolve
    scene d10date25 with dissolve
    h "Oh!"
    pc "Huh?"
    scene d10date26 with dissolve
    h "I think it's starting to rain."
    scene d10date27 with dissolve
    pc "...you're right."
    pc "Shit, I didn't check the weather forecast."
    scene d10date28 with dissolve
    scene d10date28_ with dissolve
    h "Me neither, I didn't even think about it."
    pc "Let's hope it's just a short drizzle."
    scene d10date30 with dissolve
    h "Shall we go have a look if the door to the greenhouse is open?"
    scene d10date31 with dissolve
    pc "Sure we can try."
    scene black with slowdissolve
    n "You get up and try to open the greenhouse door."
    scene d10date32door1 with dissolve
    h "Too bad, looks like it's locked."
    pc "Hmm, it's been abandoned for a while, maybe it's just jammed."
    scene d10date33 with dissolve
    h "Maybe we can push it open."
    scene d10date32door1 with dissolve
    pc "Yeah, let me try."
    scene d10date32door2 with dissolve
    pc "HNNNNGH!"
    scene d10date32door1 with dissolve
    pc "Damn..."
    scene d10date35 with dissolve
    h "Maybe I should've made more sandwiches."
    pc "Ha-Ha... you stay there and hold the lamp."
    if pcgender == "man":
        h "Sure, my gallant hero."
    else:
        h "Sure, my gallant heroine."
    scene d10date32door1 with dissolve
    menu:
        "Push.":
            play sound "audio/drop.ogg"
            pause .2
            play audio "audio/door-break1.ogg"
            scene d10date32door2 with hpunch
            scene d10date32door1 with dissolve
            pause .3
            h "Did it move?"
            pc "No idea..."
    menu:
        "Push again.":
            play sound "audio/drop.ogg"
            pause .2
            play sound "audio/door-break2.ogg"
            scene d10date32door2 with hpunch
            scene d10date32door1 with dissolve
            pause .3
            h "Don't hurt yourself."
            pc "Don't worry."
    menu:
        "Push once more.":
            play sound "audio/drop.ogg"
            pause .2
            play audio "audio/door-break3.ogg"
            pause .2
            play sound "audio/door-break4.ogg"
            scene d10date32door2 with hpunch
            scene d10date32 with dissolve
    pc "Finally!"
    scene d10date34 with dissolve
    h "Yay, you made it!"
    pc "Can't let my lady drown, can I?"
    h "Haha, it's not {b}that{/b} much rain!"
    scene d10date36 with dissolve
    h "But thanks..."
    scene d10date37 with dissolve
    pause
    scene d10date38 with dissolve
    pause
    scene d10date39 with dissolve
    pause
    scene d10date40 with dissolve
    h "Oh, I better get my stuff here before it gets wet."
    scene d10date41 with dissolve
    if pcgender == "man":
        h "Why don't you secure the dungeon for us my hero."
    else:
        h "Why don't you secure the dungeon for us my heroine."
    pc "Haha, I'll make sure the glasshouse, err... \"the dungeon\", is safe for you, my Lady!"
    scene d10date42 with dissolve
    h "Mmmmm..."
    scene d10date43 with dissolve
    h "...wha!{w=1}{nw}"
    scene d10date44 with dissolve
    h "..."
    scene d10date45 with dissolve
    h "Don't get eaten by the monster rats until I'm back!"
    pc "Heh, sure, I'll tell them to wait for you to come back before they eat me."
    h "Haha!"
    scene d10date46 with dissolve
    pcthink "Alright..."
    scene d10date47 with dissolve
    pcthink "Let's see how the dun... greenhouse looks from the inside."
    scene d10date48 with dissolve
    pc "..."
    scene d10date49 with dissolve
    pc "Looks like the rain is getting stronger... maybe I should help [h]."
    scene d10date50 with dissolve
    h "Eeek!"
    scene d10date51 with hpunch
    pc "Whoa! Did you get wet, my Lady?"
    scene d10date52 with dissolve
    h "Haha, just a little bit."
    scene d10date51_2 with dissolve
    h "Too bad, the weather doesn't want to play along."
    pc "Who cares, we have a roof and I'll keep you warm as long as it takes."
    scene d10date51_3 with dissolve
    h "..."
    scene d10date53 with dissolve
    h "I want to show you something."
    pc "What is it?"
    h "Can you hold the blanket for me?"
    scene d10date54 with dissolve
    pc "Sure..."
    scene d10date55 with dissolve
    h "..."
    scene d10date56 with dissolve
    h "Higher!"
    pc "Whoa, okay..."
    scene d10date57 with dissolve
    h "And no peeking!"
    pc "What are you doing?"
    h "You'll see!"
    pc "..."
    pause
    menu:
        "Peek.":
            scene d10date58 with slowdissolve
            h "Ahem!"
            pc "Just curious..."
            h "No! Peeking!"
            pc "Haha, okay... sorry."
            scene d10date57 with dissolve
        "Don't.":
            pass
    pause 1
    play sound "audio/clothing-rustle.ogg"
    pause 8
    scene d10date59_1 with dissolve
    stop sound fadeout .5
    h "Alright, I'm done."
    scene d10date59 with dissolve
    pause
    scene d10date60 with dissolve
    pause
    pc "Wow...!"
    scene d10date61 with dissolve
    h "You like it?"
    pc "I {b}love{/b} it!"
    scene d10date62 with dissolve
    h "You said something about skinny dipping, so I thought..."
    scene d10date63 with dissolve
    h "Well, no skinny dipping, but maybe you really wanted to dip into the water..."
    pc "I'd love to!"
    scene d10date64 with dissolve
    h "I thought so."
    scene d10date65 with dissolve
    h "So, where's your bathing suit?"
    pc "Err... well, as I said, \"skinny dipping\"."
    scene d10date66 with dissolve
    h "Wha... you'd really do that?"
    pc "Of course, especially with you."
    scene d10date67 with dissolve
    h "That's so naughty!"
    pc "Didn't we establish already that we're both naughty?"
    scene d10date68 with dissolve
    h "Haha, yes."
    scene d10date69 with dissolve
    pc "And you're such a beautiful girl..."
    scene d10date70 with dissolve
    pc "I wouldn't mind a second, skinny dipping with you..."
    scene d10date71 with dissolve
    h "..."    
    scene d10date72 with dissolve
    pc "Mind if I take a closer look?"
    h "Just a peek."
    scene d10date73 with dissolve
    pc "Hmmh, so sexy."
    scene d10date74 with dissolve
    h "..."
    scene d10date73 with dissolve
    pc "Mind if I..."
    scene d10date75 with dissolve
    pause .5
    scene d10date76 with hpunch
    h "Wha!"
    scene d10date77 with dissolve
    h "It's... it's just our first date..."
    pc "Right... you're right, sorry I got a little too excited here."
    h "It's okay."
    pc "Why don't we sit down and wait until the rains stops?"
    scene d10date78 with dissolve
    h "Uh-huh."
    scene black with slowdissolve
    scene d10date80 with dissolve
    pc "..."
    scene d10date81 with dissolve
    pause
    pc "Are you sure it's not too cold in that bathing suit?"
    scene d10date82 with dissolve
    h "I'm wearing it for you, and besides that, you keep me warm..."
    scene d10date81 with dissolve
    pc "Says the girl with the stiff nipples."
    scene d10date79 with dissolve
    h "Haha, stop staring at them..."
    pc "I'd stare at your cute face, but it's a little hard at this angle."
    scene d10date83_1 with dissolve
    h "Better?"
    scene d10date83 with dissolve
    pc "Much better!"
    h "..."
    scene d10date84 with dissolve
    pause
    scene d10date85 with dissolve
    pc "...but seriously, I don't want you to catch a cold because of me."
    h "..."
    scene d10date86 with dissolve
    h "I'm sorry..."
    pc "Huh? For what?"
    scene d10date87 with dissolve
    h "I-I didn't think about the weather and now it totally destroyed the date..."
    pc "You think it's destroyed?"
    scene d10date88 with dissolve
    h "I... don't know... it's not as I imagined..."
    scene d10date89 with dissolve
    h "I wanted to sit at the lake... watch the sunset... lying in your arms..."
    scene d10date90 with dissolve
    h "Gosh, saying it out loud is embarrassing! Haha."
    scene d10date90_2 with dissolve
    pc "Haha, you're a romantic."
    if pcgender == "man":
        h "You probably think that's boring."
        pc "No, I would've liked that."
    scene d10date91 with dissolve
    pc "But really, I wouldn't say the date is destroyed unless you don't like being with me."
    scene d10date92 with dissolve
    h "I-I like being with you of course!"
    pc "So it's not too bad, right? ...and we conquered a dungeon full of monster rats, who else can say that from their first date?"
    scene d10date93 with dissolve
    if pcgender == "woman":
        h "Haha, very true, my heroine."
    else:
        h "Haha, very true, my hero."
    scene d10date94 with dissolve
    h "But maybe we should meet somewhere inside next time..."
    pc "So you want to go on another date?"
    scene d10date95 with dissolve
    h "Eh... yes, of course... if you want to..."
    pc "Of course!"
    scene d10date96 with dissolve
    pause
    scene d10date97 with dissolve
    pause
    scene d10date98 with dissolve
    pc "So... I guess we call it a day for today?"
    scene d10date99 with dissolve
    h "If you don't mind..."
    scene d10date100 with dissolve
    pc "Oh, I {b}do{/b} mind, but I'm not going to let you freeze."
    scene d10date97 with dissolve
    pause
    scene black with fade
    n "A little while later..."
    scene d10datehhome01 with dissolve
    h "Here we go, this is where I live."
    scene d10datehhome02 with dissolve
    pc "Glad it's not too far from the lake."
    scene d10datehhome03 with dissolve
    h "Thanks for the jacket."
    pc "Anytime, my Lady."
    h "Haha..."
    scene d10datehhome04 with dissolve
    if pcgender == "woman":
        h "...my heroine..."
    else:
        h "...my hero..."
    scene d10datehhome05 with dissolve
    pause
    scene d10datehhome06 with dissolve
    pc "Alright, I need to go to the city tomorrow to hand over some papers..."
    scene d10datehhome07 with dissolve
    h "Oh, I won't keep you!"
    pc "Haha, no, I wanted to ask when your shift starts, so I can get a cup of coffee from my favorite waitress."
    scene d10datehhome08 with dissolve
    h "Oh... haha, it's in the morning... until midday."
    pc "Alright, I'll come over in the morning then."
    scene d10datehhome09 with dissolve
    h "Okay, then... see you tomorrow?"
    pc "In the morning."
    h "In the morning!"
    scene d10datehhome10 with dissolve
    pause
    scene d10datehhome05 with dissolve
    pause
    scene d10datehhome10 with dissolve
    pc "Okay, see you tomorrow, my Lady."
    scene d10datehhome09 with dissolve
    if pcgender == "woman":
        h "See you tomorrow, my Heroine."
    else:
        h "See you tomorrow, my Hero."
    scene black with dissolve
    n "You go on your way and..."
    menu:
        "Look back.":
            scene d10datehhome11 with dissolve
            pcthink "Cute..."
        "Leave.":
            pass
    scene black with fade
    n "You head back home."
    scene black with dissolve
    jump d10johnson
    
        
label d11visitcafe:
    scene d11cafe01 with slowdissolve
    pcthink "Time for some coffee!"
    if hlo >= 3:
        scene d11cafe02 with dissolve
        pcthink "Looks like [h] is busy..."
        scene d11cafe03 with dissolve
        h "..."
        scene d11cafe04 with dissolve
        pcthink "...guess I'll just sit down somewhere and wait until she's done."
        scene d11cafe05 with dissolve
        pcthink "I guess I'll have to think about how this relationship will go on from now on..."
        scene d11cafe06 with dissolve
        if pcgender == "woman":
            h "Good morning my heroine."
        else:
            h "Good morning my hero."
        scene d11cafe07 with dissolve
        pc "Good morning my Lady, did you miss me?"
        scene d11cafe08 with dissolve
        h "*smooch*"
        scene d11cafe09 with dissolve
        h "I did!"
        scene d11cafe10 with dissolve
        h "I wanted to text you, but the twins started acting up, so my mom made me take care of the baby and when I was finally free, I fell asleep."
        scene d11cafe11 with dissolve
        pc "Damn, what a shame, but I'm glad you didn't catch a cold."
        scene d11cafe12 with dissolve
        h "Haha, yes, at least that's something."
        scene d11cafe13 with hpunch
        h "*Achoo*"
        pc "Uh-Oh..."
        scene d11cafe14 with dissolve
        h "Oh no, I'm sorry."
        pc "It's okay, just a sneezer doesn't mean anything."
        scene d11cafe15 with dissolve
        h "I hope so... I can't afford getting sick now."
        scene d11cafe16 with dissolve
        pc "Do you have tea? Maybe make one for yourself."
        scene d11cafe17 with dissolve
        h "Yes, that's a good idea..."
        scene d11cafe18 with dissolve
        h "I'll be right back."
    elif hlo >= 1:
        scene d11cafe04 with dissolve
        pcthink "Guess I'll take a seat for a few minutes."
        scene d11cafe07_1 with dissolve
        h "Hey."
        pc "Hey, [h]."
        scene d11cafe08_1 with dissolve
        h "..."
        pc "What's up, [h]?"
        scene d11cafe09_1 with dissolve
        h "Err... what can I get you today?"
        pc "Just a coffee."
        scene d11cafe18_1 with dissolve
        h "Okay, will be there in a minute."
        scene d11cafe19 with dissolve
        pcthink "Hmm... she seems to be down a bit..."
        pcthink "Oh, damn I didn't call her, I totally forgot about that!"
    else:
        scene d11cafe04 with dissolve
        pcthink "Guess I'll take a seat for a few minutes."
        scene d11cafe05 with dissolve
        pcthink "Damn, I hope [boss] likes the project..."
        h "Hey."
        scene d11cafe07 with dissolve
        pc "Oh, hi."
        h "What can I get you?"
        pc "Just a coffee, please."
        scene d11cafe18_2 with dissolve
        h "On the way!"
    scene black with slowdissolve
    play sound "audio/shop-chime.ogg"
    pause .5
    scene d11cafe20 with dissolve
    pause
    scene d11cafe21 with dissolve
    if pgirls:  
        pcthink "Huh? Aren't they the girls from the other day?"
    else:
        pause
    scene d11cafe05 with dissolve
    pcthink "Hmm..."
        
    if hlo >= 3:
        pcthink "I hope there won't be an inrush like last time..."
        scene d11cafe22 with dissolve
        h "Here you go, [h] special on the house."
        pc "Don't you get in trouble when you always give me coffee for free?"
        scene d11cafe23 with dissolve
        h "It's fine, I can have as much coffee as I want."
        scene d11cafe24 with dissolve
        h "I'll be right back, need to take care of the other customers..."
        pc "Sure."
        scene d11cafe25 with dissolve
        pc "..."
        scene d11cafe26 with dissolve
        pcthink "That reminds me, wasn't there some talk about a lockdown? Shouldn't the cafe be closed?"
        
    elif hlo >= 1:
        pcthink "I hope [h] isn't mad that I didn't call her..."
        scene d11cafe22_1 with dissolve
        h "Here you go."
        scene d11cafe23_1 with dissolve
        pc "Thanks... and sorry for not calling, I've been very busy lately."
        scene d11cafe24_1 with dissolve
        h "It's okay, I can understand that."
        scene d11cafe25_1 with dissolve
        h "I need to take care of the customers."
        pc "Okay, sure..."
        scene d11cafe25 with dissolve
        pcthink "Damn, I think she's mad at me..."
        scene d11cafe26_1 with dissolve
        pcthink "Oh well, nothing I can do about it right now."
    else:
        pcthink "I wonder where I've seen them before..."
        scene d11cafe22_2 with dissolve
        h "Here you go."
        pc "Thanks."
        h "Anything else?"
        pc "Thanks, I'm good."
        scene d11cafe25_1 with dissolve
        h "Okay, I'll be taking care of the other customers, but let me know if you need anything."
        pc "Sure, thanks."
        scene d11cafe25 with dissolve
        pcthink "She seems overly friendly towards me..."
        scene d11cafe26_1 with dissolve
        pcthink "Or maybe I'm just seeing things..."
    jess "FUCK YOU!" with hpunch
    scene d11cafe27 with dissolve
    pc "What the..."
    em "[jess]!"
    scene d11cafe28 with dissolve
    jess "{b}Such an asshole!{/b}"
    scene d11cafe29 with dissolve
    em "[jess], don't yell like that!"
    scene d11cafe30 with dissolve
    h "Could you please be a bit quieter, you might annoy the other guests..."
    jess "Other..."
    scene d11cafe31 with dissolve
    jess "Oh..."
    if pgirls:
        scene d11cafe32 with dissolve
        pc "..."
        scene d11cafe33 with dissolve
        jess "[em]!"
        em "What?!"
    scene d11cafe34 with dissolve
    pcthink "I wonder what happened..."
    if hlo >= 3:
        scene d11cafe26 with dissolve
        pc "..."
        scene d11cafe35 with dissolve
        pc "*Slurp*"
        scene d11cafe36 with dissolve
        h "I'm back!"
        pc "All done?"
        h "Yes!"
        scene d11cafe37 with dissolve
        h "I'm sorry, you probably don't have much time..."
        scene d11cafe38 with dissolve
        pc "Enough to spend a few minutes with my favorite waitress. *smirks*"
        scene d11cafe39 with dissolve
        h "Won't you be late for work?"
        scene d11cafe40 with dissolve
        pc "I don't have a specific time to be there."
        pc "It's just that I don't know how long it'll take, so if I don't want to spend the night there, it's probably better to get going soon."
        scene d11cafe39 with dissolve
        h "Maybe it would've been better if you went to work first?"
        scene d11cafe38 with dissolve
        pc "But then I might've missed your shift."
        scene d11cafe39 with dissolve
        h "You really don't need to take extra time for me."
        scene d11cafe40 with dissolve
        pc "Oh, don't get me wrong, I just had to make sure my Lady is healthy, after our little adventure yesterday."
        scene d11cafe40_2 with dissolve
        h "Haha, my heroic companion took good care of me."
        scene d11cafe41
        h "*Achoo*" with hpunch
        pc "Oh dear, not good enough it seems."
        scene d11cafe42 with dissolve
        h "Damn it... it's not your fault."
        scene d11cafe43 with dissolve
        h "I'll be right back!"
        scene d11cafe44 with dissolve
        pcthink "Looks like she really caught a cold..."
    else:
        scene d11cafe26_1 with dissolve
        pc "..."
        scene d11cafe35_1 with dissolve
        pc "*Slurp*"

    scene d11cafe45 with dissolve
    if pgirls:
        jess "Forget it!"
        em "God, [jess], seriously! It's not like we have any choice."
        scene d11cafe46 with dissolve
        jess "You don't even know [himher], [em]!"
        scene d11cafe47 with dissolve
        em "As if that even matters to you."
        scene d11cafe48 with dissolve
        jess "[em], no!"
        scene d11cafe49 with dissolve
        em "Do you really want to blow it, just because of a mistake?"
        scene d11cafe48 with dissolve
        jess "What?! It's not my fault that asshole cancelled last minute!"
        scene d11cafe50 with dissolve
        em "Maybe, but we can still do it, we have our own equipment."
        scene d11cafe51 with dissolve
        jess "Uch..."
        scene d11cafe52 with dissolve
        em "I'll ask [himher]..."
        scene d11cafe53 with dissolve
        jess "[em]!"
        scene d11cafe54 with dissolve
        em "Hey, uhh... sorry for all the yelling, we had a rough day."
        pc "No problem."
        em "And sorry for last time as well."
        pc "It's okay."
        scene d11cafe55 with dissolve
        em "Jeez, I just realized, you must have a really bad impression of us."
        menu:
            "Not really.":
                pc "Everyone has a bad day once in a while."
                scene d11cafe56 with dissolve
                em "I guess that's true."
            "Only of [jess].":
                scene d11cafe56 with dissolve
                em "Oh, well, she's a little... hot-blooded, but believe me, she's really nice when you know her."
        scene d11cafe57 with dissolve
        em "Anyway, we have a little problem as you might've noticed. One of our... co-workers dropped out last minute, and we don't have a replacement for the shoot, so I thought you might be interested?"
        pc "Me? A shoot?"
        scene d11cafe58 with dissolve
        em "Mh-hm, you look good, I think you'd fit quite well, and it's a one time thing, quick money, and..."
        pc "And?"
        scene d11cafe59 with dissolve
        em "Well, we get to know each other."
        pc "Oh, of course."
        scene d11cafe60 with dissolve
        em "So? Interested?"
        pc "Well... it's not that I need money."
        scene d11cafe59 with dissolve
        em "You'd really help us out, and it's an easy and fun job, promise."
        pc "Hmm... what kind of..."
        scene d11cafe61 with dissolve
        em "You know what?"
        scene d11cafe62 with dissolve
        em "Just think about it and call me if you're interested. We have the whole week, so take your time."
        pc "Okay, sure..."
        scene black with dissolve
        n "You take your phone out and save the number she gives you."
        scene d11cafe62 with dissolve
        em "What's your name by the way?"
        pc "[pc]."
        em "Nice to meet you, [pc]. I'm Emma, but you can call me [em]."
        pc "Nice to meet you, too, [em]."
        em "And, erm..."
        scene d11cafe63 with dissolve
        em "...just call me, even if you're not interested."
        scene d11cafe64 with dissolve
        em "Alright, I better get back to [jess], she needs some special attention today."
        scene d11cafe65 with dissolve
        pc "Haha, sure."
        scene d11cafe66 with dissolve
        em "I hope to hear from you."
        if hlo >= 3:
            scene d11cafe67 with dissolve
        else:
            scene d11cafe67_1 with dissolve
        pcthink "A shoot, huh..."
        pcthink "I wonder what they're shooting for... I'm sure I've seen them somewhere before..."
    if hlo >= 3:
        if pgirls:
            scene d11cafe68 with dissolve
            h "Any trouble?"
            pc "No, she was just apologizing."
            scene d11cafe36 with dissolve
            h "Oh, that's nice of her."
            pc "Yeah."
        else:
            scene d11cafe45 with dissolve
            n "You try to listen to the girls for a while, but can't really understand much..."
            scene black with slowdissolve
        scene d11cafe39 with dissolve
        h "So, uhh... where were we?"
        scene d11cafe38 with dissolve
        pc "Hmm... good question..."
        scene d11cafe69 with dissolve
        h "..."
        pc "..."
        pc "Oh that reminds me, the house where you and your parent live, do you know what was in there when I was still a kid?"
        scene d11cafe70 with dissolve
        h "Hm? No idea, what was it?"
        scene d11cafe69 with dissolve
        pc "A store for video games."
        scene d11cafe71 with dissolve
        h "Really? I didn't know."
        scene d11cafe69 with dissolve
        pc "Yeah, I used to buy some imported games there, they had some really rare stuff you couldn't get anywhere else at the time."
        scene d11cafe71 with dissolve
        h "Wow, the twins will probably freak out when they hear that."
        scene d11cafe69 with dissolve
        pc "I guess they like video games?"
        scene d11cafe71 with dissolve
        h "Oh yes, they'll probably go on a hunt, looking for games the owner might've forgotten."
        scene d11cafe69 with dissolve
        pc "Maybe they'll be lucky, I've heard the owner stored lots of the wares in the attic."
        scene d11cafe70 with dissolve
        h "Hm, I've never been up there..."
        pc "Really? You've never been curious?"
        scene d11cafe39 with dissolve
        h "No... mostly too scared..."
        em "Bye!"
        scene d11cafe72 with dissolve
        h "Oh, good bye, have a nice day."
        scene d11cafe73 with dissolve
        em "Thanks, you too."
        jess "Bye."
        scene d11cafe74 with dissolve
        play sound "audio/shop-chime.ogg"
        pc "Hmm... I guess I better leave too."
        scene d11cafe75 with dissolve
        h "Aww... alright..."
        scene d11cafe76 with dissolve
        pc "Sorry, maybe we can talk later?"
        scene d11cafe77 with dissolve
        h "Mh-hm, yeah, can I call you?"
        scene d11cafe78 with dissolve
        pc "Sure, best in the evening."
        scene d11cafe79 with dissolve
        h "Okay..."
        scene d11cafe80 with dissolve
        pause 1
        scene d11cafe81 with dissolve
        h "O-oh... I better keep my distance."
        pc "I've kissed you before, so it would be too late now anyway."
        scene d11cafe82 with dissolve
        h "..."
        scene d11cafe83 with dissolve
        pause 2
        scene d11cafe82 with dissolve
        pc "Hear you later, my Lady."
        if pcgender == "woman":
            h "Later my heroine!"
        else:
            h "Later my hero!"
        scene black with slowdissolve
    if not pgirls and hlo < 3:
        pc "..."
        scene black with slowdissolve
        n "You try to listen to the girls, but can't understand much, so you drink your coffee at a relaxed pace, and once it's empty you pay the bill and leave."
    $ gotocafe = False
    scene bm-map with dissolve
    call screen wmap with dissolve
        
label d11work:
    if gotocafe and hlo >= 3:
        pc "Hmm, maybe I should go see [h] first, who knows how long it'll take at work."
        menu:
            "Yeah, let's go see [h].":
                scene bm-map with dissolve
                call screen wmap with dissolve
            "Nah, I'm good.":
                $ vhd11 = False
    scene d11work01 with dissolve
    pcthink "Hmm, I wonder if [st] is still busy in the library..."
    scene d11work02 with dissolve
    pcthink "Anyway, I better go straight to the boss."
    scene black with dissolve
    scene d11work03 with dissolve
    pcthink "Hm?"
    scene d11work04 with dissolve
    pcthink "Where is he?"
    play sound "audio/door-opening.ogg"
    pause 1
    play sound "audio/drop.ogg"
    scene d11work05 with hpunch
    pc "Ouch!"
    scene d11work06 with dissolve
    st "Oh my god, are you okay?"
    pc "I'm fine... I think."
    scene d11work07 with dissolve
    play sound "audio/door_close.ogg"
    st "I'm sorry, I thought there's no one in the room."
    pc "It's okay, just a flesh wound."
    scene d11work08 with dissolve
    st "Do you need an ambulance?"
    pc "That was a joke, I'm fine."
    scene d11work09 with dissolve
    st "Oh, okay... "
    pc "Err..."
    scene d11work10 with dissolve
    pc "So... where's the boss?"
    scene d11work11 with dissolve
    st "He's out of town for a meeting."
    pc "Again? But what about the project?"
    scene d11work12 with dissolve
    st "That's my responsibility."
    pc "Your responsibility? Did he just leave it to you?"
    scene d11work13 with dissolve
    st "Yes and no."
    scene d11work14 with dissolve
    st "I am the one who initiated the project."
    scene d11work15 with dissolve
    st "[boss] didn't even know it was necessary at the time, but when I told him, he agreed and told me to take care of it."
    scene d11work16 with dissolve
    pc "I see, I thought it was his project."
    scene d11work17 with dissolve
    st "He's still the boss and it's his company."
    pc "Of course..."
    scene d11work18 with dissolve
    pc "Wait, does that mean you're the one I have to thank for the job?"
    st "..."
    scene d11work19 with dissolve
    st "Can you show me the files?"
    scene d11work20 with dissolve
    pc "Sure, I actually brought my laptop in case anything needs to be changed."
    scene d11work19 with dissolve
    st "Good, show me."
    scene black with slowdissolve
    n "You upload the project onto the company's server and then show her the results of your work. She seems a little bit distracted at first, when you come closer to her to show your work, but you go on nonetheless."
    pc "...and then it goes back to the full frame logo." with dissolve
    scene d11work21 with dissolve
    st "This is a nice effect, I wouldn't have thought of that."
    pc "Well, it's my job to think of stuff like that, that's why you hired me, right?"
    st "..."
    pc "{cps=2}...{/cps}"
    scene d11work22 with dissolve
    st "There are a few things that need to be changed."
    scene d11work24 with dissolve
    pc "Okay... sure."
    pc "Let me ask you one question though."
    pc "Why did you hire me?"
    scene d11work25 with dissolve
    st "W-What do you mean? We had a vacancy..."
    pc "Sure, but why did you hire me?"
    pc "I'm sure I wasn't the only one applying and it's not that my resume looks that impressive, especially for a company like yours."
    scene d11work26 with dissolve
    st "It's... we were looking for someone not that well known."
    pc "Why?"
    st "To... save costs."
    pc "And yet, my salary is almost twice as much as is standard."
    st "..."
    if stl > 1:
        pcthink "Hm... thinking about the whole situation, it really doesn't make much sense."
        scene d11work27 with dissolve
        pcthink "...and why is she dressed like that, I thought she's shy... it doesn't fit her personality to show so much skin."
        pcthink "..."
        pcthink "Wait a minute..."
        scene black with slowdissolve
        scene boss_buro8_mem with dissolve
        n "There is nothing going on between us, so if you're interested in her, just go for it." with dissolve
        pcthink "That was the first time meeting them... I didn't think much of it, just a misunderstanding, but..."
        scene black with slowdissolve
        scene d9_job06_mem with dissolve
        n "...I called [st] and she seems to have some ideas." with dissolve
        n "Oh? So that's why..." 
        pcthink "\"So that's why...\" At the time I didn't understand what he meant, but..."
        scene black with dissolve
        scene d9_job17_mem with dissolve
        pause .5
        n "Hmm? You look kinda different today..."
        scene d9_job18_mem with dissolve
        pause .5
        n "I-I don't know what you mean."
        pause .5
        pcthink "That was the first time she was wearing makeup and no glasses, and she knew I was coming by..."
        scene black with slowdissolve
        scene d11work27 with dissolve
        pcthink "...and she knew I'd come by today..."
        scene d11work28 with dissolve
        pcthink "Could it really be that they hired me because [st] is interested in me?"
        pcthink "Would [boss] do that?"
        pcthink "Oh well, he probably didn't even know... or did he?"
        pcthink "But even if... she's his best employee who basically takes care of the whole company for him..."
        pcthink "Of course he would play along, he's the kind of easygoing person anyway..."
        pcthink "Maybe it was actually him who set the whole thing up..."
        pcthink "...maybe they were browsing through all the candidates and he noticed she had an unusual reaction when they saw my profile..."
        pcthink "And it's not that I'm bad at my job, I doubt that [st] would've accepted me if I wasn't good enough for the job, even if she likes me personally... or rather my looks."
        pc "..."
        pc "Say [st], do you plan to go on a date?"
        scene d11work29 with dissolve
        st "Hm?"
        scene d11work30 with dissolve
        st "N-No, why?"
        pc "The dress and makeup, you look stunning today."
        scene d11work31 with dissolve
        st "O-Oh... err..."
        scene d11work32 with dissolve
        st "T-Thank you..."
        pc "Do you {b}want{/b} to go on a date?"
        scene d11work33 with dissolve
        st "I-I just said that I don't plan to..."
        scene d11work34 with dissolve
        st "Wait... did you... did you just ask me to..."
        pc "Yes, I did."
        st "I-I..."
        scene d11work35 with dissolve
        st "I don't have time for such things..."
        pcthink "Of course..."
        pcthink "I guess it was probably [boss] who set the whole thing up..."
        pcthink "I mean, it's obvious that she likes me, but she's so damn shy and always focused on her work..."
        pc "Hmm, how about a business meeting then?"
        scene d11work36 with dissolve
        st "A business meeting?"
        pc "Yeah, after work."
        scene d11work37 with dissolve
        st "..."
        scene d11work38 with dissolve
        st "You mean... like we could talk about the changes necessary for the project?"
        scene d11work39 with dissolve
        pc "Exactly, just without the stress and interferences at work."
        pcthink "Damn, her eyes are stunning!"
        scene d11work40 with dissolve
        st "I... I see..."
        pc "So?"
        scene d11work41 with dissolve
        st "I guess... that's fine..."
        pc "Good, today after work?"
        scene d11work42 with dissolve
        st "I don't have time today."
        scene d11work43 with dissolve
        pc "Alright, tomorrow then."
        scene d11work44 with dissolve
        st "Uhm... yes... I think..."
    n "*Rrrrrring*"
    scene d11work45 with dissolve
    st "Oh..."
    scene d11work46 with dissolve
    st "I... I'll send you a message, you can clock out."
    pc "Already?"
    scene d11work47 with dissolve
    st "Yes, I... you're distracting me!"
    scene d11work48 with dissolve
    st "Atomic Aeronautics, hello."
    pcthink "Wow, that was quick... I'm distracting her, huh?"
    scene black with slowdissolve
    $ gotowork = False
    scene bm-map with dissolve
    call screen wmap with dissolve

label d11maggy:
    scene black with slowdissolve
    play sound "audio/knock-door1.ogg"
    pause 1
    play sound "audio/door-opening.ogg"
    scene d11maggy01 with dissolve
    pc "Morning, [ma]."
    scene d11maggy02 with dissolve
    ma "Oh, [pc], nice to see you again. Did you forget anything?"
    scene d11maggy03 with dissolve
    pc "No, but it looks like you gave me the wrong papers yesterday."
    ma "The wrong papers?"
    scene d11maggy04 with dissolve
    ma "Let's see..."
    ma "Oh damn it!"
    scene d11maggy05 with dissolve
    ma "I'm sorry, you're right, they're not yours. Please, have a seat, I'll find the right papers for you."
    scene d11maggy06 with dissolve
    ma "I'm really sorry, I have no idea how that happened."
    pc "Well there was a lot of chaos yesterday with the computer crash."
    ma "True, I must've mixed the papers at some point."
    if datemaggy:
        scene d11maggy07 with dissolve
        pcthink "Damn, what a body..."
        scene d11maggy08 with dissolve
    ma "I swear, such a mistake never happened before, we're very sensible with our clients data."
    pc "I bet."
    if datemaggy:
        jump d11maggylewd
    else:
        scene d11maggy17 with dissolve
        ma "Ah, there."
        scene d11maggy18 with dissolve
        ma "I guess I'll need to go through all the papers again..."
        scene d11maggy19 with dissolve
        ma "Here, that's the correct one, please have a look for yourself."
        scene d11maggy20 with dissolve
        pc "Sure, thanks."
        n "*Rrrrring*"
        scene d11maggy21 with dissolve
        ma "Ugh, not again..."
        n "*Rrrrring*"
        scene d11maggy21_end with dissolve
        pc "It's okay, I won't keep you any longer."
        ma "Okay, sorry again for all the trouble."
        pc "No problem, and thanks."
    scene black with fade
    $ gotomaggy = False
    scene bm-map with dissolve
    call screen wmap with dissolve
label d11maggylewd:
    if _in_replay:
        show screen endRep
    pcthink "And I bet she's stretching her ass at me on purpose."
    scene d11maggy09 with dissolve
    ma "Oh how rude of me, do you want a coffee, or something else to drink?"
    scene d11maggy10 with dissolve
    pc "I'm good, thanks... and I guess, it's a little too early for wine."
    scene d11maggy11 with dissolve
    ma "Oh, I see, you want to go on where we left last time, hmm? Sadly I don't have the time today."
    pc "Too bad..."
    ma "Are you sure you don't want anything else?"
    pc "Yeah, thanks."
    scene d11maggy12 with dissolve
    ma "Well, how about a little appetizer instead?"
    scene d11maggy13 with dissolve
    pc "Oof... now that's what I call an appetizer!"
    ma "Like what you see?"
    scene d11maggy14 with dissolve
    pc "Certainly!"
    scene d11maggy15 with dissolve
    ma "I'm glad to hear that."
    scene d11maggy16 with dissolve
    pc "Is that your regular customer service?"
    scene d11maggy17 with dissolve
    ma "Only for special customers."
    pc "I see... I guess they must be {b}very{/b} special then..."
    scene d11maggy18 with dissolve
    ma "{b}[heshe!u]{/b} is."
    scene d11maggy19 with dissolve
    ma "That's the correct one, please have a look for yourself before you sign it."
    scene d11maggy20 with dissolve
    pc "Sure, thanks."
    n "*Rrrrring*"
    scene d11maggy21 with dissolve
    ma "Ugh, not again..."
    n "*Rrrrring*"
    scene d11maggy22 with dissolve
    ma "Sorry, I'll be right back with you."
    pc "No problem."
    scene d11maggy23 with dissolve
    ma "Yes?"
    pcthink "Damn, these curves!"
    scene d11maggy24 with dissolve
    ma "Oh, is that so?"
    pcthink "Huh?"
    scene d11maggy25 with dissolve
    ma "No, no problem, I'll take care of that."
    scene d11maggy26 with dissolve
    pcthink "The fuck?"
    scene d11maggy27 with dissolve
    ma "Yes, Sir, don't worry about it."
    pcthink "Must be her boss or something..."
    ma "Bye."
    scene d11maggy28 with dissolve
    play sound "audio/hangup.ogg"
    pcthink "What's going on?"
    scene d11maggy29 with dissolve
    ma "So, it looks like my boss will leave the office for a while..."
    scene d11maggy30 with dissolve
    ma "...and he also advised me to find some documents in the meantime..."
    scene d11maggy31 with dissolve
    ma "Being the good employee I am, I know of course where they are..."
    scene d11maggy32 with dissolve
    ma "Which means I don't have to search for them."
    scene d11maggy33 with dissolve
    ma "But since he doesn't know and it has high priority, he told me to turn off the phone and ignore any emails until I found them or he comes back."
    pc "I see, how inconvenient."
    scene d11maggy34 with dissolve
    ma "Isn't it?"
    pc "I guess my paperwork has to wait then."
    scene d11maggy35 with dissolve
    ma "I hope you don't mind."
    scene d11maggy36 with dissolve
    ma "I'll make sure to make it up to you."
    scene d11maggy37 with dissolve
    ma "In the best way possible..."
    pc "Now I'm curious."
    scene d11maggy38 with dissolve
    ma "We value customer intimacy very highly." 
    scene d11maggy39 with dissolve
    pc "Customer intimacy, huh? I don't think that's what it really means, but I won't complain about a little intimacy."
    scene d11maggy40 with dissolve
    ma "Oh, it's going to get really intimate soon."
    scene d11maggy41 with dissolve
    ma "{b}Really{/b}... intimate."
    scene d11maggy42 with dissolve
    pause
    scene d11maggy41 with dissolve
    ma "Mmh..."
    scene d11maggy43 with dissolve
    ma "Let's start with these, shall we?"
    scene d11maggy44 with dissolve
    play sound "audio/clothing-rustle-c1.ogg"
    pause
    scene d11maggy45 with dissolve
    play sound "audio/clothing-rustle-c3.ogg"
    pause
    scene d11maggy46 with dissolve
    ma "So, what do you think?"
    scene d11maggy47 with dissolve
    pc "Damn, I think I'm in heaven."
    scene d11maggybt with dissolve
    ma "Haha, you're not, but maybe that's where I come from."
    pc "Oh I bet!"
    scene d11maggybt2 with dissolve
    ma "Mhh, yes."
    scene d11maggy50 with dissolve
    ma "Let me see what's under there..."
    scene black with dissolve
    play sound "audio/clothing-rustle-c2.ogg"
    pause .5
    ma "Such a nice, young body."
    scene d11maggy51 with dissolve
    if pcgender == "woman":
        ma "...and such nice and firm tits, you're such a beauty!"
    ma "Mhh... such a lucky woman..."
    pc "I think I'm the lucky one here."
    ma "Charmer..."
    scene d11maggy52 with dissolve
    ma "Let's get rid of this uncomfortable skirt..."
    scene black with dissolve
    play sound "audio/clothing-rustle-c1.ogg"
    scene d11maggy53 with dissolve
    ma "Mhh, maybe I should stay right down here."
    scene d11maggy54 with dissolve
    pc "Go ahead, I definitely wouldn't mind."
    scene d11maggy55 with dissolve
    ma "Oh, I'm sure of that..."
    scene d11maggy56 with dissolve
    ma "...but I think I'll let you have the first taste if you don't mind."
    scene d11maggy57 with dissolve
    pc "Not at all!"
    scene d11maggy58 with dissolve
    ma "Let me just... climb on the chair..."
    pc "Don't fall!"
    scene d11maggy59 with dissolve
    ma "Now that would've been awkward, wouldn't it?"
    pcthink "Damn, what a view."
    ma "Like the view?"
    pc "Let's say I wouldn't mind seeing that more often."
    scene d11maggy60 with dissolve
    ma "Mhh... convince me."
    pc "With pleasure!"
    scene d11maggylick with dissolve
    pause
    ma "What a good [boygirl]..."
    pc "..."
    menu:
        "Gently bite her clit.":
            scene d11maggy62 with hpunch
            ma "HAA!"
            ma "You little..."
            scene d11maggy65 with dissolve
            ma "Oh I see, I guess I was wrong."
            ma "Fine..."
            scene d11maggy59 with dissolve
        "Just go on.":
            ma "Mhhh... oh yes!"
            ma "You have quite a bit experience, I can tell..."
            scene d11maggylick2 with dissolve
            ma "Haa... mhh... that's the spot!"
            ma "Oh god..."
            ma "Haa..." with hpunch
            ma "Haaaa... yes!" with hpunch
            scene d11maggy64 with hpunch
            ma "HAA!"
            scene d11maggy65 with dissolve
            ma "That was better than I expected for somebody your age."
            pc "It's not like it's my first time..."
    ma "I guess it's time for me to take over..."
    scene d11maggy66 with dissolve
    ma "Let's see what's under here..."
    scene black with dissolve
    play sound "audio/clothing-rustle-c3.ogg"
    scene d11maggy67 with dissolve
    if pcgender == "man":
        ma "Mhh... looks like someone is waiting already."
    else:
        ma "Mhh... nice and wet..."
    scene d11maggy68 with dissolve
    pause 1
    scene d11maggy69 with dissolve
    ma "Hmm, come over here."
    if pcgender == "woman":
        scene d11maggy70 with hpunch
        pc "Whoa!"
    else:
        scene d11maggy70 with dissolve
    pc "I get the feeling you've been waiting for this to happen."
    scene d11maggy71 with dissolve
    ma "Maybe."
    scene d11maggy72 with dissolve
    ma "But let's not waste time talking."
    if pcgender == "man":
        scene d11maggy72_2m with dissolve
        ma "Somebody is waiting."
        scene d11maggy73_m with dissolve
        pause .5
        scene d11maggy73_2m with dissolve
        pause .3
        scene d11maggy73_m with dissolve
        pause .5
        scene d11maggy73_2m with dissolve
        pause .3
        scene d11maggy73_m with dissolve
        pause .5
        scene d11maggy74_m with dissolve
        ma "Mhh..."
        scene d11maggy75_m with dissolve
        pcthink "Damn, she looks hot down there..."
        scene mabj1_00 with dissolve
        scene d11maggym1 with dissolve
        pcthink "Oof, right down her throat!"
        pause
        ma "Mph...mhhh..."
        pc "Damn, [ma], that's incredible!"
        ma "Mwhaa... you haven't seen anything yet, honey."
        scene d11maggym2 with dissolve
        pc "Holy..."
        $ mabjdeep = True
        pause
        menu d11mabjm:
            "Not so deep." if mabjdeep:
                $ mabjdeep = False
                pc "Not so deep, [ma], I want to enjoy it a little bit longer."
                scene d11maggym1 with dissolve
                ma "Mh-hmm."
                pause
                jump d11mabjm
            "Deeper." if not mabjdeep:
                $ mabjdeep = True
                pc "Can you go deeper again?"
                scene d11maggym2 with dissolve
                pause
                jump d11mabjm
            "Go on.":
                pause
                jump d11mabjm
            "Cum.":
                pass
    else:
        scene d11maggy73f2_00 with dissolve
        $ pov1 = "d11maggyf2"
        $ pov2 = "d11maggyf1"
        $ campov = False
        show screen povscreen(pov1) with dissolve
        pause
        pc "Oh god, [ma] this feels incredible!"
            
        hide screen povscreen with dissolve
        hide screen povbutton
        scene d11maggy76 with dissolve
        ma "You could say I have some experience."
        scene d11maggyf2 with dissolve
        pc "No doubt!"
        scene d11maggyf2-3
        pause 1.9
        scene d11maggyf3
        $ malickclit = True
        pause
        pc "Damn..."
        menu d11malfm:
            "Suck it." if malickclit:
                $ malickclit = False
                pc "Suck my clit, [ma]."
                scene d11maggyf2 with dissolve
                ma "Mhh... you like that?"
                pc "I love it, your tongue feels amazing!"
                pause
                jump d11malfm
            "Lick it." if not malickclit:
                $ malickclit = True
                pc "Can you lick it again?"
                scene d11maggyf3 with dissolve
                pause
                jump d11malfm
            "Go on.":
                pause
                pc "You look so hot between my legs, [ma]."
                ma "Hn-nhh...you taste delicious."
                jump d11malfm
            "Cum":
                pass
    pc "Shit, [ma]..."
    ma "Mh-hm! Mhh-mh!"
    hide screen povscreen with dissolve
    hide screen povbutton
    if pcgender == "woman":
        scene d11maggyfcum1 with flash
    elif mabjdeep:
        scene d11maggymcum1 with flash
    else:
        scene d11maggymcum2 with flash
    pc "Fuck!" with vpunch
    if pcgender == "woman":
        scene d11maggyfcum1 with flash
    elif mabjdeep:
        scene d11maggymcum1 with flash
    else:
        scene d11maggymcum2 with flash
    pc "Fuck!"
    if pcgender == "woman":
        scene d11maggyfcum1 with flash
    elif mabjdeep:
        scene d11maggymcum1 with flash
    else:
        scene d11maggymcum2 with flash
    pc "Shit!" with vpunch
    scene black with slowdissolve
    pc "Damn, [ma], that was incredible."
    scene d11maggy77 with dissolve
    ma "I was hoping you'd say that."
    scene d11maggy78 with dissolve
    ma "Maybe we can go a little bit further next time."
    pc "Next time, huh. I wouldn't mind."
    ma "Oh, I bet."
    ma "Well, I guess I better go back to work, before my boss comes back, and I bet you have better stuff to do as well."
    scene d11maggy79 with dissolve
    pc "I wouldn't say better, but yeah, I should probably leave as well..."
    scene d11maggy80 with dissolve
    ma "It would be quite embarrassing if my boss would come in on us now."
    scene d11maggy81 with dissolve
    pc "Heh, yeah..."
    scene d11maggy82 with dissolve
    ma "Feel free to come visit me anytime soon."
    pc "Oh? Is that an invitation?"
    ma "Our special customers are always welcome, no need for an invitation."
    pc "I see, then I'm glad I'm such a special customer."
    scene black with fade
    $ renpy.end_replay()
    $ gotomaggy = False
    scene bm-map with dissolve
    call screen wmap with dissolve