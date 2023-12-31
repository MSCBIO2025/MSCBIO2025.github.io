#!/usr/bin/env python

import datetime, sys

'''Print out schedule.html page. Takes care of all the boilerplate so 
I can rearrange things easily.'''

start = datetime.date(2023,8,29)
end = datetime.date(2023,12,15)
lastassign = 12
noclass = {datetime.date(2023,11,21): "Thanksgiving Break", 
           datetime.date(2023,11,23): "Thanksgiving Break"}

lectures = [
("Introduction/Linux Commandline Basics",'DK',[('intro','notes/intro2023.pdf'),'bash',('reference','notes/bash_cheatsheet.pdf')]),
("Linux Commandline File Processing",'DK',['bash2']),
("Getting Started with Python",'JB',['pythonintro']),
("Control Flow and Basic Data Visualization with <a href='http://matplotlib.org/'>matplotlib</a>",'JB',['pyandplot']),
("<a href='http://www.numpy.org/'>numpy</a> Arrays",'JB',['numpy']),
("Systems Biology with <a href='http://pysb.org/'>PySB</a>",'JF',['pysb']),
("Dictionaries and Sets and Function Fitting",'JB',['numpy2dict']),
("Sequence Analysis with <a href='http://biopython.org/wiki/Biopython'>Biopython</a>",'JB',['biopython']),
("More Sequence Analysis",'JB',['seqcont']),
("EMR with <a href='http://pandas.pydata.org/'>pandas</a>",'JB',['emr']),
("Structure Analysis with <a href='http://prody.csb.pitt.edu/'>ProDy</a>",'MG',['prody1']),
("Protein Analysis Continued",'MG',['prody2']),
("Molecular Dynamics (<a href='http://www.mdanalysis.org/'>mdanalysis</a>)",'MG',['mdanalysis']),
("More Molecular Dynamics",'MG',['md2']),
("Clustering",'MG',['clustering']),
("Regular Expressions",'DK',['regex']),
("Web Services and Communication Protocols",'DK',['web']),
("From Data to Model to the World Web Web",'DK',['webprogramming']),
("Cheminformatics (<a href='http://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html'>Pybel</a>)",'DK',['cheminformatics']),
("Dimensionality Reduction",'SU',['dimred']),
("Machine Learning with <a href='http://scikit-learn.org/stable/'>sklearn</a>",'SU',['machinelearning']),
("Process Control with <a href='https://docs.python.org/3/library/subprocess.html'>subprocess</a>",'DK',['subprocess']),
("Bioimaging I",'SU',['bioimaging']),
("Bioimaging II",'SU',['bioimaging2']),
("Deep Learning",'SU',['deeplearning']),
("multiprocessing",'DK',['multiprocessing']),
("<b>Project Presentations</b>",'',[]),
("<b>Project Presentations</b>",'',[]),
("<b>Movie and Pizza",'',[])
]

print ('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta http-equiv="Cache-Control" content="no-store" />
<title>MSCBIO 2025: Schedule</title>
<link href="default.css" rel="stylesheet" type="text/css" />

</head>

<body>
<div class="main">
<h1>Schedule</h1>
<h3>Subject to change</h3>
<table width=100% style="border-collapse: collapse;">
<thead>
<th>Date</th><th>Instructor</th><th>Topic</th><th>Links</th>
</thead>
<tbody>''')

cmap = {'DK': ("#ede1f7","#dec6f5"),
        'SU': ("#fbffb3","#eff584"),
        'JB': ("#ace3af", "#76db7a"),
        'MG': ("#c6eaf7","#b0e4f7"),
        'JF': ("#f2c9ed","#f2c9ed"),
        '': ('#ffe8e8','#ffe8e8')
        }

def linkstr(links):
    '''given list of link information return html string'''
    ret = ''
    for l in links:
        if type(l) == str: #assume slides
            ret += '<a href="notes/{0}.slides.html" target="_blank">slides</a>&nbsp;<a href="https://nbviewer.org/urls/mscbio2025.net/notes/{0}.ipynb" target="_blank">notebook</a>&nbsp;'.format(l)
        else: # assume tuple of name,link
            ret += ' <a href="%s" target="_blank">%s</a>&nbsp;' % (l[1],l[0])
    return ret

day = start
lecpos = 0
assignpos = 0
while day < end and lecpos < len(lectures):
    # is is the monday of the week
    #first assignment and it's not "noclass"

    if assignpos > 0 and assignpos <= lastassign:
        if day in noclass: #no assignment on holiday
            assignpos -= 1
        else:
            print ("<tr class='A'><td>%s</td><td></td><td colspan=1>Assignment %d Due 11:59pm</td><td></td></tr>" % (day.strftime('%m/%d'), assignpos))
    assignpos += 1
    if day not in noclass:
        lecname = lectures[lecpos][0]
        instructor = lectures[lecpos][1]
        links = lectures[lecpos][2]
        print (f"<tr  style='background-color: {cmap[instructor][0]}'>")
        print ("<td>%s</td><td>%s</td><td>%s</td>" % (day.strftime('%m/%d'),instructor,lecname) )       
        print ("<td style='display: inline-block; width: 200px;'>%s</td>" % linkstr(links))
        lecpos += 1
    else:
        print ("<tr class='B'><td>%s</td><td></td><td colspan=1>%s</td><td></td></tr>" % (day.strftime('%m/%d'), noclass[day]))
        
    if lecpos >= len(lectures):
        break
        
    day += datetime.timedelta(2)
    if day not in noclass and lecpos < len(lectures):
        lecname = lectures[lecpos][0]
        instructor = lectures[lecpos][1]
        links = lectures[lecpos][2]
        print (f"<tr class='endweek' style='background-color: {cmap[instructor][1]}'>")
        print ("<td>%s</td><td>%s</td><td>%s</td>" % (day.strftime('%m/%d'),instructor,lecname))
        print ("<td style='display: inline-block; width: 200px;'>%s</td>" % linkstr(links))
        lecpos += 1
    else:
        print( "<tr class='B endweek'><td>%s</td><td></td><td colspan=1>%s</td><td></td></tr>" % (day.strftime('%m/%d'), noclass[day]))
  
    if lecpos >= len(lectures):
        break        
    day += datetime.timedelta(5)
        


print ('''</tbody>
</table>
</div>
</body>
</html>
''')
