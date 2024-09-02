import pyautogui as auto
import subprocess
import os
import time

# Application_monitor_position=0 # 0 for only one monitor and 1 for application is on the second monitor at right side
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

SweepMode = 'orb' # jewel or orb
SweepItem = 6
SweepLevel = -1

OrbBossSelection = 'Exo'
OrbBoss = {'Exo':0,'Sinister':1,'Amon':2}
OrbBossItem = 4
OrbBossLevel = 4

OrbBossItemPos = [[1516,445],[1517,607],[1523,776],[1631,914],[1526,850]]
OrbBossLevelPos = [[1766,277],[1770,466],[1769,661],[1765,852]]

detailPos = [[1521,366],[1517,529],[1523,690],[1631,856],[1526,473],[1513,640],[1535,813]]

BattleChar = [[168,882],[457,884],[747,879],[1017,887],[1256,884],[1501,874]]
SkillSlot = [[1108,260],[1129,431],[1117,634],[1137,740]]

turnEndPos = [1752,885]

regularRetryInterval = 0.5

def clickSpecific(image,confidence,retryAfter=-1,secondary_image='',secondary_image_confidence=0.7):
    found = 0
    time.sleep(regularRetryInterval)

    try:
        button1 = auto.locateOnScreen(image,confidence=confidence)
        auto.click(button1)
        found= 1
    except auto.ImageNotFoundException:
        print(image,' not found')

    if len(secondary_image) > 0 and found== 0:
        try:
            button2 = auto.locateOnScreen(secondary_image,confidence=secondary_image_confidence)
            auto.click(button2)
            found= 2
        except auto.ImageNotFoundException:
            print(secondary_image,' not found')

    if found == 0:
        time.sleep(retryAfter)
        clickSpecific(image,confidence,retryAfter,secondary_image,secondary_image_confidence)
    else:
        return found

def searchButton(image,confidence,retry=-1):
    try:
        button = auto.locateCenterOnScreen(image,confidence=confidence)
        return button.x,button.y
    except auto.ImageNotFoundException:
        print(image,' not found')
        if retry > -1:
            time.sleep(retry)
            searchButton(image,confidence,retry)
        return None
    1

def setSkill(slot,skill):
    auto.click(BattleChar[slot-1])
    time.sleep(0.1)

    auto.click(SkillSlot[skill-1])

def switchPos(firstChr,SecondChr):
    auto.click(BattleChar[firstChr-1])
    auto.click(BattleChar[SecondChr-1])
    
def turnEnd():
    auto.click(turnEndPos)
    time.sleep(1)

def goAutoRun():
    clickSpecific(button1,0.7,1)
    clickSpecific(toki,0.7,1)
    clickSpecific(autoRun,0.7,1)
    clickSpecific(OKButton2,0.7,1)
    clickSpecific(endGame,0.7,1)
    clickSpecific(OKButton,0.7,1)

def launchApplication():
    cwd = os.getcwd()
    os.chdir(r'C:\Users\jeffr\Desktop')
    subprocess.call('ヘブンバーンズレッド.url', shell = True)
    os.chdir(cwd)
    time.sleep(5)

def trySkipTrailer():
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
    
launchApplication()

searchButton(titleMenu,confidence=0.5,retry=regularRetryInterval)
time.sleep(1)
auto.click(1000,800)

inMainPage = False
while not inMainPage:
    print(tryExitAutoRun(),' onExitAutoRun')
    print(trySkipTrailer(),' onSkippingWhatever')
    inMainPage = searchButton(button1,confidence=0.6)
    time.sleep(regularRetryInterval)
    auto.click(1,1) # incase missed to skip battle result

# clicked = clickSpecific(end_training_image,confidence=0.7,retryAfter=7,secondary_image=button1,secondary_image_confidence=0.6)

# if clicked == 1: # if training mode is on
#     searchButton(battleResult,confidence=0.7,retry=1)
#     time.sleep(1)
#     auto.click(1000,800)
#     time.sleep(1)
#     auto.click(1000,800)
#     # handle daily first login
#     # handle event trailer
#     # handle new style trailer
clickSpecific(button1,confidence=0.6,retryAfter=regularRetryInterval)

match SweepMode:
    case 'jewel':
        clickSpecific(JewelIcon,confidence=0.7,retryAfter=3)

        if SweepItem > 3:
            auto.moveTo(1521,366)
            for i in range (10):
                auto.scroll(-10)
        time.sleep(1)
        auto.click(detailPos[SweepItem])

        time.sleep(1)

        if SweepLevel > 3:
            auto.moveTo(1521,366)
            for i in range (10):
                auto.scroll(-10)

        auto.click(detailPos[SweepLevel])

        clickSpecific(battleButton,0.7,1)
        clickSpecific(maxLifeButton,0.7,1)
        clickSpecific(OKButton,0.7,1)
        clickSpecific(formerTeamButton,0.7,1)
        clickSpecific(OKButton2,0.7,1)
        time.sleep(1)
        clickSpecific(sortieButton,0.7,1)
    case 'orb':
        clickSpecific(orbIcon,confidence=0.7,retryAfter=regularRetryInterval)
        time.sleep(regularRetryInterval)
        match OrbBoss[OrbBossSelection]:
            case 0:
                auto.click(482,242)
            case 1:
                auto.click(961,267)
            case 2:
                auto.click(1455,270)
        if OrbBossItem > 4:
            auto.moveTo(1521,366)
            for i in range (5):
                auto.scroll(-10)
        time.sleep(regularRetryInterval)
        auto.click(OrbBossItemPos[OrbBossItem-1])

        searchButton(homeButton,0.9,2)

        auto.click(685,509)
        time.sleep(1)

        auto.click(OrbBossLevelPos[OrbBossLevel-1])
        clickSpecific(orbBossChallButton,0.7,1)
        clickSpecific(OKButton,0.7,1)
        clickSpecific(maxLifeButton,0.7,1)
        clickSpecific(OKButton,0.7,1)
        # handle if 0/5 life
        clickSpecific(formerTeamButton,0.7,1)
        clickSpecific(OKButton2,0.7,1)
        time.sleep(1)
        clickSpecific(sortieButton,0.7,1)
        auto.click()

# hard coded battle step
searchButton(turnEndButton,0.9,2)
setSkill(1,4)
time.sleep(0.1)
setSkill(2,3)
time.sleep(0.1)
turnEnd()
searchButton(turnEndButton,0.9,2)
turnEnd()
searchButton(turnEndButton,0.9,2)
setSkill(1,1)
time.sleep(0.1)
setSkill(2,1)
time.sleep(0.1)
turnEnd()
setSkill(1,1)
time.sleep(0.1)
turnEnd()
searchButton(turnEndButton,0.9,2)
setSkill(1,1)
time.sleep(0.1)
turnEnd()
searchButton(turnEndButton,0.9,2)
setSkill(1,2)
time.sleep(0.1)
setSkill(2,1)
time.sleep(0.1)
setSkill(3,1)
time.sleep(0.1)
turnEnd()
pos = searchButton(battleResult,0.9,2)
auto.click(pos)
time.sleep(0.1)
auto.click()
time.sleep(0.1)
auto.click()
pos = searchButton(yameru,0.9,2)
auto.click(pos)
time.sleep(1)
auto.click()
time.sleep(1)
auto.click()
pos = searchButton(homeButton,0.9,2)
auto.click(pos)
goAutoRun()
