import pyautogui as auto
import subprocess
import os
import time
import re

titleMenu = r'C:\Users\jeffr\Desktop\AutoHebuban\titleMenu.png'
end_training_image = r'C:\Users\jeffr\Desktop\AutoHebuban\AutoTrainEnd.png'
button1 = r'C:\Users\jeffr\Desktop\AutoHebuban\button1.png'
orbIcon = r'C:\Users\jeffr\Desktop\AutoHebuban\orb.png'
JewelIcon = r'C:\Users\jeffr\Desktop\AutoHebuban\jewel.png'
detailButton = r'C:\Users\jeffr\Desktop\AutoHebuban\detailButton.png'
battleButton = r'C:\Users\jeffr\Desktop\AutoHebuban\battle.png'
maxLifeButton = r'C:\Users\jeffr\Desktop\AutoHebuban\maxLife.png'
OKButton = r'C:\Users\jeffr\Desktop\AutoHebuban\OK.png'
sortieButton = r'C:\Users\jeffr\Desktop\AutoHebuban\sortie.png'
formerTeamButton = r'C:\Users\jeffr\Desktop\AutoHebuban\formerteam.png'
OKButton2 = r'C:\Users\jeffr\Desktop\AutoHebuban\OK2.png'
orbBossChallButton = r'C:\Users\jeffr\Desktop\AutoHebuban\orbBossChall.png'
homeButton = r'C:\Users\jeffr\Desktop\AutoHebuban\homeButton.png'
turnEndButton = r'C:\Users\jeffr\Desktop\AutoHebuban\turnEnd.png'
battleResult = r'C:\Users\jeffr\Desktop\AutoHebuban\battleResult.png'
againButton = r'C:\Users\jeffr\Desktop\AutoHebuban\again.png'
yameru = r'C:\Users\jeffr\Desktop\AutoHebuban\yameru.png'
toki = r'C:\Users\jeffr\Desktop\AutoHebuban\toki.png'
autoRun = r'C:\Users\jeffr\Desktop\AutoHebuban\autoRun.png'
endGame = r'C:\Users\jeffr\Desktop\AutoHebuban\endGame.png'
skipButton = r'C:\Users\jeffr\Desktop\AutoHebuban\skip.png'
notEnoughLife = r'C:\Users\jeffr\Desktop\AutoHebuban\notEnoughLife.png'
useLifeStone = r'C:\Users\jeffr\Desktop\AutoHebuban\useLifeStone.png'
dailyFree = r'C:\Users\jeffr\Desktop\AutoHebuban\dailyFree.png'
dailyGachaConfirm = r'C:\Users\jeffr\Desktop\AutoHebuban\dailyGachaConfirm.png'
okButtonDaily = r'C:\Users\jeffr\Desktop\AutoHebuban\okButtonDaily.png'
auto1 = r'C:\Users\jeffr\Desktop\AutoHebuban\auto1.png'
autoFull = r'C:\Users\jeffr\Desktop\AutoHebuban\autoFull.png'
OrbBossItemPos = [[1516,445],[1517,607],[1523,776],[1523,914],[1526,850]]
OrbBossLevelPos = [[1766,277],[1770,466],[1769,661],[1765,852]]
detailPos = [[1521,366],[1517,529],[1523,690],[1631,856],[1526,473],[1513,640],[1535,813]]
BattleChar = [[168,882],[457,884],[747,879],[1017,887],[1256,884],[1501,874]]
SkillSlot = [[1108,260],[1129,431],[1117,634],[1137,740]]
turnEndPos = [1752,885]
regularRetryInterval = 0.5

def searchButton(image,confidence,retry=-1,clickit = False):
    time.sleep(0.5)
    try:
        button = auto.locateCenterOnScreen(image,confidence=confidence)
        if clickit:
            auto.click(button)
        print('image found')
        return button.x,button.y
    except auto.ImageNotFoundException:
        print(image,' not found')
        if retry > -1:
            time.sleep(retry)
            searchButton(image,confidence,retry)
        return None
    
def wait(waitTime = 0.5):
    if waitTime > 1:
        for i in range(waitTime):
            time.sleep(1)
            print(i)
    else:
        time.sleep(waitTime)

def dailyGacha():
    pos = searchButton(dailyFree,0.7)
    if pos is not None:
        auto.click(pos)
        searchButton(dailyGachaConfirm,0.7,1,True)
        wait(4)
        okButton = searchButton(okButtonDaily,0.7)
        while not okButton:
            wait(1)
            auto.click(1,1)
            okButton = searchButton(okButtonDaily,0.7)
        auto.click(okButton)
    else:
        return False

def handleBeforeHomePage(daily):
    inMainPage = False
    while not inMainPage:
        print(tryExitAutoRun(),' onExitAutoRun')
        if daily:
            print(dailyGacha(),' onDailyGacha')
        print(trySkip(),' onSkippingWhatever')
        inMainPage = searchButton(button1,confidence=0.6)
        time.sleep(regularRetryInterval)
        auto.click(1,1) # incase missed to skip battle result

def setSkill(slot,skill):
    slot,skill = int(slot),int(skill)
    auto.click(BattleChar[slot-1])
    wait(0.1)

    auto.click(SkillSlot[skill-1])

def switchPos(firstChr,SecondChr):
    firstChr,SecondChr = int(firstChr),int(SecondChr)
    auto.click(BattleChar[firstChr-1])
    wait()
    auto.click(BattleChar[SecondChr-1])
    
def turnEnd():
    auto.click(turnEndPos)
    time.sleep(1)

def trySkip():
    pos = searchButton(skipButton,confidence=0.7)
    if pos is not None:
        auto.click(pos)
        return True
    else:
        return False

