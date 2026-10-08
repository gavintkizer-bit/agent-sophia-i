import base64,re
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
t=open("board_template.html").read()
def uri(p,mime="image/png"): return "data:%s;base64,%s"%(mime,base64.b64encode(open(p,"rb").read()).decode())
css="/* Gavin's alphabet, one class per letter (each image appears once) */\n"+"".join(".g%02d { --g: url(%s); }\n"%(n,uri("glyphs/g%02d.png"%n)) for n in range(1,34))
t=t.replace("{{GLYPH_CSS}}",css)
t=t.replace("{{BANNER}}",uri("banner.jpg","image/jpeg"))
fr=lambda ns:"".join('<span class="glyph g%02d"></span>'%n for n in ns)
t=t.replace("{{FRIEZE}}",fr([1,4,8,10,17,18,22,27,29,31,33])).replace("{{FRIEZE2}}",fr([2,5,9,12,19,24,28,30,32]))
left=re.findall(r"\{\{\w+\}\}",t); assert not left, left
open(__import__("pathlib").Path(__file__).resolve().parents[2] / "workspace" / "crew_board.html","w").write(t); print(len(t)//1024,"KB")
