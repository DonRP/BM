########## Game #########
define nsp = " "
define config.mouse_hide_time = 10
default menuset = set()
# rooms
default pcLocation = ""

# male/female pc variables
default pcgender = "man"
default mrms = _("Mr.")
default heshe = _("he")
default boygirl = _("boy")
default md = _("Daddy")
default ds = _("son")
default himher = _("him")
default pcname = _("John")
default bs = _("brother")
default hisher = _("his")
default bpc =  ""
default pcmd = ""
default save_name = _("male")
default surename = _("Doe")
    
# date & time
default daylyActions = 15
default livingHomeDays = 0
default actionsUsed = 0
default currentDay = 0

default wday = tomorrow.strftime("%A")
default day = tomorrow.strftime("%d.")
default month = tomorrow.strftime("%B")
default dtoday = today.strftime("%A the %d. of %B")


# Variables
default introrachel = True
default storyEvent = False
default SErachelBathroomDay0 = False
default SEsearchforsis = False
default SEgetEFromSchool = False
default SErachelPills1st = False
default SErachelPills2nd = False
default SErachelPills3rd = False
default SEpcDay1Morning = False
default PCJadaName = False
default SEtLeaving1st = False
default SEGetEFromSchool = False
default SEsisBDayPresent = False
default SEAfterEBD = False
default SERachelBRAfterEBD = False
default harem = False
default doonce = False
default doonce2 = False
default visit_e_d6 = False
default visit_work_d6 = False
default visit_cafe_d6 = False
default mob = 0
default jlo = 0
default efe = 5
default hlo = 0
default stl = 0
default SEWork = False
default hnumber = False
default rpills = False
default go_home = False
default jpushed = False
default mend = False
default SEd7walk = False
default followedt = False
default d72esbed = False
#default gallery_special = False
default txtbox = True
default txtboxoff = False
default tc = True
default datemaggy = False
default appsrch = False
default mmom = m
default seenboard = False
default seenebc = False
default gotowork = True
default d9_wakeup = False
default seentd9 = False
default pgirls = False
default of10 = False
default of11 = False
default of12 = False
default d10mshowervisit = False
default lookatkat = False
default lookatkatcount = 0
default d11morning = False
default jass = False
default doporn = False
default ptest = False
default gotomaggy = True
default gotocafe = True
default gotoschool = True
default vhd11 = True
default mabjdeep = False
default malickclit = False

# dayly reset variables
default bathscene1 = 0
default bathscene2 = 0
default bathscene3 = 0
default takeAShower = False
default turnPCOn = False
default workTime = False

#camera pov
default campov = False
default pov1 = "nope.jpg"
default pov2 = "nope.jpg"

#music
default mainbgm = "audio/BMBG.mp3"
default mbgm = False

default edressall = renpy.random.randint(1, 3)
default edress2a3 = renpy.random.randint(2, 3)
default edress1a2 = renpy.random.randint(1, 2)
default edress1a3 = renpy.random.choice([1, 3])

# video anims
image porn_vr4 = Movie(play="anim/porn_vr4_30.webm")
image es_02 = Movie(play="/anim/es02.webm")
image d6jfinsert = Movie(play="anim/d6_jf_insert.webm", loop=False)
image d9jlick1 = Movie(play="anim/d9_jlick2.webm",start_image="jpg/d9_jlick2_00.jpg",image="jpg/d9_jlick2_00.jpg")
image d9jlick2 = Movie(play="anim/d9_jlick.webm",start_image="jpg/d9_jlick_00.jpg",image="jpg/d9_jlick_00.jpg")
image d9jlick3 = Movie(play="anim/d9_jlick3.webm",start_image="jpg/d9_jlick3_00.jpg",image="jpg/d9_jlick3_00.jpg")

image d9jbjlick = Movie(play="anim/d9_j_bjlick.webm",start_image="jpg/d9_j_lick_00.jpg",image="jpg/d9_jbjs_58.jpg", loop=0)
image d9jbj01 = Movie(play="anim/d9_jbj1.webm",start_image="jpg/d9_jbjs_58.jpg",image="jpg/d9_jbjs_58.jpg", loop=-1)

image d9jbj02 = Movie(play="anim/d9_jsuck2.webm",start_image="jpg/d9_jsuck2_00.jpg",image="jpg/d9_jsuck2_00.jpg")
image d9jbj02side = Movie(play="anim/d9_jsuck2_side.webm",start_image="jpg/d9_jsuck2_side_00.jpg",image="jpg/d9_jsuck2_side_00.jpg")
image d9jbj03 = Movie(play="anim/d9_jsuck3.webm",start_image="jpg/d9_jsuck3_15.jpg",image="jpg/d9_jsuck3_15.jpg", loop=7)
image d9jbjcum = Movie(play="anim/d9_jsuck_cum.webm",start_image="jpg/d9_jsuck_cum_015.jpg",image="jpg/d9_jsuck_cum_119.jpg", loop=0)
image d9egrind = Movie(play="anim/d9_egrind_060.webm",start_image="jpg/d9_egrind_060.jpg",image="jpg/d9_egrind_060.jpg")
image d9elick4 = Movie(play="anim/d9_elickloop04.webm",start_image="jpg/d9elick_00.jpg",image="jpg/d9elick_00.jpg")

image d9eride1 = Movie(play="anim/d9_eride01.webm",start_image="jpg/d9_eride01_00.jpg",image="jpg/d9_eride01_00.jpg")
image d9eride2 = Movie(play="anim/d9_eride02.webm",start_image="jpg/d9_eride02_00.jpg",image="jpg/d9_eride02_00.jpg")
image d9eride3 = Movie(play="anim/d9_eride03.webm",start_image="jpg/d9_eride03_00.jpg",image="jpg/d9_eride03_00.jpg")
image d9eride4 = Movie(play="anim/d9_eride04.webm",start_image="jpg/d9_eride04_00.jpg",image="jpg/d9_eride04_00.jpg")
image d10rshower17 = Movie(play="anim/d10rshower17full.webm",start_image="jpg/d10rshowerkiss3_01.jpg",image="jpg/d10rshowerkiss3_89.jpg")

image jfan1 = Movie(play="anim/jfan1_00.webm",start_image="jpg/jfan1_00.jpg",image="jpg/jfan1_00.jpg")
image jfan2 = Movie(play="anim/jfan2_00.webm",start_image="jpg/jfan2_00.jpg",image="jpg/jfan2_00.jpg")

image d10na1m = Movie(play="anim/d10na1m_00.webm",start_image="jpg/d10na1m_00.jpg",image="jpg/d10na1m_00.jpg")
image d10na2m = Movie(play="anim/d10na2m_00.webm",start_image="jpg/d10na2m_00.jpg",image="jpg/d10na2m_00.jpg")
image d10na2m45 = Movie(play="anim/d10na2m_45.webm",start_image="jpg/d10na2m_00.jpg",image="jpg/d10na2m_00.jpg")
image d10na3m = Movie(play="anim/d10na3m_00.webm",start_image="jpg/d10na3m_00.jpg",image="jpg/d10na3m_00.jpg")
image d10night30a = Movie(play="anim/d10night30_00.webm",start_image="jpg/d10night30_00.jpg",image="jpg/d10night30_00.jpg")
image d10night30m = Movie(play="anim/d10night30_m00.webm",start_image="jpg/d10night30_m00.jpg",image="jpg/d10night30_m00.jpg")

image d10nightfjm1 = Movie(play="anim/e&j3somenightlem0_00.webm",start_image="jpg/e&j3somenightlem000.jpg",image="jpg/e&j3somenightlem000.jpg")
image d10night30_2 = Movie(play="anim/e&j3somenightle1_00.webm",start_image="jpg/e&j3somenightle1_00.jpg",image="jpg/e&j3somenightle1_00.jpg")
image d10night30_3 = Movie(play="anim/e&j3somenightle2_00.webm",start_image="jpg/e&j3somenightle2_00.jpg",image="jpg/e&j3somenightle2_00.jpg")
image d10night30_4 = Movie(play="anim/e&j3somenightlj2_00.webm",start_image="jpg/e&j3somenightlj2_00.jpg",image="jpg/e&j3somenightlj2_00.jpg")

image d10nightle1 = Movie(play="anim/e&j3somenight3_00.webm",start_image="jpg/ej3somenight3_00.jpg",image="jpg/ej3somenight3_00.jpg")
image d10nightle2 = Movie(play="anim/e&j3somenight4_00.webm",start_image="jpg/e&j3somenight4_00.jpg",image="jpg/e&j3somenight4_00.jpg")
image d10nightle3 = Movie(play="anim/e&j3somenight5f_00.webm",start_image="jpg/ej3somenight5f_000.jpg",image="jpg/ej3somenight5f_000.jpg")
image d10nightle4 = Movie(play="anim/e&j3somenight6f_000.webm",start_image="jpg/ej3somenight6f_000.jpg",image="jpg/ej3somenight6f_000.jpg")

