#income = rent, laundry, storage, misc
#expenses = tax, insurance, utilities, hoa, weather, vacancy, repairs, property manager,mortage,capEx,
#cash_flow = income, expenses
#roi = down payment, closing costs, rehab budget, other 


class ROI_cal():
    def __init__(self, income = 0, expenses = 0, cash_flow = 0, roi = 0):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.roi = roi
        
        self.calculate_income()
        self.calculate_expenses()
        self.calculate_cash_flow()
        self.calculate_roi()
        
    def calculate_income(self):
        rent_income = int(input("What is your rent income?: "))
        laundry_income = int(input("What is your laundry income?: "))
        storage_income = int(input("What is your storage income?: "))
        misc_income = int(input("What is your miscellaneous income? These can include pet fees or special services: "))
        
        self.income = laundry_income + rent_income + storage_income + misc_income
        print("Your income is: " + str(self.income) + ".\n")
            
    def calculate_expenses(self):
        tax = int(input("What are your tax expenses?: ")) 
        insurance = int(input("What are your insurance expenses?: ")) 
        utilities = int(input("What are your utilities expenses? These can include electric, water, sewer, garbage, and gas charges.: "))
        hoa_fees = int(input("What are your HOA expenses? : "))
        weather = int(input("What are your weather expenses? This can include lawn/snow expenses.: "))   
        vacancy = int(input("What are your vacancy expenses?: ")) 
        repairs = int(input("What are your repair expenses?: ")) 
        capEx = int(input("What are your capital expenditures?: ")) 
        property_management = int(input("What are your property management expenses?: ")) 
        mortgage = int(input("What are your mortgage expenses?: "))

        self.expenses = tax + insurance + utilities + hoa_fees + weather + vacancy + repairs + capEx + property_management + mortgage
        print("Your expenses are " + str(self.expenses) + ".\n")
        
    def calculate_cash_flow(self):
        self.cash_flow = (self.income - self.expenses) * 12
        print("Your monthly cash flow is: " + str(self.cash_flow / 12) + ".")
        print("Your yearly cash flow is: " + str(self.cash_flow) + ".\n")
       
    def calculate_roi(self):
        down_payment = int(input("How much money did you put into down payment?: "))
        closing_costs = int(input("What are the closing costs?: ")) 
        rehab_budget = int(input("What is your rehab budget?: ")) 
        misc_costs = int(input("Any other miscellanous costs you can think of?: "))
        investment = down_payment + closing_costs + rehab_budget + misc_costs
        print("Your total investment is: " + str(investment) + ".")
        #ROI = annual cash flow / investment. 
        self.roi = self.cash_flow / investment * 100
        print("Your cash-on-cash percent ROI is: %" + str(self.roi) + ".\n")



property1 = ROI_cal() 