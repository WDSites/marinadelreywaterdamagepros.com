# BRIEF: 14 NEW SERVICE PAGES for Marina Del Rey Water Damage Pros

You write content modules only (python files that export PAGES, exactly as content/service.py and parts_svc/p*.py do). READ FIRST: /home/claude/mdr/SCHEMA.md, /home/claude/mdr/facts.md, /home/claude/mdr/lint.py, and parts_svc/p1.py (water-mitigation) plus two other existing pages in content/service.py for voice. Do NOT edit gen.py, css.py, home.py or any existing content. Write ONLY your own file(s). Run `cd /home/claude/mdr && python3 lint.py <yourfile>` until it is clean (it prints word counts, meta and title lengths, banned phrases, dashes, link validity). Valid link targets are listed at the bottom.

## Page dict (type 'service')
{'type':'service','slug':..., 'emergency':True/False, 'photo': <same as slug>, 'title': EXACT string given below, 'meta': 140 to 160 chars INCLUDING the display phone "(424) 550-5662" once and a call prompt, no "free", 'h1': EXACT string given below, 'hero_sub': one sentence, 'sidecard': {'h3':..., 'copy':..., 'link':[anchor, '/slug/']}, 'body':[blocks], 'faqs':[(q, a), ...]}
Every sidecard h3 and copy must be distinct and specific to the page. The sidecard link goes to the related page named in your spec.

## Content rules (all are checked by scripts)
- 1,100 to 1,300 words (body + FAQ), never under 1,000. Every paragraph new prose for Marina Del Rey. No template sentences shared with other pages, no find-and-replace of a topic into a shared paragraph. Section order and H2 wording must differ from the other pages: the required topics below are required, the headings must be page-specific wording, not the same labels on every page.
- Paragraphs max 75 words, sentences max 40 words, average sentence 11 to 17 words. Plain American English, concrete nouns, no filler. Use block types from SCHEMA.md: h2, h3, p, ul, table, cards, callout, steps, localnote (optional), cta (once). Include at least one table OR cards block AND one steps block.
- ZERO em dashes, en dashes, semicolons, "---". Hyphens inside compound words are fine. No colons-as-dashes tricks. No prices, dollar figures, per-square-foot figures, percentages you invented, no response-time or arrival-time promises ("same-day response when available" is the only allowed phrasing), no "free", no "near me", no guarantee or warranty talk, no reviews, ratings, license numbers, names of people, years in business, counts of jobs, or IICRC firm certification claims. Only credential words: "licensed and insured". Never write the phone number in prose (the meta is the only place). No forms. No health claims or diagnosis (mold: moisture first, ask a physician about health).
- Write "Marina Del Rey" with that capitalisation. Marina Del Rey is an unincorporated community of Los Angeles County, never a city.
- Required sections (use your own headings, and where noted include the word): (1) what this problem is and how it happens in local housing and climate, (2) a symptom bridge: what you see and what it means, (3) a first-hour SAFETY section (heading must contain the word "safety"): shut-off, electrical, who to call, (4) our process with real equipment (steps block: extraction pumps, air movers, LGR dehumidifiers, moisture meters, thermal imaging camera, containment, etc as relevant), (5) what changes the scope and cost (factors only, heading contains "cost"), (6) insurance fit (sudden versus gradual, flood versus plumbing, general terms only, "check your policy", "ask your insurer", no deadlines, no carriers), (7) a "mistakes to avoid" or "prevention" section, (8) FAQ: first question exactly "Is emergency {service phrase} available in Marina Del Rey?" (answer: 24/7 dispatch, same-day response when available) plus 3 to 5 other specific questions (4 to 6 FAQs total). Non-emergency pages still need that emergency FAQ.
- Name "ANSI/IICRC S500" ONCE on the page as the published standard that homeowners may ask any company about (sewage page may instead name the EPA or county source once as well). Never as a firm certification.
- Links: exactly 2 inline links to related SERVICE pages and exactly 2 inline links to LOCATION pages, as [anchor text](/slug/) inside sentences, spread through the page. Natural anchors. NEVER link to any /blog/ page.
- LOCAL FACTS: use the fact IDs assigned to your page below (at least 3). Each must appear in a paragraph WITH a practical tie-back for the reader in the same paragraph, and with the source type named in the text (e.g. "according to Los Angeles County Public Works", "the 2020 census counted"). Use only the wording allowed in the fact list. Do not invent any other local fact, landmark, direction, time, statistic or code rule. If you want a landmark, use only those in facts.md. Do not use fact IDs not assigned to your page (other pages use them).
- REGIONAL HONESTY: where the service is uncommon or depends on building type, say so plainly in the text without inventing statistics, describe the real local cases, and point to the page that handles the common case.
- Insurance and law: general terms only. Mold: no claims. Landlord/tenant: say "ask your landlord or association", no legal rules.
- Section skeletons across pages must not look alike. Do not reuse the same opening sentence pattern ("If X is happening right now...") on every page.

