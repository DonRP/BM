default tt = Tooltip("")
screen map_home_hall_entrance():
    imagemap:
        auto "maps/home_hall_entrance_%s.png"
        hotspot (834, 343, 280, 418) clicked [ tt.Action(""), Jump("leavehome") ] hovered tt.Action(_("Leave Home"))
        hotspot (1489, 259, 200, 696) clicked [ tt.Action(""), Jump("bedroom") ] hovered tt.Action(_("Rachel's Bedroom"))
        hotspot (284, 215, 261, 764) clicked [ tt.Action(""), Jump("kitchen") ] hovered tt.Action(_("Kitchen"))
        hotspot (1705, 0, 214, 1079) clicked [ tt.Action(""), Jump("hall") ] hovered tt.Action(_("Hall"))
        hotspot (0, 0, 262, 1079) clicked [ tt.Action(""), Jump("livingroom") ] hovered tt.Action(_("Livingroom"))
    text _("Where do you want to go?") yalign 0.1 xalign 0.5
    text "[tt.value!t]" yalign 0.15 xalign 0.5

screen map_home_hall():
    imagemap:
        auto "maps/home_hall_%s.png"
        hotspot (1370, 245, 223, 827) clicked[ tt.Action(""),  Jump("pcroom") ] hovered tt.Action(_("Your Room"))
        hotspot (1060, 328, 85, 365) clicked [ tt.Action(""), Jump("childroom") ] hovered tt.Action(_("Ellie's Room"))
        hotspot (656, 313, 93, 373) clicked [ tt.Action(""), Jump("bathroom") ] hovered tt.Action(_("Bathroom"))
        hotspot (0, 0, 362, 1077) clicked [ tt.Action(""), Jump("entrance") ] hovered tt.Action(_("Entrance Hall"))
        hotspot (802, 529, 221, 172) clicked [ tt.Action(""), Jump("halldesk") ] hovered tt.Action(_("Desk"))
        hotspot (1656, 0, 261, 1079) clicked [ tt.Action(""), Jump("livingroom") ] hovered tt.Action(_("Livingroom"))
    text _("Where do you want to go?") yalign 0.1 xalign 0.5
    text "[tt.value!t]" yalign 0.15 xalign 0.5
        
screen map_hall_back():
    imagemap:
        auto "maps/hall_back_%s.png"
        hotspot (577, 266, 106, 536) clicked [ tt.Action(""), Jump("pcroom") ] hovered tt.Action(_("Your Room"))
        hotspot (1136, 144, 239, 590) clicked [ tt.Action(""), Jump("entrance") ] hovered tt.Action(_("Entrance Hall"))
        hotspot (704, 226, 444, 456) clicked [ tt.Action(""), Jump("livingroom") ] hovered tt.Action(_("Livingroom"))
    text _("Where do you want to go?") yalign 0.1 xalign 0.5
    text "[tt.value!t]" yalign 0.15 xalign 0.5
    

screen wmap():
    add "maps/bm-map.jpg"
    if visit_cafe_d6 or (visit_e_d6 and hlo < 3) or (visit_work_d6 and hlo < 3):
        $ go_home = True
        $ visit_cafe_d6 = False
        $ visit_work_d6 = False
    if livingHomeDays == 11 and not gotomaggy and not gotowork:
        $ go_home = True

    if livingHomeDays != 4 != 9 and gotoschool: 
        imagebutton:
            focus_mask True
            auto "maps/wmschool_%s.webp"
            clicked [ tt.Action(""), Jump("school")]
            hovered tt.Action("School") yalign .99 xalign .99
    if livingHomeDays > 2 and livingHomeDays < 9 and gotocafe or (livingHomeDays == 9 and tc and seentd9 == False) or (livingHomeDays == 11 and gotocafe and gotowork):
        imagebutton:
            focus_mask True
            auto "maps/wmdowntown_%s.webp"
            clicked [ tt.Action(""), Jump("cityStreet") ]
            hovered tt.Action("Downtown")
    if livingHomeDays > 5 and gotowork:
        imagebutton:
            focus_mask True
            auto "maps/wmwork_%s.webp"
            clicked [ tt.Action(""), Jump("working") ]
            hovered tt.Action("Atomic Aeronautics") xalign .99
    if livingHomeDays == 9 and not go_home or (livingHomeDays == 11 and gotomaggy):
        imagebutton:
            focus_mask True
            auto "maps/wmmaggy_%s.webp"
            clicked [ tt.Action(""), Jump("rental") ] 
            hovered tt.Action("Rental Company") xalign .99 yalign .5
    if go_home:
        imagebutton:
            focus_mask True
            auto "maps/wmhome_%s.webp"
            clicked [ tt.Action(""), Jump("home") ]
            hovered tt.Action("Home") yalign .5 xalign .5
    text _("Where do you want to go?") yalign 0.03 xalign 0.5
    textbutton "[tt.value!t]" yalign 0.5 xalign 0.5 text_outlines [ (3, "#000", 0, 0) ]
        
   
