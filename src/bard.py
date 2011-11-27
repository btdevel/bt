from bt.game.state import State
from bt.game.app import app
app.read_config(["bt1-game.conf"])

from bt.game.bt1.city import get_city_handler
from bt.game.buildings import guild


state = State(get_city_handler(), guild)
state.run()
