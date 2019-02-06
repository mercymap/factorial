
def power(number, power_to_raise):
  if power_to_raise == 0:
    return 1
  else:
    power_to_raise = power_to_raise - 1
    return number * power(number, power_to_raise)

result = power(2, 3)
print(result)