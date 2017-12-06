#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Trabalho de Controle para Automação 2017/2
#Código de controle do robô cyton.
#Supervisório 2 (Utiliza a outra máquina caso a desejada esteja indisponível.)
#Author: Carlos Rocha
#Version: 1.0

# AUTOMATO DE EVENTOS NÃO CONTROLÁVEIS

import rospy
from std_msgs.msg import Int8
from std_msgs.msg import String



#######################################
### FUNÇÕES DE CALLBACK - NÃO MEXER ###
#######################################

# Callback para novo evento
def eventCallback(data):
	print('eventCallback')
	global newEvent

	newEvent = data.data


# Função que manda índice de movimento para o Cyton
def sendMovement(move):
	print('sendMovement')
	print(move)
	global pub
	moveToSend = Int8()
	moveToSend = move
	pub.publish(moveToSend)


###########################################
### LISTA DE ESTADOS - EDITE ESTA PARTE ###
###########################################

# Exemplo de estado inicial
def init():#C0G0R0E200
	# Indica novo estado no log para debug
	print('init(C0G0R0E200)')
	# As variáveis gobais devem sempre ser chamadas na definição do estado
	global state
	global newEvent


	# Loop que espera o próximo evento
	while True:
		if newEvent == 'greenNew':
			newEvent = 'none'
			state = C0G0R0E201
			break
		elif newEvent == 'redNew':
			newEvent = 'none'
			state = C0G0R0E209
			break

def C0G0R0E201():#1
	print('state1(C0G0R0E201)')

	global state
	global newEvent

	while True:
		if newEvent == 'greenLoad':
                        sendMovement(1)#greenLoad
			newEvent = 'none'
			state = C1G1R0E202
			break

	
def C1G0R0E201():#2
	print('state2(C1G0R0E201)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E201
			break

def C1G0R0E200():#3
	print('state3(C1G0R0E200)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init#C0G0R0E200
			break
		elif newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C1G0R0E201
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C1G0R0E209
                        break
                
def C1G0R0E209():#AQUI 4 
	print('state4(C1G0R0E209)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E209
			break
		
def C0G0R0E209():#5
	print('state5(C0G0R0E209)')
	global state
	global newEvent

	while True:
		if newEvent == 'redLoad':
                        sendMovement(0)#redLoad
			newEvent = 'none'
			state = C1G0R1E208
			break

def C1G1R0E202():#6
	print('state6(C1G1R0E202)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R0E202
			break
		elif newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C1G1R0E204
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C1G1R0E204
                        break
                elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C1G0R0E203
                        break

def C1G0R0E203():#7
	print('state7(C1G0R0E203)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E203
			break

def C0G0R0E203():#8
	print('state8(C0G0R0E203)')
	global state
	global newEvent

	while True:
		if newEvent == 'greenUnload':
                        sendMovement(3)#greenUnload
			newEvent = 'none'
			state = C1G0R0E200
			break

def C0G0R0E207():#9
	print('state9(C0G0R0E207)')
	global state
	global newEvent

	while True:
		if newEvent == 'redUnload':
                        sendMovement(2)#redUnload
			newEvent = 'none'
			state = C1G0R0E200
			break

def C1G0R0E207():#10
	print('state10(C1G0R0E207)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E207
			break

def C1G0R1E208():#11
	print('state11(C1G0R1E208)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R1E208
			break
		elif newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C1G0R1E210
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C1G0R1E210
                        break
                elif newEvent == 'redDone':
                        newEvent = 'none'
                        state = C1G0R0E207
                        break

def C1G1R0E204():#12 here
	print('state12(C1G1R0E204)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R0E204
			break

def C0G1R0E202():#13
	print('state13(C0G1R0E202)')
	global state
	global newEvent

	while True:
		if newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C0G1R0E204
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C0G1R0E204
                        break
                elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C0G0R0E203
                        break

def C0G0R1E208():#14
	print('state14(C0G0R1E208)')
	global state
	global newEvent
	
	while True:
		if newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C0G0R1E210
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C0G0R1E210
                        break
                elif newEvent == 'redDone':
                        newEvent = 'none'
                        state = C0G0R0E207
                        break

def C1G0R1E210():#15
	print('state15(C1G0R1E210)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R1E210
			break

def C0G1R0E204():#16 HERE
	print('state16(C0G1R0E204)')
	global state
	global newEvent

	while True:
		if newEvent == 'redLoad':
                        sendMovement(0)#redLoad
			newEvent = 'none'
			state = C1G1R1E205
			break

def C0G0R1E210():#17
	print('state17(C0G0R1E210)')
	global state
	global newEvent

	while True:
		if newEvent == 'greenLoad':
                        sendMovement(1)#greenLoad
			newEvent = 'none'
			state = C1G1R1E211
			break

def C0G1R0E206():#18
	print('state18(C0G1R0E206)')
	global state
	global newEvent

	while True:
		if newEvent == 'redUnload':
                        sendMovement(2)#redUnload
			newEvent = 'none'
			state = C1G1R0E202
			break

def C0G0R1E212():#19
	print('state19(C0G0R1E212)')
	global state
	global newEvent

	while True:
		if newEvent == 'greenUnload':
                        sendMovement(3)#greenUnload
			newEvent = 'none'
			state = C1G0R1E208
			break

def C1G1R0E206():#20
	print('state20(C1G1R0E206)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R0E206
			break

def C1G0R1E212():#21
	print('state21(C1G0R1E212)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R1E212
			break
def C1G1R1E205():#22 HERE
	print('state22(C1G1R1E205)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R1E205
			break
		elif newEvent == 'redDone':
                        newEvent = 'none'
                        state = C1G1R0E206
                        break
                elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C1G0R1E212
                        break

def C1G1R1E211():#23
	print('state23(C1G1R1E211)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R1E211
			break
		elif newEvent == 'redDone':
                        newEvent = 'none'
                        state = C1G1R0E206
                        break
                elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C1G0R1E212
                        break

def C0G1R1E205():#24
	print('state24(C0G1R1E205)')
	global state
	global newEvent

	while True:
		if newEvent == 'redDone':
                        newEvent = 'none'
                        state = C0G1R0E206
                        break
                elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C0G0R1E212
                        break

def C0G1R1E211():#25
	print('state25(C0G1R1E211)')
	global state
	global newEvent

	while True:
		if newEvent == 'redDone':
                        newEvent = 'none'
                        state = C0G1R0E206
                        break
                elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C0G0R1E212
                        break





###################################################
### DECLARAÇÃO DE VARIÁVEIS GLOBAIS - NÃO MEXER! ###
###################################################


state = init
newEvent = 'none'


##############################
### LOOP MAIN - NÃO MEXER! ###
##############################

def main():
	global state
	global pub

	rospy.init_node('automato', anonymous=False)
	pub = rospy.Publisher('move', Int8, queue_size = 10)
	rospy.Subscriber('event', String, eventCallback)

	rospy.sleep(1)

	while not rospy.is_shutdown():
		state()



if __name__ == '__main__':
	main()
