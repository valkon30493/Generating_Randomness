print("""Please provide AI some data to learn...
The current data length is 0, 100 symbols left
Print a random string containing 0 or 1:
""")

new_data_length = 0
total_string = []

while True:
    random_string = str(input())
    random_list = [n for n in random_string]
    for i in random_list:
        if i == "0" or i == "1":
            new_data_length += 1
            total_string.append(i)
        else:
            continue
    if len(total_string) < 100:
        print(f"Current data length is {new_data_length}, {100 - new_data_length} symbols left")
        print("Print a random string containing 0 or 1:\n")
    else:
        print(f"\nFinal data string:\n{''.join(total_string)}")
        break

triads = [bin(triad).replace("0b", "").zfill(3) for triad in range(8)]

joined_string = []
i = 0
while i + 3 < len(total_string):
    joined_string.append([total_string[i], total_string[i + 1], total_string[i + 2], total_string[i + 3]])
    i += 1

combinations = {}

while True:
    for i in range(8):
        counts_of_0 = 0
        counts_of_1 = 0
        for j in joined_string:
            if ''.join(j) == triads[i] + "0":
                counts_of_0 += 1
            elif ''.join(j) == triads[i] + "1":
                counts_of_1 += 1
            else:
                continue
        try:
            if counts_of_0 > counts_of_1:
                prediction = "0"
            else:
                prediction = "1"
        finally:
            combinations[triads[i]] = {"Counts of 0": counts_of_0, "Counts of 1": counts_of_1, "Prediction": prediction}

    break

print()
print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
""")

balance = 1000
while True:
    new_data_length = 0
    total_new_string = []
    print()
    print("Print a random string containing 0 or 1:")
    print()
    random_new_string = str(input())
    if random_new_string == "enough":
        print("Game over!")
        break
    else:
        random_new_list = [n for n in random_new_string]
        for i in random_new_list:
            if i == "0" or i == "1":
                new_data_length += 1
                total_new_string.append(i)
            else:
                continue
        if len(total_new_string) < 4:
            continue
        else:
            list_for_prediction = [n for n in total_new_string]
            i = 0
            predicted_string = ""
            while i + 3 < len(total_new_string):
                for j in range(8):
                    if list_for_prediction[i] + list_for_prediction[i+1] + list_for_prediction[i+2] == triads[j]:
                        predicted_string += combinations[triads[j]]["Prediction"]
                    else:
                        continue
                i += 1
            print(f"predictions:\n{predicted_string}")

            list_of_predictions = [n for n in predicted_string]
            correct = 0
            total = len(list_of_predictions)

            for i in range(len(list_of_predictions)):
                if list_of_predictions[i] == list_for_prediction[3 + i]:
                    correct += 1
                else:
                    continue
            balance = balance + total - (2 * correct)
            print()
            print(f"Computer guessed {correct} out of {total} symbols right ({round(correct / total * 100, 2)} %) ")
            print(f"Your balance is now ${balance}")








