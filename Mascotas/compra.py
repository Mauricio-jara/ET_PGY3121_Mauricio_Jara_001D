class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, producto):
        if producto.dv not in self.carrito.keys():
            self.carrito[producto.dv]={
                "producto_id":producto.dv, 
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "cantidad": 1,
                "precio": str (producto.precio),
                "total": producto.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==producto.dv:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = producto.precio
                    value["total"]= value["total"] + producto.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, producto):
        id = producto.dv
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,producto):
        for key, value in self.carrito.items():
            if key == producto.dv   :
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- producto.precio
                if value["cantidad"] < 1:   
                    self.eliminar(producto)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