screen scrbjhpov():
    zorder 99   
    imagebutton auto "switch_cam1_%s.png" clicked Jump("bjhtrd") yalign .01 xalign .99 at btnzoom
screen scrbjhtrd():
    zorder 99   
    imagebutton auto "switch_cam2_%s.png" clicked Jump("bjhpov") yalign .01 xalign .99 at btnzoom
screen povbutton():
    if povstart:
        add "switch_cam1_idle.png" yalign .01 xalign .99 at btnZoomSwitch
        $ store.povstart = False
    if campov:
        imagebutton auto "switch_cam1_%s.png" action [ ToggleVariable("campov", true_value=True,false_value=False), Show("povscreen", povimage=pov1) ] yalign .01 xalign .99 at btnzoom
    else:
        imagebutton auto "switch_cam2_%s.png" action [ ToggleVariable("campov", true_value=True,false_value=False), Show("povscreen", povimage=pov2) ] yalign .01 xalign .99 at btnzoom
screen povscreen(povimage):
    add povimage
    use povbutton

label pcroom:
    $ pcLocation = "h_pcroom"
    if storyEvent == False and (livingHomeDays < 6 or livingHomeDays > 8):
        if livingHomeDays == 2 and daylyActions == 15:
            jump stuffArrivesDay3
        else:
            scene pcroom with dissolve
            pause
            jump whatToDoHome
    elif SEsearchforsis == True:
        jump elliePCRoomSleepDay0
    elif SEpcDay1Morning == True:
        jump wakeupDay1
    elif livingHomeDays == 3 and doonce == False:
        jump wakeupDay3
    elif SEAfterEBD == True and not SERachelBRAfterEBD:
        jump afterEBD
    elif SERachelBRAfterEBD == True:
        pcthink "I need to use the bathroom..."
        call screen map_home_hall
    elif SEWork == 1 and livingHomeDays == 4:
        pcthink "I should let her sleep."
        call screen map_home_hall
    elif livingHomeDays == 5:
        jump d5morning
    elif livingHomeDays == 6 and storyEvent == False:
        jump d6morning
    elif livingHomeDays == 7 and storyEvent == False:
        $ storyEvent = True
        jump d7_wakeup
    elif livingHomeDays == 8 and storyEvent == False:
        jump d8_morning
    elif livingHomeDays == 9 and storyEvent == True:
        if d9_wakeup:
            scene pcroom with dissolve
            pcthink "Did I forget anything?"
            scene home_hall_entrance_idle with dissolve
            call screen map_home_hall_entrance
        else:
            jump d9_morning_wakeup
    elif livingHomeDays == 10:
        jump d10wakeup
        
    elif livingHomeDays == 11 and d11morning:
        jump d11wakeup
    elif livingHomeDays == 12:
        jump d12morning
    else:
        scene pcroom with dissolve
        pause
        scene home_hall_idle with dissolve
        call screen map_home_hall
        
screen cr_image():
    add "jpg/childroom_lookaround.jpg"
    imagebutton:
        auto "jpg/childroom_lookaround_%s.webp"
        focus_mask True
        action [SetVariable("seenboard", 1), Jump("eboard")]
    imagebutton:
        auto "jpg/childroom_lookaround2_%s.webp"
        focus_mask True
        action Jump("ehifi")
