init:
    $ import datetime
    $ today = datetime.date.today()
    $ tomorrow = today + datetime.timedelta(days=1)
init -2 python:
    class GetInput(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)
init python:
    def playmov(mov):
        m = renpy.get_registered_image(mov)
        if not m:
            return
        c = m.channel
        renpy.show(mov)
        d = 0
        while d == 0:
            renpy.pause(.001)
            d = renpy.music.get_duration(c)
        renpy.pause(d)
        renpy.hide(mov)
        
    def ResetToDefaults():
        _preferences.volumes['music'] = 0.4
        _preferences.volumes['sfx'] = 0.5
        _preferences.volumes['voice'] = 0.4
        renpy.restart_interaction()

    renpy.music.register_channel("music", "music", True)
    renpy.music.register_channel("sbgm", "music", True)
default preferences.show_empty_window = False           
define config.gestures = { "n" : "hide_windows", "e" : "skip", "s" : "game_menu", "w" : "rollback" }              
#narrator
define n = Character(None, what_style="centered_text", window_style="centered_window",
                          window_xfill=True,
                          window_yfill=True,
                          window_background="images/n_bg.png",
                          what_color="#ddd"
    )
define q = Character(None, what_style="centered_text", window_style="centered_window",
                          what_xalign=0.5,
                          window_xalign=0.5,
                          window_yalign=0.1,
                          what_text_align=0.5,
                          window_background=None,
                          what_outlines=[(3, "#000", 2, 2), (3, "#ddd", 0, 0)],
    )
    
#unnamed chars
define name_only = Character(None)
#main chars
define pc = Character("[pc_name]", who_color="#2b68b2")
define pcsure = Character("[pc_sure]")
define pcgender = "[pcgender]"
define pcthink = Character("[pcthink_name]", who_color="#2b68b2", who_italic=True, what_italic=True, what_style="thinking_dialogue", what_prefix="(", what_suffix=")")
define e = Character("Ellie", color="#8201ac", what_size=25)
define m = Character("[name_m]", color="#1e8510")
define j = Character("Jada", color="#b07000")
define t1 = Character("Therapist")
define t = Character("Katherine", color="#c30000")
define ts = Character("Katie", color="#c30000")
define r = Character("Melinda")
define h = Character("Hanna", who_color="#dcdf00")
define st = Character("Steph", who_color="#005a02")
define boss = Character("C.J.") #Colin-James Olafsson
define w = Character("Ward")
define oc_ = Character("Old cop", who_color="#8b4a0b")
define oc = Character("Johnson", who_color="#8b4a0b")
define ma = Character("Maggy")
define em = Character("Em", who_color="#570058") #Emily
define jess = Character("Jess", who_color="#cc5dcd") #Jessica

default name_m = "Rachel"

default pc_name = persistent.pc_name
default pcthink_name = pc_name
# Version
default uVersion = 0
default steamy = True
#style
default txtbxstl = "on"
    
if renpy.variant("touch"):
    transform btnzoom:
        zoom .5
else:
    transform btnzoom:
        zoom 0.2
transform emote:
    yalign 0.1 #  Top.
    xalign 0.9 #  Right. 
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
transform ephone:
    ypos 0
    xpos 0
    
style emote_S:
    size 65
    color "#fff"
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

    
define flash = Fade(0.1, 0.0, 0.1, color="#fff")
define blink = Fade(0.1, 0.0, 0.1, color="#000")
define fade = Fade(1, 1.0, 1)
define slowdissolve = Dissolve(2)
transform my_shake:
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        
transform brakeshake(x=5, y=5, t=.05):
    parallel:
            linear t xoffset -x
            linear t * 2 xoffset x
            linear t xoffset -x
            linear t * 2 xoffset x
            linear t xoffset -x
            linear t * 2 xoffset x
    parallel:
            linear t yoffset -y
            linear t * 2 yoffset y
            linear t yoffset -y
            linear t * 2 yoffset y
            linear t yoffset -y
            linear t * 2 yoffset y