## FACT LIBRARY (IDs). Quote only these claims, paraphrase freely, never add detail.
F1 [county site] The County of Los Angeles owns the marina and its Department of Beaches and Harbors manages it.
F2 [encyclopedia summary of county data] The harbor has eight basins separated by six strips of land.
F3 [encyclopedia summary] The harbor sits on land that was once salt marsh fed by Ballona Creek.
F4 [2020 census] The census counted 8,065 housing units in Marina del Rey.
F5 [2020 census] About 49.1 percent of Marina del Rey households are one person.
F6 [encyclopedia summary] The Admiralty High-Rise (The Cove) has about 800 condominiums and sits just across the line in the City of Los Angeles.
F7 [LA County Public Works waterworks page] The county-owned Marina del Rey Water System, run under contract by the Waterworks District Joint Fund, has about 300 metered connections serving about 8,800 people. Say the water bill shows which utility serves any address. Never claim it serves all of 90292.
F8 [same county page] Most of that system's water arrives through County Waterworks District 29, which buys nearly all its supply from the Metropolitan Water District through West Basin Municipal Water District, and the system can also draw from LADWP through two emergency interconnections.
F9a [LA County Public Works Building and Safety] It provides permits, plan review and inspection to unincorporated communities. Say "confirm which jurisdiction your parcel is in".
F9b [LADBS] City of Los Angeles addresses (Venice, Playa del Rey, Playa Vista) go through the Department of Building and Safety, with inspections before each stage is covered.
F10 [LA County Public Works] Ballona Creek is a roughly nine-mile flood protection channel draining a watershed of about 130 square miles into Santa Monica Bay.
F11 [news reports citing the National Weather Service] Los Angeles had one of its wettest months on record during the 2024 atmospheric river storms. Year only, never a month.
F12 [news] In 2022 a storm put 1.18 inches of rain over three days at the Ballona Creek gauge. Year only.
F13 [news] A 2019 storm filled Ballona Creek near Syd Kronenthal Park in Culver City.
F14 [encyclopedia summary] Venice sits at an elevation of about 10 feet and is very low-lying.
F15 [census via encyclopedia] About 69 percent of Venice housing is rented.
F16 [encyclopedia summary] Venice has older bungalows and early-1900s multifamily buildings.
F17 [encyclopedia summary] Playa Vista redevelopment began around 2001, so its housing is newer.
F20 [encyclopedia summary] Wind-blown dunes form the Del Rey Hills ("The Bluffs") rising up to 125 feet above Playa del Rey.
F21 [Golden State Water Company service area] Many Culver City addresses are served by Golden State Water Company, so tell the reader to check the bill.
F22 [City of Culver City site] The Building Safety Division at City Hall, 9770 Culver Boulevard, handles building permits. Do not print a phone number.
F24 [census via encyclopedia] About 73 percent of occupied homes in Santa Monica are renter-occupied.
F26 [county] Marina Del Rey is an unincorporated community of Los Angeles County surrounded by the City of Los Angeles.
F27 [county site] The harbor was formally dedicated in 1965.
F30 [encyclopedia summary] The lower Playa del Rey area was once wetland and dunes, and the Del Rey Lagoon pond is partly connected to Ballona Creek by an underground pipe.
F31 [encyclopedia summary] Playa Vista was built on the former Hughes Aircraft site, with redevelopment starting around 2001 and offices clustered in the area known as Silicon Beach.
F32 [encyclopedia summary] Venice was founded in 1905 as Venice of America, its canals were dug to drain marshes, and it was annexed to Los Angeles in 1926.
F35 [City of Culver City / encyclopedia] Culver City incorporated in 1917, sits at about 95 feet elevation, and Ballona Creek runs through it.
N1 [LA County Public Works sewer page] Sewer laterals are entirely owned by the private property owner they serve. The county maintains public mainlines but not private laterals, and recommends a backflow preventer and a cleanout in the lateral.
N2 [LA Sanitation] Over 50 percent of sewer backups are caused by tree roots and fats, oils and grease. Property owners are responsible for the entire private lateral. Work in the public right-of-way needs a permit from the Bureau of Engineering.
N3 [LADBS information bulletin] California requires water heaters to be strapped to resist earthquake motion, with straps in the upper and lower thirds of the tank.
N4 [California Health and Safety Code section 19211] New, replacement and existing residential water heaters must be braced, anchored or strapped against falling or horizontal displacement in an earthquake.
N5 [US Department of Energy, Energy Saver] A storage tank water heater lasts about 10 to 15 years.
N6 [US EPA] Household leaks can waste nearly 10,000 gallons of water per year in the average home.

