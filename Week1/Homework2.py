SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
# score_checker.pyより
def calculate_score(word): 
    score = 0
    for character in list(word):
        score += SCORES[ord(character) - ord('a')]
    return score

def read_words(filename): # ファイル読み込み　中身をリストとして返す
    words = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            words.append(line)
    return words

def is_anagram(word, letters): # 辞書の単語がランダムな文字列に含まれる文字だけで作れるか
    letter_counts = {} # lettersにある文字とその数を記録するための辞書型　key:文字　value:回数
    for c in letters:
        if c in letter_counts: #すでに文字が記録されているとき
            letter_counts[c] += 1
        else: # 文字が初めて出たとき
            letter_counts[c] = 1

    for c in word: 
        if c not in letter_counts: # ランダムな文字列の文字に辞書の単語の文字が含まれていないとき
            return False
        if letter_counts[c] == 0: # 文字はあるが、使える回数が0回になっているとき
            return False
        letter_counts[c] -= 1 # ループごとにある文字の（使える）回数を1減らす

    return True # 作れるならTrueを返す

def main():
   
    data_words = read_words("anagram/large.txt") # "anagram/large.txt" "anagram/medium.txt"
    dictionary_words = read_words("anagram/words.txt")
    output_file = "anagram/large_answer.txt" # "anagram/large_answer.txt" "anagram/medium_answer.txt"

    results = []
    for letters in data_words:
        best_word = ""
        best_score = 0
        for word in dictionary_words:
            if is_anagram(word, letters): # アナグラムが作れるとき
                score = calculate_score(word)
                if score > best_score: # scoreが今までの中で一番良いとき
                    best_word = word
                    best_score = score
        results.append(best_word)

    # 結果をファイルに出力
    with open(output_file, "w") as f:
        for word in results:
            f.write(word + "\n")

if __name__ == "__main__":
    main()