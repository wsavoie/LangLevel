from preferences import p
import pyperclip
import operator
from morphemizer import getAllMorphemizers,getMorphemizerByName
from morphemes import Morpheme, MorphDb, getMorphemes, altIncludesMorpheme
from anki.utils import stripHTML
import os
import io
import re
import csv
import errno

#TODO put these in a better place, perhaps inside class?
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    """
    return [atoi(c) for c in re.split(r'(\d+)', text)]
    
class Source:
    def __init__(self, name, morphs, line_morphs, unknown_db):
        self.name = os.path.basename(name)
        self.morphs = morphs
        self.line_morphs = line_morphs
        self.unknown_db = unknown_db

class readClass():
    #TODO preserve clipboard, save it in a variable and force copy to happen, or globally listen for a keystroke, copy current clipboard, save it out
    def __init__(self):
        #TODO make this agnostic from UI


        #import from ui

        self.inputPath = p['inputpath']
        #TODO make input a combo box of either clipboard or input path
        #TODO for now I will use an input path
        self.min_master_freq= p.getint('min_master_freq')
        self.read_target= p.getfloat('read_target')
        self.knownDbPath= p['knownmorphs']
        self.freq_path = p['frequencylist']
        self.getMorphemes= getMorphemizerByName(p['currmophemizer'])  
        self.outpath=p['outputpath']


        #while using this, make sure to close file after use
        self.tempFile = open("temp.txt", 'w')
        #
    def writeOutput(self, m):
        self.tempFile.write(m)
        
    def closeOut(self):
        self.tempFile.close()

    def onAnalyze(self):
        self.morphemizer = getMorphemizerByName(p['currmophemizer'])
        input_path = False # will set
        self.writeOutput('Using morphemizer: %s \n' % self.morphemizer.getDescription())
        debug_output = False


        if p.getboolean('inputtype') and ~p.getboolean('minimized'): # only uses fold when not minimized and inputtype is checked
            #TODO if certain keypress, force analyze through clipboard 
            input_path = p['inputpath']
        minimum_master_frequency= p.getint('min_master_freq')
        readability_target = p.getfloat('read_target')
        master_freq_path = p['frequencylist']
        known_words_path = p['knownmorphs']
        ext_morphs      = p['externalmorphs']
    
        output_path     = p['outputpath']
        
        save_frequency_list =  p.getboolean('save_freqency_list')
        save_word_report =  p.getboolean('save_word_report')
        save_study_plan = p.getboolean('save_study_plan')


        source_score_multiplier = p.getfloat('SourceScoreMultiplier')
        source_score_power = p.getfloat('SourceScorePower')


        proper_nouns_known = p.getboolean('ProperNounsAlreadyKnown')
        fill_all_morphs_in_plan = p.getboolean('FillAllMorphsInStudyPlan')


        if not os.path.exists(output_path):
            try:
                os.makedirs(output_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        frequency_list_path = os.path.normpath(output_path + '/frequency.txt')
        word_report_path = os.path.normpath(output_path + '/word_freq_report.txt')
        study_plan_path = os.path.normpath(output_path + '/study_plan.txt')
        readability_log_path = os.path.normpath(output_path + '/readability_log.txt')

        log_fp = open(readability_log_path, 'wt', encoding='utf-8')   

        master_db = MorphDb()
        unknown_db = MorphDb()

        master_total_instances = 0
        master_current_score = 0

        all_morphs = {}

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

        if os.path.isfile(known_words_path):
            known_db = MorphDb(known_words_path, ignoreErrors=True)

            total_k = len(known_db.groups)
            total_v = len(known_db.db)
            self.writeOutput("Known morphs loaded: K %d V %d\n" % (total_k, total_v))
        else:
            self.writeOutput("Known words DB '%s' not found\n" % known_words_path)
            known_db = MorphDb()
        self.known_db=known_db
        if master_total_instances > 0:
            master_current_score = 0
            for ms in master_db.db.values():
                for m, c in ms.items():
                    if known_db.matches(m):
                        master_current_score += c[0]
                        c[1] = True  # mark matched
            self.writeOutput("\n[Current master frequency readability] %0.02f\n" % (
                    master_current_score * 100.0 / master_total_instances))

        sources = []
        
        def measure_readability(self, file_name, is_ass, is_srt):
            self.writeOutput('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
                    "Input", "Total Morphs", "Known Morphs", "% Known Morphs", "Total Instances", "Known Instances",
                    "% Readability", "% Proper Nouns", "% Known Lines", "% i+1 Lines"))
            
            #filename will be clipboard if reading from clipboard
            log_fp.write('measure_readability %s\n' % file_name)
           
            proper_noun_count = 0
            i_count = 0
            line_count = 0
            line_morphs = []
            known_line_count = 0
            iplus1_line_count = 0
            known_count = 0
            seen_morphs = {}
            known_morphs = {}
            source_unknown_db = MorphDb()

            def proc_lines(text, is_ass, is_srt):
                nonlocal i_count, known_count, seen_morphs, known_morphs, all_morphs
                nonlocal proper_noun_count, line_count, known_line_count, iplus1_line_count, line_morphs
                
                text_index = -1
                num_fields = 1
                srt_count = 0

                def parse_text(text):
                    nonlocal i_count, known_count, seen_morphs, known_morphs, all_morphs
                    nonlocal proper_noun_count, line_count, known_line_count, iplus1_line_count, line_morphs
                    

                    log_fp.write('=== parse_text ===\n' + text + '\n')
                    # print('strip',stripHTML(text))
                    parsed_morphs = getMorphemes(self.morphemizer, stripHTML(text))
                    # parsed_morphs = getMorphemes(morphemizer, text)
                    if len(parsed_morphs) == 0:
                        return

                    unknown_count = 0
                    line_missing_morphs = set()
                    for m in parsed_morphs:
                        # Count morph for word report
                        all_morphs[m] = all_morphs.get(m, 0) + 1
                        seen_morphs[m] = seen_morphs.get(m, 0) + 1

                        if m.isProperNoun():
                            proper_noun_count += 1
                            is_proper_noun = True
                        else:
                            is_proper_noun = False

                        i_count += 1
                        if known_db.matches(m) or is_proper_noun: # Proper nouns are easy to learn, so assume they're known.
                            known_morphs[m] = known_morphs.get(m, 0) + 1
                            known_count += 1
                        else:
                            unknown_db.addMorph(m, 1)
                            source_unknown_db.addMorph(m, 1)
                            line_missing_morphs.add(m)
                            unknown_count += 1
                    line_count += 1
                    if unknown_count == 0:
                        known_line_count += 1
                    elif unknown_count == 1:
                        iplus1_line_count += 1
                    line_morphs.append(line_missing_morphs)

                filtered_text = ''
                for t in text.splitlines():
                    should_flush = True
                    if is_ass:
                        if 'Format:' in t:
                            formats = [x.strip() for x in t[8:].split(',')]
                            if 'Text' in formats:
                                text_index = formats.index('Text')
                                num_fields = len(formats)
                            else:
                                text_index = -1
                            continue
                        elif ('Dialogue:' not in t) or (text_index < 0):
                            continue
                        t = t[9:].split(',', num_fields - 1)
                        t = t[text_index]
                    elif is_srt:
                        srt_count += 1
                        if srt_count <= 2:
                            continue
                        elif t == '':
                            srt_count = 0
                        else:
                            should_flush = False
                    
                    if t != '':
                        filtered_text += t + '\n'
                    
                    # Todo: This will flush every line so we can compute per-line readability, which is slower than batching lines.
                    #       Figure out how to get per-line analysis with batched lines.
                    if should_flush:
                    #if len(filtered_text) >= 2048:
                        parse_text(filtered_text)
                        filtered_text = ''
        
                parse_text(filtered_text)

            try:
                if file_name=='clipboard':
                    input = pyperclip.paste()
                else:
                    with open(file_name.strip(), 'rt', encoding='utf-8') as f:
                        input = f.read()
                
                input = input.replace(u'\ufeff', '')
                
                #input = [l.replace(u'\ufeff', '') for l in f.read()]
                proc_lines(input, is_ass, is_srt)
                source = Source(file_name, seen_morphs, line_morphs, source_unknown_db)
                known_percent = 0.0 if len(seen_morphs.keys()) == 0 else 100.0 * len(known_morphs) / len(seen_morphs.keys())
                readability = 0.0 if i_count == 0 else 100.0 * known_count / i_count
                proper_noun_percent = 0.0 if line_count == 0 else 100.0 * proper_noun_count / i_count
                line_percent = 0.0 if line_count == 0 else 100.0 * known_line_count / line_count
                iplus1_percent = 0.0 if line_count == 0 else 100.0 * iplus1_line_count / line_count

                self.writeOutput('%s\t%d\t%d\t%0.2f\t%d\t%d\t%0.2f\t%0.2f\t%0.2f\t%0.2f\n' % (
                    source.name, len(seen_morphs), len(known_morphs), known_percent, i_count, known_count,
                    readability, proper_noun_percent, line_percent, iplus1_percent))
                # row = self.ui.readabilityTable.rowCount()
                # self.ui.readabilityTable.insertRow(row)
                # self.ui.readabilityTable.setItem(row, 0, QTableWidgetItem(source.name))
                # self.ui.readabilityTable.setItem(row, 1, TableInteger(len(seen_morphs)))
                # self.ui.readabilityTable.setItem(row, 2, TableInteger(len(known_morphs)))
                # self.ui.readabilityTable.setItem(row, 3, TablePercent(known_percent))
                # self.ui.readabilityTable.setItem(row, 4, TableInteger(i_count))
                # self.ui.readabilityTable.setItem(row, 5, TableInteger(known_count))
                # self.ui.readabilityTable.setItem(row, 6, TablePercent(readability))
                # self.ui.readabilityTable.setItem(row, 7, TablePercent(proper_noun_percent))
                # self.ui.readabilityTable.setItem(row, 8, TablePercent(line_percent))
                # self.ui.readabilityTable.setItem(row, 9, TablePercent(iplus1_percent))

                if save_study_plan:
                    sources.append(source)
            except:
                self.writeOutput("Failed to process '%s'\n" % file_name)
                raise

        def accepted_filetype(filename):
            return filename.lower().endswith(('.srt', '.ass', '.txt'))

        list_of_files= None
        ####################
        
        if os.path.isfile(input_path) or os.path.isdir(input_path):
            list_of_files = list()
            print('getting info from files!')
        ################### 

        if list_of_files is not list():
        
            for (dirpath, _, filenames) in os.walk(input_path):
                list_of_files += [os.path.join(dirpath, filename) for filename in filenames if accepted_filetype(filename)]

            # self.ui.readabilityTable.clear()
            # self.ui.readabilityTable.setRowCount(0)
            # self.ui.readabilityTable.setColumnCount(10)
            # self.ui.readabilityTable.setHorizontalHeaderLabels([
            #     "Input", "Total\nMorphs", "Known\nMorphs", "Known\nMorphs %", "Total\nInstances", "Known\nInstances",
            #     "Morph\nReadability %", "Proper\nNoun %", "Line\nReadability %", "i+1\nLines %"])

            if len(list_of_files) > 0:
                
            #     mw.progress.start( label='Measuring readability', max=len(list_of_files), immediate=True )
                for n, file_path in enumerate(sorted(list_of_files, key=natural_keys)):
            #         mw.progress.update(value=n, label='Parsing (%d/%d) %s' % (
            #             n + 1, len(list_of_files), os.path.basename(file_path)))
                    #TODO ADD PROGRESS BAR
                    if os.path.isfile(file_path):
                        is_ass = os.path.splitext(file_path)[1].lower() == '.ass'
                        is_srt = os.path.splitext(file_path)[1].lower() == '.srt'
                        measure_readability(self,file_path, is_ass, is_srt)
            #     mw.progress.finish()
            else:
                self.writeOutput('\nNo files found to process.\n')
                return
        else:
            measure_readability(self, 'clipboard',0,0) # for clipboard run
        # self.ui.readabilityTable.resizeColumnsToContents()

        if save_word_report:
            self.writeOutput("\n[Saving word report to '%s'...]\n" % word_report_path)
            with open(word_report_path, 'wt', encoding='utf-8') as f:
                last_count = 0
                morph_idx = 0
                group_idx = 0
                morph_total = 0.0
                all_morphs_count = sum(n for n in all_morphs.values())

                for m in sorted(all_morphs.items(), key=operator.itemgetter(1), reverse=True):
                    if m[1] != last_count:
                        last_count = m[1]
                        group_idx += 1
                    morph_idx += 1
                    morph_delta = 100.0 * m[1] / all_morphs_count
                    morph_total += morph_delta
                    print('%d\t%s\t%s\t%s\t%s\t%s\t%d\t%d\t%0.8f\t%0.8f matches %d' % (
                        m[1], m[0].norm, m[0].base, m[0].read, m[0].pos, m[0].subPos, group_idx, morph_idx, morph_delta,
                        morph_total, known_db.matches(m[0])), file=f)

        learned_tot = 0
        learned_morphs = []

        all_missing_morphs = []

        def get_line_readability(show, known_db):
            known_lines = 0
            for line_morphs in show.line_morphs:
                has_unknowns = False
                for m in line_morphs:
                    if known_db.matches(m):
                        continue
                    has_unknowns = True
                if not has_unknowns:
                    known_lines += 1
            line_readability = 0.0 if known_lines == 0 else 100.0 * known_lines / len(show.line_morphs)
            return line_readability

        if save_study_plan:
            self.writeOutput("\n[Saving Study Plan to '%s'...]\n" % study_plan_path)
            with open(study_plan_path, 'wt', encoding='utf-8') as f:
                # self.ui.studyPlanTable.clear()
                # self.ui.studyPlanTable.setRowCount(0)
                # self.ui.studyPlanTable.setColumnCount(7)
                # self.ui.studyPlanTable.setHorizontalHeaderLabels([
                #     "Input", "To Study\nMorphs ", "Cummulative\nMorphs", "Old Morph\nReadability %", "New Morph\nReadability %",
                #     "Old Line\nReadability %", "New Line\nReadability %"])

                # mw.progress.start( label='Building study plan', max=len(sources), immediate=True )

                for n, s in enumerate(sources):
                    # mw.progress.update( value=n, label='Processing (%d/%d) %s' % (n+1, len(sources), os.path.basename(s.name)) )
                    # if debug_output: f.write('Processing %s\n' % s.name)

                    known_i = 0
                    seen_i = 0
                    learned_m = 0
                    missing_morphs = []

                    old_line_readability = get_line_readability(s, known_db)

                    for m in s.morphs.items():
                        seen_i += m[1]
                        morph = m[0]
                        if known_db.matches(morph) or (proper_nouns_known and morph.isProperNoun()):
                            known_i += m[1]
                        else:
                            source_unknown_count = s.unknown_db.getFuzzyCount(morph, known_db)
                            unknown_count = unknown_db.getFuzzyCount(morph, known_db)
                            master_count = master_db.getFuzzyCount(morph, known_db)
                            source_count = source_unknown_count + unknown_count

                            score = pow(source_count, source_score_power) * source_score_multiplier + master_count
                            missing_morphs.append((m[0], m[1], source_unknown_count, unknown_count, master_count, score))

                            if debug_output: f.write('  missing: ' + m[0].show() + '\t[score %d ep_freq %d all_freq %d master_freq %d]\n' % (score, source_unknown_count, unknown_count, master_count))

                    all_missing_morphs += missing_morphs
                    readability = 100.0 if seen_i == 0 else known_i * 100.0 / seen_i
                    old_readability = readability

                    learned_this_source = []

                    for m in sorted(missing_morphs, key=operator.itemgetter(5), reverse=True):
                        if readability >= readability_target:
                            if debug_output: f.write('  readability target reached\n')
                            break

                        if known_db.matches(m[0]):
                            if debug_output: f.write('  known: %s\n' % m[0].show())
                            continue

                        if m[4] < minimum_master_frequency:
                            if debug_output: f.write('  low score: %s [score %d ep_freq %d all_freq %d master_freq %d]\n' % (m[0].show(), m[5], m[2], m[3], m[4]))
                            continue
                        
                        learned_morphs.append(m)
                        learned_this_source.append(m)
                        known_i += s.unknown_db.getFuzzyCount(m[0], known_db)
                        learned_m += 1
                        readability = 100.0 if seen_i == 0 else known_i * 100.0 / seen_i
                        known_db.addMLs1(m[0], set())

                    new_line_readability = get_line_readability(s, known_db)

                    learned_tot += learned_m
                    source_str = "'%s' study goal: (%3d/%4d) morph readability: %0.2f -> %0.2f line readabiltiy: %0.2f -> %0.2f\n" % (
                        s.name, learned_m, learned_tot, old_readability, readability, old_line_readability, new_line_readability)
                    self.writeOutput(source_str)
                    f.write(source_str)

                    # row = self.ui.studyPlanTable.rowCount()
                    # self.ui.studyPlanTable.insertRow(row)
                    # self.ui.studyPlanTable.setItem(row, 0, QTableWidgetItem(s.name))
                    # self.ui.studyPlanTable.setItem(row, 1, TableInteger(learned_m))
                    # self.ui.studyPlanTable.setItem(row, 2, TableInteger(learned_tot))
                    # self.ui.studyPlanTable.setItem(row, 3, TablePercent(old_readability))
                    # self.ui.studyPlanTable.setItem(row, 4, TablePercent(readability))
                    # self.ui.studyPlanTable.setItem(row, 5, TablePercent(old_line_readability))
                    # self.ui.studyPlanTable.setItem(row, 6, TablePercent(new_line_readability))

                    for m in learned_this_source:
                        f.write('\t' + m[0].show() + '\t[score %d ep_freq %d all_freq %d master_freq %d]\n' % (m[5], m[2], m[3], m[4]))

                # self.ui.studyPlanTable.resizeColumnsToContents()
                # mw.progress.finish()

                if save_frequency_list:
                    self.writeOutput("\n[Saving frequency list to '%s'...]\n" % frequency_list_path)
                    with open(frequency_list_path, 'wt', encoding='utf-8') as f:
                        unique_set = set()
                        # First output morphs according to the plan.
                        for m in learned_morphs:
                            if m[0].base in unique_set:
                                continue
                            unique_set.add(m[0].base)
                            print(m[0].base + '\t[score %d ep_freq %d all_freq %d master_freq %d]' % (m[5], m[2], m[3], m[4]), file=f)
                        
                        # Followed by all remaining morphs sorted by score.
                        if fill_all_morphs_in_plan:
                            for m in sorted(all_missing_morphs, key=operator.itemgetter(5), reverse=True):
                                if (m[0].base in unique_set):
                                    continue
                                if m[4] < minimum_master_frequency:
                                    continue
                                unique_set.add(m[0].base)
                                print(m[0].base + '\t[score %d ep_freq %d all_freq %d master_freq %d]' % (m[5], m[2], m[3], m[4]), file=f)
                
                if master_total_instances > 0:
                    master_score = 0
                    for ms in master_db.db.values():
                        for m, c in ms.items():
                            if known_db.matches(m):
                                master_score += c[0]
                                c[1] = True  # mark matched
                    self.writeOutput("\n[New master frequency readability] %0.02f -> %0.02f\n" % (
                        master_current_score * 100.0 / master_total_instances,
                        master_score * 100.0 / master_total_instances))