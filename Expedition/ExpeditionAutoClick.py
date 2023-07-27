import pyautogui
import time

defeated = pyautogui.locateCenterOnScreen('Expedition/Expedition.assets/Defeated.PNG', confidence= 0.7)

while defeated is None:
    
    startBattle = pyautogui.locateCenterOnScreen('Expedition/Expedition.assets/StartBattle.PNG', confidence= 0.7)
    if startBattle is not None:
        pyautogui.click(821,1002) #Assign All
        time.sleep(1)
        pyautogui.click(startBattle) 
        
        victory = pyautogui.locateCenterOnScreen('Expedition/Expedition.assets/Victory.PNG', confidence= 0.7)

        while victory is None:
            time.sleep(5)
            victory = pyautogui.locateCenterOnScreen('Expedition/Expedition.assets/Victory.PNG', confidence= 0.7)

    nextStage = pyautogui.locateCenterOnScreen('Expedition/Expedition.assets/NextStage.PNG', confidence= 0.7)
    pyautogui.click(nextStage)
    time.sleep(1)
    defeated = pyautogui.locateCenterOnScreen('Expedition/Expedition.assets/Defeated.PNG', confidence= 0.7)


print("Defeated")






""" 
click challenge
click assign all
click start battle
wait battle
click next Stage = 956,807
click start battle = 1098,999
wait battle


 """