image d10nightfe2 = Movie(play="anim/e&j3somenight2_00.webm",start_image="jpg/e&j3somenight2_00.jpg",image="jpg/e&j3somenight2_00.jpg")
image d10nightfe3 = Movie(play="anim/e&j3somenight1_00.webm",start_image="jpg/e&j3somenight1_00.jpg",image="jpg/e&j3somenight1_00.jpg")
image d10nightfe4 = Movie(play="anim/e&j3somenight5_00.webm",start_image="jpg/e&j3somenight5_00.jpg",image="jpg/e&j3somenight5_00.jpg")
image d10nightfe5 = Movie(play="anim/e&j3somenight5-2_00.webm",start_image="jpg/e&j3somenight5-2_00.jpg",image="jpg/e&j3somenight5-2_00.jpg")
image d10nightfe6 = Movie(play="anim/e&j3somenight5-3_00.webm",start_image="jpg/e&j3somenight5-3_00.jpg",image="jpg/e&j3somenight5-3_00.jpg")
image d10nightfe7 = Movie(play="anim/e&j3somenight5-3_50.webm",start_image="jpg/e&j3somenight5-3_00.jpg",image="jpg/e&j3somenight5-3_00.jpg")

image d11maggylick = Movie(play="anim/d11maggy60_00.webm",start_image="jpg/d11maggy60.jpg",image="jpg/d11maggy61.jpg")
image d11maggylick2 = Movie(play="anim/d11maggy63_00.webm",start_image="jpg/d11maggy60.jpg",image="jpg/d11maggy61.jpg")
image d11maggyf1 = Movie(play="anim/d11maggy73f1_00.webm",start_image="jpg/d11maggy73f2_00.jpg",image="jpg/d11maggy73f2_00.jpg")
image d11maggyf2 = Movie(play="anim/d11maggy73f2_00.webm",start_image="jpg/d11maggy73f2_00.jpg",image="jpg/d11maggy73f2_00.jpg")
image d11maggyf2-3 = Movie(play="anim/d11maggy73f2to3_00.webm",start_image="jpg/d11maggy73f2_00.jpg",image="jpg/d11maggy73f2_00.jpg")
image d11maggyf3 = Movie(play="anim/d11maggy73f3_00.webm",start_image="jpg/d11maggy73f3_00.jpg",image="jpg/d11maggy73f3_00.jpg")
image d11maggym1 = Movie(play="anim/mabj1_00.webm",start_image="jpg/mabj1_00.jpg",image="jpg/mabj1_00.jpg")
image d11maggym2 = Movie(play="anim/mabj2_00.webm",start_image="jpg/mabj2_00.jpg",image="jpg/mabj2_00.jpg")


# video switch
image brTitties = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/brtitties_fem.webm"),
    "True", Movie(play="anim/brtitties.webm"))
image bjhmovtrd = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/bjhtrd_fem.webm"),
    "True", Movie(play="anim/bjhtrd.webm"))
image bjhmovpov = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/bjh2_fem.webm"),
    "True", Movie(play="anim/bjh2.webm"))
    
image ebj01 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/elj_01.webm"),
    "True", Movie(play="anim/ebj_01.webm"))
image es01 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/es_01_fem.webm"),
    "True", Movie(play="anim/es_01.webm"))
    
image tbj_01 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/tlj1.webm"),
    "True", Movie(play="anim/tbj1.webm"))
image tbj_02 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/tlj2.webm"),
    "True", Movie(play="anim/tbj2.webm"))
    
image jtits = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/j_tits_fem_00.webm"),
    "True", Movie(play="anim/j_tits_00.webm"))
image pcroomd6jfp5 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/pcroom_d6_j_fp5_fem.webm"),
    "True", Movie(play="anim/pcroom_d6_j_fp5.webm"))
    
image d6jl1 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jl1.webm"),
    "True", Movie(play="anim/d6_jbj1.webm"))
image d6jl2 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jl2.webm"),
    "True", Movie(play="anim/d6_jdt2.webm"))
image d6jl3 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jl3.webm"),
    "True", Movie(play="anim/d6_jdt1.webm"))
    
image d6jf1 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jf1_fem.webm"),
    "True", Movie(play="anim/d6_jf1.webm"))
image d6jf2 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jf2_fem.webm"),
    "True", Movie(play="anim/d6_jf2.webm"))
image d6jf3 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jf3_fem.webm"),
    "True", Movie(play="anim/d6_jf4.webm"))
image d6jf4 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jf3_fem_60.webm"),
    "True", Movie(play="anim/d6_jf4_60.webm"))
image d6jf5 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d6_jf2_fem_60.webm"),
    "True", Movie(play="anim/d6_jf2_60.webm"))
    
image jmotelf45 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/jmotelf_fem_45.webm"),
    "True", Movie(play="anim/jmotelf_45.webm"))
image jmotelf = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/jmotelf_fem.webm"),
    "True", Movie(play="anim/jmotelf.webm"))
image jmotelf245 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/jmotelf2_fem_45.webm"),
    "True", Movie(play="anim/jmotelf2_45.webm"))
image jmotelf2 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/jmotelf2_fem.webm"),
    "True", Movie(play="anim/jmotelf2.webm"))
    
image d8jvrekiss = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/ekiss_fem.webm"),
    "True", Movie(play="anim/ekissm_001.webm"))
image d8jvrjkiss = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/jkiss_fem.webm"),
    "True", Movie(play="anim/jkissm_00.webm"))
    
image d9elicksuck = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d9_elickloop03.webm",start_image="jpg/d9_elickloop03_01.jpg",image="jpg/d9_elickloop03_01.jpg"),
    "True", Movie(play="anim/d9_esuckloop.webm",start_image="jpg/d9_esuckloop_00.jpg",image="jpg/d9_esuckloop_00.jpg"))
image d9elicksuck1 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d9_elickloop04.webm",start_image="jpg/d9elick_00.jpg",image="jpg/d9elick_00.jpg"),
    "True", Movie(play="anim/d9_esuckloop1.webm",start_image="jpg/d9_esuckloop1.jpg",image="jpg/d9_esuckloop1.jpg"))
image d9elicksuck2 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d9_elickloop02.webm",start_image="jpg/d9_elickloop02.jpg",image="jpg/d9_elickloop02.jpg"),
    "True", Movie(play="anim/d9_esuckloop2.webm",start_image="jpg/d9_esuckloop2.jpg",image="jpg/d9_esuckloop2.jpg"))
    
image d10nightsx = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d10nightsx_00.webm"),
    "True", Movie(play="anim/d10nightsxm_00.webm"))
image d10nightsx2 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d10nightsx2_00.webm", loop=0),
    "True", Movie(play="anim/d10nightsxm2_00.webm", loop=0))
image d10nightsx3 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d10nightsx3_00.webm"),
    "True", Movie(play="anim/d10nightsxm3_00.webm"))
image d10nightsx4 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d10nightsx4_00.webm",start_image="jpg/d10nightsx4_00.jpg",image="jpg/d10nightsx4_58.jpg", loop=0),
    "True", Movie(play="anim/d10nightsxm4_00.webm",start_image="jpg/d10nightsxm4_00.jpg",image="jpg/d10nightsxm4_58.jpg", loop=0))
image d10nightsx5 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d10nightsx5_00.webm",start_image="jpg/d10nightsx5_00.jpg",image="jpg/d10nightsx5_58.jpg", loop=0),
    "True", Movie(play="anim/d10nightsxm5_00.webm",start_image="jpg/d10nightsxm5_00.jpg",image="jpg/d10nightsxm5_58.jpg", loop=0))
    
image d11jf1 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d11jlick2_00.webm"),
    "True", Movie(play="anim/jfuck1_00.webm"))
image d11jf2 = ConditionSwitch(
    "pcgender == 'woman'", Movie(play="anim/d11jlick1_00.webm"),
    "True", Movie(play="anim/jfuck2_00.webm"))
# Image switch
image pcwalk = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pc walk fem.jpg",
    "True", "/jpg/pc walk.jpg")
image introcabpcdrivehome = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/intro cab pcfem drive home.jpg",
    "True", "/jpg/intro cab pc drive home.jpg")
image hotelroomwakeup = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hotelroom wakeup fem.jpg",
    "True", "/jpg/hotelroom wakeup.jpg")
image hotelroomwakeup2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hotelroom wakeup fem2.jpg",
    "True", "/jpg/hotelroom wakeup2.jpg")
image hotelroomwakeupphone1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hotelroom wakeup phone1 fem.jpg",
    "True", "/jpg/hotelroom wakeup phone1.jpg")
image hotelroomwakeupphone2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hotelroom wakeup phone2 fem.jpg",
    "True", "/jpg/hotelroom wakeup phone2.jpg")
image hotelroomphoneclothed1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hotelroom phone clothedfem1.jpg",
    "True", "/jpg/hotelroom phone clothed1.jpg")
image hotelroomphoneclothed2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hotelroom phone clothedfem2.jpg",
    "True", "/jpg/hotelroom phone clothed2.jpg")
image motelbedroomnight = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/motel bedroom night fem.jpg",
    "True", "/jpg/motel bedroom night.jpg")
image motelbedroomnight2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/motel bedroom night2 fem.jpg",
    "True", "/jpg/motel bedroom night2.jpg")
    
image coffeehouseentrancecup = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/coffeehouse entrance cup fem.jpg",
    "True", "/jpg/coffeehouse entrance cup1.jpg")
image coffeehouseentrancerachel3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/coffeehouse entrance rachel3 fem.jpg",
    "True", "/jpg/coffeehouse entrance rachel3.jpg")
