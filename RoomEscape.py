from bangtal import *

''' Setting scene1'''
scene1 = Scene('룸1', 'images/배경-1.png')

door1 = Object('images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

key = Object('images/열쇠.png')
key.setScale(0.2)
key.locate(scene1, 600, 150)
key.show()

flowerpot = Object('images/화분.png')
flowerpot.locate(scene1, 550, 150)
flowerpot.show()
''' /Setting scene1'''

''' Setting scene2'''
scene2 = Scene('룸2', 'images/배경-2.png')

door2 = Object('images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('images/문-오른쪽-닫힘.png')
door3.locate(scene2, 940, 283)
door3.setScale(0.2)
door3.show()
door3.closed = True
door3.locked = True

flowerpot2 = Object('images/화분.png')
flowerpot2.locate(scene2, 895, 200)
flowerpot2.show()

keypad = Object('images/키패드.png')
keypad.locate(scene2, 925, 315)
keypad.show()

switch = Object('images/스위치.png')
switch.locate(scene2, 695, 400)
switch.show()
switch.lighted = True

password = Object('images/1234.png')
password.locate(scene2, 400, 100)
''' /Setting scene2'''


def door1_onMouseAction(x, y, action):
    if door1.closed == True:
        if key.inHand() == True:
            door1.setImage('images/문-오른쪽-열림.png')
            door1.closed = False
        else: showMessage('열쇠가 필요합니다')
    else:
        scene2.enter()
door1.onMouseAction = door1_onMouseAction

def key_onMouseAction(x, y, action):
    key.pick()
key.onMouseAction = key_onMouseAction

flowerpot.moved = False
def flowerpot_onMouseAction(x, y, action):
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True 
flowerpot.onMouseAction = flowerpot_onMouseAction

def door2_onMouseAction(x, y, action):
    scene1.enter()
door2.onMouseAction = door2_onMouseAction

def door3_onMouseAction(x, y, action):
    if door3.locked == True:
        showMessage('문이 잠겨있습니다')
    elif door3.closed == True:
        door3.setImage('images/문-오른쪽-열림.png')
        door3.closed = False
    else:
        endGame()
door3.onMouseAction = door3_onMouseAction

flowerpot2.moved = False
def flowerpot2_onMouseAction(x, y, action):
    if flowerpot2.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot2.locate(scene2, 795, 200)
            flowerpot2.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot2.locate(scene2, 995, 200)
            flowerpot2.moved = True 
flowerpot2.onMouseAction = flowerpot2_onMouseAction

def door3_onKeypad():
    door3.locked = False
    showMessage('철커덕!!! 잠김이 해제되었습니다!')
door3.onKeypad = door3_onKeypad

def keypad_onMouseAction(x, y, action):
    showKeypad('1234', door3)
keypad.onMouseAction = keypad_onMouseAction

def switch_onMouseAction(x, y, action):
    switch.lighted = not switch.lighted
    if switch.lighted == True:
        scene2.setLight(1)
        password.hide()
    else:
        scene2.setLight(0.25)
        password.show()
switch.onMouseAction = switch_onMouseAction

startGame(scene1)