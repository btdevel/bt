################################################################################
level_number = 6
dungeon_name = 'Catacombs'
wall_style = 'Catacombs'
monster_difficulty = 3
goes_down = True
entry_position = (0, 0)

phase_door = False
level_teleport = [
    (4, True),
    (5, True),
    (6, False),
    ]

stairs_previous = [(13, 11)]
stairs_next = []
portal_down = []
portal_up = []

teleports = [
    ((0, 21), (10, 7)),
    ((21, 15), (13, 17)),
    ((20, 19), (8, 11)),
    ((16, 21), (14, 21)),
    ]
encounters = [
    ((1, 0), (60, 7)),
    ((3, 9), (51, 36)),
    ((4, 13), (30, 69)),
    ((7, 17), (10, 99)),
    ((8, 5), (10, 99)),
    ((16, 13), (20, 66)),
    ((18, 14), (20, 53)),
    ((21, 0), (60, 8)),
    ]
messages = [
    ((20, 16), "A message is scrawled on the wall in blood:\nSeek the Mad One's stoney self in Harkyn's domain."),
    ]
specials = [((19, 20), (22, 255))]

smoke_zones = []
darkness = [(3, 17), (3, 18), (4, 17), (4, 18), (5, 17), (5, 18), (6, 17), (6, 18)]
antimagic_zones = [(13, 18), (13, 19), (13, 20), (14, 17), (14, 18), (14, 19), (14, 20), (18, 20)]
spinners = [(9, 9), (12, 13), (18, 6)]
traps = [(3, 19), (4, 19), (4, 20), (7, 14), (9, 2), (10, 15), (11, 4), (11, 12), (12, 16), (15, 6), (16, 3), (17, 6)]
hitpoint_damage = []
spellpoint_restore = []
stasis_chambers = []
random_encounter = [(0, 4), (0, 8), (1, 16), (2, 5), (2, 7), (3, 0), (3, 13), (4, 5), (4, 11), (5, 1), (6, 8), (6, 11), (7, 1), (7, 2), (7, 3), (7, 4), (9, 3), (9, 4), (9, 8), (10, 1), (11, 3), (11, 4), (11, 7), (12, 21), (13, 0), (13, 3), (13, 14), (14, 0), (14, 12), (14, 21), (16, 0), (16, 17), (16, 19), (17, 21), (19, 2), (19, 9), (19, 13), (19, 17), (19, 19), (19, 21), (21, 5), (21, 9)]
specials_other = [(0, 0), (0, 15), (1, 16), (1, 19), (2, 20), (3, 6), (3, 14), (3, 20), (5, 13), (5, 21), (7, 17), (7, 18), (7, 19), (7, 20), (8, 18), (8, 19), (8, 20), (9, 13), (12, 9), (13, 5), (14, 17), (17, 13), (18, 9), (20, 0), (21, 21)]