def tryExitAutoRun():
    pos = searchButton(end_training_image,confidence=0.7)
    if pos is not None:
        time.sleep(regularRetryInterval)
        print('clicking at',pos)
        auto.click(pos)
        return True
    else:
        return False

def teamSelection(TeamSlot = 1,Former = True):
    wait(1)
    if Former:
        searchButton(formerTeamButton,0.7,1,True)
        searchButton(OKButton2,0.7,1,True)
        wait(1)
    searchButton(sortieButton,0.7,1,True)

def enterOrbBoss(Target,Color,Level):
    searchButton(button1,0.6,regularRetryInterval,True)
    searchButton(orbIcon,0.7,regularRetryInterval,True)
    wait()
    match Target:
        case 0:
            auto.click(482,242)
        case 1:
            auto.click(961,267)
        case 2:
            auto.click(1455,270)
    if Color > 4:
        auto.moveTo(1521,366)
        for i in range (5):
            auto.scroll(-10)
    wait()
    auto.click(OrbBossItemPos[Color-1])
    print(OrbBossItemPos[Color-1])
    wait(7)

    searchButton(homeButton,0.9,regularRetryInterval)

    auto.click(685,509)
    wait(1)

    auto.click(OrbBossLevelPos[Level-1])
    searchButton(orbBossChallButton,0.7,1,True)
    if Level >= 4: # if level 4
        searchButton(OKButton,0.7,1,True)
    searchButton(maxLifeButton,0.7,1,True)
    searchButton(OKButton,0.7,1,True)
    if searchButton(notEnoughLife,0.7):
        searchButton(OKButton,0.7,1,True)
        searchButton(useLifeStone,0.7,regularRetryInterval,True) # only Use LifeStone for now
        searchButton(OKButton,0.7,1,True)
        wait(1)
        searchButton(OKButton,0.7,1,True)
    # searchButton(formerTeamButton,0.7,1,True)
    # searchButton(OKButton2,0.7,1,True)
    # wait(1)
    # searchButton(sortieButton,0.7,1,True)
    # auto.click()
    teamSelection(1,True)

def enterJewel(Color,Level):
    searchButton(button1,confidence=0.6,retryAfter=regularRetryInterval,clickit=True)
    searchButton(JewelIcon,confidence=0.7,retry=regularRetryInterval,clickit=True)

    if Color > 3:
        auto.moveTo(1521,366)
        for i in range (10):
            auto.scroll(-10)
    time.sleep(1)
    auto.click(detailPos[Color])

    time.sleep(1)

    if Level > 3:
        auto.moveTo(1521,366)
        for i in range (10):
            auto.scroll(-10)

    auto.click(detailPos[Level])

    searchButton(battleButton,0.7,1,True)
    searchButton(maxLifeButton,0.7,1,True)
    searchButton(OKButton,0.7,1,True)
    # searchButton(formerTeamButton,0.7,1,True)
    # searchButton(OKButton2,0.7,1,True)
    # wait(1)
    # searchButton(sortieButton,0.7,1,True)
    teamSelection(1,True)

def battleInstruction(isAuto):
    if not isAuto:
        file = open('BattleStepPreset.txt','r')
        for line in file.readlines():
            wait(5)
            searchButton(turnEndButton,0.9,1)
            commands = line.split()
            for command in commands:

                SetSkill = re.search('^C[1-6]S[1-9]',command)
                Swap = re.search('^C[1-6]C[1-6]',command)
                if re.search('^T\d',command):
                    print('Turn',command[1:])
                    continue
                if SetSkill:
                    print('SetSkill',command[1],command[3])
                    setSkill(command[1],command[3])
                    wait()
                    continue
                if Swap:
                    print('Swap',command[1],command[3])
                    switchPos(command[1],command[3])
                    wait()
                    continue
                if command == 'TE':
                    print('TurnEnd')
                    turnEnd()
                    continue
                if command == 'BE':
                    break
                wait()
        file.close()
    else:
        searchButton(turnEndButton,0.7,1)
        searchButton(auto1,0.7,1,True)
        wait()
        searchButton(autoFull,0.7,1,True)

class autoHvbn:
    def __init__(self):
        pass

    def goAutoRun(self):
        self.clickSpecific(button1,0.7,1)
        self.clickSpecific(toki,0.7,1)
        self.clickSpecific(autoRun,0.7,1)
        self.clickSpecific(OKButton2,0.7,1)
        self.clickSpecific(endGame,0.7,1)
        self.clickSpecific(OKButton,0.7,1)

    def launchApplication(daily):
        cwd = os.getcwd()
        os.chdir(r'C:\Users\jeffr\Desktop')
        subprocess.call('ヘブンバーンズレッド.url', shell = True)
        os.chdir(cwd)
        wait(5)
        searchButton(titleMenu,confidence=0.9,retry=0.5)
        wait(1)
        auto.click(1000,800)
        handleBeforeHomePage(daily)

    def enterBattleHandler(self,target,color,Level,time,instruction):
        counter = 0
        while counter <= time:
            if 0<target<=5:
                enterJewel(target,Level)
            else:
                enterOrbBoss(target,color,Level)
            battleInstruction(not instruction)
            counter +=5
            pos = searchButton(battleResult,0.9,2)
            auto.click(pos)
            time.sleep(0.1)
            auto.click()
            time.sleep(0.1)
            auto.click()
            if counter >= time:
                pos = searchButton(againButton,0.9,2)
                auto.click(pos)
        pos = searchButton(yameru,0.9,2)
        auto.click(pos)
        if target>5:
            pos = searchButton(homeButton,0.9)
            while not pos:
                wait(1)
                auto.click(1,1)
                pos = searchButton(homeButton,0.9)
            auto.click(pos)
            searchButton(OKButton,0.7,1,clickit=True)

