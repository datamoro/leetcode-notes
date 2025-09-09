#!/usr/bin/env python3
import os, sys, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dirify(name: str) -> str:
    import re
    n = name.lower().replace("&","and").replace("/","_").replace(" ","_")
    n = re.sub(r"[^a-z0-9_]", "", n)
    n = re.sub(r"_+", "_", n).strip("_")
    return n

def slugify(title: str) -> str:
    import re
    t = title.lower()
    t = re.sub(r"\(.*?\)", "", t)
    t = re.sub(r"[^a-z0-9]+", "_", t)
    t = re.sub(r"_+", "_", t).strip("_")
    return t

def main():
    if len(sys.argv) < 4:
        print("Usage: add_problem.py <track: sql|dsa> <pattern> <problem_title>")
        sys.exit(1)
    track = sys.argv[1].lower()
    pattern = dirify(sys.argv[2])
    title = " ".join(sys.argv[3:])
    slug = slugify(title)

    track_dir = "sql" if track=="sql" else "dsa"
    base = os.path.join(ROOT, track_dir, pattern, slug)
    os.makedirs(base, exist_ok=True)

    # choose templates
    tmpl_sql = os.path.join(ROOT, "TEMPLATE_SQL.sql")
    tmpl_py = os.path.join(ROOT, "TEMPLATE_PY.py")
    tmpl_md = os.path.join(ROOT, "TEMPLATE_README.md")

    if track == "sql":
        shutil.copyfile(tmpl_sql, os.path.join(base, "solution.sql"))
    else:
        shutil.copyfile(tmpl_py, os.path.join(base, "solution.py"))
    shutil.copyfile(tmpl_md, os.path.join(base, "README.md"))
    print(f"Created: {base}")

if __name__ == "__main__":
    main()
