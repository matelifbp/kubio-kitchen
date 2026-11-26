"""クビ男の台所: レシピページ (recipes/*.html) を作る。もしものメディア登録の「5記事以上」のため (2026-11-26)。
使い方: python make_recipes.py   → recipes/ に各ページと index.html の一覧用の断片を書き出す
材料と値段は動画のテロップ (claudecode\\縦動画\\telop.py) と同じ。調味料は値段に入れない。
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).parent
OUT = HERE / "recipes"


def link(path):
    return ("https://af.moshimo.com/af/c/click?a_id=5917070&amp;p_id=54&amp;pc_id=54&amp;pl_id=616&amp;url="
            + quote(f"https://item.rakuten.co.jp/{path}/", safe=""))


ITEMS = {   # 楽天の商品 (index.html のカードと同じもの)
    "frypan": ("小さいフライパン", "貝印 軽いフライパン 20cm", "kai/000dw5629"),
    "pot": ("片手鍋", "カクセー ステンレス片手鍋 16cm ガラス蓋付", "livingplaza/10006509"),
    "knife": ("包丁", "Riverline 三徳包丁 16.5cm", "nagomi-ec/rl-st"),
    "board": ("まな板", "抗菌まな板（食洗機対応）", "aurora77/manaita"),
    "rice": ("お米", "岡山県産 コシヒカリ 無洗米 5kg", "okaman/10000003"),
    "pasta": ("パスタ", "マ・マー スパゲティ 1.6mm 1kg", "rakuten24/4902110264388"),
    "miso": ("味噌汁の素", "永谷園 あさげ 業務用 30食", "kk1206/syoku00221"),
    "mentsuyu": ("めんつゆ", "ミツカン 追いがつおつゆ 2倍 1L", "rakuten24/e339049h"),
    "gara": ("鶏ガラスープの素", "味の素 丸鶏がらスープ 瓶 55g", "jetprice/x20561"),
    "curry": ("カレールー", "ハウス バーモントカレー 中辛 230g", "matsukiyo/4902402853887"),
}

RECIPES = [
    dict(slug="tsukune", no=32, name="焼きつくね丼", yen=45, series="限界飯",
         lead="肉は買えないので、豆腐ともやしでつくねを作りました。50円以内の「限界飯」シリーズ、1回目です。",
         parts=[("もやし", 5), ("豆腐", 10), ("ごはん", 30)],
         steps=["もやしを包丁で細かく刻みます。",
                "豆腐ともやしを皿の上でよく混ぜます。",
                "スプーンで小さく丸めて、フライパンに並べます。両面に焼き色がつくまで焼きます。",
                "タレを絡めて照りを出します（タレは家にある調味料で。値段には入れていません）。",
                "ごはんにのせて、ごまをふったら完成です。"],
         tip="豆腐の水気が多いと崩れやすいので、混ぜる前に軽く水を切っておくと丸めやすいです。",
         joke=("肉は豆腐で代わりがききます。", "僕の代わりも、いくらでもいました。"),
         tools=["frypan", "knife", "board", "rice"]),
    dict(slug="kinoko", no=31, name="きのこクリームうどんセット", yen=79, series="貧乏メシ",
         lead="今日の主役はしめじです。クリームソースをかければ、うどんも洋食になります。",
         parts=[("しめじ", 10), ("玉ねぎ（スープ）", 9), ("うどん", 30), ("クリームソース", 30)],
         steps=["しめじを包丁で食べやすく切ります。",
                "フライパンでしめじを炒め、クリームソースを入れて温めます。",
                "ゆでたうどんを器に盛ります。",
                "上からきのこのクリームソースをかけます。",
                "玉ねぎを薄く切ってスープにして、セットにします。"],
         tip="ソースは少し煮詰めると、うどんによく絡みます。",
         joke=("しめじは株で増えるのに、", "僕の株は下がる一方です。"),
         tools=["frypan", "pot", "knife", "board"]),
    dict(slug="moyasi", no=30, name="もやし炒め定食", yen=72, series="貧乏メシ",
         lead="肉は買えないので、シューマイを刻んで肉の代わりにしました。もやしでかさ増しすれば、おなかはふくれます。",
         parts=[("もやし", 10), ("ニラ", 10), ("シューマイ", 11), ("味噌汁", 11), ("ごはん", 30)],
         steps=["ニラを食べやすい長さに切ります。",
                "シューマイを細かく刻みます。",
                "フライパンでシューマイとニラを炒めます。",
                "もやしを入れて、強火でさっと炒めます。",
                "皿に盛って、味噌汁とごはんを添えたら定食になります。"],
         tip="もやしは炒めすぎると水っぽくなるので、最後に入れて手早く仕上げます。",
         joke=("もやしは日陰でも育つのに、", "僕はいつまでも芽が出ません。"),
         tools=["frypan", "knife", "board", "miso", "rice"]),
    dict(slug="tyahan", no=18, name="チャーハン定食", yen=82, series="貧乏メシ",
         lead="卵かけごはんを炒めると、パラパラになるそうです。今回も肉担当はシューマイ1個です。",
         parts=[("ごはん", 30), ("玉子", 20), ("シューマイ", 11), ("たくあん", 10), ("味噌汁", 11)],
         steps=["シューマイを細かく刻みます。",
                "ごはんに玉子をかけて、よく混ぜておきます（卵かけごはん）。",
                "フライパンでシューマイと卵かけごはんを炒めます。",
                "茶碗に詰めて皿にひっくり返すと、お店っぽい形になります。",
                "たくあんと味噌汁を添えて完成です。"],
         tip="ごはんに先に玉子を混ぜておくと、ダマになりにくく、パラパラに仕上がります。",
         joke=("強火で炒めても、", "財布は冷え込む一方です。"),
         tools=["frypan", "gara", "rice", "miso"]),
    dict(slug="curry", no=9, name="野菜カレー", yen=95, series="貧乏メシ",
         lead="肉なしの野菜カレーです。カレーは裏切りません。そして白米が炊けているだけで勝ちです。",
         parts=[("カボチャ", 8), ("玉ねぎ", 9), ("ニンジン", 21), ("ジャガイモ", 9), ("カレールー", 18), ("ごはん", 30)],
         steps=["カボチャ、玉ねぎ、ニンジン、ジャガイモを食べやすい大きさに切ります。",
                "鍋に野菜と水を入れて、やわらかくなるまで煮ます。",
                "火を止めてカレールーを溶かし、もう一度とろみがつくまで煮込みます。",
                "ごはんにかけて完成です。"],
         tip="カボチャは煮崩れて甘みが出るので、肉がなくてもコクが出ます。",
         joke=("肉の代わりは、", "…想像力で補おうと思います。"),
         tools=["pot", "knife", "board", "curry", "rice"]),
    dict(slug="nori", no=8, name="海苔パスタ", yen=39, series="貧乏メシ",
         lead="めんつゆ＋マヨで和風パスタは、だいたいいけると悟りました。",
         parts=[("パスタ", 28), ("海苔", 11)],
         steps=["海苔を細く切ります。",
                "パスタをゆでます。",
                "フライパンにパスタを入れ、めんつゆとマヨネーズで味をつけます。オイスターソースを少し足すと、味が締まります。",
                "皿に盛って、海苔をたっぷりのせたら完成です。"],
         tip="めんつゆとマヨネーズは、火を止めてから絡めると分離しにくいです。",
         joke=("海苔は高級食材だと", "気付きました。"),
         tools=["pasta", "mentsuyu", "frypan", "pot"]),
]

PAGE = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{yen}円で{name}｜クビ男の台所</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="recipe.css">
</head>
<body>
<div class="pr-bar">当サイトはアフィリエイト広告（PR）を利用しています</div>
<nav class="wrap crumb"><a href="../index.html">クビ男の台所</a> ＞ <a href="../index.html#recipes">レシピ</a> ＞ {name}</nav>
<main class="wrap">
  <article>
    <p class="label">{series}｜第{no}回</p>
    <h1><span>{yen}円</span>で{name}</h1>
    <p class="lead">{lead}</p>
    <div class="photos">
      <img src="../images/recipes/{slug}.jpg" alt="{name}の完成" width="540" height="960">
      <img src="../images/recipes/{slug}_step.jpg" alt="{name}を作っているところ" width="540" height="960">
    </div>

    <h2>材料と値段（1人前）</h2>
    <table class="parts">
{parts}
      <tr class="total"><th>合計</th><td>{yen}円</td></tr>
    </table>
    <p class="small">※値段は、近所のスーパーで買ったときの1食分の目安です。しょうゆ・油などの調味料は入れていません。</p>

    <h2>作り方</h2>
    <ol class="steps">
{steps}
    </ol>
    <p class="tip"><b>ひとこと</b>{tip}</p>

    <h2>今日のクビ男</h2>
    <p class="joke">{joke}</p>

    <h2>この料理で使った道具・食材</h2>
    <p class="small">動画で使っているものに近い商品を、楽天市場で選びました（同じものとは限りません）。</p>
    <div class="tools">
{tools}
    </div>
    <p class="small">値段や在庫は変わることがあるので、リンク先でご確認ください。</p>

    <p class="sns">動画は <a href="https://www.instagram.com/kubiotoko_meshi/" target="_blank" rel="noopener">Instagram</a> と <a href="https://www.tiktok.com/@kubiotoko_meshi" target="_blank" rel="noopener">TikTok</a> で見られます。</p>
  </article>

  <section class="others">
    <h2>ほかのレシピ</h2>
    <ul>
{others}
    </ul>
  </section>
</main>
<footer>
  <div class="wrap">
    <p>当サイトは、楽天市場などのアフィリエイトプログラムを利用しています。紹介している商品のリンクから購入されると、運営者に報酬が入ることがあります。</p>
    <img class="imp" src="https://i.moshimo.com/af/i/impression?a_id=5917070&amp;p_id=54&amp;pc_id=54&amp;pl_id=616" width="1" height="1" alt="" loading="lazy">
    <p class="copy">© クビ男の台所</p>
  </div>
</footer>
</body>
</html>
"""


