################################################################################
level_number = 15
dungeon_name = 'The Tower'
wall_style = 'Mangar'
monster_difficulty = 7
goes_down = False
entry_position = (255, 255)

phase_door = False
level_teleport = [
    (11, True),
    (12, True),
    (13, True),
    (14, False),
    (15, False),
    ]

stairs_previous = []
stairs_next = []
portal_down = [(21, 0)]
portal_up = []

teleports = [
    ((1, 16), (1, 13)),
    ((2, 21), (16, 0)),
    ((11, 1), (15, 0)),
    ((12, 4), (15, 0)),
    ((10, 4), (15, 0)),
    ((0, 2), (0, 10)),
    ]
encounters = [
    ((10, 10), (107, 4)),
    ((0, 13), (121, 5)),
    ((13, 18), (125, 1)),
    ((5, 20), (123, 4)),
    ((3, 17), (122, 3)),
    ]
messages = []
specials = [
    ((15, 10), (51, 255)),
    ((21, 10), (52, 255)),
    ((8, 10), (53, 255)),
    ((10, 21), (54, 255)),
    ((17, 0), (55, 255)),
    ((1, 10), (56, 255)),
    ((1, 20), (57, 255)),
    ((20, 10), (58, 255)),
    ]

smoke_zones = [(1, 9), (1, 11)]
darkness = [(0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (1, 5), (1, 6), (1, 7), (1, 13), (1, 14), (1, 15), (2, 5), (2, 6), (2, 7), (2, 13), (2, 14), (2, 15), (3, 5), (3, 6), (3, 7), (3, 8), (3, 12), (3, 13), (3, 14), (3, 15), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (20, 13), (20, 14), (20, 15), (20, 16), (20, 17), (20, 18), (20, 19), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18), (21, 19)]
antimagic_zones = [(1, 8), (1, 12), (17, 5), (17, 6), (17, 7), (17, 8), (17, 12), (17, 13), (17, 14), (17, 15), (19, 9), (19, 10), (19, 11)]
spinners = []
traps = [(0, 11), (1, 1), (3, 3), (4, 9), (4, 10), (4, 11), (7, 3), (9, 17), (12, 18), (13, 0), (16, 15), (16, 18), (19, 0), (19, 3), (19, 5), (19, 9), (19, 15), (21, 5)]
hitpoint_damage = [(11, 10), (12, 10), (13, 10), (14, 10)]
spellpoint_restore = []
stasis_chambers = []
random_encounter = [(0, 2), (0, 4), (0, 6), (0, 8), (0, 12), (1, 6), (1, 8), (1, 12), (1, 14), (2, 0), (2, 2), (2, 3), (2, 13), (2, 20), (3, 1), (3, 3), (3, 6), (3, 13), (3, 15), (4, 4), (4, 19), (5, 10), (6, 3), (7, 6), (7, 8), (8, 15), (9, 7), (11, 6), (11, 14), (12, 3), (12, 6), (12, 14), (14, 2), (14, 18), (15, 8), (15, 12), (16, 10), (17, 2), (17, 15), (18, 7), (18, 10), (19, 14), (20, 4), (20, 21), (21, 8), (21, 14)]
specials_other = [(0, 10), (1, 10), (2, 9), (2, 10), (2, 11), (4, 0), (4, 5), (4, 6), (4, 7), (4, 8), (4, 12), (4, 13), (4, 14), (4, 15), (6, 10), (7, 10), (8, 10), (8, 18), (9, 4), (9, 10), (10, 1), (10, 10), (11, 4), (11, 10), (11, 21), (13, 10), (16, 20), (18, 17), (19, 21), (20, 8), (20, 9), (20, 10), (20, 11), (20, 12), (20, 16), (20, 20), (21, 2), (21, 13)]

