from faker import Faker
import random as r

#Prompts do cliente
def AgentPrompts(key, item = None):
    prompts = {
    'presentation': [
        f'Opa, tudo bom?\nMeu nome é {item}, vou te atender hoje!', 
        f'Bom dia, tudo bem?\nMeu nome é {item}, vou te atender hoje!', 
        f'Fala, beleza?\nSou {item}, vou te ajudar a encontrar o seu novo carro hoje!'
    ],
    'customer_name': [
        f'Boa! Muito prazer, {item}!',
        f'Muito prazer, {item}!',
        f'Prazer em te conhecer e te atender, {item}'
    ],
    'brand': [
        'Já tem alguma marca em mente?',
        'Já escolheu sua marca preferida?',
        'Tem alguma marca de preferência?',
        'Alguma marca te agrada mais?'
    ],
    'noBrand': ['po,não tenho essa']
}
    
    return r.choice(prompts[key])



#Gera um nome brasileiro aleatório a cada atendimento
fake = Faker('pt_BR')
nome = fake.first_name()

brand_list = ['TOYOTA', 'NISSAN', 'FORD', 'BYD', 'VOLKSWAGEN', 'SUBARU', 'BMW']




print(AgentPrompts('presentation', nome))

customer_name = str(input('Qual seu nome?\n')).title()
print(AgentPrompts('customer_name', customer_name),'\n')

brand = str(input(f'{AgentPrompts('brand')}\nSe ainda não, é só apertar ENTER\n')).upper()
if brand and brand not in brand_list:
    brand = str(input(f'{AgentPrompts('noBrand')}\nTenho carros das seguintes marcas\n{', '.join(brand_list)}')).upper()
    if brand and brand not in brand_list:
        brand = None
        print('A marca que você informou eu não possuo, mas vou te dar algumas opções ótimas de outras marcas ok?\n')

print