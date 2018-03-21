import os
import os.path
import sys
from graphics import *

note_dictionary = {
	'C4':1,
	'D4':2,
	'E4':3,
	'F4':4,
	'G4':5,
	'A5':6,
	'B5':7,
	'C5':8,
	'D5':9,
	'E5':10,
	'F5':11,
	'G5':12,
	'A6':13,
        '_': 27
}

win_width = 612
win_height = 768
win = GraphWin("Sheet Music", win_width, win_height)
win.setCoords(0,0,win_width,win_height)

blank = Image(Point(306,384), "blank.gif")
blank.draw(win)


###C4###
#test_note1 = Oval(Point(75,708),Point(85,713))
#test_note1line = Rectangle(Point(73,710),Point(87,711))
#test_note1line.setFill("black")
#test_note1.setFill("black")
#test_note1.draw(win)
#test_note1line.draw(win)

###D4###
#test_note2 = Oval(Point(50,712),Point(60,717))
#test_note2.setFill("black")
#test_note2.draw(win)

###E4###
#test_note3 = Oval(Point(75,717),Point(85,722))
#test_note3.setFill("black")
#test_note3.draw(win)

###F4###
#test_note4 = Oval(Point(50,721),Point(60,726))
#test_note4.setFill("black")
#test_note4.draw(win)

###G4###
#test_note5 = Oval(Point(75,726),Point(85,731))
#test_note5.setFill("black")
#test_note5.draw(win)

###A5###
#test_note6 = Oval(Point(50,730),Point(60,735))
#test_note6.setFill("black")
#test_note6.draw(win)

###B5###
#test_note7 = Oval(Point(75,735),Point(85,740))
#test_note7.setFill("black")
#test_note7.draw(win)



###C5###
#test_note8 = Oval(Point(50,739),Point(60,744))
#test_note8.setFill("black")
#test_note8.draw(win)

###D5###
#test_note9 = Oval(Point(75,743),Point(85,748))
#test_note9.setFill("black")
#test_note9.draw(win)

###E5###
#test_note10 = Oval(Point(50,748),Point(60,753))
#test_note10.setFill("black")
#test_note10.draw(win)

###F5###
#test_note11 = Oval(Point(75,752),Point(85,757))
#test_note11.setFill("black")
#test_note11.draw(win)

###G5###
#test_note12 = Oval(Point(50,757),Point(60,762))
#test_note12.setFill("black")
#test_note12.draw(win)

###A6###
#test_note13 = Oval(Point(75,761),Point(85,766))
#test_note13line = Rectangle(Point(73,763), Point(87,764))
#test_note13.setFill("black")
#test_note13line.setFill("black")
#test_note13.draw(win)
#test_note13line.draw(win)

###ML1###
#test_line = Rectangle(Point(137, 760), Point(138, 760))
#test_line.setFill("black")
#test_line.draw(win)

xacc = 100
# ! yacc needs to start at 735, move down by 70 for each line
# ! xacc from 50 to 575 per line
# ! noteid from 1 to 13
#count = 0