image hallbathroomdoor = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/hall bathroom door fem.jpg",
    "True", "/jpg/hall bathroom door.jpg")
image bathroompcclosesink = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom pcfem close sink.jpg",
    "True", "/jpg/bathroom pc close sink.jpg")
image bathroompcfiddle = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom pcfem fiddle.jpg",
    "True", "/jpg/bathroom pc fiddle.jpg")
image bathroompcwashhands = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom pcfem wash hands.jpg",
    "True", "/jpg/bathroom pc wash hands.jpg")
image bathroompcleave = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom pcfem leave.jpg",
    "True", "/jpg/bathroom pc leave.jpg")
image kitchenfridgeopentake = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kitchen fridge open take fem.jpg",
    "True", "/jpg/kitchen fridge open take.jpg")
image pcroomlaydown = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom laydown fem.jpg",
    "True", "/jpg/pcroom laydown.jpg")
    
image pcroomwakeuprachel1st = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup rachel1st fem.jpg",
    "True", "/jpg/pcroom wakeup rachel1st.jpg")
image pcroomwakeuprachel2nd = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup rachel2nd fem.jpg",
    "True", "/jpg/pcroom wakeup rachel2nd.jpg")
image pcroomwakeupellie1st = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellie1st fem.jpg",
    "True", "/jpg/pcroom wakeup ellie1st.jpg")
image pcroomwakeupfall = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup fall fem.jpg",
    "True", "/jpg/pcroom wakeup fall.jpg")
image pcroomwakeupellielookdownsurprise = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellielookdown surprise fem.jpg",
    "True", "/jpg/pcroom wakeup ellielookdown surprise.jpg")
image pcroomwakeupellielookatrachel = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellie lookatrachel fem.jpg",
    "True", "/jpg/pcroom wakeup ellie lookatrachel.jpg")
image pcroomwakeupellielookdown = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellielookdown fem.jpg",
    "True", "/jpg/pcroom wakeup ellielookdown.jpg")
image pcroomwakeupelliegetup = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellie getup fem.jpg",
    "True", "/jpg/pcroom wakeup ellie getup.jpg")
image pcroomwakeupelliejumpoverpc = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellie jumpoverpc fem.jpg",
    "True", "/jpg/pcroom wakeup ellie jumpoverpc.jpg")
image pcroomwakeupelliejumplanding = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup ellie jumplanding fem.jpg",
    "True", "/jpg/pcroom wakeup ellie jumplanding.jpg")
image pcroomwakeupexposed = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup exposed fem.jpg",
    "True", "/jpg/pcroom wakeup exposed.jpg")
image pcroomwakeupexposedhide = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup exposedhide fem.jpg",
    "True", "/jpg/pcroom wakeup exposedhide.jpg")
image pcroomsitonchair = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair fem.jpg",
    "True", "/jpg/pcroom sitonchair.jpg")
image pcroomsitonchair2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair2 fem.jpg",
    "True", "/jpg/pcroom sitonchair2.jpg")
image pcroomsitonchairtired1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair tired1 fem.jpg",
    "True", "/jpg/pcroom sitonchair tired1.jpg")
image pcroomsitonchairtired2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair tired2 fem.jpg",
    "True", "/jpg/pcroom sitonchair tired2.jpg")
image pcroomsitonchairtired3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair tired3 fem.jpg",
    "True", "/jpg/pcroom sitonchair tired3.jpg")
image pcroomsleeponchairwakeup1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sleeponchair wakeup1 fem.jpg",
    "True", "/jpg/pcroom sleeponchair wakeup1.jpg")
image pcroomsleeponchairwakeup2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sleeponchair wakeup2 fem.jpg",
    "True", "/jpg/pcroom sleeponchair wakeup2.jpg")
image pcroomsleeponchairwakeup3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sleeponchair wakeup3 fem.jpg",
    "True", "/jpg/pcroom sleeponchair wakeup3.jpg")
image pcroomsleeponchairwakeup3_2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sleeponchair wakeup3_2 fem.jpg",
    "True", "/jpg/pcroom sleeponchair wakeup3_2.jpg")
image pcroomday2night1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom day2 night1 fem.jpg",
    "True", "/jpg/pcroom day2 night1.jpg")
image pcroomday2night1_1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom day2 night1_1 fem.jpg",
    "True", "/jpg/pcroom day2 night1_1.jpg")
image pcroomday2night2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom day2 night2 fem.jpg",
    "True", "/jpg/pcroom day2 night2.jpg")
image pcroomday2nightehug = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom day2 night ehug fem.jpg",
    "True", "/jpg/pcroom day2 night ehug.jpg")
image pcroomwakeup = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup fem.jpg",
    "True", "/jpg/pcroom wakeup.jpg")
image pcroomwakeup1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup1 fem.jpg",
    "True", "/jpg/pcroom wakeup1.jpg")
image pcroomwakeuplookfore = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom wakeup lookfore fem.jpg",
    "True", "/jpg/pcroom wakeup lookfore.jpg")
image bedroomrachelpcgrabtits = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bedroom rachel pc grabtits fem.jpg",
    "True", "/jpg/bedroom rachel pc grabtits.jpg")
image pcroomsitonchair2box = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair2 fem_box.jpg",
    "True", "/jpg/pcroom sitonchair2_box.jpg")
image pcroomstuffarrivesunboxing = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom stuffarrives unboxing fem.jpg",
    "True", "/jpg/pcroom stuffarrives unboxing.jpg")
image prcoomellievrgrabhmd = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom ellievr grabhmd fem.jpg",
    "True", "/jpg/pcroom ellievr grabhmd.jpg")
image pcroomellievrpccloselappy = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom ellievr pccloselappy fem.jpg",
    "True", "/jpg/pcroom ellievr pccloselappy.jpg")
image pcroomellievrporn = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom ellievr porn fem.jpg",
    "True", "/jpg/pcroom ellievr porn.jpg")
image pcroomsitonchairehug3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom sitonchair ehug3 fem.jpg",
    "True", "/jpg/pcroom sitonchair ehug3.jpg")
image pcroomlappyf95 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom lappyf95 fem.jpg",
    "True", "/jpg/pcroom lappyf95.jpg")
image pcroomphoneanswer = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom phone answer fem.jpg",
    "True", "/jpg/pcroom phone answer.jpg")
image pcroomphonegetefromschool = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom phone getefromschool fem.jpg",
    "True", "/jpg/pcroom phone getefromschool.jpg")
image pcroomcloselappygete = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom closelappy gete fem.jpg",
    "True", "/jpg/pcroom closelappy gete.jpg")
image pcroomflirtyj1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom flirtyj1_fem.jpg",
    "True", "/jpg/pcroom flirtyj1.jpg")
image pcroomvrfun = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom vrfun fem.jpg",
    "True", "/jpg/pcroom vrfun.jpg")
image pcroomebd_jadavr1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom ebd_jadavr1 fem.jpg",
    "True", "/jpg/pcroom ebd_jadavr1.jpg")
    
image livingroomttvrachelcall1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/livingroom ttv rachelcall1 fem.jpg",
    "True", "/jpg/livingroom ttv rachelcall1.jpg")
image livingroomttvrachelcall2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/livingroom ttv rachelcall2 fem.jpg",
    "True", "/jpg/livingroom ttv rachelcall2.jpg")
    
image bathroomebdt2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd2 fem.jpg",
    "True", "/jpg/bathroom ebd2.jpg")
image bathroomebdtmolest1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest1 fem.jpg",
    "True", "/jpg/bathroom ebd tmolest1.jpg")
image bathroomebdtmolest2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest2 fem.jpg",
    "True", "/jpg/bathroom ebd tmolest2.jpg")
image bathroomebdtmolest3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest3 fem.jpg",
    "True", "/jpg/bathroom ebd tmolest3.jpg")
image bathroomebdtmolestliftskirt = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest liftskirt fem.jpg",
    "True", "/jpg/bathroom ebd tmolest liftskirt.jpg")
image bathroomebdtmolesttouch = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest touch fem.jpg",
    "True", "/jpg/bathroom ebd tmolest touch.jpg")
image bathroomebdtmolestrub = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest rub fem.jpg",
    "True", "/jpg/bathroom ebd tmolest rub.jpg")
image bathroomebdtmolestsqueeze = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest squeeze fem.jpg",
    "True", "/jpg/bathroom ebd tmolest squeeze.jpg")
image bathroomebdtmolestsqueezecum = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bathroom ebd tmolest squeezecum fem.jpg",
    "True", "/jpg/bathroom ebd tmolest squeezecum.jpg")
    
image bringjadahome5 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bringjadahome5 fem.jpg",
    "True", "/jpg/bringjadahome5.jpg")
image bringjadahome6 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bringjadahome6 fem.jpg",
    "True", "/jpg/bringjadahome6.jpg")
image bringjadahome7 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bringjadahome7 fem.jpg",
    "True", "/jpg/bringjadahome7.jpg")
image bjh2_00 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bjh2_fem_00.jpg",
    "True", "/jpg/bjh2_00.jpg")
image bringjadahome6cum = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bringjadahome6 fem.jpg",
    "True", "/jpg/bringjadahome6_cum.jpg")
    
