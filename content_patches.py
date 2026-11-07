SAFETY_MOLD={'t':'ul','items':['Stop the moisture source first, because mold needs water to keep growing.','Do not mix cleaning products. Bleach and ammonia-based products can release dangerous fumes together.','Do not scrub, sand or brush dry growth, and keep fans from blowing across it.','Keep children, pets and anyone with health concerns out of the area, and take health questions to a physician.']}
PATCHES={
'blog/ceiling-water-damage-causes-and-signs-marina-del-rey-ca':{'faq':("Is there a published standard for drying a wet ceiling?","Yes. ANSI/IICRC S500 is the published standard for professional water damage restoration, and it sets drying goals based on readings from unaffected materials. A stained ceiling that looks dry can still hold moisture above it, so ask any company whether its crews work to S500 and whether it will show you the readings.")},
'blog/ceiling-water-damage-repair-marina-del-rey-ca':{'faq':("Does ceiling repair follow an industry standard?","The drying step before repair does. ANSI/IICRC S500 describes how professionals confirm that wet materials are dry before they are closed up. Repair work then follows normal building practice and any permit rules for your address, so ask the building department what applies.")},
'blog/how-to-fix-water-damaged-wood-floors-marina-del-rey-ca':{'faq':("Is there a standard for drying wet wood floors?","ANSI/IICRC S500 is the published water damage restoration standard, and floor drying is guided by moisture readings compared with dry reference wood. Ask any company whether its crews work to S500 and whether it records readings for the floor and the subfloor.")},
'blog/mold-in-bathroom-and-closet-how-to-remove-marina-del-rey-ca':{'faq':("Is there an industry standard for mold remediation?","Yes. ANSI/IICRC S520 is the published standard for professional mold remediation. It covers containment, removal and verification. Ask any company whether its crews work to S520, and ask whether it can explain how it will contain the area before work starts.")},
'blog/water-damaged-hardwood-floors-cupping-buckling-marina-del-rey-ca':{'faq':("Which standard guides drying of cupped hardwood?","ANSI/IICRC S500 is the published standard for water damage restoration, and it ties drying to moisture readings. For hardwood, that means the floor is judged by readings over time, not by how flat it looks. Ask any company whether it follows S500 and logs those readings.")},
'blog/what-kills-mold-marina-del-rey-ca':{'blocks':[{'t':'h3','text':'What to do and what not to do while you wait'},SAFETY_MOLD],'before':'localnote'},
'water-damage-repair':{'blocks':[{'t':'h3','text':'What to do before the repair crew starts'},{'t':'ul','items':['Confirm the source is fixed and the structure has been dried and measured. Rebuilding over wet materials traps moisture.','Photograph the damage and keep receipts for materials and emergency work, since your insurer or association may ask for them.','Ask your building department or association whether permits or approvals are needed before walls are closed.','Move furniture and valuables out of the work area and keep children and pets away from dust and tools.']}],'before':'cta'},
'about':{'blocks':[{'t':'h3','text':'What to do while you wait for a crew'},{'t':'ul','items':['Shut off the water at the fixture or main valve if you can reach it safely.','Leave power on in dry areas, and turn it off to wet areas only if the panel is dry and safe to reach.','Lift valuables off wet floors and keep people and pets out of contaminated water.']}],'after_h2':'How a job runs'},
}

def _cta(t): return {'t':'cta','text':t}
PATCHES.update({
'service-area/venice-ca':{'blocks':[_cta('Water moving through a Venice walk street home or a shop on Abbot Kinney? Call the 24/7 line and tell us the nearest cross street.')]},
'service-area/playa-vista-ca':{'blocks':[_cta('Leak in a Playa Vista townhome or a Runway-area building? Call the 24/7 line with your building and unit number.')]},
'service-area/playa-del-rey-ca':{'blocks':[_cta('Water near the lagoons, the bluffs or the beach side of Playa del Rey? Call the 24/7 line and describe where it started.')]},
'service-area/culver-city-ca':{'blocks':[_cta('Water in a Culver City garage, studio-area building or Fox Hills home? Call the 24/7 line and give us the street.')]},
'service-area/santa-monica-ca':{'blocks':[_cta('Leak in a Santa Monica apartment, condo or bungalow? Call the 24/7 line and tell us which floor the water reached.')]},
'services':{'blocks':[_cta('Ready to talk through a loss? The 24/7 line is open now.')]},
'service-area':{'blocks':[_cta('Tell the dispatcher your street and cross street and we will confirm coverage on the spot.')]},
'contact':{'blocks':[_cta('Calling is faster than writing, and the line never closes.')]},
})

_B='blog/%s-marina-del-rey-ca'
_AL={
 'ceiling-water-damage-causes-and-signs':'If the stain sits under a roof or balcony, the [roof leak water damage](/roof-leak-water-damage/) page explains how that source is traced and the area dried.',
 'ceiling-water-damage-repair':'Walls that took the same water have their own page on [wall and drywall water damage repair](/drywall-water-damage-repair/).',
 'does-home-insurance-cover-water-damage':'A supply line that fails inside a wall is the kind of sudden loss described on the [burst pipe water damage](/burst-pipe-water-damage/) page.',
 'ground-floor-garage-water-cleanup':'Rain that reaches a garage from outside is covered on the [storm water damage](/storm-water-damage/) page.',
 'how-to-fix-water-damaged-wood-floors':'How drying is measured and monitored is explained on the [structural drying](/structural-drying/) page.',
 'is-mold-on-ceiling-dangerous':'A clogged air conditioner drain is one possible source, covered on the [AC leak water damage repair](/ac-leak-water-damage/) page.',
 'mold-in-bathroom-and-closet-how-to-remove':'A leaking tank in a utility closet is one common source, covered on the [water heater leak cleanup](/water-heater-leak-cleanup/) page.',
 'mold-in-condo-walls-how-to-remove':'Once the cavity is dry, the [wall and drywall water damage repair](/drywall-water-damage-repair/) page explains the patching sequence.',
 'water-damage-drying-company-how-to-choose':'Wet carpet and padding have their own page on [carpet water damage restoration](/carpet-water-damage/).',
 'water-damaged-hardwood-floors-cupping-buckling':'A dishwasher or sink leak is a common starting point, covered on the [kitchen water damage](/kitchen-water-damage/) page.',
 'what-is-water-damage-restoration':'Water that comes back up a drain is a different case, covered on the [sewage backup cleanup](/sewage-backup-cleanup/) page.',
}
for k,v in _AL.items():
    PATCHES.setdefault(_B%k,{})['addlink']=v

PATCHES.setdefault('roof-leak-water-damage',{}).update({'blocks':[{'t':'cta','text':'Water coming through a ceiling or window frame? Describe where it enters and the dispatcher will start the plan.'}],'before':'h2'})
PATCHES.setdefault('water-heater-leak-cleanup',{}).update({'blocks':[{'t':'cta','text':'Tank leaking or closet floor wet? Tell the dispatcher what you see and which rooms are affected.'}],'before':'h2'})
PATCHES.setdefault('appliance-leak-water-damage',{}).update({'blocks':[{'t':'cta','text':'Washer, dishwasher or fridge line leaked? Describe the wet area and the dispatcher will explain the next step.'}],'before':'h2'})
