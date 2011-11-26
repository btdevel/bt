#from bt.extract.bt1.data import load_street_names

from bt.game.app import app
import bt.game.action as action
import bt.extract.bt1.char as charload

from bt.game.app import app

def load_msdos_char_list(btpath):
    pass

def load_msdos_char(btpath):
    pass

def get_char_list():
    btpath = app.config.msdos_path()
    print btpath

    import glob
    files = glob.glob(btpath + "/*.TPW")
    filelist = []
    for filename in files:
        char = charload.load_base_info(filename)
        filelist.append(char)

    return filelist

