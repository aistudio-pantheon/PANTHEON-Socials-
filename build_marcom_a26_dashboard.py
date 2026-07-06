#!/usr/bin/env python3
"""Build the Pantheon Marcom Workplace A26 operations dashboard.

Data pulled live from monday.com (workspace 2928343) via MCP on 6 Jul 2026.
Aggregates per board: group x status counts, subitem counts. Regenerate by
re-pulling board_insights per board and updating BOARDS below.
"""
import html as H

PULL_DATE = "6 July 2026"
PULL_DATE_SHORT = "Jul 6"
WORKSPACE_NAME = "Pantheon Marcom Workplace A26"
WORKSPACE_URL = "https://pered-squad.monday.com/workspaces/2928343"

# monday.com status label colors (verbatim from board settings)
STATUS_COLORS = {
    "Done": "#00c875", "Completed": "#00c875",
    "Working on it": "#fdab3d", "In Progress": "#ff6d3b",
    "Stuck": "#df2f4a",
    "Planned": "#c4c4c4", "On hold": "#c4c4c4", "Confirmed": "#c4c4c4", "On Going": "#c4c4c4",
    "Pending Approval": "#007eb5", "Waiting for Confirmation": "#007eb5", "Revision 1": "#007eb5",
    "Revision 2": "#9d50dd", "Priority": "#9d50dd",
    "Waiting for Approval": "#579bfc", "Waiting For Approval": "#579bfc",
    "Not Comming": "#037f4c",
    "No status": "#3a4150",
}
DONE_LABELS = {"Done", "Completed"}
BLANK = "No status"

