transform achievement_transform:
    on show:
        xalign .98 
        yalign -.3 
        linear 0.4 xalign .98 yalign .02
    on hide:
        linear 0.4 xalign 1.9 yalign .02

screen scr_achievement_get(title, a_text, icon, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_get")
    window:
        at trans
        background "#FCFCFC"
        xalign .98
        yalign .02
        xysize (450, 100)
        hbox:
            vbox:
                spacing 10
                image icon
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
                image icon
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text

init python:
    if persistent.achievements_unlocked is None:
        persistent.achievements_unlocked = {}

    if persistent.achievements_dict is None:
        persistent.achievements_dict = {}

    def progress():
        return '\nПрогресс достижений: ' + str(len(persistent.achievements_unlocked)) + '/' + str(len(persistent.achievements_dict))

    # Define your achievements here
    persistent.achievements_dict = {
                                    "tigr-ne-govno": {
                                            "type": 0,
                                            "title": "Тигры не говно",
                                            "text": "Ты думай чем тигра кормишь",
                                            "icon": "images/icons/tigr-govno.png",
                                        },
                                    "blya_derzhi_yashik": {
                                            "type": 0,
                                            "title": "Офигеть, да?",
                                            "text": "Нет, блять, не офигеть",
                                            "icon": "images/icons/yashik_achiev.png",
                                        },
                                    "victory": {
                                            "type": 0,
                                            "title": "Все пришло в норму",
                                            "text": "Вы победили Максимуса и остановили Яндекс Вирус",
                                            "icon": "images/icons/victory.png",
                                        },
                                    }


    def get_achievement(ach_id, trans=achievement_transform):
        if persistent.achievements_unlocked is None:
            return
        if ach_id in persistent.achievements_unlocked:
            return
        ach = persistent.achievements_dict[ach_id]
        persistent.achievements_unlocked.update({ach_id: ach})
        renpy.play("audio/ach.mp3")
        renpy.save_persistent()
        renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                          a_text=progress(), icon=ach['icon'], trans=trans)

    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog']:
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]

        renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                          icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)
                                    

        for i, a in persistent.achievements_dict.items():
            if a['type'] == 0:
                achievement.register(i, steam=a['title'])
            if a['type'] == 1:
                achievement.register(i, steam=a['title'], stat_max=a['max_prog'])