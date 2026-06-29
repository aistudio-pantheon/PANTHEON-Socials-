#!/usr/bin/env python3
"""Pantheon Development — AI Social Command Center (single editable HTML).
Reels = shot list · Carousels = slide-by-slide · Statics = design layout ·
+ Stories playbook + Activities/Engagement campaigns."""
import json, os

# ---------------------------------------------------------------- REFERENCE REELS (real, verified via search)
REF = {
  "reveal":[
    ["Imtiaz — The Symphony (Zaha Hadid) reveal","https://www.instagram.com/reel/DTCon67Ec55/","Sculptural render in motion, dark→light grade, slow push-ins, ONE hero line of text."],
    ["Danube — The Big Reveal","https://www.instagram.com/reel/DQ_F2UIklKN/","Teaser/curtain before the hero shot lands — withhold, then reveal."]],
  "launch":[["Imtiaz — Symphony grand unveiling (Coca-Cola Arena)","https://www.instagram.com/reel/DRNEsTHjwVR/","Event energy cut to music: crowd + stage + product, fast highlight montage."]],
  "investment":[
    ["Samana — 8% ROI / 1% payment plan reel","https://www.instagram.com/reel/C7DulWLpSNZ/","Bold number on frame 1, simple animated counters, ONE idea per post."],
    ["Danube — luxury living meets smart investment","https://www.instagram.com/reel/DXpHL53isU9/","Lifestyle b-roll under a clear ROI / payment message."]],
  "interior":[
    ["Danube — luxury interior detailing","https://www.instagram.com/reel/DSAk_6mkhH-/","Slow-mo close-ups of materials, warm grade, tactile sound design."],
    ["Danube — effortless furnished living","https://www.instagram.com/reel/DXqzr01CMwA/","One continuous gimbal move through the whole home, no cuts."]],
  "amenities":[
    ["Danube — amenities showcase","https://www.instagram.com/reel/DPN2O9SEYWN/","Rapid cuts, one amenity per beat, biggest reveal on the drop."],
    ["BNW — FashionTV Acacia (turning heads)","https://www.instagram.com/reel/DNN90KSybpO/","Couture-styled framing + bold on-screen typography."]],
  "lifestyle":[["BNW — At FashionTV Acacia","https://www.instagram.com/reel/DKwDhHBy6bt/","Aspirational POV, golden hour, lifestyle tension BEFORE the address reveal."]],
  "ugc":[['@mr.thank.you — "Danube is the new luxury" (creator collab)',"https://www.instagram.com/mr.thank.you/reel/DPgRGrCEwQI/","Creator-voiced, face-to-camera hook, posted as an IG Collab so it hits both audiences."]],
  "construction":[["Dubai — then & now construction timelapse","https://www.instagram.com/reel/DSOQy5GiB4V/","Timelapse with progress %, before→now structure builds delivery trust."]],
}
def refs(*keys):
    out=[]
    for k in keys: out+=REF[k]
    return out

# ---------------------------------------------------------------- PILLARS
PILLARS=[
  {"key":"project","icon":"🏗️","name":"Project Showcase","pct":35,"color":"#C9A227","day":"Wed 3PM ⭐ + Fri 3PM",
   "format":"Reels 60% · Carousels 40%","hook":"Curiosity + exclusivity","cta":"DM a keyword / Visit pantheon.ae","goal":"Leads & enquiries"},
  {"key":"lifestyle","icon":"🌆","name":"Lifestyle & Aspiration","pct":25,"color":"#6C8EBF","day":"Thu 6PM + Mon 7PM",
   "format":"Reels 50% · Carousels 50%","hook":"Aspirational lifestyle tension","cta":"Save + DM","goal":"Saves, follows, emotion"},
  {"key":"community","icon":"👥","name":"Community & UGC","pct":20,"color":"#3FA796","day":"Fri 3PM + Sat 11AM",
   "format":"Reels 70% · Static 30%","hook":"Real story, real person","cta":"Tag someone / share your story","goal":"Comments, shares, brand love"},
  {"key":"invest","icon":"📈","name":"Investment & Market Intel","pct":12,"color":"#B5651D","day":"Tue 1PM (alt weeks)",
   "format":"Carousels 80% · Reels 20%","hook":"Data shock + what it means","cta":"DM for the full breakdown","goal":"High saves, profile visits, DMs"},
  {"key":"delivery","icon":"🔑","name":"Delivery & Trust","pct":8,"color":"#8E7CC3","day":"Sat 11AM",
   "format":"Reels 90%","hook":"Proof: built, handed over, real","cta":"DM to book a viewing","goal":"Trust, credibility, prestige"},
]

WEEK=[
  ["Mon","7:00 PM","Lifestyle Reel","lifestyle","A morning / evening in a Pantheon home"],
  ["Tue","1:00 PM","Investment Carousel","invest","Payment plan or ROI / market data"],
  ["Wed","3:00 PM ⭐","Project Showcase Reel","project","Hero project reveal — peak slot"],
  ["Thu","6:00 PM","Amenity / Lifestyle Reel","lifestyle","Amenity showcase or interior detail"],
  ["Fri","3:00 PM","Community / Collab Reel","community","UGC, testimonial or creator IG Collab"],
  ["Sat","11:00 AM","Delivery / Static","delivery","Progress, handover or occasion graphic"],
  ["Sun","—","Stories + engagement only","community","Polls, Q&A, reshare UGC, reply to DMs"],
]

COMPETITORS=[
  {"h":"@imtiazdevelopments","seg":"140K followers · reach 7.1M","take":"Star power + theatrical launches. The Symphony at Coca-Cola Arena with Hrithik Roshan = 2M-view reels. Steal the production value, not the celebrity budget.","reels":REF["reveal"][:1]+REF["launch"]},
  {"h":"@samana.developers","seg":"161K followers · fastest accelerating (+147% ER)","take":"Investor-first, number-led posts. ₹76 lakh / 8% ROI / 1% plan framing converts NRIs. Copy the single-number hook.","reels":REF["investment"][:1]},
  {"h":"@bnw.developments","seg":"65K followers · 2.42% ER (6× Pantheon)","take":"Highest engagement of the set. Couture-branded FashionTV Acacia reels + founder-voice captions. Copy the aspirational framing.","reels":REF["lifestyle"]+REF["amenities"][1:2]},
  {"h":"@danubeproperties","seg":"381K followers · volume machine","take":"High-frequency lifestyle + amenity + creator-collab reels. The cadence is the lesson: post often, stay top-of-feed.","reels":REF["interior"][:1]+REF["amenities"][:1]+REF["ugc"]},
]

BUDGET=[
  ["Dubai is the most expensive real-estate ad market in the world","Property keywords & lookalike audiences run AED 45–90 CPM — 3–5× a normal market. 40K→100K means buying reach in the priciest auction there is, against developers spending far more."],
  ["Organic reach alone is dead for new pages","Meta caps cold organic reach at ~2–5% of non-followers. To break past 40K you must pay to seed your best 3–4 reels/month into new audiences so the algorithm's free amplification kicks in."],
  ["Competitors are already spending heavily","Samana shows ~31% boosted reels (1.8M-view spikes), Imtiaz ~24%. Their 'organic' headline numbers are paid-assisted. You can't be the only purely-organic page in the feed."],
  ["Content production has a floor","Cinematic reels, drone permits, 3D render motion, an editor and a UGC budget. ~28 quality posts/month at Dubai rates costs money — under-funding it shows on screen instantly."],
  ["Creator & IG-Collab activations multiply reach","One collab reel reaches both audiences at once. Even mid-tier UAE property creators charge AED 1.5–5K/reel — and they're the fastest way to borrow a warm audience."],
  ["The math of 150% growth in 90 days","+60K in 90 days ≈ ~667 followers/day. That pace needs paid reach behind hero content + collabs + retargeting. AED 25–30K/mo is the realistic floor — spend below it and the timeline stretches, not the goal."],
]
BUDGET_TABLE=[
  ["Paid reach / boosting hero reels","AED 12,000 – 14,000","Amplify the 3–4 best reels/month to cold + lookalike audiences"],
  ["Creator & UGC / IG Collab activations","AED 6,000 – 8,000","2–3 creator collab reels/month borrowing warm audiences"],
  ["Content production (reels, drone, render motion, edit)","AED 5,000 – 6,000","The cinematic floor — footage, permits, editing"],
  ["Retargeting + lead-gen DM / landing funnel","AED 2,000 – 2,000","Convert reach into enquiries, not just vanity follows"],
]

ALGO=[
  ["🎬","Reels are the growth engine","85–90% of new reach on IG now comes from Reels in discovery. Pantheon goes Reels-first: ~60% of posts as Reels."],
  ["⚡","First 3 seconds decide everything","A strong visual hook + on-screen text in second 1 lifts watch-time, the #1 ranking signal. No slow logo intros."],
  ["🔖","Optimise for SAVES & SHARES","Saves and sends weigh heaviest in 2026 ranking. Every post needs a save-worthy reason (plan, checklist, floor-plan) or a tag-a-friend trigger."],
  ["💬","Comment velocity in the first hour","Ask ONE simple question; reply to every comment within 60 min to signal an active conversation and extend reach."],
  ["🎵","Trending audio, fresh window","Use audio trending in the last 7 days while it's rising; original VO over it is fine (keep your 91% original-audio habit)."],
  ["🤝","IG Native Collab = double the audience","Post creator/partner content as an IG Collab so it lands in both follower bases at once — your fastest reach multiplier."],
  ["📅","Consistency beats perfection","The algorithm rewards reliable cadence: 5–6 feed posts/week + daily Stories keeps you in the active-creator tier."],
  ["🏷️","3–5 tight hashtags, not 30","Niche + branded tags (#JVCDubai #OffPlanDubai #PantheonDevelopment) beat spray-and-pray. Your data: long caption × 1–3 tags = best ER."],
]

# ---------------------------------------------------------------- CONTENT MIX
CONTENT_MIX=[["Reels","60%","#C9A227"],["Carousels","22%","#6C8EBF"],["Static graphics","8%","#3FA796"],["Stories (daily)","10+/wk","#8E7CC3"]]

# ---------------------------------------------------------------- STORIES PLAYBOOK
STORY_RHYTHM=[
  ["Mon","Goal-setting poll","Poll sticker: 'Studio or penthouse?' → drives replies & segments audience"],
  ["Tue","'Did you know' market stat","Quiz sticker on a JVC/RAK stat → saves the answer, builds authority"],
  ["Wed","Behind today's reel","Teaser + 'Tap to watch the full reel' link sticker → pushes feed reach"],
  ["Thu","Amenity / interior detail","Slider sticker: 'Rate this kitchen' → playful, high tap-through"],
  ["Fri","UGC / testimonial reshare","Reshare a tag + 'Tag us in yours' → fuels more UGC"],
  ["Sat","Site / delivery update","Countdown sticker to next milestone → anticipation"],
  ["Sun","Open Q&A","Questions sticker: 'Ask us anything about buying in Dubai' → DMs + content ideas"],
]
STORY_TYPES=[
  ["📊 Poll","This-or-that on units, views, finishes. Lowest-effort tap, trains the audience to interact."],
  ["❓ Quiz","Market facts (yields, Golden Visa thresholds). Right-answer reveal = a save + authority."],
  ["🎚 Slider / Emoji","'Rate this view' — pure dopamine tap, boosts story completion rate."],
  ["⏳ Countdown","To launches, price changes, event days. Followers opt-in to a reminder = warm leads."],
  ["🔗 Link sticker","Drive to pantheon.ae project pages or the WhatsApp enquiry line."],
  ["💬 Questions / AMA","Weekly 'Ask about buying in Dubai' — answers become next week's content."],
  ["📍 Add-yours / UGC","Reshare every tag, credit the creator, ask others to add theirs."],
]
STORY_SEQUENCE=[
  ["Frame 1","Teaser — blurred render + 'Something's coming to JVT 👀' + countdown sticker"],
  ["Frame 2","Problem — 'Tired of off-plan that never delivers?' (poll: yes/we feel that)"],
  ["Frame 3","Reveal — hero render of the project, name drops"],
  ["Frame 4","Proof — 1 killer stat (price/plan/location) as a big graphic"],
  ["Frame 5","Amenity slider — 'Rate the rooftop'"],
  ["Frame 6","Social proof — reshare a broker/owner quote"],
  ["Frame 7","Offer — payment plan in one line + link sticker to the project page"],
  ["Frame 8","CTA — 'DM the keyword for the full deck' + the feed reel pinned"],
]

