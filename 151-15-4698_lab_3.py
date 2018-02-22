
# coding: utf-8

# In[10]:


x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
y = [0, 0, 0, 1]
w1 = 0.3
w2 = -0.1
n = 0.1 # Learning Rate
th = 0.2 

for i in range(5):
    error = []
    temp = []
    
    for j in range(len(x1)):
        y_pred =x1[j] * w1 + x2[j] * w2
        
        if y_pred < th:
            y_pred = 0
            
        else:
            y_pred = 1
        cost=y[j]-y_pred 
        temp.append(y_pred)
        error.append(cost)
        if temp == y:
            print('Final Result: ')
            print( 'Inputs:', x1[j], x2[j],'Outputs:', y[j], 'Old Weight:', w1_temp, w2_temp,
            'Output: ', y_pred, 'Cost:', cost, 'New Weight:', w1, w2)
            break
        else:
            # Updating the weights w1 and w2
            # Rule: Old weight + leraning rate * input * cost
            w1 = w1 + n * x1[j] * cost
            w1 = float("{0:.2f}".format(w1))
                
            w2 = w2 + n * x2[j] * cost
            w2 = float("{0:.2f}".format(w2))
        print( 'Inputs:', x1[j], x2[j],'Outputs:', y[j], 'Old Weight:', w1_temp, w2_temp,
            'Output: ', y_pred, 'Cost:', cost, 'New Weight:', w1, w2)