map = [
    '+-------------++-------------++-++-------------++----------------+',
    '|             SS             || SS             ||                |',
    '| .. .. .. .. || .. .. .-----++D++-----. .. .. || .---. .. .. .. |',
    '| .. .. .. .. || .. .. |+----++D++----+| .. .. || |+-+| .. .. .. |',
    '|             ||       ||    || ||    ||       || || ||          |',
    '| .. .. .. .. || .. .. || .. |+D+| .. || .. .. || || || .. .---. |',
    '| .. .. .. .. || .. .. || .. .-D-. .. || .. .. || || || .. |+-+| |',
    '|             ||       ||             ||       || || ||    || || |',
    '| .. .. .. .. || .. .. |+--. .. .. .--+| .. .. || |+D+| .. |+D+| |',
    '| .. .. .. .. || .. .. .--+| .. .. |+--. .. .. || .-D-. .. .-D-. |',
    '|             ||          ||       ||          ||                |',
    '| .. .. .. .. || .. .. .. |+---D---+| .. .. .. || .. .. .---. .. |',
    '| .. .. .. .. || .. .. .. .----D----. .. .. .. || .. .. |+-+| .. |',
    '|             ||                               ||       DD ||    |',
    '+-------------+| .. .. .. .. .. .. .. .. .. .. || .. .. |+-+| .. |',
    '+-------------+| .. .. .. .. .. .. .. .. .. .. || .. .. .---. .. |',
    '|             ||                               ||                |',
    '| .---------. |+---S---------------------------+| .. .. .. .. .. |',
    '| |+-------+| .--++S---------++-++--------------. .. .. .. .. .. |',
    '| ||       ||    ||          || ||                               |',
    '| || .-----++--. || .. .. .. || || .. .. .. .. .. .. .---. .. .. |',
    '| || .---------. || .. .. .. || || .. .. .. .. .. .. |+-+| .. .. |',
    '| ||             ||          || ||                   || ||       |',
    '| |+-----. .-----+| .. .. .. || || .. .. .------. .. || || .. .. |',
    '| .-----+| |+----+| .. .. .. || || .. .. |+----+| .. || || .. .. |',
    '|       || ||    ||          || ||       ||    DD    || ||       |',
    '+-------+| || .. || .. .. .. || || .. .. |+----+| .. |+D+| .. .. |',
    '+-------+| || || || .. .. .. || || .. .. .------. .. .-D-. .. .. |',
    '|       || || || ||          || ||                               |',
    '| .---. || |+-+| || .. .. .. || || .. .. .. .. .. .. .. .. .. .. |',
    '| |+-+| || .---. || .. .. .. || || .. .. .. .. .. .. .. .. .. .. |',
    '| || || ||       ||          || ||                               |',
    '| || || || .---. |+----------++S++--------------. .. .. .. .-----+',
    '| || || || |+-+| |+-++---------S---------++-++-+| .. .. .. |+----+',
    '| || || || || || || DD                   DD |D ||          ||    |',
    '| || || || || || |+-+| .. .. .. .. .. .. |+-+| || .. .. .. || .. |',
    '| || .. || || || |+-+| .. .. .. .. .. .. |+-+| || .. .. .. || .. |',
    '| ||    || || || || DD                   DD |D ||          ||    |',
    '| |+----+| || || |+-++--------. .--------++-+| || .. .. .. |+D---+',
    '| .------. || || |+D---------+| |+-----------. || .. .. .. .-D---+',
    '|          || || ||          || ||             ||                |',
    '| .--------+| |+S++--. .. .. || || .. .. .. .. || .. .---. .. .. |',
    '| .---------. |+S++-+| .. .. || || .. .. .. .. || .. |+-+| .. .. |',
    '|             SS D| ||       || ||             ||    || ||       |',
    '+-------------++-+| || .-----+| |+-----. .-----+| .. |+D+| .. .. |',
    '+----------------+| || |+----+| |+----+| |+-----. .. .-D-. .. .. |',
    '|                || || DD    |D D|    DD ||                      |',
    '| .. .. .. .. .. || || || .. |+D+| .. || || .. .. .. .. .. .---. |',
    '| .. .. .. .. .. || || || .. |+-+| .. || || .. .. .. .. .. |+-+| |',
    '|                || || ||    || ||    || ||                DD || |',
    '| .. .------. .. || |+-++----++D++----++-+| .. .. .. .. .. |+-+| |',
    '| .. |+----+| .. || .--------++-++--------. .. .. .. .. .. .---. |',
    '|    DD    DD    ||          || ||                               |',
    '| .. || .. || .. |+--. .. .. || || .. .. .. .. .. .---. .. .. .. |',
    '| .. || .. || .. .--+| .. .. .. .. .. .. .. .. .. |+-+| .. .. .. |',
    '|    DD    DD       ||                            DD ||          |',
    '| .. |+----+| .. .. || .. .. .. .. .. .. .. .. .. |+-+| .. .. .. |',
    '| .. .------. .. .. || .. .. .. .. .. .. .. .. .. .---. .. .. .. |',
    '|                   ||                                           |',
    '| .. .. .. .. .. .. |+------------------------------------------D+',
    '| .. .. .. .. .. .. .--++-------------++-------------------++---D+',
    '|                      ||             ||                   DD    |',
    '+--------. .. .. .. .. |+D----. .----D++--. .. .. .. .. .. || .. |',
    '+-------+| .. .. .. .. .-D---+| |+---D---+| .. .. .. .. .. || .. |',
    '|       ||                   || ||       DD                ||    |',
    '+-------++-------------------++-++-------++----------------++----+',
    ]

