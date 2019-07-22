from settings import PROJECT_ROOT
import os

def main():
    print(PROJECT_ROOT + "\\UsersReplies")
    path = PROJECT_ROOT + "\\UsersReplies"
    pathCSV = PROJECT_ROOT + "\\UsersReplies\\fileDataCSV.txt"
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if 'Metrics.txt' in file:
                files.append(os.path.join(r, file))
    first = True
    csvFile = open(pathCSV,"w+")
    for f in files:
        file = open( f , "r")
        if ( first ):
            csvFile.write( ";".join( file.readline().strip().split(",") ) + "\n" )
            csvFile.write( ";".join( file.readline().strip().split(",") ) + "\n" )
            first = False
        else:
            file.readline()
            csvFile.write( ";".join( file.readline().strip().split(",") ) + "\n" )
        print(f)
        file.close()
    csvFile.close()

if __name__ == '__main__':
    main() 