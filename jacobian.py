import numpy as np

def oldJacobian(q):
    jacobian_array = np.zeros(42)
    jacobian_array[0]=0.384*np.cos(q[0])*np.sin(q[2])*np.sin(q[3]) - 0.31599*np.sin(q[0])*\
    np.sin(q[1]) - 0.384*np.cos(q[3])*np.sin(q[0])*np.sin(q[1]) - 0.08249*np.cos(q[0])*\
    np.sin(q[2]) + 0.08249*np.sin(q[0])*np.sin(q[1])*np.sin(q[3]) - 0.08249*np.cos(q[1])*\
    np.cos(q[2])*np.sin(q[0]) + 0.08249*np.cos(q[0])*np.cos(q[3])*np.sin(q[2]) + 0.08249*\
    np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.sin(q[0]) - 0.0879*np.cos(q[0])*np.cos(q[2])*\
    np.cos(q[5])*np.sin(q[4]) + 0.384*np.cos(q[1])*np.cos(q[2])*np.sin(q[0])*np.sin(q[3]) +\
        0.1069*np.cos(q[3])*np.cos(q[5])*np.sin(q[0])*np.sin(q[1]) - 0.1069*np.cos(q[0])*\
        np.cos(q[5])*np.sin(q[2])*np.sin(q[3]) - 0.1069*np.cos(q[0])*np.cos(q[2])*np.sin(q[4])*\
        np.sin(q[5]) - 0.0879*np.cos(q[3])*np.sin(q[0])*np.sin(q[1])*np.sin(q[5]) +\
        0.0879*np.cos(q[0])*np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[0])*\
        np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[2]) - 0.1069*np.cos(q[1])*np.cos(q[2])*\
        np.cos(q[5])*np.sin(q[0])*np.sin(q[3]) - 0.1069*np.cos(q[0])*np.cos(q[3])*np.cos(q[4])*\
        np.sin(q[2])*np.sin(q[5]) + 0.0879*np.cos(q[1])*np.cos(q[2])*np.sin(q[0])*np.sin(q[3])*\
        np.sin(q[5]) + 0.0879*np.cos(q[1])*np.cos(q[5])*np.sin(q[0])*np.sin(q[2])*np.sin(q[4]) -\
        0.0879*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*np.sin(q[1])*np.sin(q[3]) + 0.1069*\
        np.cos(q[1])*np.sin(q[0])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.1069*np.cos(q[4])*\
        np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[1])*np.cos(q[2])*\
        np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[0]) - 0.1069*np.cos(q[1])*np.cos(q[2])*\
        np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[5])\


    jacobian_array[1]=0.31599*np.cos(q[0])*np.sin(q[1]) - 0.08249*np.sin(q[0])*np.sin(q[2]) - 0.08249*\
    np.cos(q[0])*np.sin(q[1])*np.sin(q[3]) + 0.08249*np.cos(q[3])*np.sin(q[0])*np.sin(q[2]) + 0.384*\
    np.sin(q[0])*np.sin(q[2])*np.sin(q[3]) + 0.08249*np.cos(q[0])*np.cos(q[1])*np.cos(q[2]) + 0.384*\
    np.cos(q[0])*np.cos(q[3])*np.sin(q[1]) - 0.08249*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[3]) - 0.384*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.sin(q[3]) - 0.1069*np.cos(q[0])*\
    np.cos(q[3])*np.cos(q[5])*np.sin(q[1]) + 0.0879*np.cos(q[0])*np.cos(q[3])*np.sin(q[1])*np.sin(q[5]) -\
    0.0879*np.cos(q[2])*np.cos(q[5])*np.sin(q[0])*np.sin(q[4]) - 0.1069*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[2])*np.sin(q[3]) - 0.1069*np.cos(q[2])*np.sin(q[0])*np.sin(q[4])*np.sin(q[5]) + 0.0879*\
    np.sin(q[0])*np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) + 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[5])*np.sin(q[3]) - 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.sin(q[3])*np.sin(q[5]) -\
    0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[5])*np.sin(q[2])*np.sin(q[4]) + 0.0879*np.cos(q[0])*\
    np.cos(q[4])*np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) - 0.0879*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[0])*np.sin(q[2]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) +\
    0.1069*np.cos(q[0])*np.cos(q[4])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) - 0.1069*np.cos(q[3])*\
    np.cos(q[4])*np.sin(q[0])*np.sin(q[2])*np.sin(q[5]) + 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[3])*np.cos(q[4])*np.cos(q[5]) + 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*\
    np.cos(q[4])*np.sin(q[5])


    jacobian_array[2]=0.0


    jacobian_array[3]=0.0


    jacobian_array[4]=0.0


    jacobian_array[5]=1.0



    jacobian_array[6]=0.31599*np.cos(q[0])*np.cos(q[1]) + 0.384*np.cos(q[0])*np.cos(q[1])*np.cos(q[3]) -\
    0.08249*np.cos(q[0])*np.cos(q[2])*np.sin(q[1]) - 0.08249*np.cos(q[0])*np.cos(q[1])*np.sin(q[3]) -\
    0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[3])*np.cos(q[5]) + 0.08249*np.cos(q[0])*np.cos(q[2])*\
    np.cos(q[3])*np.sin(q[1]) + 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[3])*np.sin(q[5]) + 0.384*\
    np.cos(q[0])*np.cos(q[2])*np.sin(q[1])*np.sin(q[3]) + 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[4])*\
    np.cos(q[5])*np.sin(q[3]) - 0.1069*np.cos(q[0])*np.cos(q[2])*np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) +\
    0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[4])*np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[0])*\
    np.cos(q[2])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[0])*np.cos(q[5])*np.sin(q[1])*\
    np.sin(q[2])*np.sin(q[4]) + 0.1069*np.cos(q[0])*np.sin(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) -\
    0.0879*np.cos(q[0])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[1]) - 0.1069*\
    np.cos(q[0])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[1])*np.sin(q[5])


    jacobian_array[7]=0.31599*np.cos(q[1])*np.sin(q[0]) - 0.08249*np.cos(q[2])*np.sin(q[0])*np.sin(q[1]) -\
    0.08249*np.cos(q[1])*np.sin(q[0])*np.sin(q[3]) + 0.384*np.cos(q[1])*np.cos(q[3])*np.sin(q[0]) -\
    0.1069*np.cos(q[1])*np.cos(q[3])*np.cos(q[5])*np.sin(q[0]) + 0.08249*np.cos(q[2])*np.cos(q[3])*\
    np.sin(q[0])*np.sin(q[1]) + 0.0879*np.cos(q[1])*np.cos(q[3])*np.sin(q[0])*np.sin(q[5]) + 0.384*\
    np.cos(q[2])*np.sin(q[0])*np.sin(q[1])*np.sin(q[3]) + 0.0879*np.cos(q[1])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[0])*np.sin(q[3]) - 0.1069*np.cos(q[2])*np.cos(q[5])*np.sin(q[0])*np.sin(q[1])*np.sin(q[3]) +\
    0.1069*np.cos(q[1])*np.cos(q[4])*np.sin(q[0])*np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[2])*\
    np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[5])*np.sin(q[0])*np.sin(q[1])*\
    np.sin(q[2])*np.sin(q[4]) + 0.1069*np.sin(q[0])*np.sin(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) -\
    0.0879*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*np.sin(q[1]) - 0.1069*\
    np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[1])*np.sin(q[5])


    jacobian_array[8]=0.08249*np.sin(q[1])*np.sin(q[3]) - 0.08249*np.cos(q[1])*np.cos(q[2]) - 0.384*np.cos(q[3])*\
    np.sin(q[1]) - 0.31599*np.sin(q[1]) - 0.0879*np.cos(q[3])*np.sin(q[1])*np.sin(q[5]) + 0.08249*np.cos(q[1])*\
    np.cos(q[2])*np.cos(q[3]) + 0.384*np.cos(q[1])*np.cos(q[2])*np.sin(q[3]) + 0.1069*np.cos(q[3])*np.cos(q[5])*\
    np.sin(q[1]) - 0.1069*np.cos(q[1])*np.cos(q[2])*np.cos(q[5])*np.sin(q[3]) + 0.0879*np.cos(q[1])*np.cos(q[2])*\
    np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[1])*np.cos(q[5])*np.sin(q[2])*np.sin(q[4]) - 0.0879*np.cos(q[4])*\
    np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) + 0.1069*np.cos(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.1069*\
    np.cos(q[4])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*\
    np.cos(q[4])*np.cos(q[5]) - 0.1069*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[5])


    jacobian_array[9] = -1.0*np.sin(q[0])


    jacobian_array[10]=np.cos(q[0])


    jacobian_array[11]=0.0




    jacobian_array[12]=0.384*np.cos(q[2])*np.sin(q[0])*np.sin(q[3]) - 0.08249*np.cos(q[2])*np.sin(q[0]) - 0.08249*np.cos(q[0])*\
    np.cos(q[1])*np.sin(q[2]) + 0.08249*np.cos(q[2])*np.cos(q[3])*np.sin(q[0]) + 0.08249*np.cos(q[0])*np.cos(q[1])*\
    np.cos(q[3])*np.sin(q[2]) + 0.384*np.cos(q[0])*np.cos(q[1])*np.sin(q[2])*np.sin(q[3]) - 0.1069*np.cos(q[2])*\
    np.cos(q[5])*np.sin(q[0])*np.sin(q[3]) + 0.0879*np.cos(q[2])*np.sin(q[0])*np.sin(q[3])*np.sin(q[5]) + 0.0879*\
    np.cos(q[5])*np.sin(q[0])*np.sin(q[2])*np.sin(q[4]) + 0.1069*np.sin(q[0])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) -\
    0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[5])*np.sin(q[4]) - 0.0879*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*\
    np.cos(q[5])*np.sin(q[0]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[5])*np.sin(q[2])*np.sin(q[3]) - 0.1069*np.cos(q[0])*\
    np.cos(q[1])*np.cos(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.1069*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*\
    np.sin(q[5]) + 0.0879*np.cos(q[0])*np.cos(q[1])*np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[0])*\
    np.cos(q[1])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[2]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[3])*\
    np.cos(q[4])*np.sin(q[2])*np.sin(q[5])


    jacobian_array[13]=0.08249*np.cos(q[0])*np.cos(q[2]) - 0.08249*np.cos(q[1])*np.sin(q[0])*np.sin(q[2]) - 0.08249*np.cos(q[0])*\
    np.cos(q[2])*np.cos(q[3]) - 0.384*np.cos(q[0])*np.cos(q[2])*np.sin(q[3]) + 0.1069*np.cos(q[0])*np.cos(q[2])*np.cos(q[5])*\
    np.sin(q[3]) + 0.08249*np.cos(q[1])*np.cos(q[3])*np.sin(q[0])*np.sin(q[2]) - 0.0879*np.cos(q[0])*np.cos(q[2])*np.sin(q[3])*\
    np.sin(q[5]) - 0.0879*np.cos(q[0])*np.cos(q[5])*np.sin(q[2])*np.sin(q[4]) + 0.384*np.cos(q[1])*np.sin(q[0])*np.sin(q[2])*\
    np.sin(q[3]) - 0.1069*np.cos(q[0])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) + 0.0879*np.cos(q[0])*np.cos(q[2])*np.cos(q[3])*\
    np.cos(q[4])*np.cos(q[5]) + 0.1069*np.cos(q[0])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[5]) - 0.0879*np.cos(q[1])*\
    np.cos(q[2])*np.cos(q[5])*np.sin(q[0])*np.sin(q[4]) - 0.1069*np.cos(q[1])*np.cos(q[5])*np.sin(q[0])*np.sin(q[2])*\
    np.sin(q[3]) - 0.1069*np.cos(q[1])*np.cos(q[2])*np.sin(q[0])*np.sin(q[4])*np.sin(q[5]) + 0.0879*np.cos(q[1])*np.sin(q[0])*\
    np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[1])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[2]) - 0.1069*np.cos(q[1])*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[2])*np.sin(q[5])


    jacobian_array[14]=0.08249*np.sin(q[1])*np.sin(q[2]) - 0.08249*np.cos(q[3])*np.sin(q[1])*np.sin(q[2]) - 0.384*np.sin(q[1])*\
    np.sin(q[2])*np.sin(q[3]) + 0.0879*np.cos(q[2])*np.cos(q[5])*np.sin(q[1])*np.sin(q[4]) + 0.1069*np.cos(q[5])*np.sin(q[1])*\
    np.sin(q[2])*np.sin(q[3]) + 0.1069*np.cos(q[2])*np.sin(q[1])*np.sin(q[4])*np.sin(q[5]) - 0.0879*np.sin(q[1])*np.sin(q[2])*\
    np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[1])*np.sin(q[2]) + 0.1069*np.cos(q[3])*\
    np.cos(q[4])*np.sin(q[1])*np.sin(q[2])*np.sin(q[5])


    jacobian_array[15]=np.cos(q[0])*np.sin(q[1])


    jacobian_array[16]=np.sin(q[0])*np.sin(q[1])


    jacobian_array[17]=np.cos(q[1])





    jacobian_array[18]=0.384*np.cos(q[3])*np.sin(q[0])*np.sin(q[2]) - 0.384*np.cos(q[0])*np.sin(q[1])*np.sin(q[3]) - 0.08249*\
    np.sin(q[0])*np.sin(q[2])*np.sin(q[3]) - 0.08249*np.cos(q[0])*np.cos(q[3])*np.sin(q[1]) - 0.384*np.cos(q[0])*\
    np.cos(q[1])*np.cos(q[2])*np.cos(q[3]) + 0.08249*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.sin(q[3]) + 0.1069*\
    np.cos(q[0])*np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) - 0.1069*np.cos(q[3])*np.cos(q[5])*np.sin(q[0])*np.sin(q[2]) -\
    0.0879*np.cos(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[3])*np.sin(q[0])*np.sin(q[2])*np.sin(q[5]) +\
    0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[5]) - 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[0])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[1]) + 0.1069*np.cos(q[0])*\
    np.cos(q[3])*np.cos(q[4])*np.sin(q[1])*np.sin(q[5]) + 0.0879*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*np.sin(q[2])*\
    np.sin(q[3]) + 0.1069*np.cos(q[4])*np.sin(q[0])*np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[0])*np.cos(q[1])*\
    np.cos(q[2])*np.cos(q[4])*np.cos(q[5])*np.sin(q[3]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[4])*\
    np.sin(q[3])*np.sin(q[5])


    jacobian_array[19]=0.08249*np.cos(q[0])*np.sin(q[2])*np.sin(q[3]) - 0.08249*np.cos(q[3])*np.sin(q[0])*np.sin(q[1]) - 0.384*\
    np.sin(q[0])*np.sin(q[1])*np.sin(q[3]) - 0.384*np.cos(q[0])*np.cos(q[3])*np.sin(q[2]) - 0.384*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[3])*np.sin(q[0]) + 0.1069*np.cos(q[0])*np.cos(q[3])*np.cos(q[5])*np.sin(q[2]) + 0.08249*np.cos(q[1])*np.cos(q[2])*\
    np.sin(q[0])*np.sin(q[3]) - 0.0879*np.cos(q[0])*np.cos(q[3])*np.sin(q[2])*np.sin(q[5]) + 0.1069*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[1])*np.sin(q[3]) - 0.0879*np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) + 0.1069*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[3])*np.cos(q[5])*np.sin(q[0]) - 0.0879*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.sin(q[0])*np.sin(q[5]) + 0.0879*\
    np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*np.sin(q[1]) - 0.0879*np.cos(q[0])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[2])*np.sin(q[3]) + 0.1069*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[1])*np.sin(q[5]) - 0.1069*np.cos(q[0])*\
    np.cos(q[4])*np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[1])*np.cos(q[2])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[0])*np.sin(q[3]) - 0.1069*np.cos(q[1])*np.cos(q[2])*np.cos(q[4])*np.sin(q[0])*np.sin(q[3])*np.sin(q[5]) 


    jacobian_array[20]=0.384*np.cos(q[2])*np.cos(q[3])*np.sin(q[1]) - 0.384*np.cos(q[1])*np.sin(q[3]) - 0.08249*np.cos(q[2])*\
    np.sin(q[1])*np.sin(q[3]) - 0.0879*np.cos(q[1])*np.sin(q[3])*np.sin(q[5]) - 0.08249*np.cos(q[1])*np.cos(q[3]) + 0.1069*\
    np.cos(q[1])*np.cos(q[5])*np.sin(q[3]) + 0.0879*np.cos(q[1])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5]) - 0.1069*np.cos(q[2])*\
    np.cos(q[3])*np.cos(q[5])*np.sin(q[1]) + 0.1069*np.cos(q[1])*np.cos(q[3])*np.cos(q[4])*np.sin(q[5]) + 0.0879*np.cos(q[2])*\
    np.cos(q[3])*np.sin(q[1])*np.sin(q[5]) + 0.0879*np.cos(q[2])*np.cos(q[4])*np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) + 0.1069*\
    np.cos(q[2])*np.cos(q[4])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5])


    jacobian_array[21]=np.cos(q[2])*np.sin(q[0]) + np.cos(q[0])*np.cos(q[1])*np.sin(q[2])


    jacobian_array[22]=np.cos(q[1])*np.sin(q[0])*np.sin(q[2]) - 1.0*np.cos(q[0])*np.cos(q[2])


    jacobian_array[23]=-1.0*np.sin(q[1])*np.sin(q[2])




    jacobian_array[24]=0.0879*np.cos(q[3])*np.cos(q[5])*np.sin(q[0])*np.sin(q[2])*np.sin(q[4]) - 0.1069*np.cos(q[2])*\
    np.cos(q[4])*np.sin(q[0])*np.sin(q[5]) - 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[2]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[4])*np.sin(q[2])*np.sin(q[5]) - 0.0879*np.cos(q[0])*\
    np.cos(q[5])*np.sin(q[1])*np.sin(q[3])*np.sin(q[4]) - 0.0879*np.cos(q[2])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[0]) - 0.1069*np.cos(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[4])*np.sin(q[5]) + 0.1069*\
    np.cos(q[3])*np.sin(q[0])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.0879*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[3])*np.cos(q[5])*np.sin(q[4]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.sin(q[4])*np.sin(q[5])


    jacobian_array[25]=0.0879*np.cos(q[0])*np.cos(q[2])*np.cos(q[4])*np.cos(q[5]) + 0.1069*np.cos(q[0])*np.cos(q[2])*np.cos(q[4])*\
    np.sin(q[5]) - 0.0879*np.cos(q[1])*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*np.sin(q[2]) - 0.0879*np.cos(q[0])*np.cos(q[3])*\
    np.cos(q[5])*np.sin(q[2])*np.sin(q[4]) - 0.1069*np.cos(q[1])*np.cos(q[4])*np.sin(q[0])*np.sin(q[2])*np.sin(q[5]) - 0.1069*\
    np.cos(q[0])*np.cos(q[3])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.0879*np.cos(q[5])*np.sin(q[0])*np.sin(q[1])*\
    np.sin(q[3])*np.sin(q[4]) - 0.1069*np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[4])*np.sin(q[5]) - 0.0879*np.cos(q[1])*\
    np.cos(q[2])*np.cos(q[3])*np.cos(q[5])*np.sin(q[0])*np.sin(q[4]) - 0.1069*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*\
    np.sin(q[0])*np.sin(q[4])*np.sin(q[5])


    jacobian_array[26]=0.0879*np.cos(q[4])*np.cos(q[5])*np.sin(q[1])*np.sin(q[2]) - 0.0879*np.cos(q[1])*np.cos(q[5])*np.sin(q[3])*\
    np.sin(q[4]) + 0.1069*np.cos(q[4])*np.sin(q[1])*np.sin(q[2])*np.sin(q[5]) - 0.1069*np.cos(q[1])*np.sin(q[3])*np.sin(q[4])*\
    np.sin(q[5]) + 0.0879*np.cos(q[2])*np.cos(q[3])*np.cos(q[5])*np.sin(q[1])*np.sin(q[4]) + 0.1069*np.cos(q[2])*np.cos(q[3])*\
    np.sin(q[1])*np.sin(q[4])*np.sin(q[5])


    jacobian_array[27]=np.sin(q[0])*np.sin(q[2])*np.sin(q[3]) + np.cos(q[0])*np.cos(q[3])*\
    np.sin(q[1]) - 1.0*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.sin(q[3])


    jacobian_array[28]=np.cos(q[3])*np.sin(q[0])*np.sin(q[1]) - 1.0*np.cos(q[0])*\
    np.sin(q[2])*np.sin(q[3]) - 1.0*np.cos(q[1])*np.cos(q[2])*np.sin(q[0])*np.sin(q[3])


    jacobian_array[29]=np.cos(q[1])*np.cos(q[3]) + np.cos(q[2])*np.sin(q[1])*np.sin(q[3])




    jacobian_array[30]=0.0879*np.cos(q[0])*np.cos(q[3])*np.cos(q[5])*np.sin(q[1]) + 0.1069*\
    np.cos(q[0])*np.cos(q[3])*np.sin(q[1])*np.sin(q[5]) - 0.1069*np.cos(q[2])*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[4]) + 0.0879*np.cos(q[5])*np.sin(q[0])*np.sin(q[2])*np.sin(q[3]) + 0.0879*np.cos(q[2])*np.sin(q[0])*\
    np.sin(q[4])*np.sin(q[5]) + 0.1069*np.sin(q[0])*np.sin(q[2])*np.sin(q[3])*np.sin(q[5]) - 0.0879*np.cos(q[0])*\
    np.cos(q[1])*np.cos(q[2])*np.cos(q[5])*np.sin(q[3]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.sin(q[3])*\
    np.sin(q[5]) - 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[5])*np.sin(q[2])*np.sin(q[4]) + 0.1069*np.cos(q[0])*\
    np.cos(q[4])*np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) - 0.1069*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*\
    np.sin(q[0])*np.sin(q[2]) + 0.0879*np.cos(q[0])*np.cos(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.0879*np.cos(q[0])*\
    np.cos(q[4])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) + 0.0879*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[2])*\
    np.sin(q[5]) + 0.1069*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5]) - 0.0879*\
    np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[5])


    jacobian_array[31]=0.1069*np.cos(q[0])*np.cos(q[2])*np.cos(q[5])*np.sin(q[4]) + 0.0879*np.cos(q[3])*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[1]) - 0.0879*np.cos(q[0])*np.cos(q[5])*np.sin(q[2])*np.sin(q[3]) - 0.0879*np.cos(q[0])*np.cos(q[2])*np.sin(q[4])*\
    np.sin(q[5]) + 0.1069*np.cos(q[3])*np.sin(q[0])*np.sin(q[1])*np.sin(q[5]) - 0.1069*np.cos(q[0])*np.sin(q[2])*np.sin(q[3])*\
    np.sin(q[5]) + 0.1069*np.cos(q[0])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[2]) - 0.0879*np.cos(q[1])*np.cos(q[2])*\
    np.cos(q[5])*np.sin(q[0])*np.sin(q[3]) - 0.0879*np.cos(q[0])*np.cos(q[3])*np.cos(q[4])*np.sin(q[2])*np.sin(q[5]) - 0.1069*\
    np.cos(q[1])*np.cos(q[2])*np.sin(q[0])*np.sin(q[3])*np.sin(q[5]) - 0.1069*np.cos(q[1])*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[2])*np.sin(q[4]) + 0.1069*np.cos(q[4])*np.cos(q[5])*np.sin(q[0])*np.sin(q[1])*np.sin(q[3]) + 0.0879*np.cos(q[1])*\
    np.sin(q[0])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.0879*np.cos(q[4])*np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*\
    np.sin(q[5]) + 0.1069*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[0]) - 0.0879*np.cos(q[1])*\
    np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[5])


    jacobian_array[32]=0.0879*np.cos(q[1])*np.cos(q[3])*np.cos(q[5]) + 0.1069*np.cos(q[1])*np.cos(q[3])*np.sin(q[5]) + 0.1069*\
    np.cos(q[1])*np.cos(q[4])*np.cos(q[5])*np.sin(q[3]) + 0.0879*np.cos(q[2])*np.cos(q[5])*np.sin(q[1])*np.sin(q[3]) - 0.0879*\
    np.cos(q[1])*np.cos(q[4])*np.sin(q[3])*np.sin(q[5]) + 0.1069*np.cos(q[2])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) + 0.1069*\
    np.cos(q[5])*np.sin(q[1])*np.sin(q[2])*np.sin(q[4]) - 0.0879*np.sin(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) - 0.1069*\
    np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.cos(q[5])*np.sin(q[1]) + 0.0879*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*\
    np.sin(q[1])*np.sin(q[5])


    jacobian_array[33]=np.cos(q[2])*np.cos(q[4])*np.sin(q[0]) + np.cos(q[0])*np.cos(q[1])*np.cos(q[4])*np.sin(q[2]) + 1.0*\
    np.cos(q[0])*np.sin(q[1])*np.sin(q[3])*np.sin(q[4]) - 1.0*np.cos(q[3])*np.sin(q[0])*np.sin(q[2])*np.sin(q[4]) + 1.0*\
    np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.sin(q[4])


    jacobian_array[34]=np.cos(q[1])*np.cos(q[4])*np.sin(q[0])*np.sin(q[2]) - 1.0*np.cos(q[0])*np.cos(q[2])*\
    np.cos(q[4]) + np.cos(q[0])*np.cos(q[3])*np.sin(q[2])*np.sin(q[4]) + np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*\
    np.sin(q[4]) + np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.sin(q[0])*np.sin(q[4])


    jacobian_array[35]=np.cos(q[1])*np.sin(q[3])*np.sin(q[4]) - 1.0*np.cos(q[4])*\
    np.sin(q[1])*np.sin(q[2]) - 1.0*np.cos(q[2])*np.cos(q[3])*np.sin(q[1])*np.sin(q[4])

    jacobian_array[36]=0


    jacobian_array[37]=0


    jacobian_array[38]=0


    jacobian_array[39]=1.0*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[5])*np.sin(q[3]) - 1.0*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[2])*np.sin(q[3]) - 1.0*np.cos(q[2])*np.sin(q[0])*np.sin(q[4])*np.sin(q[5]) - 1.0*np.cos(q[0])*np.cos(q[3])*\
    np.cos(q[5])*np.sin(q[1]) - 1.0*np.cos(q[0])*np.cos(q[1])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) + 1.0*np.cos(q[0])*\
    np.cos(q[4])*np.sin(q[1])*np.sin(q[3])*np.sin(q[5]) - 1.0*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[2])*\
    np.sin(q[5]) + 1.0*np.cos(q[0])*np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[5])


    jacobian_array[40]=1.0*np.cos(q[0])*np.cos(q[5])*np.sin(q[2])*np.sin(q[3]) - 1.0*np.cos(q[3])*np.cos(q[5])*np.sin(q[0])*\
    np.sin(q[1]) + 1.0*np.cos(q[0])*np.cos(q[2])*np.sin(q[4])*np.sin(q[5]) + 1.0*np.cos(q[1])*np.cos(q[2])*np.cos(q[5])*\
    np.sin(q[0])*np.sin(q[3]) + np.cos(q[0])*np.cos(q[3])*np.cos(q[4])*np.sin(q[2])*np.sin(q[5]) - 1.0*np.cos(q[1])*\
    np.sin(q[0])*np.sin(q[2])*np.sin(q[4])*np.sin(q[5]) + np.cos(q[4])*np.sin(q[0])*np.sin(q[1])*np.sin(q[3])*\
    np.sin(q[5]) + np.cos(q[1])*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[0])*np.sin(q[5])


    jacobian_array[41]=np.cos(q[1])*np.cos(q[4])*np.sin(q[3])*np.sin(q[5]) - 1.0*np.cos(q[2])*np.cos(q[5])*np.sin(q[1])*\
    np.sin(q[3]) - 1.0*np.cos(q[1])*np.cos(q[3])*np.cos(q[5]) + 1.0*np.sin(q[1])*np.sin(q[2])*np.sin(q[4])*\
    np.sin(q[5]) - 1.0*np.cos(q[2])*np.cos(q[3])*np.cos(q[4])*np.sin(q[1])*np.sin(q[5])

    return jacobian_array

