from pathlib import Path
import re,html,shutil,json,fitz
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'docs'; UP=ROOT.parent/'upload'
subjects={59:'Miễn thuế thu nhập từ hoạt động khởi nghiệp sáng tạo',62:'Nghiên cứu, chuyển giao công nghệ và sở hữu trí tuệ',63:'Trung tâm nghiên cứu đạt chuẩn quốc tế',64:'Chi phí ươm tạo dự án khởi nghiệp sáng tạo',65:'Hạ tầng, trung tâm đổi mới sáng tạo và hỗ trợ khởi nghiệp sáng tạo'}
e=html.escape

def shell(title,body,n=None):
 nav='<a href="/">Tổng quan</a>'+''.join(f'<a class="{"active" if k==n else ""}" href="/nq-{k}">NQ {k}</a>' for k in subjects)
 return f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} · Tra cứu chính sách</title><link rel="stylesheet" href="/style.css"><link rel="icon" href="/favicon.svg"><script src="/view.js" defer></script></head><body><header><a class="brand" href="/">CHÍNH SÁCH KHOA HỌC & ĐỔI MỚI SÁNG TẠO<span>Thành phố Hồ Chí Minh</span></a><nav>{nav}</nav></header>{body}<footer>Đối chiếu 5 PDF được cung cấp ngày 07/10/2026. Nội dung điều, khoản, điểm giữ theo văn bản gốc; xuống dòng được sắp lại để đọc trên màn hình.</footer></body></html>'

def norm(s):return re.sub(r'\s+',' ',s).strip()
def rich(s):
 s=e(norm(s))
 return re.sub(r'(?<!\w)(\d+(?:[.,]\d+)?(?:%|\s+(?:triệu đồng|tỷ đồng|ngày làm việc|tháng|năm)))(?!\w)',r'<mark>\1</mark>',s)

all_data={}
for n in subjects:
 pdf=next((p for p in UP.glob('*.pdf') if re.search(rf'(?:NQ |^){n}_2026',p.name)),D/f'NQ{n}_2026_goc.pdf')
 if pdf.resolve()!=(D/f'NQ{n}_2026_goc.pdf').resolve():shutil.copyfile(pdf,D/f'NQ{n}_2026_goc.pdf')
 # Read bold article headings to preserve full wrapped titles.
 titles=[]
 for pg in fitz.open(pdf):
  lines=[]
  for b in pg.get_text('dict')['blocks']:
   for l in b.get('lines',[]):
    spans=l['spans'];text=''.join(s['text'] for s in spans).strip()
    lines.append((text,all(s['flags']&16 for s in spans if s['text'].strip())))
  for i,(t,bold) in enumerate(lines):
   if re.match(r'^Điều \d+\.',t):
    full=t;j=i+1
    while j<len(lines) and lines[j][1] and not re.match(r'^(Điều |\d+[.)]|[a-zđ]\))',lines[j][0]):
     full+=' '+lines[j][0];j+=1
    titles.append(norm(full))
 text_path=ROOT/'sources'/f'NQ{n}.txt'
 pages=text_path.read_text().split('\f')
 entries=[];current=None;stopped=False;group='Nghị quyết';title_idx=0
 for page,txt in enumerate(pages,1):
  for raw in txt.splitlines():
   s=raw.strip()
   if not s or re.fullmatch(r'\d+',s):continue
   if re.match(r'^Điều \d+\.',s):
    if stopped and n!=63: continue
    if n==63 and stopped:group='Quy định kèm theo';stopped=False
    current={'number':int(re.match(r'^Điều (\d+)',s)[1]),'page':page,'group':group,'lines':[s]};entries.append(current);continue
   if s.startswith(('Nghị quyết này đã','Nơi nhận:')):
    current=None;stopped=True;continue
   if re.match(r'^Chương [IVX]+\b',s):current=None;continue
   if current is not None: current['lines'].append(s)
 expected={59:9,62:12,63:32,64:14,65:14}[n]
 assert len(entries)==expected,(n,len(entries))
 for i,a in enumerate(entries):
  title=titles[i];a['title']=title
  joined=norm(' '.join(a['lines']))
  assert joined.startswith(title),(n,title,joined[:200])
  # Remove heading lines only, then join continuation lines into paragraphs.
  remaining=a['lines'][:];consumed=''
  while remaining and len(norm(consumed))<len(title):consumed+=' '+remaining.pop(0)
  assert norm(consumed)==title,(n,title,consumed)
  paras=[]
  for s in remaining:
   if re.match(r'^(\d+\.|[a-zđ]\)|[-–])\s',s) or not paras:paras.append(s)
   else:paras[-1]+=' '+s
  a['paragraphs']=paras;a['id']=('qd' if a['group']=='Quy định kèm theo' else 'nq')+'-'+str(a['number'])
  assert not any('Nơi nhận:' in x or 'CHỦ TỊCH' in x for x in paras)
 all_data[n]=entries
 old=(D/f'nq-{n}.html').read_text()
 forms=''
 if n in (62,65):
  table=(ROOT/'sources'/f'forms-{n}.html').read_text()
  for row in re.findall(r'<tr>(.*?)</tr>',table,re.S)[1:]:
   cells=re.findall(r'<td>(.*?)</td>',row,re.S)
   forms+=f'<article class="form-card"><h3>{cells[0]}</h3><div class="form-actions">{cells[2]}{cells[3]}{cells[4]}</div></article>'
  forms=f'<section id="mau" class="forms"><h2>Mẫu trong phụ lục văn bản</h2><div class="form-grid">{forms}</div></section>'
 toc='';cards='';last_group=''
 for a in entries:
  if last_group!=a['group']:
   toc+=f'<h3>{a["group"]}</h3>';cards+=f'<h2 class="group-title">{a["group"]}</h2>';last_group=a['group']
  label=re.sub(r'^Điều \d+\.\s*','',a['title'])
  toc+=f'<a href="#{a["id"]}"><span>{a["number"]:02}</span>{e(label)}</a>'
  blocks='';clause=None
  for p in a['paragraphs']:
   m=re.match(r'^(\d+\.)\s*(.*)',p)
   pt=re.match(r'^([a-zđ]\))\s*(.*)',p)
   if m:
    if clause is not None:blocks+='</div></div>'
    blocks+=f'<div class="clause"><span class="number">{m[1]}</span><div class="clause-content"><p>{rich(m[2])}</p>';clause=True
   elif pt:blocks+=f'<div class="point"><span>{pt[1]}</span><p>{rich(pt[2])}</p></div>'
   else:blocks+=f'<p class="intro">{rich(p)}</p>'
  if clause is not None:blocks+='</div></div>'
  cards+=f'<article class="article" id="{a["id"]}"><details open class="article-detail"><summary><span class="article-no">Điều {a["number"]}</span><h3>{e(label)}</h3><span class="chevron">⌄</span></summary><div class="article-body">{blocks}<div class="source-line"><span>Nguyên văn · {a["group"]}</span><a href="/NQ{n}_2026_goc.pdf#page={a["page"]}" target="_blank" rel="noopener">Đối chiếu PDF · trang {a["page"]}</a></div><details class="blank-fields"><summary>Các cột bổ sung</summary><table><thead><tr><th>Xử lý khi thiếu — có căn cứ</th><th>Giấy tờ riêng — có căn cứ</th></tr></thead><tbody><tr><td></td><td></td></tr></tbody></table></details></div></details></article>'
 if forms:toc+='<a href="#mau"><span>▤</span>Mẫu phụ lục</a>'
 body=f'<main><section class="page-heading"><div><p class="eyebrow">NGHỊ QUYẾT {n}/2026/NQ-HĐND</p><h1>{subjects[n]}</h1><p class="meta">HĐND Thành phố Hồ Chí Minh · 22/09/2026 <span>· {len(entries)} điều'+(' (4 điều nghị quyết + 28 điều quy định)' if n==63 else '')+'</span></p></div><a class="button" target="_blank" rel="noopener" href="/NQ'+str(n)+'_2026_goc.pdf">Mở PDF gốc</a></section><div class="layout"><aside><div class="toc-head">Mục lục điều</div><div class="toc">'+toc+'</div></aside><div class="content"><div class="toolbar"><span>Điều · Khoản · Điểm</span><div><button data-action="expand">Mở tất cả</button><button data-action="collapse">Thu gọn tất cả</button></div></div>'+cards+forms+'</div></div></main>'
 (D/f'nq-{n}.html').write_text(shell(subjects[n],body,n))
