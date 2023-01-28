import sys
from NonNegCheck import *
from ProbabilityCheck import *
from Benchmarks import *
from WeakestPreexpectation import *
from WPOld import *
from PRISMConverter import *
from PrettyPrinter import *
from Parser import *
from ExtractVars import *
from Z3Solver import *
from CVC5Solver import *

########################### MAIN ###########################


if __name__ == "__main__":
    inputFile = sys.argv[1]

    if (len(sys.argv) > 2) :
        nonnegFlag = True if sys.argv[2] == "true" else False
        probFlag = True if sys.argv[3] == "true" else False
        z3Flag = True if sys.argv[4] == "true" else False
        cvc5Flag = True if sys.argv[5] == "true" else False
    else :
        nonnegFlag = True 
        probFlag = True 
        z3Flag = True
        cvc5Flag = True 

    pre, post, init, pgcl = parseInputFile(inputFile)
    #print("\nConstraint:\n", pre, "\n\nPost:\n", post, "\n\nInit:\n", init, "\n\nPGCL:\n", pgcl, "\n")
    
    vars = list(extractVariables(pgcl, set()))

    if nonnegFlag :
        nonNeg = nonNegAnalysis(pgcl, GEqBexpr(post, AExp(IntNum(0))))
        #print("\nNonNeg:\n", nonNeg, '\n')
    
    if probFlag :
        pbCheck = probAnalysis(pgcl, Boool(True))
        #print("\nprobCheck:\n", pbCheck, '\n')

    if z3Flag :
        try :
            solver = "z3"
            
            if probFlag :
                if not (probCheckZ3(pbCheck, vars)) :
                    print("WARNING! (Z3) The program contains a probability that may be outside the interval [0;1]")
                    #raise Exception("WARNING! (Z3) The program contains a probability outside the interval [0;1]")
            
            if nonnegFlag :
                if not (nonNegZ3(nonNeg, vars)) :
                    raise Exception("Invalid program (Z3). Program must be non-negative.")
            
            g = wp(pgcl, post)
            #print("\nWP:\n", g)
            
            g = multiplyGuards(g)
            #print("\nG: \n", g, "\n")
            g = invCheck(g, solver, vars)
            #print("\ninv: \n", g, "\n")
            
            isSat = "Sat" if solveZ3(g, pre, vars) else "Unsat"
            print("Z3: " + isSat)
            
        except Exception as e :
            #raise Exception(e)
            print(e)
    
    if cvc5Flag :
        try :
            solver = "cvc5"

            if probFlag :
                if not (probCheckCVC5(pbCheck, vars)) :
                    print("WARNING! (CVC5) The program contains a probability that may be outside the interval [0;1]")
                    #raise Exception("WARNING! (CVC5) The program contains a probability outside the interval [0;1]")
                    
            if nonnegFlag :
                if not (nonNegCVC5(nonNeg, vars)) :
                    raise Exception("Invalid program (CVC5). Program must be non-negative.")
                
            g = wp(pgcl, post)
            g = multiplyGuards(g)

            g = invCheck(g, solver, vars)
            #print("\nWP:\n", g, "\n")
            isSat = "Sat" if solveCVC5(g, pre, vars) else "Unsat"
            print("CVC5: " + isSat)
            #print("g: " + exprToString(g))
        except Exception as e :
            #raise Exception(e)
            print(e)

    
        
    