# ---------------------------------------------------------------- ACTIVITIES / ENGAGEMENT CAMPAIGNS
ACTIVITIES=[
  {"icon":"🎁","name":"Monthly 'Win a Staycation' Giveaway","cad":"1× / month (last Thu)","plat":"Reel + Stories",
   "mech":"Follow @pantheon_development + tag 2 friends + save the post. Winner drawn live. Each tag = a new warm visitor to the page.","goal":"Followers + reach + saves","kpi":"+1,500–3,000 followers / round"},
  {"icon":"🤝","name":"Broker Referral Leaderboard","cad":"Ongoing, monthly winner","plat":"Stories + DM",
   "mech":"Brokers who refer buyers get featured + a prize tier. Reshare their wins as UGC. Turns 100+ brokers into amplifiers.","goal":"Leads + broker UGC","kpi":"Qualified enquiries"},
  {"icon":"🔴","name":"'Buy in Dubai' Live AMA","cad":"Bi-weekly (Wed 8PM)","plat":"Instagram Live",
   "mech":"15-min live with a Pantheon expert answering buyer questions (Golden Visa, payment plans, JVC vs RAK). Repurpose clips into reels.","goal":"Authority + DMs","kpi":"Live viewers + saved clips"},
  {"icon":"🏆","name":"'Tag Your Dream Home' UGC Challenge","cad":"Monthly theme","plat":"Reels + Add-yours",
   "mech":"Audience posts their dream-home moodboard tagging Pantheon; best entries get reshared + a design consult. Free content + reach.","goal":"UGC volume + community","kpi":"# entries / reshares"},
  {"icon":"📲","name":"Comment-to-DM Lead Funnel","cad":"Every project reel","plat":"Reel + Auto-DM",
   "mech":"'Comment VOXA and we'll DM the deck.' Auto-DM tool sends the brochure + captures the lead. Comment velocity also boosts reach.","goal":"Leads + first-hour comments","kpi":"Comments → DMs → CRM"},
  {"icon":"⚔️","name":"Poll Battles (This or That)","cad":"Weekly (Stories)","plat":"Stories",
   "mech":"'Marble or oak? Pool or gym?' Run a bracket across the week, reveal the winner in a reel. Pure low-cost interaction.","goal":"Story completion + replies","kpi":"Tap-through rate"},
  {"icon":"⏱","name":"Launch Countdown Campaign","cad":"Per launch (10-day)","plat":"Stories + Reels",
   "mech":"10-day countdown: teasers, render drips, broker hype, a price/plan reveal, then launch-day live. Builds a waitlist of warm DMs.","goal":"Waitlist + launch-day rush","kpi":"Countdown opt-ins + day-1 DMs"},
  {"icon":"🌟","name":"Community Spotlight","cad":"Weekly (Fri)","plat":"Reel / Static",
   "mech":"Feature a real owner, broker or the team. Reshare to their network. Humanises the brand and earns reposts.","goal":"Trust + reshares","kpi":"Reshares / profile visits"},
]
ACTIVITY_SCHEDULE=[
  ["July","Launch the giveaway engine + comment-to-DM on every VOXA reel","Kick off the broker leaderboard; first 'Buy in Dubai' Live"],
  ["August","10-day countdown campaign for Maison Elysée III launch","UGC 'Dream Home' challenge; weekly poll battles in full swing"],
  ["September","Golden Visa Live AMA + portfolio giveaway finale","Q3 community spotlight series; biggest giveaway round to push past target"],
]

# ---------------------------------------------------------------- POSTS
# ftype: Reel | Carousel | Static. detail = shot list (Reel) / slides[] (Carousel) / layout (Static)
def P(date,day,time,pillar,ftype,title,hook,caption,tags,cta,direction,detail,ref,story,collab="",peak=False,boost=False):
    return {"date":date,"day":day,"time":time,"pillar":pillar,"ftype":ftype,"title":title,"hook":hook,
            "caption":caption,"tags":tags,"cta":cta,"direction":direction,"detail":detail,"ref":ref,
            "story":story,"collab":collab,"peak":peak,"boost":boost}
T="#PantheonDevelopment #DubaiRealEstate #OffPlanDubai"

