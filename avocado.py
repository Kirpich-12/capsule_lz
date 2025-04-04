import pandas as pd
import matplotlib.pyplot as plt 



class Avocado:
    def __init__(self,link:str):
        self.link = link
    
    def paint(self):
        df = pd.read_csv(self.link)
        data_pice = dict(zip(list(df['Date']), list(df['AveragePrice']) ))
        sr_data_prise = dict(sorted(data_pice.items()))
        xlist = list(sr_data_prise.keys())#список сорт. дат
        ylist = list(sr_data_prise.values())#список сорт. цен
        fig, ax = plt.subplots()
        ax.plot(xlist, ylist, color = 'r')
        ax.grid()
        plt.show()

    
    def __del__(self):
        print('Plot has been deleted')

if __name__ == '__main__':
    avc = Avocado('avocado.csv')
    avc.paint()




