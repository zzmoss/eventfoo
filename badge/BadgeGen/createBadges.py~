#
#  Copyright (c) 2007 Silver Stripe Software Pvt Ltd
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#
#  Contributions and bug reports are welcome. Send an email to
#  siddharta at silverstripesoftware dot com
#

from PIL import Image, ImageDraw, ImageFont
import os
from csvimport import CsvReader

#####################################################
######## User Defined Values ########################
#####################################################
NAME_COLOR = "#ffffff"
COMPANY_COLOR = "#ff2b06"
ID_COLOR = "#ffffff"
FOLD_COLOR = "#000000"


class BadgeImage(object):
    def __init__(self, filename, fontname):
        self.img = Image.open(filename)
        self.draw = ImageDraw.Draw(self.img)
        self.width = int(self.img.size[0]*0.9)
        self.fontname = fontname

    def drawAlignedText(self, pos, text, (font, color), xtransform, ytransform):
        width,height = font.getsize(text)
        xpos = xtransform(pos[0], width)
        ypos = ytransform(pos[1], height)
        self.draw.text((xpos, ypos), text, fill=color, font=font)

    def drawCenteredText(self, pos, text, font):
        self.drawAlignedText(pos, text, font, lambda x,w:x-w/2, lambda y,h:y-h/2)

    def getFitSize(self, startsize, text):
        size = startsize
        font = ImageFont.truetype(self.fontname, size*300/72)
        textwidth, textheight = font.getsize(text)
        while textwidth > self.width:
            size -= 1
            font = ImageFont.truetype(self.fontname, size*300/72)
            textwidth, textheight = font.getsize(text)
        return size

    def drawPerson(self, name, color, startsize):
        linepos = (self.img.size[0]/2, 240)
        line1pos = (self.img.size[0]/2, 150)
        line2pos = (self.img.size[0]/2, 320)
        if name.find(" ") >= 0:
            firstname, rest = name.split(" ", 1)
        else:
            firstname, rest = (name, "")
        if rest != "":
            personFont = ImageFont.truetype(self.fontname, self.getFitSize(startsize, firstname)*300/72)
            self.drawCenteredText(line1pos, firstname, (personFont, color))
            personFont = ImageFont.truetype(self.fontname, self.getFitSize(startsize, rest)*300/72)
            self.drawCenteredText(line2pos, rest, (personFont, color))
        else:
            personFont = ImageFont.truetype(self.fontname, self.getFitSize(startsize, name)*300/72)
            self.drawCenteredText(linepos, name, (personFont, color))

    def drawCompany(self, name, color, startsize):
        pos = (self.img.size[0]/2, 500)
        font = ImageFont.truetype(self.fontname, self.getFitSize(startsize, name)*300/72)
        self.drawCenteredText(pos, name, (font, color))

    def drawId(self, id, color):
        pos = (50, 50)
        font = ImageFont.truetype(self.fontname, 8*300/72)
        self.drawCenteredText(pos, id, (font, color))


    def save(self, filename, color, doubleSided=False):
        if not doubleSided:
            self.img.save(filename)
            return

        newimg = Image.new("RGB", (self.img.size[0]*2+20, self.img.size[1]), color)
        newimg.paste(self.img, (0,0))
        newimg.paste(self.img, (self.img.size[0]+20,0))
        newimg.save(filename)


class DataFileReader(object):
    def __init__(self, filename):
        fp = open(filename)
        self.content = fp.read()
        fp.close()

    def getData(self):
        reader = CsvReader(self.content)
        reader.setColumnAlias(0, "fname")
        reader.setColumnAlias(1, "lname")
        reader.setColumnAlias(2, "company")
        reader.setColumnAlias(3, "id")
        for row in reader.rows():
            name = row.fname + " " + row.lname
            company = row.company
            id = row.id
            name = name.title()
            # For company names that start with * we dont convert
            # to title case. This is helpful for acronym names.
            # Eg: IBM should not become Ibm, so we mark it as *IBM
            # in the file
            if not company.startswith("*"):
                company = company.title()
            else:
                # If name starts with * then remove the star and
                # take the rest as the company name
                company = company[1:]
            yield (id, name.title(), company)

import sys


class BadgeMaker(object):

    def __init__(self, fontname = "Trebucbd.ttf", template = "badge_template_black.png", namecol = "white", compcol = "red", idcol = "white", foldcol = "black", filenames = ["sample"], nfs = 45, cfs = 26):
        self.filenames = filenames
        self.fontname = fontname
        self.template = template
        self.namecol = namecol
        self.compcol = compcol
        self.idcol = idcol
        self.foldcol = foldcol
        self.namefontsize = nfs
        self.compfontsize = cfs
                   
    # I know single line funcs suck but "I shouldn't ditch Java for atleast an year" :P

    def setFont(self, name):
        self.fontname = name

    def setBgColor(self, col):
        if col == "white":
            self.template = "badge_template_white.png"
        elif col == "black":
            self.template = "badge_template_black.png"
           
    def setNameColor(self, col):
        self.namecol = col

    def setCompanyColor(self, col):
        self.compcol = col

    def setIdColor(self, col):
        self.idcol = col

    def setFoldColor(self, col):   
        self.foldcol = col

    def generateBadges(self):
        self.count = 0
        for filename in self.filenames:
            self.reader = DataFileReader(filename + ".csv")
            if not os.path.exists(filename):
                os.makedirs(filename)
            for id, name, company in self.reader.getData():
                print id, name, company
                self.badge = BadgeImage(self.template, self.fontname)
                self.badge.drawPerson(name, self.namecol, self.namefontsize)
                self.badge.drawCompany(company, self.compcol, self.compfontsize)
                self.badge.drawId(id, self.idcol)
                self.badge.save(os.path.join(filename, "badge_" + str(id) + ".png"), self.foldcol)
                self.count += 1
        print "\n%d badges created" % (self.count)
        
