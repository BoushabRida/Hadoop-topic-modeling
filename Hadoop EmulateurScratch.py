import argparse #il permet d'affecter les inputs dans les variable (praser.add_argument)
import subprocess #il permet d'ecrire un code dans le terminal
import glob #peremt de donner tt les path avec une expression reguliare

parser = argparse.ArgumentParser()

parser.add_argument('--input', help='Do the bar option')
parser.add_argument('--output', help='Foo the progra')
parser.add_argument('--mapper', help='Foo the program')
parser.add_argument('--reducer', help='Foo the program')

args = parser.parse_args()
out = ""
for filename in glob.glob("{0}/*".format(args.input)): #glob il retourne une liste quand parcour
    p1 = subprocess.Popen("cat " + filename,
                          stdout=subprocess.PIPE, shell=True) #creation d'un processus qui execute le mapper
    p2 = subprocess.Popen("python " + args.mapper,
                          stdin=p1.stdout, stdout=subprocess.PIPE, shell=True)
    out += p2.communicate()[0]


result = subprocess.Popen("python " + args.reducer, stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE, shell=True).communicate(input=out)[0]


with open(args.output + "/output.txt", "w") as f:
    f.write(result)
