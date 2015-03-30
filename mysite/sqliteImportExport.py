#!/usr/bin/python

import sqlite3
import getopt
import sys
import csv
import codecs
import cStringIO


class UserParams:
    def __init__(self):
        self.command = ""
        self.inputFile = ""
        self.outputFile = ""


class SqliteExport:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class SqliteImport:
    def __init__(self, inputFile, outputFile, tableName):
        self.inputFile = inputFile
        self.conn = sqlite3.connect(outputFile)
        self.tableName = tableName
        self.cur = self.conn.cursor()

    def writeRows(self):
        with open(self.inputFile, "rb") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                to_db = []
                values_string = " VALUES("
                for i in range(0, len(row)):
                    to_db = to_db + [unicode(row[i], "utf8")]
                    values_string += "?"
                    if i != len(row) - 1:
                        values_string += ","
                    else:
                        values_string += ");"
                self.cur.execute("INSERT INTO " + self.tableName + values_string, to_db)
                self.conn.commit()
        self.conn.close()

    def getNumOfColumns(self):
        ncol = 0
        f = open(self.inputFile, 'r')
        reader = csv.reader(f, delimiter=',')
        try:
            ncol = len(next(reader))
        except:
            ncol = 0
        return ncol


def main(argvs):
    argv = argvs[1:]
    userParam = UserParams()
    inputfile = ""
    outputfile = ""
    command = ""
    tableName = ""
    opts = ""
    try:
        opts, args = getopt.getopt(argv, "ht:c:i:o:", ["table=", "command=", "ifile=", "ofile="])
    except getopt.GetoptError:
        print argvs[0] + ' -c <import|export> -t <tableName> -i <inputfile> -o <outputfile>';
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print argvs[0] + ' -c <import|export> -t <tableName> -i <inputfile> -o <outputfile>';
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-c", "--command"):
            command = arg
        elif opt in ("-t", "--table"):
            tableName = arg

    if (inputfile != "") and (outputfile != "") and (command != "") and (tableName != ""):
        userParam.command = command
        userParam.inputfile = inputfile
        userParam.outputfile = outputfile
        userParam.tableName = tableName
    else:
        print argvs[0] + ' -c <import|export> -t <tableName> -i <inputfile> -o <outputfile>';
        sys.exit()
    return userParam;


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print sys.argv[0] + ' -c <import|export> -t <tableName> -i <inputfile> -o <outputfile>';
        sys.exit()
        userParam = main(sys.argv[0:])
    if userParam.command == "export":
        conn = sqlite3.connect(userParam.inputfile)
        c = conn.cursor()
        c.execute('select * from ' + userParam.tableName)
        writer = SqliteExport(open(userParam.outputfile, "wb"))
        writer.writerows(c);
    elif userParam.command == "import":
        writer = SqliteImport(userParam.inputfile, userParam.outputfile, userParam.tableName)
        writer.writeRows()