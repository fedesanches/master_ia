"""

"""
"""
    Aplicamos el 21 de iva y 30 de importado
"""
class ImportedCarStrategy:
    def apply_tax(self, item):
        tax= item['price'] * 0.30  # 30% tax on cellphones
        tax+= item['price'] * 0.20  # 20% tax on cellphones
        return tax