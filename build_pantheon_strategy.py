#!/usr/bin/env python3
"""Pantheon Development — consolidated Social Media STRATEGY + EXECUTION hub (single HTML).
Strategy layer (objectives, audience, positioning, ecosystem, platforms, campaigns, paid,
funnel, founder, brokers, community, KPIs) + execution (calendar, content, stories, activities)
+ competitor benchmarks. Format inspired by the uploaded KK dashboard."""
import json, importlib.util, os

# ---- import execution data (POSTS with unique reels + iso, stories, activities) ----
_here=os.path.dirname(os.path.abspath(__file__))
_spec=importlib.util.spec_from_file_location("ex", os.path.join(_here,"build_pantheon_command_center.py"))
ex=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ex)

# ---- NEW 6-pillar model (user framework) ----
PILLARS=[
 {"key":"projects","name":"Projects","pct":30,"color":"#0D2B6E","purpose":"Generate enquiries.",
  "content":["Project launches","Apartment tours","Drone videos","Masterplans","Floor plans","Construction progress"],"cta":"Book a Viewing","kpi":"Leads"},
 {"key":"lifestyle","name":"Lifestyle","pct":20,"color":"#1B4F9B","purpose":"Sell aspiration.",
  "content":["Morning routines","Family life","Community","Interiors","Amenities","Dubai lifestyle"],"cta":"Save this home","kpi":"Saves & follows"},
 {"key":"investment","name":"Investment","pct":15,"color":"#C8922A","purpose":"Educate investors.",
  "content":["ROI","Market reports","Payment plans","Golden Visa","Why Dubai / JVC / RAK"],"cta":"DM INVEST","kpi":"Qualified investor leads"},
 {"key":"construction","name":"Construction & Delivery","pct":15,"color":"#1A7A45","purpose":"Build trust.",
  "content":["Site progress","Engineers","Behind the scenes","Timelapse","Quality checks","Handover"],"cta":"Track the build","kpi":"Trust / credibility"},
 {"key":"people","name":"People Behind Pantheon","pct":10,"color":"#6C3483","purpose":"Humanise the brand — most developers ignore this.",
  "content":["Architects","Engineers","Sales team","CRM","Designers","Site managers"],"cta":"Meet the team","kpi":"Brand affinity"},
 {"key":"community","name":"Community","pct":10,"color":"#C0392B","purpose":"Build belonging & proof.",
  "content":["Homeowners","Testimonials","Broker stories","Resident interviews","Events","UGC"],"cta":"Share your story","kpi":"Shares / UGC"},
]
PCOLOR={p["key"]:p["color"] for p in PILLARS}
PNAME={p["key"]:p["name"] for p in PILLARS}

OBJECTIVES=[
 ["Build Pantheon as a premium developer","Brand awareness"],
 ["Generate qualified buyer enquiries","Leads"],
 ["Build broker confidence","Broker registrations"],
 ["Showcase construction credibility","Trust"],
 ["Increase project demand before launches","Waitlist"],
 ["Position founders as industry leaders","Authority"],
]

AUDIENCES=[
 {"icon":"🏡","name":"UAE End Users","meta":"Age 28–45 · resident buyers","want":["First home","Upgrade","Luxury lifestyle"],
  "content":["Lifestyle","Amenities","Community","Interior walkthroughs"],"color":"#1B4F9B"},
 {"icon":"📈","name":"Investors","meta":"India · UK · Europe · Russia · KSA","want":["ROI","Capital appreciation","Rental yield","Payment plans"],
  "content":["Investment reels","Market reports","ROI calculators","Golden Visa"],"color":"#C8922A"},
 {"icon":"🤝","name":"Real Estate Brokers","meta":"Channel partners","want":["Commission","Fast inventory","Marketing support"],
  "content":["Broker success stories","New inventory","Sales toolkit","Leaderboards"],"color":"#1A7A45"},
 {"icon":"🏢","name":"Corporate / Brand","meta":"Media · partners · suppliers · talent","want":["Credibility","Partnership","Reputation"],
  "content":["Awards","CSR","Company culture","Events","Leadership"],"color":"#6C3483"},
]

PLATFORMS=[
 {"icon":"📸","name":"Instagram","obj":"Awareness + Leads","content":["Reels","Stories","Carousels","Broadcast Channel"],"cad":"5 feed posts / week · Stories daily","color":"#C0392B"},
 {"icon":"💼","name":"LinkedIn","obj":"Authority","content":["Market insights","Founder posts","Company updates","Construction","Awards"],"cad":"3 posts / week","color":"#1B4F9B"},
 {"icon":"▶️","name":"YouTube","obj":"Evergreen content","content":["Project documentaries","Apartment tours","CEO interviews","Market analysis"],"cad":"2 videos / month","color":"#C0392B"},
 {"icon":"🎵","name":"TikTok / Shorts","obj":"Reach (repurpose)","content":["Apartment tours","POV walkthroughs","Luxury lifestyle","Construction transformations"],"cad":"Repurpose 3–4× / week","color":"#6C3483"},
]

VOLUME=[
 ["July","Launch & Awareness",["12 Reels","6 Carousels","4 Graphics","Daily Stories"]],
 ["August","Community + Education",["10 Reels","8 Carousels","4 Graphics","Daily Stories"]],
 ["September","Trust + Conversion",["12 Reels","6 Carousels","4 Graphics","Daily Stories"]],
]
CAMPAIGNS=[
 ["July","VOXA Campaign",["Reach","Leads","Waitlist"],"#0D2B6E"],
 ["August","Maison Elysée III",["Launch","Sales","Broker activation"],"#C8922A"],
 ["September","Why Pantheon",["Brand positioning","Delivery proof","Portfolio awareness"],"#1A7A45"],
]
PAID=[
 ["Awareness","Top-performing Reels → cold + lookalike",40,"#0D2B6E"],
 ["Lead Generation","Project campaigns → enquiry forms / DM",30,"#C8922A"],
 ["Engagement","Lifestyle · construction · community",20,"#1A7A45"],
 ["Retargeting","Website visitors · IG engagers · video viewers",10,"#6C3483"],
]
FUNNEL=[
 ["1 · Hook","Reel / carousel stops the scroll","Reach"],
 ["2 · Trigger","Comment keyword (VOXA, PLAN, INVEST)","Comment velocity"],
 ["3 · Capture","Auto-DM sends deck + qualifying question","DM started"],
 ["4 · Qualify","WhatsApp flow: budget, timeline, end-use","Qualified lead"],
 ["5 · Route","Lead lands in CRM → assigned to sales","Site visit booked"],
 ["6 · Nurture","Retargeting + follow-up sequence","Booking"],
]
FOUNDER=[
 "Kalpesh Kinariwala becomes a visible thought leader — his account out-engages the brand many times over; that gap is unrealised reach.",
 "Weekly LinkedIn founder post: a market take, a delivery milestone, or a lesson from building in Dubai.",
 "Monthly executive video / podcast appearance, repurposed into 3–4 reels for the brand account.",
 "Founder appears IN brand content via IG Native Collab — never siloed — so both audiences compound.",
]
BROKER=[
 "Monthly broker leaderboard — top referrers featured + a prize tier; reshare their wins as UGC.",
 "Exclusive first-access previews of new inventory before public launch.",
 "Ready-to-use sales toolkit: reels, carousels, floor plans, payment-plan cards, captions.",
 "Commission & availability updates in a dedicated Broadcast Channel.",
 "Quarterly broker recognition / event content for prestige.",
]
COMMUNITY=[
 "Reply to comments within 1 hour (protects first-hour ranking).",
 "Reply to DMs within 15 minutes (speed-to-lead wins deals).",
 "Reshare every tagged Story, credit the creator.",
 "Follow up on every project enquiry the same day.",
 "Engage daily with brokers and industry pages.",
]
KPIS=[
 ["Reach","2–3M","#0D2B6E"],["Profile Visits","25K+","#1B4F9B"],["Engagement Rate","2%+","#C8922A"],
 ["Website Clicks","8K+","#1A7A45"],["WhatsApp Clicks","2K+","#6C3483"],["Qualified Leads","300+","#C0392B"],
 ["Broker Registrations","100+","#0D2B6E"],["Saved Posts","8K+","#C8922A"],["Shares","4K+","#1A7A45"],
 ["Video Completion","40%+","#6C3483"],
]