class DualNumber:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real,
                              self.dual + other.dual)
        else:
            return DualNumber(self.real + other, self.dual)
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real,
                              self.dual - other.dual)
        else:
            return DualNumber(self.real - other, self.dual)

    def __rsub__(self, other):
        return DualNumber(other, 0) - self

    def __mul__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real * other.real,
                              self.real * other.dual + self.dual * other.real)
        else:
            return DualNumber(self.real * other, self.dual * other)
    __rmul__ = __mul__

    def __div__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real/other.real,
                              (self.dual*other.real - self.real*other.dual)/(other.real**2))
        else:
            return (1/other) * self

    def __rdiv__(self, other):
        return DualNumber(other, 0).__div__(self)

    def __pow__(self, other):
        return DualNumber(self.real**other,
                          self.dual * other * self.real**(other - 1))

    def __repr__(self):
        return repr(self.real) + ' + ' + repr(self.dual) + '

def transformFromDH(lastA, d, lastAlpha, angle):
    return np.array([
        [np.cos(angle), -np.sin(angle), 0, lastA],
        [np.sin(angle)*np.cos(lastAlpha), np.cos(angle)*np.cos(lastAlpha), -np.sin(lastAlpha), -d*np.sin(lastAlpha)],
        [np.sin(angle)*np.sin(lastAlpha), np.cos(angle)*np.sin(lastAlpha), np.cos(lastAlpha), d*np.cos(lastAlpha)],
        [0, 0, 0, 1],
    ])

def kinematics(q):
    transform = transformFromDH(0, 0.333, 0, q[0]) * \
            transformFromDH(0, 0, 0, q[1]) * \
            transformFromDH(0, 0.316, - np.pi/2, q[2]) * \
            transformFromDH(0, 0, np.pi/2, q[3]) * \
            transformFromDH(0.0825, 0.384, np.pi/2, q[4]) * \
            transformFromDH(-0.0825, 0, -np.pi/2, q[5]) * \
            transformFromDH(0, 0, np.pi/2, q[6]) * \
            transformFromDH(0.088, 0.107, np.pi/2, 0)
    

if __name__ == '__main__':
    print(oldJacobian([0,0,0,0,0,0]).reshape((6,7)))
    x = kinematics([DualNumber(theta,0) for theta in [0,0,0,0,0,0,0]])
    
