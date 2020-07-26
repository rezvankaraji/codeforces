players = input()

is_dangerous = 0

for i in range(len(players)):
    i_th_seven = players[i : i + 7]
    if i_th_seven == "0000000" or i_th_seven == "1111111":
        is_dangerous = 1
        break

if is_dangerous == 0:
    print("NO")
else:
    print("YES")