# ---- competitor benchmarks (6 accounts) ----
COMP=[
 {"h":"@imtiazdevelopments","note":"Theatrical launches + celebrity (Hrithik, Zaha Hadid). Steal the production value.","url":"https://www.instagram.com/imtiazdevelopments/","reel":ex.REELS[0]},
 {"h":"@samana.developers","note":"Fastest-accelerating; investor-first single-number reels convert NRIs.","url":"https://www.instagram.com/samana.developers/","reel":ex.REELS[6]},
 {"h":"@bnw.developments","note":"Highest engagement rate of the set; couture-branded, founder-voice captions.","url":"https://www.instagram.com/bnw.developments/","reel":ex.REELS[4]},
 {"h":"@danubeproperties","note":"Volume machine — high-frequency lifestyle, amenity & creator-collab reels.","url":"https://www.instagram.com/danubeproperties/","reel":ex.REELS[9]},
 {"h":"@official.richmind","note":"Emerging boutique developer — study their design-led aesthetic & launch cadence.","url":"https://www.instagram.com/official.richmind/","reel":None},
 {"h":"@wadandevelopments","note":"Newer entrant — watch their positioning and broker-facing content.","url":"https://www.instagram.com/wadandevelopments/","reel":None},
]

# ---- remap execution posts to the 6-pillar model ----
OLD2NEW={"project":"projects","lifestyle":"lifestyle","invest":"investment","delivery":"construction","community":"community"}
PEOPLE_TITLES={"48 hours of Pantheon (BTS)","Why our brokers keep coming back"}
EPOSTS=[]
for p in ex.POSTS:
    q=dict(p)
    q["pillar"]=("people" if p["title"] in PEOPLE_TITLES else OLD2NEW.get(p["pillar"],p["pillar"]))
    EPOSTS.append(q)

EDATA={"posts":EPOSTS,"pcolor":PCOLOR,"pname":PNAME,
       "storyRhythm":ex.STORY_RHYTHM,"storyTypes":ex.STORY_TYPES,"storySequence":ex.STORY_SEQUENCE,
       "activities":ex.ACTIVITIES,"activitySchedule":ex.ACTIVITY_SCHEDULE,
       "growthLabels":ex.GROWTH_LABELS,"growth":ex.GROWTH,
       "pillars":PILLARS,"paid":PAID,"kpis":KPIS}

# ================================================================= HTML build
def esc(s): return (str(s)).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

NAV=[
 ("STRATEGY",[("overview","Overview"),("objectives","Objectives"),("audience","Audience"),
   ("positioning","Positioning"),("ecosystem","Content Ecosystem"),("platforms","Platforms"),
   ("campaigns","Campaigns & Volume"),("paid","Paid Media"),("funnel","Conversion Funnel"),
   ("founder","Founder Layer"),("brokers","Broker Program"),("community","Community Ops"),("kpis","KPI Dashboard")]),
 ("EXECUTION",[("calendar","Calendar"),("content","Content Engine"),("stories","Stories"),("activities","Activities")]),
 ("INTEL",[("competitors","Competitors"),("growth","Growth Model")]),
]

def sidebar():
    h='<div class="sb"><div class="sb-brand"><h2>PANTHEON</h2><p>Social Strategy · Q3 2026</p></div>'
    for lbl,items in NAV:
        h+='<div class="sb-section"><div class="sb-section-lbl">'+lbl+'</div>'
        for sid,nm in items:
            h+='<a class="sb-link" href="#'+sid+'"><span class="sb-dot" style="background:#C8922A"></span>'+nm+'</a>'
        h+='</div>'
    h+='<div class="sb-section"><button class="sbbtn" onclick="toggleEdit()" id="editBtn">✏️ Edit Mode</button>'
    h+='<button class="sbbtn gold" onclick="downloadCopy()">⬇ Download</button></div></div>'
    return h

def hero():
    chips="".join('<span class="ct-chip">'+w+'</span>' for w in ["Design","Trust","Delivery"])
    return ('<div class="hero"><div class="hero-meta">'
      '<h1>Pantheon Development — Social Media Strategy</h1>'
      '<div class="hero-tag">July – September 2026 · Strategy + Execution Hub</div>'
      '<p class="hero-desc">A complete marketing strategy, not just a content calendar. It answers <b>why</b> we post, <b>who</b> we speak to, what <b>business result</b> each pillar drives, and how we <b>convert</b> viewers into enquiries — then hands the team a day-by-day execution playbook with real creative references.</p>'
      '<div class="hero-pos">Positioning: <b>Building Tomorrow\'s Lifestyle Through Design, Delivery &amp; Trust.</b></div>'
      '<div class="ct-row">'+chips+'</div>'
      '<div class="hero-stats">'
      '<div class="hs"><div class="v">40K → 100K</div><div class="l">Follower goal · 90 days</div></div>'
      '<div class="hs"><div class="v">6</div><div class="l">Content pillars</div></div>'
      '<div class="hs"><div class="v">4</div><div class="l">Audience segments</div></div>'
      '<div class="hs"><div class="v">300+</div><div class="l">Qualified leads / mo target</div></div>'
      '</div></div></div>')

def sec(sid,title,sub,body,bg=""):
    return ('<section id="'+sid+'" class="ps'+(' alt' if bg else '')+'"><div class="ps-title">'+title+'</div>'
      +('<div class="ps-sub">'+sub+'</div>' if sub else '')+body+'</section>')

def objectives():
    rows="".join('<tr><td>'+esc(o)+'</td><td><span class="kpibadge">'+esc(k)+'</span></td></tr>' for o,k in OBJECTIVES)
    return sec("objectives","Primary Business Objectives","Every pillar maps to a business goal — not just engagement.",
      '<table class="tbl"><tr><th>Objective</th><th>KPI</th></tr>'+rows+'</table>')