label eboard:
    scene childroom_lookaround2 with dissolve
    pause
    if not _preferences.language == None:
        pcthink "Hmm, what does the image say... \"I'll be making noise with my brother tonight, so please bear with us, sorry.\""
        pcthink "\"{b}Incest{/b} - if you're about to do it, please inform your neighbours, so they know what's going on.\""
    pcthink "Well that's interesting..."
    pcthink "I wonder if [m] has ever seen it..."
    if _preferences.language == None:
        pcthink "...but she probably never really took a closer look..."
    else:
        pcthink "...but she probably doesn't even understand english..."
    #achievement
    $achievement.grant("Achievement_eboard")
    init: 
        $achievement.register("Achievement_eboard")
        $achievement.sync()
    $achievement.sync()
    ###########
label ehifi:
    if seenboard:
        scene black with slowdissolve
        call screen map_hall_back
    scene childroom_lookaround with dissolve
    pcthink "Hmm... the clock is showing the wrong time..."
    call screen cr_image
        
label childroom:
    if storyEvent == True and livingHomeDays > 0 and not seenboard:
        if SErachelPills2nd == True:
            pcthink "I have to talk with [m] about that Therapist!"
        elif SErachelPills3rd == True:
            pcthink "I have to talk with [m]."
        elif SEsisBDayPresent == True and not doonce2:
            jump childroomESleepDay3
        else:
            $ pcLocation = "h_childroom"
            scene childroom front with dissolve
            pause
            scene childroom back with dissolve
            pause
            if livingHomeDays == 9:
                scene childroom_lookaround3 with dissolve
                pcthink "Huh? What's this?"
                scene childroom_lookaround with dissolve
                call screen cr_image
                
            pause
    elif SEsearchforsis == True:
        $ pcLocation = "h_childroom"
        scene childroom front with dissolve
        pause
        scene childroom back with dissolve
        pause
    else:
        scene hall door with dissolve
        if workTime == True:
            pcthink "I shouldn't go in there when she's not home."
        else:
            pcthink "I have no reason to go in there at the moment."
    scene hall_back_idle with dissolve
    call screen map_hall_back


label halldesk:
    $ pcLocation = "h_hall"
    scene home_hall_idle with dissolve
    pcthink "Boxes full of paperwork. Nothing special."
    if livingHomeDays >= 9:
        menu:
            "Look closer.":
                if not ptest:
                    scene black with slowdissolve
                    n "You rummage through the paperwork..."
                    n "Most of the documents are uninteresting, old bills, some insurance documents... but you also find the deed of ownership of the house with your name on it."
                    pcthink "Good to know where it is..."
                    n "You go on but there seems to be nothing of interest left..."
                    menu:
                        "Keep going.":
                            pc "{cps=3}...{/cps}"
                            extend "."
                            extend "."
                            extend "."
                            pcthink "Hmm? What's this?"
                            scene home_hall_idle with dissolve
                            show ptest1 with dissolve
                            pause
                            show ptest2 with dissolve
                            pause
                            pcthink "Look at that, [m] didn't lie, [e] really is my sister after all..."
                            scene black with dissolve
                        "No point in going on...":
                            pass
                else:
                    pcthink "Doesn't look like there's anything left to discover..."
            "Nah, better not touch it.":
                pass
    scene home_hall_idle with dissolve
    call screen map_home_hall
label entrance:
    $ pcLocation = "h_entrance"
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance
label leavehome:
    if not SEGetEFromSchool and not SEsisBDayPresent and not SEWork or (storyEvent == False and SEWork >= 1):
        scene home_hall_entrance_idle with dissolve
        pcthink "I have no reason to go outside at the moment."
        call screen map_home_hall_entrance
    elif SEd7walk:
        scene black with slowdissolve
        jump d7_city
    elif livingHomeDays == 9:
        $ pcLocation = "h_leave"
        scene black with dissolve
        pcthink "Alright, [ma] said to come over after work time, so I guess I should do whatever else I want to do before I go to the rental company..."
        call screen wmap
    else:
        $ pcLocation = "h_leave"
        scene black with dissolve
        call screen wmap