# board: (emoji, name, owner_line, board_id, total, groups=[(gname, {label: count})], sub=(total, done) or None)
UNITS = [
    ("📁 Unit 1 — Brand & Content", [
        ("📱", "Social Media Content Calendar", "Owner: Rashid · Support: Elias", 5027783015, [
            ("PANTHEON June Calendar", {"Done": 61, "Planned": 8, "Working on it": 1}),
            ("Pantheon Linkedin April", {"Done": 25}),
            ("Pantheon Instagram April - May", {"Done": 165}),
            ("Pantheon General Social", {"Done": 7}),
            ("Other", {"Done": 2, "Pending Approval": 1}),
            ("Google Business Profile", {"Done": 9}),
            ("PANTHEON - AI STUDIO", {"Done": 26}),
        ], (4, 0)),
        ("🎨", "Creative Brief & Production Tracker", "Owner: Magalie · Support: Elias", 5027783014, [
            ("All briefs", {"Done": 336, "Working on it": 2, "Revision 2": 2, "On Going": 2}),
        ], (16, 7)),
        ("📄", "Brand Collateral Library", "Owner: Magalie · Support: Fayiz / Rinas / Lipin / Jishnu", 5027783017, [
            ("Collateral", {"Done": 2}),
        ], None),
        ("📰", "PR & Media Relations", "Owner: Elias · Support: Sehar", 5027783018, [
            ("Office Launch — Influencer List", {"Not Comming": 11, "Waiting for Confirmation": 9, "Confirmed": 7, "Done": 2, "Stuck": 2}),
            ("Office Launch — Media List", {"Confirmed": 18}),
            ("New Group", {"Done": 5, "Working on it": 3}),
        ], None),
        ("🎬", "Video & Photography Production", "Owner: Magalie", 5027783016, [
            ("Production", {"Done": 116, "Revision 1": 2, "Waiting for Approval": 1, BLANK: 6}),
        ], None),
    ]),
    ("📁 Unit 2 — Engagement & Partnerships", [
        ("🤝", "Broker Activations & Engagement", "Owner: Sehar", 5027783019, [
            ("Brokers Pull Initiatives", {"Done": 20, BLANK: 1}),
            ("May 2026", {"Done": 4}),
        ], None),
        ("🏘️", "Community & Stakeholder Outreach", "Owner: Laxman · Support: Akhil", 5027783023, [
            ("General", {BLANK: 1}),
        ], None),
        ("📇", "Vendor & Agency Registry", "Owner: Anees · Support: Sehar", 5027783022, [
            ("Vendors", {"Done": 15}),
            ("Vendor & Purchase Orders Details", {"Done": 22, "Working on it": 2}),
        ], None),
        ("🎪", "Event Activations", "Owner: Sehar · Support: Anees", 5027783021, [
            ("Pantheon Event Tasks", {"Done": 123, "On hold": 6, "In Progress": 2, "Waiting For Approval": 1, "Priority": 1}),
            ("General Tasks", {"Done": 55, "In Progress": 2, "On hold": 1}),
            ("Event Organization", {"Done": 124}),
        ], (1, 0)),
        ("🏛️", "Institutional & JV Outreach", "Owner: Lara / Abhishek / Elias", 5027783020, [], None),
    ]),
    ("📁 Unit 3 — Digital & Analytics", [
        ("🌐", "Website & SEO Tracker", "Owner: Laxman · Support: Akhil", 5027783025, [
            ("pantheon.ae", {"Done": 11}),
            ("On-Page SEO", {"Done": 14}),
            ("Off-Page SEO", {"Done": 8}),
        ], (13, 13)),
        ("📧", "CRM, Email & WhatsApp Campaigns", "Owner: Laxman · Support: Akhil", 5027783026, [
            ("Lead Management (Scrapping / Sorting / Nurturing)", {"Completed": 22, "In Progress": 1}),
            ("WhatsApp Campaign — New Project Offers", {"Completed": 20}),
            ("Email Campaign — New Project Offers", {"Completed": 14}),
            ("Zoho Forms", {"Completed": 1}),
        ], (1, 0)),
        ("📈", "Marketing Dashboards & KPIs", "Owner: Rohit · Support: Akhil", 5027783027, [
            ("Artist/Event Intelligence Dashboard (AI Tool)", {"Completed": 47}),
            ("PACS (AI Content Studio)", {"Completed": 44}),
            ("Data Research AI Tool", {"Completed": 14}),
            ("Founder/Brand Competitor Intelligence (AI Tool)", {"Completed": 11}),
            ("Data Scrapping Dashboard (AI Tool)", {"Completed": 4}),
            ("Lead Reports / Analytics", {"Completed": 3}),
        ], (1, 0)),
        ("📊", "Performance Marketing & Paid Media", "Owner: Laxman · Support: Akhil", 5027783024, [
            ("META Ads", {"Done": 36}),
            ("TikTok Ads", {"Done": 7}),
            ("Google Ads", {"Done": 6}),
        ], (10, 10)),
    ]),
    ("📁 KK Personal Brand", [
        ("🛡️", "KK Personal Brand Scorecard", "Owner: Elias", 5027783030, [], None),
        ("🎤", "KK Founder Content Pipeline", "Owner: Elias", 5027783029, [
            ("Founder Instagram June", {"Done": 39}),
            ("Founder Instagram April - May", {"Done": 41}),
        ], None),
        ("👔", "KK LinkedIn Content Tracker", "Owner: Elias · Rule: min 2 posts/week", 5027783028, [
            ("Backlog — Ideas & Drafts", {BLANK: 10}),
        ], None),
    ]),
    ("📁 Governance, Finance & Operations", [
        ("✅", "Sehar Approval Gate — Finance & Vendors", "Owner: Sehar · AED < 25k authority", 5027783035, [
            ("Pending Approval", {"Done": 1, "Working on it": 1, BLANK: 1}),
        ], (1, 0)),
        ("📅", "Meeting Cadence & Minutes", "Owner: Mohd Amir · Support: Rohit", 5027801080, [], None),
        ("📊", "Team KRAs & Performance", "Owner: Akhil & Elias", 5027783034, [], None),
        ("📋", "Marketing Master Plan", "Owner: Elias", 5027783033, [], None),
        ("🚩", "Chairman & COO Task Board", "Owner: Chairman & Akhil", 5027783032, [], None),
        ("💰", "Marketing Budget Tracker", "Owner: Akhil + Sehar (dual sign-off)", 5027783031, [
            ("Overheads & Misc", {BLANK: 1}),
        ], None),
    ]),
    ("📁 Make Noise — Broker Engagement Engine", [
        ("📊", "Make Noise — Master Dashboard", "Owner: Rohit", 5027783662, [], None),
        ("📢", "Layer 1 — Make Noise (BDM Activity Tracker)", "Owner: Elias", 5027783658, [
            ("Activities", {"Working on it": 1}),
        ], None),
        ("👁️", "Layer 2 — Make Noise Visible (Proof Events)", "Owner: Elias", 5027783659, [
            ("Activities", {"Done": 10}),
        ], None),
        ("🏆", "Layer 3 — Make Noise Enviable (Broker Tiers)", "Owner: Elias · Support: Sehar", 5027783660, [
            ("Activity", {BLANK: 1}),
        ], None),
        ("💎", "Layer 4 — Make Noise Profitable (Future)", "Owner: Elias", 5027783661, [
            ("Activity", {BLANK: 1}),
        ], None),
    ]),
]

