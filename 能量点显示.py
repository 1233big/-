def create_character(name,strength, intelligence, charisma):
    full_dot = '●'
    empty_dot = '○'
    if not isinstance(name,str):
        return 'The character name should be a string'
    elif name == "":
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if not (isinstance(strength, int) and
        isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4  or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence +charisma != 7:
        return 'The character should start with 7 points'
    def get_dots(num):
        return full_dot * num + empty_dot * (10 - num)
    line1 = name
    line2 = f"STR {get_dots(strength)}"
    line3 = f"INT {get_dots(intelligence)}"
    line4 = f"CHA {get_dots(charisma)}"

    return "\n".join([line1, line2, line3, line4])
print(create_character('ren', 4, 2, 1))



