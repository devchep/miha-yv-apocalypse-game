label vsem_pizda:
    play music 'audio/saw_ambient.mp3' volume 0.5
    scene black
    scene zaraznie
    centered '{b}Большая часть населения была поражена Яндекс.Вирусом{/b}' (what_color='#f8f9ff')
    scene dzenovie
    centered '{b}Многие погрузились в вечный Яндекс.Дзен{/b}' (what_color='#f8f9ff')
    centered '{b}В том числе твои друзья и товарищи{/b}' (what_color='#f8f9ff')
    scene dzen_boys
    centered '{b}Минус вайб{/b}' (what_color='#f8f9ff')
    centered '{b}Минус парни{/b}' (what_color='#f8f9ff')
    centered '{b}Минус вайб{/b}' (what_color='#f8f9ff')
    scene black with Dissolve(7)
    $ MainMenu(confirm=False)()