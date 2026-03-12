##go no go

#Hi, I’m trying to adapt a GO/NOGO protocol from Price et al., 2016. Food-specific response inhibition,
#dietary restraint and snack intake in lean and overweight/obese adults.
#The task consists in 50 trials (40 go and 10 no-go). During go trials the 
#subject should press a key as fast as possible. During no-go trials, no key should be pressed. 
#Each trial is composed by an image presented for 750ms and was separated by a blank screen for 500 ms 
#and preceded by a fixation cross for 500 ms. The sequence of go/nogo stimuli are predetermined. 
#Two set of images are used: 10 go images (each one is presented 4 times) and 10 no-go images 
#(each one is presented one time). Image order should be randomized across subjects.
# we are going to change for anorexia nervosa intervention

import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim, Circle
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random

exp_info = {'participant_nr': '', 'age': '21'}
dlg = DlgFromDict(exp_info)

p_name= exp_info['participant_nr']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False)

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

# Initialize a (global) clock
clock = Clock()
f_list = f"Users\Aashree\Downloads\Food-Choice-Task-main\Food-Choice-Task-main\lists\HF_LF_60.csv"
foods = pd.read_csv(f_list)
hf = foods[foods['fat']==1]
lf = foods[foods['fat']==0]
lf = lf.sample(frac=0.4)
hf = hf.sample(frac=0.4)
trial_foods=pd.concat([lf,lf,lf,hf])
trial_foods = trial_foods.sample(frac=1)
kb=Keyboard()

instructions = TextStim(
    win,
    text="""In this task you will see pictures of food.
         Press the SPACEBAR for every food image UNLESS you see a RED circle.
         Green circle = PRESS SPACE
         Red circle = DO NOT PRESS
         Respond as quickly and accurately as possible.
         Press SPACE to begin.,"""
         
    height=0.05,
    wrapWidth=1.2
)

instructions.draw()
win.flip()

event.waitKeys(keyList=['space'])


for i in range(0,len(trial_foods)):
    trial=trial_foods.iloc[i]
    print(trial)
    t=TextStim(win,"+")
    t.draw()
    win.flip()
    wait(0.5)
    path = "Users\Aashree\Downloads\Food-Choice-Task-main\Food-Choice-Task-main\stimuli" + trial.food
    print(trial.fat)
    if trial.fat==1:
        correct = "nogo"
        go_cue = Circle(
                    win,
                    radius=0.05,
                    fillColor='red',
                    lineColor='red',
                    pos=(0.7, 0.4) 
                ) 
    else: 
        correct = "go"
        go_cue = Circle(
                    win,
                    radius=0.05,
                    fillColor='green',
                    lineColor='green',
                    pos=(0.7, 0.4) 
                )
    im=ImageStim(win, path)
    
    
    t_clock=Clock()
    response = "nongo"
    rt="NA"
    while t_clock.getTime() < .75:
        if correct == "go":
            go_cue.draw()
        else:
            nogo_cue.draw()

win.flip()
        
        keys = kb.getKeys(['space','escape'], waitRelease=False)
        if keys:
            resp = keys[0].name
            rt = keys[0].rt
            if resp == 'escape':
                win.close()
                quit()
            else:
                response = "go"

    win.flip()
    wait(.5)
    trial_foods['response']=response
    trial_foods['rt']= rt

trials.save(f"{p_name}_gonogo.csv")

## tasks
# 1. figure out what is happening in the task & add instructions
# 2. we need to add go-nogo! How would we do that?

    
