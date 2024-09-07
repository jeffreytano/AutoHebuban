import pyautogui as auto
import subprocess
import os
import time
import re
import _thread
from pynput.keyboard import Key, Controller

keyboard = Controller()

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
missionButton = r'C:\Users\jeffr\Desktop\AutoHebuban\missionButton.png'
takeReward = r'C:\Users\jeffr\Desktop\AutoHebuban\takeReward.png'
backButton = r'C:\Users\jeffr\Desktop\AutoHebuban\backButton.png'
weeklyButton = r'C:\Users\jeffr\Desktop\AutoHebuban\weeklyButton.png'
takeRewardDisabled = r'C:\Users\jeffr\Desktop\AutoHebuban\takeRewardDisabled.png'
maxLifeButton2 = r'C:\Users\jeffr\Desktop\AutoHebuban\maxLife2.png'
OrbBossItemPos = [[1516,445],[1517,607],[1523,776],[1523,914],[1526,850]]
OrbBossLevelPos = [[1766,277],[1770,466],[1769,661],[1765,852]]
detailPos = [[1521,366],[1517,529],[1523,690],[1631,856],[1526,473],[1513,640],[1535,813]]
BattleChar = [[168,882],[457,884],[747,879],[1017,887],[1256,884],[1501,874]]
SkillSlot = [[1108,260],[1129,431],[1117,634],[1137,740]]
teamPos = [[326,78],[390,78],[454,78],[523,78],[587,78],[678,78],[742,78],[808,78],[872,78],[939,78],[1028,78],[1093,78],[1159,78],[1225,78],[1290,78],[1378,78],[1446,78],[1510,78],[1576,78],[1641,78]]
turnEndPos = [1752,885]
regularRetryInterval = 0.5

def press(key,times = 1):
    key = str(key)
    if len(key) == 1:
        for i in range(times):
            keyboard.press(key)
            keyboard.release(key)
            wait(0.1)
    else:
        match key:
            case 'down':
                for i in range(times):
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    wait(0.1)
            case 'up':
                for i in range(times):
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    wait(0.1)
            case 'left':
                for i in range(times):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    wait(0.1)
            case 'right':
                for i in range(times):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    wait(0.1)
            case 'enter':
                for i in range(times):
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    wait(0.1)

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
    press(slot)
    # auto.click(BattleChar[slot-1])
    wait()
    press('down',skill)
    press('enter')

    # auto.click(SkillSlot[skill-1])

def switchPos(firstChr,SecondChr):
    firstChr,SecondChr = int(firstChr),int(SecondChr)
    press(firstChr)
    wait()
    press(SecondChr)
    # auto.click(BattleChar[firstChr-1])
    # wait()
    # auto.click(BattleChar[SecondChr-1])
    
def turnEnd():
    # auto.click(turnEndPos)
    press('enter')
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

def teamSelection(TeamSlot = 0,Former = False):
    wait(1)
    auto.click(teamPos[TeamSlot])
    wait()
    if Former:
        searchButton(formerTeamButton,0.7,1,True)
        searchButton(OKButton2,0.7,1,True)
        wait(1)
    searchButton(sortieButton,0.7,1,True)

def enterOrbBoss2(Level,useLife,ticket,refill,team,former):
    print('team ',team)
    auto.click(685,509)
    wait()
    press('s',Level+1)
    wait()
    press('enter')
    wait()
    press('enter')
    if Level >= 3: # if level 4
        wait()
        # searchButton(OKButton,0.7,1,True)
        press('enter')
    if ticket:
        press('q')
    if 0<useLife< 5:
        wait()
        press('d',useLife-1)
    elif useLife == -1:
        searchButton(maxLifeButton,0.7,1,True)
    elif useLife <= 5:
        pos = searchButton(maxLifeButton,0.7,1,True)
        auto.click(pos)
    if searchButton(notEnoughLife,0.7):
        # searchButton(OKButton,0.7,1,True)
        press('enter')
        wait()
        searchButton(useLifeStone,0.7,regularRetryInterval)
        wait()
        press('down',2)
        match refill:
            case 0:
                press('right')
                press('enter')
            case 1:
                press('enter')
            case 2:
                press('left')
                press('enter')
        # searchButton(OKButton,0.7,1,True)
        wait()
        press('enter')
        wait()
    # searchButton(OKButton,0.7,1,True)
    press('enter')
    # searchButton(formerTeamButton,0.7,1,True)
    # searchButton(OKButton2,0.7,1,True)
    # wait(1)
    # searchButton(sortieButton,0.7,1,True)
    # auto.click()
    teamSelection(team,former)

def enterOrbBoss(Target,Level,useLife,ticket,refill,team,former):
    searchButton(button1,0.6,regularRetryInterval,True)
    searchButton(orbIcon,0.7,regularRetryInterval,True)
    wait()

    match Target:
        case Target if Target in range(6,10):
            pass
        case Target if Target in range(11,15):
            press('e')
        case Target if Target in range(16,20):
            press('e',2)

    press('s',(Target-1)%5+1)
    press('enter')

    searchButton(homeButton,0.9,regularRetryInterval)

    enterOrbBoss2(Level,useLife,ticket,refill,team,former)

