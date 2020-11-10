from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from Apps import Appss
from reseñas import Reseña
from Personas import Persona
from Solicitudes import solicitud

app = Flask(__name__)
CORS(app)

Usuarios = []
Aplicaciones =[]
Reseñas =[]
Soli =[]
#-------------------Usuario Pre-Establecidos-------------------------
Usuarios.append(Persona('Usuario','Maestro','admin','admin','admin','Administrador',''))

@app.route('/NewAppss', methods=['POST'])
def AgregarSolicitud():
    global Aplicaciones,Soli
    No =0
    for aplication in Aplicaciones:
            No = int(aplication.getIds())
            sums = No+1 

    titulo = request.json['title']
    url = request.json['url']
    categoria = request.json['category']
    descargas = request.json['download']
    descripcion = request.json['description']
    precio = request.json['price']
    like = request.json['like']
    
    print(sums)

    nuevo = solicitud(sums,titulo,url,categoria,descargas,descripcion,precio,like)
    Soli.append(nuevo)
    return jsonify({
                        'message':'Success',
                        'reason':'Se agrego la app'
                        })


@app.route('/DataSolicitud', methods=['GET'])
def ObtenerSolicitud():
    global Soli
    Datos = []
    for rq in Soli:
            Dato = {
                'ids': rq.getIds(),
                'titulo': rq.getTitulo(),
                'url': rq.getUrl(),
                'categoria': rq.getCategoria(),
                'descargas': rq.getDescargas(),
                'descripcion': rq.getDescripcion(),
                'precio': rq.getPrecio(),
                'likes': rq.getLikes()
                }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)   

    

@app.route('/', methods=['GET'])
def rutaInicial():
    print("Hola mundo (consola)")
    return("Hola mundo (web)")

@app.route('/Reseña', methods=['POST'])
def Reseña1():
    global Reseñas
    comentario = request.json['reseña']
    No = request.json['count']
    Name = request.json['usuario']


    nuevo = Reseña(comentario,No,Name)
    Reseñas.append(nuevo)
    return jsonify({
                        'message':'Success',
                        'reason':'Se agrego el usuario'
                        })        

@app.route('/DReseñas', methods=['GET'])
def obtenerReseña():
    global Reseñas
    Datos = []
    for comentario in Reseñas:
        Dato = {
            'ids': comentario.getIds(), 
            'reseña': comentario.getReseña(),
            'usuario': comentario.getUsuario() 
            }
        Datos.append(Dato)
    
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Login', methods=['POST'])
def Login():
    global Usuarios
    username = request.json['usuario']
    password = request.json['password']
    for usuario in Usuarios:
        if usuario.getUsuario() == username and usuario.getPassword() == password:
            if usuario.getRol() == "Administrador":
                Dato = {
                'message': 'Success2',
                }
                break
            else:
                Dato = {
                'message': 'Success',
                }
                break
        else:
            Dato = {
                'message': 'Failed',
            }
    respuesta = jsonify(Dato)
    return(respuesta)


@app.route('/NewPersonas', methods=['POST'])
def AgregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    confirm = request.json['confirm']
    rol = request.json['rol']
    encontrado = False

    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            encontrado = True
            break

    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })
    else:
        if password == confirm:
            print("Si son iguales")

            if len(nombre)>0 and len(username)>0 and len(password)>0 and len(apellido)>0:
                        nuevo = Persona(nombre,apellido,username,password,confirm,rol,"")
                        Usuarios.append(nuevo)
                        return jsonify({
                        'message':'Success',
                        'reason':'Se agrego el usuario'
                        })
            else:
                return jsonify({
                        'message':'Failed2',
                        'reason':'Problema con los campos, (Todos los campos son obligatorios).'
                    })     

        else:
            print("No son iguales")   
            return jsonify({
                    'message':'Failed1',
                    'reason':'Problema con los campos, (Verifique contraseña y confirmar contraseña).'
            })   
        






