"""
    if you just want to use this for checking if character in this file or not then
    we have to use dictionary because it's O(1) time complexity compared to list
    which is O(n) time complexity
"""


def getPossGujChars(filePath=None):
    allPossGujChars = "ૌ  ૈ ા ી ૂ બ હ ગ દ જ ડ ઼ ૉ ો ે ્ િ ુ પ ર ક ત ચ ટ ં " \
                      "મ ન વ લ સ ય ઍ ૅ ્ ર જ ત ક શ ઃ ઋ ઔ ઐ આ ઈ ઊ " \
                      "ભ ઙ ઘ ધ ઝ ઢ ઞ ઑ ઓ એ અ ઇ ઉ ફ ખ થ છ ઠ ઁ ણ ળ શ ષ ઠ"

    characters = list(set(map(str.strip, allPossGujChars.split())))
    characters.sort()

    v = ''
    characters = {k: v for k in allPossGujChars}
    # print("Total Characters :", len(characters))
    # print("All characters : \n", characters)

    if filePath is not None:
        file = open(filePath, 'wt', encoding='utf-8')

        for i in characters:
            file.write(i + '\n')
        file.close()

    else:
        return characters


if __name__ == "__main__":
    print(getPossGujChars())