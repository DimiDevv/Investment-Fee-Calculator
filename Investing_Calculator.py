import sys

print('Type Quit at any point to exit the program!\nType New to start a new calculation.')

def fee_calculation() :
    while True :
        piece_cost = input('How much the investment piece costs. : ')
        if piece_cost.lower() == 'quit' :
            print('Exiting the program...')
            sys.exit()
        elif piece_cost.lower() == 'new' :
            continue
        try :
            piece_cost = float(piece_cost)
        except ValueError :
            print('Invalid Entry! Please enter a numeric value.')
            continue

        while True :
            pieces_to_be_bought = input('How many pieces will you buy? : ')
            if pieces_to_be_bought.lower() == 'quit' :
                print('Exiting the program...')
                sys.exit()
            elif pieces_to_be_bought.lower() == 'new' :
                break
            try :
                pieces_to_be_bought = int(pieces_to_be_bought)
                investment_value = piece_cost * pieces_to_be_bought
                fees = 2 + 0.02 * pieces_to_be_bought
                percentage_fees = round((fees / investment_value) * 100 , 4)
                net_investment = round(piece_cost * pieces_to_be_bought , 2)
                gross_investment = net_investment + fees
                fee_category = ('Excellent' if percentage_fees <= 0.20 else
                                'Good' if percentage_fees <= 0.5 else
                                'High' if percentage_fees <= 1 else
                                'Very High')
                print(f'Your gross investment will be {gross_investment}€. Your net investment will be {net_investment}€. '
                      f'\nYou will pay in fees {fees}€ which is {percentage_fees}% of your Net investment which is '
                      f'considered "{fee_category}"!')
            except ValueError :
                print('Invalid Entry! Please enter an integer value.')
fee_calculation()