@app.route('/NewAdmin', methods=['POST'])
def AgregarAdmin():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    confirm = request.json['confirm']
    rol = request.json['rol']
    encontrado = False

    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            encontrado = True
            break

    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })
    else:
        if password == confirm:
            print("Si son iguales")

            if len(nombre)>0 and len(username)>0 and len(password)>0 and len(apellido)>0:
                        nuevo = Persona(nombre,apellido,username,password,confirm,rol,"")
                        Usuarios.append(nuevo)
                        return jsonify({
                        'message':'Success',
                        'reason':'Se agrego el usuario'
                        })
            else:
                return jsonify({
                        'message':'Failed2',
                        'reason':'Problema con los campos, (Todos los campos son obligatorios).'
                    })     

        else:
            print("No son iguales")   
            return jsonify({
                    'message':'Failed1',
                    'reason':'Problema con los campos, (Verifique contraseña y confirmar contraseña).'
            })   

@app.route('/DPersona/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre):
    global Usuarios
    for usuario in Usuarios:
        if usuario.getUsuario() == nombre:
            Dato = {
                'nombre': usuario.getNombre(), 
                'apellido': usuario.getApellido(),
                'usuario': usuario.getUsuario(),
                'password': usuario.getPassword(),
                'confirm': usuario.getConfirm(),
                'rol': usuario.getRol()
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta)


@app.route('/CountLike/<string:nombre1>', methods=['PUT'])
def NuevoLike(nombre1):
    global Aplicaciones
    like = int(request.json['count'])
    uno = int(request.json['suma']) 

    add = like+ uno

    for aplication in Aplicaciones:
                if aplication.getIds() == nombre1:
                    aplication.setLikes(add)
                    break
    return jsonify({
                            'message':'Success',
                            'reason':add
                            })

         


@app.route('/UPersonas/<string:nombre1>', methods=['PUT'])
def ActualizarPersona(nombre1):
    global Usuarios

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    confirm = request.json['confirm']
    rol = request.json['rol']
    encontrado = False

    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
            })
    else:
        if password == confirm:
            if len(nombre)>0 and len(username)>0 and len(password)>0 and len(apellido)>0:    
                        for usuario in Usuarios:
                            if  usuario.getUsuario() == nombre1:
                                usuario.setNombre(request.json['nombre'])
                                usuario.setApellido(request.json['apellido'])
                                usuario.setUsuario(request.json['usuario'])
                                usuario.setPassword(request.json['password'])
                                usuario.setConfirm(request.json['confirm'])
                                usuario.setRol(request.json['rol'])
                                break
                        return jsonify({
                        'message':'Success',
                        'reason':'Se modifico el usuario'
                        })
            else:
                return jsonify({
                        'message':'Failed2',
                        'reason':'Problema con los campos, (Todos los campos son obligatorios).'
                    })     

        else:
            print("No son iguales")   
            return jsonify({
                    'message':'Failed1',
                    'reason':'Problema con los campos, (Verifique contraseña y confirmar contraseña).'
            })       
    

@app.route('/listPersonas', methods=['GET'])
def listsPersonas():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
      
        Dato = {
            'nombre': usuario.getNombre(), 
            'apellido': usuario.getApellido(),
            'usuario': usuario.getUsuario(),
            'password': usuario.getPassword(),
            'confirm': usuario.getConfirm(),
            'rol': usuario.getRol()
            }
        Datos.append(Dato)

    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/DPersonass', methods=['GET'])
def obtenerPersonas():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato = {
            'nombre': usuario.getNombre(), 
            'apellido': usuario.getApellido(),
            'usuario': usuario.getUsuario(),
            'password': usuario.getPassword(),
            'confirm': usuario.getConfirm(),
            'rol': usuario.getRol()
            }
        Datos.append(Dato)
    
    return jsonify({"DATOS": Datos, "message": "LISTA DE TODOS LOS USUARIOS"})


