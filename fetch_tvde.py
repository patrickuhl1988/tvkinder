#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Holt einen Sendertag von tv.de und gibt die Sendungen als Tupel zurück."""
import html, re, subprocess, sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ENTRY = re.compile(
    r'tw-bg-secondary[^>]*>(\d{2}:\d{2})</span>.*?'
    r'<h3[^>]*>\s*(.*?)</h3>.*?'
    r'tw-text-body-2">(.*?)</span>.*?'
    r'tw-line-clamp-3">(.*?)</p>', re.S)


def hole(slug, datum):
    url = f"https://tv.de/sender/{slug}/{datum}/"
    r = subprocess.run(["curl", "-s", "-m", "30", "-A", UA, url],
                       capture_output=True, text=True)
    h = r.stdout
    out = []
    for zeit, titel, kat, beschr in ENTRY.findall(h):
        t = re.sub(r"<span[^>]*>", "|", titel)
        t = html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
        teile = [x.strip(" :") for x in t.split("|")]
        haupt = teile[0]
        sub = teile[1] if len(teile) > 1 else ""
        out.append(dict(zeit=zeit, titel=haupt, sub=sub,
                        kat=html.unescape(re.sub(r"<[^>]+>", "", kat)).strip(),
                        text=html.unescape(re.sub(r"<[^>]+>", "", beschr)).strip()))
    # Doppelte (mobile/desktop) entfernen
    ein, seen = [], set()
    for e in out:
        k = (e["zeit"], e["titel"])
        if k in seen:
            continue
        seen.add(k)
        ein.append(e)
    ein.sort(key=lambda e: e["zeit"])
    return ein


if __name__ == "__main__":
    for e in hole(sys.argv[1], sys.argv[2])[:6]:
        print(e["zeit"], "|", e["titel"], "|", e["sub"][:28], "|", e["kat"], "|", e["text"][:50])
