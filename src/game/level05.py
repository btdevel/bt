################################################################################
level_number = 5
dungeon_name = 'Catacombs'
wall_style = 'Catacombs'
monster_difficulty = 3
goes_down = True
entry_position = (0, 0)

phase_door = True
level_teleport = [
    (4, True),
    (5, True),
    (6, False),
    ]

stairs_previous = [(6, 16)]
stairs_next = [(13, 11)]
portal_down = []
portal_up = []

teleports = []
encounters = [
    ((11, 6), (30, 49)),
    ((0, 21), (120, 1)),
    ]
messages = [
    ((18, 11), 'A sign proclaims that you have entered the chambers of Bashar Kavilor, High Priest. Prepare to die!'),
    ((0, 1), 'Stasis chamber ahead: Those who venture ahead should prepare for a long stay!'),
    ((11, 11), 'A voice from no where proclaims:\n\nTo the tower fly\nA mad one die\nOnce lost the eye'),
    ]
specials = [
    ((12, 10), (20, 255)),
    ((13, 6), (21, 255)),
    ]

smoke_zones = []
darkness = [(6, 9), (6, 10), (6, 11), (7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11), (9, 11), (17, 14), (17, 15), (18, 13), (18, 14), (18, 15), (18, 16), (19, 14), (19, 15)]
antimagic_zones = [(19, 11)]
spinners = [(18, 2), (5, 8)]
traps = [(3, 9), (3, 10), (4, 9), (4, 10), (4, 11), (5, 9), (5, 10), (5, 11), (16, 0), (16, 4), (16, 12), (16, 17), (20, 4), (20, 8), (20, 12), (20, 17)]
hitpoint_damage = []
spellpoint_restore = []
stasis_chambers = [(0, 0)]
random_encounter = [(1, 10), (3, 7), (3, 8), (3, 12), (3, 13), (3, 15), (3, 17), (3, 21), (5, 20), (6, 13), (7, 13), (7, 20), (10, 13), (10, 14), (10, 16), (10, 18), (11, 0), (11, 8), (11, 10), (11, 11), (13, 10), (13, 15), (14, 2), (14, 6), (15, 9), (15, 15), (15, 18), (15, 20), (15, 21), (17, 2), (17, 5), (17, 10), (17, 13), (17, 16), (19, 7), (19, 16), (19, 18), (19, 20)]
specials_other = [(2, 11), (3, 2), (3, 11), (8, 6), (9, 10), (10, 6), (10, 11), (16, 8), (21, 0), (21, 1), (21, 21)]