map = [
    '+-++-------++-++---D---++-++----------++----++-++----++----------+',
    '| DD       DD ||       DD ||          ||    || ||    ||          |',
    '+-++-----. |+-++--. .--++-+| .------. || .. || || .. || .------. |',
    '+--------. |+----+| |+----+| .-----+| || || .. || .. || |+----+| |',
    '|          ||    || ||    ||       || || ||    ||    || ||    || |',
    '+D---------+| .. || || .. |+-----. || || |+----++D---+| || .. || |',
    '+D---++----+| .. || || .. |+----+| || .. |+----++D----. || .. || |',
    '|    ||    ||    DD DD    ||    || ||    ||    ||       ||    || |',
    '| .. || .. |+---D+| |+D---+| .. || |+---D+| .. || .-----++---D+| |',
    '| .. || .. .----D-. .-D----. .. || .--++D+| .. || |+----++---D+| |',
    '|    DD                         DD    || ||    || ||    ||    || |',
    '+D---+| .. .----D-. .-D----. .. |+--. |+D++D---+| || .. || .--+| |',
    '+D---+| .. |+---D+| |+D---+| .. |+-+| |+D++D----. || || || .--+| |',
    '|    ||    ||    DD DD    ||    || DD || ||       || || ||    || |',
    '| .. |+----+| .. || || .. |+----++-+| |+D+| .. .. || || |+---D+| |',
    '| .. |+----+| .. || || .. |+--------. |+D+| .. .. || || |+---D+| |',
    '|    DD    ||    || ||    ||          || ||       || || ||    || |',
    '+----+| .. |+----+| |+----+| .----D---++-+| .. .. || || || .. || |',
    '+-----. .. |+-++--. .--++-+| |+---D++-----. .. .. || || .. .. || |',
    '|          DD ||       DD || ||    ||             || ||       || |',
    '| .--------++-++---D---++-+| || .. || .. .. .. .. || |+-------+| |',
    '| |+-++-++-++-++-++----++--. || .. || .. .. .. .. || .--------+| |',
    '| || || || || || ||    ||    ||    ||             ||          || |',
    '+D++D++D++D++D++D++--. |+D---++----+| .. .. .. .. |+--------. || |',
    '+D++D++D++D++D++D++-+| |+D---++-----. .. .. .. .. |+--------. || |',
    '| DD DD || DD || DD || ||    ||                   ||          || |',
    '+-++D++-++-++D+| |+-+| || .. || .. .. .-D-. .. .. |+----------+| |',
    '+-++D++-++-++D+| |+-+| || .. || .. .. |+D+| .. .. .------------. |',
    '| DD DD DD || DD DD || DD    ||       DD DD                      |',
    '+D++-++-++D++-++D++-++D++----+| .. .. |+D+| .. .. .. .. .. .-D---+',
    '+D++-++-++D++-++D++-++D++-----. .. .. .-D-. .. .. .. .. .. |+D---+',
    '| || || DD DD DD DD || ||                                  ||    |',
    '+D++D++D++-++-++-++-++D+| .. .. .. .. .. .. .. .. .. .-D---+| .. |',
    '+D--D--D++-++-++-++-++D+| .. .. .. .. .. .. .. .. .. |+D---+| .. |',
    '|       DD || DD DD || ||                            ||    ||    |',
    '+D----. |+-++-++D++-++-+| .-D-. .. .. .. .. .. .-D---+| .. || .-D+',
    '+D++-+| |+-++-++D++-----. |+D+| .. .. .. .. .. |+D---+| .. || |+D+',
    '| || || DD || DD DD       DD DD                ||    ||    || DD |',
    '+-++D+| |+-++D++-+| .. .. |+D+| .. .. .. .-D---+| .. || .-D+| |+-+',
    '+-++D+| |+-++D++-+| .. .. .-D-. .. .. .. |+D---+| .. || |+D+| |+-+',
    '| DD || DD DD || DD                      ||    ||    || DD || DD |',
    '+-++D++D+| |+-++-+| .. .. .. .. .. .-D---+| .. || .-D+| |+-+| |+-+',
    '+-++D--D+| |+-----. .. .. .. .. .. |+D---+| .. || |+D+| |+-+| |+-+',
    '| DD    DD ||                      ||    ||    || DD || DD || DD |',
    '+-+| .. |+-+| .. .. .. .. .. .-D---+| .. || .-D+| |+-+| |+-+| |+-+',
    '+-+| .. |+-+| .. .. .. .. .. |+D---+| .. || |+D+| |+-+| |+-+| |+-+',
    '| DD    DD ||                ||    ||    || DD || DD || DD || DD |',
    '+-++D---++D+| .. .. .. .-D---+| .. || .-D+| |+-+| |+-+| |+-+| |+-+',
    '+-++D++---D-. .. .. .. |+D---+| .. || |+D+| |+-+| |+-+| |+-+| |+-+',
    '| DD ||                ||    ||    || DD || DD || DD || DD || DD |',
    '+-+| || .. .. .. .-D---+| .. || .-D+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '+-+| || .. .. .. |+D---+| .. || |+D+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '| DD ||          ||    ||    || DD || DD || DD || DD || DD || DD |',
    '+-++D+| .. .-D---+| .. || .-D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '+---D-. .. |+D---+| .. || |+D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '|          ||    ||    || DD || DD || DD || DD || DD || DD || DD |',
    '| .. .-D---+| .. || .-D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '| .. |+D---+| .. || |+D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '|    ||    ||    || DD || DD || DD || DD || DD || DD || DD || DD |',
    '+D---+| .. || .-D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '+D---+| .. || |+D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '|    ||    || DD || DD || DD || DD || DD || DD || DD || DD || DD |',
    '| .. || .-D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '| .. || |+D+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+| |+-+',
    '|    || DD || DD || DD || DD || DD || DD || DD || DD || DD || DD |',
    '+----++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+',
    ]

