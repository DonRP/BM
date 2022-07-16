init python:
    #images
    def galeryImg(imgID):
        if renpy.seen_image(imgID):
            return imgID
        else:
            return "nope_i.jpg"
    #scenes
    def galeryImgscene(imgIDscene):
        if renpy.seen_image(imgIDscene):
            return imgIDscene
        else:
            return "nope.jpg"
    #special images
    def galeryImgSpecial(imgIDspecial):
        if imgIDspecial:
            return imgIDspecial
            
define nameByID = ["bathroom pcfem mirror",
                "bathroom rachel shower2",
                "pcroom sitonchair eonlap2",
                "livingroom diningtable dinner2",
                "livingroom diningtable dinner4_2",
                "pcroom esorry2",
                "pcroom jandehelpunpack jtitties",
                "pcroom day2 night epeek",
                "bedroom rachelmast1",
                "bedroom rachelmast titties3",#
                "coffeehouse2_4",
                "porn-vr1_4",
                "pcroom ebd_jadavr2",
                "pcroom ebd_jadavr9",
                "childroom ebd9",
                "bathroom ebd tmolest4_1",
                "livingroom ebd all rtobed9",
                "ebd jadahome5_2",
                "pcroom afterebd3",#
                "bathroom rachel_afterebd3",
                "childroom kitty31",
                "childroomkitty27",
                "coffeehouse3_4_2",
                "coffeehouse3_9_1",
                "coffeehouse3_11",
                "job intro1",
                "pcroomehump2",
                "pcroom_ehump4",
                "epic",#
                "holdingcell7",
                "jbikebrake",
                "after_kandbf6",
                "job_d6_sort6",
                "job_d6_sort8",
                "coffeehouse_d6_h21",
                "coffeehouse_d6_h19",
                "bedroom_d6_backhome3",
                "bedroom_rpills3_2",#
                "pcroom_tcoerce3_1",
                "pcroom_d6_jakiss_4",
                "pcroom_d6_j_mc_undress6",
                "pcroom_d7_wakeup_j6",
                "pcroom_d7_wakeup_j16",
                "jmotelf200",
                "d7_motel_fendcum2",
                "kitchen_e_eat",
                "kitcheneeat_smile",
                "d7_pcroomkitty3",#
                "d8_jvr11",
                "d9_morning_br07",
                "d9_city09",
                "d9_job24",
                "d9_tcoffee39",
                "d9_jlick_01_0",
                "d9_jsuc_swallow1",
                "d9_jsuc_swallow2",
                "d9_eride",
                "d9_pcroom_eride_switch1",
                "d9_pcroom_backhome_e25",
                "d9_eride_cum_face",
                "d9_elick_cum",
                "d9_eride03_cum",
                "d10outdoor30",
                "d10ao08",
                "d10eshow02",
                "d10eshow03",
                "d10eshow10",
                "d10rshower11",
                "d10bth70",
                "kathouse41",
                "d10date70",
                "d11maggy59",
                "d11katvisit116",
                "d11katvisit145",
                "d11katvisit162_f",
                "d11katvisit176",
                "d11ev04",
                "d11evhall23",
                "d11evhall34",
                "d11night32",
                "d12wakeup08",
                "d12morning12",
                "d12morning36",
                "d12morning44",
                "d12morning46_m",
                "d12morning47",
                "d12morning48",
                "d12morning57",
                "d12morning58"
                ]

define nameByIDscene = [["bedroomrachelpcgrabtits","rachelPills2nd"],
                ["pcroomday2night2","eNightTwo"],
                ["bringjadahome1_3","bringJadaHome"],
                ["bathroomebdt2","coerceT1"],
                ["pcroom_codingwork_t9","tcoerce2_r"],
                ["pcroom_ehump_cum","eHumpNight5_r"],
                ["bedroom_rpills3_1","d6_rachel_pills_r"],
                ["hall_d6_kat4","coerceT3"],
                ["pcroom_d6_jakiss_4","d6_gotobed_withj"],
                ["d7_motel_jada24","d7_motel_r"],
                ["vrporn3_30","JVREbirthday"],
                ["porn_vr4","porn_vr_4"],
                ["d9_j_bathroom03","d9_backhome_j_fun"],
                ["d9egrind","d9_pcroom_e01"],
                ["d10rshower05","d10shower2"],
                ["d10night38","d10nightsex"],
                ["d11beforel12","d11jbeforlsex"],
                ["d11maggy56","d11maggylewd"],
                ["d11katvisit66","d11tfirsts"],
                ["d12morning12","d12rachels"]
                ]
                