def drawfunction(xacc,yacc, noteid):
    if noteid == 1: #draw c4
        new_note = Oval(Point(xacc,(yacc-27)),Point((xacc + 10),(yacc-22)))
        new_note_line = Rectangle(Point((xacc - 2),(yacc-25)),Point((xacc + 12),(yacc-24)))
        new_note_stem = Rectangle(Point((xacc+9), (yacc-23)), Point((xacc + 10), (yacc + 4)))
        new_note_line.setFill("black")
        new_note_stem.setFill("black")
        new_note.setFill("black")
        new_note.draw(win)
        new_note_line.draw(win)
        new_note_stem.draw(win)

    if noteid == 2: #draw d4
        new_note = Oval(Point(xacc,(yacc - 23)),Point((xacc + 10),(yacc - 18)))
        new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-19)), Point((xacc + 10), (yacc + 8)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 3:#e4
        new_note = Oval(Point(xacc,(yacc-18)),Point((xacc + 10),(yacc - 13)))
        new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-14)), Point((xacc + 10), (yacc + 13)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 4:#f4
        test_note = Oval(Point(xacc,(yacc - 14)),Point((xacc + 10),(yacc - 9)))
        test_note.setFill("black")
        test_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-10)), Point((xacc + 10), (yacc + 17)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 5:#g4
        new_note = Oval(Point(xacc,(yacc - 9)),Point((xacc+10),(yacc - 4)))
        new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-5)), Point((xacc + 10), (yacc + 22)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 6:#a5
        new_note =  Oval(Point(xacc,(yacc - 5)),Point((xacc + 10), yacc))
        new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-1)), Point((xacc + 10), (yacc + 30)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 7:#b5#################
        new_note = Oval(Point(xacc,yacc),Point((xacc + 10),(yacc + 5)))
        new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+9), (yacc+4)), Point((xacc + 10), (yacc + 31)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 8:#c5
        new_note =  Oval(Point(xacc,(yacc + 4)),Point((xacc + 10),(yacc + 9)))
        new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 5)), Point((xacc), (yacc - 22)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 9:#d5
        new_note =  Oval(Point(xacc,(yacc + 8)),Point((xacc + 10),(yacc + 13)))
        new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 9)), Point((xacc), (yacc - 18)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 10:#e5
        new_note = Oval(Point(xacc,(yacc + 13)),Point((xacc + 10),(yacc + 18)))
        new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 14)), Point((xacc), (yacc - 13)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 11:#f5
        new_note = Oval(Point(xacc,(yacc + 17)),Point((xacc + 10),(yacc + 22)))
        new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 18)), Point((xacc), (yacc - 9)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 12:#g5
        new_note = Oval(Point(xacc,(yacc + 22)),Point((xacc + 10),(yacc + 27)))
        new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 23)), Point((xacc), (yacc - 4)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 13:#a6
        new_note = Oval(Point(xacc,(yacc + 26)), Point((xacc + 10),(yacc + 31)))
        new_noteline = Rectangle(Point((xacc - 2),(yacc + 28)), Point((xacc + 12),(yacc + 29)))
        new_note.setFill("black")
        new_noteline.setFill("black")
        new_note.draw(win)
        new_noteline.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 27)), Point((xacc), (yacc)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

    if noteid == 27: #rest
        rest = Image(Point(xacc, (yacc + 5)), "resize_rest.gif")
        rest.draw(win)

    if noteid == 14:#c4 halfnote
        new_note = Oval(Point(xacc,(yacc-27)),Point((xacc + 10),(yacc-22)))
        new_note_line = Rectangle(Point((xacc - 2),(yacc-25)),Point((xacc + 12),(yacc-24)))
        new_note_stem = Rectangle(Point((xacc+9), (yacc-23)), Point((xacc + 10), (yacc + 4)))
        new_note_line.setFill("black")
        new_note_stem.setFill("black")
        #new_note.setFill("black")
        new_note.draw(win)
        new_note_line.draw(win)
        new_note_stem.draw(win)
        #count += 1


    if noteid == 15:#d4 halfnote
        new_note = Oval(Point(xacc,(yacc - 23)),Point((xacc + 10),(yacc - 18)))
        #new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-19)), Point((xacc + 10), (yacc + 8)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1
    
    if noteid == 16:#e4 halfnote
        new_note = Oval(Point(xacc,(yacc-18)),Point((xacc + 10),(yacc - 13)))
        #new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-14)), Point((xacc + 10), (yacc + 13)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1 


    if noteid == 17:#f4
        test_note = Oval(Point(xacc,(yacc - 14)),Point((xacc + 10),(yacc - 9)))
        #test_note.setFill("black")
        test_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-10)), Point((xacc + 10), (yacc + 17)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1

    if noteid == 18:#g4
        new_note = Oval(Point(xacc,(yacc - 9)),Point((xacc+10),(yacc - 4)))
        #new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-5)), Point((xacc + 10), (yacc + 22)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1

    if noteid == 19:#a5
        new_note =  Oval(Point(xacc,(yacc - 5)),Point((xacc + 10), yacc))
        #new_note.setFill("black")
        new_note.draw(win)
        new_note_stem = Rectangle(Point((xacc+9), (yacc-1)), Point((xacc + 10), (yacc + 30)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1


    if noteid == 20:#b5#################
        new_note = Oval(Point(xacc,yacc),Point((xacc + 10),(yacc + 5)))
        #new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+9), (yacc+4)), Point((xacc + 10), (yacc + 31)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1


    if noteid == 21:#c5
        new_note =  Oval(Point(xacc,(yacc + 4)),Point((xacc + 10),(yacc + 9)))
        #new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 5)), Point((xacc), (yacc - 22)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1


    if noteid == 22:#d5
        new_note =  Oval(Point(xacc,(yacc + 8)),Point((xacc + 10),(yacc + 13)))
        #new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 9)), Point((xacc), (yacc - 18)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1 


    if noteid == 23:#e5
        new_note = Oval(Point(xacc,(yacc + 13)),Point((xacc + 10),(yacc + 18)))
        #new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 14)), Point((xacc), (yacc - 13)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1


    if noteid == 24:#f5
        new_note = Oval(Point(xacc,(yacc + 17)),Point((xacc + 10),(yacc + 22)))
        #new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 18)), Point((xacc), (yacc - 9)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1


    if noteid == 25:#g5
        new_note = Oval(Point(xacc,(yacc + 22)),Point((xacc + 10),(yacc + 27)))
        #new_note.setFill("black")
        new_note.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 23)), Point((xacc), (yacc - 4)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)
        #count += 1


    if noteid == 26:#a6
        new_note = Oval(Point(xacc,(yacc + 26)), Point((xacc + 10),(yacc + 31)))
        new_noteline = Rectangle(Point((xacc - 2),(yacc + 28)), Point((xacc + 12),(yacc + 29)))
        #new_note.setFill("black")
        new_noteline.setFill("black")
        new_note.draw(win)
        new_noteline.draw(win)

        new_note_stem = Rectangle(Point((xacc+1), (yacc + 27)), Point((xacc), (yacc)))
        new_note_stem.setFill("black")
        new_note_stem.draw(win)

#    if note == 4: #measure line 1
#        new_line = Rectangle(Point(), Point())
#        new_line.setFill("black")
#        new_line.draw(win)

'''
drawfunction(xacc, 735, 14)
drawfunction(125, 735, 2)
drawfunction(150, 735, 3)
drawfunction(175, 735, 4)
drawfunction(200, 735, 5)
drawfunction(225, 735, 6)
drawfunction(250, 735, 7)
drawfunction(275, 735, 8)
drawfunction(300, 735, 9)
drawfunction(325, 735, 10)
drawfunction(350, 735, 11)
drawfunction(375, 735, 12)
drawfunction(400, 735, 14)
############Newline############
drawfunction(100, 665, 1)
drawfunction(125, 665, 2)
drawfunction(150, 665, 3)
drawfunction(175, 665, 4)
drawfunction(200, 665, 5)
drawfunction(225, 665, 6)
drawfunction(250, 665, 7)
drawfunction(275, 665, 8)
drawfunction(300, 665, 9)
drawfunction(325, 665, 10)
drawfunction(350, 665, 11)
drawfunction(375, 665, 12)
drawfunction(400, 665, 13)
drawfunction(415, 665, 14)
#loop to test plot on multiple lines of the sheet music
'''
i = 0
nid = 1
xacc = 50
yacc = 735
while i < 200:
    drawfunction(xacc, yacc, nid)
    i +=1
    nid += 1
    xacc += 25
    if xacc == 575:
        xacc = 50
        yacc -= 70
    if nid == 28:
        nid = 1
#'''

#drawfunction(xacc, 735, 1)
#drawfunction(125, 735, 2)
#drawfunction(150, 735, 3)
#drawfunction(175, 735, 4)
#drawfunction(200, 735, 5)
#drawfunction(225, 735, 6)
#drawfunction(250, 735, 7)
#drawfunction(275, 735, 8)
#drawfunction(300, 735, 9)
#drawfunction(325, 735, 10)
#drawfunction(350, 735, 11)
#drawfunction(375, 735, 12)
#drawfunction(400, 735, 13)
#drawfunction(100, 665, 1)
#drawfunction(125, 665, 2)
#drawfunction(150, 665, 3)
#drawfunction(175, 665, 4)
#drawfunction(200, 665, 5)
#drawfunction(225, 665, 6)
#drawfunction(250, 665, 7)
#drawfunction(275, 665, 8)
#drawfunction(300, 665, 9)
#drawfunction(325, 665, 10)
#drawfunction(350, 665, 11)
#drawfunction(375, 665, 12)
#drawfunction(400, 665, 13)

###575 is the end of the line, reset xacc to 50

win.getMouse()
win.close()