def audience():
    cards=""
    for a in AUDIENCES:
        cards+=('<div class="acard" style="border-top-color:'+a["color"]+'">'
          '<div class="aic">'+a["icon"]+'</div><div class="anm">'+a["name"]+'</div>'
          '<div class="ameta">'+esc(a["meta"])+'</div>'
          '<div class="albl">Looking for</div><div class="achips">'+"".join('<span>'+esc(w)+'</span>' for w in a["want"])+'</div>'
          '<div class="albl">Content they care about</div><div class="achips alt">'+"".join('<span>'+esc(c)+'</span>' for c in a["content"])+'</div>'
          '</div>')
    return sec("audience","Target Audience","Stop speaking to everyone. Four segments, four content strategies.",'<div class="agrid">'+cards+'</div>')

def positioning():
    body=('<div class="posrow">'
      '<div class="poscard old"><div class="poslbl">Instead of</div><div class="posbig">"Luxury Real Estate Developer"</div></div>'
      '<div class="posarrow">→</div>'
      '<div class="poscard new"><div class="poslbl">Position as</div><div class="posbig">Building Tomorrow\'s Lifestyle Through Design, Delivery &amp; Trust.</div></div>'
      '</div><div class="posthree">'
      +"".join('<div class="pword">'+w+'</div>' for w in ["Design","Trust","Delivery"])+'</div>')
    return sec("positioning","Brand Positioning","Three words should dominate every piece of communication.",body)

def ecosystem():
    cards=""
    for p in PILLARS:
        cards+=('<div class="ecard" style="--c:'+p["color"]+'">'
          '<div class="ehead"><span class="epct">'+str(p["pct"])+'%</span><span class="enm">'+p["name"]+'</span></div>'
          '<div class="epur">'+esc(p["purpose"])+'</div>'
          '<div class="albl">Content</div><div class="achips">'+"".join('<span>'+esc(c)+'</span>' for c in p["content"])+'</div>'
          '<div class="ecta">CTA: <b>'+esc(p["cta"])+'</b> · drives '+esc(p["kpi"])+'</div></div>')
    return sec("ecosystem","Content Ecosystem","Six pillars, each with a purpose and a business result. The mix below is the target allocation.",
      '<div class="mixbar" id="mixBar"></div><div class="ecogrid">'+cards+'</div>')

def platforms():
    cards=""
    for p in PLATFORMS:
        cards+=('<div class="pfcard" style="border-top-color:'+p["color"]+'">'
          '<div class="pfh"><span class="pfic">'+p["icon"]+'</span><span class="pfnm">'+p["name"]+'</span></div>'
          '<div class="pfobj">'+esc(p["obj"])+'</div>'
          '<div class="achips">'+"".join('<span>'+esc(c)+'</span>' for c in p["content"])+'</div>'
          '<div class="pfcad">📅 '+esc(p["cad"])+'</div></div>')
    return sec("platforms","Platform Strategy","One message, adapted per platform's job.",'<div class="pfgrid">'+cards+'</div>')

def campaigns():
    vol=""
    for m,theme,items in VOLUME:
        vol+=('<div class="volcard"><div class="volm">'+m+'</div><div class="voltheme">'+esc(theme)+'</div>'
          '<ul>'+"".join('<li>'+esc(i)+'</li>' for i in items)+'</ul></div>')
    camp=""
    for m,nm,goals,c in CAMPAIGNS:
        camp+=('<div class="campcard" style="--c:'+c+'"><div class="campm">'+m+'</div><div class="campnm">'+esc(nm)+'</div>'
          '<div class="achips">'+"".join('<span>'+esc(g)+'</span>' for g in goals)+'</div></div>')
    return sec("campaigns","Monthly Campaigns & Volume","A flagship campaign anchors every month; volume ramps for momentum.",
      '<div class="albl big">Flagship campaigns</div><div class="campgrid">'+camp+'</div>'
      '<div class="albl big" style="margin-top:22px">Posting volume</div><div class="volgrid">'+vol+'</div>')

def paid():
    bars="".join('<div class="paidrow"><div class="paidn">'+esc(b[0])+'</div><div class="paidbarwrap">'
      '<div class="paidbar" style="width:'+str(b[2])+'%;background:'+b[3]+'">'+str(b[2])+'%</div></div>'
      '<div class="paidd">'+esc(b[1])+'</div></div>' for b in PAID)
    return sec("paid","Paid Media Strategy","Don't boost everything. Allocate by funnel stage.",'<div class="paidwrap">'+bars+'</div>')

def funnel():
    steps="".join('<div class="fstep"><div class="fsnum">'+esc(s[0])+'</div><div class="fsbody">'
      '<div class="fst">'+esc(s[1])+'</div><div class="fsk">📈 '+esc(s[2])+'</div></div></div>'
      +('<div class="farrow">↓</div>' if i<len(FUNNEL)-1 else '') for i,s in enumerate(FUNNEL))
    return sec("funnel","Conversion Funnel","Turn reach into enquiries — comment keyword → auto-DM → WhatsApp → CRM.",'<div class="funnel">'+steps+'</div>')

def listsec(sid,title,sub,items,icon="✔"):
    body='<div class="checklist">'+"".join('<div class="cli"><span class="clk">'+icon+'</span><span>'+esc(x)+'</span></div>' for x in items)+'</div>'
    return sec(sid,title,sub,body)

def kpis():
    cards="".join('<div class="kcard" style="border-top-color:'+k[2]+'"><div class="kv">'+esc(k[1])+'</div><div class="kl">'+esc(k[0])+'</div></div>' for k in KPIS)
    return sec("kpis","KPI Dashboard","Measure business impact, not just followers. Monthly targets.",
      '<div class="kgrid">'+cards+'</div><div class="chartbox"><h4>Pillar mix vs paid-media split</h4><div class="cv"><canvas id="cMix"></canvas></div></div>')

import re as _re
def _ig_embed(url):
    m=_re.search(r"/(reel|p|tv)/([^/?#]+)",url or "")
    return "https://www.instagram.com/reel/%s/embed"%m.group(2) if m else url
def competitors():
    cards=""
    for c in COMP:
        reel=''
        if c["reel"]:
            r=c["reel"]
            reel=('<div class="refnote">🎬 <b>'+esc(r[0])+'</b> — Copy this: '+esc(r[2])+'</div>'
                  '<div class="igwrap"><iframe class="igframe" src="'+_ig_embed(r[1])+'" loading="lazy" scrolling="no" allowtransparency="true" allowfullscreen></iframe></div>')
        cards+=('<div class="ccard"><div class="ch">'+esc(c["h"])+'</div><div class="cnote">'+esc(c["note"])+'</div>'
          +reel+'<a class="cprofile" href="'+c["url"]+'" target="_blank" rel="noopener">Open profile →</a></div>')
    return sec("competitors","Competitor Benchmarks","Six UAE developers to study — each with one high-performing reel embedded inline to watch right here.",'<div class="cgrid">'+cards+'</div>')

