import pandas as pd 
from randomCarData import Car
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#função para criar o dataframe com 100 carros e popular um banco

'''Decidi utilizar o SQlite, pois por ser nativo do Python não é necessário a instalação de nenhuma dependencia externa,
desta forma a aplicação pode ser testada em qualquer ambiente com apenas o Python com requirements.txt instalados'''

'''Os dados pseudo-aleatórios serão recriados em toda execução do servidor para assegurar variedade nos testes'''
def carFrameCreation():

    car = Car()
    car_list = []

    #Criando uma lista com 100 carros pseudo-aleatórios
    for _ in range(100):
        car_list.append(car.carCreate())
    
    #criando um dataframe com os dados da lista de carros
    df_cars = pd.DataFrame(car_list)

    #criando a engine SQLite e populando dados
    engine = create_engine('sqlite:///carBase.db', echo=True)
    df_cars.to_sql('tb.cars', con=engine, if_exists='replace', index=True)
