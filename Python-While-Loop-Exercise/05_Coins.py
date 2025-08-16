change_to_be_returned = float(input())
change_to_be_returned_in_stotinkis = change_to_be_returned * 100
coins = 0
while change_to_be_returned_in_stotinkis > 0:

    if change_to_be_returned_in_stotinkis - 200 >= 0:
        change_to_be_returned_in_stotinkis -= 200
        coins += 1
    elif change_to_be_returned_in_stotinkis - 100 >= 0:
        change_to_be_returned_in_stotinkis -= 100
        coins += 1
    elif change_to_be_returned_in_stotinkis - 50 >= 0:
        change_to_be_returned_in_stotinkis -= 50
        coins += 1
    elif change_to_be_returned_in_stotinkis - 20 >= 0:
        change_to_be_returned_in_stotinkis -= 20
        coins += 1
    elif change_to_be_returned_in_stotinkis - 10 >= 0:
        change_to_be_returned_in_stotinkis -= 10
        coins += 1
    elif change_to_be_returned_in_stotinkis - 5 >= 0:
        change_to_be_returned_in_stotinkis -= 5
        coins += 1
    elif change_to_be_returned_in_stotinkis - 2 >= 0:
        change_to_be_returned_in_stotinkis -= 2
        coins += 1
    elif change_to_be_returned_in_stotinkis - 1 >= 0:
        change_to_be_returned_in_stotinkis -= 1
        coins += 1
print(coins)

# this bottom code got 100 points only because the top one took too long, but it technically works fine
'''
change_str = input()
change_float = float(change_str)
change = int(change_float * 100)
coin_counter = 0
coin_counter += change // 200
change %= 200
coin_counter += change // 100
change %= 100
coin_counter += change // 50
change %= 50
coin_counter += change // 20
change %= 20
coin_counter += change // 10
change %= 10
coin_counter += change // 5
change %= 5
coin_counter += change // 2
change %= 2
coin_counter += change // 1
change %= 1
print(coin_counter)
'''