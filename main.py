# This is a sample Python script.
import utils
a=0
b=1
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print(utils.converti_in_maiuscolo('hello world'))
print(utils.somma(a,b))
print(utils.sottrazione(a,b))
print(utils.moltiplicazione(a,b))
print(utils.divisione(a,b))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
numeri=[1,2,3,4]
quadrati=[numero**2 for numero in numeri]
#[trasformazione for elemento in elementi]
print(quadrati)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
