from manabi import MainWindow as mw
import configparser as cp
import importlib


cfg = cp.ConfigParser()
cfg.read('prefs.cfg')
# def init_preferences():
#     _init_config_py()

# def _init_config_py():
#     global config_py
#     from . import config
#     importlib.reload(config)
#     config_py = config
def default_prefs():
    cfg['OPTIONS'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
    cfg['LOCATIONS'] = {r'FrequencyList': r'C:/Users/WS/AppData/Roaming/Anki2/main/dbs/frequency.txt',
                    'KnownMorphsDir': r'C:\Users\WS\AppData\Roaming\Anki2\main\dbs\known.db'
                    'Outputdir':r'C:\Users\WS\AppData\Roaming\Anki2\main\dbs'
                    'morphemizerMainFold': r'C:\Users\WS\PyProjs\Manabi\MM\morph\deps',
                    }

def _get_config_py_preference(key, modelId=None, deckId=None):
    assert config_py, 'Tried to use cfgMods before profile loaded'
    profile = mw.pm.name
    model = mw.col.models.get(modelId)['name'] if modelId else None
    deck = mw.col.decks.get(deckId)['name'] if deckId else None
    if key in config_py.deck_overrides.get(deck, []):
        return config_py.deck_overrides[deck][key]
    elif key in config_py.model_overrides.get(model, []):
        return config_py.model_overrides[model][key]
    elif key in config_py.profile_overrides.get(profile, []):
        return config_py.profile_overrides[profile][key]
    else:
        return config_py.default[key]

def set_pref(input):
    cfg

def get_preferences():
#TODO do this method
    pref= {
        
    }
    return pref
def init_preferences():
    # TODO write this method
    pref = {}

def get_preference(key, model_id=None, deck_id=None):
    try:
        return _get_config_py_preference(key, model_id, deck_id)
    except KeyError:
        return _get_anki_json_config(key)

def update_preferences(jcfg):
    pref_copy = mw.col.conf['addons']['morphman'].copy()
    pref_copy.update(jcfg)
    if not mw.col.conf['addons']['morphman'] == pref_copy:
        mw.col.conf['addons']['morphman'] = pref_copy
        mw.col.setMod()
