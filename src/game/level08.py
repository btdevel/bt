################################################################################
level_number = 8
dungeon_name = 'Castle'
wall_style = 'Cellar'
monster_difficulty = 4
goes_down = False
entry_position = (0, 0)

phase_door = False
level_teleport = [
    (7, True),
    (8, False),
    (9, True),
    ]

stairs_previous = [(2, 0)]
stairs_next = []
portal_down = []
portal_up = [(2, 19)]

teleports = [
    ((5, 11), (3, 10)),
    ((9, 10), (0, 1)),
    ((17, 12), (3, 6)),
    ((5, 18), (16, 4)),
    ]
encounters = [
    ((4, 14), (99, 8)),
    ]
messages = [
    ((5, 6), 'You are in a splendid library.'),
    ((4, 13), 'A sign on the wall reads, "Slave quarters."'),
    ((6, 10), 'The air nearby has a foul reek to it.'),
    ((20, 18), 'Something is not quite right here.'),
    ]
specials = [
    ((9, 9), (28, 255)),
    ((0, 0), (29, 255)),
    ((0, 19), (30, 255)),
    ]

smoke_zones = [(6, 7), (7, 7), (8, 8)]
darkness = [(7, 3), (7, 4), (8, 21), (9, 20), (9, 21)]
antimagic_zones = [(2, 10)]
spinners = []
traps = [(3, 7), (7, 2), (16, 14)]
hitpoint_damage = [(16, 5), (17, 5), (18, 5), (19, 5), (20, 5), (20, 10), (6, 8), (7, 9), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6), (7, 10), (7, 11)]
spellpoint_restore = []
stasis_chambers = []
random_encounter = [(1, 2), (3, 11), (4, 7), (5, 12), (6, 0), (6, 8), (7, 16), (8, 9), (8, 11), (8, 14), (9, 6), (9, 9), (9, 10), (9, 11), (9, 13), (9, 14), (10, 2), (10, 16), (12, 12), (13, 13), (13, 17), (14, 0), (15, 11), (16, 9), (18, 0), (19, 0), (19, 1), (19, 19), (20, 17), (21, 17), (21, 19)]
specials_other = [(1, 5), (1, 6), (1, 18), (2, 5), (2, 6), (3, 5), (3, 6), (4, 5), (4, 6), (4, 12), (5, 5), (5, 6), (12, 9), (12, 10), (13, 8), (14, 7), (14, 9), (14, 10), (14, 11), (15, 7), (15, 8), (15, 10), (16, 6), (16, 11), (16, 18), (17, 10), (17, 13), (17, 14), (19, 10), (21, 0), (21, 19)]