# execution sections render client-side
EXEC_SECTIONS=('<section id="calendar" class="ps"><div class="ps-title">Calendar View</div>'
 '<div class="ps-sub">Every flagship post on its day, July → September. Colour = pillar, icon = format. Tap a post to jump to its brief.</div><div id="calWrap"></div></section>'
 '<section id="content" class="ps alt"><div class="ps-title">Content Engine</div>'
 '<div class="ps-sub">'+str(len(EPOSTS))+' fully-briefed posts across the quarter — every reel, carousel and static the plan calls for. Reels get a shot brief, carousels a slide-by-slide breakdown, statics a design layout — each with a Story tie-in and a real reference reel. Filter below.</div>'
 '<div class="filters" id="filters"></div><div class="posts" id="postGrid"></div></section>'
 '<section id="stories" class="ps"><div class="ps-title">Stories Playbook</div>'
 '<div class="ps-sub">The daily growth layer: rhythm, interaction toolkit and the launch-day sequence.</div>'
 '<div class="albl big">Daily rhythm</div><table class="tbl" id="storyRhythm"></table>'
 '<div class="albl big" style="margin-top:20px">Interaction toolkit</div><div id="storyTypes"></div>'
 '<div class="albl big" style="margin-top:20px">Launch-day sequence (8 frames)</div><div id="storySeq"></div></section>'
 '<section id="activities" class="ps alt"><div class="ps-title">Activities & Engagement Campaigns</div>'
 '<div class="ps-sub">The recurring campaigns that manufacture reach, leads and UGC.</div>'
 '<div class="actgrid" id="activityGrid"></div>'
 '<div class="albl big" style="margin-top:20px">Quarter schedule</div><table class="tbl" id="activitySchedule"></table></section>'
 '<section id="growth" class="ps"><div class="ps-title">Growth Model</div>'
 '<div class="ps-sub">40K → 100K trajectory and a transparent simulator: drag the levers to see the 90-day outcome.</div>'
 '<div class="growthrow"><div class="chartbox"><h4>Follower trajectory</h4><div class="cv"><canvas id="cGrowth"></canvas></div></div>'
 '<div class="sim"><div class="row"><span>Feed posts / week</span><span class="val" id="vPosts">6</span></div><input type="range" id="sPosts" min="2" max="10" value="6" oninput="sim()">'
 '<div class="row"><span>Collab reels / month</span><span class="val" id="vCollab">3</span></div><input type="range" id="sCollab" min="0" max="8" value="3" oninput="sim()">'
 '<div class="row"><span>Monthly boost (AED)</span><span class="val">AED <span id="vBudget">27,000</span></span></div><input type="range" id="sBudget" min="0" max="45000" step="1000" value="27000" oninput="sim()">'
 '<div class="simout"><div class="b"><div class="n" id="oFollowers">100K</div><div class="l">90-day followers</div></div>'
 '<div class="b"><div class="n" id="oReach">14M</div><div class="l">Est. reach</div></div>'
 '<div class="b"><div class="n" id="oVerdict">On track</div><div class="l">Verdict</div></div></div>'
 '<div class="note" id="simNote"></div></div></div></section>')