PREV = {"date": "29 Jun", "items": 1469, "done": 1383, "pending": 64, "blank": 22, "sub_total": 47, "sub_done": 30}


def board_stats(groups):
    total = done = blank = 0
    labels = {}
    for _, counts in groups:
        for label, n in counts.items():
            total += n
            labels[label] = labels.get(label, 0) + n
            if label in DONE_LABELS:
                done += n
            elif label == BLANK:
                blank += n
    pending = total - done - blank
    return total, done, pending, blank, labels


def seg_bar(labels, total, height=8):
    """Battery bar: one segment per status, 2px surface gaps, done first."""
    if total == 0:
        return '<div class="bar empty"></div>'
    order = sorted(labels.items(), key=lambda kv: (kv[0] not in DONE_LABELS, kv[0] == BLANK, -kv[1]))
    segs = []
    for label, n in order:
        pct = n / total * 100
        segs.append(f'<span class="seg" title="{H.escape(label)}: {n}" '
                    f'style="width:{pct:.2f}%;background:{STATUS_COLORS.get(label, "#8a94a6")}"></span>')
    return f'<div class="bar">{"".join(segs)}</div>'


def chips(labels):
    out = []
    order = sorted(labels.items(), key=lambda kv: (kv[0] not in DONE_LABELS, kv[0] == BLANK, -kv[1]))
    for label, n in order:
        c = STATUS_COLORS.get(label, "#8a94a6")
        out.append(f'<span class="chip"><i style="background:{c}"></i>{H.escape(label)} <b>{n}</b></span>')
    return "".join(out)


