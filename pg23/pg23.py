import matplotlib.pyplot as plt
import numpy as np
import numpy as pd
xpoint=np.array([1,2,6,18])
ypoint=np.array([3,10,12,20])
plt.plot(xpoint,ypoint,marker='*',color="red",mec='y',mfc='g',markersize=11,
         linestyle='dotted')
plt.show()