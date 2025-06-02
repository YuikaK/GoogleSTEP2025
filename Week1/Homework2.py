import time
start = time.perf_counter()

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

def get_best(dictionary_words, letters): # 1番スコアの高いスコアと単語を返す関数
    letter_counts = {}  # letters に含まれる文字の出現回数を記録
    for c in letters:
        if c in letter_counts:
            letter_counts[c] += 1 #すでに文字が記録されているとき
        else: # 文字が初めて出たとき
            letter_counts[c] = 1

    best_score = 0
    best_word = ""

    for word in dictionary_words: #
        word_counts = {} # dictionary_wordsに含まれる文字の出現回数を記録
        for c in word:
            if c in word_counts:
                word_counts[c] += 1 #すでに文字が記録されているとき
            else: # 文字が初めて出たとき
                word_counts[c] = 1

        can_make = True # word_counts が letter_counts で表せるか確認する
        for c in word_counts:
            if c not in letter_counts or word_counts[c] > letter_counts[c]:
                can_make = False
                break

        if can_make:
            score = calculate_score(word)
            if score > best_score:
                best_score = score
                best_word = word

    return best_score, best_word

def main():
    data_words = read_words("anagram/large.txt") # "anagram/large.txt" "anagram/medium.txt"
    dictionary_words = read_words("anagram/words.txt")
    output_file = "anagram/large_answer.txt" # "anagram/large_answer.txt" "anagram/medium_answer.txt"

    results = []
    for letters in data_words:
        score, best_word = get_best(dictionary_words, letters)
        results.append(best_word)
    
    # 結果をファイルに出力
    with open(output_file, "w") as f:
        for word in results:
            f.write(word + "\n")

if __name__ == "__main__":
    main()

end = time.perf_counter() #計測終了
print('{:.2f}'.format(end-start))