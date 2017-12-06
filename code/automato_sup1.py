#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Trabalho de Controle para Automação 2017/2
#Código de controle do robô cyton.
#Supervisório 1 (Peças verdes na máquina verde, peças vermelhas na máquina vermelha)
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
def init():#C0G0R0E10
	# Indica novo estado no log para debug
	print('init(C0G0R0E10)')
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
			state = C0G0R0E11
			# Sair do loop
			break
		elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C0G0R0E13
                        break

def C0G0R0E11():#1
	print('state1(C0G0R0E11)')

	global state
	global newEvent

        while True:
                if newEvent == 'greenLoad':
                        sendMovement(1)#greenLoad!
                        newEvent = 'none'
                        state = C1G1R0E10
                        break

def C1G0R0E11():#X1
	print('state3(C1G0R0E11)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E11
			break
	
def C0G0R0E12():#2
	print('state2(C0G0R0E12)')
	global state
	global newEvent

        while True:
                if newEvent == 'greenUnload':
                        sendMovement(3)#greenUnload!
                        newEvent = 'none'
                        state = C1G0R0E10
                        break
	

def C1G0R0E10():#3
	print('state3(C1G0R0E10)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = init#C0G0R0E10
			break
		elif newEvent == 'greenNew':
                        newEvent = 'none'
                        state = C1G0R0E11#X1
                        break
                elif newEvent == 'redNew':
                        newEvent = 'none'
                        state = C1G0R0E13#X2
                        break
def C1G0R0E13():#X2
	print('state3(C1G0R0E13)')
	global state
	global newEvent

	while True:
		if newEvent == 'cytonIdle':
			newEvent = 'none'
			state = C0G0R0E13  
			break

def C0G0R0E14():#4
        print('state4(C0G0R0E14)')
        global state
        global newEvent

        while True:
                if newEvent == 'redUnload':
                        sendMovement(2)#redUnload!
                        newEvent = 'none'
                        state = C1G0R0E10
                        break

                        
def C0G0R0E13():#5
        print('state5(C0G0R0E13)')
        global state
        global newEvent

        while True:
                if newEvent == 'redLoad':
                        sendMovement(0)#redLoad!
                        newEvent = 'none'
                        state = C1G0R1E10
                        break
        


def C1G0R0E12():#6
        print('state6(C1G0R0E12)')
        global state
        global newEvent

        while True:
                if newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G0R0E12
                        break



def C1G0R0E14():#7
        print('state7(C1G0R0E14)')
        global state
        global newEvent

        while True:
                if newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G0R0E14
                        break

def C1G1R0E10():#8
        print('state8(C1G1R0E10)')
        global state
        global newEvent

        while True:
                if newEvent =='greenDone':
                        newEvent = 'none'
                        state = C1G0R0E12
                        break
                elif newEvent =='redNew':
                        newEvent = 'none'
                        state = C1G1R0E13
                        break
                elif newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G1R0E10
                        break


def C1G0R1E10():#9
        print('state9(C1G0R1E10)')
        global state
        global newEvent

        while True:
                if newEvent =='redDone':
                        newEvent = 'none'
                        state = C1G0R0E14
                        break
                elif newEvent =='greenNew':
                        newEvent = 'none'
                        state = C1G0R1E11
                        break
                elif newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G0R1E10
                        break

def C1G1R0E13():#10
        print('state10(C1G1R0E13)')
        global state
        global newEvent

        while True:
                if newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G1R0E13
                        break

def C0G1R0E10():#11
        print('state11(C0G1R0E10)')
        global state
        global newEvent

        while True:
                if newEvent =='greenDone':
                        newEvent = 'none'
                        state = C0G0R0E12
                        break
                elif newEvent =='redNew':
                        newEvent = 'none'
                        state = C0G1R0E13
                        break

def C0G1R0E14():#12
        print('state12(C0G1R0E14)')
        global state
        global newEvent

        while True:
                if newEvent == 'redUnload':
                        sendMovement(2)#redUnload!
                        newEvent = 'none'
                        state = C1G1R0E10
                        break
                        

def C0G0R1E12():#13
        print('state13(C0G0R1E12)')
        global state
        global newEvent

        while True:
                if newEvent == 'greenUnload':
                        sendMovement(3)#greenUnload!
                        newEvent = 'none'
                        state = C1G0R1E10
                        break
                        

def C0G0R1E10():#14
        print('state14(C0G0R1E10)')
        global state
        global newEvent

        while True:
                if newEvent =='redDone':
                        newEvent = 'none'
                        state = C0G0R0E14
                        break
                elif newEvent =='greenNew':
                        newEvent = 'none'
                        state = C0G0R1E11
                        break

def C1G0R1E11():#15 C1G0R1E11 +GREENnEW -CYTONIDLE
        print('state15(C1G0R1E11)')
        global state
        global newEvent

        while True:
                if newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G0R1E11
                        break

def C0G1R0E13():#16
        print('state16(C0G1R0E13)')
        global state
        global newEvent

        while True:
                if newEvent == 'redLoad':
                        sendMovement(0)#redLoad!
                        newEvent = 'none'
                        state = C1G1R1E10
                        break
                        

def C1G1R0E14():#17
        print('state17(C1G1R0E14)')
        global state
        global newEvent

        while True:
                if newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G1R0E14
                        break
                
def C1G0R1E12():#18
        print('state18(C1G0R1E12)')
        global state
        global newEvent

        while True:
                if newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G0R1E12
                        break
                
def C0G0R1E11():#19
        print('state19(C0G0R1E11)')
        global state
        global newEvent

        while True:
                if newEvent == 'greenLoad':
                        sendMovement(1)#greenLoad
                        newEvent = 'none'
                        state = C1G1R1E10
                        break
                        
def C1G1R1E10():#20
        print('state20(C1G1R1E10)')
        global state
        global newEvent

        while True:
                if newEvent =='redDone':
                        newEvent = 'none'
                        state = C1G1R0E14
                        break
                elif newEvent =='greenDone':
                        newEvent = 'none'
                        state = C1G0R1E12
                        break
                elif newEvent =='cytonIdle':
                        newEvent = 'none'
                        state = C0G1R1E10
                        break
                
def C0G1R1E10():#21
        print('state21(C0G1R1E10)')
        global state
        global newEvent

        while True:
                if newEvent =='redDone':
                        newEvent = 'none'
                        state = C0G1R0E14
                        break
                elif newEvent =='greenDone':
                        newEvent = 'none'
                        state = C0G0R1E12
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
