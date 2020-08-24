########################################################################
########################################################################
############################## Question 1 ##############################
########################################################################
########################################################################

def hmmQ1(iteration, evidence,observations,probabilities):
    current=[1,0,0,0]
    previous=[0,0,0,0]
    for iter in range(iteration):                    # for each itration of hmm 
           previous.clear()
           for i in current:
               previous.append(i)
           observeProb = 0

           for j in range(len(current)):  # for each variable to be caculated in current
               item = 0.0
               
               for k in range(len(previous)):
                   if(evidence[iter] != -1) :
                       item += previous[k]*probabilities[k][j]*observations[j][evidence[iter]]
                       observeProb += previous[k]*probabilities[k][j]*observations[j][evidence[iter]]
                   else :
                       item += previous[k]*probabilities[k][j]
                    
               current[j] = item
           if(evidence[iter] != -1) :
                   current=[x / observeProb for x in current]
    
    return current


#
#    data structures
#
probabilities=[
    [0,0.5,0,0.5], #S0
    [0,0.5,0.5,0], #S1
    [0,0,0.5,0.5], #S2
    [0,0,0,1.0]    #S3
    ]
##print(probabilities[0][1])


obervations=[
    [1,1,1],
    [0.5,0.5,0.0],
    [0.5,0,0.5],
    [0,0.5,0.5]
    ]

#print(obervations[1][1])

print("#### Q1 P1")
evidence=[0,2,0,1]  # x0 y1 z2  NOINFO-1 
iteration=4
print( hmmQ1(iteration, evidence,obervations,probabilities) )

print("#### Q1 P2")
evidence=[0,2,0,1,-1]  # x0 y1 z2  NOINFO-1
iteration=5
print( hmmQ1(iteration, evidence,obervations,probabilities) )




########################################################################
########################################################################
############################## Question 2 ##############################
########################################################################
########################################################################



def hmmQ2(iteration, evidence,observations,probabilities):
    current=[1,0,0,0,0,0,0]
    previous=[0,0,0,0,0,0,0]
    for iter in range(iteration):                    # for each itration of hmm 
           previous.clear()
           for i in current:
               previous.append(i)
           observeProb = 0

           for j in range(len(current)):  # for each variable to be caculated in current
               item = 0.0
               
               for k in range(len(previous)):
                   if(evidence[iter] != -1) :
                       item += previous[k]*probabilities[k][j]*observations[j][evidence[iter]]
                       observeProb += previous[k]*probabilities[k][j]*observations[j][evidence[iter]]
                   else :
                       item += previous[k]*probabilities[k][j]
                    
               current[j] = item
           if(evidence[iter] != -1) :
                   current=[x / observeProb for x in current]
    
    return current

#
#    data structures
#
probabilities=[
    [0, 1,  0,  0,  0,  0,  0],     #S0
    [0, 0.5,0.5,0,  0,  0,  0],     #A
    [0, 0,  0.5,0.5,0,  0,  0],     #B
    [0, 0,  0,  0.5,0.5,0,  0],     #C
    [0, 0,  0,  0,  0.5,0.5,0],     #D
    [0, 0,  0,  0,  0,  0.5,0.5],   #E
    [0, 0,  0,  0,  0,  0,  1]      #F

    ]
##print(probabilities[0][1])


obervations=[
    [1,1], #S0
    [1,0], #A
    [0,1], #B
    [0,1], #C
    [1,0], #D
    [0,1], #E
    [0,1], #F
    ]


print("#### Q2 P1") 
evidence=[0,1,1]  # H0 C1 NOINFO-1 
iteration=3
print( hmmQ2(iteration, evidence,obervations,probabilities) )


print("#### Q2 P2") 
evidence=[0,1,1,-1]  # H0 C1 NOINFO-1
iteration=4
print( hmmQ2(iteration, evidence,obervations,probabilities) )








