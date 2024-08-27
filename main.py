# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(f'This is car lock/open simulator by {name}')

# state =
def lock():
    print('Lock all the car door!')

def open(count):
    if count==1:
        print('Unlock one car door!')
    else:
        print('Unlock ALL car doors!')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Neil')
    # Infinite loop until user inputs 'i' to stop
    print('Instruction ==> j: Lock all doors; k: Unlock one door; kk: Unlock all doors; f: Stop the program')

    while True:
        user_input = input("\nPlease enter 'j|k|f': ")

        # 打印用户输入的内容
        print("Your input is：", user_input)
        user_intput_lower = user_input.lower()
        if (user_intput_lower == "j"):
            lock()
        elif (user_intput_lower == "k"):
            open(1)
        elif (user_intput_lower == "kk"):
            open(2)
        elif (user_intput_lower == "f"):
            print("Stop this program!")
            break
        else:
            print("The input is invalid!")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
