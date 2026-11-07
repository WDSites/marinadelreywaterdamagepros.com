# Content module schema (each content/*.py exports PAGES = [dict, ...])

Common keys
- type: 'service' | 'location' | 'blog'
- slug: 'water-mitigation' | 'service-area/venice-ca' | 'blog/<topic>-marina-del-rey-ca'  (no slashes at ends)
- title, meta (140-160 chars measured), h1, hero_sub (one sentence)
- body: list of blocks (below). FAQ separate.
- faqs: list of (question, answer) where answer is a str or list of str paragraphs. Visible FAQ == FAQPage JSON-LD exactly.
- sidecard: {'h3': page-specific heading, 'copy': one line, 'link': (anchor text, '/service-slug/')}
  The generator adds kicker "24/7 Emergency Line Open", the tel button and the four approved bullets itself.
Inline markup inside any string: [anchor text](/root-relative-path/) for internal links. No other markup. No HTML.

Block types
- {'t':'h2','text':...}  starts a new card section (the generator wraps each h2 group in a card)
- {'t':'h3','text':...}
- {'t':'p','text':...}   2-4 sentences, max about 75 words
- {'t':'ul','items':[str,...]}  checklists (rendered as icon list)
- {'t':'table','head':[...],'rows':[[...],...]}  comparison/decision table (no prices)
- {'t':'cards','items':[{'h':..,'p':..},...]}  2-4 short cards (used for "If water is still spreading" prep cards, symptom tiers, etc.)
- {'t':'callout','h':..., 'paras':[...]}  tinted insight card
- {'t':'steps','items':[{'h':..,'p':..},...]}  numbered process
- {'t':'localnote','h':'Marina Del Rey notes: ...','paras':[...]}  .localnote card (blogs: mandatory; services/locations: optional)
- {'t':'cta','text':...} a mid-page call prompt sentence (generator adds the tel button). Use at most once.

Service extras: 'emergency': True/False, 'photo': slug of image file (same as page slug). 
Location extras: 'loc': 'Venice', 'zips': ['90291','90292'], 'primary_zip': '90291', 'zip_note': str or '' (e.g. also serves Marina Del Rey),
  'map_q': 'Venice, Los Angeles, CA', 'map_z': 14, 'county': 'Los Angeles County', 'utility': str, 'permit': str, 'nearby': [slugs of 2 other location pages]
  Location body must include: an H2 naming the emergency situation in that place, a 'cards' block titled by an h2 like "If water is still spreading" with 4 prep cards, ZIP FAQ "Do you cover every ZIP code in {Loc}?" and FAQ "Is emergency water removal available in {Loc}?"
Blog extras: 'category': 'repair'|'mold'|'flood'|'pipe'|'drying'|'general', 'date': '2026-10-27', 'topic': original keyword, 'localnote' block mandatory, one local FAQ (the last faq).

Rules reminder: zero em dash, en dash, semicolons, or "---" in any string. No banned phrases (see build prompt Section 9). Paragraphs under 80 words. Floors: service/location 800 words, blog 1,100+ words (target 1,200), counting body text + faqs.