image pcroomafterebd2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom afterebd2_fem.jpg",
    "True", "/jpg/pcroom afterebd2.jpg")
image pcroomafterebd2_2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom afterebd2_2 fem.jpg",
    "True", "/jpg/pcroom afterebd2_2.jpg")
    
image coffeehouse3_9_2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/coffeehouse3_9_2_fem.jpg",
    "True", "/jpg/coffeehouse3_9_2.jpg")
    
image city7ephoto1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/city_7_ephoto1_fem.jpg",
    "True", "/jpg/city_7_ephoto1.jpg")
image city7ephoto2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/city_7_ephoto2_fem.jpg",
    "True", "/jpg/city_7_ephoto2.jpg")
    
image holdingcell_1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/holdingcell1_fem.jpg",
    "True", "/jpg/holdingcell1.jpg")
image holdingcell_5 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/holdingcell5_fem.jpg",
    "True", "/jpg/holdingcell5.jpg")
    
    
image childroomkitty10 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/childroom kitty10 fem.jpg",
    "True", "/jpg/childroom kitty10.jpg")
image childroomkitty11 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/childroom kitty11 fem.jpg",
    "True", "/jpg/childroom kitty11.jpg")
image childroomkitty26 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/childroom kitty26 fem.jpg",
    "True", "/jpg/childroom kitty26.jpg")
image childroomkitty27 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/childroom kitty27 fem.jpg",
    "True", "/jpg/childroom kitty27.jpg")
image childroomkitty28 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/childroom kitty28 fem.jpg",
    "True", "/jpg/childroom kitty28.jpg")
image childroomkitty29 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/childroom kitty29 fem.jpg",
    "True", "/jpg/childroom kitty29.jpg")
    
image pcroomrachelgivepillssingle = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_rachel_givepillssingle_fem.jpg",
    "True", "/jpg/pcroom_rachel_givepillssingle.jpg")
image pcroomrachelgivepillsbottle = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_rachel_givepillsbottle_fem.jpg",
    "True", "/jpg/pcroom_rachel_givepillsbottle.jpg")
image pcroomcodingwork = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_fem.jpg",
    "True", "/jpg/pcroom_codingwork.jpg")
    
image pcroomcodingworkt13 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_t13_fem.jpg",
    "True", "/jpg/pcroom_codingwork_t13.jpg")
image pcroomcodingworkt14_1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_t14_1_fem.jpg",
    "True", "/jpg/pcroom_codingwork_t14_1.jpg")
image pcroomcodingworkt14_3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_t14_3_fem.jpg",
    "True", "/jpg/pcroom_codingwork_t14_3.jpg")
image pcroomcodingworkt15_1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_t15_1_fem.jpg",
    "True", "/jpg/pcroom_codingwork_t15_1.jpg")
image pcroomcodingworkt15_2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_t15_2_fem.jpg",
    "True", "/jpg/pcroom_codingwork_t15_2.jpg")
image pcroomcodingworktcum = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_codingwork_t_cum_fem.jpg",
    "True", "/jpg/pcroom_codingwork_t_cum.jpg")
    
image pcroomaftercodingwork2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_aftercodingwork2_fem.jpg",
    "True", "/jpg/pcroom_aftercodingwork2.jpg")
    
image pcroomaftertcoerced2rachelpills = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_aftertcoerced2_rachelpills_fem.jpg",
    "True", "/jpg/pcroom_aftertcoerced2_rachelpills.jpg")
    
image pcroomafterpornvr4_1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_afterpornvr4_1_fem.jpg",
    "True", "/jpg/pcroom_afterpornvr4_1.jpg")
    
    
image kitchenesearchforfoodkissmc = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kitchen_e_searchforfood_kiss_mc_fem.jpg",
    "True", "/jpg/kitchen_e_searchforfood_kiss_mc.jpg")
image kitcheneeat_mc = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kitchen_e_eat_mc_fem.jpg",
    "True", "/jpg/kitchen_e_eat_mc.jpg")
image kitcheneeat_mc2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kitchen_e_eat_mc2_fem.jpg",
    "True", "/jpg/kitchen_e_eat_mc2.jpg")
image kitcheneeat_mc3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kitchen_e_eat_mc3_fem.jpg",
    "True", "/jpg/kitchen_e_eat_mc3.jpg")
    
    
image pcroomebjfirst = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_fem.jpg",
    "True", "/jpg/pcroom_ebj_first.jpg")
image pcroomebjfirst2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_2_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_2.jpg")
image pcroomebjfirst3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_3_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_3.jpg")
image pcroomebjfirst4 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_4_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_4.jpg")
image pcroomebjfirst5 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_5_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_5.jpg")
image pcroomebjfirst60 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_6_0_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_6_0.jpg")
image pcroomebjfirst6sad = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_sad_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_sad.jpg")
image pcroomebjfirst6sadrun = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_sad_run_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_sad_run.jpg")
image pcroomebjfirst6 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ebj_first_6_fem.jpg",
    "True", "/jpg/pcroom_ebj_first_6.jpg")
    
image ebj000 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/elj_000.jpg",
    "True", "/jpg/ebj_000.jpg")
    
image pcroomehump1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ehump1_fem.jpg",
    "True", "/jpg/pcroom_ehump1.jpg")
image pcroomehump2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ehump2_fem.jpg",
    "True", "/jpg/pcroom_ehump2.jpg")
image pcroomehump3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_ehump3_fem.jpg",
    "True", "/jpg/pcroom_ehump3.jpg")
    
    
image pcroomwakeupd6 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom laydown fem.jpg",
    "True", "/jpg/pcroom_d6_wakeup1.jpg")
    
image pcroom_d6_callh = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_callh1_fem.jpg",
    "True", "/jpg/pcroom_d6_callh1.jpg")
    
image jkiss = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/j_kiss_fem.jpg",
    "True", "/jpg/j_kiss.jpg")
image afterkbf9 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/after_kandbf9_fem.jpg",
    "True", "/jpg/after_kandbf9.jpg")
image afterkbf10 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/after_kandbf10_fem.jpg",
    "True", "/jpg/after_kandbf10.jpg")
    
image bedroom_rpills3_3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bedroom_rpills3_3_fem.jpg",
    "True", "/jpg/bedroom_rpills3_3.jpg")
image bedroom_rpills3_4 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bedroom_rpills3_4_fem.jpg",
    "True", "/jpg/bedroom_rpills3_4.jpg")
image bedroom_rpills3_5 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bedroom_rpills3_5_fem.jpg",
    "True", "/jpg/bedroom_rpills3_5.jpg")
image bedroom_rpills3_5_2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/bedroom_rpills3_5_2_fem.jpg",
    "True", "/jpg/bedroom_rpills3_5_2.jpg")
    
image pcroom_tcoerce3_3_1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_tcoerce3_3_1_fem.jpg",
    "True", "/jpg/pcroom_tcoerce3_3_1.jpg")
image pcroom_tcoerce3_3_2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_tcoerce3_3_2_fem.jpg",
    "True", "/jpg/pcroom_tcoerce3_3_2.jpg")
image tbj1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/tlj1.jpg",
    "True", "/jpg/tbj1.jpg")
image tbj2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/tlj2.jpg",
    "True", "/jpg/tbj2.jpg")
image pcroom_tcoerce3talk = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_tcoerce3_talk_fem.jpg",
    "True", "/jpg/pcroom_tcoerce3_talk.jpg")
image tbj2_15 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/tlj2_25.jpg",
    "True", "/jpg/tbj2_15.jpg")
image tbj2_25 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/tlj2_58.jpg",
    "True", "/jpg/tbj2_25.jpg")
    
image pcroomd6jkiss = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jkiss_fem.jpg",
    "True", "/jpg/pcroom_d6_jkiss.jpg")
image pcroomd6jkiss1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jakiss_1_fem.jpg",
    "True", "/jpg/pcroom_d6_jakiss_1.jpg")
image pcroomd6jkiss2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jakiss_2_fem.jpg",
    "True", "/jpg/pcroom_d6_jakiss_2.jpg")
    
image pcroomd6jkiss5 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jakiss_5_fem.jpg",
    "True", "/jpg/pcroom_d6_jakiss_5.jpg")
image jtits00 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/j_tits_fem_00.jpg",
    "True", "/jpg/j_tits_00.jpg")
image pcroomd6jmc_undress = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_mc_undress_fem.jpg",
    "True", "/jpg/pcroom_d6_j_mc_undress.jpg")
image pcroomd6jmc_undress2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_mc_undress2_fem.jpg",
    "True", "/jpg/pcroom_d6_j_mc_undress2.jpg")
image pcroomd6jmc_undress7 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_mc_undress7_fem.jpg",
    "True", "/jpg/pcroom_d6_j_mc_undress7.jpg")
image pcroomd6jmc_undress8 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_mc_undress8_fem.jpg",
    "True", "/jpg/pcroom_d6_j_mc_undress8.jpg")
    
