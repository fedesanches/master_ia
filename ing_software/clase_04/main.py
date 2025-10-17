
import json
from typing import List, Dict
from FoodItemStrategy import FoodItemStrategy
from CellphoneStrategy import CellphoneStrategy
from ComputerStrategy import ComputerStrategy
from ImportedCarStrategy import ImportedCarStrategy
from CarStrategy import CarStrategy
from BlackFridayStrategy import BlackFridayStrategy
from StudentStrategy import StudentStrategy

if __name__ == "__main__":
    with open('input.json', 'r') as file:
        data = json.load(file)

    items = data['items']
    discount_type = data['discount']

    print("Items:", items)
    print("Discount Type:", discount_type)

    tax_strategies = {
        "food_item": FoodItemStrategy(),
        "cellphone": CellphoneStrategy(),
        "computer": ComputerStrategy(),
        "imported_car": ImportedCarStrategy(),
        "car": CarStrategy()
    }
    
    discount_strategies = {
        "black_friday": BlackFridayStrategy(),
        "student": StudentStrategy()
    }   
    
    item_taxes = []
    total_taxes=0
    subtotal=0
    for item in items:
        subtotal+= item['price']
        impuestosStrategy=tax_strategies.get(item['product_category'])
        impuesto=impuestosStrategy.apply_tax(item)
        item_taxes.append({"id": item['id'], "tax": impuesto})
        print(f"Item ID: {item['id']}, Category: {item['product_category']}, Price: {item['price']}, Tax: {impuesto}")

        total_taxes+= impuesto
        
    applied_discount=discount_strategies[discount_type].apply_discount(subtotal + total_taxes)

    final_total= subtotal + total_taxes - applied_discount

    recibo={
        "subtotal": subtotal,
        "applied_discount": applied_discount,
        "items": item_taxes,
        "total_taxes": total_taxes,
        "final_total": final_total
    }
    
    ## guardar recibo en un archivo receipt.json
    with open('receipt.json', 'w') as file:
        json.dump(recibo, file, indent=4)
    
    
