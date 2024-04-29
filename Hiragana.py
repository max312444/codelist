import random

Hiragana = [["あ", "a"],["い", "i"],["う", "u"],["え", "e"],["お", "o"],
            ["か", "ka"],["き", "ki"],["く", "ku"],["け", "ke"],["こ", "ko"],
            ["さ", "sa"],["し", "shi"],["す", "su"],["せ", "se"],["そ", "so"],
            ["た", "ta"],["ち", "chi"],["つ", "tsu"],["て", "te"],["と", "to"],
            ["な", "na"],["に", "ni"],["ぬ", "nu"],["ね", "ne"],["の", "no"],
            ["は", "ha"],["ひ", "hi"],["ふ", "fu"],["へ", "he"],["ほ", "ho"],
            ["ま", "ma"],["み", "mi"],["む", "mu"],["め", "me"],["も", "mo"],
            ["や", "ya"],["ゆ", "yu"],["よ", "yo"],
            ["ら", "ra"],["り", "ri"],["る", "ru"],["れ", "re"],["ろ", "ro"],
            ["わ", "wa"],["を", "o"], 
            ["ん", "n"],
            ["が", "ga"],["ぎ", "gi"],["ぐ", "gu"],["げ", "ge"],["ご", "go"],
            ["ざ", "za"],["じ", "zi"],["ず", "zu"],["ぜ", "ze"],["ぞ", "zo"],
            ["だ", "da"],["ぢ", "ji"],["づ", "zu"],["で", "de"],["ど", "do"],
            ["ば", "ba"],["び", "bi"],["ぶ", "bu"],["べ", "be"],["ぼ", "bo"],
            ["ぱ", "pa"],["ぴ", "pi"],["ぷ", "pu"],["ぺ", "pe"],["ぽ", "po"],]
while(1):
    Question = random.randrange(47, 71) #46은 n까지 71은 전체

    print("다음 히라가나의 발음을 입력하시오:", Hiragana[Question][0])

    Answer = input()

    if(Answer == Hiragana[Question][1]):
        print(f"\n정답입니다\n{Hiragana[Question][0]}의 발음은 {Hiragana[Question][1]}입니다.\n")
    elif(Answer == "exit"):
        break
    else:
        print(f"\n오답입니다\n{Hiragana[Question][0]}의 발음은 {Hiragana[Question][1]}입니다.\n")
