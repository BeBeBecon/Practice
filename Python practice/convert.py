#-------------------------------------------------------------------------------
#convert.py
# A program to convert Celsius temps to Fahrenheit
#-------------------------------------------------------------------------------

def main():
    celsius = eval(input("What is the Celsius temperrature?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temp is", fahrenheit, "degrees Fahrenheit.")

main()