POSTS=[
 # ---------- JULY
 P("Jul 2","Wed","3:00 PM","project","Reel","VOXA — the JVT landmark reveal",
   "AED 800M is rising in Jumeirah Village Triangle.",
   "VOXA. A landmark reimagined for how Dubai actually lives — fully-furnished studios to 4-bed penthouses in the heart of JVT.\\n\\nThis isn't another tower. It's the address JVT was waiting for.\\n\\n📍 Jumeirah Village Triangle\\nComment \\\"VOXA\\\" and we'll DM the investor deck.",
   "#VOXA #JVTDubai #DubaiProperty "+T,"Comment \"VOXA\" → auto-DM deck",
   "Dark→light cinematic reveal. Open on a single sculptural detail, pull back to the full render at the music swell. One gold hero line: VOXA.",
   "0:00 sculptural close-up + text hook · 0:03 slow push-in · 0:10 exterior render reveal on drop · 0:20 amenity flashes · 0:38 logo + CTA card.",
   refs("reveal"),"Story sequence (8 frames): teaser → poll → reveal → price stat → amenity slider → broker quote → plan + link → 'DM VOXA'.",peak=True,boost=True),
 P("Jul 3","Thu","6:00 PM","lifestyle","Reel","A morning in your Maison Elysée home",
   "Wake up to this.",
   "07:14 AM. Light through floor-to-ceiling glass, coffee on the balcony, the city still waking up.\\n\\nThis is Maison Elysée — French-inspired living in JVC.\\n\\nSave this for the mornings you're working toward. 🤍",
   "#MaisonElysee #JVCDubai #LuxuryHomesDubai "+T,"Save + DM \"ELYSEE\"",
   "Warm champagne grade. POV gimbal glide: bed → window → coffee → balcony view. Soft trending audio.",
   "0:00 eyes-open POV + text · 0:06 window light · 0:14 coffee detail · 0:22 balcony reveal · 0:30 save CTA.",
   refs("interior"),"Thu story: 'Rate this kitchen' emoji-slider on the same home + link sticker to the project page."),
 P("Jul 5","Sat","11:00 AM","delivery","Reel","Elysée Heights — this month on site",
   "Proof, not promises.",
   "Concrete, steel and momentum. Here's exactly where Elysée Heights stands this month.\\n\\nWe post progress because delivery is the only metric that matters.\\n\\nComment \\\"HEIGHTS\\\" for the construction tracker.",
   "#ElyseeHeights #DubaiConstruction #OffPlanDubai "+T,"Comment \"HEIGHTS\"",
   "Dramatic site timelapse with a progress % counter overlay. Hard cuts on beat.",
   "0:00 drone over site + % overlay · 0:08 timelapse pour · 0:18 worker detail · 0:26 progress card + CTA.",
   refs("construction"),"Sat story: countdown sticker to the next construction milestone."),
 P("Jul 8","Tue","1:00 PM","invest","Carousel","Why JVC rents beat the bank",
   "Your money is losing a race you didn't enter.",
   "JVC is one of Dubai's highest-yielding communities — and Pantheon builds right in the middle of it.\\n\\nSwipe for the numbers most investors miss. 📈\\n\\nComment \\\"YIELD\\\" for the full Maison Elysée payment plan.",
   "#JVCDubai #DubaiInvestment #PropertyInvestment "+T,"Comment \"YIELD\"",
   "Dark luxury data carousel. Gold accents, one number per slide, big type, consistent footer with the @handle.",
   ["Slide 1 — HOOK: 'Your savings account is losing a race.' (bold, full-bleed)",
    "Slide 2 — STAT: JVC avg rental yield ≈ 7–8% vs ~1% bank deposit (side-by-side bars)",
    "Slide 3 — MATH: AED 1M in JVC property vs in the bank over 5 years (two end numbers)",
    "Slide 4 — WHY JVC: location, tenant demand, limited new supply — 3 icons + one line each",
    "Slide 5 — WHY NOW: Pantheon Maison Elysée plan = enter with a fraction",
    "Slide 6 — CTA: 'Comment YIELD for the full payment plan' + @pantheon_development"],
   refs("investment"),"Tue story: quiz — 'What's JVC's average rental yield?' reveal answer → save."),
 P("Jul 11","Fri","3:00 PM","community","Reel","Creator walks Maison Elysée (IG Collab)",
   "I didn't expect this in JVC.",
   "We handed a creator the keys and said: be honest.\\n\\nThis is Maison Elysée through their eyes — unscripted.\\n\\nTag someone who'd live here. 👇",
   "#MaisonElysee #DubaiRealEstate #JVCDubai "+T,"Tag a friend",
   "Creator face-to-camera hook, then handheld walk-through. Post as IG Native Collab with the creator.",
   "0:00 creator hook to camera · 0:05 entry reaction · 0:15 best room · 0:28 verdict + tag CTA.",
   refs("ugc"),"Fri story: reshare the creator's own story + 'Add yours' sticker.",collab="@creator (IG Collab)",boost=True),
 P("Jul 15","Tue","6:00 PM","invest","Static","Islamic New Year greeting",
   "From all of us at Pantheon.",
   "Wishing you and your family a blessed Islamic New Year. May the year ahead bring growth, peace and a place to truly call home. 🌙\\n\\n— The Pantheon Development family",
   "#IslamicNewYear #Pantheon #Dubai "+T,"—",
   "Typography-led occasion graphic. Arabic + English, crescent motif, navy + gold. No stock photos — keep it brand-pure.",
   "Static design layout — Center: crescent + 'Happy Islamic New Year'. Top: small Pantheon logo. Bottom: handle + muted greeting line. 1080×1350.",
   [],"Story: matching greeting frame with a 'Send blessings' resharable sticker."),
 P("Jul 16","Wed","3:00 PM","project","Reel","ONE RAK CENTRAL — RAK's next icon",
   "Ras Al Khaimah is the smartest entry in the UAE right now.",
   "ONE RAK CENTRAL. A landmark mixed-use destination at the centre of the fastest-growing emirate.\\n\\nWaterfront energy, island access, RAK's momentum.\\n\\nComment \\\"RAK\\\" for first-access pricing.",
   "#OneRAKCentral #RasAlKhaimah #RAKRealEstate "+T,"Comment \"RAK\"",
   "Cinematic reveal cut with RAK coastline drone. Position RAK as opportunity, not second-choice.",
   "0:00 aerial coastline + text · 0:08 render reveal · 0:18 location context · 0:32 logo + CTA.",
   refs("reveal","launch"),"Story: poll 'Dubai vs RAK for your next investment?' → segments the audience.",peak=True,boost=True),
 P("Jul 18","Fri","3:00 PM","community","Reel","Handover day — real reaction",
   "This is what we actually build for.",
   "Keys. First step inside. That look on their face.\\n\\nEvery render, every site visit, every late night — for this one moment.\\n\\nComment \\\"PANTHEON\\\" to start your story.",
   "#PantheonDevelopment #DubaiHandover #DubaiRealEstate "+T,"Comment \"PANTHEON\"",
   "Mini-doc, emotional. Real resident, soft piano. Get a signed release before posting.",
   "0:00 key in hand + text · 0:08 door opens · 0:16 reaction · 0:26 wide of home + CTA.",
   refs("ugc","interior"),"Story: reshare the owner's reaction + 'Ask them anything' questions sticker."),
 P("Jul 22","Tue","1:00 PM","invest","Reel","1% per month. That's it.",
   "You don't need millions to own in Dubai.",
   "Flexible payment plans on Pantheon homes mean you can start with a fraction and grow into ownership.\\n\\nOne number changes the whole conversation. 👇\\n\\nComment \\\"PLAN\\\" for your options.",
   "#DubaiInvestment #OffPlanDubai #PaymentPlan "+T,"Comment \"PLAN\"",
   "Samana-style single-number reel. Big animated counter, lifestyle b-roll underneath.",
   "0:00 '1%' fills screen · 0:05 what it means text · 0:12 home b-roll · 0:22 DM CTA.",
   refs("investment"),"Story: countdown to a 'plan webinar' or DM-day + link sticker.",boost=True),
 P("Jul 24","Thu","6:00 PM","lifestyle","Reel","Amenities that earn the address",
   "A home is the building. This is the lifestyle.",
   "Infinity edge. Wellness floor. Sky lounge. The parts of Pantheon living you feel before you see.\\n\\nWhich one would you use first? 👇",
   "#LuxuryHomesDubai #DubaiLifestyle #MaisonElysee "+T,"Comment below",
   "Rapid amenity cuts, one per beat, biggest reveal on the drop. Electronic track.",
   "0:00 pool edge + text · per-beat amenity cuts · 0:24 hero amenity on drop · 0:30 question CTA.",
   refs("amenities"),"Story: slider 'Rate this rooftop' on the hero amenity."),
 P("Jul 26","Sat","11:00 AM","community","Static","Weekend market quote card",
   "Save this before Monday.",
   "\\\"In Dubai, the best time to buy was yesterday. The second-best time is before the next launch.\\\"\\n\\nSave this as your reminder. Then comment \\\"START\\\" and we'll send you where to begin. 👇",
   "#DubaiRealEstate #DubaiInvestment #MaisonElysee "+T,"Comment \"START\" + Save",
   "Quote-card static. Big serif quote, navy bg, thin gold rule, handle bottom. Built to be saved & reshared.",
   "Static design layout — Quote centered (2 lines max). Top-left small logo. Bottom: attribution + @handle. Keep negative space generous.",
   [],"Story: reshare the quote with an 'Agree?' poll."),
 P("Jul 30","Wed","3:00 PM","project","Carousel","Maison Elysée I & II — full tour",
   "Everything you need to decide, in one swipe.",
   "Maison Elysée I & II — floor plans, finishes, amenities and pricing, all in one place.\\n\\nSwipe through, then comment the unit type you want.\\n\\n📍 JVC, Dubai.",
   "#MaisonElysee #JVCDubai #DubaiProperty "+T,"Comment your unit type",
   "Premium render carousel. Consistent gold framing, project name on every slide, scroll-stopping hero first.",
   ["Slide 1 — HERO: aerial render of Maison Elysée I & II + 'The full tour →'",
    "Slide 2 — LOBBY: arrival/lobby render + one line on the design language",
    "Slide 3 — UNIT: living space render + sizes (studio / 1BHK / 2BHK)",
    "Slide 4 — AMENITIES: pool / gym / lounge grid (4 thumbnails)",
    "Slide 5 — FLOOR PLAN: a clean plan with key dimensions",
    "Slide 6 — PRICE + CTA: 'Starting from AED __' + 'Comment your unit type'"],
   refs("interior","amenities"),"Story: 'Which floor plan fits you?' poll linking to the carousel.",peak=True),
 # ---------- AUGUST
 P("Aug 4","Mon","7:00 PM","lifestyle","Reel","Sunset from Elysée Heights",
   "The view you'd never scroll past in real life.",
   "Golden hour hits different from up here.\\n\\nElysée Heights — where the skyline becomes your evening routine.\\n\\nSave it. 🌇",
   "#ElyseeHeights #DubaiSkyline #LuxuryHomesDubai "+T,"Save + DM \"HEIGHTS\"",
   "Single hero golden-hour shot held long, subtle parallax. Less is more.",
   "0:00 silhouette + text · 0:10 slow reveal of view · 0:24 logo + save CTA.",
   refs("lifestyle"),"Mon story: poll 'Sunrise or sunset balcony?'"),
 P("Aug 6","Wed","3:00 PM","project","Reel","Maison Elysée III — the reveal",
   "The trilogy completes.",
   "Maison Elysée III. The most refined chapter yet — same JVC address, elevated everything.\\n\\nFirst look, first access.\\n\\nComment \\\"III\\\" for the launch list.",
   "#MaisonElysee #JVCDubai #NewLaunch "+T,"Comment \"III\"",
   "Cinematic dark→light reveal, position as the premium finale of the line. This kicks off the 10-day countdown campaign.",
   "0:00 detail + text · 0:06 push-in · 0:14 full reveal on swell · 0:38 logo + CTA.",
   refs("reveal"),"Launch countdown begins — Day 1 of the 8-frame launch story sequence.",peak=True,boost=True),
 P("Aug 8","Fri","3:00 PM","community","Reel","Why our brokers keep coming back",
   "Don't take our word for it.",
   "The agents who sell Dubai every day choose to sell Pantheon. Here's why, in their words.\\n\\nTag a broker who should see this. 🤝",
   "#DubaiBrokers #DubaiRealEstate #PantheonDevelopment "+T,"Tag a broker",
   "Rapid broker testimonial compilation, multiple faces, fast cuts. Film several in one day.",
   "0:00 broker hook · rapid quotes · 0:26 logo + tag CTA.",
   refs("ugc"),"Story: launch the Broker Referral Leaderboard with a 'Join' link sticker."),
 P("Aug 12","Tue","1:00 PM","invest","Carousel","Rent vs buy in JVC — the real math",
   "You've paid someone else's mortgage long enough.",
   "5 years of JVC rent vs 5 years owning a Pantheon home. The gap is bigger than you think.\\n\\nSwipe, then comment \\\"MATH\\\" for your personalised breakdown.",
   "#JVCDubai #RentVsBuy #DubaiInvestment "+T,"Comment \"MATH\"",
   "Split comparison carousel — red (rent) vs gold (own). Clean finance design, end on the 5-year delta.",
   ["Slide 1 — HOOK: 'You've paid someone else's mortgage long enough.'",
    "Slide 2 — RENT: 5 yrs of JVC rent = AED __ gone, nothing owned (red)",
    "Slide 3 — BUY: 5 yrs on a Pantheon plan = equity + an asset (gold)",
    "Slide 4 — DELTA: side-by-side end position, the gap circled",
    "Slide 5 — HOW: the entry payment that makes it possible",
    "Slide 6 — CTA: 'Comment MATH for your own breakdown'"],
   refs("investment"),"Story: 'Rent or own right now?' poll → DM the math to 'own' voters."),
 P("Aug 15","Fri","3:00 PM","community","Reel","Creator tours ONE RAK CENTRAL (IG Collab)",
   "Is RAK actually worth it? Let's find out.",
   "We took a creator to Ras Al Khaimah to pressure-test the hype around ONE RAK CENTRAL.\\n\\nHonest verdict inside.\\n\\nTag your investment buddy. 👇",
   "#OneRAKCentral #RasAlKhaimah #RAKRealEstate "+T,"Tag a friend",
   "Creator-led, on-location. Post as IG Collab with the creator + a RAK travel page if possible.",
   "0:00 creator skeptical hook · 0:06 arrival · 0:18 the case for RAK · 0:30 verdict + CTA.",
   refs("ugc","reveal"),"Story: reshare creator's POV + 'Would you invest in RAK?' poll.",collab="@creator (IG Collab)",boost=True),
 P("Aug 16","Sat","11:00 AM","delivery","Reel","VOXA breaks ground",
   "From render to reality.",
   "VOXA is no longer a render. Ground broken, momentum building in JVT.\\n\\nWe'll show you every floor as it rises.\\n\\nComment \\\"VOXA\\\" to follow the build.",
   "#VOXA #JVTDubai #DubaiConstruction "+T,"Comment \"VOXA\"",
   "Site reveal + drone, energetic. Anchor the render-to-reality promise with a match-cut.",
   "0:00 drone over site + text · 0:08 ground works · 0:18 render overlay match-cut · 0:24 CTA.",
   refs("construction","reveal"),"Story: countdown to the next VOXA milestone reveal."),
 P("Aug 20","Wed","3:00 PM","project","Reel","Inside a Pantheon penthouse",
   "Most people never see the top floor.",
   "Four bedrooms in the sky, wrap-around views, finishes you feel.\\n\\nThis is the Pantheon penthouse most buyers don't know exists.\\n\\nComment \\\"PENTHOUSE\\\" for availability.",
   "#DubaiPenthouse #LuxuryHomesDubai #VOXA "+T,"Comment \"PENTHOUSE\"",
   "One continuous gimbal move through the penthouse, no cuts — flex the space.",
   "0:00 door opens POV + text · continuous glide · 0:26 view reveal + CTA.",
   refs("interior","amenities"),"Story: slider 'Rate this view' + link to availability.",peak=True,boost=True),
 P("Aug 23","Sat","11:00 AM","community","Static","Tag-a-friend challenge card",
   "Which Pantheon home is your friend?",
   "Studio minimalist or penthouse maximalist? 😅\\n\\nTag the friend who's the complete opposite of you — let's settle it in the comments.",
   "#DubaiRealEstate #MaisonElysee #VOXA "+T,"Tag a friend",
   "Playful A vs B static. Left half minimalist studio, right half bold penthouse, 'Which are you?' center.",
   "Static design layout — split 50/50 panel, label each side, big center question, handle bottom. Comment-bait by design.",
   [],"Story: run it as an A/B poll for 24h, reveal the winner."),
 P("Aug 27","Wed","3:00 PM","project","Carousel","Elysée Heights — pick your floor",
   "The higher you go, the rarer it gets.",
   "Elysée Heights — view tiers, unit types, and what's still available by floor.\\n\\nSwipe, then comment the floor you want before it's gone.",
   "#ElyseeHeights #DubaiProperty #OffPlanDubai "+T,"Comment your floor",
   "Render carousel with a scarcity angle. Use a 'selling fast' tag on limited tiers.",
   ["Slide 1 — HERO: tower render + 'Pick your floor →'",
    "Slide 2 — LOW TIER: garden/city view units + price band",
    "Slide 3 — MID TIER: skyline view units + price band",
    "Slide 4 — TOP TIER: penthouse/sky units ('limited')",
    "Slide 5 — VIEW COMPARISON: same window, 3 heights",
    "Slide 6 — CTA: 'Comment your floor before it's gone'"],
   refs("amenities","interior"),"Story: 'Which floor?' poll across the three tiers.",peak=True),
 P("Aug 29","Fri","3:00 PM","community","Reel","48 hours of Pantheon (BTS)",
   "What actually goes into one launch.",
   "Site visits, shoots, render reviews, broker calls — two days behind Pantheon in one reel.\\n\\nThe work behind the homes. 🤍",
   "#BehindTheScenes #PantheonDevelopment #DubaiRealEstate "+T,"Follow for more",
   "Fast BTS montage, real team, energetic. Humanises the brand.",
   "0:00 'a launch takes...' text · rapid BTS cuts · 0:26 logo + follow CTA.",
   refs("ugc","construction"),"Story: 'Ask the team anything' questions sticker (becomes next week's content)."),
 # ---------- SEPTEMBER
 P("Sep 1","Mon","7:00 PM","lifestyle","Reel","September in your Pantheon home",
   "New season. New address.",
   "Cooler evenings, longer balcony nights, the city coming back to life.\\n\\nThis is the season Dubai feels like home — make it yours.\\n\\nSave for later. 🍂",
   "#DubaiLifestyle #MaisonElysee #LuxuryHomesDubai "+T,"Save + DM",
   "Seasonal mood reel, warm grade, lifestyle b-roll across projects.",
   "0:00 season text · lifestyle cuts · 0:26 save CTA.",
   refs("lifestyle","interior"),"Story: poll 'Ready to move this season?'"),
 P("Sep 3","Wed","3:00 PM","project","Reel","VOXA — full building reveal",
   "The one everyone in JVT is talking about.",
   "VOXA, head to toe. Architecture, amenities, the address — the complete reveal.\\n\\nThis is the JVT landmark.\\n\\nComment \\\"VOXA\\\" for the investor deck.",
   "#VOXA #JVTDubai #DubaiProperty "+T,"Comment \"VOXA\"",
   "Flagship cinematic hero film — your highest-production reel of the quarter.",
   "0:00 detail + text · 0:08 exterior on swell · 0:18 amenity montage · 0:30 unit · 0:38 logo + CTA.",
   refs("reveal","launch"),"Story sequence: full 8-frame launch set for VOXA.",peak=True,boost=True),
 P("Sep 5","Fri","3:00 PM","community","Reel","Owner story — 6 months in",
   "We checked back in after handover.",
   "Six months living in a Pantheon home — what changed, what they'd tell a buyer today.\\n\\nReal, unfiltered.\\n\\nComment \\\"PANTHEON\\\" to start yours.",
   "#PantheonDevelopment #DubaiRealEstate #OwnerStory "+T,"Comment \"PANTHEON\"",
   "Calm mini-doc, real owner at home. Authentic > polished.",
   "0:00 owner hook · 0:08 home life b-roll · 0:18 their advice · 0:28 CTA.",
   refs("ugc","interior"),"Story: reshare owner clip + 'Ask an owner' questions sticker."),
 P("Sep 9","Tue","1:00 PM","invest","Carousel","Golden Visa through property",
   "Your home can also be your residency.",
   "A AED 2M Pantheon home can qualify you for the UAE Golden Visa. Here's exactly how it works.\\n\\nSwipe, then comment \\\"VISA\\\" for the eligible units.",
   "#GoldenVisa #DubaiInvestment #OffPlanDubai "+T,"Comment \"VISA\"",
   "Authority carousel, clean infographic. One step per slide, cite official thresholds, professional gold-on-navy.",
   ["Slide 1 — HOOK: 'Your home can also be your 10-year residency.'",
    "Slide 2 — THRESHOLD: AED 2M property = Golden Visa eligibility",
    "Slide 3 — BENEFITS: 10-yr renewable, sponsor family, no local sponsor (3 icons)",
    "Slide 4 — STEP-BY-STEP: buy → valuation → application → visa (4 steps)",
    "Slide 5 — ELIGIBLE: which Pantheon units cross AED 2M",
    "Slide 6 — CTA: 'Comment VISA for the eligible-unit list'"],
   refs("investment"),"Story: quiz 'What property value unlocks the Golden Visa?' → reveal AED 2M."),
 P("Sep 10","Wed","3:00 PM","project","Reel","Maison Elysée III — last release",
   "Final units. Then it's a memory.",
   "The last release of Maison Elysée III is live. Once these are gone, the trilogy is closed.\\n\\nComment \\\"III\\\" before the final units sell.",
   "#MaisonElysee #JVCDubai #LastUnits "+T,"Comment \"III\"",
   "Scarcity-driven reveal, countdown energy. Urgency without gimmicks.",
   "0:00 'final units' text · 0:06 reveal · 0:18 unit highlights · 0:30 urgent CTA.",
   refs("reveal","interior"),"Story: countdown to 'final units close' + DM link.",peak=True,boost=True),
 P("Sep 13","Sat","11:00 AM","delivery","Reel","ONE RAK CENTRAL — site progress",
   "RAK is moving fast. So are we.",
   "Latest from ONE RAK CENTRAL — real progress on the ground in Ras Al Khaimah.\\n\\nComment \\\"RAK\\\" for the delivery timeline.",
   "#OneRAKCentral #RasAlKhaimah #DubaiConstruction "+T,"Comment \"RAK\"",
   "Drone + timelapse with % overlay. Reinforce the delivery-trust theme.",
   "0:00 aerial + % · 0:08 site works · 0:18 timeline card + CTA.",
   refs("construction"),"Story: progress % graphic + countdown to next milestone."),
 P("Sep 16","Tue","1:00 PM","invest","Static","Q3 Dubai market snapshot",
   "Save this if you're buying this year.",
   "Dubai Q3 in three numbers: transactions, average price growth, and JVC/RAK demand.\\n\\nThe market is telling you something. Save this, then comment \\\"REPORT\\\" for the full breakdown. 📊",
   "#DubaiRealEstate #DubaiMarket #DubaiInvestment "+T,"Comment \"REPORT\" + Save",
   "Static data-snapshot graphic. 3 big numbers, source line (DLD/Bayut), gold-on-navy, ultra-saveable.",
   "Static design layout — 3 stat blocks stacked, each a big number + one label. Header 'Dubai · Q3 2026'. Footer: source + @handle.",
   [],"Story: quiz on one of the three stats, reveal the answer."),
 P("Sep 17","Wed","3:00 PM","project","Reel","The Pantheon portfolio in 30s",
   "Five projects. Two emirates. One standard.",
   "VOXA. ONE RAK CENTRAL. Maison Elysée I, II & III. Elysée Heights.\\n\\nEverything we're building, in 30 seconds.\\n\\nComment \\\"PORTFOLIO\\\" for the full deck.",
   "#PantheonDevelopment #DubaiRealEstate #RAKRealEstate "+T,"Comment \"PORTFOLIO\"",
   "Fast portfolio montage, one project per beat, unified gold grade across mixed footage.",
   "0:00 'five projects' text · per-beat project cuts · 0:26 logo + CTA.",
   refs("reveal","amenities"),"Story: 'Which project should we tour next?' poll across the five.",peak=True),
 P("Sep 19","Fri","3:00 PM","community","Reel","You tagged us — we're resharing",
   "Our community said it better than we could.",
   "The best Pantheon content this month came from you.\\n\\nKeep tagging @pantheon_development — you might be next. 🤍",
   "#PantheonCommunity #DubaiRealEstate #MaisonElysee "+T,"Tag us in yours",
   "UGC repost montage, credit every creator on-screen. Encourages more UGC.",
   "0:00 'you posted...' text · UGC clips with @handles · 0:26 tag CTA.",
   refs("ugc"),"Story: 'Add yours' UGC sticker + reshare the best entries."),
 P("Sep 24","Wed","3:00 PM","project","Reel","Why buyers choose Pantheon",
   "Same budget. Different developer. Here's the difference.",
   "On-time delivery, real amenities, JVC & RAK locations, plans that work for investors.\\n\\nThis is why the smart money picks Pantheon.\\n\\nComment \\\"WHY\\\" for the comparison.",
   "#PantheonDevelopment #DubaiInvestment #OffPlanDubai "+T,"Comment \"WHY\"",
   "Confident value reel, text-driven over hero b-roll. Position vs the market without naming rivals.",
   "0:00 'same budget...' hook · point-by-point text over b-roll · 0:30 CTA.",
   refs("interior","amenities"),"Story: 'What matters most when you buy?' poll (delivery / location / price).",peak=True,boost=True),
 P("Sep 27","Sat","11:00 AM","delivery","Reel","Q3 in review — what we delivered",
   "A quarter of receipts.",
   "Launches, ground-breakings, handovers and a community that grew with us. Thank you for an unreal Q3.\\n\\nQ4 is bigger. Comment \\\"PANTHEON\\\" to be part of it.",
   "#PantheonDevelopment #DubaiRealEstate #Q3Review "+T,"Comment \"PANTHEON\"",
   "Quarterly recap montage, uplifting. Consistent LUT across all the quarter's footage.",
   "0:00 'Q3...' text · best moments montage · 0:26 thank-you + CTA.",
   refs("launch","ugc"),"Story: giveaway finale — 'Win a staycation' draw goes live."),
 # ================= ADDITIONAL POSTS — full quarterly volume per the strategy (34 Reels · 20 Carousels · 12 Statics) =================
 # ---------- JULY (fills to 12 Reels · 6 Carousels · 4 Statics)
 P("Jul 1","Tue","1:00 PM","invest","Carousel","VOXA payment plan, decoded",
   "AED 800M landmark — and you can start with a fraction.",
   "Everyone asks about VOXA pricing. Here's the actual payment structure — booking, construction milestones, handover.\\n\\nSwipe through, then comment \\\"VOXA\\\" for the full plan PDF.",
   "#VOXA #JVTDubai #PaymentPlan "+T,"Comment \"VOXA\"",
   "Dark luxury data carousel. Gold accents, one milestone per slide, @handle footer on every slide.",
   ["Slide 1 — HOOK: 'AED 800M landmark. Start with a fraction.'",
    "Slide 2 — BOOKING: down-payment % to reserve a unit",
    "Slide 3 — DURING BUILD: instalments mapped to construction stages",
    "Slide 4 — HANDOVER: balance on completion + what you own",
    "Slide 5 — UNIT BANDS: studio / 1BHK / 2BHK / penthouse entry prices",
    "Slide 6 — CTA: 'Comment VOXA for the full payment plan'"],
   [],"Story: quiz 'Guess VOXA's booking %' → reveal → link to plan."),
 P("Jul 7","Mon","7:00 PM","lifestyle","Reel","A day in JVT",
   "The community everyone underestimates.",
   "Cafés, parks, the school run, sunset padel — JVT is quietly one of Dubai's best places to actually live.\\n\\nThis is the neighbourhood VOXA calls home.\\n\\nSave it. 🌳",
   "#JVTDubai #JumeirahVillageTriangle #DubaiLifestyle "+T,"Save + DM \"JVT\"",
   "Golden-hour day-in-the-life montage across JVT. Warm grade, real people, one continuous energy.",
   "0:00 morning café POV + text · 0:08 park / families · 0:16 sunset padel · 0:24 VOXA exterior tie-in + save CTA.",
   [],"Story: poll 'JVT or JVC?' → segments buyers."),
 P("Jul 9","Wed","3:00 PM","project","Carousel","VOXA — floor plans & unit mix",
   "Find your exact unit.",
   "Studios to 4-bed penthouses — every VOXA layout, sizes and orientations in one swipe.\\n\\nComment the unit type you want and we'll send the floor plan.\\n\\n📍 JVT.",
   "#VOXA #JVTDubai #FloorPlans "+T,"Comment your unit type",
   "Premium plan carousel. Clean line-drawing plans on navy, VOXA name + @handle every slide.",
   ["Slide 1 — HERO: VOXA tower render + 'Find your floor plan →'",
    "Slide 2 — STUDIO: plan + size + ideal-for line",
    "Slide 3 — 1 BHK: plan + size + balcony orientation",
    "Slide 4 — 2 BHK: plan + size + view notes",
    "Slide 5 — PENTHOUSE: 3–4 bed sky units + features",
    "Slide 6 — CTA: 'Comment your unit type for the plan'"],
   [],"Story: 'Which layout fits you?' poll across unit types."),
 P("Jul 10","Thu","6:00 PM","delivery","Reel","Maison Elysée — quality you can't see",
   "The details buyers never check. We obsess over them.",
   "Waterproofing, MEP first-fix, acoustic insulation — the work that decides how a home feels in year five, not month one.\\n\\nThis is delivery, done right.\\n\\nComment \\\"BUILD\\\" to follow the process.",
   "#DubaiConstruction #QualityCheck #MaisonElysee "+T,"Comment \"BUILD\"",
   "Engineer-led site reel, hard-hat POV, hand-on-material close-ups. Trust over polish.",
   "0:00 engineer hook + text · 0:08 material close-ups · 0:18 quality-check moment · 0:26 progress card + CTA.",
   [],"Story: 'Ask our site engineer anything' questions sticker."),
 P("Jul 14","Mon","7:00 PM","community","Static","Meet the architect behind Maison Elysée",
   "Every home starts as one person's obsession.",
   "Meet the mind behind Maison Elysée's French-inspired lines. We asked what 'home' means to the person who drew yours.\\n\\nFollow to meet the whole team. 🤍",
   "#PantheonPeople #DubaiArchitecture #MaisonElysee "+T,"Follow for more",
   "Portrait-led people static. B&W portrait, gold pull-quote, navy footer with name + role.",
   "Static design layout — portrait left, pull-quote right ('We design for the morning, not the brochure'), name + role bottom, @handle footer. 1080×1350.",
   [],"Story: reshare with 'Ask the architect' questions sticker."),
 P("Jul 17","Thu","6:00 PM","invest","Carousel","JVC vs Downtown — where the smart money goes",
   "Same budget. Very different returns.",
   "Price per sqft, rental yield, entry point — JVC vs Downtown, side by side.\\n\\nThe answer surprises most buyers. Swipe, then comment \\\"COMPARE\\\".",
   "#JVCDubai #DubaiInvestment #DowntownDubai "+T,"Comment \"COMPARE\"",
   "Two-column comparison carousel. JVC gold, Downtown grey, one metric per slide.",
   ["Slide 1 — HOOK: 'Same budget. Different return.'",
    "Slide 2 — PRICE/SQFT: JVC vs Downtown (bars)",
    "Slide 3 — YIELD: JVC ≈ 7–8% vs Downtown ≈ 5%",
    "Slide 4 — ENTRY: what AED 1M buys in each",
    "Slide 5 — VERDICT: why end-users + investors pick JVC now",
    "Slide 6 — CTA: 'Comment COMPARE for the full data'"],
   [],"Story: quiz 'Which yields more — JVC or Downtown?'"),
 P("Jul 21","Mon","7:00 PM","community","Reel","Broker first-access preview — VOXA",
   "Our brokers saw it before the public did.",
   "We opened VOXA to our broker partners first — first picks, first plans, first commissions.\\n\\nIf you sell Dubai, you want this inventory.\\n\\nComment \\\"BROKER\\\" to join the partner list.",
   "#DubaiBrokers #VOXA #RealEstateAgents "+T,"Comment \"BROKER\"",
   "Event-style broker preview reel, handshake energy, room full of agents, fast cuts.",
   "0:00 'first access' text · 0:06 brokers viewing models · 0:16 plans handed over · 0:26 join CTA.",
   [],"Story: broker leaderboard teaser + 'Join' link sticker."),
 P("Jul 23","Wed","3:00 PM","project","Carousel","VOXA — the amenity deck",
   "Eight floors of reasons to never leave.",
   "Pool, wellness floor, co-working, padel, kids' zone — VOXA's full amenity stack in one swipe.\\n\\nWhich one sells it for you? Comment below.\\n\\n📍 JVT.",
   "#VOXA #DubaiAmenities #JVTDubai "+T,"Comment your favourite",
   "Render carousel, one amenity per slide, consistent gold label chips, VOXA footer.",
   ["Slide 1 — HERO: amenity-floor render + 'Eight floors of lifestyle →'",
    "Slide 2 — POOL & DECK render",
    "Slide 3 — WELLNESS / GYM render",
    "Slide 4 — CO-WORKING / LOUNGE render",
    "Slide 5 — PADEL / KIDS / OUTDOOR render",
    "Slide 6 — CTA: 'Comment your favourite amenity'"],
   [],"Story: slider 'Rate the rooftop pool'."),
 P("Jul 25","Fri","3:00 PM","lifestyle","Reel","Weekend, reset",
   "Your Friday could look like this.",
   "Slow coffee, rooftop laps, friends over as the sun drops. The Pantheon weekend.\\n\\nSave this for the life you're building toward.\\n\\nDM \\\"WEEKEND\\\" to see the homes.",
   "#DubaiWeekend #LuxuryHomesDubai #MaisonElysee "+T,"Save + DM \"WEEKEND\"",
   "Aspirational weekend montage, warm golden grade, lifestyle tension before address reveal.",
   "0:00 coffee POV + text · 0:08 rooftop laps · 0:16 friends / sunset · 0:24 address reveal + save CTA.",
   [],"Story: 'Rate this Friday' emoji slider."),
 P("Jul 29","Tue","1:00 PM","invest","Static","Why Dubai, why now — 3 signals",
   "The window is open. Here's the proof.",
   "Population growth, golden-visa demand, limited prime supply. Three signals that explain why 2026 is a buyer's year.\\n\\nSave this. Comment \\\"WHY\\\" for the full brief. 📊",
   "#DubaiRealEstate #DubaiInvestment #WhyDubai "+T,"Comment \"WHY\" + Save",
   "Data static, 3 stacked signal blocks, source line, gold-on-navy, ultra-saveable.",
   "Static design layout — 3 signal blocks (population / visa demand / supply), each a big number + one line. Header 'Why Dubai · 2026'. Footer: source + @handle.",
   [],"Story: quiz on one signal, reveal the number."),
 # ---------- AUGUST (fills to 10 Reels · 8 Carousels · 4 Statics)
 P("Aug 1","Fri","3:00 PM","project","Carousel","Maison Elysée III — first look specs",
   "The finale is coming.",
   "Maison Elysée III — the specs that matter before launch. Same JVC address, elevated everything.\\n\\nSwipe, then comment \\\"III\\\" to join the launch list.",
   "#MaisonElysee #JVCDubai #NewLaunch "+T,"Comment \"III\"",
   "Teaser spec carousel, withhold the hero render, gold-on-navy, build anticipation.",
   ["Slide 1 — HOOK: 'The trilogy completes →' (blurred render)",
    "Slide 2 — POSITION: how III elevates I & II",
    "Slide 3 — UNIT MIX: studios → 2-bed + sky units",
    "Slide 4 — DESIGN: French-inspired language, finishes",
    "Slide 5 — LAUNCH: date + first-access mechanic",
    "Slide 6 — CTA: 'Comment III for the launch list'"],
   [],"Launch countdown — Day 1 teaser frame.",boost=True),
 P("Aug 5","Tue","1:00 PM","invest","Carousel","Maison Elysée III — the investor case",
   "Run the numbers before the launch crowd does.",
   "Entry price, payment plan, projected yield and exit options for Maison Elysée III.\\n\\nSwipe, then comment \\\"NUMBERS\\\" for the investor sheet.",
   "#MaisonElysee #DubaiInvestment #PaymentPlan "+T,"Comment \"NUMBERS\"",
   "Investor data carousel, one metric per slide, gold accents, @handle footer.",
   ["Slide 1 — HOOK: 'The investor case for Elysée III'",
    "Slide 2 — ENTRY: starting price + booking %",
    "Slide 3 — PLAN: milestone instalments to handover",
    "Slide 4 — YIELD: projected JVC rental return",
    "Slide 5 — UPSIDE: trilogy track record on resale",
    "Slide 6 — CTA: 'Comment NUMBERS for the sheet'"],
   [],"Story: quiz 'Projected JVC yield?' reveal."),
 P("Aug 7","Thu","6:00 PM","lifestyle","Reel","Evening in Maison Elysée",
   "The hour the home earns its name.",
   "Warm light, the city humming below, dinner on the balcony. Evenings in Maison Elysée.\\n\\nSave it for the life you're working toward. 🌆",
   "#MaisonElysee #JVCDubai #DubaiLifestyle "+T,"Save + DM \"ELYSEE\"",
   "Warm evening POV glide, champagne grade, soft trending audio.",
   "0:00 dusk window POV + text · 0:08 interior warm light · 0:16 balcony dinner · 0:26 save CTA.",
   [],"Story: 'Sunrise or sunset balcony?' poll."),
 P("Aug 11","Mon","7:00 PM","project","Carousel","Maison Elysée III — unit types",
   "Pick the one that's yours.",
   "Every Maison Elysée III layout — sizes, orientations and who each suits.\\n\\nComment your unit type and we'll send the plan before launch.",
   "#MaisonElysee #FloorPlans #JVCDubai "+T,"Comment your unit type",
   "Clean plan carousel, navy line-drawings, gold labels, project footer.",
   ["Slide 1 — HERO: III render + 'Find your layout →'",
    "Slide 2 — STUDIO: plan + ideal-for",
    "Slide 3 — 1 BHK: plan + balcony note",
    "Slide 4 — 2 BHK: plan + view note",
    "Slide 5 — SKY UNIT: premium layout + features",
    "Slide 6 — CTA: 'Comment your unit type'"],
   [],"Story: 'Which layout?' poll."),
 P("Aug 13","Wed","3:00 PM","community","Static","Maison Elysée III — 48 hours to launch",
   "Set your reminder.",
   "Maison Elysée III opens in 48 hours. First access, best units, launch-day pricing.\\n\\nComment \\\"III\\\" and we'll DM you the moment it's live. ⏳",
   "#MaisonElysee #NewLaunch #JVCDubai "+T,"Comment \"III\"",
   "Countdown occasion static, big '48 HOURS', render backdrop dimmed, gold timer motif.",
   "Static design layout — '48 HOURS' centered, project name above, 'Comment III' CTA below, @handle footer. 1080×1350.",
   [],"Story: countdown sticker to launch hour."),
 P("Aug 14","Thu","6:00 PM","project","Reel","Maison Elysée III — amenity walkthrough",
   "Step inside before anyone else.",
   "A first walk through Maison Elysée III's amenities — pool, lounge, wellness, the lobby that sets the tone.\\n\\nComment \\\"III\\\" for the full deck.",
   "#MaisonElysee #DubaiAmenities #JVCDubai "+T,"Comment \"III\"",
   "Continuous gimbal amenity glide, premium grade, one flowing move.",
   "0:00 lobby POV + text · 0:08 pool deck · 0:16 wellness/lounge · 0:26 logo + CTA.",
   [],"Story: slider 'Rate the lobby'."),
 P("Aug 18","Mon","7:00 PM","invest","Carousel","Maison Elysée III — ROI projection",
   "What AED 1M could become.",
   "A 5-year projection on a Maison Elysée III unit — rent, appreciation, total position.\\n\\nSwipe, then comment \\\"ROI\\\" for your personalised model.",
   "#MaisonElysee #DubaiInvestment #ROI "+T,"Comment \"ROI\"",
   "Projection carousel, animated-style number reveals, gold growth curve.",
   ["Slide 1 — HOOK: 'AED 1M today → ? in 5 years'",
    "Slide 2 — RENT: annual yield stacked over 5 yrs",
    "Slide 3 — APPRECIATION: JVC trend applied",
    "Slide 4 — TOTAL: combined 5-year position",
    "Slide 5 — ASSUMPTIONS: sourced + conservative",
    "Slide 6 — CTA: 'Comment ROI for your model'"],
   [],"Story: 'Guess the 5-yr total' quiz."),
 P("Aug 19","Tue","1:00 PM","invest","Static","Launch day — Maison Elysée III price reveal",
   "It's live.",
   "Maison Elysée III is officially open. Starting prices, payment plan, first-access units — all live now.\\n\\nComment \\\"III\\\" and we'll send everything. 🔑",
   "#MaisonElysee #NewLaunch #JVCDubai "+T,"Comment \"III\"",
   "Launch-day price static, 'STARTING FROM AED __' hero, render backdrop, gold seal.",
   "Static design layout — 'NOW LIVE' tag, 'Starting from AED __' hero number, project name, CTA, @handle footer. 1080×1350.",
   [],"Story: launch-day live + link sticker.",boost=True),
 P("Aug 21","Thu","6:00 PM","project","Carousel","Maison Elysée III — floor plans",
   "The plans, before they're gone.",
   "Detailed Maison Elysée III floor plans with dimensions and orientations.\\n\\nComment the unit you want — first-access buyers get first pick.",
   "#MaisonElysee #FloorPlans #OffPlanDubai "+T,"Comment your floor",
   "Plan carousel, clean dimensions, navy + gold, project footer.",
   ["Slide 1 — HERO: 'The floor plans →'",
    "Slide 2 — STUDIO plan + dimensions",
    "Slide 3 — 1 BHK plan + dimensions",
    "Slide 4 — 2 BHK plan + dimensions",
    "Slide 5 — SKY UNIT plan + dimensions",
    "Slide 6 — CTA: 'Comment the unit you want'"],
   [],"Story: 'Which plan fits you?' poll."),
 P("Aug 25","Mon","7:00 PM","community","Reel","The night Maison Elysée III launched",
   "You showed up. All of you.",
   "Launch night recap — the room, the energy, the units that moved in hours.\\n\\nThank you for making Maison Elysée III the fastest yet. 🤍\\n\\nComment \\\"NEXT\\\" for what's coming.",
   "#MaisonElysee #LaunchNight #DubaiRealEstate "+T,"Comment \"NEXT\"",
   "Event recap montage, crowd + stage + product, uplifting cut to music.",
   "0:00 'launch night' text · crowd + reveal montage · 0:20 sold tags · 0:26 thank-you + CTA.",
   [],"Story: reshare attendee tags + 'Add yours'.",boost=True),
 P("Aug 26","Tue","1:00 PM","delivery","Carousel","Elysée Heights — the build, milestone by milestone",
   "Promises are cheap. Receipts aren't.",
   "Where Elysée Heights stands today vs the plan — foundation to facade, milestone by milestone.\\n\\nComment \\\"TRACK\\\" for the live construction tracker.",
   "#ElyseeHeights #DubaiConstruction #Delivery "+T,"Comment \"TRACK\"",
   "Progress carousel, site photos + % bars per stage, trust-first design.",
   ["Slide 1 — HOOK: 'Built, not promised →'",
    "Slide 2 — FOUNDATION: stage % + photo",
    "Slide 3 — STRUCTURE: floors poured + photo",
    "Slide 4 — FACADE: cladding progress + photo",
    "Slide 5 — TIMELINE: handover quarter on track",
    "Slide 6 — CTA: 'Comment TRACK for live updates'"],
   [],"Story: progress % + countdown to next milestone."),
 P("Aug 28","Thu","6:00 PM","community","Static","Broker leaderboard — August",
   "These agents closed the most this month.",
   "Our top broker partners for August. Real referrals, real commissions, real recognition.\\n\\nWant your name here? Comment \\\"BROKER\\\" to join. 🏆",
   "#DubaiBrokers #RealEstateAgents #PantheonPartners "+T,"Comment \"BROKER\"",
   "Leaderboard static, gold podium 1-2-3, agency logos masked, prestige framing.",
   "Static design layout — 'August Top Brokers' header, 1/2/3 podium with names, prize-tier note, CTA + @handle footer. 1080×1350.",
   [],"Story: reshare winners + tag them."),
 # ---------- SEPTEMBER (fills to 12 Reels · 6 Carousels · 4 Statics)
 P("Sep 2","Tue","1:00 PM","invest","Carousel","RAK vs Dubai — the investor case",
   "The emirate everyone's about to discover.",
   "Entry price, yield, growth trajectory — Ras Al Khaimah vs Dubai, honestly compared.\\n\\nSwipe, then comment \\\"RAK\\\" for the ONE RAK CENTRAL brief.",
   "#OneRAKCentral #RasAlKhaimah #DubaiInvestment "+T,"Comment \"RAK\"",
   "Comparison carousel, RAK gold vs Dubai grey, one metric per slide.",
   ["Slide 1 — HOOK: 'RAK vs Dubai — the honest take'",
    "Slide 2 — ENTRY: price/sqft compared",
    "Slide 3 — YIELD: RAK upside vs mature Dubai",
    "Slide 4 — CATALYST: tourism + gaming + infrastructure",
    "Slide 5 — VERDICT: why RAK is the early entry",
    "Slide 6 — CTA: 'Comment RAK for the brief'"],
   [],"Story: 'Dubai or RAK?' poll."),
 P("Sep 4","Thu","6:00 PM","lifestyle","Reel","Waterfront mornings — ONE RAK CENTRAL",
   "Imagine this is your commute view.",
   "Sea air, island access, the pace a little slower — ONE RAK CENTRAL living.\\n\\nSave it. DM \\\"RAK\\\" to see the homes. 🌊",
   "#OneRAKCentral #RasAlKhaimah #WaterfrontLiving "+T,"Save + DM \"RAK\"",
   "Waterfront day-in-life reel, coastal grade, drone + POV blend.",
   "0:00 coastline POV + text · 0:08 marina / island · 0:16 home tie-in · 0:24 save CTA.",
   [],"Story: 'Rate this view' slider."),
 P("Sep 8","Mon","7:00 PM","project","Carousel","ONE RAK CENTRAL — the masterplan",
   "A destination, not just a tower.",
   "Retail, residences, waterfront, leisure — how ONE RAK CENTRAL fits together.\\n\\nSwipe the masterplan, then comment \\\"RAK\\\" for pricing.",
   "#OneRAKCentral #RasAlKhaimah #Masterplan "+T,"Comment \"RAK\"",
   "Masterplan carousel, aerial render + zone callouts, gold keylines.",
   ["Slide 1 — HERO: aerial masterplan render + 'The destination →'",
    "Slide 2 — RESIDENCES: tower + unit mix",
    "Slide 3 — RETAIL & DINING: ground-plane life",
    "Slide 4 — WATERFRONT: promenade + island access",
    "Slide 5 — CONNECTIVITY: location + drive times",
    "Slide 6 — CTA: 'Comment RAK for pricing'"],
   [],"Story: 'Which zone excites you?' poll."),
 P("Sep 11","Thu","6:00 PM","delivery","Static","Our delivery record",
   "Ask the only question that matters: do they deliver?",
   "Projects handed over, on-time rate, units delivered. The numbers behind the trust.\\n\\nSave this. Comment \\\"RECORD\\\" for the full track record. 🔑",
   "#Delivery #DubaiRealEstate #PantheonDevelopment "+T,"Comment \"RECORD\" + Save",
   "Trust static, 3 delivery numbers, gold-on-navy, source/disclaimer line.",
   "Static design layout — 3 stat blocks (handed over / on-time % / units delivered), header 'Our Record', footer @handle. 1080×1350.",
   [],"Story: quiz on the on-time %."),
 P("Sep 12","Fri","3:00 PM","invest","Carousel","5-year forecast — where JVC & RAK go next",
   "Buy where the line is still rising.",
   "A sober 5-year price + rent outlook for JVC and RAK, with the assumptions in plain sight.\\n\\nSwipe, then comment \\\"FORECAST\\\" for the model.",
   "#DubaiInvestment #JVCDubai #RasAlKhaimah "+T,"Comment \"FORECAST\"",
   "Forecast carousel, gold trend lines, conservative framing, sourced.",
   ["Slide 1 — HOOK: 'The next 5 years, soberly'",
    "Slide 2 — JVC: price trajectory + drivers",
    "Slide 3 — RAK: price trajectory + catalysts",
    "Slide 4 — RENT: yield outlook both markets",
    "Slide 5 — RISKS: honest counter-view",
    "Slide 6 — CTA: 'Comment FORECAST for the model'"],
   [],"Story: 'Which grows faster?' poll."),
 P("Sep 15","Mon","7:00 PM","community","Reel","The people who deliver",
   "Behind every handover is a team you never see.",
   "Site managers, engineers, the sales team, the CRM desk — the people who turn a render into your keys.\\n\\nFollow to meet them all. 🤍",
   "#PantheonPeople #DubaiRealEstate #BehindTheScenes "+T,"Follow for more",
   "Team montage reel, real faces, warm grade, human and proud.",
   "0:00 'who actually builds it' text · team cuts on site + office · 0:24 logo + follow CTA.",
   [],"Story: 'Ask the team anything'."),
 P("Sep 18","Thu","6:00 PM","project","Carousel","Elysée Heights — final availability",
   "What's left, before it's gone.",
   "Elysée Heights — the units, floors and views still available right now.\\n\\nComment the floor you want before it closes.",
   "#ElyseeHeights #DubaiProperty #LastUnits "+T,"Comment your floor",
   "Availability carousel, 'selling fast' tags, scarcity but tasteful.",
   ["Slide 1 — HERO: tower render + 'What's left →'",
    "Slide 2 — AVAILABLE LOW FLOORS + price band",
    "Slide 3 — MID FLOORS + view note ('limited')",
    "Slide 4 — TOP / SKY UNITS ('final few')",
    "Slide 5 — WHY NOW: handover near, price step coming",
    "Slide 6 — CTA: 'Comment your floor'"],
   [],"Story: 'Which floor?' poll across tiers."),
 P("Sep 22","Mon","7:00 PM","community","Static","Thank you — to our community",
   "We set out to reach more of you. You showed up.",
   "To everyone who followed, tagged, DM'd, visited and trusted us this quarter — thank you. This is your community as much as ours. 🤍\\n\\nComment \\\"PANTHEON\\\" to be part of what's next.",
   "#PantheonCommunity #DubaiRealEstate #ThankYou "+T,"Comment \"PANTHEON\"",
   "Gratitude static, warm gradient, big 'THANK YOU', subtle community photo grid backdrop.",
   "Static design layout — 'THANK YOU' hero, one warm line below, CTA + @handle footer, subtle community photo grid background. 1080×1350.",
   [],"Story: reshare community tags + 'Add yours'."),
 P("Sep 23","Tue","1:00 PM","invest","Carousel","Golden Visa — your eligible Pantheon units",
   "Residency and a home, in one decision.",
   "Which Pantheon units cross the AED 2M Golden Visa threshold — and exactly what you get.\\n\\nSwipe, then comment \\\"VISA\\\" for the eligible list.",
   "#GoldenVisa #DubaiInvestment #OffPlanDubai "+T,"Comment \"VISA\"",
   "Authority carousel, clean infographic, official thresholds, gold-on-navy.",
   ["Slide 1 — HOOK: 'A home that's also a 10-year visa'",
    "Slide 2 — THRESHOLD: AED 2M = eligibility",
    "Slide 3 — ELIGIBLE: VOXA penthouses + Elysée sky units",
    "Slide 4 — BENEFITS: 10-yr renewable, family sponsorship",
    "Slide 5 — PROCESS: buy → valuation → apply → visa",
    "Slide 6 — CTA: 'Comment VISA for the list'"],
   [],"Story: quiz 'Golden Visa threshold?' reveal AED 2M."),
 P("Sep 25","Thu","6:00 PM","project","Reel","ONE RAK CENTRAL — full reveal",
   "The landmark that puts RAK on the map.",
   "ONE RAK CENTRAL, head to toe — architecture, waterfront, the whole destination.\\n\\nThis is RAK's next icon.\\n\\nComment \\\"RAK\\\" for first-access pricing.",
   "#OneRAKCentral #RasAlKhaimah #RAKRealEstate "+T,"Comment \"RAK\"",
   "Flagship cinematic hero film for RAK, coastline drone → render reveal → amenity montage.",
   "0:00 coastline detail + text · 0:08 render reveal on swell · 0:18 amenity montage · 0:30 unit · 0:38 logo + CTA.",
   [],"Story: full 8-frame launch sequence for RAK.",peak=True,boost=True),
 P("Sep 29","Mon","7:00 PM","invest","Static","Q3 → Q4 — what's next",
   "Save this. The next quarter is bigger.",
   "What we delivered in Q3 and what's launching in Q4 — projects, milestones, the roadmap.\\n\\nComment \\\"Q4\\\" to get on every launch list early. 📅",
   "#PantheonDevelopment #DubaiRealEstate #Q4 "+T,"Comment \"Q4\"",
   "Roadmap static, timeline strip Q3→Q4, gold milestones, save-worthy.",
   "Static design layout — horizontal Q3→Q4 timeline, milestone dots labelled, header 'The Road Ahead', CTA + @handle footer. 1080×1350.",
   [],"Story: 'Which launch are you waiting for?' poll."),
]