map = [
    '------. .. .. || .. .. || .. .. .. .. .. .. |+D+| .------------. .',
    '              ||       ||                   || ||                 ',
    '---. .--------++-------+| .. .. .. .. .. .. || || .------------. .',
    '+--. |+-++----++-------+| || .. .. .. .. .. || || |+-++-------+| |',
    '|    DD DD    ||       DD ||                || || || ||       || |',
    '| .. || || .. |+-------+| || .------------. || |+-+| || .. .. || |',
    '| .. || || .. |+-------+| || |+----------+| .. .---. || .. .. || |',
    '|    || ||    DD       DD || ||          ||          ||       || |',
    '| .. || || .. |+-------+| || || .------. || .. .-----++------D+| |',
    '| .. || || .. |+-------+| || || |+----+| || .. .-------------D+| |',
    '|    || ||    ||       DD || || ||    || ||                   || |',
    '+----++D+| .. |+-------+| || || || .. || || .. .. .. .--------++-+',
    '+------D-. .. |+-------+| || || || || || || .. .. .. .-----------+',
    '|             ||       DD || || || || || ||                      |',
    '| .. .. .. .. |+-------+| || || || |+-+| || .. .. .. .. .. .. .. |',
    '| .. .. .. .. |+-------+| || || || .---. || .. .. .. .. .. .. .. |',
    '|             ||       DD || || ||       ||                      |',
    '+--. .. .. .. |+-------+| || || |+-------+| .---. .. .-D-----D---+',
    '+-+| .. .. .. .---------. .. .. .---------. |+-+| || .-D-----D---+',
    'D DD                                        || || ||             D',
    '+-++--------------. .. .. .. .. .. .. .. .. || |+-++D-. .. .-----+',
    '-----++-------++-+| .. .. .. .. .. .. .. .. .. .----D+| || .------',
    '     ||       SS ||                                  || DD        ',
    '. .. |+---D--D+| |+D-----D--D--D--D--D--D--D-. .. .. || || .. .. .',
    '. || .----D--D-. .-D---++D++D++D++D++D++D++D+| .. .. || || .. .. .',
    '  ||                   || || || || || || || ||       DD ||        ',
    '. |+--------. .------. |+-++-++-++-++-++-++-+| .. .--+| |+--. .. .',
    '. .--++----+| |+-++-+| |+-++-++-++-++-++-++-+| .. |+--. |+--. .. .',
    '     ||    || DD DD DD || || || || || || || ||    DD    ||        ',
    '. .. |+----+| |+-++-+| |+D++D++D++D++D++D++D+| .. |+----+| .. .. .',
    '. .. .--++--. .------. .-D--D--D--D--D--D--D-. .. .-----+| .. || .',
    '        ||                                              ||    ||  ',
    '. .. .--++D-. .. .---. .. .. .. .. .. .. .. .. .. .. .--+| .--+| .',
    '. .. |+---D+| .. |+--. .. .. .. .. .. .. .. .. .. .. |+-+| .---. .',
    '     DD    ||    ||                                  || DD        ',
    '. .. |+--. |+----++--------------------------------. |+-++--. .. .',
    '. .. .--+| |+-------------------++----++---------D+| .-----+| || .',
    '        || ||                   D|    |D          ||       || ||  ',
    '------. |+-+| .-----------------+| .-D++-----. .. |+-------+| |+--',
    '-----+| .--+| .-----------++-----. |+-++-++--. .. |+----++--. .---',
    '     ||    ||             |D       || || |D       ||    ||        ',
    '---. |+----++-------------++-------+| |+D++--. .. |+--. || .------',
    '--+| |+----++-------++----++-++-++-+| .-D---+| .. |+--. || |+-----',
    '  SS ||    ||       ||    SS || || ||       DD    ||    || ||     ',
    '. || || .. || .. .. || .--++D++D++D++-----. |+--. |+--. || || .. .',
    '. || || .. || .. .. || |+-++D--D--D++----+| |+-+| |+--. || || .. .',
    '  || ||    ||       || || DD       DD    || || DD ||    || ||     ',
    '--+| || .. || .. .. || |+-++--. .--++--. |+-+| || |+--. || |+-----',
    '---. || .. || .. .. .. .-----+| |+-----. .---. .. |+--. || .------',
    '     ||    ||                || ||                ||    ||        ',
    '-----+| .. |+----------------+| |+----------------++--. |+--------',
    '------. .. .-----------------+| |+-------++----------+| .---------',
    '                             || ||       DD          ||           ',
    '------------. .. .. .. .. .. || || .. .. |+--. .. .. || .. .------',
    '-----------+| .. .. .. .. .. || || .. .. |+--. .. .. || .. |+-----',
    '           ||                || ||       ||          ||    ||     ',
    '. .. .. .. || .. .. .. .. .. || || .. .. |+----------+| .--+| .. .',
    '. .. .. .. || .. .. .. .. .. || || .. .. |+----++-++-+| |+--. .. .',
    '           ||                || ||       ||    DD DD || DD        ',
    '-----------+| .. .. .. .. .. || || .. .. || .-D++-++D+| |+D----. .',
    '+D++--------. .. .. .. .. .. .. .. .. .. || |+D++-++D+| |+D---+| |',
    '| ||                                     || || || || || ||    || |',
    '| |+--. .. .. .---------. .. .. .. .-----+| |+D+| |+D++-+| .. || |',
    '| .--+| .. .. |+-------+| .. .. .. .------. |+D+| |+D++-+| .. || |',
    '|    ||       ||       DD                   D| |D || DD DD    || |',
    '+----+| .. .. || .. .. || .. .. .. .. .. .. |+-+| |+-++-++----+| |',
    ]

