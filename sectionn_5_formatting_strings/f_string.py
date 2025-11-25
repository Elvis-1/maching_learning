name = 'Zoe'
temperature = 32.3356

greetings = "Hello {}, the temperature is {:.1f} C".format(name,temperature)

greetings = f"Hello {name.upper()}, the temperature is {temperature:.1f} C"
print(greetings)