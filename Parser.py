from antlr4 import *
from Grammar.dist.GrammarLexer import GrammarLexer
from Grammar.dist.GrammarParser import GrammarParser
from Grammar.Visitor import *
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error: " + msg + " at line " + str(line) + ':' + str(column))

def parseInputFile(filename) :
    program = open(filename, "r")
    program.seek(0)
    
    # split input into: pre, post and pgcl
    data = program.read().split(',')
    
    initiateVars = True if len(data) == 4 else False
    if len(data) == 4 :
        initiateVars = True
    
    # print("\nDATA:\n", data)
    pre = data[0] 
    post = data[1] 
    
    if initiateVars :
        init = data[2]
        pgcl = data[3]
    else :
        pgcl = data[2]
    
    visitor = Visitor()
    
    # Parse pre-expectation (constraint):
    dataPre = InputStream(pre)
    lexerPre = GrammarLexer(dataPre)
    lexerPre.addErrorListener(MyErrorListener())
    streamPre = CommonTokenStream(lexerPre)
    parserPre = GrammarParser(streamPre)
    parserPre.addErrorListener(MyErrorListener())
    treePre = parserPre.preexpectation()
    #print ("pre tree:\n", treePre.toStringTree(recog=parserPre));
    nodePre = visitor.visit(treePre)
    
   # print(nodePre)
    if isinstance(nodePre, Constraint) :
        if nodePre.exp is None :
            raise Exception("Unable to parse pre-expectation")
    
    # Parse post-expectation:
    dataPost = InputStream(post)
    lexerPost = GrammarLexer(dataPost)
    streamPost = CommonTokenStream(lexerPost)
    parserPost = GrammarParser(streamPost)
    parserPost.addErrorListener(MyErrorListener())
    treePost = parserPost.postexpectation()
    nodePost = visitor.visit(treePost)

    if nodePost is None :
        raise Exception("Unable to parse post-expectation")

    if initiateVars :
        #parse variable initializaion
        dataInit = InputStream(init)
        lexerInit = GrammarLexer(dataInit)
        streamInit = CommonTokenStream(lexerInit)
        parserInit = GrammarParser(streamInit)
        parserInit.addErrorListener(MyErrorListener())
        treeInit = parserInit.inits()
        #print ("init tree:\n", treeInit.toStringTree(recog=parserInit));
        nodeInit = visitor.visit(treeInit)
    else :
        nodeInit = None
    
    # Parse pgcl program:
    dataPGCL = InputStream(pgcl)
    lexerPGCL = GrammarLexer(dataPGCL)
    streamPGCL = CommonTokenStream(lexerPGCL)
    parserPGCL = GrammarParser(streamPGCL)
    parserPGCL.addErrorListener(MyErrorListener())
    treePGCL = parserPGCL.program()
    #print ("pgcl tree:\n", treePGCL.toStringTree(recog=parserPGCL));
    nodePGCL = visitor.visit(treePGCL)
    
    if nodePGCL is None :
        raise Exception("Unable to parse pgcl program")
    
    return nodePre, nodePost, nodeInit, nodePGCL
    
