# coding=UTF8

strmap = [
    #012345678901234567890123456789
    u"██████████████████████████████",
    u"███                     ██   █",
    u"██  ███████ █████ █████    █ █",
    u"██        █ █   █      █ █   █",
    u"█  ███  █ █ █ █   ████ █ ██ ██",
    u"█  ██     █ █          █ ██ ██",
    u"██ ███  ███ ████ ███  ██ ██ ██",
    u"██     █       █     █       █",
    u"█      █ ██ ██  ████ █ ██ ████",
    u"█ ████ █  █   █    █ █ ██ █ ██",
    u"█    █    ███ ████   █ ██    █",
    u"█ ██ ████  ██ ████████ █  S ██",
    u"█ █      █ ██        █ █     █",
    u"███ █ ██ ████     ██ █ ██ 4███",
    u"█   █ ██   ██     ██   █G ████",
    u"███ █   ██ ██     ████ ██ ████",
    u"█ █ ███  █        ████ █     █",
    u"█ █    █ ████████ █  █ █  ████",
    u"█   ██ █   ██████ █     █    █",
    u"█      █ █   ██   █ ███  ██ ██",
    u"███ ██ █  ██ ██ ███    █ ██  █",
    u"███ ██ █  ██       █  ██  █ ██",
    u"█    █ █  █████████████ █ █  █",
    u"███ ██ █     ██    ███  █ █ ██",
    u"██  █  █  ██    ██      █ █ ██",
    u"██ ███ █  ██████       ██ █ ██",
    u"█   █  █          █  █  █ █ ██",
    u"█ █   ███████████       █ █  █",
    u"█   ██████████████████  █ ████",
    u"█████████████████████████ ████"
  ]

strmap = [
    #012345678901234567890123456789
    u"██████████████████████████████",
    u"███                     ██   █",
    u"██  ███████ █████ █████    █ █",
    u"██        █ █   █      █ █   █",
    u"█  ███  █ █ █ █   ████ █ ██ ██",
    u"█  ██     █ █          █ ██ ██",
    u"██ ███  ███ ████ ███  ██ ██ ██",
    u"██     █       █     █       █",
    u"█      █ ██ ██  ████ █ ██ ████",
    u"█ ████ █  █   █    █ █ ██ █ ██",
    u"█    █    ███ ████   █ ██    █",
    u"█ ██ ████  ██ ████████ █  S ██",
    u"█ █      █ ██        █ █     █",
    u"███ █ ██ ████     ██ █ █4 4███",
    u"█   █ ██   ██     ██   █G 1███",
    u"███ █   ██ ██     ████ █2 213█",
    u"█ █ ███  █        ████ 2     2",
    u"█ █    █ ████████ █  █ 1  124█",
    u"█   ██ █   ██████ █     4    2",
    u"█      █ █   ██   █ ███  32 3█",
    u"███ ██ █  ██ ██ ███    █ █T  3",
    u"███ ██ █  ██       █  ██  3 4█",
    u"█    █ █  █████████████ █ 1  1",
    u"███ ██ █     ██    ███  █ 2 1█",
    u"██  █  █  ██    ██      █ 1 P█",
    u"██ ███ █  ██████       ██ 4 3█",
    u"█   █  █          █  █  █ 3 1█",
    u"█ █   ███████████       █ 1  3",
    u"█   ██████████████████  █ █43█",
    u"█████████████████████████ ████"
  ]

repl = {u" ": Street("Unknown"),
        u"█": Building('house1'),
        u"1": Building('house1'),
        u"2": Building('house2'),
        u"3": Building('house3'),
        u"4": Building('house4'),
        u"G": Building('house3', 'guild.png'),
        u"S": Building('house4', 'shop.png'),
        u"T": Building('house1', 'temple.png'),
        u"P": Building('house2', 'pub.png')
        }
