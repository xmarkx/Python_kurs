import seaborn
import pandas

stock_name = 'Dow Jones'

def print_stock_name():
    print(f'The name of the stock is: {stock_name}')
    
def print__name__():
    print(f'The scripts __name__ is: {__name__}')

class Data:
    
    def __init__(self):
        self.df = seaborn.load_dataset('dowjones')

    def basic_eda(self):
        print('\n-==### HEAD ###==-\n')
        print(self.df.head())
        print('\n-==### INFO ###==-\n')
        self.df.info()
        
    def data_transform(self):
        self.df['year'] = self.df['Date'].dt.year
        self.df['month'] = self.df['Date'].dt.month
        self.df['day'] = self.df['Date'].dt.day

    def calculate_yearly_avg(self):
        self.yearly_avg = self.df.groupby(self.df['year'])['Price'].mean()

    def show_yearly_avg(self):
        print(self.yearly_avg)
        

if __name__ == '__main__':
    print('I am the sript that is run and that is why i am called main')
    
print__name__()

        
