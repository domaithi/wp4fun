from PRISMConverter import *
from Parser import *

inputFile = sys.argv[1]
filename = sys.argv[2]

pre, post, init, pgcl = parseInputFile(inputFile)

print("\nConstraint:\n", pre, "\n\nPost:\n", post, "\n\nInit:\n", init, "\n\nPGCL:\n", pgcl, "\n")

prism, props = toPrism(pgcl, pre, post, init)
folder = "PRISM/"

# Prism file
prismFileName = filename + ".prism"
prismPath = folder + prismFileName
prismFile = open(prismPath,"w")
prismFile.write(prism)
prismFile.close()

# Props file
propsFileName = filename + ".props"
propsPath = folder + propsFileName
propsFile = open(propsPath, "w")
propsFile.write(props)
propsFile.close()
