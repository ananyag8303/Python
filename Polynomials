# OOP code to perform different functions with polynomials

class Polynomials:
    
    def __init__(self, coeff_x = []):
        self.coeff_x = coeff_x
        
    #Method to calculate the order of P(x)
    def order_Px(self):
        order = len(self.coeff_x) - 1
        return order
    #Method to add 2 polynomials together
    def add_Px(self, py):
        px = self.coeff_x
        py = py.coeff_x
        res_add = []
        for i in range(0,self.order_Px()+1):
            res_add.append(px[i]+py[i])
        return res_add
    #Method 2 to add polynomials
    def adder(self,py):
        px_coeff = self.coeff_x.copy()
        py_coeff = py.coeff_x.copy()
        if (len(py_coeff) >= len(px_coeff)):
            biggerOrderPol = py_coeff
            smallerOrderPol = px_coeff
        else:
            biggerOrderPol = px_coeff
            smallerOrderPol = py_coeff
        for i in range(len(smallerOrderPol)):
            biggerOrderPol[i] += smallerOrderPol[i]
        return biggerOrderPol
        
    #Method to differentiate it
    def derivative(self):
        Pd = [0]*len(self.coeff_x)
        for i in range(len(self.coeff_x)):
            Pd[i] = self.coeff_x[i] * i 
        return Polynomials(Pd)
    
    #Method to integrate the function
    def integrate(self):
        c = 2
        length = len(self.coeff_x) 
        Pi = [0]*length
        Pi[0] = c
        for i in range(1, len(self.coeff_x)):
            Pi[i] = self.coeff_x[i] / (i)
        return Polynomials(Pi)
    #Method to organise into string
    def string_rep(self):
        string = ""
        for i in range(len(self.coeff_x)):
            string += str(self.coeff_x [i]) + "x^"+ str(i) + "+"
        print(string.rstrip("+"))
        #print(string[:-1])
    
def main():
    px = Polynomials([2,0,4,-1,0,6])
    py = Polynomials([-1,-3,0,4.5,0,0])
    order = px.order_Px()
    #order_2 = py.order_Px()
    #add = px.add_Px(py)
    add = px.adder(py)
    differentiate = px.derivative().coeff_x
    differentiate = Polynomials(differentiate)
    integrate = differentiate.integrate().coeff_x
    print("Order of px: ", order)
    #print("Order of py: ",order_2)
    print("Addition of py to px: ",add)
    print("Px: ", px.coeff_x)
    print("Differentiation of Px: ", differentiate.coeff_x)
    print("Integrate:", integrate)
    px.string_rep()
main()   
