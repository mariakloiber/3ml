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
        'c4':14,
        'd4':15,
        'e4':16,
        'f4':17,
        'g4':18,
        'a5':19,
        'b5':20,
        'c5':21,
        'd5':22,
        'e5':23,
        'f5':24,
        'g5':25,
        'a6':26,
        'QR':27
}

def drawfunction(x,y,note_id,c):
        if note_id == 1 or note_id == 14:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y-27)+"),Point("+str(x+10)+","+str(y-22)+"))\n")
                out_program.write("new_note_line = Rectangle(Point("+str(x-2)+","+str(y-25)+"),Point("+str(x+12)+","+str(y-24)+"))\n")
                out_program.write('''new_note_line.setFill("black")\n''')
                if note_id == 1:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_line.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y-23)+"),Point("+str(x+10)+","+str(y+4)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 2 or note_id == 15:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y-23)+"),Point("+str(x+10)+","+str(y-18)+"))\n")
                if note_id == 2:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y-19)+"),Point("+str(x+10)+","+str(y+8)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 3 or note_id == 16:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y-18)+"),Point("+str(x+10)+","+str(y-13)+"))\n")
                if note_id == 3:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y-14)+"),Point("+str(x+10)+","+str(y+13)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 4 or note_id == 17:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y-14)+"),Point("+str(x+10)+","+str(y-9)+"))\n")
                if note_id == 4:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y-10)+"),Point("+str(x+10)+","+str(y+17)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 5 or note_id == 18:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y-9)+"),Point("+str(x+10)+","+str(y-4)+"))\n")
                if note_id == 5:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y-5)+"),Point("+str(x+10)+","+str(y+22)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 6 or note_id == 19:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y-5)+"),Point("+str(x+10)+","+str(y)+"))\n")
                if note_id == 6:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y-1)+"),Point("+str(x+10)+","+str(y+26)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 7 or note_id == 20:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y)+"),Point("+str(x+10)+","+str(y+5)+"))\n")
                if note_id == 7:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+9)+","+str(y+4)+"),Point("+str(x+10)+","+str(y+31)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 8 or note_id == 21:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y+4)+"),Point("+str(x+10)+","+str(y+9)+"))\n")
                if note_id == 8:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+1)+","+str(y+5)+"),Point("+str(x)+","+str(y-22)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 9 or note_id == 22:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y+8)+"),Point("+str(x+10)+","+str(y+13)+"))\n")
                if note_id == 9:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+1)+","+str(y+9)+"),Point("+str(x)+","+str(y-18)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 10 or note_id == 23:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y+13)+"),Point("+str(x+10)+","+str(y+18)+"))\n")
                if note_id == 10:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+1)+","+str(y+14)+"),Point("+str(x)+","+str(y-13)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 11 or note_id == 24:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y+17)+"),Point("+str(x+10)+","+str(y+22)+"))\n")
                if note_id == 11:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+1)+","+str(y+18)+"),Point("+str(x)+","+str(y-9)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 12 or note_id == 25:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y+22)+"),Point("+str(x+10)+","+str(y+27)+"))\n")
                if note_id == 12:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+1)+","+str(y+23)+"),Point("+str(x)+","+str(y-4)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")

        if note_id == 13 or note_id == 26:
                out_program.write("new_note = Oval(Point("+str(x)+","+str(y+26)+"),Point("+str(x+10)+","+str(y+31)+"))\n")
                out_program.write("new_note_line = Rectangle(Point("+str(x-2)+","+str(y+28)+"),Point("+str(x+12)+","+str(y+29)+"))\n")
                out_program.write('''new_note_line.setFill("black")\n''')
                if note_id == 13:
                	out_program.write('''new_note.setFill("black")\n''')
                out_program.write("new_note.draw(win)\n")
                out_program.write("new_note_line.draw(win)\n")
                out_program.write("new_note_stem = Rectangle(Point("+str(x+1)+","+str(y+27)+"),Point("+str(x)+","+str(y)+"))\n")
                out_program.write('''new_note_stem.setFill("black")\n''')
                out_program.write("new_note_stem.draw(win)\n")
        
        if note_id == 27:
        		out_program.write('''rest = Image(Point('''+str(x)+''','''+str(y+5)+'''), "resize_rest.gif")\n''')
        		out_program.write("rest.draw(win)\n")

        if c == 4:
        		out_program.write("bar_line = Rectangle(Point("+str(x+17)+","+str(y-15)+"), Point("+str(x+17)+","+str(y+19)+"))\n")
        		out_program.write('''bar_line.setFill("black")\n''')
        		out_program.write("bar_line.draw(win)\n")

name_of_in_program = sys.argv[1]
name_of_in_program = name_of_in_program + ".txt"

in_program = open(name_of_in_program,"r")
title = in_program.readline()
title = title[:len(title)-1]
title = title + ".py"

if os.path.isfile(title):
        os.remove(title)

out_program = open(title,"w")
title = title[:len(title)-3]

is_start = in_program.readline()
if is_start == "start\n" or is_start == "Start\n" or is_start == "START\n":
        out_program.write("import os\n")
        out_program.write("from graphics import *\n")
        out_program.write("win_width = 612\n")
        out_program.write("win_height = 768\n")
        out_program.write('''win = GraphWin("'''+title+'''", win_width, win_height)\n''')
        out_program.write("win.setCoords(0,0,win_width,win_height)\n")
        out_program.write('\n')
        out_program.write('''blank = Image(Point(306,384),"blank.gif")\n''')
        out_program.write("blank.draw(win)\n")
        out_program.write("\n")
        started = True
else:
        print("ERROR ON START")
        started = False

x_acc = 25
y_acc = 735

if started:
        current_line = in_program.readline()
        count = 0

        while current_line != "":
                id_list = []
                index = 0
                x_acc += 25

                while current_line[index+2] != '\n':
                        note = current_line[index] + current_line[index+1]
                        id_list.append(note_dictionary[note])
                        index += 2
                note = current_line[index] + current_line[index+1]
                id_list.append(note_dictionary[note])
                
                if id_list[0]==27 or id_list[0]<=13:
                	count += 1
                else:
                	count += 2
                
                for i in id_list:
                	drawfunction(x_acc,y_acc,i,count)

                if count == 4:
                	count = 0

                if count >= 4:
                	out_program.write('''print("MEASURE ERROR! CHECK YOUR COUNTING!!!")\n''')

                if x_acc == 575:
                        x_acc = 25
                        y_acc -= 70
                current_line = in_program.readline()

if started:
        out_program.write("win.getMouse()\n")
        out_program.write("win.close()\n")

out_program.close()

in_program.close()
