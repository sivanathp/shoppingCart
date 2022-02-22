
class shoppingCart(object):
    def __init__(self):
        self.lineItems = dict()
        self.products = dict()
        self.salesTax = 0.0

    def getTotalProductsInCart(self):
        return len(self.lineItems)

    
    def createProduct(self,name, price):
        try:
            productPrice = float(price)
        except ValueError:
            print("price is not a valid number")

        if name not in self.products:
            self.products[name] = price

    
    def addProductToCart(self,name, quantity):
        
        try:
            qty = int(quantity)
        except ValueError:
            print("quantity is not a valid integer")

        if name not in self.lineItems.keys():
            self.lineItems[name]= quantity
        else:
            self.lineItems[name] = self.lineItems[name] + quantity
    
    

    def getTotal(self):
        total = 0
        for name,qty in self.lineItems.items():
            total = total + (qty * self.products[name])
        return total
    
    def roundUp(self,num):
        numberStr = str(num)
        try:
            findPosition = numberStr.find('.')
            thirdDecimal = numberStr[findPosition + 3]
            if int(thirdDecimal) == 5:
                num = num+0.001
            return round(num,2)
        except:
            return round(num,2)

    def setSalesTax(self,taxPercent):
        try:
            self.salesTax = float(taxPercent)
        except ValueError:
            print("input Tax is not a valid number")

    def getSalesTaxAmount(self):
        totalTaxAmount = 0
        totalItemsPrice = self.getTotal()
        totalTaxAmount = totalItemsPrice * self.salesTax * 1.0 / 100
        return self.roundUp(totalTaxAmount)
    
    def getCartTotalAmountWithTax(self):
        totalItemsPrice = self.getTotal() 
        totalTaxAmount = self.getSalesTaxAmount()
        return self.roundUp(totalItemsPrice + totalTaxAmount)
    
    

def testCreateEmptyCart():
    cart = shoppingCart()
    qty = cart.getTotalProductsInCart()
    if qty == 0:
        print('Test Success: Created Empty shopping Cart')
    else:
        print('Error: Not an Empty shopping Cart')
    return cart

def testCreateEmptyCartWithOneProduct():
    cart = testCreateEmptyCart()
    productName = 'Dove Soap'
    price = 39.99
    cart.createProduct(productName,price)
    if  ((productName in cart.products.keys()) and (price == cart.products[productName])) :
        print('Test Success: Created Product '+ productName )
    else:
        print('Error: Product Not created ')
    return cart

def testDecimalsUptoTwo(price):
    if (len(str(price).split(".")) > 1) and len(str(price).split(".")[1]) > 2:
        print('Error: Cart total is more than two decimals' )
    else:
        print('Test Success: Cart total is not more than two decimals')

def testAddSingleProductToCart():
    cart = testCreateEmptyCartWithOneProduct()
    productName = 'Dove Soap'
    qty = 1
    cart.addProductToCart(productName,qty)
    
    if  ((productName in cart.lineItems.keys()) and (qty == cart.lineItems[productName])) :
        print('Test Success: Added {} quantity of Product {} to cart'.format(qty,productName))
    else:
        print('Error: Product Not added to cart ')
    
    total = cart.getTotal()
    if total == cart.products[productName]:
        print('Test Success:  Cart total is equal to product price {}'.format(39.99))
    else:
        print('Error: Cart total is not correct. Expected {}'.format(39.99))
    
    testDecimalsUptoTwo(total)
    return cart

def testAddManyProductsToCart():
    cart = testCreateEmptyCartWithOneProduct()
    productName = 'Dove Soap'
    qty = 5
    
    cart.addProductToCart(productName,qty)
    if  ((productName in cart.lineItems.keys()) and (qty == cart.lineItems[productName])) :
        print('Test Success: Total {} quantity of Product {} in cart'.format(qty,productName))
    else:
        print('Error: Product Not added to cart ')
    
    qty = 3
    cart.addProductToCart(productName,qty)
    
    if  cart.lineItems[productName] == 8 :
        print('Test Success: Total {} quantity of Product {} in cart'.format(8,productName))
    else:
        print('Error: Product Not added to cart ')

    total = cart.getTotal()
    if total == 319.92:
        print('Test Success:  Cart total is equal to product price {}'.format(319.92))
    else:
        print('Error: Cart total is not correct. Expected {}. Actual value {}'.format(319.92,total))
    
    testDecimalsUptoTwo(total)
    return cart

def testCalculateTaxWithManyProducts():
    cart = testCreateEmptyCartWithOneProduct()
    firstProductName = 'Dove Soap'
    secondProductName = 'Axe Deo'
    price= 99.99

    cart.createProduct(secondProductName,price)
    cart.setSalesTax(12.5)
    cart.addProductToCart(firstProductName, 2)
    cart.addProductToCart(secondProductName, 2)
    for name,val in cart.lineItems.items():
        print('Test Success: Added {} quantity of Product {} in cart'.format(val,name))

    totalSalesTaxAmount = cart.getSalesTaxAmount()
    if totalSalesTaxAmount != 35.00 :
        print('Error: Sales tax is not equal to expected value {}. Actual value {}'.format(35.00,totalSalesTaxAmount) )
    else:
        print('Test Success: Sales tax is equal to expected value 35.00')
    
    totalCartPriceWithTax = cart.getCartTotalAmountWithTax()
    
    if totalCartPriceWithTax != 314.96 :
        print('Error: Total cart price is not equal to expected value {}. Actual value {}'.format(314.96,totalCartPriceWithTax) )
    else:
        print('Test Success: Total cart price is equal to expected value 314.96')
    
    testDecimalsUptoTwo(totalCartPriceWithTax)
    return cart
    
if __name__ == '__main__':
    print('AC0 Test')
    cart = testAddSingleProductToCart()
    print('AC1 Test')
    cart = testAddManyProductsToCart()
    print('AC2 Test')
    cart = testCalculateTaxWithManyProducts()
    