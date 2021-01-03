# pip install pypiwin32
import win32com.client as wincl

def demo_win10():
    syn = wincl.Dispatch('SAPI.SpVoice') # use Windows SAPI (Speech API)
    syn.Rate = 0 # normal speed = 0
    syn.Volume = 100 # max volume = 100
    s = 'I love Thailand'
    print(s)
    syn.Speak(s)

demo_win10()