# 以下のリンクより参照
# https://www.keishicho.metro.tokyo.lg.jp/tetsuzuki/other/style/lost.html
# おそらくフォームフィールド無い；；
# 画像に変換して編集する方針
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image, ImageDraw, ImageFont

# 画像を読み込む
image = Image.open("style05.jpg")

# フォントの設定
font = ImageFont.truetype('Arial.ttf', 24)

# 描画用のオブジェクトを作成
draw = ImageDraw.Draw(image)

# 色を指定
color = 'black'

# テキスト追記
# 年月日
year, month, day = "2024", "11", "09"
draw.text((830,  52), year , color, font=font)
draw.text((930,  52), month, color, font=font)
draw.text((1000, 52), day  , color, font=font)

# 画像を保存
image.save("output_image.png")

# PDFとして保存
image.save("output.pdf", 'PDF', resolution=100.0)
