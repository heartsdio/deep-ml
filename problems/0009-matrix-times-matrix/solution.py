import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

              ar_1 = np.array(a)
              ar_2 = np.array(b)
    
    
              if ar_1.shape[1] != ar_2.shape[0]:
                return -1
        
    
              return ar_1 @ ar_2

                
	            