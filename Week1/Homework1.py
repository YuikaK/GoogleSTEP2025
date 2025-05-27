def anagram_solution(random_word, dictionary):
    sorted_random_word = sorted(random_word) # ランダムな文字列をソート

    new_dictionary = []
    for word in dictionary:
        new_dictionary.append((sorted(word),word)) # ソートした辞書の単語と元の単語を合わせて保存
    new_dictionary = sorted(new_dictionary,key=lambda x: x[0]) # リストを0番目の要素でソート
    # new_dictionary[i][0]:単語をソートしたリスト
    # new_dictionary[i][1]:元の単語
    anagram = binary_search(new_dictionary, sorted_random_word)
    return anagram
    
def binary_search(sorted_dictionary, sorted_word):
    anagram = []
    left, right = 0, len(sorted_dictionary) - 1
    while left <= right:
        mid = left + (right - left) // 2 # 質問する "mid = left + right // 2" オーバーフロー？
        if sorted_dictionary[mid][0] < sorted_word: # 中央よりあとにあるとき
            left = mid + 1
        elif sorted_dictionary[mid][0] > sorted_word: # 中央より前にあるとき
            right = mid - 1
        else:
            anagram.append(sorted_dictionary[mid][1]) # anagramリストに元の単語を追加
            upper = mid + 1 # 中央よりひとつ後ろの要素も探す
            lower = mid - 1 # 中央よりひとつ前の要素も探す
            while True:
                if upper >= len(sorted_dictionary): # リストの長さを超えるとき
                    break
                if sorted_dictionary[upper][0] != sorted_word: # 単語が異なるとき
                    break
                anagram.append(sorted_dictionary[upper][1])
                upper += 1

            while True:
                if lower < 0: # 範囲外になるとき
                    break
                if sorted_dictionary[lower][0] != sorted_word: # 単語が異なるとき
                    break
                anagram.append(sorted_dictionary[lower][1])
                lower -= 1  
            break
    return anagram

def main():
    random_word = input()
    f = open("anagram/words.txt", 'r') # 読み込みモードで開く
    dictionary = f.readlines()
    for i in range(len(dictionary)):
        dictionary[i] = dictionary[i].replace('\n', '') # 改行を取り除く
    print(anagram_solution(random_word, dictionary))
    f.close()

if __name__ == "__main__":
    main()