image pcroomd6j_fp1 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp1_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp1.jpg")
image pcroomd6j_fp2 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp2_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp2.jpg")
image pcroomd6j_fp3 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp3_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp3.jpg")
image pcroomd6j_fp4 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp4_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp4.jpg")
image pcroomd6j_fp5 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp5_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp5.jpg")
image pcroomd6j_fp6 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp6_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp6.jpg")
image pcroomd6j_fp7 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp7_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp7.jpg")
image pcroomd6j_fp8 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp8_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp8.jpg")
image pcroomd6j_fp9 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp9_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp9.jpg")
image pcroomd6j_fp11 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp11_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp11.jpg")
image pcroomd6j_fp12 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp12_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp12.jpg")
image pcroomd6j_fp13 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp13_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp13.jpg")
image pcroomd6j_fp14 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp14_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp14.jpg")
image pcroomd6j_fp16 = ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_j_fp16_fem.jpg",
    "True", "/jpg/pcroom_d6_j_fp16.jpg")
    
image d6_jbj1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d6_jl_00.jpg",
    "True", "/jpg/d6_jbj_00.jpg")
image d6_jf1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d6_jf4_60_fem.jpg",
    "True", "/jpg/d6_jf100.jpg")
image d6_jf2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d6_jf4_2_fem.jpg",
    "True", "/jpg/d6jf_2.jpg")
    
image pcroomd6jfuckend1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jfuckend1_fem.jpg",
    "True", "/jpg/pcroom_d6_jfuckend1.jpg")
image pcroomd6jfuckend1_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jfuckend1_2_fem.jpg",
    "True", "/jpg/pcroom_d6_jfuckend1_2.jpg")
image pcroomd6jfuckend2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d6_jfuckend2_fem.jpg",
    "True", "/jpg/pcroom_d6_jfuckend1_3.jpg")
    
image pcroomd7wakeup_j1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j1_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j1.jpg")
image pcroomd7wakeup_j2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j2_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j2.jpg")
image pcroomd7wakeup_j3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j3_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j3.jpg")
image pcroomd7wakeup_j7= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j7_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j7.jpg")
image pcroomd7wakeup_j9= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j9_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j9.jpg")
image pcroomd7wakeup_j9_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j9_2_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j9_2.jpg")
image pcroom_d7_wakeup_j15= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/pcroom_d7_wakeup_j15_fem.jpg",
    "True", "/jpg/pcroom_d7_wakeup_j15.jpg")
    
image d7_city_pg32= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_city_pg32_fem.jpg",
    "True", "/jpg/d7_city_pg32.jpg")
image d7_city_pg34= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_city_pg34_fem.jpg",
    "True", "/jpg/d7_city_pg34.jpg")
    
image d7_pcroomkitty4= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_pcroom_kitty4_fem.jpg",
    "True", "/jpg/d7_pcroom_kitty4.jpg")
image d7_pcroomkitty3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_pcroom_kitty3_fem.jpg",
    "True", "/jpg/d7_pcroom_kitty3.jpg")
image d7pcroomkitty18_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_pcroom_kitty18_2_fem.jpg",
    "True", "/jpg/d7_pcroom_kitty18_2.jpg")
    
image d8jcall1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d8_jcall1_fem.jpg",
    "True", "/jpg/d8_jcall1.jpg")
image d8jcall2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d8_jcall2_fem.jpg",
    "True", "/jpg/d8_jcall2.jpg")
image d8jcall3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d8_jcall3_fem.jpg",
    "True", "/jpg/d8_jcall3.jpg")
    
image jmotelf200= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/jmotelf_fem_00.jpg",
    "True", "/jpg/jmotelf_00.jpg")
    
image d7motelfend= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_motel_fendcum_fem.jpg",
    "True", "/jpg/d7_motel_fend.jpg")
image d7motelfend2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d7_motel_fend_fem.jpg",
    "True", "/jpg/d7_motel_fendcum1.jpg")
    
image ekiss_00= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/ekiss_fem_00.jpg",
    "True", "/jpg/ekissm_00.jpg")
image jkiss_00= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/jkiss_fem_00.jpg",
    "True", "/jpg/jkissm_00.jpg")
    
image d9morningbr01= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_morning_br01_fem.jpg",
    "True", "/jpg/d9_morning_br01.jpg")
image d9morningbr10= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_morning_br10_fem.jpg",
    "True", "/jpg/d9_morning_br10.jpg")
    
image d9pcroomwork2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_work2_fem.jpg",
    "True", "/jpg/d9_pcroom_work2.jpg")
image d9pcroomwork3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_work3_fem.jpg",
    "True", "/jpg/d9_pcroom_work3.jpg")
image d9pcroomwork4= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_work4_fem.jpg",
    "True", "/jpg/d9_pcroom_work4.jpg")
image d9pcroomwork23= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_work2_3_fem.jpg",
    "True", "/jpg/d9_pcroom_work2_3.jpg")
    
image d9job12= ConditionSwitch(
    "stl == '0'", "/jpg/d9_job12_2.jpg",
    "True", "/jpg/d9_job12.jpg")
image d9job13= ConditionSwitch(
    "stl == '0'", "/jpg/d9_job13_2.jpg",
    "True", "/jpg/d9_job13.jpg")
image d9job15= ConditionSwitch(
    "stl == '0'", "/jpg/d9_job15_2.jpg",
    "True", "/jpg/d9_job15.jpg")
image d9job16= ConditionSwitch(
    "stl == '0'", "/jpg/d9_job16_2.jpg",
    "True", "/jpg/d9_job16.jpg")
image d9job17= ConditionSwitch(
    "stl == '0'", "/jpg/d9_job17_2.jpg",
    "True", "/jpg/d9_job17.jpg")
    
image d9tcoffee05= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee05_fem.jpg",
    "True", "/jpg/d9_tcoffee05.jpg")
image d9tcoffee12= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee12_fem.jpg",
    "True", "/jpg/d9_tcoffee12.jpg")
image d9tcoffee14= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee14_fem.jpg",
    "True", "/jpg/d9_tcoffee14.jpg")
image d9tcoffee27= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee27_fem.jpg",
    "True", "/jpg/d9_tcoffee27.jpg")
image d9tcoffee28= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee28_fem.jpg",
    "True", "/jpg/d9_tcoffee28.jpg")
image d9tcoffee29= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee29_fem.jpg",
    "True", "/jpg/d9_tcoffee29.jpg")
image d9tcoffee30= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee30_fem.jpg",
    "True", "/jpg/d9_tcoffee30.jpg")
image d9tcoffee31= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee31_fem.jpg",
    "True", "/jpg/d9_tcoffee31.jpg")
image d9tcoffee32= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee32_fem.jpg",
    "True", "/jpg/d9_tcoffee32.jpg")
image d9tcoffee33= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee33_fem.jpg",
    "True", "/jpg/d9_tcoffee33.jpg")
image d9tcoffee34= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee34_fem.jpg",
    "True", "/jpg/d9_tcoffee34.jpg")
image d9tcoffee38= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee38_fem.jpg",
    "True", "/jpg/d9_tcoffee38.jpg")
image d9tcoffee41= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_tcoffee41_fem.jpg",
    "True", "/jpg/d9_tcoffee41.jpg")
    
image d9backhome8= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_backhome8_fem.jpg",
    "True", "/jpg/d9_backhome8.jpg")
    
image d9pcroombackhome= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_backhome_fem.jpg",
    "True", "/jpg/d9_pcroom_backhome.jpg")
    
image d9_jlick= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_jlick00.jpg",
    "True", "/jpg/d9_jsuck00.jpg")
image d9jbathroom13= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_j_bathroom13_fem.jpg",
    "True", "/jpg/d9_j_bathroom13.jpg")
image d9jbathroom_flush= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_j_bathroom_flush_fem.jpg",
    "True", "/jpg/d9_j_bathroom_flush.jpg")
    
image d9pcroombackhomee03= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_backhome_e03_fem.jpg",
    "True", "/jpg/d9_pcroom_backhome_e03.jpg")
image d9pcroombackhomee04= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_backhome_e04_fem.jpg",
    "True", "/jpg/d9_pcroom_backhome_e04.jpg")
image d9pcroombackhomee09= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_backhome_e09_fem.jpg",
    "True", "/jpg/d9_pcroom_backhome_e09.jpg")
image d9pcroombackhomee12= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_backhome_e12_fem.jpg",
    "True", "/jpg/d9_pcroom_backhome_e12.jpg")
image d9pcroombackhomee26= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_pcroom_backhome_e26.jpg",
    "True", "/jpg/d9_esuckloop_00.jpg")
    
image d9eend1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_elick_end.jpg",
    "True", "/jpg/d9_eride_end.jpg")
image d9eend2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_elick_end2.jpg",
    "True", "/jpg/d9_eride_end2.jpg")
image d9eend3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_elick_end3.jpg",
    "True", "/jpg/d9_eride_end3.jpg")
    
image d9end01= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_end01_fem.jpg",
    "True", "/jpg/d9_end01.jpg")
image d9end04= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_end04_fem.jpg",
    "True", "/jpg/d9_end04.jpg")
image d9end10= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d9_end10_fem.jpg",
    "True", "/jpg/d9_end10.jpg")
    
image d10shower01= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10shower01.jpg",
    "True", "/jpg/d10shower01_m.jpg")
image d10shower02= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10shower02.jpg",
    "True", "/jpg/d10shower02_m.jpg")
image d10shower03= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10shower03.jpg",
    "True", "/jpg/d10shower03_m.jpg")