CSS=r"""
:root{--ink:#0A0A0A;--navy:#0D2B6E;--blue:#1B4F9B;--gold:#C8922A;--gold-bg:#FBF5E8;
--surface:#FAFAF8;--border:#E8E4DC;--gray:#5D6D7E;--shadow:0 3px 18px rgba(0,0,0,.08);--shadow-lg:0 6px 28px rgba(0,0,0,.12)}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:'Segoe UI',Arial,sans-serif;background:#F5F3EF;color:var(--ink);line-height:1.55}
a{text-decoration:none}
.sb{position:fixed;top:0;left:0;width:230px;height:100vh;background:var(--ink);overflow-y:auto;z-index:200;padding-bottom:24px}
.sb-brand{padding:18px;border-bottom:1px solid rgba(255,255,255,.1)}
.sb-brand h2{color:var(--gold);font-size:17px;font-weight:900;letter-spacing:1px}
.sb-brand p{color:rgba(255,255,255,.4);font-size:10px;margin-top:2px}
.sb-section{padding:12px 12px 4px}
.sb-section-lbl{color:rgba(255,255,255,.32);font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.sb-link{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:7px;color:rgba(255,255,255,.66);font-size:12.5px;font-weight:600;cursor:pointer}
.sb-link:hover{background:rgba(255,255,255,.08);color:#fff}
.sb-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;opacity:.7}
.sbbtn{width:100%;margin-top:8px;padding:9px;border-radius:8px;border:1px solid rgba(255,255,255,.2);background:transparent;color:#fff;font-weight:700;font-size:12px;cursor:pointer}
.sbbtn.gold{background:var(--gold);color:var(--ink);border:none}
.main{margin-left:230px}
.hero{background:var(--ink);padding:40px 46px;border-bottom:4px solid var(--gold)}
.hero-meta h1{color:#fff;font-size:30px;font-weight:900;line-height:1.12}
.hero-tag{color:var(--gold);font-size:12.5px;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin:6px 0 14px}
.hero-desc{color:rgba(255,255,255,.72);font-size:14px;max-width:780px;margin-bottom:14px}
.hero-pos{color:#fff;font-size:14px;background:rgba(200,146,42,.14);border:1px solid var(--gold);border-radius:9px;padding:11px 15px;max-width:780px;margin-bottom:14px}
.ct-row{display:flex;gap:8px;margin-bottom:18px}
.ct-chip{padding:5px 16px;border-radius:18px;font-size:12px;font-weight:800;border:1.5px solid var(--gold);color:var(--gold)}
.hero-stats{display:flex;gap:30px;flex-wrap:wrap}
.hs .v{color:#fff;font-size:21px;font-weight:900}.hs .l{color:rgba(255,255,255,.45);font-size:10px;text-transform:uppercase;letter-spacing:.5px}
.ps{padding:34px 46px;border-bottom:2px solid var(--border);background:#fff}
.ps.alt{background:var(--surface)}
.ps-title{font-size:21px;font-weight:900;color:var(--navy);margin-bottom:4px}
.ps-sub{color:var(--gray);font-size:13.5px;margin-bottom:20px;max-width:820px}
.albl{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.7px;color:var(--gray);margin:10px 0 7px}
.albl.big{font-size:12px;color:var(--navy)}
.tbl{width:100%;border-collapse:collapse;font-size:13.5px;background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.tbl th{background:var(--navy);color:#fff;text-align:left;padding:11px 14px;font-size:11px;text-transform:uppercase;letter-spacing:.5px}
.tbl td{padding:11px 14px;border-bottom:1px solid var(--border);vertical-align:top}
.kpibadge{background:var(--gold-bg);color:var(--gold);font-weight:800;padding:3px 11px;border-radius:14px;font-size:12px}
.agrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.acard{background:#fff;border:1px solid var(--border);border-top:4px solid;border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.aic{font-size:26px}.anm{font-weight:900;color:var(--navy);font-size:15px;margin-top:6px}.ameta{font-size:11.5px;color:var(--gray);margin-bottom:8px}
.achips{display:flex;flex-wrap:wrap;gap:5px}.achips span{background:var(--gold-bg);color:#8a6418;font-size:11px;font-weight:700;padding:3px 9px;border-radius:12px}
.achips.alt span{background:#EAF2FB;color:var(--blue)}
.posrow{display:flex;align-items:stretch;gap:16px;flex-wrap:wrap}
.poscard{flex:1;min-width:240px;border-radius:12px;padding:20px}
.poscard.old{background:#F4F1EC;border:1px dashed #c9c2b4}.poscard.new{background:var(--navy);color:#fff}
.poslbl{font-size:10px;text-transform:uppercase;letter-spacing:1px;color:var(--gray);font-weight:800;margin-bottom:8px}
.poscard.new .poslbl{color:var(--gold)}
.posbig{font-size:18px;font-weight:900}.poscard.old .posbig{color:#7a7466}
.posarrow{display:flex;align-items:center;font-size:26px;color:var(--gold);font-weight:900}
.posthree{display:flex;gap:14px;margin-top:16px}
.pword{flex:1;text-align:center;background:var(--gold-bg);border:1px solid var(--gold);color:var(--gold);font-weight:900;font-size:16px;padding:14px;border-radius:10px;letter-spacing:1px}
.mixbar{display:flex;height:34px;border-radius:8px;overflow:hidden;margin-bottom:18px;box-shadow:var(--shadow)}
.mixseg{display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:800}
.ecogrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.ecard{background:#fff;border:1px solid var(--border);border-left:5px solid var(--c);border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.ehead{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.epct{background:var(--c);color:#fff;font-weight:900;font-size:15px;padding:3px 11px;border-radius:8px}
.enm{font-weight:900;color:var(--navy);font-size:15px}
.epur{font-size:13px;color:var(--gray);margin-bottom:10px;font-style:italic}
.ecta{font-size:12px;color:var(--ink);margin-top:10px;border-top:1px solid var(--border);padding-top:9px}.ecta b{color:var(--c)}
.pfgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.pfcard{background:#fff;border:1px solid var(--border);border-top:4px solid;border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.pfh{display:flex;align-items:center;gap:8px}.pfic{font-size:22px}.pfnm{font-weight:900;color:var(--navy);font-size:15px}
.pfobj{font-size:12px;font-weight:700;color:var(--gold);margin:4px 0 10px}.pfcad{font-size:11.5px;color:var(--gray);margin-top:10px}
.campgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.campcard{background:#fff;border:1px solid var(--border);border-top:4px solid var(--c);border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.campm{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:var(--gray);font-weight:800}.campnm{font-size:17px;font-weight:900;color:var(--c);margin:3px 0 10px}
.volgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.volcard{background:#fff;border:1px solid var(--border);border-radius:12px;padding:16px;box-shadow:var(--shadow)}
.volm{font-weight:900;color:var(--navy)}.voltheme{font-size:12px;color:var(--gold);font-weight:700;margin-bottom:8px}
.volcard ul{margin-left:16px;font-size:13px;color:var(--gray)}
.paidwrap{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.paidrow{display:grid;grid-template-columns:140px 1fr;gap:10px;align-items:center;margin-bottom:12px}
.paidn{font-weight:800;color:var(--navy);font-size:13px}
.paidbarwrap{background:#F0ECE4;border-radius:8px;overflow:hidden}
.paidbar{padding:6px 12px;color:#fff;font-weight:800;font-size:12px;border-radius:8px}
.paidd{grid-column:2;font-size:11.5px;color:var(--gray);margin-top:-6px}
.funnel{max-width:620px}
.fstep{display:flex;gap:14px;background:#fff;border:1px solid var(--border);border-left:4px solid var(--gold);border-radius:10px;padding:13px 16px;box-shadow:var(--shadow)}
.fsnum{font-weight:900;color:var(--gold);min-width:74px;font-size:12px}
.fst{font-weight:700;color:var(--ink);font-size:13.5px}.fsk{font-size:11.5px;color:var(--G,#1A7A45);color:#1A7A45;margin-top:2px}
.farrow{text-align:center;color:var(--gold);font-size:18px;margin:3px 0}
.checklist{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.cli{display:flex;gap:10px;background:#fff;border:1px solid var(--border);border-radius:10px;padding:12px 14px;font-size:13px;color:var(--ink);box-shadow:var(--shadow)}
.clk{color:var(--gold);font-weight:900}
.kgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:20px}
.kcard{background:#fff;border:1px solid var(--border);border-top:4px solid;border-radius:11px;padding:16px;text-align:center;box-shadow:var(--shadow)}
.kv{font-size:22px;font-weight:900;color:var(--navy)}.kl{font-size:11px;color:var(--gray);margin-top:3px}
.chartbox{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.chartbox h4{font-size:13px;color:var(--navy);margin-bottom:12px}.cv{position:relative;height:260px}
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.ccard{background:#fff;border:1px solid var(--border);border-radius:12px;padding:16px;box-shadow:var(--shadow)}
.ch{font-weight:900;color:var(--navy);font-size:14px}.cnote{font-size:12.5px;color:var(--gray);margin:5px 0 9px}
.reflink{display:block;background:var(--gold-bg);border:1px solid var(--gold);border-radius:9px;padding:10px 12px;font-size:12.5px;margin-bottom:8px}
.reflink .ti{color:#8a6418;font-weight:800}.reflink .cp{display:block;color:var(--gray);font-size:11.5px;margin-top:3px}
.media{margin:12px 0}
.igwrap{max-width:340px;margin:8px auto;background:#fff;border-radius:12px;overflow:hidden;border:1px solid var(--border)}
.igframe{width:100%;height:560px;border:0;display:block;background:#fff}
.refnote{font-size:11.5px;color:var(--gray);margin-top:8px;line-height:1.4}.refnote b{color:#8a6418}
.cdeck{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px 2px 12px;scrollbar-width:thin}
.cslide{scroll-snap-align:center;flex:0 0 80%;max-width:300px;aspect-ratio:4/5;background:linear-gradient(160deg,var(--navy),#08306b);border:1px solid var(--gold);border-radius:14px;padding:18px;display:flex;flex-direction:column;box-shadow:var(--shadow-lg)}
.cslide .cn{font-size:11px;font-weight:800;color:var(--ink);background:var(--gold);align-self:flex-start;padding:3px 10px;border-radius:10px;letter-spacing:.5px}
.cslide .ctxt{margin-top:12px;font-size:14.5px;color:#fff;font-weight:600;line-height:1.45}
.cslide .cft{margin-top:auto;font-size:10px;color:var(--gold);letter-spacing:1.5px;text-transform:uppercase;padding-top:10px}
.cdeckhint{font-size:11px;color:var(--gray);text-align:center;margin-top:-2px}
.smock{max-width:300px;aspect-ratio:4/5;margin:8px auto;background:radial-gradient(130% 80% at 50% 0%,rgba(200,146,42,.22),transparent),linear-gradient(180deg,var(--navy),#08306b);border:1px solid var(--gold);border-radius:16px;padding:24px;display:flex;flex-direction:column;text-align:center;box-shadow:var(--shadow-lg)}
.smock .sbrand{font-size:11px;letter-spacing:4px;color:var(--gold);font-weight:800}
.smock .shead{margin:auto 0;font-size:22px;font-weight:900;color:#fff;line-height:1.28}
.smock .ssub{font-size:13px;color:var(--gold);margin-top:12px;font-weight:700}
.smock .sfoot{font-size:10.5px;color:rgba(255,255,255,.6);margin-top:16px;letter-spacing:1px}
.cprofile{font-size:12px;font-weight:700;color:var(--blue)}
/* calendar */
.calmonth{margin-bottom:24px}.calmonth h4{color:var(--navy);margin-bottom:8px;font-size:15px}
.calgrid{display:grid;grid-template-columns:repeat(7,1fr);gap:5px}
.caldow{font-size:10px;color:var(--gray);text-transform:uppercase;text-align:center;font-weight:800;padding-bottom:3px}
.calcell{min-height:88px;background:#fff;border:1px solid var(--border);border-radius:7px;padding:5px}
.calcell.empty{background:transparent;border:none}
.calday{font-size:10px;color:var(--gray);font-weight:800;margin-bottom:3px}
.calchip{display:block;font-size:10px;color:#fff;background:var(--c);border-radius:5px;padding:3px 6px;margin-bottom:3px;font-weight:700;cursor:pointer;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
/* posts */
.filters{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:18px}
.fbtn{background:#fff;border:1px solid var(--border);color:var(--gray);padding:7px 13px;border-radius:18px;cursor:pointer;font-size:12px;font-weight:700}
.fbtn.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.posts{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.post{background:#fff;border:1px solid var(--border);border-top:4px solid var(--c);border-radius:12px;padding:18px;box-shadow:var(--shadow)}
.post .top{display:flex;justify-content:space-between;gap:8px;margin-bottom:6px}
.post .date{font-size:11.5px;color:var(--gray)}.post .date b{color:var(--navy)}
.badges{display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end}
.pill{font-size:10px;font-weight:800;padding:2px 8px;border-radius:11px;text-transform:uppercase;letter-spacing:.4px}
.pill.peak{background:var(--gold-bg);color:var(--gold);border:1px solid var(--gold)}
.pill.boost{background:#EAFAF1;color:#1A7A45;border:1px solid #1A7A45}
.pill.ft{background:#F0ECE4;color:var(--gray)}
.post h3{color:var(--navy);font-size:16px;margin:3px 0 7px}
.hook{font-style:italic;color:var(--gold);font-size:13.5px;margin-bottom:9px}
.cap{font-size:12.5px;color:var(--ink);white-space:pre-line;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:11px;margin-bottom:7px}
.tags{font-size:11.5px;color:var(--blue);margin-bottom:5px}
.cta{font-size:11.5px;color:var(--gray);margin-bottom:9px}.cta b{color:var(--gold)}
details{background:var(--surface);border:1px solid var(--border);border-radius:8px;margin-bottom:6px}
summary{cursor:pointer;padding:9px 12px;font-size:12px;font-weight:800;color:var(--navy);list-style:none}
summary::-webkit-details-marker{display:none}summary::before{content:'▸ ';color:var(--gold)}
details[open] summary::before{content:'▾ '}
.dbody{padding:0 12px 11px;font-size:12px;color:var(--gray)}
.slides{list-style:none;padding:0 12px 11px;margin:0}
.slides li{font-size:12px;color:var(--gray);padding:6px 0;border-bottom:1px solid var(--border)}.slides li:last-child{border:none}
.storyline{font-size:11.5px;color:#6C3483;background:#F5EEF8;border:1px solid #d9c5e3;border-radius:7px;padding:8px 11px;margin-bottom:6px}
.collabtag{font-size:11px;color:#1A7A45;margin:4px 0 7px}
.stype{display:flex;gap:10px;background:#fff;border:1px solid var(--border);border-radius:10px;padding:12px;margin-bottom:8px;box-shadow:var(--shadow)}
.stype .t{font-weight:800;color:var(--navy);font-size:13px}.stype .d{font-size:12px;color:var(--gray)}
.seqitem{display:flex;gap:12px;background:#fff;border:1px solid var(--border);border-radius:9px;padding:11px 13px;margin-bottom:7px;box-shadow:var(--shadow)}
.seqitem .fn{color:var(--gold);font-weight:900;min-width:62px;font-size:12px}
.actgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.act{background:#fff;border:1px solid var(--border);border-top:3px solid var(--gold);border-radius:12px;padding:16px;box-shadow:var(--shadow)}
.act .h{display:flex;gap:9px;align-items:center;margin-bottom:5px}.act .h .e{font-size:20px}.act .h .nm{font-weight:900;color:var(--navy);font-size:14px}
.act .meta{font-size:11.5px;color:var(--gold);font-weight:700;margin-bottom:7px}.act .mech{font-size:12.5px;color:var(--gray)}
.act .kpi{font-size:11.5px;color:#1A7A45;margin-top:7px;border-top:1px solid var(--border);padding-top:7px}
.growthrow{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.sim{background:var(--navy);border-radius:12px;padding:20px;color:#fff}
.sim .row{display:flex;justify-content:space-between;font-size:12.5px;margin:12px 0 5px}.sim .val{color:var(--gold);font-weight:800}
.sim input[type=range]{width:100%;accent-color:var(--gold)}
.simout{display:flex;gap:12px;margin-top:14px}.simout .b{flex:1;background:rgba(255,255,255,.07);border-radius:10px;padding:13px;text-align:center}
.simout .n{font-size:22px;font-weight:900;color:var(--gold)}.simout .l{font-size:10px;color:rgba(255,255,255,.6);text-transform:uppercase}
.note{background:rgba(200,146,42,.12);border:1px solid var(--gold);border-radius:9px;padding:11px 13px;font-size:12px;margin-top:12px;color:#fff}
.editing [contenteditable]{outline:1px dashed var(--gold);outline-offset:2px}
@media(max-width:980px){.sb{width:100%;height:auto;position:relative}.main{margin-left:0}
.agrid,.pfgrid,.kgrid,.ecogrid,.campgrid,.volgrid,.posts,.actgrid,.cgrid,.growthrow,.checklist{grid-template-columns:1fr}
.calgrid{gap:2px}.calchip{white-space:normal}.calcell{min-height:auto}}
"""

