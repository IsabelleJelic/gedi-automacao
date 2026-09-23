
def lista_posicoes_carimbo():
    lista_carimbo = {
        '_': [
            {
                'modo': '', 
                'tamanho': 0, 
                'pedido': (70, 475), 
                'cnpj': (70, 485), 
                'sge': (70, 495)
            }
        ],
        'COELBA': [
            {
                'modo': '>', 
                'tamanho': 65, 
                'pedido': (55, 55), 
                'cnpj': (55, 65), 
                'sge': (55, 75)
            },
            {
                'modo': '<=', 
                'tamanho': 65, 
                'pedido': (450, 20), 
                'cnpj': (450, 30), 
                'sge': (450, 40)
            }
        ],
        'CELPE': [
            {
                'modo': '>', 
                'tamanho': 65, 
                'pedido': (70, 55), 
                'cnpj': (70, 65), 
                'sge': (70, 75)
            },
            {
                'modo': '<=', 
                'tamanho': 65, 
                'pedido': (385, 190), 
                'cnpj': (385, 200), 
                'sge': (385, 210)
            }
        ],
        'COSERN': [
            {
                'modo': '>', 
                'tamanho': 65, 
                'pedido': (55, 55),
                'cnpj': (55, 65),
                'sge': (55, 75)
            },
            {
                'modo': '<=',
                'tamanho': 65,
                'pedido': (385, 190),
                'cnpj': (385, 200),
                'sge': (385, 210)
            }
        ],
        'ENEL_CE': [
            {
                'modo': '>=',
                'tamanho': 500,
                'pedido': (460, 15),
                'cnpj': (460, 25),
                'sge': (460, 35)
            },
            {
                'modo': '<',
                'tamanho': 500,
                'pedido': (460, 35),
                'cnpj': (460, 45),
                'sge': (460, 55)
            }
        ],
        'CPFL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (500, 15),
                'cnpj': (500, 25),
                'sge': (500, 35)
            }
        ],
        'RGE': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (480, 10),
                'cnpj': (480, 20),
                'sge': (480, 30)
            }
        ],
        'ENERGISA': [
            {
                'modo': '<=',
                'tamanho': 99,
                'pedido': (220, 295),
                'cnpj': (220, 305),
                'sge': (220, 315)
            },
            {
                'modo': '>=',
                'tamanho': 100,
                'pedido': (410, 310),
                'cnpj': (410, 320),
                'sge': (410, 330)
            }
        ],
        'ENERGISA_SUL_SUDESTE_(ENERGISA__CNEE)': [
            {
                'modo': '<=',
                'tamanho': 250,
                'pedido': (330, 10),
                'cnpj': (330, 20),
                'sge': (330, 30)  
            }
        ],
        'ENERGISA_SUL_SUDESTE_(BRAGANTINA)': [
             {
                'modo': '>=',
                'tamanho': 310,
                'pedido': (310, 30),
                'cnpj': (310, 40),
                'sge': (310, 50)
            }
        ],
        'ENERGISA_MT': [
            {
                'modo': '<=',
                'tamanho': 16,
                'pedido': (430, 295),
                'cnpj': (430, 305),
                'sge': (430, 315)
            },
            {
                'modo': '>',
                'tamanho': 140,
                'pedido': (460, 40),
                'cnpj': (460, 50),
                'sge': (460, 60)
            }
        ],
        'ENERGISA_MS': [
            {
                'modo': '<=',
                'tamanho': 305,
                'pedido': (185, 305),
                'cnpj': (185, 315),
                'sge': (185, 325)
            },
            {
                'modo': '>=',
                'tamanho': 306,
                'pedido': (270, 100),
                'cnpj': (270, 110),
                'sge': (270, 120)
            }
        ],
        'ENERGISA_RO': [
            {
                'modo': '<=',
                'tamanho': 306,
               'pedido': (190, 295),
                'cnpj': (190, 305),
                'sge': (190, 315)
            },
            {
                'modo': '>=',
                'tamanho': 307,
                'pedido': (430, 305),
                'cnpj': (430, 315),
                'sge': (430, 325)
            }
        ],
        'ENERGISA_TO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (160, 325),
                'cnpj': (160, 335),
                'sge': (160, 345)
            },
            {
                'modo': '<=',
                'tamanho': 305,
                'pedido': (280, 310),
                'cnpj': (280, 320),
                'sge': (280, 330)
            },
            {
                'modo': '>=',
                'tamanho': 540,
                'pedido': (265, 100),
                'cnpj': (265, 110),
                'sge': (265, 120)
            }
        ],
        'ENERGISA_ACRE': [
            {
                'modo': '<=',
                'tamanho': 305,
                'pedido': (185, 305),
                'cnpj': (185, 315),
                'sge': (185, 325)
            },
            {
                'modo': '>=',
                'tamanho': 306,
                'pedido': (270, 100),
                'cnpj': (270, 110),
                'sge': (270, 120)
            }
        ],
        'ENERGISA_SE': [
            {
                'modo': '>',
                'tamanho': 150,
                'pedido': (460, 10),
                'cnpj': (460, 20),
                'sge': (460, 30)
            }
        ],
        'ENERGISA_MR': [
            {
                'modo': '>',
                'tamanho': 306,
                'pedido': (460, 10),
                'cnpj': (460, 20),
                'sge': (460, 30)
            }
        ],
        'ENERGISA_PB': [
            {
                'modo': '>',
                'tamanho': 306,
              'pedido': (450, 50),
                'cnpj': (450, 60),
                'sge': (450, 70)
            }
        ],
        'COPEL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (200, 250),
                'cnpj': (200, 260),
                'sge': (200, 270)
            }
        ],
        'ELEKTRO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (310, 490),
                'cnpj': (310, 500),
                'sge': (310, 510)
            }
        ],
        'ELEKTRO_SP': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (310, 425),
                'cnpj': (310, 435),
                'sge': (310, 445)
            }
        ],
        'ELEKTRO_MS': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (310, 570),
                'cnpj': (310, 580),
                'sge': (310, 590)
            }
        ],
        'CEROC': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (160, 280),
                'cnpj': (160, 290),
                'sge': (160, 300)
            }
        ],
        'CERMISSOES': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (400, 295),
                'cnpj': (400, 305),
                'sge': (400, 315)
            }
        ],
        'FORCEL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 255),
                'cnpj': (460, 265),
                'sge': (460, 275)
            }
        ],
        'CERTEL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 285),
                'cnpj': (460, 295),
                'sge': (460, 305)
            }
        ],
        'CHESP': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (370, 275),
                'cnpj': (370, 285),
                'sge': (370, 295)
            }
        ],
        'CERFOX': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (10, 490),
                'cnpj': (10, 500),
                'sge': (10, 510)
            }
        ],
        'CERGRAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (370, 275),
                'cnpj': (370, 285),
                'sge': (370, 295)
            }
        ],
        'CERBRANORTE': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (490, 50),
                'cnpj': (490, 60),
                'sge': (490, 70)
            }
        ],
        'CERPALO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (450, 50),
                'cnpj': (450, 60),
                'sge': (450, 70)
            }
        ],
        'CERAL_(ARARUAMA)': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (340, 275),
                'cnpj': (340, 285),
                'sge': (340, 295)
            }
        ],
        'COOPERJAMA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (450, 50),
                'cnpj': (450, 60),
                'sge': (450, 70)
            }
        ],
        'COOPERALIANCA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 285),
                'cnpj': (460, 295),
                'sge': (460, 305)
            }
        ],
        'CERGAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 265),
                'cnpj': (460, 275),
                'sge': (460, 285)
            }
        ],
        'COOPERCOCAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (340, 275),
                'cnpj': (340, 285),
                'sge': (340, 295)
            }
        ],
        'CERSUL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (325, 280),
                'cnpj': (325, 290),
                'sge': (325, 300)
            }
        ],
        'UHENPAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (325, 260),
                'cnpj': (325, 270),
                'sge': (325, 280)
            }
        ],
        'EFLJC': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (325, 325),
                'cnpj': (325, 335),
                'sge': (325, 345)
            }
        ],
        'CERGRAND': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (70, 450),
                'cnpj': (70, 460),
                'sge': (70, 470)
            }
        ],
        'CERCI': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (340, 285),
                'cnpj': (340, 295),
                'sge': (340, 305)
            }
        ],
        'IGUACU': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (340, 285),
                'cnpj': (340, 295),
                'sge': (340, 305)
            }
        ],
        'CERIPA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (340, 475),
                'cnpj': (340, 485),
                'sge': (340, 495)
            }
        ],
        'EFLUL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (340, 325),
                'cnpj': (340, 335),
                'sge': (340, 345)
            }
        ],
        'CERNHE': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (380, 35),
                'cnpj': (380, 45),
                'sge': (380, 55)
            }
        ],
        'DMED': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 270),
                'cnpj': (460, 280),
                'sge': (460, 290)
            }
        ],
        'CERILUZ': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 255),
                'cnpj': (460, 265),
                'sge': (460, 275)
            }
        ],
        'ELFSM': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (160, 225),
                'cnpj': (160, 235),
                'sge': (160, 245)
            }
        ],
        'CERME': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (480, 385),
                'cnpj': (480, 395),
                'sge': (480, 405)
            }
        ],
        'COOPERA_': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (390, 50),
                'cnpj': (390, 60),
                'sge': (390, 70)
            }
        ],
        'CERPRO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 355),
                'cnpj': (460, 365),
                'sge': (460, 375)
            }
        ],
        'CERTAJA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CEDRAP': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (310, 375),
                'cnpj': (310, 385),
                'sge': (310, 395)
            }
        ],
        'CERIM': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (185, 360),
                'cnpj': (185, 370),
                'sge': (185, 380)
            }
        ],
        'COCEL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'DEMEI': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CEPRAG': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERACA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CEREJ': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERGAPA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CRERAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERAL_(Anitopolis)': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERMOFUL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERAL_(Arapoti)': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 355),
                'cnpj': (460, 365),
                'sge': (460, 375)
            }
        ],
        'COORSEL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'COOPERLUZ': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'COOPERZEM': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERCAMPO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 270),
                'cnpj': (460, 280),
                'sge': (460, 290)
            }
        ],
        'COPREL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 155),
                'cnpj': (460, 165),
                'sge': (460, 175)
            }
        ],
        'CERTREL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CASTRO_DIS_(ELETRORURAL)': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 255),
                'cnpj': (460, 265),
                'sge': (460, 275)
            }
        ],
        'CEGERO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CELETRO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (320, 450),
                'cnpj': (320, 460),
                'sge': (320, 470)
            }
        ],
        'CEMIRIM': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (310, 455),
                'cnpj': (310, 465),
                'sge': (310, 475)
            }
        ],
        'CERPA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 275),
                'cnpj': (460, 285),
                'sge': (460, 295)
            }
        ],
        'CERPAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (470, 90),
                'cnpj': (470, 100),
                'sge': (470, 110)
            }
        ],
        'CERRP': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 280),
                'cnpj': (460, 290),
                'sge': (460, 300)
            }
        ],
        'COESO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (360, 290),
                'cnpj': (360, 300),
                'sge': (360, 310)
            }
        ],
        'ELETROPAULO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (360, 28),
                'cnpj': (360, 38),
                'sge': (360, 48)
            }
        ],
        'AMAZONAS': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (180, 10),
                'cnpj': (180, 20),
                'sge': (180, 30)
            },
            {
                'modo': '<',
                'tamanho': 60,
                'pedido': (505, 520),
                'cnpj': (505, 530),
                'sge': (505, 540)
            }
        ],
        'EQUATORIAL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 355),
                'cnpj': (460, 365),
                'sge': (460, 375)
            }
        ],
        'EQUATORIAL_PI': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (400, 15),
                'cnpj': (400, 25),
                'sge': (400, 35)
            }
        ],
        'EQUATORIAL_PA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (440, 9),
                'cnpj': (440, 19),
                'sge': (440, 29)
            }
        ],
        'EQUATORIAL_MAR': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (420, 15),
                'cnpj': (420, 25),
                'sge': (420, 35)
            }
        ],
        'EQUATORIAL_AL': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 10),
                'cnpj': (460, 20),
                'sge': (460, 30)
            }
        ],
        'RORAIMA_ENERGIA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (250, 20),
                'cnpj': (250, 30),
                'sge': (250, 40)
            }
        ],
        'CEA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 10),
                'cnpj': (460, 20),
                'sge': (460, 30)
            }
        ],
        'LIGHT': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (490, 55),
                'cnpj': (490, 65),
                'sge': (490, 75)
            },
            {
                'modo': '<',
                'tamanho': 120,
                'pedido': (160, 430),
                'cnpj': (160, 440),
                'sge': (160, 450)
            }
        ],
        'ELETROCAR': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (160, 275),
                'cnpj': (160, 285),
                'sge': (160, 295)
            }
        ],
        'ENEL_RIO': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (450, 50),
                'cnpj': (450, 40),
                'sge': (450, 30)
            },
            {
                'modo': '>',
                'tamanho': 600,
                'pedido': (100, 235),
                'cnpj': (100, 245),
                'sge': (100, 255)
            }
        ],
        'ESCELSA': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (460, 15),
                'cnpj': (460, 25),
                'sge': (460, 35)
            },
            {
                'modo': '<',
                'tamanho': 40,
                'pedido': (50, 540),
                'cnpj': (50, 550),
                'sge': (50, 560)
            }
        ],
        'BANDEIRANTE': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (490, 15),
                'cnpj': (490, 25),
                'sge': (490, 35)
            }
        ],
        'ENEL_GOIAS': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (100, 635),
                'cnpj': (100, 645),
                'sge': (100, 655)
            }
        ],
        'EQUATORIAL_GOIAS': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (70, 520),
                'cnpj': (70, 530),
                'sge': (70, 540)
            }
        ],
        'CEEE': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (220, 435),
                'cnpj': (220, 445),
                'sge': (220, 455)
            }
        ],
        'CERVALE': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (90, 495),
                'cnpj': (90, 505),
                'sge': (90, 515)
            }
        ],
        'CERIS': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (400, 365),
                'cnpj': (400, 375),
                'sge': (400, 385)
            }
        ],
        'CELESC': [
            {
                'modo': '',
                'tamanho': 60,
               'pedido': (400, 60),
                'cnpj': (400, 70),
                'sge': (400, 80)
            }
            # {
            #     'modo': '>',
            #     'tamanho': 340,
            #     'pedido': (460, 15),
            #     'cnpj': (460, 25),
            #     'sge': (460, 35)
            # }
        ],
        'CEMIG': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (400, 10),
                'cnpj': (400, 20),
                'sge': (400, 30)
            }
        ],
        'CEB': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (450, 15),
                'cnpj': (450, 25),
                'sge': (450, 35)
            }
        ],
        'CEDRI': [
            {
                'modo': '', 
                'tamanho': 0, 
                'pedido': (185, 10),
                'cnpj': (185, 20),
                'sge': (185, 30)
            }
        ],
        'CERVAM': [
            {
                'modo': '', 
                'tamanho': 0, 
                'pedido': (70, 375), 
                'cnpj': (70, 385), 
                'sge': (70, 395)
            }
        ],
        'CETRIL': [
            {
                'modo': '', 
                'tamanho': 0, 
                'pedido': (400, 565), 
                'cnpj': (400, 575), 
                'sge': (400, 585)
            }
        ],
        'CPFL_SANTA_CRUZ': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (500, 15),
                'cnpj': (500, 25),
                'sge': (500, 35)
            }
        ],
        'CPFL_SANTA_CRUZ_(JAGUARI)': [
            {
                'modo': '',
                'tamanho': 0,
                'pedido': (245, 100),
                'cnpj': (245, 110),
                'sge': (245, 120)
            }
        ]
    }

    return lista_carimbo