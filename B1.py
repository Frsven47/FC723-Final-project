import string

booking_references = set()

def generate_booking_reference():
    while True:
        ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if ref not in booking_references:
            booking_references.add(ref)
            return ref

#Sample Use
print(generate_booking_reference())
