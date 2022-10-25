import pyautogui

def spam(text, num=10, victim, paste=False, tts=False):
    if tts:
        txt = f"/tts {text} @{victim}"
    else:
        txt = f"{text} @{victim}"

    # uses a copy-paste method; will run into rate-limitation when num is > 10
    if paste:
        pyautogui.typewrite(txt, interval=0.12) # interval is set at 12 miliseconds to avoid Discord crashing
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press('enter')

        for i in range(num):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        return
    
    # uses continuous iteration; won't run into rate-limitation but will be more demanding on computer
    for i in range(num):
        pyautogui.typewrite(txt + "\n", interval=0.12)

person = pyautogui.prompt('who to spam?')
amount = int(pyautogui.prompt('how many times?'))
sentence = pyautogui.prompt("what to say?") 
pyautogui.alert('ready?')

spam(sentence, amount, person, True, True)
