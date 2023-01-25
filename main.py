import random
import json
from kana2vowel import kana2vowel
from pronounce import getPronunciation


class Naniyuki:
    def __init__(self, keyword="感想"):
        self.keyword = keyword
        self.pronounce = getPronunciation(keyword)
        self.vowel = kana2vowel(self.pronounce)
        self.keywordBasedRandom = self.getNewRandom("keyword")
        self.pronounceBasedRandom = self.getNewRandom("pronounce")
        self.vowelBasedRandom = self.getNewRandom("vowel")

    def getNewRandom(self, base: str = "keyword", additional_seed: int = 0) -> int:
        if not base in ["keyword", "pronounce", "vowel"]:
            print(f"error: invalid base {base}")
            return False

        additional_seed = str(additional_seed) if additional_seed != 0 else ""

        if base == "keyword":
            random.seed(self.keyword + additional_seed)
        elif base == "pronounce":
            random.seed(self.pronounce + additional_seed)
        elif base == "vowel":
            random.seed(self.vowel + additional_seed)
        return random.random()

    def getRandom(self, base="keyword"):
        if not base in ["keyword", "pronounce", "vowel"]:
            print(f"error: invalid base {base}")
            return False

        if base == "keyword":
            return self.keywordBasedRandom
        elif base == "pronounce":
            return self.pronounceBasedRandom
        elif base == "vowel":
            return self.vowelBasedRandom

    def tryRandom(self, probability: float, seed: int = None, base: str = "keyword") -> bool:
        if not 0 <= probability < 1:
            print(f"error: invalid probability {probability}")
            return False
        random = self.getRandom(base)
        if seed is not None:
            random = self.getNewRandom(base, seed)
        return probability > random

    def getNaniyuki(self):
        translatedNaniyuki = self.translateUniqueNaniyuki(self.keyword)
        pronounce = self.pronounce
        keyword = self.keyword
        vowel = self.vowel
        plength = len(self.pronounce)

        # ひろゆき
        if keyword == "感想":
            return "ひろゆき"

        # 僕の彼女というか妻というか細君というか奥さんというか
        elif translatedNaniyuki:
            return translatedNaniyuki

        # プリクラ博之
        elif plength == 4 and vowel[-2:] == "ウア" and pronounce[-1] == "ラ":
            return keyword + "博之"

        # 道草博之
        elif vowel == "イイウア":
            return keyword + "博之"

        # 南村博之
        elif keyword in ["東", "西", "南", "北"]:
            return keyword + "村博之"

        # 台所浩二
        elif pronounce[-3:] == "ドコロ":
            return keyword + "浩二"

        # はまぐり
        elif plength == 4 and vowel[-2:] == "ウイ":
            return keyword

        # 餅ゆき
        elif plength == 2 and self.tryRandom(0.5, base="pronounce"):
            return keyword + "ゆき"

        # 加湿器, 切り抜き
        elif plength == 4 and pronounce[-1] == "キ":
            return keyword
        
        # # どぴゅゆき
        # elif 

        # ハンバーグひろゆき
        else:
            return keyword + "ひろゆき"

    def translateUniqueNaniyuki(self, keyword):
        path = "unique.json"
        result = None

        with open(path) as f:
            unique = json.load(f)
        for e in unique:
            if (
                keyword in e["keywords"]
                or self.pronounce in e["pronounces"]
                or self.vowel in e["vowels"]
            ):
                result = e["pattern"]
                result = result.format(keyword)
                break
        return result


def main():
    while True:
        keyword = input("\nkeyword?: ")
        if keyword == "":
            continue
        naniyuki = Naniyuki(keyword)
        print(f"{naniyuki.getNaniyuki()} 「それってあなたの{keyword}ですよね」")

        # print("\ndebug information")
        # print("Pronounce:      " + getPronunciation(keyword))
        # print("K Based Random: " + str(naniyuki.getRandom("keyword")))
        # print("P Based Random: " + str(naniyuki.getRandom("pronounce")))
        # print("V Based Random: " + str(naniyuki.getRandom("vowel")))


if __name__ == "__main__":
    main()
