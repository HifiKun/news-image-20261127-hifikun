#!/usr/bin/env python3
"""Draw the front page for Friday 27 November 2026.

A newspaper front page, 1024x1024, drawn from scratch with Pillow:
masthead, one lead story with a drawn scene, three picture stories
and a briefs strip. Every fact is news first reported on 27 Nov 2026.
Run: python3 draw_front.py  ->  entry.png
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 243, 232)
INK = (22, 22, 22)
RED = (176, 30, 30)
BLUE = (26, 64, 122)
GREY = (96, 92, 84)
SKY = (18, 32, 64)
ORANGE = (206, 92, 18)
TEAL = (16, 108, 108)
GOLD = (170, 128, 22)
LIGHT = (226, 232, 240)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(d, text, font, width):
    """Greedy word wrap to a pixel width."""
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def para(d, x, y, text, font, width, fill=INK, leading=None):
    """Draw a wrapped paragraph; return y below the last line."""
    leading = leading or int(font.size * 1.3)
    for line in wrap_lines(d, text, font, width):
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def hline(d, x0, x1, y, fill=INK, width=2):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


def pic_kuwait(d, x, y, w, h):
    """Night sky over Kuwait: towers, a drone, smoke."""
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    for sx, sy in [(30, 26), (90, 60), (150, 30), (210, 70), (280, 40),
                   (340, 24), (390, 66), (120, 90), (250, 96)]:
        d.ellipse([x + sx - 2, y + sy - 2, x + sx + 2, y + sy + 2],
                  fill=(240, 240, 200))
    # Kuwait Towers: three spires with spheres.
    for tx, th in [(60, 120), (150, 150), (250, 110)]:
        d.rectangle([x + tx - 7, y + h - th, x + tx + 7, y + h],
                    fill=(70, 90, 130))
        d.ellipse([x + tx - 24, y + h - th - 18, x + tx + 24, y + h - th + 30],
                  fill=(120, 150, 190))
    d.rectangle([x + 320, y + h - 90, x + 380, y + h], fill=(70, 90, 130))
    d.rectangle([x + 390, y + h - 60, x + 430, y + h], fill=(70, 90, 130))
    # Smoke plume rising from the city, low on the right.
    for i, r in enumerate([14, 18, 22]):
        d.ellipse([x + 330 + i * 8 - r, y + h - 150 - i * 20 - r,
                   x + 330 + i * 8 + r, y + h - 150 - i * 20 + r],
                  fill=(120, 118, 112))
    # Drone: small quadcopter with red lights, upper left.
    cx, cy = x + 110, y + 56
    d.line([(cx - 34, cy - 16), (cx + 34, cy + 16)], fill=(220, 220, 220),
           width=3)
    d.line([(cx - 34, cy + 16), (cx + 34, cy - 16)], fill=(220, 220, 220),
           width=3)
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(230, 230, 230))
    d.ellipse([cx - 38, cy - 20, cx - 30, cy - 12], fill=RED)
    d.ellipse([cx + 30, cy + 12, cx + 38, cy + 20], fill=RED)
    d.text((x + 12, y + 10), "KUWAIT CITY", font=fnt(SANS_B, 20),
           fill=(255, 255, 255))


def pic_gaza(d, x, y, w, h):
    """Dusk skyline with damaged buildings and smoke."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 196, 150))
    d.ellipse([x + w - 70, y + 14, x + w - 10, y + 74], fill=(240, 180, 90))
    for bx, bw, bh, tilt in [(0, 70, 100, 0), (80, 60, 120, 8),
                             (150, 80, 85, 0), (240, 60, 110, -6)]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h],
                    fill=(90, 78, 70))
        if tilt:
            d.polygon([(x + bx, y + h - bh), (x + bx + bw, y + h - bh),
                       (x + bx + bw - tilt, y + h - bh - 18),
                       (x + bx + 14, y + h - bh - 18)], fill=(90, 78, 70))
    for i, r in enumerate([14, 18, 22]):
        d.ellipse([x + 190 + i * 10 - r, y + 26 + i * 18 - r,
                   x + 190 + i * 10 + r, y + 26 + i * 18 + r],
                  fill=(150, 140, 130))
    d.text((x + 12, y + 10), "GAZA", font=fnt(SANS_B, 20), fill=(90, 40, 20))


def pic_chess(d, x, y, w, h):
    """Chessboard with a king and a queen facing off."""
    d.rectangle([x, y, x + w, y + h], fill=(238, 228, 205))
    sq = 17
    ox, oy = x + (w - 8 * sq) // 2, y + 7
    for r in range(8):
        for c in range(8):
            if (r + c) % 2:
                d.rectangle([ox + c * sq, oy + r * sq,
                             ox + (c + 1) * sq, oy + (r + 1) * sq],
                            fill=(60, 60, 60))
    # White king on a light square, black queen on a dark one.
    kx, ky = ox + 2 * sq + sq // 2, oy + 6 * sq + sq // 2
    d.ellipse([kx - 8, ky - 8, kx + 8, ky + 8], fill=(250, 250, 250),
              outline=INK, width=2)
    d.line([(kx, ky - 13), (kx, ky - 3)], fill=INK, width=2)
    d.line([(kx - 5, ky - 8), (kx + 5, ky - 8)], fill=INK, width=2)
    qx, qy = ox + 5 * sq + sq // 2, oy + 6 * sq + sq // 2
    d.ellipse([qx - 8, qy - 8, qx + 8, qy + 8], fill=(30, 30, 30))
    d.polygon([(qx - 8, qy - 8), (qx - 4, qy - 15), (qx, qy - 8),
               (qx + 4, qy - 15), (qx + 8, qy - 8)], fill=(30, 30, 30))


