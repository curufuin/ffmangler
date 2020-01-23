#!/usr/bin/python

import re
import random
import time

class ffMangler:

    def __init__(self):
        self.profileName = "FIREFOX_PROFILE_NAME"
        self.userJS = "ENTER_HOME_FOLDER" + self.profileName + ".default/user.js"
        self.userAgentsFile = "./useragents.txt"
        self.userAgent = ""
        self.osFile = "./os.txt"
        self.os = ""
        self.fontSize = ""


    def getRandomUseragent(self):
        lines = open(self.userAgentsFile, "r").read().splitlines()
        self.userAgent = str(random.choice(lines))
        return self.userAgent

    def getRandomOS(self):
        lines = open(self.osFile, "r").read().splitlines()
        self.os = str(random.choice(lines))
        print self.os
        return self.os

    def getRandomFontSize(self):
        self.fontSize = str(random.randint(4,7))
        return self.fontSize

    def mangle(self):
        contents = open(self.userJS, "r").read()
        contents = re.sub(r'(?<=useragent\.override\"\,\s\").*?(?=\"\)\;)', str(self.userAgent), str(contents))
        contents = re.sub(r'(?<=oscpu\.override\"\,\s\").+?(?=\")', str(self.os), str(contents))
        contents = re.sub(r'[0-9]*?(?=\)\;)', str(self.fontSize), str(contents))
        open(self.userJS, "w").write(contents)

    def run(self):
        self.getRandomFontSize()
        self.getRandomOS()
        self.getRandomUseragent()
        self.mangle()

mangler = ffMangler()
mangler.run()