transform brakeshake_end(x=5, y=5, t=.05):
    parallel:
            linear t * 2 xoffset x
            linear t xoffset -x
            linear t * 2 xoffset x
            linear t xoffset -x
            linear t * 2 xoffset x
            linear t xoffset 0
    parallel:
            linear t * 2 yoffset y
            linear t yoffset -y
            linear t * 2 yoffset y
            linear t yoffset -y
            linear t * 2 yoffset y
            linear t yoffset 0
        
# Animations
transform dream:
    linear 0.5 xoffset -2 yoffset 2 
image dream_01:
    "anim/dream_01.jpg" with dissolve
    pause .4
    "anim/dream_02.jpg" with dissolve
    pause .4
    "anim/dream_03.jpg" with dissolve
    pause .4
    "anim/dream_04.jpg" with dissolve
    pause .4
    "anim/dream_05.jpg" with dissolve
    pause .4
    "anim/dream_06.jpg" with dissolve
    pause .4
    "anim/dream_07.jpg" with dissolve
    pause .4
    "anim/dream_08.jpg" with dissolve
    pause .4
    "anim/dream_09.jpg" with dissolve
    pause .4
    "anim/dream_10.jpg" with dissolve
    pause .4
    "anim/dream_11.jpg" with dissolve
    pause .4
    "anim/dream_12.jpg" with dissolve
    pause .4
    "anim/dream_13.jpg" with dissolve
    pause .4
    "anim/dream_14.jpg" with dissolve
    pause .4
    "anim/dream_15.jpg" with dissolve
    pause .4
    "anim/dream_16.jpg" with dissolve
    pause .4
    repeat

image motel_static:
    "/anim/motelroom tv.jpg"
    pause 1.0
    "/anim/motelroom tv2.jpg"
    pause 0.2
    "/anim/motelroom tv3.jpg"
    pause 0.1
    "/anim/motelroom tv4.jpg"
    pause 0.5
    "/anim/motelroom tv5.jpg"
    pause 0.1
    "/anim/motelroom tv4.jpg"
    pause 0.1
    "/anim/motelroom tv3.jpg"
    pause 0.1
    "/anim/motelroom tv2.jpg"
    pause 0.2
    repeat  

image livingroom_tv:
    "/anim/livingroom tv1.jpg"
    pause 2
    "/anim/livingroom tv2.jpg"
    pause 2
    "/anim/livingroom tv3.jpg"
    pause 3
    repeat  

image ebj_ac:
    "/anim/ebj_ac_00.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_01.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_02.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_03.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_04.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_05.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_06.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_07.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_08.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_09.jpg" with dissolve
    pause 0.3
    "/anim/ebj_ac_10.jpg" with dissolve
    pause 0.3
    repeat

image jbikebrake:
    "/anim/after_kandbf3_20.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_21.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_22.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_23.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_24.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_25.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_26.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_27.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_28.jpg" with dissolve
    pause 0.1
    "/anim/after_kandbf3_29.jpg" with dissolve
    pause 0.1

image d9_morning_e:
    "images/jpg/d9_morning_br04.jpg" with dissolve
    pause 1
    "images/jpg/d9_morning_br04_2.jpg"
    pause .5
    repeat
    
image maggyoffice28:
    "images/jpg/maggy_office28.jpg" with dissolve
    pause 1
    "images/jpg/maggy_office29.jpg" with dissolve
    pause 2
    repeat

    #################
image mm_anim:
    "images/jpg/livingroom rachel couch1.jpg" with dissolve
    pause 7
    "images/jpg/home welcome ellie closeup2.jpg" with dissolve
    pause 7
    "images/jpg/coffeehouse waitress.jpg" with dissolve
    pause 7
    "images/jpg/hall jada look back.jpg" with dissolve
    pause 7
    "images/jpg/bathroom rachel check bath.jpg" with dissolve
    pause 7
    "images/jpg/pcroom sitonchair esmilebeforejump_mirrored_mm.jpg" with dissolve
    pause 7
    repeat