image d10shower04= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10shower04.jpg",
    "True", "/jpg/d10shower04_m.jpg")
    
image d10outdoor20= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10outdoor20_f.jpg",
    "True", "/jpg/d10outdoor20.jpg")
image d10outdoor21= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10outdoor21.jpg",
    "True", "/jpg/d10outdoor21_m.jpg")
image d10outdoor25= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10outdoor25_f.jpg",
    "True", "/jpg/d10outdoor25.jpg")
image d10outdoor49= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10outdoor49.jpg",
    "True", "/jpg/d10outdoor49_m.jpg")
    
image d10eshow16= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10eshow16_f.jpg",
    "True", "/jpg/d10eshow16.jpg")
    
image d10rshower07= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower07.jpg",
    "True", "/jpg/d10rshower07_m.jpg")
image d10rshower09_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower09_2.jpg",
    "True", "/jpg/d10rshower09_2_m.jpg")
image d10rshower12= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower12_f.jpg",
    "True", "/jpg/d10rshower12.jpg")
image d10rshower13= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower13_f.jpg",
    "True", "/jpg/d10rshower13.jpg")
image d10rshower14= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower14.jpg",
    "True", "/jpg/d10rshower14_m.jpg")
image d10rshower14_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower14_2.jpg",
    "True", "/jpg/d10rshower14_2_m.jpg")
image d10rshower15= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower15_f.jpg",
    "True", "/jpg/d10rshower15.jpg")
image d10rshower18= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower18.jpg",
    "True", "/jpg/d10rshower18_m.jpg")
image d10rshower19= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower19.jpg",
    "True", "/jpg/d10rshower19_m.jpg")
image d10rshower20= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower20.jpg",
    "True", "/jpg/d10rshower20_m.jpg")
image d10rshower21= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower21_f.jpg",
    "True", "/jpg/d10rshower21.jpg")
image d10rshower22= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower22_f.jpg",
    "True", "/jpg/d10rshower22.jpg")
image d10rshower23= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower23_f.jpg",
    "True", "/jpg/d10rshower23.jpg")
image d10rshower25= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower25_f.jpg",
    "True", "/jpg/d10rshower25.jpg")
image d10rshower25_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower25_2.jpg",
    "True", "/jpg/d10rshower25_2_m.jpg")
image d10rshower26= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower26_f.jpg",
    "True", "/jpg/d10rshower26.jpg")
image d10rshower27= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10rshower27.jpg",
    "True", "/jpg/d10rshower27_m.jpg")
    
image d10pcroom05= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10pcroom05_f.jpg",
    "True", "/jpg/d10pcroom05.jpg")
image d10pcroom06= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10pcroom06_f.jpg",
    "True", "/jpg/d10pcroom06.jpg")
image d10pcroom19= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10pcroom19.jpg",
    "True", "/jpg/d10pcroom19_m.jpg")
    
image d10hannacalls01= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10hannacalls01_f.jpg",
    "True", "/jpg/d10hannacalls01.jpg")
image d10hannacalls02= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10hannacalls02_f.jpg",
    "True", "/jpg/d10hannacalls02.jpg")
    
image kathouse27= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse27_fem.jpg",
    "True", "/jpg/kathouse27.jpg")
image kathouse33= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse33.jpg",
    "True", "/jpg/kathouse33_m.jpg")
image kathouse34= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse34.jpg",
    "True", "/jpg/kathouse34_m.jpg")
image kathouse34_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse34_2.jpg",
    "True", "/jpg/kathouse34_m2.jpg")
image kathouse49= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse49.jpg",
    "True", "/jpg/kathouse49_m.jpg")
image kathouse50= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse50.jpg",
    "True", "/jpg/kathouse50_m.jpg")
image kathouse51= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse51.jpg",
    "True", "/jpg/kathouse51_m.jpg")
image kathouse52= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse52.jpg",
    "True", "/jpg/kathouse52_m.jpg")
image kathouse50_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse50_.jpg",
    "True", "/jpg/kathouse50_m_.jpg")
image kathouse51_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse51_.jpg",
    "True", "/jpg/kathouse51_m_.jpg")
image kathouse52_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse52_.jpg",
    "True", "/jpg/kathouse52_m_.jpg")
image kathouse53= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse53.jpg",
    "True", "/jpg/kathouse53_m.jpg")
image kathouse54= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse54.jpg",
    "True", "/jpg/kathouse54_m.jpg")
image kathouse55= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse55.jpg",
    "True", "/jpg/kathouse55_m.jpg")
image kathouse56= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse56.jpg",
    "True", "/jpg/kathouse56_m.jpg")
image kathouse57= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse57.jpg",
    "True", "/jpg/kathouse57_m.jpg")
image kathouse58= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse58.jpg",
    "True", "/jpg/kathouse58_m.jpg")
image kathouse59= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse59.jpg",
    "True", "/jpg/kathouse59_m.jpg")
image kathouse60= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse60.jpg",
    "True", "/jpg/kathouse60_m.jpg")
image kathouse61= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse61.jpg",
    "True", "/jpg/kathouse61_m.jpg")
image kathouse61_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse61_2.jpg",
    "True", "/jpg/kathouse61_2_m.jpg")
image kathouse61_3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse61_3.jpg",
    "True", "/jpg/kathouse61_3_m.jpg")
image kathouse62= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse62.jpg",
    "True", "/jpg/kathouse62_m.jpg")
image kathouse63= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse63.jpg",
    "True", "/jpg/kathouse63_m.jpg")
image kathouse64= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse64.jpg",
    "True", "/jpg/kathouse64_m.jpg")
image kathouse65= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse65.jpg",
    "True", "/jpg/kathouse65_m.jpg")
image kathouse77= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse77_f.jpg",
    "True", "/jpg/kathouse77.jpg")
image kathouse78= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse78_f.jpg",
    "True", "/jpg/kathouse78.jpg")
image kathouse78_2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse78_2_f.jpg",
    "True", "/jpg/kathouse78_2.jpg")
image kathouse80= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse80_f.jpg",
    "True", "/jpg/kathouse80.jpg")
image kathouse82= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse82.jpg",
    "True", "/jpg/kathouse82_m.jpg")
image kathouse83= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/kathouse83.jpg",
    "True", "/jpg/kathouse83_m.jpg")
    
image d10beforedate1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10beforedate1_f.jpg",
    "True", "/jpg/d10beforedate1.jpg")
image d10beforedate2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10beforedate2_f.jpg",
    "True", "/jpg/d10beforedate2.jpg")
image d10beforedate3= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10beforedate3_f.jpg",
    "True", "/jpg/d10beforedate3.jpg")
image d10beforedate4= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10beforedate4_f.jpg",
    "True", "/jpg/d10beforedate4.jpg")
    
image d10date39= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date39.jpg",
    "True", "/jpg/d10date39_m.jpg")
image d10date46= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date46.jpg",
    "True", "/jpg/d10date46_m.jpg")
image d10date72= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date72.jpg",
    "True", "/jpg/d10date72_m.jpg")
image d10date73= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date73.jpg",
    "True", "/jpg/d10date73_m.jpg")
image d10date75= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date75.jpg",
    "True", "/jpg/d10date75_m.jpg")
image d10date76= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date76.jpg",
    "True", "/jpg/d10date76_m.jpg")
image d10date81= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date81.jpg",
    "True", "/jpg/d10date81_m.jpg")
image d10date82= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date82.jpg",
    "True", "/jpg/d10date82_m.jpg")
image d10date84= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10date84.jpg",
    "True", "/jpg/d10date84_m.jpg")
    
image d10datehhome01= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10datehhome01.jpg",
    "True", "/jpg/d10datehhome01_m.jpg")
image d10datehhome02= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10datehhome02.jpg",
    "True", "/jpg/d10datehhome02_m.jpg")
image d10datehhome03= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10datehhome03.jpg",
    "True", "/jpg/d10datehhome03_m.jpg")
    
image d10ahd02= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd02_1.jpg",
    "of10 == 2", "/jpg/d10ahd02_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd02_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd02_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd02_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd02_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd02_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd02_[edressall].jpg",
    "True", "/jpg/d10ahd02.jpg")
image d10ahd06= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd06_1.jpg",
    "of10 == 2", "/jpg/d10ahd06_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd06_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd06_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd06_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd06_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd06_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd06_[edressall].jpg",
    "True", "/jpg/d10ahd06.jpg")
image d10ahd19= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd19_1.jpg",
    "of10 == 2", "/jpg/d10ahd19_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd19_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd19_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd19_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd19_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd19_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd19_[edressall].jpg",
    "True", "/jpg/d10ahd19.jpg")
image d10ahd20= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd20_1.jpg",
    "of10 == 2", "/jpg/d10ahd20_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd20_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd20_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd20_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd20_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd20_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd20_[edressall].jpg",
    "True", "/jpg/d10ahd20.jpg")
image d10ahd21= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd21_1.jpg",
    "of10 == 2", "/jpg/d10ahd21_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd21_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd21_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd21_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd21_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd21_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd21_[edressall].jpg",
    "True", "/jpg/d10ahd21.jpg")
