import configparser
# from PyQt5.QtWidgets import *
import importlib
import preferences
import os
     

class pfile(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        self.PREFS_FILE='prefs.cfg'
        self.comments= {
            'projectfold' : 'programs directory',
            'dbdir' : 'location where databases reside',
            'freqencylist': 'location of the frequency list file',
            'outputdir' : 'location to output stat files to',
            'morphemizerfold': 'location where morphemizers are found',
            'knownmorphs': 'location of Known morphs db file',
            'externalmorphs': 'location of external morphs file',
            'currmophemizer' : 'name of currently selected morphemizer'
        }
            


        self.default_settings = {
            'DEFAULT'         : {
            'projectfold'       : os.getcwd(), # should I use relative dir here?:}
            'ankipath'          : 'C:\\Users\\WS\\AppData\\Roaming\\Anki2',
            'dbdir'             : '%(ankipath)s\\main\\dbs', #should I make a folder to place them in the project?
            'outputpath'        : '%(projectfold)s\\output',
            'outfreq'           : '%(outputdir)s\\frequency.txt',
            'morphemizerfold'   : '%(projectfold)s\\deps',
            'frequencylist'     : '%(dbdir)s\\frequencyM.txt',
            'knownmorphs'       : '%(dbdir)s\\known.db',
            'externalmorphs'    : '%(dbdir)s\\external.db',
            'inputpath'         : 'C:\\Users\\WS\\Desktop\\blah\\kiki\\chbk1\\ch07',
            'morphman_name'     : 'MM', #usually is 900801631
            'database_union'    :  '',
            
            
            #numerical values
            'min_master_freq'   : '0',
            'read_target'       : '98',
            'SourceScorePower'  : '2.0',
            'SourceScoreMultiplier' : '60.0',

            #checkboxes   inputtype 0   minimized 0
            'inputtype'         : '1', #clipboard = 0,  from file= 1 ;  # can be path,clipboard, #path splits into file or folder in code
            'save_study_plan'   : '1',
            'save_word_report'  : '1',
            'save_freqency_list': '1',
            'proper_nouns_known': '1',
            'fill_all_morphs_in_plan' : '1', # i think this should be 1
            'minimized'         : '0',
            'open_minimized'    : '0',
            'minimizetotray'    : '0',
            'wk_check'          : '0',
            'duo_check'         : '0',
                #special options checkboxes
            'ignorebracketcontents' : '1',
            'ignoreroundbracketcontents' : '1',
            'replacerules'      : '1', # TODO dont know what this is 
            'ignoregrammarposition' : '0',

            #morphemizer 
            'currmophemizer'    : 'MecabMorphemizer',
            'morphemizerlang'   : 'Japanese',

            #prefs external media
            'wk_api_key'        : '',
            'duolingo_user'     : '',
            'duolingo_pass'     : '',
            'shortcut'          : 'Ctrl+F3',
            'wk_db_name'        : '',
            'duo_db_name'        : ''
            }
        }
    def write_prefs(self):
        # par = os.path.split(PREFS_PATH)[0]
        # if not os.path.exists(par):
        #         os.makedirs(par)
        with open(self.PREFS_FILE, 'w') as configfile:
            self.write(configfile)

    def set_default_prefs(self):
        self.read_dict(self.default_settings)
        self.write_prefs()
    
    def add_comments(self,section,key):
        self[section][key]= self[section][key] + '#' + self.comments[key]
        # for list to loop through and add comments to the database file for readability
        # make sure to add # before matching values in the 

# PREFS_FOLDER='prefs'

# PREFS_PATH= os.path.join(PREFS_FOLDER,PREFS_FILE)

def init():
    prefs = pfile()
    prefs.read(prefs.PREFS_FILE)
    # print('items len:',len(prefs['DEFAULT']))
    if(len(prefs['DEFAULT'])<1): #if it is blank
        prefs.read_dict(prefs.default_settings)
        with open(prefs.PREFS_FILE, 'w') as configfile:
            prefs.write(configfile)
        print('write file')
    return prefs

if 'p' not in locals():
    p=init()

   

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
   

#    default_settings = {
#     'LOCATIONS'         : {
#     'projectfold'       : os.getcwd(), # should I use relative dir here?:}
#     'dbdir'             : 'C:\\Users\\WS\AppData\\Roaming\\Anki2\\main\\dbs', #should I make a folder to place them in the project?
#     'outputdir'         : '%(projectfold)s\\output',
#     'morphemizerfold'   : '%(projectfold)s\\deps'
#     },
    
#     'DATABASES'         : {
#     'frequencylist'     : '%(dbdir)s\\frequency.txt',
#     'knownmorphs'       : '%(dbdir)s\\known.db',
#     'externalmorphs'    : '%(dbdir)s\\external.db',
#     'currmophemizer'    : 'mecab'    
#     },

#     'VALUES'            : {
#     'min_master_freq'   : '0',
#     'read_target'       : '98'   
#     },
    
#     'CHECKBOXES'        : {
#     'save_study_plan'   :'1',
#     'save_word_report'  :'1',
#     'save_freqency_list':'1'    
#     }
# }