JS=r"""
const D=__EDATA__;
function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function ce(){return ' contenteditable="false" '}
/* mix bar + chart data */
document.getElementById('mixBar').innerHTML=D.pillars.map(p=>`<div class="mixseg" style="flex:${p.pct};background:${p.color}">${p.pct}%</div>`).join('');
/* calendar */
const MONTHS=[['July',7],['August',8],['September',9]];const DOW=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
function fic(ft){return ft==='Reel'?'🎬':ft==='Carousel'?'🗂':'🎨'}
document.getElementById('calWrap').innerHTML=MONTHS.map(([nm,mi])=>{
 const first=new Date(2026,mi-1,1).getDay();const lead=(first+6)%7;const dim=new Date(2026,mi,0).getDate();let cells='';
 for(let i=0;i<lead;i++)cells+='<div class="calcell empty"></div>';
 for(let d=1;d<=dim;d++){const iso='2026-'+String(mi).padStart(2,'0')+'-'+String(d).padStart(2,'0');
  const ps=D.posts.filter(p=>p.iso===iso);
  const chips=ps.map(p=>`<span class="calchip" style="--c:${D.pcolor[p.pillar]}" onclick="jump('${iso}')" title="${esc(p.title)}">${fic(p.ftype)} ${esc(p.title)}</span>`).join('');
  cells+=`<div class="calcell"><div class="calday">${d}</div>${chips}</div>`;}
 return `<div class="calmonth"><h4>${nm} 2026</h4><div class="calgrid">${DOW.map(x=>`<div class="caldow">${x}</div>`).join('')}${cells}</div></div>`}).join('');
function jump(iso){const mon={'2026-07':'Jul','2026-08':'Aug','2026-09':'Sep'}[iso.slice(0,7)];
 const b=[...document.querySelectorAll('.fbtn')].find(x=>x.dataset.f===mon);if(b)b.click();
 document.getElementById('content').scrollIntoView({behavior:'smooth'})}
/* posts */
function igCode(u){const m=(u||'').match(/\/(reel|p|tv)\/([^/?#]+)/);return m?m[2]:''}
function igEmbed(u){const c=igCode(u);return c?('https://www.instagram.com/reel/'+c+'/embed'):u}
function igFrame(u){return `<div class="igwrap"><iframe class="igframe" src="${igEmbed(u)}" loading="lazy" scrolling="no" allowtransparency="true" allowfullscreen></iframe></div>`}
function refNote(p){return p.ref.length?`<div class="refnote">🎬 Style reference: <b>${esc(p.ref[0][0])}</b> — ${esc(p.ref[0][2])}</div>`:''}
function carouselDeck(p){
 const slides=p.detail.map((s,i)=>{const k=s.indexOf(' — ');const lbl=k>0?s.slice(0,k):('Slide '+(i+1));const txt=k>0?s.slice(k+3):s;
  return `<div class="cslide"><span class="cn">${esc(lbl)}</span><div class="ctxt" ${ce()}>${esc(txt)}</div><div class="cft">PANTHEON · @pantheon_development</div></div>`;}).join('');
 return `<div class="cdeck">${slides}</div><div class="cdeckhint">← swipe the ${p.detail.length}-slide carousel →</div>`;}
function staticMock(p){return `<div class="smock"><div class="sbrand">PANTHEON</div><div class="shead" ${ce()}>${esc(p.hook||p.title)}</div><div class="ssub" ${ce()}>${esc(p.cta)}</div><div class="sfoot">@pantheon_development</div></div>`;}
function mediaBlock(p){
 if(p.ftype==='Reel')return `<div class="media">${p.ref.length?igFrame(p.ref[0][1]):''}${refNote(p)}</div>`;
 if(p.ftype==='Carousel')return `<div class="media">${carouselDeck(p)}${p.ref.length?`<details><summary>🎬 Style reference (video)</summary><div class="dbody">${igFrame(p.ref[0][1])}${refNote(p)}</div></details>`:''}</div>`;
 return `<div class="media">${staticMock(p)}${p.ref.length?`<details><summary>🎬 Style reference (video)</summary><div class="dbody">${igFrame(p.ref[0][1])}${refNote(p)}</div></details>`:''}</div>`;}
function brief(p){if(p.ftype==='Carousel')return `<details><summary>🗂 Slide copy (${p.detail.length})</summary><ul class="slides">${p.detail.map(s=>`<li ${ce()}>${esc(s)}</li>`).join('')}</ul></details>`;
 if(p.ftype==='Static')return `<details><summary>🎨 Design layout</summary><div class="dbody" ${ce()}>${esc(p.detail)}</div></details>`;
 return `<details><summary>🎬 Shot brief</summary><div class="dbody" ${ce()}>${esc(p.detail)}</div></details>`}
function card(p){const c=D.pcolor[p.pillar];const badges=[`<span class="pill ft">${p.ftype}</span>`];
 if(p.peak)badges.push('<span class="pill peak">⭐ Peak</span>');if(p.boost)badges.push('<span class="pill boost">Boost</span>');
 return `<div class="post" data-pillar="${p.pillar}" data-ft="${p.ftype}" data-peak="${p.peak}" data-boost="${p.boost}" style="--c:${c}">
 <div class="top"><div class="date"><b>${p.date}</b> · ${p.day} ${p.time} · ${D.pname[p.pillar]}</div><div class="badges">${badges.join('')}</div></div>
 <h3 ${ce()}>${esc(p.title)}</h3><div class="hook" ${ce()}>“${esc(p.hook)}”</div>
 ${mediaBlock(p)}
 <div class="cap" ${ce()}>${esc(p.caption)}</div><div class="tags" ${ce()}>${esc(p.tags)}</div>
 <div class="cta">CTA: <b>${esc(p.cta)}</b></div>${p.collab?`<div class="collabtag">🤝 ${esc(p.collab)}</div>`:''}
 <details><summary>🎨 Creative direction</summary><div class="dbody" ${ce()}>${esc(p.direction)}</div></details>
 ${brief(p)}<div class="storyline" ${ce()}>📱 Story tie-in: ${esc(p.story)}</div></div>`}
function render(f){let ps=D.posts.slice();
 if(f&&f!=='all'){if(f==='peak')ps=ps.filter(p=>p.peak);else if(f==='boost')ps=ps.filter(p=>p.boost);
  else if(['Reel','Carousel','Static'].includes(f))ps=ps.filter(p=>p.ftype===f);
  else if(['Jul','Aug','Sep'].includes(f))ps=ps.filter(p=>p.date.startsWith(f));else ps=ps.filter(p=>p.pillar===f)}
 document.getElementById('postGrid').innerHTML=ps.map(card).join('')}
const FILT=[['all','All'],['Jul','July'],['Aug','Aug'],['Sep','Sep'],['Reel','🎬 Reels'],['Carousel','🗂 Carousels'],['Static','🎨 Statics'],
 ['projects','Projects'],['lifestyle','Lifestyle'],['investment','Investment'],['construction','Construction'],['people','People'],['community','Community'],['peak','⭐ Peak']];
document.getElementById('filters').innerHTML=FILT.map((f,i)=>`<button class="fbtn ${i?'':'on'}" data-f="${f[0]}">${f[1]}</button>`).join('');
document.querySelectorAll('.fbtn').forEach(b=>b.onclick=()=>{document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');render(b.dataset.f)});
render('all');
/* stories */
document.getElementById('storyRhythm').innerHTML='<tr><th>Day</th><th>Story</th><th>Why it works</th></tr>'+D.storyRhythm.map(r=>`<tr><td><b>${r[0]}</b></td><td ${ce()}>${esc(r[1])}</td><td ${ce()}>${esc(r[2])}</td></tr>`).join('');
document.getElementById('storyTypes').innerHTML=D.storyTypes.map(s=>`<div class="stype"><div class="t">${s[0]}</div><div class="d" ${ce()}>— ${esc(s[1])}</div></div>`).join('');
document.getElementById('storySeq').innerHTML=D.storySequence.map(s=>`<div class="seqitem"><div class="fn">${s[0]}</div><div ${ce()}>${esc(s[1])}</div></div>`).join('');
/* activities */
document.getElementById('activityGrid').innerHTML=D.activities.map(a=>`<div class="act"><div class="h"><span class="e">${a.icon}</span><span class="nm" ${ce()}>${esc(a.name)}</span></div><div class="meta">${esc(a.cad)} · ${esc(a.plat)}</div><div class="mech" ${ce()}>${esc(a.mech)}</div><div class="kpi">📈 ${esc(a.kpi)}</div></div>`).join('');
document.getElementById('activitySchedule').innerHTML='<tr><th>Month</th><th>Flagship</th><th>Always-on</th></tr>'+D.activitySchedule.map(r=>`<tr><td><b>${r[0]}</b></td><td ${ce()}>${esc(r[1])}</td><td ${ce()}>${esc(r[2])}</td></tr>`).join('');
/* charts */
const navy='#0D2B6E',gold='#C8922A';
new Chart(cMix,{type:'bar',data:{labels:['Pillar mix','Paid split'],datasets:
 D.pillars.map((p,i)=>({label:p.name,data:[p.pct,0],backgroundColor:p.color,stack:'a'}))
 .concat(D.paid.map(b=>({label:b[0],data:[0,b[2]],backgroundColor:b[3],stack:'b'})))},
 options:{indexAxis:'y',plugins:{legend:{position:'bottom',labels:{boxWidth:10,font:{size:10}}}},
 scales:{x:{stacked:true,max:100,ticks:{callback:v=>v+'%'}},y:{stacked:true}}}});
new Chart(cGrowth,{type:'line',data:{labels:D.growthLabels,datasets:[
 {label:'Best',data:D.growth.best,borderColor:gold,backgroundColor:'rgba(200,146,42,.12)',fill:true,tension:.4},
 {label:'Base',data:D.growth.base,borderColor:navy,tension:.4},
 {label:'Conservative',data:D.growth.conservative,borderColor:'#9aa6c4',borderDash:[5,4],tension:.4}]},
 options:{plugins:{legend:{labels:{boxWidth:12}}},scales:{y:{ticks:{callback:v=>v+'K'}}}}});
/* simulator */
function sim(){const posts=+sPosts.value,collab=+sCollab.value,budget=+sBudget.value;
 vPosts.textContent=posts;vCollab.textContent=collab;vBudget.textContent=budget.toLocaleString();
 let total=Math.round((40000+posts*1100*3+collab*2600*3+budget*0.62*3)/1000)*1000;
 const reach=((posts*4*3*9000)+(collab*3*120000)+(budget*3*120))/1e6;
 oFollowers.textContent=(total/1000).toFixed(0)+'K';oReach.textContent=reach.toFixed(1)+'M';
 let v,n;if(total>=100000){v='🎯 100K';n='This combination lands 100K inside 90 days. Recommended setup.';}
 else if(total>=80000){v='On track';n='Reaches 80–95K — add a collab or a little reach to close the gap.';}
 else if(total>=62000){v='Slower';n='Healthy growth but 100K slips past 90 days.';}
 else{v='⚠ Too light';n='Barely breaks out of 40K — raise volume, collabs and reach.';}
 oVerdict.textContent=v;simNote.textContent=n}
sim();
/* edit + download */
let editing=false;
function toggleEdit(){editing=!editing;document.body.classList.toggle('editing',editing);
 document.querySelectorAll('[contenteditable]').forEach(e=>e.setAttribute('contenteditable',editing));
 editBtn.textContent=editing?'✅ Done':'✏️ Edit Mode'}
function downloadCopy(){if(editing)toggleEdit();const html='<!DOCTYPE html>\n'+document.documentElement.outerHTML;
 const b=new Blob([html],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(b);
 a.download='Pantheon_Social_Strategy_edited.html';a.click()}
"""

