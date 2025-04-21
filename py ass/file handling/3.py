import vobject

def create_vcard():
    name = input("Full name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    vcard = vobject.vCard()
    vcard.add('fn').value = name
    vcard.add('tel').value = phone
    vcard.add('email').value = email

    with open(f"{name}.vcf", "w") as f:
        f.write(vcard.serialize())

    print(f"VCard for {name} created successfully!")