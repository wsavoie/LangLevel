import codecs
import gzip
import os
import pickle5 as pickle

from abc import ABC, abstractmethod

import re
def char_set(start, end):
    # type: (str, str) -> set
    return set(chr(c) for c in range(ord(start), ord(end) + 1))


kanji_chars = char_set('㐀', '䶵') | char_set('一', '鿋') | char_set('豈', '頻')

class Morpheme:
    def __init__(self, norm, base, inflected, read, pos, subPos):
        """ Initialize morpheme class.

        POS means part-of-speech.

        Example morpheme infos for the expression "歩いて":

        :param str norm: 歩く [normalized base form]
        :param str base: 歩く
        :param str inflected: 歩い  [mecab cuts off all endings, so there is not て]
        :param str read: アルイ
        :param str pos: 動詞
        :param str subPos: 自立

        """
        # values are created by "mecab" in the order of the parameters and then directly passed into this constructor
        # example of mecab output:    "歩く     歩い    動詞    自立      アルイ"
        # matches to:                 "base     infl    pos     subPos    read"
        self.norm = norm if norm is not None else base
        self.base = base
        self.inflected = inflected
        self.read = read
        self.pos = pos  # type of morpheme determined by mecab tool. for example: u'動詞' or u'助動詞', u'形容詞'
        self.subPos = subPos

    def __setstate__(self, d):
        """ Override default pickle __setstate__ to initialize missing defaults in old databases
        """
        self.norm = d['norm'] if 'norm' in d else d['base']
        self.base = d['base']
        self.inflected = d['inflected']
        self.read = d['read']
        self.pos = d['pos']
        self.subPos = d['subPos']

    def __eq__(self, o):
        return all([isinstance(o, Morpheme), self.norm == o.norm, self.base == o.base, self.inflected == o.inflected,
                    self.read == o.read, self.pos == o.pos, self.subPos == o.subPos,
                    ])

    def __hash__(self):
        return hash((self.norm, self.base, self.inflected, self.read, self.pos, self.subPos))

    def __str__(self):
        return '\n'.join(['%d\t%s' % (len(m[1]), m[0].show()) for m in self])


    def base_kanji(self):
        # type: () -> set
        # todo: profile and maybe cache
        return set(self.base) & kanji_chars

    def getGroupKey(self):
        # type: () -> str
        #TODO get ignore grammaar position preference here
        # if cfg('Option_IgnoreGrammarPosition'):
        if True:
            return '%s\t%s' % (self.norm, self.read)
        else:
            return '%s\t%s\t%s\t' % (self.norm, self.read, self.pos)

    def isProperNoun(self):
        return (self.subPos == '固有名詞')

    def show(self):  # str
        return '\t'.join([self.norm, self.base, self.inflected, self.read, self.pos, self.subPos])


def ms2str(ms):  # [(Morpheme, locs)] -> Str
    return '\n'.join(['%d\t%s' % (len(m[1]), m[0].show()) for m in ms])

class MorphDBUnpickler(pickle.Unpickler):

    # def find_class(self, cmodule, cname):
    #     # Override default class lookup for this module to allow loading databases generated with older
    #     # versions of the MorphMan add-on.
    #     if cmodule.endswith('.morph.morphemes'):
    #         return globals()[cname]
    #     return pickle.Unpickler.find_class(self, cmodule, cname)
    def find_class(self, cmodule, cname):
                #return pickle.Unpickler.find_class(self, cmodule, cname)
        #TODO fix unpickling here
        return pickle.Unpickler.find_class(self, r'{0}.morph.morphemes'.format(addonName), cname)

square_brackets_regex = re.compile(r'\[[^\]]*\]')
round_brackets_regex = re.compile(r'\([^)]*\)')

def getMorphemes(morphemizer, expression, note_tags=None):
    if cfg('Option_IgnoreBracketContents'):
        if square_brackets_regex.search(expression):
            expression = square_brackets_regex.sub('', expression)
    if cfg('Option_IgnoreRoundBracketContents'):
        if round_brackets_regex.search(expression):
            expression = round_brackets_regex.sub('', expression)

    # go through all replacement rules and search if a rule (which dictates a string to morpheme conversion) can be
    # applied
    replace_rules = cfg('ReplaceRules')
    if note_tags is not None and replace_rules is not None:
        note_tags_set = set(note_tags)
        for (filter_tags, regex, morphemes) in replace_rules:
            if not set(filter_tags) <= note_tags_set:
                continue

            # find matches
            split_expression = re.split(
                regex, expression, maxsplit=1, flags=re.UNICODE)

            if len(split_expression) == 1:
                continue  # no match
            assert (len(split_expression) == 2)

            # make sure this rule doesn't lead to endless recursion
            if len(split_expression[0]) >= len(expression) or len(split_expression[1]) >= len(expression):
                continue

            a_morphs = getMorphemes(
                morphemizer, split_expression[0], note_tags)
            b_morphs = [Morpheme(mstr, mstr, mstr, mstr,
                                 'UNKNOWN', 'UNKNOWN') for mstr in morphemes]
            c_morphs = getMorphemes(
                morphemizer, split_expression[1], note_tags)

            return a_morphs + b_morphs + c_morphs

    ms = morphemizer.getMorphemesFromExpr(expression)

    return ms