body=(sidebar()+'<div class="main">'+hero()
 +sec("overview","Why This Strategy Exists","A premium developer needs more than a posting schedule. This document answers why we post, who we reach, what each pillar earns the business, and how attention becomes enquiries.",
   '<div class="checklist">'+''.join('<div class="cli"><span class="clk">✔</span><span>'+esc(x)+'</span></div>' for x in
     ["Business-first: every pillar maps to a KPI, not just engagement.",
      "Audience-led: four segments, four content strategies.",
      "Conversion-built: comment keywords → auto-DM → WhatsApp → CRM.",
      "Founder authority layer amplifies the brand account.",
      "Broker-specific program turns 100+ agents into a sales channel.",
      "Measured on revenue signals, not vanity metrics."])+'</div>')
 +objectives()+audience()+positioning()+ecosystem()+platforms()+campaigns()+paid()+funnel()
 +listsec("founder","Founder Authority Layer","Kalpesh Kinariwala as a visible thought leader — the brand's biggest unrealised reach.",FOUNDER,"★")
 +listsec("brokers","Broker Program","Turn 100+ brokers into an amplification and sales channel.",BROKER,"◆")
 +listsec("community","Community Operations","Daily discipline that protects ranking and speed-to-lead.",COMMUNITY,"⏱")
 +kpis()+EXEC_SECTIONS.replace('id="growth"','id="growth"',1)
 # reorder: calendar/content/stories/activities then competitors then growth
 +competitors()
 +'</div>')

