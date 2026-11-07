def P(t): return {'t': 'p', 'text': t}
def H2(t): return {'t': 'h2', 'text': t}

PAGES = []

# ---------------------------------------------------------------- POST 3
PAGES.append({
    'type': 'blog',
    'slug': 'blog/does-home-insurance-cover-water-damage-marina-del-rey-ca',
    'category': 'general',
    'date': '2026-10-27',
    'topic': 'does home insurance cover water damage',
    'title': 'Does Home Insurance Cover Water Damage in Marina Del Rey?',
    'meta': 'Sudden pipe bursts, slow leaks, storm flooding and condo walls are treated differently by insurers. A plain guide for Marina Del Rey homeowners. Call 24/7.',
    'h1': 'Does Home Insurance Cover Water Damage in Marina Del Rey, CA?',
    'hero_sub': 'A plain-language look at which kinds of water damage policies often cover, which they often exclude, and how condo owners should read the difference.',
    'sidecard': {
        'h3': 'Documenting a water loss for your insurer',
        'copy': 'Our crews record moisture readings and photos while they work, so your claim file has facts in it.',
        'link': ('Water damage cleanup', '/water-damage-cleanup/'),
    },
    'body': [
        H2('The short answer: it depends on how the water got in'),
        P('Home insurance often covers water damage that is sudden and accidental, such as a pipe that bursts or an appliance hose that fails. It often does not cover damage from a leak that went unnoticed for a long time, from neglected maintenance, or from flooding. Flood damage usually needs a separate flood policy.'),
        P('That is a general pattern, not a promise. Every policy has its own wording, limits, deductibles and endorsements, so the only answer that counts comes from your policy and your insurer. We are a restoration company, not an insurer or adjuster, and we do not decide what a claim will pay.'),

        H2('How insurers usually sort water losses'),
        {'t': 'table', 'head': ['Situation', 'How it is often treated', 'What to ask your insurer'],
         'rows': [
             ['Pipe or supply line bursts suddenly', 'Often covered as sudden and accidental', 'Does the policy cover the resulting damage and the cost of drying'],
             ['Dishwasher or washer hose fails', 'Often covered when sudden', 'Is there a limit on appliance related water damage'],
             ['Slow leak behind a wall for months', 'Often not covered when gradual', 'How does the policy define gradual or continuous seepage'],
             ['Roof leak during a storm', 'Often covered if the roof was in sound condition', 'Does age or maintenance of the roof affect coverage'],
             ['Storm water entering from the street or a creek', 'Usually treated as flood and excluded', 'Do I have a separate flood policy or endorsement'],
             ['Sewer or drain backup', 'Often needs an added endorsement', 'Is backup coverage on my policy and what is the limit'],
             ['Mold after a covered loss', 'Varies a great deal, often capped', 'Is mold included and is there a sublimit']]},
        P('Treat that table as vocabulary for a conversation with your insurer, not as a prediction. Two homes with the same flood of water can get different answers because of wording, endorsements or the timeline of the damage.'),

        H2('Sudden versus gradual: why the timeline matters'),
        P('Adjusters look at how long water has been present. A supply line that breaks overnight leaves a clear event. A drain that has seeped for months leaves staining, rot and sometimes mold, which can look like neglect even when no one knew.'),
        P('You help yourself by finding leaks early and recording when you found them. Dated photos, a plumber\'s report and moisture readings give your insurer something concrete to evaluate. Acting quickly also matters for another reason: many policies expect owners to take reasonable steps to prevent further damage, so check yours for that wording.'),

        H2('Condo owners: what the association insures and what you do'),
        P('If you own a condo, two policies usually meet at the wall. The association typically insures the building structure and common areas as its documents describe, while your own policy usually covers your belongings, interior finishes and your liability to neighbors. The dividing line is different in every building.'),
        P('That line decides who handles a leak that starts upstairs. Ask the association for a copy of its master policy summary and your governing documents, then compare them with your own policy so you know where the gaps sit. If water moved between units, notify both your insurer and the association early.'),
        {'t': 'callout', 'h': 'One question worth asking before a loss',
         'paras': ['Ask your insurer: "If a neighbor\'s pipe floods my unit, whose policy responds first, and what do you need from me?" The answer is far easier to hear before the ceiling is wet.']},

        H2('What to document for a claim'),
        {'t': 'ul', 'items': [
            'Photos and video of the damage before anything is moved, showing the source if visible.',
            'The date, time and cause as best you know it, plus any plumber or technician report.',
            'A list of damaged belongings with approximate age and value.',
            'Moisture readings and a written scope of work from your restoration crew.',
            'Receipts for emergency steps you took, such as water extraction or temporary storage.']},
        P('A mitigation company can supply readings, photos and a drying log. Our crews work with the documentation your insurer asks for, and we explain the scope and price before work starts. We do not promise that a claim will be approved, and we do not bill insurers directly on your behalf.'),
        P('If the loss is still active, see how [water damage cleanup](/water-damage-cleanup/) is scoped in the first 48 hours, or read about [flood damage restoration](/flood-damage-restoration/) when stormwater is involved.'),

        {'t': 'cta', 'text': 'If water is already in the home, call now. Stopping the damage early helps both the repair and the paper trail.'},

        {'t': 'localnote', 'h': 'Marina Del Rey notes: creek water, flood maps and your policy',
         'paras': [
             'Ballona Creek is a roughly nine-mile flood protection channel draining a watershed of about 130 square miles, according to Los Angeles County Public Works. That watershed includes parts of Beverly Hills, Culver City, Inglewood, Los Angeles, Santa Monica, West Hollywood and unincorporated county land, and it runs near the southeast edge of the harbor. Storm runoff from all of those places moves toward it.',
             'The practical lesson is to check, not assume. Look up your address on the FEMA flood map to see its mapped zone, then compare that with the flood coverage, if any, on your policy. Ask your insurer whether stormwater entering a ground-level garage or unit would be treated as flood. Owners just upstream in [Culver City](/service-area/culver-city-ca/) and across the water in [Santa Monica](/service-area/santa-monica-ca/) should have the same conversation.']},
    ],
    'faqs': [
        ('Does homeowners insurance cover a burst pipe?',
         'Policies often cover the damage from a pipe that bursts suddenly, though the pipe repair itself may be treated differently from the water damage it caused. Read the water damage section of your policy and ask your insurer how your deductible applies.'),
        ('Is flood damage covered by regular home insurance?',
         'Usually not. Flood damage, meaning water that rises over normally dry ground, is typically excluded from standard homeowners policies and requires separate flood coverage. Ask your insurer or agent whether you have it.'),
        ('Will my claim be paid if I call a restoration company first?',
         'Calling to stop the damage is normal and many policies expect it. Keep receipts, take photos and notify your insurer promptly. We cannot promise any claim outcome, but we can document the moisture and the work performed.'),
        ('What about mold after water damage?',
         'Mold coverage varies widely and is sometimes limited or excluded. Ask whether your policy includes mold and whether there is a cap. Fixing the water problem quickly lowers the chance that mold becomes a separate issue.'),
        ('Should I check a flood map if I live on the marina side of Marina Del Rey?',
         'Yes. Use the FEMA flood map for your exact address, since conditions differ by parcel, and then ask your insurer how a storm water entry or a creek related event would be handled under your policy.'),
    ],
})