@app.route('/DltApp/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Aplicaciones
    for i in range(len(Aplicaciones)):
        if nombre == Aplicaciones[i].getIds():
            del Aplicaciones[i]
            break
    return jsonify({'message':'Se elimino la app exitosamente'})

#CSV
@app.route('/Aplica', methods=['POST'])
def SavesApp():
    global Aplicaciones
    data = request.json
    for x in data['datos']:
        
        if len(x)>0 and x[0]!='Id':
            nuevo = Appss(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
            Aplicaciones.append(nuevo)
    return jsonify({
            'message':'Success',
            'reason':'Se agrego la app'
            })
  

@app.route('/Clients', methods=['POST'])
def SavesClients():
    global Usuarios
    data = request.json
    for x in data['datos']:
        
        if len(x)>0 and x[0]!='Nombre':
            nuevo = Persona(x[0], x[1], x[2], x[3],x[3],"Cliente",x[4])
            Usuarios.append(nuevo)
    return jsonify({
            'message':'Success',
            'reason':'Se agrego el cliente'
            })


@app.route('/DataClients', methods=['GET'])
def ResultClients():
    global Usuarios
    Datos = []
    for cliente in Usuarios:
      if cliente.getRol() != "Administrador":
        Dato = {
            'nombre': cliente.getNombre(),
            'apellido': cliente.getApellido(),
            'usuario': cliente.getUsuario(),
            'contraseña': cliente.getPassword(),
            'confirm': cliente.getConfirm(),
            'rol': cliente.getRol(),
            'foto': cliente.getFoto()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#CARGAR A TABLA
@app.route('/DataApp', methods=['GET'])
def ResultApp():
    global Aplicaciones
    Datos = []
    for aplication in Aplicaciones:
        Dato = {
            'ids': aplication.getIds(),
            'titulo': aplication.getTitulo(),
            'url': aplication.getUrl(),
            'categoria': aplication.getCategoria(),
            'descargas': aplication.getDescargas(),
            'descripcion': aplication.getDescripcion(),
            'precio': aplication.getPrecio(),
            'likes': aplication.getLikes()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Modificar App
@app.route('/DataApp/<string:nombre>', methods=['GET'])
def ObtenerApp(nombre):
    global Aplicaciones
    for aplication in Aplicaciones:
        if aplication.getIds() == nombre:
            Dato = {
                'ids': aplication.getIds(),
                'titulo': aplication.getTitulo(),
                'url': aplication.getUrl(),
                'categoria': aplication.getCategoria(),
                'descargas': aplication.getDescargas(),
                'descripcion': aplication.getDescripcion(),
                'precio': aplication.getPrecio(),
                'likes': aplication.getLikes()
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta)



@app.route('/UpdateApp/<string:nombre1>', methods=['PUT'])
def ActualizarApp(nombre1):
    global Aplicaciones

    ids = request.json['ids']
    titulo = request.json['titulo']
    url = request.json['url']
    categoria = request.json['categoria']
    descargas = request.json['descargas']
    descripcion = request.json['descripcion']
    precio = request.json['precio']
    likes = request.json['likes']
    encontrado = False

    for aplication in Aplicaciones:
        if aplication.getIds() == ids:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'La app ya esta registrado'
            })
    else:
            if len(ids)>0:    
                        for aplication in Aplicaciones:
                            if  aplication.getIds() == nombre1:
                                aplication.setIds(request.json['ids'])
                                aplication.setTitulo(request.json['titulo'])
                                aplication.setUrl(request.json['url'])
                                aplication.setCategoria(request.json['categoria'])
                                aplication.setDescargas(request.json['descargas'])
                                aplication.setDescripcion(request.json['descripcion'])
                                aplication.setPrecio(request.json['precio'])
                                aplication.setLikes(request.json['likes'])
                                break
                        return jsonify({
                        'message':'Success',
                        'reason':'Se modifico la app'
                        })
            else:
                return jsonify({
                        'message':'Failed2',
                        'reason':'Problema con los campos, (Todos los campos son obligatorios).'
                    })         

if __name__ == "__main__":
    app.run(threaded=True, port=5001, debug=True)