# ---------------------------------------------------------------- UNIQUE REFERENCE REEL POOL (33 distinct real reels)
IG="https://www.instagram.com/reel/"
SO="https://www.instagram.com/sobharealty/reel/"
REELS=[
 ["Imtiaz — The Symphony reveal (Zaha Hadid)",IG+"DTCon67Ec55/","Dark→light sculptural render in motion, slow push-ins, one hero line of text."],
 ["Imtiaz — Symphony sculptural detail",IG+"DW30Aj1DAk6/","Architecture-in-motion close-ups; restrained text; let the form carry it."],
 ["Imtiaz — Symphony grand unveiling (arena)",IG+"DRNEsTHjwVR/","Event energy: crowd + stage + product, fast highlight montage on music."],
 ["Danube — The Big Reveal",IG+"DQ_F2UIklKN/","Teaser/curtain build-up — withhold, then drop the hero shot (render→reality match-cut)."],
 ["BNW — At FashionTV Acacia",IG+"DKwDhHBy6bt/","Aspirational POV, golden hour, lifestyle tension before the address reveal."],
 ["BNW — FashionTV turning heads",IG+"DNN90KSybpO/","Couture-styled framing + bold on-screen typography; portfolio-montage energy."],
 ["Samana — 8% ROI / 1% plan",IG+"C7DulWLpSNZ/","Bold number on frame 1, animated counters, ONE idea per post."],
 ["Danube — smart investment",IG+"DXpHL53isU9/","Lifestyle b-roll under a single clear ROI / payment message."],
 ["Danube — interior detailing",IG+"DSAk_6mkhH-/","Slow-mo close-ups of materials, warm grade, tactile sound design; calm home life."],
 ["Danube — effortless furnished living",IG+"DXqzr01CMwA/","One continuous gimbal move through the whole home, no cuts (morning-POV style)."],
 ["Danube — amenities showcase",IG+"DPN2O9SEYWN/","Rapid cuts, one amenity per beat, biggest reveal on the music drop."],
 ["DAMAC — townhouse amenities",IG+"DABad1SKTm7/","Bright family-lifestyle amenities, wide community shots, people in the space."],
 ["DAMAC — Islander lifestyle",IG+"DRMuCgkk3Mh/","Waterfront day-in-the-life storytelling; creator/location-led."],
 ["DAMAC — District lifestyle",IG+"DOQcQ3FExzZ/","'Where lifestyle meets' framing, playful day-in-life energy."],
 ["@mr.thank.you — Danube creator collab",IG+"DPgRGrCEwQI/","Creator face-to-camera hook; posted as an IG Native Collab to hit both audiences."],
 ["Dubai — construction timelapse",IG+"DSOQy5GiB4V/","Timelapse with progress %, before→now build — pure delivery trust."],
 ["Binghatti — Titania reveal",IG+"DP39hPfCIno/","Bold architectural reveal, signature facade as the hero."],
 ["Binghatti — Skyblade downtown icon",IG+"DOT4BvaEUsC/","Icon-in-skyline reveal, strong vertical emphasis."],
 ["Binghatti — Elite luxury living",IG+"DDlsqjsJ82n/","Refined interiors + luxury-living lifestyle (own-the-home aspiration)."],
 ["Binghatti — Skyblade future living",IG+"DOtMBuvk2LT/","Futuristic luxury with a scarcity / urgency tone."],
 ["Emaar — 418m² penthouse interior",IG+"DShstCgjVFz/","High-end interior design walkthrough; detail-led tour."],
 ["Emaar — Beachfront duplex penthouse",IG+"DLrcMBOx6o9/","View-led penthouse tour, premium finishes, continuous flow."],
 ["Emaar — brand film",IG+"DTe3rQHk94O/","Polished brand-grade b-roll with a unified colour grade."],
 ["Sobha — SkyVue sunset",IG+"DEFU8MNIySp/","Single hero sunset over the skyline, held long, subtle parallax."],
 ["Sobha — Dubai brand event",SO+"DC3ggLRpDW9/","Brand event recap: people + stage + prestige."],
 ["Sobha — first-time reveal",SO+"DG28sD9yISS/","'Presenting for the first time' reveal; anticipation build."],
 ["Sobha — exclusive luxury",IG+"DQWqmqSjpa7/","Exclusive luxury showcase, slow elegant cuts."],
 ["Sobha — event highlights",SO+"DF8BdBzSS4F/","Event highlight reel — energy, crowd, behind-the-scenes feel."],
 ["Sobha — SkyPark skyline living",IG+"DQWvatiEgkb/","Skyline-living tiers + view comparison by height."],
 ["Sobha — a new era (Abu Dhabi)",IG+"DYL0sWfMYm_/","Authority / era-defining reveal, confident grade."],
 ["Danube — luxury homes story",IG+"DRFdaougrO0/","Emotional luxury-home storytelling; warm, human."],
 ["Emaar — influencer penthouse tour",IG+"DWTyOociByt/","Influencer-led penthouse walkthrough; face + space."],
 ["@starlingproperties — DAMAC lifestyle pitch",IG.replace('/reel/','/starlingproperties/reel/')+"CzTXHvVyBW-/","Agent/broker-led lifestyle pitch, face-to-camera trust."],
]
# Assign a reference reel to each post (theme-tuned). 66 posts share a 33-reel pool,
# so each reel is used at most twice: the original 33 assignments + a second pass for the added posts.
ORDER=[0,9,15,6,14,22,17,30,7,10,29,20,23,16,32,18,12,3,21,13,28,27,11,1,8,25,19,2,31,5,24,26,4,
       6,13,16,15,22,7,32,10,12,29,17,28,23,25,24,0,19,5,20,30,3,27,21,11,1,2,26,31,4,14,18,9,8]