# ---------------------------------------------------------------- POST 4
PAGES.append({
    'type': 'blog',
    'slug': 'blog/mold-in-condo-walls-how-to-remove-marina-del-rey-ca',
    'category': 'mold',
    'date': '2026-10-27',
    'topic': 'mold in basement how to remove',
    'title': 'Mold in Condo Walls in Marina Del Rey: How to Remove It',
    'meta': 'Mold behind walls and in closets usually follows a hidden leak. See how it is found, what a homeowner can handle, and when to call a pro in Marina Del Rey.',
    'h1': 'Mold in Condo Walls in Marina Del Rey, CA: How It Is Found and Removed',
    'hero_sub': 'Why mold shows up inside shared-wall buildings, what you can safely do, and what removal looks like when a crew sets up containment.',
    'sidecard': {
        'h3': 'Mold in a wall or closet?',
        'copy': 'Describe what you see and where the moisture may be coming from, and we will explain the next steps.',
        'link': ('Mold remediation', '/mold-remediation/'),
    },
    'body': [
        H2('The short answer: mold in a wall is a moisture problem first'),
        P('Mold needs moisture to grow. If you find it on or inside a condo wall, something is wetting that wall, whether it is a slow pipe leak, a failed seal, a condensation line or a neighbor\'s plumbing. Wiping the surface without fixing the water only treats what is visible.'),
        P('Small, surface level spots on a hard, nonporous surface can sometimes be cleaned by a homeowner once the moisture is gone. Mold that sits inside drywall, behind baseboards or across a large area is a different job. It is removed with containment and the affected material is cut out. Our crews handle that work as part of [mold remediation](/mold-remediation/).'),

        H2('How mold ends up inside a wall'),
        P('Drywall has a paper face that holds moisture and feeds mold. A leak from a shower valve, a toilet supply line or an ice maker line can wet the back of a wall for weeks without a drop on the floor. Warm, still air in a closed cavity completes the conditions.'),
        P('Shared-wall buildings add another layer. A cavity may connect to plumbing that serves several units, so the wet area can sit on the far side of the wall from where you see the problem. A musty smell in a hallway closet can trace to a bathroom you do not even use.'),

        H2('Wipe it, watch it, or call a pro'),
        {'t': 'table', 'head': ['What you find', 'Reasonable response', 'When to call a crew'],
         'rows': [
             ['Small spots on tile, glass or sealed surface', 'Clean after fixing the moisture', 'If spots return within weeks'],
             ['Spots on painted drywall in a bathroom corner', 'Check for a leak or ventilation problem', 'If drywall is soft or the spots are spreading'],
             ['Dark patches behind furniture on an exterior wall', 'Move furniture, check the window and wall for moisture', 'If the area is larger than a few square feet'],
             ['Musty smell with no visible growth', 'Look for the source with a moisture meter', 'If a meter shows moisture in the wall'],
             ['Growth on both sides of a wall or in several rooms', 'Stop and do not disturb the area', 'Right away, before the spores are spread']]},
        P('The reason for the last row is practical. Sanding or scraping dry mold sends material into the air and into other rooms, which is how a small area turns into a larger one. If you are unsure, leave it alone and call.'),

        H2('Step one is always the water'),
        P('No mold removal lasts if the wet source is still active. A plumber closes the leak, or the association repairs the shared line, before anyone opens the wall. In a condo, that often means a conversation with the manager and sometimes a neighbor.'),
        P('Once the source is fixed, wet areas are dried. Our [water mitigation](/water-mitigation/) service covers moisture mapping, air movers and dehumidifiers, so the wall is dry before it is rebuilt. Closing a wall over damp framing gives mold a second chance.'),

        H2('What removal looks like when it is done right'),
        {'t': 'steps', 'items': [
            {'h': 'Assess and map', 'p': 'Moisture meters and visual checks outline the affected area, including areas you cannot see. Testing may be recommended to guide the scope.'},
            {'h': 'Contain', 'p': 'Plastic barriers, negative air and sealed doorways keep disturbed material inside the work area.'},
            {'h': 'Remove affected material', 'p': 'Porous materials such as drywall and insulation are cut out and bagged. Framing is cleaned and dried.'},
            {'h': 'Clean the air and surfaces', 'p': 'HEPA vacuuming and damp wiping follow. Air scrubbers run during the work.'},
            {'h': 'Verify', 'p': 'Moisture readings are checked again. Independent clearance testing is sometimes arranged when a lender, landlord or buyer asks for it.'},
            {'h': 'Rebuild', 'p': 'New drywall, paint and trim are installed, often as a separate step by a repair crew.'}]},
        P('Ask whether the company works to the published ANSI/IICRC S520 standard for mold remediation. You can ask any company that question, and the answer should be clear.'),

        H2('Closets, baseboards and the spots people forget'),
        P('Closets are a repeat offender because they hold clothes close to an exterior or plumbing wall with little airflow. Pull a few items away and look at the bottom of the wall and the baseboard. A bulging baseboard or a line of discoloration along the floor usually means moisture traveled along the framing.'),
        P('Check behind headboards, bookcases and large wall art as well. Anything that sits flat against a wall for months can hide a growing patch.'),

        {'t': 'cta', 'text': 'If you can see growth on drywall or smell mold without finding a source, call before you disturb the wall.'},

        H2('A note on health questions'),
        P('We do not diagnose or give medical advice, and no visual check can say what a particular mold means for a particular person. If anyone in the home has health concerns related to the indoor environment, speak with a physician, and tell your contractor about any sensitivities so the work is planned around them.'),

        {'t': 'localnote', 'h': 'Marina Del Rey notes: built on a former salt marsh',
         'paras': [
             'Before the harbor was developed, the land was a salt marsh fed by Ballona Creek. Today the harbor has eight basins separated by six strips of land, and most buildings stand close to water on at least one side. Proximity to water is not proof of a moisture problem inside your unit, but it is a reason to take a musty smell on an exterior wall seriously.',
             'The practical step is to check exterior walls, window sills and closets near the basins at least once each season, and to ask your manager how often the building\'s roof, windows and balcony seals are inspected. If you live in the adjacent [Venice](/service-area/venice-ca/) or [Playa del Rey](/service-area/playa-del-rey-ca/) neighborhoods, the same seasonal check applies.']},
    ],
    'faqs': [
        ('Can I remove mold from drywall myself?',
         'Small surface spots on sealed surfaces can sometimes be cleaned once the moisture is fixed. Mold that has penetrated drywall or covers a larger area is usually handled by cutting out the material under containment.'),
        ('Do I need mold testing before removal?',
         'Not always. A visual and moisture assessment is often enough to define a scope. Testing can help when the source is unclear or when someone, such as a lender or a buyer, wants documentation after the work.'),
        ('Will bleach kill the mold in my wall?',
         'Bleach on a porous surface does not reach the roots that sit inside the material, and it adds moisture. Removing affected drywall and fixing the water source is the dependable approach.'),
        ('Who is responsible for mold caused by a neighbor\'s leak?',
         'It depends on your governing documents, the cause and your insurance. Document the damage, notify the association and your insurer, and keep records of every step.'),
        ('Does living near the harbor make mold in Marina Del Rey walls more likely?',
         'Being near water is not the cause by itself. Mold needs a moisture source in the building. Because the harbor area was once marsh and many buildings sit beside basins, regular checks of exterior walls, windows and closets are a sensible habit.'),
    ],
})
