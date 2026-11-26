import openpyxl,json,collections,re
n=lambda s:re.sub(r'\W+','',str(s or '').lower())
ws=openpyxl.load_workbook('data/raw/verified_emissions_2025.xlsx',read_only=True)['data']
rows=list(ws.iter_rows(values_only=True)); hi=[i for i,r in enumerate(rows) if r and r[0]=='REGISTRY_CODE'][0]
h=rows[hi]; V=[dict(zip(h,r)) for r in rows[hi+1:] if r and r[0] in('IT','SI','HR')]
wo=openpyxl.load_workbook('data/raw/operators.xlsx',read_only=True)['data']
orows=list(wo.iter_rows(values_only=True)); oi=[i for i,r in enumerate(orows) if r and r[0]=='Account Holder Name'][0]
oh=list(orows[oi]); O=[dict(zip(oh,r)) for r in orows[oi+1:] if r and r[3] in('IT','SI','HR')]
for o in O: o['Permit Expiry/Revocation Date ']=o.get('Permit Expiry/Revocation Date ')
byp=collections.defaultdict(list)
for o in O: byp[(o['MS Registry'],n(o['Permit ID']))].append(o)
def num(x): return x if isinstance(x,(int,float)) else None
SEC=[('pig iron|steel|ferrous','Steel & metals',.45,.149),('aluminium','Steel & metals',.6,.149),('ammonia','Ammonia / fertiliser',.9,.105),
('refining','Refining',.5,.149),('cement','Cement',.1,.149),('lime|gypsum','Lime & gypsum',.3,.149),('glass','Glass',.6,.149),('ceramics|mineral wool','Ceramics & wool',.65,.149),
('paper|pulp','Paper & pulp',.8,.149),('combustion','Power & heat',.15,.149)]
def sec(a):
    for k,l,s,f in SEC:
        if re.search(k,a.lower()): return l,s,f
    return 'Other',.3,.149
KEY=re.compile(r'rijeka|plomin|labin|pula|\bistra\b|koroma|trieste|gorizia|monfalcone|udine|pordenone|servola|osoppo|nova gorica|koper|anhovo|ljubljana',re.I)
out=[];seen=set()
for x in V:
    t=x['ACCOUNT_TYPE'] or ''
    if x['MAIN_ACTIVITY_TYPE_CODE']==10 or t!='OPERATOR HOLDING ACCOUNT': continue
    c=x['REGISTRY_CODE']; cand=byp.get((c,n(x['PERMIT_IDENTIFIER'])))
    if not cand: continue
    nm=n(x['IDENTIFIER_IN_REG'])
    o=max(cand,key=lambda o:len(set(n(o['Installation Name']))&set(nm))) if len(cand)>1 else cand[0]
    if o['Permit Expiry/Revocation Date ']!='ACTIVE': continue
    e=num(x['VERIFIED_EMISSIONS_2025'])
    if not e: continue
    pc=str(o['Contact PCode'] or '');name=o['Installation Name'] or x['IDENTIFIER_IN_REG']
    hint=bool(KEY.search(f"{name} {o['Contact City']}"))
    if c=='SI': z='core'
    elif c=='HR': z='core' if (pc[:2] in('51','52','53','47') or hint) else 'ring'
    else: z='core' if (pc[:2] in('33','34') or hint) else ('ring' if pc[:2] in('30','31','35','45','48') else None)
    if not z: continue
    uid=(c,name,o['Account Holder Name'],round(e))
    if uid in seen: continue
    seen.add(uid)
    l,s,f=sec(o['Activity Type'])
    out.append(dict(c=c,z=z,n=name,h=o['Account Holder Name'],city=o['Contact City'],a=o['Activity Type'],s=l,sh=s,f=f,e=e,e24=num(x['VERIFIED_EMISSIONS_2024']),e23=num(x['VERIFIED_EMISSIONS_2023'])))
out.sort(key=lambda r:-r['e'])
print(len(out),collections.Counter(r['z'] for r in out))
tot=collections.Counter()
for r in out: tot[r['z']]+=r['e']*r['sh']*r['f']
print({k:round(v/1e3,1) for k,v in tot.items()},'kt H2 (core/ring)')
air=json.load(open('data/airports.json'))
json.dump(out,open('data/installations.json','w'),ensure_ascii=False,indent=0)
for src,dst in [('fuel','adriatic-fuel.html'),('hydrogen','hydrogen.html')]:
    t=open(f'scripts/template_{src}.html').read().replace('__DATA__',json.dumps(out,ensure_ascii=False)).replace('__AIR__',json.dumps(air))
    open(dst,'w').write(t)
