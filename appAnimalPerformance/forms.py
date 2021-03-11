from django.forms import ModelForm
from .models import Rendimiento,LoteAnimal,Animal,Producto,Usuario
from django import forms

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['idAnimal','nombre_animal','peso_animal']        

class LoteAnimalForm(ModelForm):
    class Meta:
        model = LoteAnimal
        fields = ['idLoteAnimal','peso_lote','precio_costo','nombre_proveedor']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nombre_producto','precio_venta','unidad']

class ProductoForm2(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','peso_producto','precio_costo','nombre_producto','precio_venta','unidad','utilidad_producto']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['idUsuario','cedula','nombres','apellidos','correo','password']

class RendimientoForm(ModelForm):
    class Meta:
        model = Rendimiento
        fields = ['idRendimiento','total_costo','total_venta','margen_utilidad',
                    'rendimiento_neto','merma_deshidratacion','porcentaje_peso_neto',
                    'porcentaje_peso_producto','total_costo_producto','total_venta_producto','margen_utilidad_producto']
