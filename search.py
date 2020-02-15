import glob
import os
def search(dir,fname):
    os.chdir(dir )
    
    try:
        for files in glob.glob( "*.*" ):
            f = open( files, 'r' )
            file_contents = f.read()
            #if "AIzaSyAbg4XZm-68VmFtLnKWSAnNanO1oNTukT4" in file_contents:
            #if "AIzaSyDkM2fJKHovUnCx5AihUbQc136XgGutASc" in file_contents:
            if fname in file_contents:
                    print
                    print "*********************************************************************************"
                    print dir,"/", f.name
                    print "*********************************************************************************"
                    print
            f.close()
        os.walk(dir)
    except IOError:
        print "dir error"

dir =  os.getcwd()
fname = raw_input("Enter search keyword: ")
print "Iterating root directory"
search(dir,fname)
for x in os.walk(dir):
    dir = x[0]
    #print "Iterating dir: ", dir
    search(dir,fname)