label bedroom:
    if storyEvent == False or SEsearchforsis == True:
        $ pcLocation = "h_bedroom"
        scene bedroom with dissolve
        pause
    elif SErachelPills1st == True:
        jump rachelPills1st
    elif SErachelPills2nd == True:
        jump rachelPills2nd
    elif SErachelPills3rd == True:
        jump rachelPills3rd
    elif livingHomeDays == 9 and not seenebc:
        scene bedroom_lookaround with dissolve
        show screen ebc
        pause
        hide screen ebc
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance
screen ebc():
    add "jpg/bedroom_lookaround.jpg"
    imagebutton:
        auto "jpg/bedroom_lookaround_%s.webp"
        focus_mask True
        action [SetVariable("seenebc", 1), Jump("ebc_")]
label ebc_:
    hide screen ebc
    scene bedroom_lookaround2 with dissolve
    pcthink "Huh, what's that?"
    scene ebc with dissolve
    pause
    pcthink "So she really is..."
    scene bedroom_lookaround2 with dissolve
    pcthink "The old man didn't seem too confident though..."
    #achievement
    $achievement.grant("Achievement_ebirth")
    init: 
        $achievement.register("Achievement_ebirth")
    $achievement.sync()
    ###########
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance
label kitchen:
    $ pcLocation = "h_kitchen"
    if (storyEvent == False or SEsearchforsis == True) and (daylyActions > 14 or SEsearchforsis == True):
        scene kitchen rachel doing breakfast with dissolve
        pause
    elif SEWork == 1 and not storyEvent:
        scene kitchen rscrub floor1 with dissolve
        pcthink "Looks like [m] is scrubbing the kitchen floor..."
    else:
        scene kitchen with dissolve
        pause
    scene home_hall_entrance_idle with dissolve
    call screen map_home_hall_entrance
label school:
    if SEGetEFromSchool == True:
        jump getEfromSchool1
    elif storyEvent and livingHomeDays == 6 and not visit_e_d6:
        jump eschool_d6
    else:
        scene school1 with dissolve
        pcthink "Looks like there is no one here I know."
        scene black with dissolve
        $ gotoschool = False
        call screen wmap
        
label cityStreet:
    if SEsisBDayPresent and livingHomeDays == 3:
        $ SEsisBDayPresent = False
        jump pcCityDay3
    elif storyEvent and SEWork == 1 and livingHomeDays < 6:
        scene city4 with dissolve
        pcthink "Okay, I think I have to go right at the end of the street."
        pcthink "Hum... I wonder if the cafe is open today... and if the girl, what was her name? [h]? ...is there..."
        pcthink "Maybe I should have a look before I check the office? It's not like I'm in a hurry."
        menu:
            "Check the cafe.":
                pcthink "Yep, nothing better than a nice, hot coffee served by a cute girl."
                scene black with fade
                jump cafeBeforeOffice
            "Go to the office.":
                scene city_5 with dissolve
                pcthink "Yeah, whatever, let's go to the office."
                jump officeFirst
    elif storyEvent and livingHomeDays == 6 and not visit_cafe_d6:
        jump cafe_d6
    elif livingHomeDays == 9 and tc:
        jump d9_tcoffee
    elif livingHomeDays == 11:
        jump d11visitcafe
    else:
        pcthink "Hum... nothing to do... here."
        scene black with dissolve
        call screen wmap
        
label working:
    if storyEvent and livingHomeDays == 6 and not visit_work_d6:
        pcthink "Yeah, I could check the company, maybe there's something new..."
        scene black with dissolve
        n "You head to Atomic Aeronautics and enter the building."
        jump job_d6
    elif livingHomeDays == 9:
        jump porngirls
    elif livingHomeDays == 11:
        jump d11work
    else:
        pcthink "Should I? ... nah, better not."
        call screen wmap
label home:
    if livingHomeDays == 6:
        $ go_home = False
        jump d6_wayBackHome
    if livingHomeDays == 11:
        $ go_home = False
        jump d11stepladder
        
label rental:
    if livingHomeDays == 9:
        jump maggy1
    if livingHomeDays == 11:
        jump d11maggy