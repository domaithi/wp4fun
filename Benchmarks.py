import random
from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *

def randomExpr(n):
    var = random.choice(["x", "y", "z"])
    if (n>1) :
        x = random.randint(1,16)
        if (x==1 or x==2) :
            return var
        elif (x==3) : # int
            return random.randint(0,99).__str__()
        elif (x==4) : # float
            return (random.random()*100).__str__()
        elif (x==5 or x==6 or x==7) : 
            return randomExpr(n-1) + "+" + randomExpr(n-1)
        elif(x==8 or x==9 or x==10) : 
            return  randomExpr(n-1) + "-" + randomExpr(n-1) 
        elif (x==11 or x==12 or x==13) : 
            return randomExpr(n-1) + "*" + randomExpr(n-1) 
        elif (x==14 or x==15 or x==16):
            return randomExpr(n-1) + "/" + randomExpr(n-1) 
    else :
        x = random.randint(1,4)
        if (x==1 or x==2) :
            return var
        elif (x==3) : # int
            return random.randint(0,99).__str__()
        elif (x==4) : # float
            return (random.random()*100).__str__()

def randomBExpr2(n):
    x = random.randint(1,7)
    if (n>1) :
        if (x==1) : 
            return randomExpr(n-1)
        elif (x==2) : 
            return randomBExpr2(n-1) + "=" + randomBExpr2(n-1) 
        elif (x==3) : 
            return randomBExpr2(n-1) + "!=" + randomBExpr2(n-1) 
        elif (x==4) : 
            return randomBExpr2(n-1) + ">=" + randomBExpr2(n-1) 
        elif (x==5) :
            return randomBExpr2(n-1) + ">" + randomBExpr2(n-1) 
        elif (x==6) : 
            return randomBExpr2(n-1) + "<=" + randomBExpr2(n-1) 
        elif (x==7) : 
            return randomBExpr2(n-1) + "<" + randomBExpr2(n-1) 
    else :
        return randomExpr(n-1)

def randomBExpr1(n):
    x = random.randint(1,4)
    if (x==1) : # and
        return randomBExpr1(n-1) + "&" + randomBExpr1(n-1)
    elif (x==2) : # or
        return randomBExpr1(n-1) + "|" + randomBExpr1(n-1)
    elif (x==3) : # neg
        return "!" + randomBExpr1(n-1)
    elif (x==4) :
        return randomBExpr2(n-1)

def whileLoops(n, var1):
    res = var1 + ":=100;\n"
    for i in range(1,n+1):
        if i%2 == 0: 
            # Increment
            res += "while (" + var1 + "<100) [" + var1 + "+[" + var1 + "<100]] {\n    " + var1 + ":=" + var1 + "+1\n}"
        else:
            #Decrement
            res += "while (" + var1 + ">1) [[" + var1 + ">1]] {\n    " + var1 + ":=" + var1 + "-1\n}"
            
        res += (";\n" if i<n else "")

    return res


def sequentialWhileLoops(n):
    if n > 10 :
        return "while (x<" + str(n) + " && y>" + str(n) + ") [y] {\n    y:=y-x\n};\n" + sequentialWhileLoops(n-10)
    else :
        return "while (x<" + str(n) + " && y>" + str(n) + ") [y] {\n    y:=y-x\n}"


def nestedWhileLoops(n, var, c):
    if n > 1 :
        return "while (" + var + ">" + str(c) + ") [" + var + "+[" + var + ">" + str(c) + "]] { \n     " +  nestedWhileLoops(n-1, var, c+1) + ";\n" + var+ ":=" + var + "-1\n }"
    else :
        return "while (" + var + ">" + str(c) + ") [" + var + "+[" + var + ">" + str(c) + "]] { \n     " + var + ":=" + var + "-1\n }"


def nestedProbs(n, var):
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    if (n>=1) :
        return "{" + nestedProbs(n-1, var) + "} ["+ min(n1,n2).__str__() + "/" + max(n1,n2).__str__() + "] {" +nestedProbs(n-1, var) + "}\n"
    else :
        return var + ":=" + n1.__str__()

def ifElse(n, var):
    value = random.randint(1,100)
    if (n>=1) :
        return var + ":=" + value.__str__() + ";\nif (" +var+ " > 50) {" + ifElse(n-1, var) + "} else {" + ifElse(n-1, var) + "}"
    else :
        return var + ":=" + value.__str__()
        
