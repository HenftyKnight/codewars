def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6):
        if pin.isnumeric():
            return True
        return False

print(validate_pin("0123"))