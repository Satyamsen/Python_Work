# # balance = 0

# # def check_balance():
# #     return balance

# # def deposit_funds(amount):
# #     global balance
# #     balance += amount
# #     return f"Deposited {amount} INR. Current balance: {balance} INR"

# # def withdraw_funds(amount):
# #     global balance
# #     if amount > balance:
# #         return "Insufficient funds"
# #     else:
# #         balance -= amount
# #         return f"Withdrawn {amount} INR. Current balance: {balance} INR"

# # def main():
# #     global balance

# #     while True:
# #         print("\nBank Of India")
# #         print("1. Check Balance")
# #         print("2. Deposit Funds")
# #         print("3. Withdraw Funds")
# #         print("4. Exit")

# #         choice = input("Enter your choice: ")

# #         if choice == '1':
# #             print("Current Balance:", check_balance())
# #         elif choice == '2':
# #             amount = float(input("Enter the amount to deposit: "))
# #             print(deposit_funds(amount))
# #         elif choice == '3':
# #             amount = float(input("Enter the amount to withdraw: "))
# #             print(withdraw_funds(amount))
# #         elif choice == '4':
# #             print("Thank you for banking with Bank of India!")
# #             break
# #         else:
# #             print("Invalid choice. Please enter a valid option.")


# # if __name__ == "__main__":
# #     main()

# import random

# def get_user_choice():
#     while True:
#         user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
#         if user_choice in ['rock', 'paper', 'scissors']:
#             return user_choice
#         else:
#             print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     print("Welcome to Rock, Paper, Scissors!")

#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()

#         print(f"You chose: {user_choice}")
#         print(f"Computer chose: {computer_choice}")

#         result = determine_winner(user_choice, computer_choice)
#         print(result)

#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             print("Thank you for playing!")
#             break

# if __name__ == "__main__":
#     play_game()
