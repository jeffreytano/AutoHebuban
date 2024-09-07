import pyautogui as auto
import subprocess
import os
import time
import re
from pynput.keyboard import Key, Controller

keyboard = Controller()

titleMenu = 'titleMenu.png'
end_training_image = 'AutoTrainEnd.png'
strengthen = 'strengthen.png'
orbIcon = 'orb.png'
JewelIcon = 'jewel.png'
battleButton = 'battle.png'
maxLifeButton = 'maxLife.png'
OKButton = 'OK.png'
sortieButton = 'sortie.png'
formerTeamButton = 'formerteam.png'
homeButton = 'homeButton.png'
turnEndButton = 'turnEnd.png'
battleResult = 'battleResult.png'
againButton = 'again.png'
yameru = 'yameru.png'
toki = 'toki.png'
autoRun = 'autoRun.png'
endGame = 'endGame.png'
skipButton = 'skip.png'
notEnoughLife = 'notEnoughLife.png'
useLifeStone = 'useLifeStone.png'
dailyFree = 'dailyFree.png'
dailyGachaConfirm = 'dailyGachaConfirm.png'
okButtonDaily = 'okButtonDaily.png'
missionButton = 'missionButton.png'
takeRewardButton = 'takeReward.png'
backButton = 'backButton.png'
weeklyButton = 'weeklyButton.png'
takeRewardDisabled = 'takeRewardDisabled.png'
maxLifeButton2 = 'maxLife2.png'
arenaButton = 'arenaButton.png'
skipDialog = 'skipDialog.png'
arenaYameru = 'arenaYameru.png'
arenaBack = 'arenaBack.png'
autoOn = 'autoOn.png'
arenaForm = 'arenaForm.png'
dialogAutoOff = 'dialogAutoOff.png'
menu = 'menu.png'
terminate = 'terminate.png'
detailPos = [[1521,366],[1517,529],[1523,690],[1631,856],[1526,473],[1513,640],[1535,813]]
BattleChar = [[168,882],[457,884],[747,879],[1017,887],[1256,884],[1501,874]]
SkillSlot = [[1108,260],[1129,431],[1117,634],[1137,740]]
teamPos = [[326,78],[390,78],[454,78],[523,78],[587,78],[678,78],[742,78],[808,78],[872,78],[939,78],[1028,78],[1093,78],[1159,78],[1225,78],[1290,78],[1378,78],[1446,78],[1510,78],[1576,78],[1641,78]]
regularRetryInterval = 0.5
mainStoryPos = (831,937)
    
def press(key,times = 1,delay = 0.1):
    key = str(key).lower()
    if len(key) == 1:
        for i in range(times):
            keyboard.press(key)
            keyboard.release(key)
            wait(delay)
    else:
        match key:
            case 'down':
                for i in range(times):
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    wait(delay)
            case 'up':
                for i in range(times):
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    wait(delay)
            case 'left':
                for i in range(times):
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    wait(delay)
            case 'right':
                for i in range(times):
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    wait(delay)
            case 'enter':
                for i in range(times):
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    wait(delay)

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
        # searchButton(dailyGachaConfirm,0.7,1,True)
        wait()
        press('enter')
        wait(4)
        okButton = searchButton(okButtonDaily,0.7)
        while not okButton:
            wait(1)
            press('enter')
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
        arenaBackButton = searchButton(arenaBack,0.7)
        if arenaBackButton:
            wait()
            auto.click(arenaBackButton)
            wait(2)
            if searchButton(dialogAutoOff,0.7):
                press('r')
        inMainPage = searchButton(strengthen,confidence=0.6)
        time.sleep(regularRetryInterval)
        press('enter') # incase missed to skip battle result

def setSkill(slot,skill,target = 0):
    slot,skill,target = int(slot),int(skill),int(target)
    press(slot)
    # auto.click(BattleChar[slot-1])
    wait()
    press('down',skill)
    if (target):
        press('enter')
        wait()
        if (target>slot):
            press('d',target-slot,0.2)
        else:
            press('a',slot-target,0.2)
        wait()
        press('enter')
        wait()
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
    if pos:
        time.sleep(regularRetryInterval)
        press('left')
        wait()
        press('enter')
        return True
    else:
        return False

def teamSelection(TeamSlot = 0,Former = False):
    wait(1)
    auto.click(teamPos[TeamSlot])
    wait()
    if Former:
        # searchButton(formerTeamButton,0.7,1,True)
        press('down')
        press('right')
        press('enter')
        wait()
        press('enter')
        wait(2)
    # searchButton(sortieButton,0.7,1,True)
    press('down')
    press('enter')

def enterOrbBoss2(level,useLife,ticket,refill,team,former):
    print('team ',team)
    auto.click(685,509)
    wait()
    press('s',level+1)
    wait()
    press('enter')
    wait()
    press('enter')
    if level >= 3: # if level 4
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
        wait(1)
        press('enter')
        wait(1)
    # searchButton(OKButton,0.7,1,True)
    press('enter')
    # searchButton(formerTeamButton,0.7,1,True)
    # searchButton(OKButton2,0.7,1,True)
    # wait(1)
    # searchButton(sortieButton,0.7,1,True)
    # auto.click()
    teamSelection(team,former)

def enterOrbBoss(Target,level,useLife,ticket,refill,team,former):
    pos = searchButton(strengthen,0.6,regularRetryInterval)
    wait()
    auto.click(pos)
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

    enterOrbBoss2(level,useLife,ticket,refill,team,former)

