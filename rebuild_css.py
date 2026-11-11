#!/usr/bin/env python3
"""Kompilasi ulang CSS Tailwind ke dalam index.html (jalankan setiap menambah kelas Tailwind baru).
Perlu Node: npm i tailwindcss@3 lalu python3 rebuild_css.py"""
import subprocess, re, tempfile, os
here = os.path.dirname(os.path.abspath(__file__)); f = os.path.join(here, 'index.html')
cfg = os.path.join(tempfile.mkdtemp(), 'tw.config.js'); inp = cfg.replace('tw.config.js', 'in.css'); out = cfg.replace('tw.config.js', 'out.css')
open(cfg, 'w').write("module.exports={content:[%r],theme:{extend:{fontFamily:{sans:['Inter','sans-serif']},colors:{brand:{50:'#fff7ed',100:'#ffedd5',200:'#fed7aa',400:'#fb923c',500:'#f97316',600:'#ea580c',700:'#c2410c',800:'#9a3412',warning:'#eab308'}}}}}" % f)
open(inp, 'w').write('@tailwind base;@tailwind components;@tailwind utilities;')
subprocess.run(['npx', 'tailwindcss', '-c', cfg, '-i', inp, '-o', out, '--minify'], check=True)
css = open(out).read(); h = open(f, encoding='utf-8').read()
h = re.sub(r'/\*TW-START\*/.*?/\*TW-END\*/', lambda m: '/*TW-START*/\n' + css + '\n/*TW-END*/', h, flags=re.S)
open(f, 'w', encoding='utf-8').write(h); print('CSS', len(css), 'bytes')