def build():
    OUT.mkdir(exist_ok=True)
    for r in RECIPES:
        e = {k: escape(str(v)) for k, v in r.items() if isinstance(v, (str, int))}
        parts = "\n".join(f"      <tr><th>{escape(n)}</th><td>{y}円</td></tr>" for n, y in r["parts"])
        steps = "\n".join(f"      <li>{escape(s)}</li>" for s in r["steps"])
        tools = "\n".join(
            f'      <a class="buy" href="{link(ITEMS[t][2])}" target="_blank" rel="nofollow sponsored noopener">'
            f'<small>{escape(ITEMS[t][0])}</small>{escape(ITEMS[t][1])}<span>楽天市場で見る（PR）</span></a>' for t in r["tools"])
        others = "\n".join(f'      <li><a href="{o["slug"]}.html">{escape(o["name"])}</a><span>{o["yen"]}円</span></li>'
                           for o in RECIPES if o is not r)
        desc = f'{r["yen"]}円で{r["name"]}。材料と値段、作り方を紹介します。会社をクビになった男の、1食100円以内の貧乏メシ。'
        html = PAGE.format(**e, desc=escape(desc), parts=parts, steps=steps,
                           joke="<br>".join(escape(j) for j in r["joke"]), tools=tools, others=others)
        (OUT / f'{r["slug"]}.html').write_text(html, encoding="utf-8")
    cards = "\n".join(
        f'      <a class="recipe" href="recipes/{r["slug"]}.html"><img src="images/recipes/{r["slug"]}.jpg" alt="" width="540" height="960" loading="lazy">'
        f'<span class="tag">{escape(r["series"])}｜第{r["no"]}回</span><b>{escape(r["name"])}</b><span class="yen">{r["yen"]}円</span></a>'
        for r in RECIPES)
    (HERE / "_recipe_cards.html").write_text(cards, encoding="utf-8")
    print("done", len(RECIPES), "pages")


if __name__ == "__main__":
    build()