image d10ahd23= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd23_1.jpg",
    "of10 == 2", "/jpg/d10ahd23_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd23_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd23_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd23_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd23_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd23_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd23_[edressall].jpg",
    "True", "/jpg/d10ahd23.jpg")
image d10ahd29= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd29_1.jpg",
    "of10 == 2", "/jpg/d10ahd29_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd29_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd29_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd29_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd29_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd29_[edress2a3].jpg",
    "of10  and of11 and of12", "/jpg/d10ahd29_[edressall].jpg",
    "True", "/jpg/d10ahd29.jpg")
image d10ahd30= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd30_1.jpg",
    "of10 == 2", "/jpg/d10ahd30_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd30_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd30_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd30_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd30_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd30_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd30_[edressall].jpg",
    "True", "/jpg/d10ahd30.jpg")
image d10ahd32= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd32_1.jpg",
    "of10 == 2", "/jpg/d10ahd32_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd32_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd32_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd32_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd32_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd32_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd32_[edressall].jpg",
    "True", "/jpg/d10ahd32.jpg")
image d10ahd33= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd33_1.jpg",
    "of10 == 2", "/jpg/d10ahd33_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd33_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd33_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd33_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd33_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd33_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd33_[edressall].jpg",
    "True", "/jpg/d10ahd33.jpg")
image d10ahd34= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd34_1.jpg",
    "of10 == 2", "/jpg/d10ahd34_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd34_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd34_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd34_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd34_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd34_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd34_[edressall].jpg",
    "True", "/jpg/d10ahd34.jpg")
image d10ahd36= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd36_1.jpg",
    "of10 == 2", "/jpg/d10ahd36_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd36_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd36_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd36_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd36_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd36_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd36_[edressall].jpg",
    "True", "/jpg/d10ahd36.jpg")
image d10ahd37= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd37_1.jpg",
    "of10 == 2", "/jpg/d10ahd37_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd37_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd37_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd37_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd37_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd37_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd37_[edressall].jpg",
    "True", "/jpg/d10ahd37.jpg")
image d10ahd38= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd38_1.jpg",
    "of10 == 2", "/jpg/d10ahd38_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd38_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd38_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd38_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd38_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd38_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd38_[edressall].jpg",
    "True", "/jpg/d10ahd38.jpg")
image d10ahd39= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd39_1.jpg",
    "of10 == 2", "/jpg/d10ahd39_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd39_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd39_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd39_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd39_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd39_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd39_[edressall].jpg",
    "True", "/jpg/d10ahd39.jpg")
image d10ahd40= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd40_1.jpg",
    "of10 == 2", "/jpg/d10ahd40_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd40_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd40_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd40_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd40_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd40_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd40_[edressall].jpg",
    "True", "/jpg/d10ahd40.jpg")
image d10ahd41= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd41_1.jpg",
    "of10 == 2", "/jpg/d10ahd41_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd41_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd41_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd41_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd41_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd41_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd41_[edressall].jpg",
    "True", "/jpg/d10ahd41.jpg")
image d10ahd42= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd42_1.jpg",
    "of10 == 2", "/jpg/d10ahd42_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd42_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd42_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd42_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd42_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd42_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd42_[edressall].jpg",
    "True", "/jpg/d10ahd42.jpg")
image d10ahd40_x= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd40_x_1.jpg",
    "of10 == 2", "/jpg/d10ahd40_x_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd40_x_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd40_x_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd40_x_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd40_x_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd40_x_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd40_x_[edressall].jpg",
    "True", "/jpg/d10ahd40_x.jpg")
image d10ahd44= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd44_1.jpg",
    "of10 == 2", "/jpg/d10ahd44_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd44_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd44_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd44_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd44_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd44_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd44_[edressall].jpg",
    "True", "/jpg/d10ahd44.jpg")
image d10ahd51= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd51_1.jpg",
    "of10 == 2", "/jpg/d10ahd51_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd51_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd51_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd51_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd51_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd51_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd51_[edressall].jpg",
    "True", "/jpg/d10ahd51.jpg")
image d10ahd53= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd53_1.jpg",
    "of10 == 2", "/jpg/d10ahd53_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd53_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd53_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd53_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd53_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd53_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd53_[edressall].jpg",
    "True", "/jpg/d10ahd53.jpg")
image d10ahd54= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd54_1.jpg",
    "of10 == 2", "/jpg/d10ahd54_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd54_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd54_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd54_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd54_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd54_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd54_[edressall].jpg",
    "True", "/jpg/d10ahd54.jpg")
image d10ahd55= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd55_1.jpg",
    "of10 == 2", "/jpg/d10ahd55_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd55_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd55_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd55_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd55_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd55_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd55_[edressall].jpg",
    "True", "/jpg/d10ahd55.jpg")
image d10ahd56= ConditionSwitch(
    "of10 and not of11 and not of12", "/jpg/d10ahd56_1.jpg",
    "of10 == 2", "/jpg/d10ahd56_1.jpg",
    "of11 and not of10 and not of12", "/jpg/d10ahd56_2.jpg",
    "of12 and not of11 and not of10", "/jpg/d10ahd56_3.jpg",
    "of10 and of11 and not of12", "/jpg/d10ahd56_[edress1a2].jpg",
    "of10 and not of11 and of12", "/jpg/d10ahd56_[edress1a3].jpg",
    "of11 and not of10 and of12", "/jpg/d10ahd56_[edress2a3].jpg",
    "of10 and of11 and of12", "/jpg/d10ahd56_[edressall].jpg",
    "True", "/jpg/d10ahd56.jpg")
    
image d10night02= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night02.jpg",
    "True", "/jpg/d10night02_m.jpg")
image d10night03= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night03.jpg",
    "True", "/jpg/d10night03_m.jpg")
image d10night04= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night04.jpg",
    "True", "/jpg/d10night04_m.jpg")
image d10night08= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night08.jpg",
    "True", "/jpg/d10night08_m.jpg")
image d10night09= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night09.jpg",
    "True", "/jpg/d10night09_m.jpg")
image d10night11= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night11.jpg",
    "True", "/jpg/d10night11_m.jpg")
image d10night12= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night12.jpg",
    "True", "/jpg/d10night12_m.jpg")
image d10night13= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night13.jpg",
    "True", "/jpg/d10night13_m.jpg")
image d10night14= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night14.jpg",
    "True", "/jpg/d10night14_m.jpg")
image d10night15= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night15.jpg",
    "True", "/jpg/d10night15_m.jpg")
image d10night16= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night16.jpg",
    "True", "/jpg/d10night16_m.jpg")
image d10night17= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night17.jpg",
    "True", "/jpg/d10night17_m.jpg")
image d10night18= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night18.jpg",
    "True", "/jpg/d10night18_m.jpg")
image d10night19= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night19.jpg",
    "True", "/jpg/d10night19_m.jpg")
image d10night19_1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d10night19_1.jpg",
    "True", "/jpg/d10night19_m_1.jpg")
    
image d11fjcum= ConditionSwitch(
    "jass and campov", "jpg/jfan2_29.jpg",
    "jass and not campov", "jpg/jfan1_29.jpg",
    "campov and not jass", "jpg/jfuck2_29.jpg",
    "True", "/jpg/jfuck1_29.jpg")
image d11jcum1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11beforelffa_cum3.jpg",
    "jass == True", "jpg/d11beforelmf02cum1.jpg",
    "True", "/jpg/d11beforelmf01cum1.jpg")
image d11jcum2= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11beforelffa_cum4.jpg",
    "jass == True", "jpg/d11beforelmf02cum2.jpg",
    "True", "/jpg/d11beforelmf01cum2.jpg")
image d11beforelffa= ConditionSwitch(
    "campov == True", "/jpg/d11beforelffa_cum1.jpg",
    "True", "/jpg/d11beforelffa_cum2.jpg")
    
image d11backhomej07= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11backhomej07.jpg",
    "True", "/jpg/d11backhomej07_m.jpg")
    
image d11work06= ConditionSwitch(
    "stl > 1", "/jpg/d11work06.jpg",
    "True", "/jpg/d11work06_1.jpg")
image d11work07= ConditionSwitch(
    "stl > 1", "/jpg/d11work07.jpg",
    "True", "/jpg/d11work07_1.jpg")
image d11work08= ConditionSwitch(
    "stl > 1", "/jpg/d11work08.jpg",
    "True", "/jpg/d11work08_1.jpg")
image d11work09= ConditionSwitch(
    "stl > 1", "/jpg/d11work09.jpg",
    "True", "/jpg/d11work09_1.jpg")
    
image d11work11= ConditionSwitch(
    "stl > 1", "/jpg/d11work11.jpg",
    "True", "/jpg/d11work11_1.jpg")
image d11work12= ConditionSwitch(
    "stl > 1", "/jpg/d11work12.jpg",
    "True", "/jpg/d11work12_1.jpg")
image d11work13= ConditionSwitch(
    "stl > 1", "/jpg/d11work13.jpg",
    "True", "/jpg/d11work13_1.jpg")
image d11work14= ConditionSwitch(
    "stl > 1", "/jpg/d11work14.jpg",
    "True", "/jpg/d11work14_1.jpg")
image d11work15= ConditionSwitch(
    "stl > 1", "/jpg/d11work15.jpg",
    "True", "/jpg/d11work15_1.jpg")
