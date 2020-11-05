
import os.path


#Creacion de la carpeta que guardara las llaves en el directorio acutal
path = (os.getcwd() + "/ssh-keys" )

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


# Activando servicios de ssh-agent, creando y guardando una llave ssh privada y publica
os.system("eval `ssh-agent`")
os.system("ssh-keygen -q -t rsa -b 4096 -f " + path + "/id_rsa")
os.system("ssh-add "+ path +"/id_rsa")


# Ruta al archivo de texto con la lista de servidores para agregar y nombre de usuario
path = (os.getcwd() + "/servers.txt" )
user = input(" : Ingrese el usuario con permisos Administrativos :  ")

# Loop para determinar si los componentes necesarios existen, e iterar por cada uno de las direcciones ip en la lista de servidores
# para crear conexiones por ssh para autenticarse por primera vez y copiar la llave publica 
if os.path.isfile (path) :
    servers = open(os.getcwd() + "/servers.txt", 'r')
    current_server = servers.readlines()
    for l in current_server:
        os.system( "ssh-copy-id -i " + os.getcwd() + "/ssh-keys/id_rsa.pub "+ user +"@" + l)
        
                
else:
    print("Necesita proveer un archivo de servidores (servers.txt) ")