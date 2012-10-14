################################################################################
level_number = 3
dungeon_name = 'Sewers'
wall_style = 'Sewers'
monster_difficulty = 2
goes_down = True
entry_position = (0, 0)

phase_door = True
level_teleport = [
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    ]

stairs_previous = []
stairs_next = []
portal_down = []
portal_up = [(0, 5), (10, 21)]

teleports = [
    ((7, 17), (11, 17)),
    ((17, 15), (3, 19)),
    ((0, 13), (10, 14)),
    ]
encounters = [
    ((20, 8), (26, 8)),
    ((17, 12), (40, 3)),
    ((15, 1), (26, 7)),
    ((9, 11), (40, 4)),
    ((8, 9), (26, 5)),
    ((6, 1), (40, 3)),
    ((1, 2), (40, 2)),
    ((1, 7), (40, 4)),
    ]
messages = [
    ((0, 5), 'An inscription on the wall reads:\n\nSeek the Snare from behind the scenes.'),
    ((13, 7), 'An inscription on the wall reads:\n\nThe hand of time writes and cannot erase.'),
    ]
specials = [((16, 17), (16, 255))]

smoke_zones = []
darkness = [(8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2), (10, 1), (10, 2), (11, 0), (11, 1), (11, 2)]
antimagic_zones = []
spinners = [(10, 4)]
traps = [(11, 12), (15, 3)]
hitpoint_damage = []
spellpoint_restore = []
stasis_chambers = []
random_encounter = [(0, 16), (0, 21), (1, 2), (1, 17), (2, 12), (3, 10), (4, 4), (4, 8), (4, 17), (4, 21), (6, 0), (6, 19), (7, 18), (8, 15), (8, 21), (9, 12), (9, 14), (10, 0), (11, 11), (11, 19), (12, 0), (12, 1), (12, 2), (12, 12), (13, 11), (14, 13), (14, 15), (14, 18), (14, 21), (15, 19), (16, 11), (16, 21), (17, 2), (17, 7), (17, 11), (18, 5), (18, 10), (18, 11), (18, 15), (18, 17), (19, 2), (20, 16), (21, 12)]
specials_other = [(1, 8), (4, 12), (4, 15), (5, 17), (6, 1), (8, 7), (11, 4), (12, 11), (13, 9), (14, 17), (15, 1), (20, 2), (20, 7), (21, 5), (21, 13)]

