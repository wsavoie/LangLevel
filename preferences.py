import configparser
# from PyQt5.QtWidgets import *
import importlib
import preferences
import os
     

def write_prefs():
    par = os.path.split(PREFS_PATH)[0]
    if not os.path.exists(par):
            os.makedirs(par)
    with open(PREFS_PATH, 'w') as configfile:
        prefs.write(configfile)

def set_default_prefs():
    prefs.read_dict(default_settings)
    write_prefs()
    
def add_comments(section,key):
    prefs[section][key]= prefs[section][key] + '#' + comments[key]
    # for list to loop through and add comments to the database file for readability
    # make sure to add # before matching values in the 
def init():
    prefs = configparser.ConfigParser()
    prefs.read(PREFS_PATH)
    if(len(prefs)==1): #if it is blank
        set_default_prefs()
    return prefs
PREFS_FOLDER='prefs'
PREFS_FILE='prefs.cfg'
PREFS_PATH= os.path.join(PREFS_FOLDER,PREFS_FILE)


comments= {
        'projectfold' : 'programs directory',
        'dbdir' : 'location where databases reside',
        'freqencylist': 'location of the frequency list file',
        'outputdir' : 'location to output stat files to',
        'morphemizerfold': 'location where morphemizers are found',
        'knownmorphs': 'location of Known morphs db file',
        'externalmorphs': 'location of external morphs file',
        'currmophemizer' : 'name of currently selected morphemizer'
}
        
default_settings = {
    'LOCATIONS'         : {
    'projectfold'       : os.getcwd(), # should I use relative dir here?:}
    'dbdir'             : 'C:\\Users\\WS\AppData\\Roaming\\Anki2\\main\\dbs', #should I make a folder to place them in the project?
    'outputdir'         : '%(projectfold)s\\output',
    'morphemizerfold'   : '%(projectfold)s\\deps'
    },
    
    'DATABASES'         : {
    'frequencylist'     : '%(dbdir)s\\frequency.txt',
    'knownmorphs'       : '%(dbdir)s\\known.db',
    'externalmorphs'    : '%(dbdir)s\\external.db',
    'currmophemizer'    : 'mecab'    
    },

    'VALUES'            : {
    'min_master_freq'   : '0',
    'read_target'       : '98'   
    },
    
    'CHECKBOXES'        : {
    'save_study_plan'   :'1',
    'save_word_report'  :'1',
    'save_freqency_list':'1'    
    }
}

if 'prefs' not in locals():
    prefs=init()

   

   


# for key in config['LOCATIONS']:
#     add_comments('LOCATIONS')
# print(prefs['LOCATIONS']['frequencylist'])


# cfg['OPTIONS'] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# cfg['LOCATIONS'] = {r'FrequencyList': r'C:/Users/WS/AppData/Roaming/Anki2/main/dbs/frequency.txt',
#                     'KnownMorphsDir': r'C:\Users\WS\AppData\Roaming\Anki2\main\dbs\known.db',
#                     'Outputdir': r'C:\Users\WS\AppData\Roaming\Anki2\main\dbs',
#                     'morphemizerMainFold': r'C:\Users\WS\PyProjs\Manabi\MM\morph\deps',
#                     }
#  with open('')       



# class manabuPrefs(configparser.ConfigParser):
#     def __init__(self):
#         super().__init__()
#         self.PREFS_FOLDER='prefs'
#         self.PREFS_FILE='prefs.cfg'
#         self.PREFS_PATH= os.path.join(self.PREFS_FOLDER,self.PREFS_FILE)
        
#         # TODO if empty perform set defaults 


#         self.comments= {
#         'projectfold' : 'programs directory',
#         'dbdir' : 'location where databases reside',
#         'freqencylist': 'location of the frequency list file',
#         'outputdir' : 'location to output stat files to',
#         'morphemizerfold': 'location where morphemizers are found',
#         'knownmorphs': 'location of Known morphs db file',
#         'externalmorphs': 'location of external morphs file',
#         'currmophemizer' : 'name of currently selected morphemizer'
#         }
        
#         self.default_settings = {
#             'LOCATIONS'         : {
#             'projectfold'       : os.getcwd(), # should I use relative dir here?:}
#             'dbdir'             : 'C:\\Users\\WS\AppData\\Roaming\\Anki2\\main\\dbs', #should I make a folder to place them in the project?
#             'outputdir'         : '%(projectfold)s\\output',
#             'morphemizerfold'   : '%(projectfold)s\\deps'
#             },
            
#             'DATABASES'         : {
#             'frequencylist'     : '%(dbdir)s\\frequency.txt',
#             'knownmorphs'       : '%(dbdir)s\\known.db',
#             'externalmorphs'    : '%(dbdir)s\\external.db',
#             'currmophemizer'    : 'mecab'    
#             },

#             'VALUES'            : {
#             'min_master_freq'   : '0',
#             'read_target'       : '98'   
#             },
            
#             'CHECKBOXES'        : {
#             'save_study_plan'   :'1',
#             'save_word_report'  :'1',
#             'save_freqency_list':'1'    
#             }
#         }

#         self.read(self.PREFS_PATH)
#         if(len(self)==1):
#             self.read_dict(self.default_settings)
#             self.write_prefs()

#     def write_prefs(self):
#         par = os.path.split(self.PREFS_PATH)[0]
#         if not os.path.exists(par):
#                 os.makedirs(par)
#         with open(self.PREFS_PATH, 'w') as configfile:
#             self.write(configfile)

#     def set_default_prefs(self):
#         #TODO change these before deploying
#         pass
#         # write_prefs()
#     def add_comments(self, section,key):
#         prefs[section][key]= prefs[section][key] + '#' + self.comments[key]
#         # for list to loop through and add comments to the database file for readability
#         # make sure to add # before matching values in the 

#     def load_prefs(self):
#         self.read(self.PREFS_PATH)

# if __name__ == "__main__":
#     prefs=manabuPrefs()
   