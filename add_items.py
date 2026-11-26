"""クビ男の台所: 商品カードを index.html に足す (2026-11-26 ユーザー「クビ男に合う商品を30個」)。
写真は商品写真ではなく、これまでの動画の場面 (images/items/*.jpg) を使う (ユーザー「あからさまにアフィリエイトとわかるものじゃなく自然な写真」)。
一度だけ実行する (<!-- items:... --> の印があれば足さない)。
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).parent


def link(path):
    return ("https://af.moshimo.com/af/c/click?a_id=5917070&amp;p_id=54&amp;pc_id=54&amp;pl_id=616&amp;url="
            + quote(f"https://item.rakuten.co.jp/{path}/", safe=""))


# (写真, タグ, 見出し, 説明, 動画では (なければ ""), 商品名, 楽天の 店/商品コード)
TOOLS = [
    ("saibashi", "調理器具", "菜箸", "炒めるのも、盛りつけるのも菜箸です。竹のものは軽くて、手になじみます。", "チャーハン、もやし炒め など", "酒井産業 竹の菜箸 33cm 3膳セット", "kurashino/145211"),
    ("otama", "調理器具", "お玉", "カレーも味噌汁も、すくうのはこれ一本。安いステンレスで十分です。", "野菜カレー", "ケユカ ステンレスレードル", "keyuca/3501261"),
    ("turner", "調理器具", "フライ返し", "豆腐ステーキやつくねを返すときに。薄いほうが、崩さずに返せます。", "", "貝印 SELECT100 ターナー", "thinkrich/sk02921"),
    ("bowl", "調理器具", "ボウルとザル", "麺の湯切り、野菜を洗う、混ぜる。セットで持っておくと困りません。", "", "貝印 ステンレス ボウル・ザル 6点セット", "kai/ss0032"),
    ("hasami", "調理器具", "キッチンばさみ", "海苔もネギも、まな板を出さずに切れます。洗い物が一つ減ります。", "海苔パスタ（海苔を切るところ）", "貝印 SELECT100 キッチンばさみ", "kai/000dh3005"),
    ("peeler", "調理器具", "ピーラー", "ニンジンやジャガイモの皮むきに。包丁より、むく皮が薄くてすみます。", "", "貝印 SELECT100 T型ピーラー", "kai/000dh3000"),
    ("youki", "調理器具", "保存容器", "多めに炊いたごはんや、残ったおかずを小分けに。レンジでそのまま温められます。", "", "ケユカ フタごとレンジパック 4個セット", "keyuca/s3300977"),
    ("donburi", "食器", "どんぶり", "丼ものは、器がそれっぽいだけで少し豪華に見えます。", "", "多用どんぶり（色・柄が選べる）", "longisland/don"),
    ("suihanki", "家電", "3合の炊飯器", "一人暮らしなら3合で足ります。ごはんが炊けていれば、だいたい何とかなります。", "", "象印 マイコン炊飯器 極め炊き 3合", "shopworld/143916-143917"),
]
FOODS = [
    ("wakame", "食材", "乾燥わかめ", "ひとつまみで、ラーメンも味噌汁も具だくさんに見えます。日持ちするのも助かります。", "醤油ラーメン、月見うどん", "カットわかめ 業務用 200g", "segawahonten/04935006"),
    ("katakuri", "食材", "片栗粉", "あんかけのとろみや、つくねのつなぎに。少しあると料理の幅が広がります。", "", "北海道産 片栗粉 1kg", "tabemon-dikara/660"),
    ("nori", "食材", "味付け海苔", "パスタにのせても、おにぎりに巻いても。訳ありなら、たっぷり入って安いです。", "海苔パスタ（39円）", "訳あり 有明産 味付海苔 8切160枚", "komanori/compass1631340650"),
    ("katsuobushi", "食材", "かつお節パック", "うどんや冷奴に一袋かけるだけで、ちゃんとした味になります。", "", "はごろも かつおパック 3g×20袋", "goodys/kezuribusi"),
    ("udon", "食材", "乾麺のうどん", "乾麺なら買い置きができます。月見にしても、焼きうどんにしても。", "", "北海道産小麦 乾麺うどん", "kitakuranohatake/fw-jikonaudon-5"),
]
SEASONINGS = [
    ("mayo", "調味料", "マヨネーズ", "めんつゆと合わせると、和風パスタはだいたいいけます。", "海苔パスタ", "キユーピー マヨネーズ 450g", "rakuten24/e350358h"),
    ("shoyu", "調味料", "しょうゆ", "結局いちばん使う調味料です。迷ったらこれをかけています。", "", "キッコーマン しょうゆ 1L", "rakuten24/4901515111150"),
    ("oyster", "調味料", "オイスターソース", "少し足すだけで、味がぐっと締まります。中華っぽくしたい日に。", "海苔パスタ（隠し味）", "李錦記 オイスターソース 255g", "rakuten24/e236746h"),
    ("goma", "調味料", "いりごま", "最後にふるだけで、それっぽく見えます。業務用なら長く持ちます。", "焼きつくね丼", "かどや いりごま 白 業務用 1kg", "rakuten24/4901458200140"),
    ("dashi", "調味料", "顆粒だし", "味噌汁もうどんのつゆも、これがあれば一から作れます。", "", "味の素 ほんだし 箱（60g×2袋）", "rakuten24/4901001084159"),
    ("shantan", "調味料", "中華だし", "チャーハンやスープに。肉がなくても、肉っぽいコクが出ます。", "", "創味シャンタン デラックス 250g", "rakuten24/e398743h"),
]


def card(photo, tag, title, text, used, name, path):
    u = f'<p class="used">動画では：{escape(used)}</p>' if used else ""
    return (f'      <div class="card"><span class="tag">{escape(tag)}</span><h3>{escape(title)}</h3>'
            f'<img class="pic" src="images/items/{photo}.jpg" alt="{escape(title)}を使った料理" width="540" height="540" loading="lazy">'
            f'<p>{escape(text)}</p>{u}'
            f'<a class="buy" href="{link(path)}" target="_blank" rel="nofollow sponsored noopener">{escape(name)}<span>楽天市場で見る（PR）</span></a></div>')


def main():
    p = HERE / "index.html"
    s = p.read_text(encoding="utf-8")
    if "<!-- items:" in s:
        print("already added")
        return
    css = "  .card img.pic { width: 100%; height: auto; aspect-ratio: 1 / 1; object-fit: cover; border-radius: 12px; margin: 4px 0; }\n"
    s = s.replace("  .pick-note {", css + "  .pick-note {", 1)
    for sec, items in [("tools", TOOLS), ("foods", FOODS), ("seasonings", SEASONINGS)]:
        i = s.index(f'<section id="{sec}">')
        j = s.index("    </div>\n", i)   # その section のカード一覧の終わり
        add = f"<!-- items:{sec} -->\n" + "\n".join(card(*it) for it in items) + "\n"
        s = s[:j] + add + s[j:]
    p.write_text(s, encoding="utf-8")
    print("added", len(TOOLS) + len(FOODS) + len(SEASONINGS))


if __name__ == "__main__":
    main()