image d11work16= ConditionSwitch(
    "stl > 1", "/jpg/d11work16.jpg",
    "True", "/jpg/d11work16_1.jpg")
image d11work17= ConditionSwitch(
    "stl > 1", "/jpg/d11work17.jpg",
    "True", "/jpg/d11work17_1.jpg")
image d11work18= ConditionSwitch(
    "stl > 1", "/jpg/d11work18.jpg",
    "True", "/jpg/d11work18_1.jpg")
image d11work19= ConditionSwitch(
    "stl > 1", "/jpg/d11work19.jpg",
    "True", "/jpg/d11work19_1.jpg")
image d11work20= ConditionSwitch(
    "stl > 1", "/jpg/d11work20.jpg",
    "True", "/jpg/d11work20_1.jpg")
image d11work21= ConditionSwitch(
    "stl > 1", "/jpg/d11work21.jpg",
    "True", "/jpg/d11work21_1.jpg")
image d11work22= ConditionSwitch(
    "stl > 1", "/jpg/d11work22.jpg",
    "True", "/jpg/d11work22_1.jpg")
image d11work23= ConditionSwitch(
    "stl > 1", "/jpg/d11work23.jpg",
    "True", "/jpg/d11work23_1.jpg")
image d11work24= ConditionSwitch(
    "stl > 1", "/jpg/d11work24.jpg",
    "True", "/jpg/d11work24_1.jpg")
image d11work25= ConditionSwitch(
    "stl > 1", "/jpg/d11work25.jpg",
    "True", "/jpg/d11work25_1.jpg")
image d11work26= ConditionSwitch(
    "stl > 1", "/jpg/d11work26.jpg",
    "True", "/jpg/d11work26_1.jpg")
    
image d11work45= ConditionSwitch(
    "stl > 1", "/jpg/d11work45.jpg",
    "True", "/jpg/d11work45_1.jpg")
image d11work46= ConditionSwitch(
    "stl > 1", "/jpg/d11work46.jpg",
    "True", "/jpg/d11work46_1.jpg")
image d11work47= ConditionSwitch(
    "stl > 1", "/jpg/d11work47.jpg",
    "True", "/jpg/d11work47_1.jpg")
image d11work48= ConditionSwitch(
    "stl > 1", "/jpg/d11work48.jpg",
    "True", "/jpg/d11work48_1.jpg")
    
image d11maggy37= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy37_f.jpg",
    "True", "/jpg/d11maggy37.jpg")
image d11maggy41= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy41.jpg",
    "True", "/jpg/d11maggy41_m.jpg")
image d11maggy42= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy42.jpg",
    "True", "/jpg/d11maggy42_m.jpg")
image d11maggy48= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy48.jpg",
    "True", "/jpg/d11maggy48_m.jpg")
image d11maggy48_1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy48_1.jpg",
    "True", "/jpg/d11maggy48_m_1.jpg")
image d11maggybt:
    "d11maggy48" with dissolve
    pause 1
    "d11maggy48_1" with dissolve
    pause 1
    repeat
image d11maggy49= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy49.jpg",
    "True", "/jpg/d11maggy49_m.jpg")
image d11maggy49_1= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy49_1.jpg",
    "True", "/jpg/d11maggy49_m_1.jpg")
image d11maggybt2:
    "d11maggy49" with dissolve
    pause 1
    "d11maggy49_1" with dissolve
    pause 1
    repeat
image d11maggy50= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy50.jpg",
    "True", "/jpg/d11maggy50_m.jpg")
image d11maggy51= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy51.jpg",
    "True", "/jpg/d11maggy51_m.jpg")
image d11maggy68= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy68.jpg",
    "True", "/jpg/d11maggy68_m.jpg")
image d11maggy69= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy69.jpg",
    "True", "/jpg/d11maggy69_m.jpg")
image d11maggy70= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy70.jpg",
    "True", "/jpg/d11maggy70_m.jpg")
image d11maggy71= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy71.jpg",
    "True", "/jpg/d11maggy71_m.jpg")
image d11maggy72= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11maggy72.jpg",
    "True", "/jpg/d11maggy72_m.jpg")
    
image d11bhpcroom01= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11bhpcroom01_f.jpg",
    "True", "/jpg/d11bhpcroom01.jpg")
image d11bhpcroom02= ConditionSwitch(
    "pcgender == 'woman'", "/jpg/d11bhpcroom02_f.jpg",
    "True", "/jpg/d11bhpcroom02.jpg")
    
label dateTime:

    $ daylyActions = daylyActions-actionsUsed
    if daylyActions > 14 or daylyActions < 8:
        $ workTime = False
    else:
        $ workTime = True
    if daylyActions <= 0:
        $ bathscene1 = 0
        $ bathscene2 = 0
        $ bathscene3 = 0
        $ takeAShower = False
        $ turnPCOn = False
        $ workTime = False
        $ livingHomeDays += 1
        $ daylyActions = 15
        $ gotomaggy = True
        $ gotocafe = True
        $ gotoschool = True
        $ gotowork = True
        $ currentDay = "Day " + str(livingHomeDays)
        scene black with fade
        n "[currentDay]"
        window hide
        pause 2
        jump pcroom
    else:
        return

label whatToDoHome:
    if storyEvent == False:
        menu:
            q "What do you want to do?"
            "Take a nap":
                if currentDay == 0:
                    pcthink "I guess I could use a bit more sleep. There's nothing to do anyway until my stuff arrives..."
                    jump pcDream1
                $ actionsUsed = 3
                scene black with dissolve
                call dateTime from _call_dateTime
            "Look for [e]" if workTime == False:
                pass
            "Look for [m]" if workTime == False:
                pass
            "Turn the pc on" if currentDay >= 3 and turnPCOn == False:
                $ turnPCOn = True
                $ actionsUsed = 5
                call dateTime from _call_dateTime_2
            "Leave" if currentDay > 0:
                scene home_hall_idle with dissolve
                call screen map_home_hall
            "Look around" if currentDay == 0:
                scene home_hall_idle with dissolve
                call screen map_home_hall 
            
        n "Later" with dissolve
        window hide
        pause 2


####### Hall ########

label hall:
    $ pcLocation = "h_hall"
    
    if SErachelBathroomDay0 == True:
        scene home_hall_idle with dissolve
        pcthink "Okay, the bathroom should be the last room on the left if I remember correctly..."
    scene home_hall_idle with dissolve
    call screen map_home_hall

####### Livingroom ########

label livingroom:
    $ pcLocation = "h_livingroom"
    
    $ randomLivingroomScene = renpy.random.randint(1, 10)
    if randomLivingroomScene == 1 and storyEvent == False and workTime == False:
        scene livingroom rachel couch1 with dissolve
        pause
        scene home_hall_idle with dissolve
        call screen map_home_hall
    else:
        scene livingroom with dissolve
        pause
        scene home_hall_idle with dissolve
        call screen map_home_hall
    
####### Bathroom ########

screen timedAnswerMBath():
    timer 5.0 action Jump("pcStareMBath")

if 'mousedown_1':
    hide screen timedAnswerMBath
    pc "S-shit, sorry."
    scene home_hall_idle with dissolve
    call screen map_home_hall
    
label pcStareBathTimer:
    window hide
    show screen timedAnswerMBath
    pause
    
label pcStareMBath:
    if mob >= 7:
        pass #placeholder
    elif mob >=10:
        pass #placeholder
    else:
        m "Um... [pc]? Are you staring at me?"
        pc "Ugh... shit, s-sorry."
        
    scene home_hall_idle with dissolve
    call screen map_home_hall

label bathroom:
    $ pcLocation = "h_bathroom"
    
    if storyEvent == False and livingHomeDays > 0:
        $ randombathroomscene = renpy.random.randint(1, 10)
        if randombathroomscene == 1 and bathscene1 == 0 and daylyActions < 3:
            $ bathscene1 = 1
            scene bathroom rachel check bath with dissolve
            pause
            scene home_hall_idle with dissolve
            call screen map_home_hall
        elif randombathroomscene == 2 and bathscene2 == 0:
            if uVersion == 0:
                $ bathscene2 = 1 
                scene bathroom ellie toilet1 with dissolve
                pause
                scene bathroom ellie toilet2 with dissolve
                pcthink "Ups..."
                scene home_hall_idle with dissolve
                call screen map_home_hall
        elif randombathroomscene == 3 and bathscene3 == 0 and workTime == False:
            $ bathscene3 = 1
            scene bathroom rachel naked mirror peep with dissolve
            pcthink "Whoa... looks like [m] just got out of the shower."
            menu:
                "Look":
                    scene bathroom rachel naked mirror busted with dissolve
                    m "[pc]!?"
                    pcthink "Uhh..."
                    call pcStareBathTimer from _call_pcStareBathTimer
                "Leave":
                    scene home_hall_idle with dissolve
                    call screen map_home_hall
        else:
            scene bathroom with dissolve
            pause
            scene home_hall_idle with dissolve
            call screen map_home_hall
    elif SErachelBathroomDay0 == True:
        jump rachelBathroomDay0
    elif SERachelBRAfterEBD == True:
        jump bathroomRAfterEBD
    else:
        scene bathroom with dissolve
        pause
    scene home_hall_idle with dissolve
    call screen map_home_hall
