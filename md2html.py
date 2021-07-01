import os

def findAllFile(base, type):
    for root, _, fs in os.walk(base):
        for f in fs:
            if f.endswith(type):
                fullname = os.path.join(root, f)
                yield fullname

def indexGen():
    with open("index.md", 'w') as index:
        index.write("## Slides List \n")

        for file in findAllFile('./', '.html'):
            name = file.split('/')[-1]
            string_written = "["+name+"]"+"("+file+")"
            index.write("-"+" "+string_written+"\n")
    index.close()


def main():
    base = './'
    for file in findAllFile(base, '.md'):   
        print("find md file:", file)
        command = 'marp --html' + ' ' + file
        print("os command used:", command)
        ret = os.system(command)
        print("ret should be 0", ret)

    indexGen()

if __name__ == '__main__':
    main()
