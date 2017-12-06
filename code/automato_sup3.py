#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Trabalho de Controle para Automação 2017/2
#Código de controle do robô cyton.
#Supervisório 3 (Peças vermelhas devem passar nas duas máquinas (R to G) antes de sairem do processo)
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
def init():#C0G0R0E30
	# Indica novo estado no log para debug
	print('init(C0G0R0E30)')
	# As variáveis gobais devem sempre ser chamadas na definição do estado
	global state
	global newEvent

	# Manda pose 0 para o Cyton
	#sendMovement(0)

	# Loop que espera o próximo evento
	while True:
		# Condição para cada evento que afeta o estado
		if newEvent == 'greenNew':
			# Zerar evento
			newEvent = 'none'
			# Atualizar próximo estado
			state = C0G0R0E31
			# Sair do loop
			break
		elif newEvent == 'redNew':
			newEvent = 'none'
			state = C0G0R0E34
			break

def C0G0R0E31():#1
	print('state1(C0G0R0E31)')

	global state
	global newEvent

        while True:
                if newEvent == 'greenLoad':
                        sendMovement(1)#GREENLOAD
                        newEvent = 'none'
                        state = C1G1R0E32
                        break
			
def C1G0R0E31():#X1
        print('stateX1(C1G0R0E31)')
        global state
        global newEvent

        while True:
                if newEvent == 'cytonIdle':
                        newEvent = 'none'
                        state = C0G0R0E31
                        break
	
def C0G0R0E33():#2
	print('state2(C0G0R0E33)')
	global state
	global newEvent

        while True:
                if newEvent == 'greenUnload':
                        sendMovement(3)#GREENUNLOAD
                        newEvent = 'none'
                        state = C1G0R0E30
                        break
			

def C1G0R0E30():#3
	print('state3(C1G0R0E30)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init#C0G0R0E30
			break
		elif newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C1G0R0E31#x1
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C1G0R0E34#X2
                        break

def C1G0R0E34():#X2
        print('stateX2(C1G0R0E34)');
        global state
        global newEvent

        while True:
                if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E34
			break

def C0G0R0E34():#4
	print('state4(C0G0R0E34)')
	global state
	global newEvent

        while True:
                if newEvent == 'redLoad':
                        sendMovement(0)#redload
                        newEvent = 'none'
                        state = C1G0R1E30
                        break
			

def C1G0R0E33():#5
	print('state5(C1G0R0E33)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E33
			break

def C1G1R0E32():#6
	print('state6(C1G1R0E32)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R0E32
			break
		elif newEvent == 'redNew':
			newEvent = 'none'
			state = C1G1R0E36
			break
		elif newEvent == 'greenDone':
			newEvent = 'none'
			state = C1G0R0E33
			break

def C0G0R0E35():#7
	print('state7(C0G0R0E35)')
	global state
	global newEvent

        while True:
                if newEvent == 'red2Green':
                        sendMovement(4)#RED2GREEN
                        newEvent = 'none'
                        state = C1G1R0E32
                        break
			

def C1G0R0E35():#8
	print('state8(C1G0R0E35)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E35
			break

def C1G0R1E30():#9
	print('state9(C1G0R1E30)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R1E30
			break
		elif newEvent == 'greenNew':
			newEvent = 'none'
			state = C1G0R1E31
			break
		elif newEvent == 'redDone':
			newEvent = 'none'
			state = C1G0R0E35
			break

def C1G1R0E36():#10
	print('state10(C1G1R0E36)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R0E36
			break

def C0G1R0E32():#11
	print('state11(C0G1R0E32)')
	global state
	global newEvent

	while True:
		if newEvent == 'redNew':
			newEvent = 'none'
			state = C0G1R0E36
			break
		elif newEvent == 'greenDone':
			newEvent = 'none'
			state = C0G0R0E33
			break

def C0G0R1E33():#12
	print('state12(C0G0R1E33)')
	global state
	global newEvent

        while True:
                if newEvent == 'greenUnload':
                        sendMovement(3)#GREENUNLOA
                        newEvent = 'none'
                        state = C1G0R1E30
                        break
			
def C0G0R1E30():#13
	print('state13(C0G0R1E30)')
	global state
	global newEvent

	while True:
		if newEvent == 'greenNew':
			newEvent = 'none'
			state = C0G1R1E31
			break
		elif newEvent == 'redDone':
			newEvent = 'none'
			state = C0G0R0E35
			break

def C1G0R1E31():#14
	print('state14(C1G0R1E31)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R1E31
			break

def C0G1R0E36():#15
	print('state15(C0G1R0E36)')
	global state
	global newEvent

        while True:
                if newEvent == 'redLoad':
                        sendMovement(0)#REDLOAD
                        newEvent = 'none'
                        state = C1G1R1E32
                        break
			

def C0G1R131():#16
	print('state16(C0G1R131)')
	global state
	global newEvent

        while True:
                if newEvent == 'greenLoad':
                        sendMovement(1)#GREENLOAD
                        newEvent = 'none'
                        state = C1G1R1E32
                        break
			

def C1G0R1E33():#17
	print('state17(C1G0R1E33)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R1E33
			break

def C1G1R1E32():#18
	print('state18(C1G1R1E32)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G1R1E32
			break
		elif newEvent == 'greenDone':
                        newEvent = 'none'
                        state = C1G0R1E33
                        break

def C0G1R1E32():#19
	print('state19(C0G1R1E32)')
	global state
	global newEvent

	while True:
		if newEvent == 'greenDone':
			newEvent = 'none'
			state = C1G0R1E33
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
