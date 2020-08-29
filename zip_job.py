import sys
import zipfile
import os

print("*******************")
print("**START*ZIP*BUILD**")
print("*******************")

list = ['a','b','c','d']
for name in list:
    try:
        f = open('/tmp/zip_builds/{}.txt'.format(name),'w')
    except:
        sys.exit("Filad to create {}.txt".format(name))
    f.close()
    print("Build {}_{}.zip".format(name, os.environ['VERSION']))
    try:
        zipfile.ZipFile('/tmp/zip_builds/{}_{}.zip'.format(name, os.environ['VERSION']), mode='w').write("/tmp/zip_builds/{}.txt".format(name))
    except:
        sys.exit("Filad to create {}_{}.zip".format(name, os.environ['VERSION']))
