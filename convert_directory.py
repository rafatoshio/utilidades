#convert all files in a directory based on major side
#usage:python  convert_directory.py [-dir /path/] [-extensao .jpg] [-append _v2][-majorSide 1500]

#################################################
__author__ = 'Toshio'
modificado = "30/03/2015"
versao = "v1.0" 
#################################################
descricao="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\
+     conversor de fotos de um diretorio                      +\n\
+                                                                        +\n\
+ autor: %-20s                                            +\n\
+ modificado: %-10s                                                 +\n\
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\
" % (__author__,modificado)

epilogo="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\
"

parser = argparse.ArgumentParser(description=descricao,epilog=epilogo,formatter_class=argparse.RawTextHelpFormatter,add_help=False)
parser.add_argument("-h","--help",help="mostra essa mensagem e sai\n\n",action="help")
parser.add_argument("-dir",help="path where images are [default=./]\n\n", \
                    default="./", action="store", metavar='/path/')
parser.add_argument("-extensao",help="file extension (JPG, png,...) [default=.JPG]\n\n", \
                    default=".JPG", action="store", metavar='.jpg')
parser.add_argument("-append",help="add at the end of the new image [default=_v2]\n\n", \
                    default="_v2", action="store", metavar='_v2')
parser.add_argument("-majorSide",help="size of the major side [default=1500]\n\n", \
                    default="1500", action="store", metavar='1500')                    
parser.add_argument('--version', help="mostra a versao do programa e sai",action='version', version='%s %s'%('%(prog)s',versao))
args = parser.parse_args()
###################################################################################################################################################


os.chdir(args.dir)
arquivos = os.listdir('./')

len_ext = len(args.extensao)

for a in arquivos:
    if a[-len_ext:] == args.extensao:
       file_base = a[:-(len_ext)]
       nova_img = file_base+args.append+args.extensao
       #identifica o lado maior (em alguns casos  o comando convert nao identifica a orientacao direito)
       p = subprocess.Popen(["identify",a],stdout=subprocess.PIPE)
       info_img,err = p.communicate()
       info_img = info_img.split()[2].split("x")
       #se for landscape
       if info_img[0] > info_img[1]:
        cmd = 'convert %s -resize "%s>" %s'%(a,args.majorSide,nova_img) #em teoria esse comando deveria funcionar para qualquer orientacao
        os.system(cmd)
       #se for portrait 
       else: 
        cmd = 'convert %s -geometry x%s %s'%(a,args.majorSide,nova_img)
        os.system(cmd)
