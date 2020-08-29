import sys
import zipfile
import os

print("*******************")
print("**START*ZIP*BUILD**")
print("*******************")

list = ['a','b','c','d']
for name in list:
    try:
        f = open('./{}.txt'.format(name),'w')
    except:
        sys.exit("Filad to create {}.txt".format(name))
    f.close()
    try:
        zipfile.ZipFile('{}_{}.zip'.format(name, os.environ['VERSION']), mode='w').write("{}.txt".format(name))
    except:
        sys.exit("Filad to create {}_{}.zip".format(name, os.environ['VERSION']))