def build():
    # grand totals
    G = {"items": 0, "done": 0, "pending": 0, "blank": 0, "sub_total": 0, "sub_done": 0, "boards": 0}
    unit_html = []
    for unit_name, boards in UNITS:
        cards = []
        u_total = u_done = 0
        for emoji, name, owner, bid, groups, sub in boards:
            G["boards"] += 1
            total, done, pending, blank, labels = board_stats(groups)
            u_total += total; u_done += done
            G["items"] += total; G["done"] += done; G["pending"] += pending; G["blank"] += blank
            if sub:
                G["sub_total"] += sub[0]; G["sub_done"] += sub[1]
            pct = round(done / total * 100) if total else 0
            url = f"https://pered-squad.monday.com/boards/{bid}"
            if total == 0:
                body = '<div class="empty-note">No items yet</div>'
            else:
                grows = []
                for gname, counts in groups:
                    g_total = sum(counts.values())
                    g_done = sum(n for l, n in counts.items() if l in DONE_LABELS)
                    grows.append(
                        f'<div class="grow"><span class="gname" title="{H.escape(gname)}">{H.escape(gname)}</span>'
                        f'{seg_bar(counts, g_total)}'
                        f'<span class="gcount">{g_done}/{g_total}</span></div>')
                body = (f'{seg_bar(labels, total)}'
                        f'<div class="chips">{chips(labels)}</div>'
                        f'<div class="groups">{"".join(grows)}</div>')
            sub_html = (f'<span class="subpill" title="Subitems">↳ {sub[1]}/{sub[0]} subitems</span>' if sub else "")
            cards.append(f"""
      <article class="card">
        <header>
          <div class="bname"><span class="bemoji">{emoji}</span>
            <div><a href="{url}" target="_blank" rel="noopener">{H.escape(name)}</a>
            <div class="owner">{H.escape(owner)}</div></div></div>
          <div class="bstat"><span class="pct">{pct}%</span><span class="count">{done}/{total}</span>{sub_html}</div>
        </header>
        {body}
      </article>""")
        u_pct = round(u_done / u_total * 100) if u_total else 0
        unit_html.append(f"""
    <section class="unit">
      <div class="unit-head"><h2>{H.escape(unit_name)}</h2>
        <span class="unit-meta">{len(boards)} boards · {u_total} items · {u_pct}% done</span></div>
      <div class="grid">{"".join(cards)}</div>
    </section>""")

    pct = round(G["done"] / G["items"] * 100, 1)
    d_items = G["items"] - PREV["items"]; d_done = G["done"] - PREV["done"]
    d_pending = G["pending"] - PREV["pending"]; d_blank = G["blank"] - PREV["blank"]

    def delta(v, invert=False):
        if v == 0:
            return '<span class="delta flat">— vs %s</span>' % PREV["date"]
        good = (v > 0) ^ invert
        sign = "+" if v > 0 else "−"
        return f'<span class="delta {"up" if good else "down"}">{sign}{abs(v)} vs {PREV["date"]}</span>'

    kpis = f"""
    <div class="kpis">
      <div class="kpi"><span class="klabel">Boards</span><span class="kval">{G["boards"]}</span><span class="delta flat">6 folders</span></div>
      <div class="kpi"><span class="klabel">Total items</span><span class="kval">{G["items"]:,}</span>{delta(d_items)}</div>
      <div class="kpi"><span class="klabel">Done</span><span class="kval done-ink">{G["done"]:,}</span>{delta(d_done)}</div>
      <div class="kpi"><span class="klabel">Pending</span><span class="kval pend-ink">{G["pending"]}</span>{delta(d_pending, invert=True)}</div>
      <div class="kpi"><span class="klabel">No status</span><span class="kval blank-ink">{G["blank"]}</span>{delta(d_blank, invert=True)}</div>
      <div class="kpi"><span class="klabel">Completion</span><span class="kval">{pct}%</span>
        <div class="kbar"><span style="width:{pct}%"></span></div></div>
      <div class="kpi"><span class="klabel">Subitems</span><span class="kval">{G["sub_done"]}/{G["sub_total"]}</span><span class="delta flat">done / total</span></div>
    </div>"""

    css = """
:root{--bg:#0e1117;--panel:#151a23;--panel2:#1a2029;--line:#242c39;--ink:#e8ecf3;--ink2:#9aa4b5;
--ink3:#5f6a7d;--gold:#d4af37;--green:#00c875;--amber:#fdab3d;--blank:#3a4150;--r:12px}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:28px 32px 60px}
a{color:inherit;text-decoration:none}a:hover{color:var(--gold)}
.top{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;flex-wrap:wrap;margin-bottom:22px}
h1{font-size:22px;font-weight:700;letter-spacing:.2px}
.sub{color:var(--ink2);margin-top:4px;font-size:13px}
.badge{display:inline-flex;align-items:center;gap:7px;background:rgba(0,200,117,.12);border:1px solid rgba(0,200,117,.4);
color:var(--green);font-weight:600;font-size:12px;padding:6px 12px;border-radius:999px;white-space:nowrap}
.badge i{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 6px var(--green)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:28px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:var(--r);padding:14px 16px;display:flex;flex-direction:column;gap:3px}
.klabel{font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--ink3);font-weight:600}
.kval{font-size:26px;font-weight:700;letter-spacing:-.5px}
.done-ink{color:var(--green)}.pend-ink{color:var(--amber)}.blank-ink{color:var(--ink2)}
.delta{font-size:11px;font-weight:600}.delta.up{color:var(--green)}.delta.down{color:#e8736c}.delta.flat{color:var(--ink3)}
.kbar{height:6px;background:var(--blank);border-radius:4px;overflow:hidden;margin-top:6px}
.kbar span{display:block;height:100%;background:var(--green);border-radius:4px}
.unit{margin-bottom:30px}
.unit-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:14px}
h2{font-size:15px;font-weight:700;color:var(--gold)}
.unit-meta{font-size:12px;color:var(--ink3)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:12px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--r);padding:14px 16px;display:flex;flex-direction:column;gap:10px}
.card header{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}
.bname{display:flex;gap:9px;min-width:0}.bemoji{font-size:18px;line-height:1.3}
.bname a{font-weight:600;font-size:13.5px;display:block;line-height:1.35}
.owner{font-size:11px;color:var(--ink3);margin-top:2px}
.bstat{text-align:right;white-space:nowrap;display:flex;flex-direction:column;align-items:flex-end;gap:1px}
.pct{font-size:17px;font-weight:700}.count{font-size:11px;color:var(--ink2)}
.subpill{font-size:10.5px;color:var(--ink3);border:1px solid var(--line);border-radius:999px;padding:1px 7px;margin-top:3px}
.bar{display:flex;gap:2px;height:8px;border-radius:5px;overflow:hidden;background:var(--blank)}
.bar.empty{opacity:.4}
.seg{display:block;height:100%;min-width:3px}
.chips{display:flex;flex-wrap:wrap;gap:5px}
.chip{display:inline-flex;align-items:center;gap:5px;font-size:11px;color:var(--ink2);background:var(--panel2);
border:1px solid var(--line);border-radius:999px;padding:2px 8px}
.chip i{width:7px;height:7px;border-radius:50%}.chip b{color:var(--ink);font-weight:600}
.groups{display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--line);padding-top:9px}
.grow{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(70px,1fr) 44px;gap:9px;align-items:center}
.grow .bar{height:6px}
.gname{font-size:11.5px;color:var(--ink2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gcount{font-size:11px;color:var(--ink3);text-align:right;font-variant-numeric:tabular-nums}
.empty-note{color:var(--ink3);font-size:12px;font-style:italic;padding:2px 0 4px}
footer{margin-top:36px;color:var(--ink3);font-size:11.5px;border-top:1px solid var(--line);padding-top:14px;line-height:1.7}
@media(max-width:640px){body{padding:18px 14px 40px}.grid{grid-template-columns:1fr}}
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pantheon Marcom A26 — Operations Dashboard · {PULL_DATE_SHORT}</title>
<style>{css}</style>
</head>
<body>
  <div class="top">
    <div>
      <h1>🏛️ {WORKSPACE_NAME} — Operations Dashboard</h1>
      <div class="sub"><a href="{WORKSPACE_URL}" target="_blank" rel="noopener">{WORKSPACE_URL}</a> · Brand &amp; Content · Engagement &amp; Partnerships · Digital &amp; Analytics · KK Personal Brand · Governance · Make Noise</div>
    </div>
    <span class="badge"><i></i>🟦 LIVE — all 28 boards · {PULL_DATE}</span>
  </div>
  {kpis}
  {"".join(unit_html)}
  <footer>
    Source: monday.com workspace <a href="{WORKSPACE_URL}" target="_blank" rel="noopener">Pantheon Marcom Workplace A26 (2928343)</a>,
    pulled live via MCP on {PULL_DATE}. All 28 boards across 6 folders returned live data this pull (previous build {PREV["date"]}: {PREV["items"]:,} items, {PREV["done"]:,} done).<br>
    Done = items with status <b>Done</b>/<b>Completed</b> · No status = items with an empty status label · Pending = everything else (incl. Stuck, On hold, Confirmed, revisions).
  </footer>
</body>
</html>
"""


if __name__ == "__main__":
    out = "Pantheon_Marcom_A26_Operations_Dashboard_Jul06.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(build())
    print("wrote", out)