# EXEC_SECTIONS already contains growth at the end; competitors should come before growth.
# Simpler: rebuild ordering explicitly
EXEC_NO_GROWTH=EXEC_SECTIONS.split('<section id="growth"')[0]
GROWTH_SEC='<section id="growth"'+EXEC_SECTIONS.split('<section id="growth"')[1]
body=(sidebar()+'<div class="main">'+hero()
 +sec("overview","Why This Strategy Exists","A premium developer needs more than a posting schedule. This document answers why we post, who we reach, what each pillar earns the business, and how attention becomes enquiries.",
   '<div class="checklist">'+''.join('<div class="cli"><span class="clk">✔</span><span>'+esc(x)+'</span></div>' for x in
     ["Business-first: every pillar maps to a KPI, not just engagement.",
      "Audience-led: four segments, four content strategies.",
      "Conversion-built: comment keywords → auto-DM → WhatsApp → CRM.",
      "Founder authority layer amplifies the brand account.",
      "Broker-specific program turns 100+ agents into a sales channel.",
      "Measured on revenue signals, not vanity metrics."])+'</div>')
 +objectives()+audience()+positioning()+ecosystem()+platforms()+campaigns()+paid()+funnel()
 +listsec("founder","Founder Authority Layer","Kalpesh Kinariwala as a visible thought leader — the brand's biggest unrealised reach.",FOUNDER,"★")
 +listsec("brokers","Broker Program","Turn 100+ brokers into an amplification and sales channel.",BROKER,"◆")
 +listsec("community","Community Operations","Daily discipline that protects ranking and speed-to-lead.",COMMUNITY,"⏱")
 +kpis()+EXEC_NO_GROWTH+competitors()+GROWTH_SEC+'</div>')

HTML=('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1">'
 '<title>Pantheon Development — Social Media Strategy · Q3 2026</title>'
 '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>'
 '<style>'+CSS+'</style></head><body>'+body
 +'<script>'+JS.replace("__EDATA__",json.dumps(EDATA))+'</script></body></html>')

out=os.path.join(_here,"Pantheon_Social_Strategy_Q3_2026.html")
with open(out,"w",encoding="utf-8") as f: f.write(HTML)
print("Wrote",out,len(HTML),"bytes ·",len(EPOSTS),"posts · pillars",len(PILLARS))
