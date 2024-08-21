from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def agregarUsuario(db,user):

    table = db.Table('hospital')

    user.nombre = user.nombre.capitalize()
    user.nombre2 = user.nombre2.capitalize()
    user.apellido1 = user.apellido1.capitalize()
    user.apellido2 = user.apellido2.capitalize()

    user.tiempo = str(user.tiempo)

    user = dict(user)

    table.put_item(Item=user)
    return "Item creado"
    

def obtenerUsuarios(db, numero):
    table = db.Table('hospital')

    response = table.scan()

    usuarios = response['Items']

    usuarios_ordenados = sorted(usuarios, key=lambda x: x['tiempo'], reverse=True)

    ultimos = usuarios_ordenados[:numero]

    return ultimos

def obtenerUsuarioID(db, id):

    table = db.Table('hospital')

    response = table.get_item(Key={ 'documento': id  })
    print(response)
    return response["Item"]

def actualizarUsuario(db, user):

    table = db.Table('hospital')

    user.nombre = user.nombre.capitalize()
    user.nombre2 = user.nombre2.capitalize()
    user.apellido1 = user.apellido1.capitalize()
    user.apellido2 = user.apellido2.capitalize()

    user.tiempo = str(user.tiempo)

    user = dict(user)

    table.put_item(Item=user)

    return "Item actualizado"


def eliminarUsuario(db, documento):
    table = db.Table('hospital')
    try:
        # Intentar eliminar el ítem
        response = table.delete_item(
            Key={'documento': documento},
            ReturnValues='ALL_OLD'  # Devuelve el ítem eliminado, si existe
        )
        # Verificar si se ha eliminado algún ítem
        if 'Attributes' in response:
            return response['Attributes']  # Devuelve el ítem eliminado
        else:
            return None  # El ítem no existía y no se eliminó
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        raise
