def stuff(something):
    has_alphanumeric = False
    has_alphabetical = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False
    for i in something:
        if i.isalnum():
            has_alphanumeric = True
        if i.isalpha():
            has_alphabetical = True
        if i.isdigit():
            has_digits = True
        if i.islower():
            has_lowercase = True
        if i.isupper():
            has_uppercase = True
    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)

if __name__ == '__main__':
    s = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
    print(len(s))
    stuff(s)