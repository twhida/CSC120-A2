
from typing import Dict, Union
from computer import Computer
from oo_resale_shop import ResaleShop

def main():
    
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    oo_resale_shop = ResaleShop({}, 0)

    print("." * 39)
    print("TOMOKO'S AWESOME COMPUTER RESALE STORE")
    print("." * 39)

    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = oo_resale_shop.buy(computer)
    print("Done.\n")
   
    print("Checking inventory...")
    oo_resale_shop.print_inventory()
    print("Done.\n")

    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    oo_resale_shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    print("Checking inventory...")
    oo_resale_shop.print_inventory()
    print("Done.\n")
    
    print("Selling Item ID:", computer_id)
    oo_resale_shop.sell(computer_id)
    
    print("Checking inventory...")
    oo_resale_shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