## PAGE SPECS (use exactly the title, h1; slug; assigned facts; related service links; location links)

### burst-pipe-water-damage
- file/slug: burst-pipe-water-damage   emergency: True   photo: burst-pipe-water-damage
- title: Emergency Burst Pipe Water Damage in Marina Del Rey, CA
- h1: Emergency Burst Pipe Water Damage in Marina Del Rey, CA
- facts: F7,F8,F4,N6
- related service links (inline): /emergency-water-removal/ and /water-mitigation/
- location links (inline): /service-area/venice-ca/ and /service-area/santa-monica-ca/
- sidecard link: first related service
- angle and honesty notes: Supply line or main bursts, spray inside walls and ceilings in stacked condo buildings, shutting off at the unit stop vs building riser, who to tell (association). NOT frozen pipes (say plainly that freezing is rare on this coast and this page is about the common causes: age, pressure, corrosion, failed fittings). Differentiate from emergency water removal: this page is about the pipe failure, finding the source, wall and ceiling cavity water, not pump-out technique.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### roof-leak-water-damage
- file/slug: roof-leak-water-damage   emergency: True   photo: roof-leak-water-damage
- title: Emergency Roof Leak Water Damage in Marina Del Rey, CA
- h1: Emergency Roof Leak Water Damage in Marina Del Rey, CA
- facts: F11,F12,F16
- related service links (inline): /water-damage-repair/ and /water-mitigation/
- location links (inline): /service-area/playa-del-rey-ca/ and /service-area/venice-ca/
- sidecard link: first related service
- angle and honesty notes: Rain intrusion through flat or low-slope roofs, flashing, skylights, balcony and parapet details, stains that appear far from the entry point, tarp and temporary protection are roofer jobs while we dry, wet insulation, who owns roof (association), do not go on a wet roof. Do not link to ceiling blog. Differentiate from ceiling repair (a blog owns that) by focusing on the roof as the source and the drying of what it wetted.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### water-heater-leak-cleanup
- file/slug: water-heater-leak-cleanup   emergency: True   photo: water-heater-leak-cleanup
- title: Emergency Water Heater Leak Cleanup in Marina Del Rey, CA
- h1: Emergency Water Heater Leak Cleanup in Marina Del Rey, CA
- facts: F7,F9a,F6,N3,N4,N5
- related service links (inline): /water-damage-cleanup/ and /appliance-leak-water-damage/
- location links (inline): /service-area/playa-vista-ca/ and /service-area/culver-city-ca/
- sidecard link: first related service
- angle and honesty notes: Tank failure vs fitting leak, relief valve discharge, closet and utility room water, shut off cold supply and power or gas to the unit (gas smell means leave and call the gas utility, not us), stacked units where closet water reaches the unit below, replacement is a plumber job, bracing is code. Heating element and flooded closet drying.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### appliance-leak-water-damage
- file/slug: appliance-leak-water-damage   emergency: False   photo: appliance-leak-water-damage
- title: Appliance Leak Water Damage Cleanup in Marina Del Rey, CA
- h1: Appliance Leak Water Damage Cleanup in Marina Del Rey, CA
- facts: F4,F5,F24
- related service links (inline): /kitchen-water-damage/ and /water-damage-cleanup/
- location links (inline): /service-area/santa-monica-ca/ and /service-area/playa-vista-ca/
- sidecard link: first related service
- angle and honesty notes: Washing machine hoses and drain, dishwasher, refrigerator ice line, leaks while nobody is home, water categories (washer discharge is not clean water), under-cabinet and under-floor travel, hoses and shutoff valves as prevention. Do not cover kitchen cabinets and flooring beyond a short pointer: kitchen page owns that.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### ac-leak-water-damage
- file/slug: ac-leak-water-damage   emergency: False   photo: ac-leak-water-damage
- title: AC Leak Water Damage Repair in Marina Del Rey, CA | Dry Out
- h1: AC Leak Water Damage Repair in Marina Del Rey, CA
- facts: F8,F6,F2
- related service links (inline): /water-damage-repair/ and /drywall-water-damage-repair/
- location links (inline): /service-area/playa-vista-ca/ and /service-area/santa-monica-ca/
- sidecard link: first related service
- angle and honesty notes: Condensate drain line clog, overflow pan, air handler in closet or ceiling, ductless wall units dripping behind walls, ceiling stains below attic or soffit units, stacked units. REGIONAL HONESTY: say plainly that how much air conditioning runs near the coast varies by building and season and give no statistics, that the real local cases are condensate and ductless leaks in condos and apartments, and that refrigerant or equipment repair is an HVAC contractor job, we dry and restore.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### slab-leak-water-damage
- file/slug: slab-leak-water-damage   emergency: True   photo: slab-leak-water-damage
- title: Emergency Slab Leak Water Damage in Marina Del Rey, CA
- h1: Emergency Slab Leak Water Damage in Marina Del Rey, CA
- facts: F14,F3,F32,N6
- related service links (inline): /burst-pipe-water-damage/ and /structural-drying/
- location links (inline): /service-area/playa-del-rey-ca/ and /service-area/culver-city-ca/
- sidecard link: first related service
- angle and honesty notes: Leak in a supply or drain line under or inside a concrete slab, signs: warm spot, water meter running with fixtures off, damp flooring, sound of running water, rising bill. REGIONAL HONESTY: many harbor buildings are multi-story with concrete floors over parking, so the slab case depends on the building, say how to tell, say a leak detection plumber finds and fixes the pipe, we dry the structure and flooring. Meter check is a reader action, cite EPA fact N6 only as stated.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### crawl-space-water-damage
- file/slug: crawl-space-water-damage   emergency: True   photo: crawl-space-water-damage
- title: Emergency Crawl Space Water Damage in Marina Del Rey, CA
- h1: Emergency Crawl Space Water Damage in Marina Del Rey, CA
- facts: F16,F30,F20,F14
- related service links (inline): /structural-drying/ and /mold-remediation/
- location links (inline): /service-area/venice-ca/ and /service-area/playa-del-rey-ca/
- sidecard link: first related service
- angle and honesty notes: Standing water or damp soil under raised floors, plumbing leaks and drainage under floors, wet insulation, wet subfloor and joists, vapor barriers, sump or drain solutions are a contractor job. REGIONAL HONESTY: most condo towers around the basins have no crawl space, say so plainly without a number, and say the real cases are raised foundations on older bungalows and small buildings in places such as Venice and Playa del Rey, and for a ground-floor unit point to /flood-damage-restoration/ is NOT one of your two service links so instead mention ground-floor water only in words without a link. Safety: do not enter a wet crawl space alone, electrical hazards, confined space.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### sewage-backup-cleanup
- file/slug: sewage-backup-cleanup   emergency: True   photo: sewage-backup-cleanup
- title: Emergency Sewage Backup Cleanup in Marina Del Rey, CA | 24/7
- h1: Emergency Sewage Backup Cleanup in Marina Del Rey, CA
- facts: N1,N2,F9a
- related service links (inline): /flood-damage-restoration/ and /water-damage-cleanup/
- location links (inline): /service-area/culver-city-ca/ and /service-area/venice-ca/
- sidecard link: first related service
- angle and honesty notes: Category 3 water, floor drains and toilets backing up, main line blockage vs building line, who owns what (private lateral vs public main, condo building lines and the association), contamination handling, PPE, containment, porous materials removed, disinfecting, drying. Safety: leave the area, no kids or pets, do not use drains, do not mix chemicals. Name the EPA or county source once instead of S500 only if you also name S500 once. Differentiate from flood page: this page is about sewage from the building drain system, not storm or surface flooding.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### structural-drying
- file/slug: structural-drying   emergency: False   photo: structural-drying
- title: Structural Drying and Dehumidification in Marina Del Rey, CA
- h1: Structural Drying and Dehumidification in Marina Del Rey, CA
- facts: F10,F3,F26
- related service links (inline): /water-mitigation/ and /carpet-water-damage/
- location links (inline): /service-area/santa-monica-ca/ and /service-area/culver-city-ca/
- sidecard link: first related service
- angle and honesty notes: The drying phase itself: moisture mapping, drying goals and dry standard, air movers, LGR and desiccant dehumidifiers, heat, drying framing, subfloor, concrete, injection drying behind baseboards, monitoring visits, when to stop, why drying takes days. Differentiate from /water-mitigation/ (emergency first response): this page is the science and monitoring of drying. Do not discuss emergency extraction beyond one sentence.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### commercial-water-damage
- file/slug: commercial-water-damage   emergency: False   photo: commercial-water-damage
- title: Commercial Water Damage Restoration in Marina Del Rey, CA
- h1: Commercial Water Damage Restoration in Marina Del Rey, CA
- facts: F1,F27,F26,F31
- related service links (inline): /emergency-water-removal/ and /structural-drying/
- location links (inline): /service-area/playa-vista-ca/ and /service-area/culver-city-ca/
- sidecard link: first related service
- angle and honesty notes: Commercial and multi-tenant spaces generally: extraction, drying around business hours, protecting contents, documentation for the building owner and the business insurer, who to call first (property manager), shared walls and tenant spaces. NO industries, NO client or tenant names, NO response guarantees, NO certifications, cover only what we can do: extraction, drying, cleanup, documentation, coordination. Do not name any specific business.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### storm-water-damage
- file/slug: storm-water-damage   emergency: True   photo: storm-water-damage
- title: Emergency Storm Water Damage Cleanup in Marina Del Rey, CA
- h1: Emergency Storm Water Damage Cleanup in Marina Del Rey, CA
- facts: F10,F11,F13
- related service links (inline): /flood-damage-restoration/ and /roof-leak-water-damage/
- location links (inline): /service-area/playa-del-rey-ca/ and /service-area/culver-city-ca/
- sidecard link: first related service
- angle and honesty notes: Heavy rain events, atmospheric rivers, runoff reaching garages and ground floors, drains and downspouts overwhelmed, wind-driven rain at windows and doors, what is storm damage vs flood, flood insurance needs separate coverage (general terms, say "check the FEMA flood map for your address"), do not name any storm date or month, do not state rainfall normals.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### kitchen-water-damage
- file/slug: kitchen-water-damage   emergency: False   photo: kitchen-water-damage
- title: Kitchen Water Damage Restoration in Marina Del Rey, CA
- h1: Kitchen Water Damage Restoration in Marina Del Rey, CA
- facts: F5,F15,F24,F2
- related service links (inline): /appliance-leak-water-damage/ and /water-damage-repair/
- location links (inline): /service-area/venice-ca/ and /service-area/santa-monica-ca/
- sidecard link: first related service
- angle and honesty notes: Sink supply and drain leaks under cabinets, dishwasher and fridge lines (short pointer to the appliance page), swollen cabinet bases, laminate and tile floors, subfloor, countertop-adjacent walls, hidden cabinet moisture, what gets removed (toe kicks, base cabinets) vs dried in place, rental and shared-wall situations, who to notify.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### carpet-water-damage
- file/slug: carpet-water-damage   emergency: False   photo: carpet-water-damage
- title: Carpet Water Damage Restoration in Marina Del Rey, CA
- h1: Carpet Water Damage Restoration in Marina Del Rey, CA
- facts: F17,F21,F35,F12
- related service links (inline): /structural-drying/ and /water-damage-cleanup/
- location links (inline): /service-area/playa-del-rey-ca/ and /service-area/playa-vista-ca/
- sidecard link: first related service
- angle and honesty notes: Wet carpet and pad: clean vs contaminated water (category decides whether carpet is saved), extraction, pad removal, lifting and drying carpet in place, antimicrobial treatment, tack strip, odor, when to replace, dry time, commercial-grade equipment, protecting the subfloor. Basement water is NOT a separate page: mention briefly that below-grade rooms are rare near the harbor and ground-floor carpet is the real case.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

