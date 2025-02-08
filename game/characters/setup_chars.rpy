define miha = Character('Миха', color="#215831")

define maks = Character('Макс', color="#2A28C3")

define stepa = Character('Степа', color="#E10B84")

define gera = Character('Гера', color="#5E5F00")

define lush = Character('Люш', color="#FFFFFF")

define unknown = Character('', color="#FFFFFF")

define igoryas = Character('Игорян', color="#E2AD59")

define creep = Character('Учебный Крип', color="#E2AD59")

define tigr = Character('Тигр', color="#F28100")

define andrei = Character('Дрюс', color="#2CADD1")

define torop = Character('Тороп', color="#AF0115")

define maximus = Character('{b}Максимус{/b}', color="#E80000")

define zlodei_1 = Character('Прихвостень', color="#717171")

define diman = Character('Диман', color="#1A1D31")

define ruta = Character('Рута', color="#FF3B96")

define law = Character('Law', color="#EBC41D")

define first = Character('001', color="#09505D")

define chineseLesh = Character('Лещ Dage', color="#8A5500")

define knee = Character('Knee', color="#A1292D")

define fakeLarkin = Character('Larkin', color="#54176A")

define tanya = Character('Капитан Татьяна Линчина', color = "#9c00ac")

define boy = Character('Крейзи школьник', color = '#810050')

define grisha = Character('Гриша', color = '#ff1f00')

define nvle = Character(_("&"), color="#c8ffc8", kind=nvl)

init 2 python:
    party = Party()
    style.default.font = "fonts/chinese.ttf"
    style.default.language = "eastasian"


    def hide_all_max():
        renpy.hide("max_angry")
        renpy.hide("max_happy")
        renpy.hide("max_pipe")
        renpy.hide("max1")
        renpy.hide("max2")
        renpy.hide("maxsit")
        renpy.hide("maxwait")
        renpy.hide("max_angry")
        renpy.hide("max3")
        renpy.hide("max4")

    def hide_all_igoryas():
        renpy.hide("igor_dovolen")
        renpy.hide("igor_ne_hochet")
        renpy.hide("igor_pretty")
        renpy.hide("igor_s_dr")
        renpy.hide("igor_shok_s_telef")
        renpy.hide("igor_shok")
        renpy.hide("igor_sret1")
        renpy.hide("igor_v_govne")
        renpy.hide("igor_wc_1")
        renpy.hide("igor_wc_2")
        renpy.hide("igor1")
        renpy.hide("igor_govno")

    def hide_all_lush():
        renpy.hide("lush_s_dr")
        renpy.hide("lush_wc_1")
        renpy.hide("lush_wc_2")
        renpy.hide("lush1")
        renpy.hide("lush2")
        renpy.hide("lush3")
        renpy.hide("lush4")
        renpy.hide("lush5")
        renpy.hide("lush6")
        renpy.hide("lush7")
        renpy.hide("lush_ananas")

    def hide_all_drei():
        renpy.hide("drei1")
        renpy.hide("tigr")
