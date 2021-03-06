import os
from graphics import *
win_width = 612
win_height = 768
win = GraphWin("Beethoven", win_width, win_height)
win.setCoords(0,0,win_width,win_height)

blank = Image(Point(306,384),"blank.gif")
blank.draw(win)

new_note = Oval(Point(50,717),Point(60,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(59,721),Point(60,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(75,717),Point(85,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(84,721),Point(85,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(100,721),Point(110,726))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(109,725),Point(110,752))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(125,726),Point(135,731))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(134,730),Point(135,757))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(142,720), Point(142,754))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(150,726),Point(160,731))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(159,730),Point(160,757))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(175,721),Point(185,726))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(184,725),Point(185,752))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(200,717),Point(210,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(209,721),Point(210,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(225,712),Point(235,717))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(234,716),Point(235,743))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(242,720), Point(242,754))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(250,708),Point(260,713))
new_note_line = Rectangle(Point(248,710),Point(262,711))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(259,712),Point(260,739))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(275,708),Point(285,713))
new_note_line = Rectangle(Point(273,710),Point(287,711))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(284,712),Point(285,739))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(300,712),Point(310,717))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(309,716),Point(310,743))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(325,717),Point(335,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(334,721),Point(335,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(342,720), Point(342,754))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(350,717),Point(360,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(359,721),Point(360,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(375,712),Point(385,717))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(384,716),Point(385,743))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(400,712),Point(410,717))
new_note.draw(win)
new_note_stem = Rectangle(Point(409,716),Point(410,743))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(417,720), Point(417,754))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(425,717),Point(435,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(434,721),Point(435,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(450,717),Point(460,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(459,721),Point(460,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(475,721),Point(485,726))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(484,725),Point(485,752))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(500,726),Point(510,731))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(509,730),Point(510,757))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(517,720), Point(517,754))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(525,726),Point(535,731))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(534,730),Point(535,757))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(550,721),Point(560,726))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(559,725),Point(560,752))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(575,717),Point(585,722))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(584,721),Point(585,748))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(50,642),Point(60,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(59,646),Point(60,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(67,650), Point(67,684))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(75,638),Point(85,643))
new_note_line = Rectangle(Point(73,640),Point(87,641))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(84,642),Point(85,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(100,638),Point(110,643))
new_note_line = Rectangle(Point(98,640),Point(112,641))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(109,642),Point(110,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(125,642),Point(135,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(134,646),Point(135,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(150,647),Point(160,652))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(159,651),Point(160,678))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(167,650), Point(167,684))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(175,642),Point(185,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(184,646),Point(185,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(200,638),Point(210,643))
new_note_line = Rectangle(Point(198,640),Point(212,641))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(209,642),Point(210,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(225,638),Point(235,643))
new_note_line = Rectangle(Point(223,640),Point(237,641))
new_note_line.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(234,642),Point(235,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(242,650), Point(242,684))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(250,642),Point(260,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(259,646),Point(260,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(275,642),Point(285,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(284,646),Point(285,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(300,647),Point(310,652))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(309,651),Point(310,678))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(325,638),Point(335,643))
new_note_line = Rectangle(Point(323,640),Point(337,641))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(334,642),Point(335,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(342,650), Point(342,684))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(350,642),Point(360,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(359,646),Point(360,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(375,647),Point(385,652))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(384,651),Point(385,678))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(400,651),Point(410,656))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(409,655),Point(410,682))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(425,647),Point(435,652))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(434,651),Point(435,678))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(442,650), Point(442,684))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(450,638),Point(460,643))
new_note_line = Rectangle(Point(448,640),Point(462,641))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(459,642),Point(460,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(475,642),Point(485,647))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(484,646),Point(485,673))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(500,647),Point(510,652))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(509,651),Point(510,678))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(525,651),Point(535,656))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(534,655),Point(535,682))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(542,650), Point(542,684))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(550,647),Point(560,652))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(559,651),Point(560,678))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(575,638),Point(585,643))
new_note_line = Rectangle(Point(573,640),Point(587,641))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(584,642),Point(585,669))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(50,572),Point(60,577))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(59,576),Point(60,603))
new_note_stem.setFill("black")
new_note_stem.draw(win)
rest = Image(Point(75,600), "resize_rest.gif")
rest.draw(win)
bar_line = Rectangle(Point(92,580), Point(92,614))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(100,586),Point(110,591))
new_note.draw(win)
new_note_stem = Rectangle(Point(109,590),Point(110,617))
new_note_stem.setFill("black")
new_note_stem.draw(win)
rest = Image(Point(125,600), "resize_rest.gif")
rest.draw(win)
new_note = Oval(Point(150,577),Point(160,582))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(159,581),Point(160,608))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(167,580), Point(167,614))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(175,577),Point(185,582))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(184,581),Point(185,608))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(200,581),Point(210,586))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(209,585),Point(210,612))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(225,586),Point(235,591))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(234,590),Point(235,617))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(250,586),Point(260,591))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(259,590),Point(260,617))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(267,580), Point(267,614))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(275,581),Point(285,586))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(284,585),Point(285,612))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(300,577),Point(310,582))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(309,581),Point(310,608))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(325,572),Point(335,577))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(334,576),Point(335,603))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(350,568),Point(360,573))
new_note_line = Rectangle(Point(348,570),Point(362,571))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(359,572),Point(360,599))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(367,580), Point(367,614))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(375,568),Point(385,573))
new_note_line = Rectangle(Point(373,570),Point(387,571))
new_note_line.setFill("black")
new_note.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(384,572),Point(385,599))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(400,572),Point(410,577))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(409,576),Point(410,603))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(425,577),Point(435,582))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(434,581),Point(435,608))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(450,572),Point(460,577))
new_note.setFill("black")
new_note.draw(win)
new_note_stem = Rectangle(Point(459,576),Point(460,603))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(467,580), Point(467,614))
bar_line.setFill("black")
bar_line.draw(win)
new_note = Oval(Point(475,568),Point(485,573))
new_note_line = Rectangle(Point(473,570),Point(487,571))
new_note_line.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(484,572),Point(485,599))
new_note_stem.setFill("black")
new_note_stem.draw(win)
new_note = Oval(Point(500,568),Point(510,573))
new_note_line = Rectangle(Point(498,570),Point(512,571))
new_note_line.setFill("black")
new_note.draw(win)
new_note_line.draw(win)
new_note_stem = Rectangle(Point(509,572),Point(510,599))
new_note_stem.setFill("black")
new_note_stem.draw(win)
bar_line = Rectangle(Point(517,580), Point(517,614))
bar_line.setFill("black")
bar_line.draw(win)
win.getMouse()
win.close()
