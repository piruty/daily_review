#! /usr/bin/env python3
# coding: utf-8


def main():
    date = input("何日のレビューですか？ >> ")
    review_body = ""

    # ---- 今日の健康状態

    review_body += "## 今日の健康状態\n\n"

    sleep = input("睡眠時間(h) >> ")
    review_body += "### 睡眠時間\n\n{0}時間\n\n".format(sleep)

    weight = input("体重(kg) >> ")
    review_body += "### 体重\n\n{0}kg\n\n".format(weight)

    fat_rate = input("体脂肪率(％) >> ")
    review_body += "### 体脂肪率\n\n{0}%\n\n".format(fat_rate)

    review_body += "-----\n\n"

    # ---- ポモドーロ数

    review_body += "## ポモドーロ数\n\n"

    pomodoro = input("今日のポモドーロ数 >> ")
    review_body += "### 今日のポモドーロ数\n\n{0}\n\n".format(pomodoro)

    review_body += "-----\n\n"

    # ---- 習慣のチェック

    review_body += "## 習慣のチェック\n\n"

    answer = create_ox("「すごいHaskell」の写経をしましたか？")
    review_body += "### 「すごいHaskell」の写経をしましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("「SoftSkills」は読みましたか？")
    review_body += "### 「SoftSkills」は読みましたか？\n\n{0}\n\n".format(answer)

    review_body += "-----\n\n"

    # ---- 機械学習 習慣確認

    review_body += "## 機械学習 習慣確認\n\n"

    answer = create_ox("「ゼロから作るDeep Learing」は読むか書くかしましたか？")
    review_body += "### 「ゼロから作るDeep Learing」は読むか書くかしましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("「自然言語の基本と技術」は読みましたか？")
    review_body += "### 「自然言語の基本と技術」は読みましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("その他、機械学習に関わることは何かしましたか？（kaggleの問題を解いた など）")
    review_body += "### その他、機械学習に関わることは何かしましたか？（kaggleの問題を解いた など）\n\n{0}\n\n".format(answer)

    review_body += "-----\n\n"

    # ---- プログラミングによる問題解決能力向上委員会

    review_body += "## プログラミングによる問題解決能力向上委員会\n\n"

    answer = create_ox("プログラミングの問題（AOJ, paiza, CodeIQ, TopCoderなど）は解きましたか？")
    review_body += "### プログラミングの問題（AOJ, paiza, CodeIQ, TopCoderなど）は解きましたか？\n\n{0}\n\n".format(answer)

    review_body += "-----\n\n"

    # ---- 独立してやっていこうぜ交響楽団

    review_body += "## 独立してやっていこうぜ交響楽団\n\n"

    answer = create_ox("ブログは書きましたか？")
    review_body += "### ブログは書きましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("独自のアプリは実装しましたか？")
    review_body += "### 独自のアプリは実装しましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("配信用の動画は撮りましたか？")
    review_body += "### 配信用の動画は撮りましたか？\n\n{0}\n\n".format(answer)

    review_body += "-----\n\n"

    # ---- Why not study English??

    review_body += "## Why not study English??\n\n"

    answer = create_ox("「Global News Podcast」は聞きましたか？")
    review_body += "### 「Global News Podcast」は聞きましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("英単語は確認しましたか？")
    review_body += "### 英単語は確認しましたか？\n\n{0}\n\n".format(answer)

    review_body += "-----\n\n"

    # ---- 手書きメモの振返り

    review_body += "## Why not study English??\n\n"

    answer = create_ox("手書きメモは確認しましたか？")
    review_body += "### 手書きメモは確認しましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("Trelloは確認しましたか？")
    review_body += "### Trelloは確認しましたか？\n\n{0}\n\n".format(answer)

    answer = create_ox("Amazonの欲しいものリストは確認しましたか？")
    review_body += "### Amazonの欲しいものリストは確認しましたか？\n\n{0}\n\n".format(answer)

    review_body += "-----\n\n"

    # ---- 今日の一言

    todays_voice = input("今日の一言は？ >> ")
    review_body += "## 今日の一言\n\n{0}".format(todays_voice)

    with open("{0}.md".format(date), "w+", encoding='utf-8') as f:
        f.write(review_body)


def create_ox(q):
    answer = input("{0} (1 or o: o, else: x) >> ".format(q))
    if answer == "1" or answer == 'o':
        return 'o'
    return "x"


def create_ox_with_comment(q):
    answer = input("{0} (1 or o: o, else: x) >> ".format(q))
    comment = input("気になったことはありますか？ (無ければ未入力) >> ".format(q))
    answer_ox = 'o' if answer == "1" or answer == 'o' else 'x'
    return answer_ox, comment


if __name__ == '__main__':
    main()
