import bt.util.configobj as configobj

class App(object):
    def read_config(self, filenames):
        self.config = configobj.ConfigObj(filenames[0])
        #conf = ConfigObj("bt1-user.conf")

app = App()
