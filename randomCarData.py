#importando a biblioteca random como r devido a convenção própria
import random as r



#Função que gera dados de carros pseudo-aleatórios

class Car:

    def __init__(self):
        #Variáveis de atributos do carro
        self.fuel_type = ['gasolina', 'álcool', 'diesel' , 'GNV' , 'flex', 'bateria']
        self.transmission = ['manual', 'automático', 'CVT']
        self.color = ['preto', 'prata', 'vermelho', 'branco', 'azul', 'cinza']
        self.brand_model = {'Toyota': ['Corolla Cross', 'Corolla Sedan', 'Hilux'],
                       'Nissan': ['Versa', 'Kicks'],
                       'Ford': ['Focus', 'Fiesta', 'Territory'],
                       'BYD': ['Dolphin', 'Seal', 'Song'],
                       'Volkswagen': ['Gol', 'Golf', 'Polo', 'T-Cross', 'Nivus'],
                       'Subaru': ['Forester', 'WRX', 'Crosstrek'],
                       'BMW': ['320i', '530E']}
        self.doors = [2,4]
        self.engine_type = ['1.0', '1.0 turbo', '1.6', '1.8', '2.0']


    def carCreate(self):

        #sorteia marca e modelo
        brand = r.choice(list(self.brand_model.keys()))
        model = r.choice(self.brand_model[brand])

        #garante que motor = N/A e combustível = bateria se a marca for BYD e motor N/A se marca não for BYD mas combustível for bateria
        if brand == 'BYD':
            engine = 'N/A'
            fuel = 'bateria'
        else:
            fuel = r.choice(self.fuel_type)
            if fuel == 'bateria':
                engine = 'N/A'
            else:
                engine = r.choice(self.engine_type)
        
        #Define os atributos do carro
        car = {
            'brand': brand,
            'model': model,
            'year': r.randint(2010,2025),
            'fuel': fuel,
            'color': r.choice(self.color),
            'transmission': r.choice(self.transmission),
            'doors': r.choice(self.doors),
            'engine': engine,
            'electric_glass' : r.choice(['SIM', 'NÃO']),
            'leather_seats' : r.choice(['SIM', 'NÃO']),
            'wheel_drive' : r.choice(['SIM', 'NÃO']),
            'airbag' : r.choice(['SIM', 'NÃO']),
            'multimedia' : r.choice(['SIM', 'NÃO']),
            'air_conditioner' : r.choice(['SIM', 'NÃO']),
            'price': round(r.uniform(10000,500000),2),
            'mileage': r.randint(0,100000)
            }

        
        return car