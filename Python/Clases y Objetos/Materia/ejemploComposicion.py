class Categorias:
    idCategoria = 15
    nombre = ''

class Proveedores:
    idProveedor = 0
    nombre = 'Juan Guarnizo'

class Producto:
    introduccion = 0
    categoriaProducto = Categorias()
    precio = 0
    tamaño =  0
    tipoDeProducto = 0
    CIFProveedor = Proveedores()


p = Producto()
print(p.CIFProveedor.nombre)
print(p.categoriaProducto.idCategoria)