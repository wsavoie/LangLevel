import sys
print(sys.version)
import numpy as np

import pandas as pd
import json
from pandas.io.json import json_normalize

#import nagisa
import os
import sys
import requests
import gzip
import asyncio as aio
import importlib
import pickle5 as pickle

import config 
import ankiF
import wanikaniF as wk


addonName='MM'
sys.path.insert(1, r'C:\Users\WS\AppData\Roaming\Anki2\addons21\{0}'.format(addonName))
from morph import morphemes
from morph import morphemizer
# from morph import preferences
# from morph.readability import CountingMorphDB


# import MM

# from MM.morph.util import *
# from PyQt5.QtWidgets import *

# from MM.morph.morphemes import MorphDb


class mm(pickle.Unpickler):
    def find_class(self, cmodule, cname):
                #return pickle.Unpickler.find_class(self, cmodule, cname)
        return pickle.Unpickler.find_class(self, r'{0}.morph.morphemes'.format(addonName), cname)
class MMorphDb(morphemes.MorphDb):        
    def load(self, path):  # FilePath -> m ()
#         '''asfddsaf
#         '''
        f = gzip.open(path)
        try:
            db = mm(f).load()
            for m, locs in db.items():
                self.addMLs1(m, locs)
        except ModuleNotFoundError as e:
            aqt.utils.showInfo(
                "ModuleNotFoundError was thrown. That probably means that you're using database files generated in "
                "the older versions of MorphMan. To fix this issue, please refer to the written guide on database "
                "migration (copy-pasteable link will appear in the next window): "
                "https://gist.github.com/InfiniteRain/1d7ca9ad307c4203397a635b514f00c2")
            raise e
        f.close()
    
    def DbInteractions(self,db2,kind): 
        a_set = set(self.db.keys()) 
        b_set = set(db2.db.keys())

        if kind == 'sym':
            ms = a_set.symmetric_difference(b_set)
        elif kind == 'A-B':
            ms = a_set.difference(b_set)
        elif kind == 'B-A':
            ms = b_set.difference(a_set)
        elif kind == 'inter':
            ms = a_set.intersection(b_set)
        elif kind == 'union':
            ms = a_set.union(b_set)
        else:
            raise ValueError("'kind' must be one of [sym, A-B, B-A, inter, union], it was actually '{kind}'")


        ms=a_set.union(b_set)
        # self.db.clear()
        for m in ms:
            locs = set()
            if m in self.db:
                locs.update(self.db[m])
            if m in db2.db:
                locs.update(db2.db[m])
            self.addMLs1(m, locs)


    # def union(dbA, dbB)
    #     a_set = set(db1.db.keys()) 
    #     b_set = set(db2.db.keys())

    #     ms=a_set.union(b_set)
    #     # self.db.clear()
    #     for m in ms:
    #         locs = set()
    #         if m in self.db:
    #             locs.update(self.db[m])
    #         if m in db2.db:
    #             locs.update(db2.db[m])
    #         self.addMLs1(m, locs)
    def save(self,path):
        fpath = os.path.split(path)[0]
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        f = gzip.open(path, 'wb')
        pickle.dump(self.db, f, -1)
        f.close()

        with gzip.open(path,'rb') as f:
            unpickler = mm(f)
            unpickler
            # unpickler.find_global = 'MM.morph.morphemes'
            obj = unpickler.load()
        
        with gzip.open(path,'wb') as f:
            pickle.dump(obj, f) # ClassA will now have a new path in 'dump-new'

    def union(self,db2):
        a_set = set(self.db.keys()) 
        b_set = set(db2.db.keys())

        ms=a_set.union(b_set)
        # self.db.clear()
        for m in ms:
            locs = set()
            if m in self.db:
                locs.update(self.db[m])
            if m in db2.db:
                locs.update(db2.db[m])
            self.addMLs1(m, locs)

    def unionExternal(self):
        db2= MMorphDb()
        # par = os.path.split(config.DBDIR.format('external.db'))[0]
        # if not os.path.exists(par):
        #     os.makedirs(par)
        if not os.path.exists(config.DBDIR.format('external.db')):
            db2.save(config.DBDIR.format('external.db'))

        db2.load(config.DBDIR.format('external.db'))
        
        self.union(db2)

        self.save(config.DBDIR.format('external.db')) 

# def readability(path):

def readfrequencyfile(path,masterDB):
    if os.path.isfile(master_freq_path):
        with io.open(master_freq_path, encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile, delimiter="\t")
            for row in csvreader:
                try:
                    instances = int(row[0])
                    m = Morpheme(row[1], row[2], row[2], row[3], row[4], row[5])

                    master_db.addMorph(m, instances)
                    master_total_instances += instances
                except:
                    pass
        self.writeOutput("Master morphs loaded: K %d V %d\n" % (
            master_db.getTotalNormMorphs(), master_db.getTotalVariationMorphs()))
    else:
        self.writeOutput("Master frequency file '%s' not found.\n" % master_freq_path)
        minimum_master_frequency = 0


def getClipboard():
    return pyperclip.paste()


def main():
    
    # # get wkdata from website and save it into a textfile
    #wkData=wanikaniText()

    mdb=MMorphDb()
    mecab=morphemizer.MecabMorphemizer()

    # #make wk.db file
    mdb.importFile(config.DBDIR.format('wanikaniVocab.txt'),mecab,maturity=21)
    mdb.save(config.DBDIR.format('wk.db')) #only need this line 
    
    # #union of wkData and external db file
    # mdb.unionExternal()

    db2 = MMorphDb()

    db2.load(config.DBDIR.format(' external.db'))
    mdb.DbInteractions(db2,'union')
    mdb.save(config.DBDIR.format('external.db'))



    

       

def wanikaniText():
    wklevel= wk.getWKLevel()
    print(f'current level is {wklevel}')

    wkData=wk.getWKData(wklevel)
    wkData.to_csv(config.DBDIR.format('wanikaniVocab.txt'))
    print('wanikani text file created')
    return wkData

    

main()