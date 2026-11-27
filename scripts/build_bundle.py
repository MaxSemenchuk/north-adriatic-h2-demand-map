"""Build claude-esaf/ALL_IN_ONE.md: instructions, dictionary and every CSV in one file."""
import pathlib
d=pathlib.Path(__file__).resolve().parent.parent/'claude-esaf'
B='https://raw.githubusercontent.com/MaxSemenchuk/north-adriatic-h2-demand-map/main/claude-esaf/'
out=['# Europe e-SAF map: complete data pack (one file)\n\nThis single file contains the analyst instructions, the data dictionary and every data table. Nothing else needs to be opened. Sections are marked `=== FILE: name ===`.\n']
for n in ['INSTRUCTIONS.md','DATA_DICTIONARY.md']+sorted(p.name for p in (d/'data').glob('*.csv')):
    p=d/n if n.endswith('.md') else d/'data'/n
    out.append(f'\n\n=== FILE: {n} ({B}{"" if n.endswith(".md") else "data/"}{n}) ===\n\n'+p.read_text(encoding='utf-8').strip()+f'\n\n=== END FILE: {n} ===')
(d/'ALL_IN_ONE.md').write_text(''.join(out),encoding='utf-8')
print(len(''.join(out))//1024,'KB')