def nonDet(n, var):
    if (n>=1) :
        return "{" + nonDet(n-1, var) + "} [] {" + nonDet(n-1, var) + "}\n"
    else :
        return var + ":=" + random.randint(1,100).__str__()

def assignments(n, var) :
    s = ""
    while (n > 1):
        s += var + ":=" + var + " + " + random.randint(1,100).__str__() + ";\n"
        n -= 1    
    return s + var + ":=" + var + " + " + random.randint(1,100).__str__()


def mixed(n) :
    selector = random.randint(1,4)
    value = random.randint(1,100)
    var = random.choice(["x","y","z"])
    if (n>1) :
        if selector == 1: #prop
            n1 = random.randint(1,100)
            n2 = random.randint(1,100)
            return "{" + mixed(n-1) + "} ["+ min(n1,n2).__str__() + "/" + max(n1,n2).__str__() + "] {" + mixed(n-1)  + "}\n"
        elif selector == 2: #IfElse
            return "x:=" + value.__str__() + ";\nif (" + var +" > 50) {" + mixed(n-1) + "} else {" + mixed(n-1) + "}"
        elif selector == 3: #nonDet 
            return "{" + mixed(n-1) + "} [] {" + mixed(n-1) + "}\n"
        elif selector == 4:
            return mixed(n-1) + ";\n" + mixed(n-1) 
        elif selector == 5: #Assign
            return var + ":=" + randomExpr(random.randint(1,n-1)) 
    else :
        if selector == 1:
            return nestedProbs(1, var)
        elif selector == 2: 
            return ifElse(1, var)
        elif selector == 3: 
            return nonDet(1, var)
        elif selector == 4: 
            return assignments(1, var)


def printToFile(n, methodName) :
    folder = "Input/Generated/"+ methodName + "/"
    fileName = methodName + "_" + n.__str__() + ".pgcl"
    path = folder + fileName
    f = open(path,"w")
    param = n
    
    if methodName == "nestedProbs":
        f.write("pre: >= 50, post: x, init: x [0..100] -> 0,\n")
        f.write(nestedProbs(n, "x"))
        param = pow(2,n+1)
    elif methodName == "assignments" :
        temp = 100*n
        f.write("pre: <= 50, post: x/n, init: x [0.." + str(temp) + "] -> 0; n [0.." + str(n) + "] -> 0 ,\n")
        f.write("x:=0;\nn:=" + n.__str__() + ';\n')
        f.write(assignments(n,"x"))
    elif methodName == "ifElse" :
        f.write("pre: <= 50, post: x, init: x [0..100] -> 0,\n")
        f.write(ifElse(n,"x"))
        param = pow(2,n+1)
    elif methodName == "nonDet": 
        f.write("pre: >= 50, post: x, init: x [0..100] -> 0,\n")
        f.write(nonDet(n,"x"))
        param = pow(2,n+1)
    elif methodName == "mixed" :
        f.write("pre: > 1, post: x+y+z, init: ,\n")
        f.write("x:=0; y:=0; z:=0;")
        f.write(mixed(n))
    elif methodName == "whileLoops" :
        ran = random.randint(1,30)
        var1 = "y"
        f.write("pre: <= " + str(ran) + ", \npost: " + var1 + ", \ninit: " + var1 + " [0..100] -> 0,\n\n")
        f.write(whileLoops(n, var1))
    elif methodName == "nestedWhileLoops":
        ran1 = random.randint(1,30)
        var = "y"
        f.write("pre: <= " + str(ran1) + ", \npost: " + var + ", \ninit: " + var + " [0.." + str(n*2) + "] -> 0 ,\n\n")
        f.write(var + ":=" + str(n*2) + ";\n")
        f.write(nestedWhileLoops(n, var, 1))
    elif methodName == "sequentialWhileLoops":
        ran1 = random.randint(n*9,11*n)
        var = "y"
        y = n*10
        f.write("pre: <= " + str(ran1) + ", \npost: y,\ninit: y [0.." + str(n*11) + "] -> 0 ,\n\n")
        f.write("y:=" + str(y) + ";\n")
        f.write("x:=1;\n")
        f.write(sequentialWhileLoops(y))

    f.close()
    return (folder, fileName, param)


if __name__ == "__main__" :
    printToFile(10, "sequentialWhileLoops")