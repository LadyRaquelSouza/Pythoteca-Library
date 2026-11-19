#!/usr/bin/env python3
"""Validate importable v2 modules separately from legacy catalog."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"modules"
def require(ok,msg):
    if not ok: raise ValueError(msg)
def field(o,k,n,empty=False):
    v=o.get(k)
    require(isinstance(v,str) and len(v.encode("utf-16-le"))//2<=n and (empty or v.strip()),"Invalid "+k)
    return v
def ident(v):
    return re.fullmatch(r"(?:0[1-9]|[1-9][0-9]{1,3})",v)
def validate(p):
    raw=p.read_bytes()
    require(0<len(raw)<=1024*1024,"Size")
    l=json.loads(raw.decode("utf-8"))
    require(type(l.get("schema_version")) is int and l["schema_version"]==2,"Version")
    require(l.get("discipline") in {"python","portugol","java","arquitetura","sistemas_operacionais","ti","modelagem_dados"},"Discipline")
    require(field(l,"id",8)==p.stem and l["id"].startswith("aula") and ident(l["id"][4:]),"ID")
    for k,n in [("title",180),("subtitle",160),("objectives",24000),("source",12000)]:field(l,k,n)
    require(isinstance(l.get("chapters"),list) and 1<=len(l["chapters"])<=80,"Chapters")
    for c in l["chapters"]:
        field(c,"title",180);field(c,"text",48000);field(c,"example",24000,True)
    require(isinstance(l.get("exercises"),list) and 1<=len(l["exercises"])<=250,"Exercises")
    ids=set()
    for e in l["exercises"]:
        i=field(e,"id",4);require(ident(i) and i not in ids,"Exercise ID");ids.add(i)
        for k,n in [("title",180),("group",160),("prompt",24000),("explanation",24000)]:field(e,k,n)
        for k,n in [("hint",12000),("starter",24000),("solution",24000)]:field(e,k,n,True)
        mode=e.get("mode")
        require(mode in {"quiz","text","code"} and (mode!="code" or l["discipline"]=="python"),"Mode")
        require("expected" in e and (e["expected"] is None or (mode=="code" and isinstance(e["expected"],str) and len(e["expected"])<=32000)),"Expected")
        if mode=="quiz":
            options=e.get("options")
            require(isinstance(options,list) and 2<=len(options)<=6,"Options")
            choices=set();labels=set()
            for o in options:
                require(set(o)=={"id","text"},"Option keys")
                oid=field(o,"id",1);label=field(o,"text",3000).strip()
                require(oid in "abcdef" and oid not in choices and label not in labels,"Option")
                choices.add(oid);labels.add(label)
            require(e.get("answer") in choices and e["starter"]==e["solution"]=="","Quiz answer")
        else: require("options" not in e and "answer" not in e,"Unexpected options")
        if "sample_inputs" in e:
            require(mode=="code" and isinstance(e["sample_inputs"],list) and len(e["sample_inputs"])<=50 and all(isinstance(v,str) and len(v)<=2000 and "\n" not in v and "\r" not in v for v in e["sample_inputs"]),"Sample inputs")
    print(f"{p.name}: {len(l['chapters'])} chapters, {len(ids)} exercises")
if __name__=="__main__":
    files=sorted(ROOT.glob("aula*.json"))
    require(bool(files),"No modules")
    legacy={p.stem for p in (ROOT.parent/"catalog").glob("aula*.json")}
    require(not (legacy & {p.stem for p in files}),"Legacy ID collision")
    for p in files:validate(p)
