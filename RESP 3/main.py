import pandas as pd, pylab as plt, numpy as np

def read_to_csv(path):
    return pd.read_csv(path)

def filter_ON(df,on = 1):
    it_on = df['onoff'] == on
    new_df = df[it_on]
    return new_df

def filter_ID(df,id):
    id = df['id'] == id
    new_df = df[id]
    return new_df

def get_data_velo(df):
    data_Array = list(df['velo'].head(300))
    return data_Array

def get_data_acel(df):
    data_Array = list(df['velo'].head(300))
    new_Array = [int((i-0)/60) for i in data_Array] #(velocidad final - velocidad incicial )/ tiempo (60 min) = aceleracion
    return new_Array


def grafica(dict, name):
    plt.figure(figsize=(14, 20))
    color = ['red','blue','green','yellow','cyan','black','brown','orange','gray','m']
    for i in range(1,len(dict)+1):
        
        plt.subplot(10,1,i)
        plt.tight_layout()
        plt.title('vehicles - '+ str(i))
        plt.xlabel('Trama de velocidades (x)')
        plt.ylabel(name +'h (y)')
        plt.plot(np.array(range(0, len(dict[i]), 1)), dict[i], '-', color=color[i-1])
        plt.grid()
        
    plt.savefig(f'img/{name}.png')
    plt.show()
    
def Velocidad(df):
    new_dict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}

    for i in range(1,11):
        temp = filter_ID(df,i)
        new_dict[i] = get_data_velo(temp)
    grafica(new_dict,'Velocidades')


def Aceleracion(df):
    new_dict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}

    for i in range(1,11):
        temp = filter_ID(df,i)
        new_dict[i] = get_data_acel(temp)
    grafica(new_dict,'Aceleraciones')


def main ():
    df = read_to_csv("data/rutas.csv")
    df = filter_ON(df)
    Velocidad(df)
    Aceleracion(df)


if __name__ == '__main__':
    main()