map = [
    '+-------++----------++----++-++-++-------------------------------+',
    '|       ||          ||    || DD ||                               |',
    '| .---. || .------. || .. || |+-+| .---------------------------. |',
    '| .--+| || .------. .. || || |+-+| |+--------------------------. |',
    '|    || ||             || || DD || ||                            |',
    '+--. || |+-----. .---. || || |+-+| || .--------------------------+',
    '+--. || .------. .--+| || .. .--+| || .--------------------++----+',
    '|    ||             || ||       || ||                      ||    |',
    '| .--+| .------. .--++-++-------++D++--------------------. || .. |',
    '| .---. .-----+| |+-++-++-++------D++-++-++-++-++-++-++-+| || .. |',
    '|             || || || || ||       || DD || || || || || || ||    |',
    '| .. .------. |+-++D++D++D+| .. .. |+D++-++D++D++D++D++D++-++---S+',
    '| || .-----+| .--++D--D--D+| .. .. |+D++-++D--D--D--D--D--D++-++S+',
    '| ||       ||    ||       ||       || || DD                DD || |',
    '| |+-----. || .. || .. .. || .. .. |+S++-+| .---------. .. |+-+| |',
    '| .------. || || || .. .. || .. .. |+S---+| |+-------+| || |+--. |',
    '|          || || ||       DD       ||    DD ||       || || DD    |',
    '| .------. || || |+-------++D------+| .. || || .---. || || |+----+',
    '| .--++--. .. || |+-------++D------+| .. || || |+--. || || |+----+',
    '|    ||       || ||       ||       ||    DD || ||    || || DD    |',
    '+--. |+-----. || || .---. |+-----. |+----+| || || .. || || |+--. |',
    '+--. .--++--. .. || .--+| |+-----. |+-++-+| || || .. || || |+-+| |',
    '|       ||       ||    || ||       || || DD || ||    || || DD || |',
    '| .---. || .-----++--. || || .-----+| |+-+| || |+----+| || |+-++-+',
    '| .--+| || .-----++-+| || || .-----+| .--+| || .------. || |+----+',
    '|    || ||       |D || || ||       ||    DD ||          || DD    |',
    '+--. || || .---. |+D+| || |+-----. |+----+| |+----------+| || .. |',
    '+--. || .. |+--. |+D-. || |+----+| |+----+| .------------. || .. |',
    '|    ||    ||    ||    || SS    DD ||    DD                DD    |',
    '| .--+| .--++----++----++-+| .. |+-+| .--++D--D--D--D--D--D++----+',
    '| .--+| .-----++-++-++-++-+| .. |+-+| |+-++D++D++D--D++D++D++----+',
    '|    ||       || || DD DD DD    SS || || || || ||    || || SS    |',
    '+--. |+-------+| |+-++-++-++----++-+| |+D++-+| || .. || |+-+| .. |',
    '+-+| .---------. .--++-++-++-++-++-+| .-D++--. || .. || .--+| .. |',
    '| DD                DD DD DD DD || SS    ||    ||    ||    ||    |',
    '+-++-----. .--------++-++-++-++-++-++D---++----++----++----++----+',
    '---------. .-------------------------D----------------------------',
    '                                                                  ',
    '. .---------. .---------. .---------. .------------. .------------',
    '| |+-------+| |+-------+| |+-++-++-+| |+----++-++-+| |+----------+',
    '| ||       || ||       || || DD || || ||    DD || || ||          |',
    '| || .-D-. || || .---. || |+-++-++S+| || .. |+-+| || || .------. |',
    '| || |+D+| || || |+-+| || |+-++-++S+| || .. |+--. || || .-----+| |',
    '| || || || || || || DD || || DD DD || ||    ||    || ||       || |',
    '| || |+-+| || || |+-++-+| |+-++-++D+| || .. || .. || |+D----. |+D+',
    '| || .---. || || .-----+| |+-++-++D+| || .. || .. || |+D++-+| |+D+',
    '| ||       || ||       || || DD DD || ||    ||    || || || || || |',
    '| |+---D---+| |+---D---+| |+-++D++-+| |+---D++D---+| |+-++D++D++-+',
    '. .----D----. .----D----. .----D----. .----D--D----. .----D--D----',
    '                                                                  ',
    '. .----D----. .----D----. .----D----. .----D--D----. .----D--D----',
    '| |+-++D---+| |+-++D---+| |+---D---+| |+-++D--D++-+| |+---D++D---+',
    '| || ||    || || ||    || ||       || || ||    || || ||    ||    |',
    '| || |+--. || |+D+| .. || || .. .. || |+D+| .. |+D+| || .. || .. |',
    '| || .--+| || |+D+| .. || || .. .. || |+D-. .. .-D+| || .. || .. |',
    '| ||    || || || ||    || ||       || ||          || ||    ||    |',
    '| || .. || || || |+---D+| || .. .. || |+D-. .. .-D+| |+D--D++D--D+',
    '| || || .. || || |+---D+| || .. .. || |+D+| .. |+D+| |+D++D++D++D+',
    '| || ||    || || DD    || ||       || || ||    || || || || || || |',
    '| |+-++----+| |+-++----+| |+-------+| |+-++----++-+| |+-++-++-++-+',
    '. .---------. .---------. .---------. .------------. .------------',
    '                                                                  ',
    '-------------------S----------------------------------------------',
    '+D++-++------------S++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+',
    'D DD DD             D| D| D| D| D| D| D| D| D| D| D| D| D| D| D| |',
    '+D++-++-------------++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+',
    ]