def pic_storm(d, x, y, w, h):
    """Storm clouds, rain and a sagging parade balloon."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 208, 222))
    for cx, cy, r in [(70, 58, 38), (130, 52, 44), (200, 60, 38),
                      (260, 54, 32)]:
        d.ellipse([x + cx - r, y + cy - r // 2, x + cx + r, y + cy + r // 2],
                  fill=(90, 100, 116))
    # Sagging balloon, drooping low over the street.
    d.ellipse([x + 90, y + 66, x + 230, y + 128], fill=(176, 30, 30))
    d.ellipse([x + 120, y + 74, x + 165, y + 108], fill=(210, 80, 80))
    d.line([(x + 160, y + 128), (x + 150, y + h - 8)], fill=(90, 80, 70),
           width=3)
    d.line([(x + 190, y + 128), (x + 205, y + h - 8)], fill=(90, 80, 70),
           width=3)
    for rx in range(20, w, 34):
        d.line([(x + rx, y + 132), (x + rx - 6, y + 146)],
               fill=(70, 90, 120), width=3)
    d.text((x + 12, y + 10), "NEW YORK", font=fnt(SANS_B, 20), fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36
    R = W - M

    # Masthead: shrink until it fits the page width.
    size = 62
    while (d.textlength("THE WORLD IN ONE DAY", font=fnt(SERIF_B, size))
           > R - M):
        size -= 1
    d.text((M, 22), "THE WORLD IN ONE DAY", font=fnt(SERIF_B, size), fill=INK)
    hline(d, M, R, 104, width=4)
    d.text((M, 114), "FRIDAY 27 NOVEMBER 2026  ·  THE DAY'S NEWS IN ONE IMAGE",
           font=fnt(SANS_B, 21), fill=RED)
    hline(d, M, R, 148, width=2)

    # Lead story: Kuwait drone strike.
    y = 168
    d.text((M, y), "KUWAIT", font=fnt(SANS_B, 22), fill=RED)
    y = para(d, M, y + 30,
             "Drone strike kills two Italians; Iran denies role",
             fnt(SERIF_B, 40), 500, leading=48)
    y = para(d, M, y + 10,
             "Two Italian workers were killed in a drone strike in "
             "Kuwait, officials said. Iran denied responsibility "
             "for the attack, which drew condemnation across the "
             "region and raised fears of a wider escalation.",
             fnt(SERIF, 22), 500, leading=29)
    pic_kuwait(d, 560, 168, R - 560, 300)

    # Section divider.
    hline(d, M, R, 496, width=3)
    d.text((M, 508), "AROUND THE WORLD", font=fnt(SANS_B, 22), fill=BLUE)

    # Three picture stories.
    cards = [
        (pic_gaza, "Gaza",
         "Israel kills 10 in Gaza; Hamas weighs its response",
         "Reuters: ten people were killed in Gaza as Hamas "
         "considered its answer to the latest strikes."),
        (pic_chess, "Chess",
         "Gukesh and Sindarov draw a marathon Game 3",
         "Nothing separates the two in the World Championship "
         "match after three games in a long, tense draw."),
        (pic_storm, "Thanksgiving",
         "Storm postpones the 100th Macy's parade",
         "New York delayed the centenary parade for the first "
         "time as a storm cut power to half a million homes."),
    ]
    cw = (R - M - 2 * 24) // 3
    for i, (pic, kick, head, body) in enumerate(cards):
        cx = M + i * (cw + 24)
        pic(d, cx, 544, cw, 150)
        yy = para(d, cx, 706, head, fnt(SERIF_B, 21), cw, leading=26)
        para(d, cx, yy + 4, body, fnt(SERIF, 16), cw, leading=21)

    # Briefs strip.
    hline(d, M, R, 872, width=3)
    d.text((M, 884), "ALSO ON 27 NOVEMBER", font=fnt(SANS_B, 22), fill=BLUE)
    briefs = [
        ("BRITAIN", "Net migration falls to its lowest since 1997."),
        ("EGYPT", "Fuel tanker fire near Cairo kills at least 31."),
        ("EUROPE", "Leaders debate a €1.6 trillion EU budget."),
        ("WASHINGTON", "Trump seeks a probe of 'fake' GDP figures."),
        ("FRANCE", "Depardieu to stand trial over alleged 2018 rape."),
        ("BANGKOK", "Massive refinery fire leaves several injured."),
    ]
    bw = (R - M - 24) // 2
    for i, (kick, text) in enumerate(briefs):
        bx = M + (i % 2) * (bw + 24)
        by = 918 + (i // 2) * 30
        d.text((bx, by), kick + " — ", font=fnt(SANS_B, 15), fill=RED)
        kw = d.textlength(kick + " — ", font=fnt(SANS_B, 15))
        d.text((bx + kw, by), text, font=fnt(SANS, 15), fill=INK)

    d.text((M, 1002), "All stories first reported on Friday 27 November 2026.",
           font=fnt(SANS, 14), fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