import calendar as _cal
from collections import Counter as _Counter
_MON={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
assert len(ORDER)==len(POSTS), (len(ORDER),len(POSTS))
assert max(_Counter(ORDER).values())<=2, "a reel is reused more than twice"
for i,p in enumerate(POSTS):
    p["ref"]=[REELS[ORDER[i]]]
    mon,day=p["date"].split()
    p["iso"]="2026-%02d-%02d"%(_MON[mon],int(day))

GROWTH_LABELS=["Now","Jul","Aug","Sep"]
GROWTH={"conservative":[40,47,55,64],"base":[40,52,68,84],"best":[40,58,78,100]}

DATA={"pillars":PILLARS,"week":WEEK,"competitors":COMPETITORS,"budget":BUDGET,"budgetTable":BUDGET_TABLE,
      "algo":ALGO,"posts":POSTS,"growthLabels":GROWTH_LABELS,"growth":GROWTH,"contentMix":CONTENT_MIX,
      "storyRhythm":STORY_RHYTHM,"storyTypes":STORY_TYPES,"storySequence":STORY_SEQUENCE,
      "activities":ACTIVITIES,"activitySchedule":ACTIVITY_SCHEDULE}
PILLAR_BY={p["key"]:p for p in PILLARS}

HTML = r"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pantheon Development — AI Social Command Center · Q3 2026</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{--navy:#0a1124;--navy2:#111a33;--navy3:#16213f;--gold:#C9A227;--gold2:#e7c75a;
--text:#eef2fb;--muted:#9aa6c4;--border:#243456;--glow:rgba(201,162,39,.35)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:
radial-gradient(900px 500px at 80% -5%,rgba(201,162,39,.12),transparent),
radial-gradient(900px 500px at 0% 10%,rgba(108,142,191,.12),transparent),var(--navy);
color:var(--text);line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--gold2);text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
nav{position:sticky;top:0;z-index:50;background:rgba(10,17,36,.82);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
.navrow{display:flex;align-items:center;gap:18px;height:60px;overflow-x:auto}
.brand{font-weight:800;letter-spacing:.5px;color:#fff;white-space:nowrap}.brand b{color:var(--gold)}
.navlinks{display:flex;gap:15px;font-size:13px;white-space:nowrap}
.navlinks a{color:var(--muted)}.navlinks a:hover{color:var(--gold2)}
.editbtn{margin-left:auto;display:flex;gap:8px;white-space:nowrap}
.btn{background:linear-gradient(135deg,var(--gold),var(--gold2));color:#1a1404;border:none;font-weight:700;padding:9px 16px;border-radius:9px;cursor:pointer;font-size:13px}
.btn.ghost{background:transparent;color:var(--gold2);border:1px solid var(--gold)}
section{padding:54px 0;border-bottom:1px solid var(--border)}
.tag{display:inline-block;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:10px}
h1{font-size:42px;line-height:1.1;color:#fff;margin-bottom:14px}
h2{font-size:28px;color:#fff;margin-bottom:8px}
.sub{color:var(--muted);max-width:780px;margin-bottom:26px}
.hero{padding:70px 0 50px;text-align:center}.hero h1{font-size:50px}
.hero .grad{background:linear-gradient(135deg,var(--gold2),var(--gold));-webkit-background-clip:text;background-clip:text;color:transparent}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:34px}
.kpi{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:22px}
.kpi .n{font-size:34px;font-weight:800;color:var(--gold2)}
.kpi .l{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-top:4px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:22px}
.card h3{color:#fff;font-size:16px;margin-bottom:10px}
.chartbox{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:18px}
.chartbox h3{font-size:14px;color:var(--muted);margin-bottom:12px;text-transform:uppercase;letter-spacing:1px}
.cv{position:relative;height:240px}
.sim{background:linear-gradient(135deg,var(--navy3),var(--navy2));border:1px solid var(--gold);border-radius:16px;padding:26px;box-shadow:0 0 40px -16px var(--glow)}
.sim .row{display:flex;justify-content:space-between;align-items:center;margin:14px 0 6px;font-size:13px}
.sim .val{color:var(--gold2);font-weight:700}
input[type=range]{width:100%;accent-color:var(--gold)}
.simout{display:flex;gap:18px;margin-top:18px;flex-wrap:wrap}
.simout .b{flex:1;min-width:130px;background:var(--navy);border:1px solid var(--border);border-radius:12px;padding:16px;text-align:center}
.simout .b .n{font-size:30px;font-weight:800;color:var(--gold2)}
.simout .b .l{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:1px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:16px}
.pcard{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:20px;position:relative;overflow:hidden}
.pcard::before{content:'';position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--c)}
.pcard .ic{font-size:26px}.pcard .pc{font-size:30px;font-weight:800;color:var(--gold2);margin:6px 0 2px}
.pcard .nm{font-weight:700;color:#fff}.pcard .dy{font-size:12px;color:var(--gold2);margin:8px 0}
.pcard .meta{font-size:12px;color:var(--muted);border-top:1px solid var(--border);padding-top:10px;margin-top:10px}
.week{display:grid;grid-template-columns:repeat(7,1fr);gap:10px}
.wd{background:var(--navy2);border:1px solid var(--border);border-radius:12px;padding:14px;border-top:3px solid var(--c)}
.wd .d{font-weight:800;color:#fff}.wd .t{font-size:11px;color:var(--gold2);margin:4px 0}
.wd .ty{font-size:12px;color:var(--text);font-weight:600}.wd .ds{font-size:11px;color:var(--muted);margin-top:6px}
.alist{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.ai{display:flex;gap:14px;background:var(--navy2);border:1px solid var(--border);border-radius:12px;padding:16px}
.ai .e{font-size:22px}.ai .t{font-weight:700;color:#fff;font-size:14px}.ai .d{font-size:13px;color:var(--muted);margin-top:4px}
table{width:100%;border-collapse:collapse;margin-top:14px;font-size:13.5px}
th,td{text-align:left;padding:11px 12px;border-bottom:1px solid var(--border);vertical-align:top}
th{color:var(--gold2);text-transform:uppercase;font-size:11px;letter-spacing:1px}
td.amt{color:var(--gold2);font-weight:700;white-space:nowrap}
.brow{display:flex;gap:14px;background:var(--navy2);border:1px solid var(--border);border-radius:12px;padding:16px;margin-bottom:10px}
.brow .num{font-size:22px;font-weight:800;color:var(--gold);min-width:30px}
.brow .t{font-weight:700;color:#fff}.brow .d{font-size:13px;color:var(--muted);margin-top:3px}
.compcard{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:20px}
.compcard .h{font-size:17px;font-weight:800;color:#fff}.compcard .seg{font-size:12px;color:var(--gold2);margin:2px 0 10px}
.compcard .take{font-size:13.5px;color:var(--muted);margin-bottom:12px}
.reflink{display:block;background:var(--navy);border:1px solid var(--border);border-left:3px solid var(--gold);border-radius:9px;padding:11px 13px;margin-top:8px;font-size:13px}
.reflink .ti{color:var(--gold2);font-weight:700}.reflink .cp{color:var(--muted);font-size:12px;margin-top:3px}.reflink:hover{border-color:var(--gold)}
.mixrow{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:24px}
.mixc{background:var(--navy2);border:1px solid var(--border);border-radius:12px;padding:16px;border-top:3px solid var(--c)}
.mixc .n{font-size:26px;font-weight:800;color:var(--gold2)}.mixc .l{font-size:12px;color:var(--muted)}
.stype{display:flex;gap:12px;background:var(--navy2);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:10px}
.stype .t{font-weight:700;color:#fff;font-size:13.5px}.stype .d{font-size:12.5px;color:var(--muted)}
.seq{counter-reset:f}.seqitem{display:flex;gap:14px;background:var(--navy);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:8px}
.seqitem .fn{color:var(--gold);font-weight:800;min-width:62px;font-size:12px}
.act{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:18px;border-top:3px solid var(--gold)}
.act .h{display:flex;gap:10px;align-items:center;margin-bottom:6px}.act .h .e{font-size:22px}.act .h .nm{font-weight:800;color:#fff;font-size:15px}
.act .meta{font-size:12px;color:var(--gold2);margin-bottom:8px}.act .mech{font-size:13px;color:var(--muted)}
.act .kpi{font-size:12px;color:#5fd3bf;margin-top:8px;border-top:1px solid var(--border);padding-top:8px}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}
.fbtn{background:var(--navy2);border:1px solid var(--border);color:var(--muted);padding:8px 14px;border-radius:20px;cursor:pointer;font-size:12.5px;font-weight:600}
.fbtn.on{background:var(--gold);color:#1a1404;border-color:var(--gold)}
.posts{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.post{background:var(--navy2);border:1px solid var(--border);border-radius:14px;padding:20px;border-top:4px solid var(--c)}
.post .top{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:8px}
.post .date{font-size:12px;color:var(--muted)}.post .date b{color:#fff}
.badges{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.pill{font-size:10.5px;font-weight:700;padding:3px 9px;border-radius:12px;text-transform:uppercase;letter-spacing:.5px}
.pill.peak{background:rgba(201,162,39,.16);color:var(--gold2);border:1px solid var(--gold)}
.pill.boost{background:rgba(63,167,150,.16);color:#5fd3bf;border:1px solid #3FA796}
.pill.ft{background:var(--navy);color:#cdd6ec;border:1px solid var(--border)}
.pill.ft.reel{border-color:var(--gold)}.pill.ft.carousel{border-color:#6C8EBF}.pill.ft.static{border-color:#3FA796}
.post h3{color:#fff;font-size:17px;margin:4px 0 8px}
.hook{font-style:italic;color:var(--gold2);font-size:14px;margin-bottom:10px}
.cap{font-size:13px;color:var(--text);white-space:pre-line;background:var(--navy);border:1px solid var(--border);border-radius:9px;padding:12px;margin-bottom:8px}
.tags{font-size:12px;color:#6C8EBF;margin-bottom:6px}
.cta{font-size:12px;color:var(--muted);margin-bottom:10px}.cta b{color:var(--gold2)}
details{background:var(--navy);border:1px solid var(--border);border-radius:9px;margin-bottom:7px}
summary{cursor:pointer;padding:10px 13px;font-size:12.5px;font-weight:700;color:#fff;list-style:none}
summary::-webkit-details-marker{display:none}summary::before{content:'▸ ';color:var(--gold)}
details[open] summary::before{content:'▾ '}
.dbody{padding:0 13px 12px;font-size:12.5px;color:var(--muted)}
.slides{list-style:none;padding:0 13px 12px;margin:0}
.slides li{font-size:12.5px;color:var(--muted);padding:7px 0 7px 0;border-bottom:1px solid var(--border)}
.slides li:last-child{border-bottom:none}
.storyline{font-size:12px;color:#b9a6e0;background:rgba(142,124,195,.1);border:1px solid #5a4a86;border-radius:8px;padding:9px 12px;margin-bottom:7px}
.collabtag{font-size:11.5px;color:#5fd3bf;margin-top:4px;margin-bottom:8px}
.editing [contenteditable]{outline:1px dashed var(--gold);outline-offset:2px;border-radius:3px}
footer{padding:40px 0;text-align:center;color:var(--muted);font-size:13px}
.note{background:rgba(201,162,39,.08);border:1px solid var(--gold);border-radius:10px;padding:12px 15px;font-size:13px;color:var(--text);margin-top:16px}
.calmonth{margin-bottom:26px}.calmonth h3{color:#fff;margin-bottom:10px}
.calgrid{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}
.caldow{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;text-align:center;padding-bottom:4px}
.calcell{min-height:96px;background:var(--navy2);border:1px solid var(--border);border-radius:8px;padding:6px}
.calcell.empty{background:transparent;border:none}
.calday{font-size:11px;color:var(--muted);font-weight:700;margin-bottom:4px}
.calchip{display:block;font-size:10.5px;color:#0a1124;background:var(--c);border-radius:5px;padding:3px 6px;margin-bottom:3px;font-weight:700;cursor:pointer;line-height:1.25;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
@media(max-width:880px){.calcell{min-height:auto}.calgrid{gap:3px}.calchip{white-space:normal}}
@media(max-width:880px){.grid2,.grid3,.posts,.alist{grid-template-columns:1fr}.kpis,.mixrow{grid-template-columns:1fr 1fr}
.week{grid-template-columns:1fr 1fr}h1{font-size:34px}.hero h1{font-size:36px}}
</style></head>
<body>
<nav><div class="wrap navrow">
<span class="brand">PANTHEON<b>·</b>AI Command Center</span>
<span class="navlinks">
<a href="#dash">Dashboard</a><a href="#sim">Simulator</a><a href="#budget">Budget</a>
<a href="#algo">Algorithm</a><a href="#pillars">Pillars</a><a href="#week">Weekly Plan</a><a href="#calendar">Calendar</a>
<a href="#stories">Stories</a><a href="#activities">Activities</a><a href="#comp">Competitors</a><a href="#content">Content Engine</a></span>
<span class="editbtn">
<button class="btn ghost" onclick="toggleEdit()" id="editBtn">✏️ Edit Mode</button>
<button class="btn" onclick="downloadCopy()">⬇ Download</button></span>
</div></nav>

<header class="hero"><div class="wrap">
<span class="tag">Q3 2026 · Jul – Sep · AI-Powered Growth Plan</span>
<h1>From <span class="grad">40K to 100K</span> in 90 days.</h1>
<p class="sub" style="margin:0 auto">One command center — live dashboard, growth simulator, the full content engine (Reels, carousels slide-by-slide, statics & a Stories playbook), engagement activities, competitor battlecards and the Meta algorithm playbook. Built to be edited and shared with your team.</p>
<div class="kpis">
<div class="kpi"><div class="n" data-count="40000">0</div><div class="l">Followers today</div></div>
<div class="kpi"><div class="n" data-count="100000">0</div><div class="l">90-day target</div></div>
<div class="kpi"><div class="n" data-count="28">0</div><div class="l">Posts / month</div></div>
<div class="kpi"><div class="n">2.0%+</div><div class="l">Target ER (from 0.38%)</div></div>
</div></div></header>

<section id="dash"><div class="wrap">
<span class="tag">Live Dashboard</span><h2>The growth picture</h2>
<p class="sub">Projected trajectory, content mix and the engagement gap vs the developers you're competing with.</p>
<div class="grid2">
<div class="chartbox"><h3>Follower trajectory · 40K → 100K</h3><div class="cv"><canvas id="cGrowth"></canvas></div></div>
<div class="chartbox"><h3>Engagement rate vs competitors</h3><div class="cv"><canvas id="cER"></canvas></div></div>
<div class="chartbox"><h3>Content pillar mix</h3><div class="cv"><canvas id="cPillar"></canvas></div></div>
<div class="chartbox"><h3>Posting volume ramp · posts / month</h3><div class="cv"><canvas id="cVol"></canvas></div></div>
</div></div></section>

<section id="sim"><div class="wrap">
<span class="tag">AI Growth Simulator</span><h2>Drag the levers. Watch 100K move.</h2>
<p class="sub">A transparent model of what drives IG growth in Dubai real estate: posting volume, collab reels and paid reach. Move the sliders to see the 90-day outcome.</p>
<div class="sim">
<div class="row"><span>Feed posts per week</span><span class="val"><span id="vPosts">6</span></span></div>
<input type="range" id="sPosts" min="2" max="10" value="6" oninput="sim()">
<div class="row"><span>Creator / IG-Collab reels per month</span><span class="val"><span id="vCollab">3</span></span></div>
<input type="range" id="sCollab" min="0" max="8" value="3" oninput="sim()">
<div class="row"><span>Monthly boost budget (AED)</span><span class="val">AED <span id="vBudget">27,000</span></span></div>
<input type="range" id="sBudget" min="0" max="45000" step="1000" value="27000" oninput="sim()">
<div class="simout">
<div class="b"><div class="n" id="oFollowers">100K</div><div class="l">Followers in 90 days</div></div>
<div class="b"><div class="n" id="oGain">+60K</div><div class="l">Net new</div></div>
<div class="b"><div class="n" id="oReach">14.2M</div><div class="l">Est. 90-day reach</div></div>
<div class="b"><div class="n" id="oVerdict">On track</div><div class="l">Verdict</div></div>
</div>
<div class="note" id="simNote"></div>
</div></div></section>

<section id="budget"><div class="wrap">
<span class="tag">The Investment</span><h2>Why ~AED 25–30K / month is the real floor</h2>
<p class="sub">Not a boost-per-post tax — the genuine cost of moving 150% in 90 days inside the most competitive real-estate ad market on earth.</p>
<div id="budgetReasons"></div>
<h3 style="color:#fff;margin:22px 0 4px">Where it goes</h3>
<table id="budgetTable"></table>
<div class="note">Spend below this floor and the <b>timeline</b> stretches, not the target.</div>
</div></section>

<section id="algo"><div class="wrap">
<span class="tag">Meta Algorithm Playbook</span><h2>Post the way 2026 IG actually rewards</h2>
<p class="sub">More posts, Reels-first, engineered for saves and shares — to earn free algorithmic reach on top of the paid push.</p>
<div class="alist" id="algoList"></div></div></section>

<section id="pillars"><div class="wrap">
<span class="tag">Content Pillars & Mix</span><h2>Five pillars + the format mix</h2>
<p class="sub">Every post belongs to a pillar; every pillar maps to a format mix so the feed stays balanced.</p>
<div class="mixrow" id="mixRow"></div>
<div class="pgrid" id="pillarGrid"></div></div></section>

<section id="week"><div class="wrap">
<span class="tag">Weekly Rhythm</span><h2>The repeatable week</h2>
<p class="sub">This cadence runs every week of the quarter — ~6 feed posts + daily Stories.</p>
<div class="week" id="weekGrid"></div>
<div class="note">⭐ Wednesday 3PM is your peak slot (your data's best window). Protect it for your strongest project reel every week.</div>
</div></section>

<section id="calendar"><div class="wrap">
<span class="tag">Calendar View</span><h2>The 3-month calendar at a glance</h2>
<p class="sub">Every flagship post on its day, July → September. Colour = pillar, icon = format. Tap any post to jump to its full brief.</p>
<div id="calWrap"></div>
</div></section>

<section id="stories"><div class="wrap">
<span class="tag">Stories Playbook</span><h2>Stories: the daily growth layer</h2>
<p class="sub">Stories aren't filler — they drive interaction, reach and warm leads every single day. Here's the daily rhythm, the interaction toolkit, and the launch-day sequence.</p>
<h3 style="color:#fff;margin:6px 0 10px">Daily story rhythm</h3>
<table id="storyRhythm"></table>
<h3 style="color:#fff;margin:24px 0 10px">Story interaction toolkit</h3>
<div id="storyTypes"></div>
<h3 style="color:#fff;margin:24px 0 10px">Launch-day story sequence (8 frames)</h3>
<div class="seq" id="storySeq"></div>
</div></section>

<section id="activities"><div class="wrap">
<span class="tag">Activities & Engagement Campaigns</span><h2>The activities that actually move followers</h2>
<p class="sub">Posting alone won't 2.5× the page. These recurring campaigns manufacture reach, leads and UGC — the engine behind the growth curve.</p>
<div class="grid2" id="activityGrid"></div>
<h3 style="color:#fff;margin:26px 0 8px">Quarter activity schedule</h3>
<table id="activitySchedule"></table>
</div></section>

<section id="comp"><div class="wrap">
<span class="tag">Competitor Battlecards</span><h2>Study the exact posts that work</h2>
<p class="sub">Each link opens ONE specific high-performing reel — not a profile. Tap through, see the style, copy the technique.</p>
<div class="grid2" id="compGrid"></div></div></section>

<section id="content"><div class="wrap">
<span class="tag">Content Engine</span><h2>The 3-month content calendar</h2>
<p class="sub">Flagship posts across July–September. Reels get a shot brief, carousels get a slide-by-slide breakdown, statics get a design layout — and every post has a Story tie-in and a real reference reel. Filter below.</p>
<div class="filters" id="filters"></div>
<div class="posts" id="postGrid"></div>
<div class="note">This is the briefed flagship layer. Around it runs the weekly rhythm + the Stories & Activities above (~28 posts/month total). Duplicate the closest card as your template for filler slots.</div>
</div></section>

<footer><div class="wrap">
Pantheon Development · AI Social Command Center · Q3 2026 &nbsp;·&nbsp; Reference reels are live competitor/best-in-class posts captured June 2026 — verify before shooting.<br>
Built to be edited: hit <b>Edit Mode</b>, change any text, then <b>Download</b> your version.
</div></footer>

<script>
const DATA = __DATA__;
const PILLAR_BY = __PILLARBY__;
function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function ce(){return ' contenteditable="false" '}
function animateCounters(){document.querySelectorAll('[data-count]').forEach(el=>{
 const tgt=+el.dataset.count;let c=0;const step=tgt/60;
 const fmt=n=>n>=1000?(n/1000).toFixed(n%1000&&n<100000?1:0).replace(/\.0$/,'')+'K':Math.round(n);
 const iv=setInterval(()=>{c+=step;if(c>=tgt){c=tgt;clearInterval(iv)}el.textContent=fmt(c)},16)});}

/* mix */
document.getElementById('mixRow').innerHTML=DATA.contentMix.map(m=>`
<div class="mixc" style="--c:${m[2]}"><div class="n">${m[1]}</div><div class="l">${m[0]}</div></div>`).join('');
/* pillars */
document.getElementById('pillarGrid').innerHTML=DATA.pillars.map(p=>`
<div class="pcard" style="--c:${p.color}"><div class="ic">${p.icon}</div>
<div class="pc">${p.pct}%</div><div class="nm" ${ce()}>${p.name}</div><div class="dy">${p.day}</div>
<div class="meta"><b style="color:#cdd6ec">Format:</b> ${p.format}<br><b style="color:#cdd6ec">Hook:</b> ${p.hook}<br>
<b style="color:#cdd6ec">CTA:</b> ${p.cta}<br><b style="color:#cdd6ec">Goal:</b> ${p.goal}</div></div>`).join('');
/* week */
document.getElementById('weekGrid').innerHTML=DATA.week.map(w=>{const c=PILLAR_BY[w[3]].color;
 return `<div class="wd" style="--c:${c}"><div class="d">${w[0]}</div><div class="t">${w[1]}</div>
 <div class="ty" ${ce()}>${w[2]}</div><div class="ds" ${ce()}>${w[4]}</div></div>`}).join('');
/* algo */
document.getElementById('algoList').innerHTML=DATA.algo.map(a=>`
<div class="ai"><div class="e">${a[0]}</div><div><div class="t" ${ce()}>${a[1]}</div><div class="d" ${ce()}>${a[2]}</div></div></div>`).join('');
/* budget */
document.getElementById('budgetReasons').innerHTML=DATA.budget.map((b,i)=>`
<div class="brow"><div class="num">${i+1}</div><div><div class="t" ${ce()}>${b[0]}</div><div class="d" ${ce()}>${b[1]}</div></div></div>`).join('');
document.getElementById('budgetTable').innerHTML='<tr><th>Line</th><th>Monthly</th><th>What it buys</th></tr>'+
 DATA.budgetTable.map(r=>`<tr><td ${ce()}>${r[0]}</td><td class="amt">${r[1]}</td><td ${ce()}>${r[2]}</td></tr>`).join('')+
 '<tr><td><b>Total floor</b></td><td class="amt">AED 25–30K</td><td>The realistic minimum for 100K in 90 days</td></tr>';
/* stories */
document.getElementById('storyRhythm').innerHTML='<tr><th>Day</th><th>Story</th><th>Why it works</th></tr>'+
 DATA.storyRhythm.map(r=>`<tr><td><b style="color:#fff">${r[0]}</b></td><td ${ce()}>${r[1]}</td><td ${ce()}>${r[2]}</td></tr>`).join('');
document.getElementById('storyTypes').innerHTML=DATA.storyTypes.map(s=>`
<div class="stype"><div class="t">${s[0]}</div><div class="d" ${ce()}>— ${s[1]}</div></div>`).join('');
document.getElementById('storySeq').innerHTML=DATA.storySequence.map(s=>`
<div class="seqitem"><div class="fn">${s[0]}</div><div ${ce()}>${esc(s[1])}</div></div>`).join('');
/* activities */
document.getElementById('activityGrid').innerHTML=DATA.activities.map(a=>`
<div class="act"><div class="h"><span class="e">${a.icon}</span><span class="nm" ${ce()}>${a.name}</span></div>
<div class="meta">${a.cad} · ${a.plat} · Goal: ${a.goal}</div>
<div class="mech" ${ce()}>${esc(a.mech)}</div><div class="kpi">📈 KPI: ${esc(a.kpi)}</div></div>`).join('');
document.getElementById('activitySchedule').innerHTML='<tr><th>Month</th><th>Flagship activity</th><th>Always-on</th></tr>'+
 DATA.activitySchedule.map(r=>`<tr><td><b style="color:#fff">${r[0]}</b></td><td ${ce()}>${esc(r[1])}</td><td ${ce()}>${esc(r[2])}</td></tr>`).join('');
/* competitors */
document.getElementById('compGrid').innerHTML=DATA.competitors.map(c=>`
<div class="compcard"><div class="h" ${ce()}>${c.h}</div><div class="seg">${c.seg}</div><div class="take" ${ce()}>${c.take}</div>
${c.reels.map(r=>`<a class="reflink" href="${r[1]}" target="_blank" rel="noopener"><span class="ti">▶ ${esc(r[0])}</span><span class="cp">Copy this: ${esc(r[2])}</span></a>`).join('')}</div>`).join('');
/* posts */
function briefBlock(p){
 if(p.ftype==='Carousel'){
   return `<details open><summary>🗂 Slide-by-slide (${p.detail.length} slides)</summary>
   <ul class="slides">${p.detail.map(s=>`<li ${ce()}>${esc(s)}</li>`).join('')}</ul></details>`;}
 if(p.ftype==='Static'){
   return `<details><summary>🎨 Design layout</summary><div class="dbody" ${ce()}>${esc(p.detail)}</div></details>`;}
 return `<details><summary>🎬 Shot brief</summary><div class="dbody" ${ce()}>${esc(p.detail)}</div></details>`;}
function postCard(p){const pl=PILLAR_BY[p.pillar];
 const badges=[`<span class="pill ft ${p.ftype.toLowerCase()}">${p.ftype}</span>`];
 if(p.peak)badges.push('<span class="pill peak">⭐ Peak</span>');
 if(p.boost)badges.push('<span class="pill boost">Boost</span>');
 const refs=p.ref.length?`<details><summary>▶ Reference — how it should look</summary><div class="dbody">${
   p.ref.map(r=>`<a class="reflink" href="${r[1]}" target="_blank" rel="noopener"><span class="ti">▶ ${esc(r[0])}</span><span class="cp">Copy this: ${esc(r[2])}</span></a>`).join('')}</div></details>`:'';
 return `<div class="post" data-pillar="${p.pillar}" data-ft="${p.ftype}" data-peak="${p.peak}" data-boost="${p.boost}" style="--c:${pl.color}">
 <div class="top"><div class="date"><b>${p.date}</b> · ${p.day} ${p.time} · ${pl.icon} ${pl.name}</div><div class="badges">${badges.join('')}</div></div>
 <h3 ${ce()}>${esc(p.title)}</h3>
 <div class="hook" ${ce()}>“${esc(p.hook)}”</div>
 <div class="cap" ${ce()}>${esc(p.caption)}</div>
 <div class="tags" ${ce()}>${esc(p.tags)}</div>
 <div class="cta">CTA: <b>${esc(p.cta)}</b></div>
 ${p.collab?`<div class="collabtag">🤝 ${esc(p.collab)}</div>`:''}
 <details><summary>🎨 Creative direction</summary><div class="dbody" ${ce()}>${esc(p.direction)}</div></details>
 ${briefBlock(p)}
 <div class="storyline" ${ce()}>📱 Story tie-in: ${esc(p.story)}</div>
 ${refs}</div>`;}
function renderPosts(f){const g=document.getElementById('postGrid');let ps=DATA.posts.slice();
 if(f&&f!=='all'){
  if(f==='peak')ps=ps.filter(p=>p.peak);
  else if(f==='boost')ps=ps.filter(p=>p.boost);
  else if(['Reel','Carousel','Static'].includes(f))ps=ps.filter(p=>p.ftype===f);
  else if(['Jul','Aug','Sep'].includes(f))ps=ps.filter(p=>p.date.startsWith(f));
  else ps=ps.filter(p=>p.pillar===f);}
 g.innerHTML=ps.map(postCard).join('');}
const FILTERS=[['all','All'],['Jul','July'],['Aug','August'],['Sep','September'],
 ['Reel','🎬 Reels'],['Carousel','🗂 Carousels'],['Static','🎨 Statics'],
 ['project','🏗️ Project'],['lifestyle','🌆 Lifestyle'],['community','👥 Community'],
 ['invest','📈 Investment'],['delivery','🔑 Delivery'],['peak','⭐ Peak'],['boost','Boost']];
document.getElementById('filters').innerHTML=FILTERS.map((f,i)=>`<button class="fbtn ${i===0?'on':''}" data-f="${f[0]}">${f[1]}</button>`).join('');
document.querySelectorAll('.fbtn').forEach(b=>b.onclick=()=>{document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');renderPosts(b.dataset.f);});
renderPosts('all');

/* calendar grid */
const MONTHS=[['July',7],['August',8],['September',9]];
const DOW=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
function fmtIcon(ft){return ft==='Reel'?'🎬':ft==='Carousel'?'🗂':'🎨'}
document.getElementById('calWrap').innerHTML=MONTHS.map(([nm,mi])=>{
 const first=new Date(2026,mi-1,1).getDay();const lead=(first+6)%7;const dim=new Date(2026,mi,0).getDate();
 let cells='';for(let i=0;i<lead;i++)cells+='<div class="calcell empty"></div>';
 for(let d=1;d<=dim;d++){const iso='2026-'+String(mi).padStart(2,'0')+'-'+String(d).padStart(2,'0');
  const ps=DATA.posts.filter(p=>p.iso===iso);
  const chips=ps.map(p=>{const pl=PILLAR_BY[p.pillar];
   return `<span class="calchip" style="--c:${pl.color}" onclick="jumpPost('${iso}')" title="${esc(p.title)}">${fmtIcon(p.ftype)} ${esc(p.title)}</span>`}).join('');
  cells+=`<div class="calcell"><div class="calday">${d}</div>${chips}</div>`;}
 return `<div class="calmonth"><h3>${nm} 2026</h3><div class="calgrid">${DOW.map(x=>`<div class="caldow">${x}</div>`).join('')}${cells}</div></div>`;
}).join('');
function jumpPost(iso){const mon={'2026-07':'Jul','2026-08':'Aug','2026-09':'Sep'}[iso.slice(0,7)];
 const btn=[...document.querySelectorAll('.fbtn')].find(b=>b.dataset.f===mon);if(btn)btn.click();
 document.getElementById('content').scrollIntoView({behavior:'smooth'});}

/* charts */
const gold='#C9A227',gold2='#e7c75a',gtxt='#9aa6c4',gline='#243456';
Chart.defaults.color=gtxt;Chart.defaults.font.family="Segoe UI";
new Chart(cGrowth,{type:'line',data:{labels:DATA.growthLabels,datasets:[
 {label:'Best case',data:DATA.growth.best,borderColor:gold2,backgroundColor:'rgba(231,199,90,.12)',fill:true,tension:.4},
 {label:'Base',data:DATA.growth.base,borderColor:gold,tension:.4},
 {label:'Conservative',data:DATA.growth.conservative,borderColor:'#6C8EBF',borderDash:[5,4],tension:.4}]},
 options:{plugins:{legend:{labels:{boxWidth:12}}},scales:{y:{grid:{color:gline},ticks:{callback:v=>v+'K'}},x:{grid:{color:gline}}}}});
new Chart(cER,{type:'bar',data:{labels:['Pantheon','BNW','Samana','Imtiaz','Target'],
 datasets:[{data:[0.38,2.42,0.52,0.28,2.0],backgroundColor:['#6C8EBF',gold,'#3FA796','#B5651D',gold2]}]},
 options:{plugins:{legend:{display:false}},scales:{y:{grid:{color:gline},ticks:{callback:v=>v+'%'}},x:{grid:{display:false}}}}});
new Chart(cPillar,{type:'doughnut',data:{labels:DATA.pillars.map(p=>p.name),
 datasets:[{data:DATA.pillars.map(p=>p.pct),backgroundColor:DATA.pillars.map(p=>p.color),borderColor:'#0a1124',borderWidth:2}]},
 options:{plugins:{legend:{position:'right',labels:{boxWidth:11,font:{size:11}}}},cutout:'58%'}});
new Chart(cVol,{type:'bar',data:{labels:['Now','Jul','Aug','Sep'],datasets:[{data:[8,22,22,22],backgroundColor:[gline,gold,gold,gold2]}]},
 options:{plugins:{legend:{display:false}},scales:{y:{grid:{color:gline}},x:{grid:{display:false}}}}});

/* simulator */
function sim(){const posts=+sPosts.value,collab=+sCollab.value,budget=+sBudget.value;
 vPosts.textContent=posts;vCollab.textContent=collab;vBudget.textContent=budget.toLocaleString();
 const base=40000;const organic=posts*1100*3;const collabGain=collab*2600*3;const paid=budget*0.62*3;
 let total=Math.round((base+organic+collabGain+paid)/1000)*1000;const gain=total-base;
 const reach=((posts*4*3*9000)+(collab*3*120000)+(budget*3*120))/1e6;
 oFollowers.textContent=(total/1000).toFixed(0)+'K';oGain.textContent='+'+(gain/1000).toFixed(0)+'K';
 oReach.textContent=reach.toFixed(1)+'M';let verdict,note;
 if(total>=100000){verdict='🎯 100K hit';note='This lands the 100K target inside 90 days. Recommended: ~6 posts/week, 3 collabs/month, ~AED 27K boost.';}
 else if(total>=80000){verdict='On track';note='Strong — you reach 80–95K. Add one more collab/month or a little reach to close the gap to 100K.';}
 else if(total>=62000){verdict='Slower';note='Healthy growth but 100K slips past 90 days. The goal still happens, it just takes longer.';}
 else{verdict='⚠ Too light';note='At this level the page barely breaks out of 40K. Volume + collabs + reach all need to come up.';}
 oVerdict.textContent=verdict;simNote.textContent=note;}
sim();

/* edit + download */
let editing=false;
function toggleEdit(){editing=!editing;document.body.classList.toggle('editing',editing);
 document.querySelectorAll('[contenteditable]').forEach(e=>e.setAttribute('contenteditable',editing));
 editBtn.textContent=editing?'✅ Done editing':'✏️ Edit Mode';}
function downloadCopy(){if(editing)toggleEdit();
 const html='<!DOCTYPE html>\n'+document.documentElement.outerHTML;
 const blob=new Blob([html],{type:'text/html'});const a=document.createElement('a');
 a.href=URL.createObjectURL(blob);a.download='Pantheon_Social_Command_Center_edited.html';a.click();}
animateCounters();
</script></body></html>"""

html = HTML.replace("__DATA__", json.dumps(DATA)).replace("__PILLARBY__", json.dumps(PILLAR_BY))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pantheon_Social_Command_Center_Q3_2026.html")
with open(out,"w",encoding="utf-8") as f:
    f.write(html)
carousels=sum(1 for p in POSTS if p["ftype"]=="Carousel")
statics=sum(1 for p in POSTS if p["ftype"]=="Static")
reels=sum(1 for p in POSTS if p["ftype"]=="Reel")
print("Wrote",out,len(html),"bytes ·",len(POSTS),"posts (",reels,"reel,",carousels,"carousel,",statics,"static ) ·",len(ACTIVITIES),"activities")
