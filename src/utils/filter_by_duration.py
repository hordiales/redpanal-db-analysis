#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 
Recorre un directorio con archivos jsons con descriptores MIR y los separa en canciones y samples.
El criterio para esta división es tomar como samples o muestras, aquellos archivos con una duración inferior a los 3 segundos

"""

import os
import sys

import logging
import json

EXT_FILTER = ['.json']
SAMPLE_SEC_REFERENCE = 10 # lower than (in seconds)
SONG_SEC_REFERENCE = 30 # greater than (in seconds)

# CONFIG (add ending '/')
# JSON_SONGS_DIR = "./json-songs/"
# JSON_SAMPLES_DIR = "./json-samples/"
# JSON_SAMPLES_DIR = "./json-samples-less-5seg/"
report_file = "./report-less-10seg.txt"

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)  

Usage = "./.py [JSON_DIR] [TMP-DB.csv]"
def main():  
    if len(sys.argv) < 3:
        print("\nBad amount of input arguments\n\t", Usage, "\n")
        print(Usage)
        sys.exit(1)

    try:
        files_dir = sys.argv[1]
        csv_db_file = sys.argv[2]

        if not os.path.exists(files_dir):                         
            raise IOError("There is no sound directory")

        file_db_csv = open(csv_db_file,'r')
        print("Reading "+csv_db_file)
        file_db_dict = dict()
        for line in file_db_csv.readlines():
            # print(line)
            s_id, s_pathfile, s_json_namefile = line.split(',')
            file_db_dict[int(s_id)-1]  = s_pathfile #wARNING: hack because a bug in one tmp-db.csv file
            # file_db_dict[int(s_id)]  = s_pathfile

        error_count = 0
        for subdir, dirs, files in os.walk(files_dir):
            for input_filename in files:
                if not os.path.splitext(input_filename)[1] in EXT_FILTER:
                    continue
                tag_dir = subdir
                json_file = subdir+'/'+input_filename
                sound_id = int( input_filename.split('_')[0] )
                # print("Processed id: "+str(sound_id))

                report = open(report_file,'w')
                try:
                    # print(( "\n*** Json MIR analysis %s\n"%f ))
                    data = json.load( open(json_file,'r') )

                    # Samples detection
                    if float(data["ac:signalDuration"]) < SAMPLE_SEC_REFERENCE:
                        # pass
                        # print( input_filename, data["ac:signalDuration"], " it's a SAMPLE")
                        #report.write(str(id)+'\n') # writes id
                        # report.write(file_db_dict[sound_id]+'\n') # writes file path
                        # print(file_db_dict[sound_id]+','+json_file+','+str(data["ac:signalDuration"])+'\n') # writes file path
                        print(file_db_dict[sound_id]+'\n') # writes file path
                        # with open(JSON_SAMPLES_DIR+f, "w") as write_file:
                        #     json.dump(data, write_file)
                    # Songs detection
                    # elif float(data["ac:signalDuration"]) > SONG_SEC_REFERENCE:
                    #     pass
                        # print( input_filename, data["ac:signalDuration"], " it's a SONG")
                        #with open(JSON_SONGS_DIR+f, "w") as write_file:
                        #    json.dump(data, write_file)
                    # Residual files: not song neither samples
                    else:
                        pass
                except Exception as e:
                    # report.close()
                    print(logger.exception(e))
                    error_count += 1 
                    continue					                		                        
                report.close()

        print(("Errors: %i"%error_count))
        sys.exit( error_count )
    except Exception as e:
        logger.exception(e)
        exit(1)

if __name__ == '__main__': 
    main()
