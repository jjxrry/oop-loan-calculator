class Loan:
    #create Loan object
    def __init__(self, intRate: float, numYears: int, loanAmt: float, nameBorrow: str):
        self.__intRate =  intRate                               #Private data fields
        self.__numYears =  numYears
        self.__loanAmt = loanAmt
        self.__nameBorrow = nameBorrow

    #getters
    def getIntRate(self) -> float:
        return self.__intRate

    def getNumYears(self) -> int:
        return self.__numYears

    def getLoanAmt(self) -> float:
        return self.__loanAmt

    def getNameBorrow(self) -> str:
        return self.__nameBorrow

    #setters
    def setIntRate(self, intRate: float) -> float:
        self.__intRate =  intRate


    def setNumYears(self, numYears: int) -> int:
        self.__numYears =  numYears


    def setLoanAmt(self, loanAmt: float) -> float:
        self.__loanAmt = loanAmt


    def setNameBorrow(self, nameBorrow: str) -> str:
        self.__nameBorrow = nameBorrow


    #class methods
    def  getMonthlyPayment(self) -> float:
        """Method calculates the monthly payment of the loan"""
        monthlyInterestRate = self.__intRate / 1200
        monthlyPayment = self.__loanAmt * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (self.__numYears * 12)))
        
        return monthlyPayment


    def getTotalPayment(self) -> float: 
        """Method calculates the total amount of payment"""
        totalPayment = self.getMonthlyPayment() * self.__numYears * 12

        return totalPayment


def main():
    #user input for annual int rate, number of years on loan, loan amount and the borrower's name
    intRate = float(input("Enter Yearly Interest Rate: "))
    numYears =  int(input("Enter number of years as an integer: "))
    loanAmt = float(input("Enter loan amount: "))
    nameBorrow = str(input("Enter a borrower's name: "))

    
    #Calculates the loan in the borrower's name, gives the monthly and total payment
    loan1 = Loan(intRate, numYears, loanAmt, nameBorrow)
    print("The loan is for", loan1.getNameBorrow())
    print("The monthly payment is", format(loan1.getMonthlyPayment(), ".2f"))
    print("The total payment is", format(loan1.getTotalPayment(), ".2f"))

    #space formatting
    print()
    
    #Allows for the user to change the input information
    changeInput = input("Do you want to change the loan amount? Y for yes or enter to quit ")
    while changeInput == 'y':

        loanAmt = float(input("Enter new loan amount "))
        loan1.setLoanAmt(loanAmt)   #access private data member by mutator method
                                                             #changes the original loanAmt to the new input
        
        print("The loan is for", loan1.getNameBorrow())
        print("The monthly payment is", format(loan1.getMonthlyPayment(), ".2f"))
        print("The total payment is", format(loan1.getTotalPayment(), ".2f"))
        
        print()
        changeInput = input("Do you want to change the loan amount? Y for yes or enter to quit ")
    
if __name__ == "__main__":
    main() 
