label maximus_palace_split:
    scene ptrg_pano with Dissolve(3)
    show maximusback at left
    pause 4
    hide maximusback
    show maximushands at left
    pause 4
    play sound 'audio/bone_crack.mp3'
    hide maximushands
    show maximus_crooked
    maximus 'ЧТО?!'
    if maximus_friend:
        maximus 'Твоя кровь не работает'
    else:
        maximus 'Его кровь не работает'
    play audio 'audio/splitscream.mp3' fadeout 20
    play audio 'audio/bone_crack.mp3'
    pause 0.6
    play audio 'audio/bone_crack.mp3'
    pause 0.4
    play audio 'audio/bone_crack.mp3'
    pause 0.2
    play audio 'audio/bone_crack.mp3'
    pause 0.1
    play audio 'audio/bone_crack.mp3'
    hide maximus_crooked
    show maximus_down
    scene black with Dissolve(2)
    stop audio
    scene ptrg_pano
    show maximus
    scene black with Dissolve(2)
    show maximus at left
    show maximus_mirrored at right
    scene ptrg_pano
    show maximus at left
    show maximus_mirrored at right
    maximus 'Невероятно'
    maximus 'Я.сам в ахуе'
    maximus 'Разделяй и властвуй, как говорится'
    maximus 'Вот теперь мы с тобой попляшем'
    stop music
    scene black with Dissolve(2)
    image maximus_postsplit = Movie(play = "./video/maximus_postsplit.webm", loop=False)
    show maximus_postsplit
    pause 38.5
    scene black
    pause 2
    if maximus_friend == True:
        scene home with Dissolve(2)
        miha 'Вот как-то так'
        miha 'Бля, ну и денёк'
    scene black with Dissolve(2)
    call vsem_pizda
    centered 'THE END'
    scene black
    nvle "Это конец"
    nvle "Максимус реализовал все, что планировал"
    nvle "Такое себе чето)"
    $ MainMenu(confirm=True)()
    