define nameByIDSpecial = [["4",_("One of my ealiest test render from when I was working on the livingroom, added a char to test the lighting, kudos to you if you recognize the character, it's a really early version ;)")],
                ["5tre",_("360° VR test render of Ellie. She looks great in VR ;)")],
                ["cakeshop1",_("An early render of Ellie in a cake shop. I thought about adding a scene like that in the game, but didn't find an opportunity yet.")],
                ["eschoolphone",_("A test render I made for one of the in-game scenes, I thought it looked really cute, so I let it run for a while. There's some dirt on her mouth from the scene I was working on previously to this one. One of the reasons why test render are important.")],
                ["good_memories",_("A special render I made for the winner of a contest on the f95zone forum.")],
                ["htfdhfdrh",_("A test render I made while working on the scene where MC follows \"Katie\" to the old \"dopehead corner\". I was testing a few new camera and tone mapping styles I've learned.\nThey look great imo, but are too different from the rest of the game, so I decided against using it in production.")],
                ["j&e",_("A special render I made for the invitation screen of a specific discord server ;)")],
                ["kat",_("A special render I made after getting a few requests for a Kat render in the style I was testing previously.")],
                ["naughtyh3",_("A special render I made for fun. Hanna is one of my personal favorites in the game and I wanted to show a bit of her naughty side ;)")],
                ["kiss",_("One of the earliest renders of Ellie :3")],
                ["photo ellie",_("Like the previous render I made this one while thinking of some scenes in the early stages in development. The scene itself has changed a lot since then (including Ellie), but the main idea is still there: Ellie sends MC a photo made with her new phone.")],
                ["childroom kitty8",_("A render that didn't make it into the game because I made an error with the camera position and only noticed it after the render was finished.")],
                ["eelf",_("A random render I made after getting inspired by a painted image by the artist \"wlop\" on deviantart. The model is basically Ellie, I used her shape, but different hair and different skin.")],
                ["rn",_("A render I made for a contest a loooooong while ago. Not my best tbh, but hey, it was fun^^")],
                ["mel_test1",_("The very first version of Jada's mom. Pose and background are just random and not really related to the game (I always try to make render look kinda special, even if I'm just testing stuff).")],
                ["bellie1",_("One of my patreon/subscribestar special render, the topic was \"preggo Ellie\" *shrug*.")],
                ["j&ecycle2",_("Another patreon/ss special render. I really like this one, so I thought I'd include it here as well. There's a little non-canon story behind this. If you're wondering: Ellie and Jada are using a small tricycle for kids to search for MC^^")],
                ["pcroom_codingwork_t12_4", _("Unused render from the scene where Kat comes in our room to ask us some questions. I used a \"pussyshot\" instead ;)")]
                ]
                
default gridSize = 9
default page = 0
default infotext = ""
default pageImageCount =""
#placeholder image
image my_image:
    "nope.jpg" with dissolve

screen endRep():
    zorder 666
    imagebutton auto "exit_%s.png" action EndReplay() yalign .99 xalign .99

#main gallery menu
screen gallery():
    style_prefix "special"
    tag menu

    add "mm_anim" at zoomEffect
    vbox:
        style_prefix "galleryint"
        
        textbutton _("Scenes") action ShowMenu("g_scenes")
        textbutton _("Images") action ShowMenu("g_images")
        if persistent.gallery_special:
            textbutton _("Special") action ShowMenu("g_special")

    textbutton _("Return") action Return() xalign 0.5 yalign .99 text_outlines [ (0, "#333", 2, 2) ]

#gender choice
screen g_scene_gender(curr_scene):
    modal True
    style_prefix "choice"
    vbox:
        textbutton _("Male") action [ Hide("g_scene_gender"), Replay(curr_scene, scope={"pc_name":persistent.pc_mname, "pcthink_name":persistent.pc_mname, "pcgender":"man", "pcmd":persistent.pcmdm}) ]
        textbutton _("Female") action [ Hide("g_scene_gender"), Replay(curr_scene, scope={"pc_name":persistent.pc_fname, "pcthink_name":persistent.pc_fname, "pcgender":"woman", "pcmd":persistent.pcmdf}) ]
        textbutton _("Cancel") action Hide("g_scene_gender")
    
#image gallery
screen g_images():
    style_prefix "gallery"
    tag menu
    add "mm_anim" at zoomEffect
    default page = 0
    grid 3 3:
        for i in range(page*gridSize,(page+1)*gridSize):
            if i < len(nameByID):
                imagebutton:
                    idle galeryImg(nameByID[i])
                    hover LiveComposite(
                        (1920, 1080),
                        (0, 0), nameByID[i],
                        (0, 0), im.Alpha("h.jpg",0.3)
                        )
                    action Show("g_image_full", my_image=nameByID[i])
                    sensitive renpy.seen_image(nameByID[i])
                    at btnZoom
            else:
                imagebutton:
                    idle im.Alpha("h.jpg",0)
                    at btnZoom
    $ pageImageCount = nameByID
    use changePages
    
