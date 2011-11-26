import bt.util.configobj as configobj

_Empty = object()

class Config(object):
    def __init__(self, map={}, value=_Empty):
        #TODO: map has to be changed to maps and the lookup performed in all maps
        if not isinstance(map, dict):
            print map
            print type(map)
            raise Exception()
        self._map = map
        self._value = value

    def add(self, config):
        # see comment above
        self._map = config._map
        self._value = config._value

    def __getattr__(self, name):
        value = self._map.get(name, _Empty)
        if isinstance(value, dict):
            return Config(map=value)
        else:
            return Config(value=value)
        return map
    def _cast(self, value, type):
        if type is bool:
            return value.lower() not in ["off", "false", "f", "no", "n", ""]
        else:
            return type(value)
    def __call__(self, default=None, type=str):
        if self._value is _Empty:
            return default
        else:
            return self._cast(self._value, type)




class App(object):
    def __init__(self):
        self.config = Config()
        self.values = {}

    def read_config(self, filenames):
        self.config.add(self._make_config(filenames[0]))

    def _make_config(self, filename):
        try:
            conf = configobj.ConfigObj(filename, raise_errors=False)
        except configobj.ConfigObjError as conferr:
            print "Errors in config file (%s) detected:" % filename
            for err in conferr.errors:
                print ">", err
            conf = conferr.config
        return Config(conf)

app = App()