map = [
    '| .. .. .. .. .---. |+-----. || .--------+| |+----++----++----++-+',
    '|                   ||       ||          || ||    DD    DD    DD |',
    '| .---------------. |+-----. |+--------. || |+---D++---D++---D++D+',
    '| .--++----++----+| |+----+| .---------. || |+---D++---D++---D++D+',
    '|    ||    ||    || ||    DD             || ||    DD    DD    || |',
    '| .. |+D-. || .. || || .. |+-----. .---. || || .. || .. || .. || |',
    '| || |+D+| || || || || .. |+----+| |+-+| .. || .. || .. || .. || |',
    '| || || || || || || ||    ||    DD || DD    ||    ||    ||    DD |',
    '| || || || || || || |+----+| .--+| |+-++--. |+D---++D---++D---++D+',
    '| || || || || || || |+----+| |+-+| .-----+| |+D---++D---++D---++D+',
    '| || || || || || || ||    || DD ||       || ||    ||    DD    || |',
    '| || || || |+D+| || || .-D+| |+-++-----. || || .. || .. || .. || |',
    '| || .. || .-D+| .. || |+D+| |+-++-++-+| || || .. || .. || .. || |',
    '| ||    ||    ||    || || || DD || DD || || ||    DD    ||    DD |',
    '| |+----++----++--. || |+-++-++-+| |+-+| || |+D---++----++D---++D+',
    '| .---------------. || |+----++--. |+--. || |+D---++----++D---++D+',
    '|                   || ||    ||    ||    || ||    ||    ||    || |',
    '+---------D-. .---. || || .. || .--+| .--++D+| .. || .. || .. || |',
    '+-++-++-++D+| .--+| .. .. .. || .--+| .----D+| .. || .. || .. || |',
    '| || DD DD ||    ||          ||    ||       ||    ||    ||    DD |',
    '+S++-++-+| || .. |+--------. || .--+| .-----++D---++---S++D---++D+',
    '+S-------. || || |+----++-+| || .--+| |+----++D---++---S++D---++D+',
    '|          || || ||    DD || ||    || ||    ||    DD    DD    || |',
    '| .------. || || || .--++-+| |+--. || || .. || .. || .. || .. || |',
    '| .-----+| || || .. .------. .---. .. || .. || .. || .. || .. || |',
    '|       || || ||                      DD    ||    ||    ||    DD |',
    '| .. .. || || |+-----. .----------D---++----++D---++D---++D---++D+',
    '| .. .. || || .------. .--------++D++-++-++-++D---++D---++D---++D+',
    '|       || ||                   || || DD DD ||    DD    ||    || |',
    '+-----. || |+-----. .. .---. .. |+D++D++-++D+| .. || .. || .. || |',
    '+-++--. || .-----+| || .--+| || |+D++D++-++D+| .. || .. || .. || |',
    '| DD    ||       || ||    || || || DD || DD ||    ||    DD    DD |',
    '+-+| .. || .. .. || |+--. |+-+| |+-++-++D++-++D---++D---++D---++D+',
    '+--. .. || .. .. || |+--. |+-+| |+-++-++D++-++D---++D---++D---++D+',
    '|       ||       || ||    || || || DD DD DD ||    DD    DD    || |',
    '+S------+| .. .. || || .--++D+| |+D++-++-++-+| .. || .. || .. || |',
    '+S++-++-+| .. .. || || .--++D-. |+D++-++-++-+| .. || .. || .. || |',
    '| || DD ||       || ||    ||    || DD DD DD ||    ||    ||    DD |',
    '+-++-++D++-------+| |+--. |+----++-++-++-++D++D---++D---++D---++D+',
    '+------D----------. |+--. |+----++-++----++D++D---++D---++D---++D+',
    '|                   ||    DD    || DD    || ||    DD    ||    || |',
    '| .------------. .. || .. || .. |+D+| .. || || .. || .. || .. || |',
    '| |+----++----+| .. || .. || .. |+D+| .. || || .. || .. || .. || |',
    '| ||    ||    ||    ||    ||    || ||    || ||    ||    DD    DD |',
    '| || .. || .. || .. || .. |+----+| |+---S+| |+D---++D---++D---++D+',
    '| || .. || .. || .. || || .------. |+---S+| |+D---++D---++D---++D+',
    '| DD    ||    ||    || ||          ||    || ||    DD    DD    || |',
    '| |+---D++S---++--. || |+--. .-----+| .--+| || .. || .. || .. || |',
    '| .--++D--S++----+| || .--+| .--++-+| |+--. || .. || .. || .. || |',
    '|    ||    ||    || ||    ||    || DD ||    ||    ||    ||    DD |',
    '| .. || .. || .. || |+--. |+--. |+-+| || .--++----++D--D++D---++D+',
    '| .. || .. || .. || |+-+| |+--. |+-+| || .--++----++D--D++D---++D+',
    '|    ||    DD    || || DD ||    || DD ||    ||    DD    ||    || |',
    '| .--++D---++---D+| |+-+| |+---D++-+| |+--. || .. || .. || .. || |',
    '| |+---D++----++D+| |+--. |+-++D++-+| |+--. || .. || .. || .. || |',
    '| ||    ||    || DD ||    || DD || DD ||    ||    ||    ||    DD |',
    '| || .--+| .. |+-+| || .--++-++-++-++-+| .. |+D---++D---++D---++D+',
    '| || |+-+| .. |+--. || .--------++----+| .. |+D---++D---++D---++D+',
    '| || || DD    ||    ||          ||    DD    ||    ||    DD    || |',
    '| |+-++D++----+| .. |+D----. .. || .. || .. || .. || .. || .. || |',
    '| .--++D++-----. .. |+D---+| || || .. || .. || .. || .. || .. || |',
    '|    DD ||          ||    || || DD    ||    ||    DD    ||    DD |',
    '| .. |+-+| .. .---. || .. || |+-++----++--. |+----++----++----+| |',
    '| .. .---. .. |+-+| || .. || |+----++-++-+| .-----------------+| |',
    '|             || DD ||    DD ||    DD DD ||                   DD |',
    '| .. .. .. .. |+-+| |+----+| || .--++-++-+| .-----------------++-+',
    ]