### drywall-water-damage-repair
- file/slug: drywall-water-damage-repair   emergency: False   photo: drywall-water-damage-repair
- title: Wall and Drywall Water Damage Repair in Marina Del Rey, CA
- h1: Wall and Drywall Water Damage Repair in Marina Del Rey, CA
- facts: F9b,F15,F22,F1
- related service links (inline): /water-damage-repair/ and /mold-remediation/
- location links (inline): /service-area/culver-city-ca/ and /service-area/venice-ca/
- sidecard link: first related service
- angle and honesty notes: Wet, stained, soft or bubbling walls: how to test (probe, moisture meter), flood cut, insulation, replacing vs drying in place, patching sequence (dry first, then cut, board, tape, texture, prime, paint), matching texture, baseboards, when permits or association approval may apply (say ask the building department), tenants and landlords. Differentiate from /water-damage-repair/ (whole rebuild) and from the ceiling blog by keeping this about walls and drywall specifically.
- emergency FAQ first question: "Is emergency {service phrase} available in Marina Del Rey?" (service phrase suits the page, e.g. burst pipe cleanup)

## VALID LINK TARGETS
Services: /water-mitigation/ /emergency-water-removal/ /flood-damage-restoration/ /water-damage-cleanup/ /water-damage-repair/ /mold-remediation/ /burst-pipe-water-damage/ /roof-leak-water-damage/ /water-heater-leak-cleanup/ /appliance-leak-water-damage/ /ac-leak-water-damage/ /slab-leak-water-damage/ /crawl-space-water-damage/ /sewage-backup-cleanup/ /structural-drying/ /commercial-water-damage/ /storm-water-damage/ /kitchen-water-damage/ /carpet-water-damage/ /drywall-water-damage-repair/
Locations: /service-area/venice-ca/ /service-area/playa-vista-ca/ /service-area/playa-del-rey-ca/ /service-area/culver-city-ca/ /service-area/santa-monica-ca/
(Only the exact 2+2 links assigned to your page. Do not link anywhere else. Do not link to /services/ or /service-area/ either.)