(D/'articles.json').write_text(json.dumps(all_data,ensure_ascii=False,indent=2))
# Keep existing audience overview as verbatim clause cards rather than a wide table.
home='<main><section class="page-heading"><div><p class="eyebrow">05 NGHỊ QUYẾT · HĐND TP. HỒ CHÍ MINH</p><h1>Tra cứu chính sách</h1></div><a class="button secondary" href="/Tat_ca_mau_Word.zip" download>Tải Word của 14 mẫu phụ lục</a></section><div class="overview-grid">'
for n,entries in all_data.items():
 audience=next(a for a in entries if a['number']==2 and (n!=63 or a['group']=='Quy định kèm theo'))
 home+=f'<article class="overview-card"><div class="overview-top"><span class="eyebrow">NQ {n}/2026</span><span class="count">{len(entries)} điều</span></div><h2><a href="/nq-{n}">{subjects[n]}</a></h2><details><summary>Đối tượng áp dụng · nguyên văn Điều 2</summary>'+''.join(f'<p>{rich(p)}</p>' for p in audience['paragraphs'])+f'<a href="/NQ{n}_2026_goc.pdf#page={audience["page"]}">Đối chiếu PDF · trang {audience["page"]}</a></details><a class="button" href="/nq-{n}">Xem các điều</a></article>'
home+='</div></main>'
(D/'index.html').write_text(shell('Tra cứu chính sách',home))
print('Validated article counts:',{n:len(a) for n,a in all_data.items()})

# GitHub Pages project sites use /repository-name/ as their base URL.
# Keep all website references relative so that repository names can change.
for page in D.glob('*.html'):
 def relative_link(match):
  attr,url=match.groups()
  if url.startswith('/') and not url.startswith('//'):
   url=url[1:] or 'index.html'
   if re.fullmatch(r'nq-\d+',url):url+='.html'
  return attr+'="'+url+'"'
 page.write_text(re.sub(r'(href|src)="([^"]*)"',relative_link,page.read_text()))
