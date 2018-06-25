class Expenditure:
    def __init__(self,Expenditure,Saving):
        self.Expenditure=Expenditure
        self.Saving=Saving

    def Total_salary(self):
        self.total=self.Expenditure+self.Saving

    def display_salary(self):
        self.Total_salary()
        print("Total Salary : ",self.total)

exp=Expenditure(1200,800)
exp.display_salary()