def enterJewel(Color,level,useLife,ticket,refill,team,former):
    searchButton(strengthen,confidence=0.6,retry=regularRetryInterval,clickit=True)
    pos =searchButton(JewelIcon,confidence=0.8,retry=regularRetryInterval,clickit=True)
    print(pos)
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

    for i in range(level+1):
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
        wait(1)
        press('enter')
        wait(1)
    press('enter')
    # searchButton(maxLifeButton,0.7,1,True)
    # searchButton(OKButton,0.7,1,True)
    # searchButton(formerTeamButton,0.7,1,True)
    # searchButton(OKButton2,0.7,1,True)
    # wait(1)
    # searchButton(sortieButton,0.7,1,True)
    teamSelection(team,former)

def battleInstruction(txtName):
    if txtName != 'Auto':
        fileName = f'{txtName}.txt'
        file = open(fileName,'r')
        for line in file.readlines():
            if line == 'BE':
                break
            wait(5)
            while not searchButton(turnEndButton,0.9):
                if searchButton(homeButton,0.9) or searchButton(strengthen,0.9):
                    file.close()
                    return False
                if searchButton(battleResult,0.9) :
                    file.close()
                    return True
                wait(1)
                if searchButton(autoOn,0.9):
                    press('r')
            commands = line.split()
            for command in commands:
                SetSkill = re.search('^C[1-6]S[1-9]',command)
                SetSkillTarget = re.search('^C[1-6]S[1-9]C[1-6]',command)
                Swap = re.search('^C[1-6]C[1-6]',command)
                if re.search('^T\d',command):
                    print('Turn',command[1:])
                    continue
                if SetSkillTarget:
                    print('SetSkill',command[1],command[3],command[5])
                    setSkill(command[1],command[3],command[5])
                    wait()
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
                if command == 'OD':
                    print('OD')
                    while not searchButton(turnEndButton,0.7):
                        print('pressing O')
                        press('o')
                        wait()
                if command == 'TE':
                    print('TurnEnd')
                    turnEnd()
                    continue
                wait()
        file.close()
        return True
    else:
        searchButton(turnEndButton,0.7,1)
        autoIsOn = searchButton(autoOn,0.9)
        if not autoIsOn:
            press('r')
        while not searchButton(battleResult,0.9,):
            if searchButton(homeButton,0.9) or searchButton(strengthen,0.9):
                return False
            wait(2)
        return True

# def interrupt_function():
#     print("Interrupting the main thread...")
#     _thread.interrupt_main()

def launchApplication(daily):
    auto.PAUSE = 0.1
    cwd = os.getcwd()
    path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(path)
    subprocess.call('ヘブンバーンズレッド.url', shell = True)
    os.chdir(cwd)
    wait(5)
    searchButton(titleMenu,confidence=0.9,retry=0.5)
    wait(1)
    press('enter')
    handleBeforeHomePage(daily)

def closeProcess(daily,weekly,autoRun):
    print(daily,weekly)
    if daily or weekly:
        searchButton(strengthen,0.7,1)
        searchButton(missionButton,0.7,1,True)
        if daily:
            reward = searchButton(takeRewardButton,0.8)
            disabled = searchButton(takeRewardDisabled,0.8)
            while not (reward or disabled):
                print(reward, disabled, reward or disabled)
                reward = searchButton(takeRewardButton,0.8)
                disabled = searchButton(takeRewardDisabled,0.8)
            if reward:
                auto.click(reward)
                wait(1)
                searchButton(OKButton,0.7,1,True)
                wait(1)
        if weekly:
            wait(1)
            searchButton(weeklyButton,0.7,1,True)
            reward = searchButton(takeRewardButton,0.8)
            disabled = searchButton(takeRewardDisabled,0.8)
            while not (reward or disabled):
                print(reward, disabled, reward or disabled)
                reward = searchButton(takeRewardButton,0.8)
                disabled = searchButton(takeRewardDisabled,0.8)
            if reward:
                auto.click(reward)
                wait(1)
                searchButton(OKButton,0.7,1,True)
                wait(1)
        searchButton(backButton,0.7,1,True)
    match autoRun:
        case 0:
            searchButton(strengthen,0.7,1,True)
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
        case 1:
            #arena
            auto.click(mainStoryPos)
            pos = searchButton(arenaButton,0.9,1)
            wait()
            auto.click(pos)
            pos = searchButton(skipButton,0.9,1)
            wait()
            auto.click(pos)
            while not searchButton(arenaForm,0.9):
                press('enter')
            press('left')
            press('enter')
            wait()
            press('enter')
            searchButton(endGame,0.7,1)
            wait()
            press('right',2)
            wait()
            press('enter')
            wait()
            press('enter')
        case 2:
            #exit
            print('exit')
            pos = searchButton(menu,0.8,1)
            wait()
            auto.click(pos)
            wait()
            pos = searchButton(terminate,0.8,1)
            wait()
            auto.click(pos)
            wait()
            press('enter')

def battleOnly(txt):
    battleInstruction(txt)

def enterBattleHandler(target,level,times,team=0,former=False,ticket=False,instruction = 'auto', refill = 0):
        print('enterBattleHandler')
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
                    enterJewel(target,level,useLife,ticket,refill,team,former)
                    continue
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
            # searchButton(OKButton,0.7,1,clickit=True)
            wait()
            press('enter')
        while not searchButton(strengthen,0.7):
            press('enter')
            wait()
        

def bunChan(count):
    counter = 0
    print('bunChan')
    while counter < count:
        print(counter)
        press('enter')
        searchButton(turnEndButton,0.7,2)
        searchButton(battleResult,0.7,1)
        while not searchButton(arenaYameru,0.7):
            press('enter')
            wait()
        counter +=1
    searchButton(arenaYameru,0.7,1,True)
    press('enter')
    searchButton(arenaBack,0.7,1,True)


