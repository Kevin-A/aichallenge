import sys
import configparser

apiKey = sys.argv[1]
iniFile = "../aichallenge.ini"

parser = configparser.ConfigParser()
parser.read(iniFile)
parser["hce"]["apiKey"] = str(apiKey)
parser.write(open(iniFile, "w"))