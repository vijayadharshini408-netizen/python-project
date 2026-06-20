scores = [78, 92, 65, 88, 45, 100, 55]

total = 0
for score in scores:
    total += score

print(f"Total is: {total}")

highest_score = scores[0]
for score in scores:
    if score > highest_score:
        highest_score = score

print(f"Highest Score: {highest_score}")

lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score

print(f"Lowest Score: {lowest_score}")
pass_count = 0

for score in scores:
    if score >= 50:
        pass_count += 1

print(f"Pass Count: {pass_count}")
for number in range(1,10):
 print(number)
for even in range(0,20,2):
 print(even)
print(sum(range( 1,50 )))