################################################################################
level_number = 0
dungeon_name = 'Cellars'
wall_style = 'Cellar'
monster_difficulty = 0
goes_down = True
entry_position = (5, 28)

phase_door = True
level_teleport = [
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    ]

stairs_previous = [(21, 0)]
stairs_next = [(3, 7)]
portal_down = []
portal_up = []

teleports = []
encounters = []
messages = [
    ((1, 1), 'This is the wine cellar of the Scarlet Bard. The air is musty with old wine.'),
    ((10, 18), 'Rare wines - 5O years and older. Keep Out!'),
    ((12, 17), 'Fine wines - 1O years and older. For regular customers only.'),
    ]
specials = []

smoke_zones = []
darkness = []
antimagic_zones = []
spinners = [(11, 10)]
traps = [(5, 16)]
hitpoint_damage = []
spellpoint_restore = []
stasis_chambers = []
random_encounter = [(3, 2), (3, 3), (5, 7), (8, 17), (13, 2), (13, 3), (14, 15), (16, 2), (18, 15), (18, 17)]
specials_other = [(9, 17), (10, 10), (11, 18), (20, 1)]

map = [
    '+----------------------------------------------------------------+',
    '|                                                                |',
    '| .------------------------------------------------------------. |',
    '| |+----------------------------------------------------------+| |',
    '| ||                                                          || |',
    '| || .------. .------------. .. .. .------------------------. || |',
    '| || |+-++-+| |+-------++-+| .. .. |+-++-------------------+| || |',
    '| || || || || ||       || ||       || ||                   || || |',
    '| || |+-++-+| || .. .--+| || .. .. || || .---------------. || || |',
    '| || |+----+| || .. |+-+| || .. .. || || |+-------------+| || || |',
    '| || DD    DD ||    || || ||       || || ||             || || || |',
    '| || |+----+| |+----++D+| || .. .. || || || .---. .---. || || || |',
    '| || |+-++-+| .-----++D+| || .. .. || || || |+-+| |+-+| || || || |',
    '| || || || ||       || || ||       || || || || || || || || || || |',
    '| || || || || .---. || || || .. .. || || || |+-+| |+-+| || || || |',
    '| || || || || |+-+| || || || .. .. || || || .---. .---. || || || |',
    '| || || || || || || DD || ||       || || ||             || || || |',
    '| || |+-++-+| || || |+-+| || .. .. || || || .---. .. .--+| || || |',
    '| || |+----+| || || |+-+| || .. .. || || || |+-+| || |+--. || || |',
    '| || ||    || || || || || ||       || || || || || || ||    || || |',
    '| || |+--. || || || || || || .. .. || || || |+-+| || || .. || || |',
    '| || |+-+| || || || || || || .. .. || || || .---. || || .. || || |',
    '| || || || || || || || || ||       || || ||       || ||    || || |',
    '| || || || || || |+-+| || || .---. || || |+-------+| || .. || || |',
    '| || || || || || .---. || || |+-+| || || .--------+| || .. || || |',
    '| || || || || ||       || || || || || ||          || ||    || || |',
    '| || |+-++-+| |+-------++-+| |+-+| |+-++----------++D++----+| || |',
    '| || .------. .------------. .---. .----------------D-------. || |',
    '| ||                                                          || |',
    '| || .. .. .. .. .. .. .---. .. .. .---. .. .. .. .. .. .. .. || |',
    '| || .. .. .. .. .. .. |+-+| .. .. |+-+| .. .. .. .. .. .. .. || |',
    '| ||                   || ||       || ||                      || |',
    '| || .. .. .. .. .. .. |+-+| .. .. |+-+| .. .. .. .. .. .. .. || |',
    '| || .. .. .. .. .. .. .---. .. .. .---. .. .. .. .. .. .. .. || |',
    '| ||                                                          || |',
    '| || .------. .------------. .---. .-------------------D----. || |',
    '| || |+----+| |+----------+| |+-+| |+----------------++D++-+| || |',
    '| || ||    || ||          || || || ||                || || || || |',
    '| || |+----+| || .---. .. || |+-+| || .--------------+| || || || |',
    '| || |+-++-+| || |+-+| .. || .---. || |+-------------+| || || || |',
    '| || DD || DD || || ||    ||       || ||             || || || || |',
    '| || |+-++-+| || || || .. || .. .. || || .-----------+| || || || |',
    '| || |+----+| || || || .. || .. .. || || |+-++-++-++-+| || || || |',
    '| || ||    || || || ||    ||       || || || || || || || || || || |',
    '| || || .. || || || || .. || .. .. || || || |+D++D++D+| || || || |',
    '| || || .. || || || || .. || .. .. || || || |+D--D--D-. || || || |',
    '| || ||    || || || ||    ||       || || || DD          || || || |',
    '| || |+--. || |+-+| || .. || .. .. || || |+-+| .. .. .. || || || |',
    '| || |+-+| || .---. || .. || .. .. || || |+-+| .. .. .. || || || |',
    '| || DD || ||       ||    ||       || || || DD          || || || |',
    '| || || || || .-----+| .. || .. .. || || |+-+| .. .. .. || || || |',
    '| || || || || |+-----. .. || .. .. || || |+-+| .. .. .. || || || |',
    '| || || || || ||          ||       || || || DD          || || || |',
    '| || || || || || .. .. .. || .. .. || || || |+D--D--D--D+| || || |',
    '| || || || || || .. .. .. || .. .. || || || |+D++D++D++D+| || || |',
    '| || || || || ||          ||       || || || || || || || || || || |',
    '| || || |+-+| || .. .. .. || .. .. || || |+-++-++-++-++-+| || || |',
    '| || || .--+| || .. .. .. || .. .. || || .---------------. || || |',
    '| || ||    || ||          ||       || ||                   || || |',
    '+-+| |+----+| |+----------+| .. .. |+-++-------------------+| || |',
    '+--. .------. .------------. .. .. .------------------------. || |',
    '|                                                             || |',
    '| .. .--------------------------------------------------------+| |',
    '| .. |+--------------------------------------------------------. |',
    '|    ||                                                          |',
    '+----++----------------------------------------------------------+',
    ]
