yearly_basketball_tax = int(input())

basketball_sneakers = yearly_basketball_tax * 60 / 100
basketball_suit = basketball_sneakers * 80 / 100
ball = basketball_suit * 25 / 100
accessories = ball * 20 / 100

final_price = yearly_basketball_tax + basketball_sneakers + basketball_suit + ball + accessories
print(final_price)