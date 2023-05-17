from django.contrib import admin

from core0.models import Categoria, Compra, Responsavel, Produto, ItensCompra

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Responsavel)

class ItensInline(admin.TabularInline):
    # Alem de TabularInline tem outras como stackinline para deixar a 
    # listagem de cima para baixo, é uma classe referente a exibição no django admin
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)