#scene gallery
screen g_scenes():
    style_prefix "gallery"
    tag menu
    add "mm_anim" at zoomEffect
    default page = 0
    grid 3 3:
        for i in range(page*gridSize,(page+1)*gridSize):
            if i < len(nameByIDscene):
                if persistent.pc_mname and persistent.pc_fname:
                    imagebutton:
                        idle galeryImgscene(nameByIDscene[i][0])
                        hover LiveComposite(
                            (1920, 1080),
                            (0, 0), galeryImgscene(nameByIDscene[i][0]),
                            (0, 0), im.Alpha("h.jpg",0.3)
                            )
                        action Show("g_scene_gender", curr_scene=nameByIDscene[i][1])
                        sensitive renpy.seen_label(nameByIDscene[i][1])
                        at btnZoom
                    
                else:
                    imagebutton:
                        idle galeryImgscene(nameByIDscene[i][0])
                        hover LiveComposite(
                            (1920, 1080),
                            (0, 0), galeryImgscene(nameByIDscene[i][0]),
                            (0, 0), im.Alpha("h.jpg",0.3)
                            )
                        action [ Replay(nameByIDscene[i][1], scope={"pc_name":persistent.pc_name, "pcgender":persistent.pcgender})]
                        sensitive renpy.seen_label(nameByIDscene[i][1])
                        at btnZoom
            else:
                imagebutton:
                    idle im.Alpha("h.jpg",0)
                    at btnZoom
                    
    $ pageImageCount = nameByIDscene
    use changePages
    
#Special images gallery
screen g_special():
    style_prefix "gallery"
    tag menu
    add "mm_anim" at zoomEffect
    default page = 0
    grid 3 3:
        for i in range(page*gridSize,(page+1)*gridSize):
            if i < len(nameByIDSpecial):
                imagebutton:
                    idle galeryImgSpecial(nameByIDSpecial[i][0])
                    hover LiveComposite(
                        (1920, 1080),
                        (0, 0), galeryImgSpecial(nameByIDSpecial[i][0]),
                        (0, 0), im.Alpha("h.jpg",0.3)
                        )
                    action [SetVariable("infotext", nameByIDSpecial[i][1]), Show("g_image_full", my_image=nameByIDSpecial[i][0])]
                    at btnZoom
            else:
                imagebutton:
                    idle im.Alpha("h.jpg",0)
                    at btnZoom
    $ pageImageCount = nameByIDSpecial
    use changePages
    
#full image view
screen g_image_full(my_image):
    style_prefix "special"
    modal True
    add my_image xalign 0.5 yalign 0.5
    if infotext != "":
        imagebutton idle "info_icon.png" hover "" action tt.Action(infotext) hovered tt.Action(infotext) xalign .99 yalign .01
        text "[tt.value!t]" yalign 0.2 xalign 0.5 xsize 0.9
    textbutton _("Return") action [ SetVariable("infotext", ""), Hide("g_image_full") ] xalign 0.5 yalign .99 text_outlines [ (0, "#333", 2, 2) ]
    
#change pages
screen changePages:
    style_prefix "special"
    if len(pageImageCount) > (page+1)*gridSize:
        imagebutton:
            idle "gui/galery_right_idle.png"
            hover "gui/galery_right.png"
            action SetScreenVariable("page", page+1) 
            xpos 1604
            yalign .5 
            yfill True 
            xfill True
    if page > 0:
        imagebutton:
            idle "gui/galery_left_idle.png"
            hover "gui/galery_left.png"
            action SetScreenVariable("page", page-1)
            xalign 0
            yalign .5
            yfill True
    textbutton _("Return") action [ Hide("g_scene_gender"), ShowMenu("gallery")] xalign 0.5 yalign .99 text_outlines [ (0, "#333", 2, 2) ]


style gallery_grid:
    spacing 50
    xpos .5
    ypos .5
    xanchor .5
    yanchor .5
    xmaximum 200
style special_text:
    outlines [ (absolute(3), "#bbb", absolute(1), absolute(1)) ]
style special_button_text:
    size 45
    
style galleryint_vbox is vbox
style galleryint:
    xfill True
    yfill True
style galleryint_vbox:
    xalign .5
    yalign .5
    
style galleryint_text_button:
    yanchor .5
    xalign .5
style galleryint_button is default:
    properties gui.button_properties("choice_button")
style galleryint_button_text is default:
    properties gui.button_text_properties("choice_button")
    
style galleryint_button is button:
    xalign 0.5
style galleryint_button_text is button_text:
    size 60 
    color "#333" 
    hover_color "#ccc"