image d9jbathroom09:
    "images/jpg/d9_j_bathroom09.jpg" with dissolve
    pause 1
    "images/jpg/d9_j_bathroom09_2.jpg" with dissolve
    pause 1
    repeat
    
image d10bth:
    "images/jpg/d10bth21.jpg" with dissolve
    pause .2
    "images/jpg/d10bth21_2.jpg" with dissolve

transform zoomEffect:
    ease 7 truecenter zoom 1.1
    ease 7 truecenter zoom 1
    repeat
    #################
    
transform btnZoom:
    zoom 0.2
    xalign 0.5
    yalign 0.5
transform btnZoomSwitch:
    xalign 0.99
    yalign .01
    linear .2 zoom 0.2
transform delbtn:
    zoom 0.3
    xalign 0.99
    ypos -80
label splashscreen:
    scene childroom back with dissolve
    pause 1
    scene splash1 with flash
    pause 1
    scene splash2 with slowdissolve
    pause 3
    scene black with dissolve
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .4
            _preferences.volumes['sfx'] *= .5
            _preferences.volumes['voice'] *= .4
return
label start:
    stop music
    $ pc_name = "You"
    $ pcthink_name = pc_name
    if not steamy:
        n "This game is a work of fiction, all characters are at least 99 years old and obviously not related to any living persons.\n" with fade
    else:
        n "This game is a work of fiction, all characters are designed to represent their age in the game and are at least 18 years old. None of the characters are in any way related to any living persons.\n" with fade
    n "If you're not an adult, close the game now, delete it, and burn your computer/mac/phone! DON'T CLICK AGAIN, OR...\n"
    extend "...or the game starts as usual ;_;"
    $ renpy.set_style_preference("txtbox", "on")
    menu:
        "Play as Man":
            $ save_name = "male"
            #achievement
            $achievement.grant("Achievement_malemc")
            init: 
                $achievement.register("Achievement_malemc")
            $achievement.sync()
            ###########
            pass
        "Play as Woman (lesbian)":
            $ save_name = _("female")
            $ pcgender = "woman"
            $ mrms = _("Ms.")
            $ heshe = _("she")
            $ boygirl = _("girl")
            $ md = _("Mommy")
            $ ds = _("daughter")
            $ himher = _("her")
            $ pcname = _("Jill")
            $ bs = _("sister")
            $ hisher = _("her")
            #achievement
            $achievement.grant("Achievement_femalemc")
            init: 
                $achievement.register("Achievement_femalemc")
            $achievement.sync()
            ###########
    $ persistent.pcgender = pcgender
    call screen showtextbox 
    jump intro
    
label start_rachel:
    $ save_name = "Rachels Story"
    scene black with dissolve
    $ mc_name = persistent.mc_name
    $ mc_sure = persistent.mc_sure
    m "Hello [pc] [pcsure], this is a test!"
    
label endGame:
    scene uh-oh with dissolve
    pause 1
    scene black with dissolve
    n "This is the end of the current version, a quick save has been created."
    n "I hope you had fun! Be sure to check back soon. The story will progress a lot over time ;)"
    show d7_pcroom_kitty2:
        alpha 0.0
        time 1
        linear 1.0 alpha 1.0
    if not steamy:
        n "{size=+20}{b}Special thanks to all my {a=https://www.patreon.com/bmgames}{b}{color=#FF9D1F}Patrons{/color}{/b}{/a} and {a=https://subscribestar.adult/bm-games}{b}{color=#FF9D1F}Subscriber{/color}{/b}{/a}\nand everyone who helped me in some way.\nyou guys are awesome!{/b}{/size}"
    else:
        n "{size=+20}{b}Special thanks to all my supporters, testers and everyone who helped me in some way.\nyou guys are awesome!{/b}{/size}"
    #$ persistent.endGame = True
    $ persistent.gallery_special = True
    $ renpy.full_restart()
label gameOverE:
    scene uh-oh with slowdissolve
    pause 1
    n "Congratulation! You broke her heart...idiot!"
    $ renpy.full_restart()