def enterJewel(Color,Level,resource,refill):
    searchButton(button1,confidence=0.6,retry=regularRetryInterval,clickit=True)
    searchButton(JewelIcon,confidence=0.7,retry=regularRetryInterval,clickit=True)

    wait()

    for i in range(Color+1):
        print('press S')
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        wait(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # if Color > 3:
    #     auto.moveTo(1521,366)
    #     for i in range (10):
    #         auto.scroll(-10)
    # time.sleep(1)
    # auto.click(detailPos[Color])

    time.sleep(1)

    for i in range(Level+1):
        print('press S')
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        wait(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # if Level > 3:
    #     auto.moveTo(1521,366)
    #     for i in range (10):
    #         auto.scroll(-10)

    # auto.click(detailPos[Level])

    searchButton(battleButton,0.7,1,True)
    searchButton(maxLifeButton,0.7,1,True)
    searchButton(OKButton,0.7,1,True)
    # searchButton(formerTeamButton,0.7,1,True)
    # searchButton(OKButton2,0.7,1,True)
    # wait(1)
    # searchButton(sortieButton,0.7,1,True)
    teamSelection(1,True)

def battleInstruction(txtName):
    if txtName != 'Auto':
        fileName = f'{txtName}.txt'
        file = open(fileName,'r')
        for line in file.readlines():
            if line == 'BE':
                break
            wait(5)
            while not searchButton(turnEndButton,0.9):
                if searchButton(homeButton,0.9):
                    file.close()
                    return False
                if searchButton(battleResult,0.9):
                    file.close()
                    return True
                wait(1)
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
                wait()
        file.close()
        return True
    else:
        searchButton(turnEndButton,0.7,1)
        #search if auto is already on
        press('r')
        while not searchButton(battleResult,0.9,):
            if searchButton(homeButton,0.9):
                return False
            wait(2)
        return True

def interrupt_function():
    print("Interrupting the main thread...")
    _thread.interrupt_main()

class autoHvbn:
    def __init__(self):
        pass

    def goAutoRun(self):
        searchButton(button1,0.7,1,True)
        searchButton(toki,0.7,1,True)
        wait()
        press('down')
        press('up')
        press('right')
        press('enter')
        wait()
        press('enter')
        # self.clickSpecific(autoRun,0.7,1)
        # self.clickSpecific(OKButton2,0.7,1)
        searchButton(endGame,0.7,1)
        wait()
        press('right',2)
        # searchButton(OKButton,0.7,1,True)
        wait()
        press('enter')
        wait()
        press('enter')

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

    def enterBattleHandler(self,target,level,times,team=0,former=False,ticket=False,instruction = 'auto', refill = 0):
        counter = 0
        if times == 'All':
            useLife = -1
            times = 5
        else:
            times = useLife = int(times)
        print('useLife ', useLife)
        if 0<target<=5:
            enterJewel(target,level,useLife,ticket,refill,team,former)
        else:
            enterOrbBoss(target,level,useLife,ticket,refill,team,former)
        while counter <= times:
            won = battleInstruction(instruction)
            if not won:
                if 0<target<=5:
                    # re enter jewel
                    print('re enter jewel')
                else:
                    enterOrbBoss2(level,useLife,ticket,refill,team,former)
                    continue
                    # re enter orb
            counter +=5
            # pos = searchButton(battleResult,0.9,2)
            # wait()
            # auto.click(pos)
            # wait()
            # auto.click(1,1)
            # wait()
            # auto.click(1,1)
            while not searchButton(againButton,0.9):
                press('enter')
                wait()
            if counter < times:
                print('again',counter,times)
                press('enter')
                wait()
                searchButton(maxLifeButton2,0.7,1,True)
                press('enter')
                wait()
                searchButton(useLifeStone,0.7,1,True)
                wait()
                press('enter')
                wait()
                press('enter')
                wait()
                press('enter')
                battleInstruction(instruction)
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

    def interrupt(self):
        interrupt_function()

    def takeReward(self,daily,weekly):
        print(daily,weekly)
        if daily or weekly:
            searchButton(button1,0.7,1)
            searchButton(missionButton,0.7,1,True)
            if daily:
                reward = searchButton(takeReward,0.8)
                disabled = searchButton(takeRewardDisabled,0.8)
                while not (reward or disabled):
                    print(reward, disabled, reward or disabled)
                    reward = searchButton(takeReward,0.8)
                    disabled = searchButton(takeRewardDisabled,0.8)
                if reward:
                    auto.click(reward)
                    wait(1)
                    searchButton(OKButton,0.7,1,True)
                    wait(1)
            if weekly:
                wait(1)
                searchButton(weeklyButton,0.7,1,True)
                reward = searchButton(takeReward,0.8)
                disabled = searchButton(takeRewardDisabled,0.8)
                while not (reward or disabled):
                    print(reward, disabled, reward or disabled)
                    reward = searchButton(takeReward,0.8)
                    disabled = searchButton(takeRewardDisabled,0.8)
                if reward:
                    wait(1)
                    auto.click(reward)
                    wait(1)
                    searchButton(OKButton,0.7,1,True)
                    wait(1)
            searchButton(backButton,0.7,1,True)

    def battleOnly(self,txt):
        battleInstruction(txt)