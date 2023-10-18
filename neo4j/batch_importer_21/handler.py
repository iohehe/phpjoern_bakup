#! /usr/bin/env python
#coding=utf-8
import csv

'''
@author: iohex
~~~~~~~
解决循环数据流，高地址给低地址赋值
'''

class phpJoernHandler(object):
    def __init__(self):
        cpg_file = 'cpg_edges.csv'
        self._cpg = self.loadCSVFile(cpg_file)
        _res = self.working()
        self.saveCSVFile(cpg_file, _res)


    def loadCSVFile(self, cpg_file):
        _cpg = []
        with open(cpg_file, 'r') as csv_file:
            all_lines = csv.reader(csv_file)
            for l in all_lines:
                _cpg.append(l)
        return _cpg

    
    def saveCSVFile(self, cpg_file, _res):
        with open(cpg_file, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter='\t')
            for i in _res:
                writer.writerow(i)
        print("--------------- Python handler exectuion Done")

    def working(self):
        control_list = []
        reaches_list = []
        for l in self._cpg:
            format_line = l[0].split('\t')
            if format_line[2] == 'REACHES':
                reaches_list.append(format_line)
            else:
                control_list.append(format_line)

        # get the id(start_id, end_id) of the reaches
        work_list = [[i[0], i[1]] for i in reaches_list]
        print(work_list)
        # find the start_id is higher than the end_id and remove them
        _remove = []
        for i, r in enumerate(work_list):
            _start = r[0]
            _end = r[1]

            if int(_start) == int(_end): #exception
                print("Exception Equation: {} => {}".format(_start, _end))
                _remove.append(i) 
            if int(_start) > int(_end): #exception
                print("Exception Higher: {} => {}".format(_start, _end))
                _remove.append(i) 
        
        # delete the exceptions from the reaches list
        for d in sorted(_remove, reverse=True):
            del reaches_list[d]

        return_list = control_list+reaches_list
        return return_list


if __name__=='__main__':
    _handle = phpJoernHandler()
