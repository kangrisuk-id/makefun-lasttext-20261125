#!/usr/bin/env python3
"""Render the gallery cards for the README: the winning text as a phone
chat card at 1% battery, and the finalists card. Build-time only — the
entry itself (main.py) is pure standard library."""

from PIL import Image, ImageDraw, ImageFont

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

BG = (16, 18, 24)
PANEL = (26, 29, 38)
BUBBLE = (38, 84, 124)
WHITE = (240, 242, 245)
MUTED = (150, 158, 170)
RED = (235, 70, 60)
GOLD = (240, 190, 60)


def font(size, bold=False):
    return ImageFont.truetype(SANS_BOLD if bold else SANS, size)


def wrap(draw, text, fnt, width):
    words, lines, current = text.split(), [], ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def battery(draw, x, y, pct_text="1%"):
    draw.rounded_rectangle([x, y, x + 54, y + 26], radius=6, outline=MUTED, width=3)
    draw.rectangle([x + 56, y + 8, x + 62, y + 18], fill=MUTED)
    draw.rectangle([x + 4, y + 4, x + 8, y + 22], fill=RED)
    draw.text((x + 70, y - 2), pct_text, font=font(26, bold=True), fill=RED)


def header(draw, w, title):
    draw.text((36, 30), title, font=font(30, bold=True), fill=WHITE)
    battery(draw, w - 170, 32)


def bubble(draw, x, y, w, text, label=None):
    fnt = font(30)
    lines = wrap(draw, text, fnt, w - 48)
    h = len(lines) * 40 + 36
    if label:
        draw.text((x + 4, y), label, font=font(22, bold=True), fill=GOLD)
        y += 34
        h += 34
    draw.rounded_rectangle([x, y, x + w, y + h - (34 if label else 0)],
                           radius=18, fill=BUBBLE)
    ty = y + 18
    for line in lines:
        draw.text((x + 24, ty), line, font=fnt, fill=WHITE)
        ty += 40
    return y + h


def winner_card():
    w, h = 900, 430
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    header(draw, w, "THE LAST TEXT — WINNER")
    bubble(draw, 36, 110, w - 72,
           "1%. I used it to type this instead of saving myself. "
           "That's how much I\u2014")
    draw.text((36, h - 52),
              "71 characters · scored 49/50 · won the final on brevity",
              font=font(22), fill=MUTED)
    img.save("card-winner.png")


def finalists_card():
    w, h = 900, 745
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    header(draw, w, "THE FINALISTS")
    y = 100
    entries = [
        ("RUNNER-UP · 49/50",
         "I'm at 1%. Your ex texted. It just says 'hey.' "
         "I'm taking what it means to my grave."),
        ("SEMIFINALIST · 48/50",
         "Dying at 1%, and my final text has no typo. Four years of "
         "autocorrect and I finally send one clean\u2014oh duck."),
        ("SEMIFINALIST · 47/50",
         "Before the screen goes: I never liked the case. "
         "There. I said it. I die free."),
    ]
    for label, text in entries:
        y = bubble(draw, 36, y, w - 72, text, label=label) + 26
    img.save("card-finalists.png")


if __name__ == "__main__":
    winner_card()
    finalists_card()
    print("cards written")
