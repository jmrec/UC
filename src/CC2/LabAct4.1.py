def not_a_number(string):
    if not string.isdigit():
        return True
    else:
        return False
    
def starts_with_0_and_has_many_digits(string):
    if string[0] == "0" and len(string) > 1:
        return True
    else:
        return False
    
def only_0(string):
    if string == "0":
        return True
    else:
        return False

def empty_balance(balance):
    if balance == 0:
        return True
    else:
        return False

number_of_equal_signs = 70
def print_home_interface():
    print("Welcome to the app of Infinite Money Bank!")
    print("Please type in the command of your chosen transaction below [1-4]")
    print("="*number_of_equal_signs)
    print("[1] Check Balance")
    print("[2] Withdraw Money")
    print("[3] Deposit Money")
    print("[4] Exit Application")
    print("="*number_of_equal_signs)

# -------------------------------------------------

balance = 100.0
customer_wants_to_transact = True
while customer_wants_to_transact:
    print_home_interface()
    choice = input("[INPUT] What do you want to do? ").strip()

    match choice:
        case "1":
            print(f"[RESPONSE] Your current balance is PHP {balance}.\n")
        case "2":
            customer_can_withdraw = True
            if empty_balance(balance):
                customer_can_withdraw = False
                print("[RESPONSE] Your balance is PHP 0, so you can not make any withdrawals.\n")

            while customer_can_withdraw:
                withdraw_amount = input("[INPUT] How much cash do you want to withdraw? ").strip()
                if not_a_number(withdraw_amount) or starts_with_0_and_has_many_digits(withdraw_amount):
                    print("[ERROR] Your input is invalid. It must be a counting number.\n")
                    continue
                else:
                    withdraw_amount = int(withdraw_amount)

                if withdraw_amount == 0:
                    print("[ERROR] You can not withdraw PHP 0.\n")
                    continue
                elif withdraw_amount > balance:
                    print(f"[ERROR] You do not have enough balance to withdraw PHP {withdraw_amount}.\n")
                    continue

                balance -= withdraw_amount
                print(f"[RESPONSE] You have withdrawed PHP {withdraw_amount}.")
                print(f"[RESPONSE] Your current balance is now PHP {balance}.\n")

                if not empty_balance(balance):
                    customer_wants_another_withdrawal = input("[INPUT] Do you want to do another withdrawal (Y/N)?: ")
                    if customer_wants_another_withdrawal == "Y":
                        continue
                break
        case "3":
            yet_to_enter_correct_input = True
            while yet_to_enter_correct_input:
                deposit_amount = input("[INPUT] How much cash do you want to deposit: ").strip()
                if not_a_number(deposit_amount) or starts_with_0_and_has_many_digits(deposit_amount):
                    print("[ERROR] Your input is invalid. It must be a counting number.\n")
                    continue
                elif only_0(deposit_amount):
                    print("[ERROR] You can not deposit PHP 0.\n")
                    continue
                else:
                    yet_to_enter_correct_input = False
                    deposit_amount = int(deposit_amount)

                balance += deposit_amount
                print(f"[RESPONSE] You have deposited PHP {deposit_amount}.")
                print(f"[RESPONSE] Your balance is now PHP {balance}.\n")
        case "4":
            customer_wants_to_transact = False
            break
        case _:
            print("[ERROR] Invalid choice.")
            print()
    
    print("="*number_of_equal_signs)

print("[RESPONSE] Thank you for using our app. Have a nice day!")

# -------------------------------------------------
