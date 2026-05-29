from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(os.path.abspath(__file__))

def text_wrap(text, max_chars):
    words = text.split()
    lines, line = [], []
    for w in words:
        if sum(len(x)+1 for x in line) + len(w) > max_chars:
            lines.append(' '.join(line))
            line = [w]
        else:
            line.append(w)
    if line:
        lines.append(' '.join(line))
    return lines

def draw_placeholder(path, width, height, bg_color, text_color, label, sub=""):
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    # 绘制简单网格背景
    grid = 60
    for x in range(0, width, grid):
        draw.line([(x, 0), (x, height)], fill=tuple(max(0,c-20) for c in bg_color), width=1)
    for y in range(0, height, grid):
        draw.line([(0, y), (width, y)], fill=tuple(max(0,c-20) for c in bg_color), width=1)
    # 中心文字
    try:
        font_big = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", max(24, min(72, width//12)))
        font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", max(14, min(36, width//20)))
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()
    # 主标签
    bbox = draw.textbbox((0,0), label, font=font_big)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text(((width-tw)//2, (height-th)//2 - (30 if sub else 0)), label, fill=text_color, font=font_big)
    # 尺寸标注
    size_text = f"{width} x {height}"
    if sub:
        size_text = f"{sub}  |  {size_text}"
    bbox2 = draw.textbbox((0,0), size_text, font=font_small)
    sw = bbox2[2]-bbox2[0]
    draw.text(((width-sw)//2, (height+th)//2 - 10), size_text, fill=tuple(min(255,c+80) for c in text_color), font=font_small)
    img.save(path)
    print(f"  Generated: {os.path.basename(path)}  ({width}x{height})")

# ─── 头像  200x200 ──────────────────────────────────────────────
draw_placeholder(os.path.join(OUT, "avatar.png"),
    200, 200, (37, 99, 235), (220, 235, 255), "AVATAR", "200×200")

# ─── Banner 亮色  1920x1080 ─────────────────────────────────────
draw_placeholder(os.path.join(OUT, "banner-light.webp"),
    1920, 1080, (224, 231, 255), (30, 58, 138), "BANNER (Light)", "1920×1080")

# ─── Banner 暗色  1920x1080 ─────────────────────────────────────
draw_placeholder(os.path.join(OUT, "banner-dark.webp"),
    1920, 1080, (15, 23, 42), (148, 179, 255), "BANNER (Dark)", "1920×1080")

# ─── 文章封面  800x400 ──────────────────────────────────────────
draw_placeholder(os.path.join(OUT, "placeholder-cover.png"),
    800, 400, (30, 41, 59), (148, 163, 184), "POST COVER", "800×400")

# ─── OG 分享图  1200x630 ────────────────────────────────────────
draw_placeholder(os.path.join(OUT, "og-image.png"),
    1200, 630, (17, 24, 39), (165, 180, 252), "Unk1ndled's Blog", "OG Image  1200×630")

print("\nAll placeholder images generated successfully!")
