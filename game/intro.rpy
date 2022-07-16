label intro:
    #window hide
    play music "audio/memory.mp3" fadein 1
    scene black with dissolve
    n "Somewhere in a cab."
    play sound "audio/driving.ogg" fadein 1
    scene introcabpcdrivehome with dissolve
    pcthink "Alright, almost there..."
    pcthink "...it feels weird to come back here..."
    pcthink "After all these years to be back in my hometown..."
    pcthink "Who would have guessed I'd ever come back..."
    pcthink "...just for a job."
    pcthink "..."
    scene black with fade
    scene intro_cab2 with dissolve
    pcthink "We must be close to the hotel..."
    pcthink "I hope the new apartment is ready when I move in, in a few days..."
    pcthink "And that it looks as good as it does in the pictures."
    pcthink "...maybe I should have a look before I go to the hotel?"
    pcthink "On the other hand, my stuff won't be shipped for another few days, and I can't move in yet anyway..."
    pcthink "Naaah, whatever, I'm too curious right now. I'll have a look!"
    scene black with fade
    stop sound fadeout 2
    scene intro cab pc arrive home with dissolve
    "Cab driver" "Alright, that's as close as we can get."
    "Cab driver" "As I said earlier, the road is blocked by construction work, but it's not far from here anyway."
    pc "That's okay, I'll walk."
    "Cab driver" "You know the way?"
    pc "Yeah, I grew up in this town."
    "Cab driver" "'Kay, good luck."
    scene black with dissolve
    n "You give the driver his money and walk towards your new apartment, using some side roads you still remember from the past."
    n "As you turn into a small alley you notice a girl looking at you."
    scene 2walk with dissolve
    pcthink "Huh?! Why is that girl looking at me like that?"
    pcthink "Do I know her?"
    scene 2walk close with dissolve
    pcthink "She's cute... I guess I'd remember her."
    if pcgender == "woman":
        pcthink "I love her hair..."
        n "You give her a small smile as you walk by."
    scene pcwalk with dissolve
    pcthink "She must have fallen for me at first sight...haha."
    pcthink "Anyway, my new apartment should be just around the corner."
    pcthink "My new home in my old hometown."
    pcthink "...What the?!"
    scene black with dissolve
    stop music fadeout 2
    play music "audio/LightSteps.mp3" fadein 1
    n "As you go around the corner you see the building where your soon-to-be apartment is located in flames."
    n "You run towards the building, but a cop stops you."
    scene apartment burn police1 with dissolve
    "Cop" "Hey! Stop! What do you think you're doing?"
    pc "T-That is my new apartment!"
    "Cop" "Your apartment?"
    pc "Y-yeah, I mean, I haven't moved in yet, but still..."
    "Cop" "You haven't moved in yet, and it's already on fire?"
    scene apartment burn police2 with dissolve
    "Cop" "...that sounds fishy! Let me see your ID!"
    pc "What? I just arrived in the city! I haven't been here for years!!"
    "Cop" "Yeah, that's what they all say... Your ID!"
    pc "Who are \"they\"? This doesn't make any sense!"
    "Cop" "Listen, [boygirl]! If you don't show me your ID right now, I have some comfortable cuffs and a cosy little holding cell waiting for you." 
    pc "Ugh, this is insane...!"
    pc "Fine... Here is my ID... and don't call me [boygirl]..."
    scene black with dissolve
    n "You give him your ID and answer a lot of stupid questions while the officer is treating you like a felonious gangster."
    n "After a while..." with slowdissolve
    scene apartment burn police2 with dissolve
    "Cop" "...and you better stay in the city, or you'll be in trouble!"
    pc "Yeah, yeah, sure..."
    pcthink "Asshole..."
    scene black with dissolve
    stop music fadeout 2
    pcthink "Damn, the day started out so well and now this..."
    n "You head to the hotel..."
    pause 1
    play music mainbgm fadein 1
    scene intro_hotel1 with slowdissolve
    "Receptionist" "Good evening, how can I help you?"
    pc "Hey, I booked a room for a few days, the name is..."
    if renpy.get_style_preference("txtbox") == "off":
        $ txtboxoff = True
        $ renpy.set_style_preference("txtbox", "on")
    $ mcname = renpy.input(_("Choose your first name."), default=pcname)
    $ mcsure = renpy.input(_("Choose your last name."),default=surename)
    $ pc_name = mcname.strip()
    if pc_name == "":
        $ pc_name = pcname
    $ pcthink_name = pc_name
    $ bpc = pc_name.upper()
    $ pcmd = pc_name
    
    $ pc_sure = mcsure.strip()
    if pc_sure == "":
        $ pc_sure = surename
    if pcgender == "woman":
        $ persistent.pc_fname = pc_name
        $ persistent.pc_fsure = pc_sure
        $ persistent.pcmdf = pc_name
    else:
        $ persistent.pc_mname = pc_name
        $ persistent.pc_msure = pc_sure
        $ persistent.pcmdm = pc_name
    $ persistent.pc_name = pc_name
    if txtboxoff:
        $ renpy.set_style_preference("txtbox", "off")
    scene intro_hotel2 with dissolve
    "Receptionist" "Uhm... uh-huh, yes..."
    pcthink "Hum... should I tell her that her areolas are peaking out of her top?"
    scene intro_hotel3 with dissolve
    "Receptionist" "It's room number 24 on the second floor."
    scene intro_hotel4 with dissolve
    "Receptionist" "Here's the key. Have a pleasant stay!"
    pc "Thanks, I hope so."
    scene black with dissolve
    scene hotelroom with dissolve
    pc "At least the room seems to be okay..."
    pc "..."
    pc "Looks like I need to find a new apartment... As soon as possible!"
    pc "Yaaaahwn..."
    pc "...damn, I'm tired."
    pc "Shit, it's late already..."
    pc "I better go to bed... I can't do anything at this time anyway."
    stop music fadeout 3
    jump intro_day1
