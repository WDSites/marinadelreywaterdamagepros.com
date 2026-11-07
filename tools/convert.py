import json,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from pick import *
from PIL import Image
OUT='/home/claude/mdr/images'
os.makedirs(OUT+'/blog',exist_ok=True)
ALT={
 'burst-pipe-water-damage':'Water spraying from a burst joint in an exposed metal pipe against a red wall',
 'roof-leak-water-damage':'Water dripping from a stained ceiling panel',
 'water-heater-leak-cleanup':'White tank water heater with chrome supply fittings and tools beside it',
 'appliance-leak-water-damage':'Water running from the base of a front-loading washing machine onto the floor',
 'ac-leak-water-damage':'Water droplets falling from the underside of a wall-mounted air conditioner',
 'slab-leak-water-damage':'Water welling up through a crack in a concrete floor slab',
 'crawl-space-water-damage':'Rusty pipe dripping into a wet patch of soil under a raised wood floor',
 'sewage-backup-cleanup':'Gloved hand pointing at grime around an open floor drain beside a scrub brush',
 'structural-drying':'Hand holding a moisture meter against a painted block wall to check for moisture',
 'commercial-water-damage':'Office floor covered in water with a desk, laptop and chairs sitting in it',
 'storm-water-damage':'Flooded living room with water covering the floor in front of a sofa and television',
 'kitchen-water-damage':'Modern kitchen with water covering the floor and chairs knocked over',
 'carpet-water-damage':'Large wet stain spreading across beige carpet in a room',
 'drywall-water-damage-repair':'Wall cut open to the studs with green air movers drying the room',
 'home':'Blue air movers and a dehumidifier drying a wet carpeted living room',
 'emergency-water-removal':'Technician extracting standing water from a living room floor with a hose and air movers',
 'flood-damage-restoration':'Flooded hardwood floor in a bright room with tall windows after a flood',
 'mold-remediation':'Technician in protective suit and respirator treating a mold-stained wall',
 'water-damage-cleanup':'Person in yellow rubber boots mopping standing water in a living room',
 'water-damage-repair':'Two workers kneeling on a bare floor during water damage repair',
 'water-mitigation':'Technician working with drying equipment in a flooded room',
 'blog/ceiling-causes':'Water stain spreading across a stained ceiling tile in the corner of a room',
 'blog/ceiling-repair':'Peeling paint and damaged plaster on a water-damaged ceiling',
 'blog/insurance':'Homeowner photographing a water-stained wall while another person holds a bucket',
 'blog/garage':'Standing water on a garage floor in front of shelves and a garage door',
 'blog/wood-floors-fix':'Wood floor planks lifted from a wet subfloor with plastic sheeting along the wall',
 'blog/mold-ceiling':'Gloved hand with a spray bottle beside mold growth along a ceiling edge',
 'blog/mold-bathroom':'Mold on a corner wall with cleaning spray, gloves and a sponge on the floor',
 'blog/mold-condo':'Mold spreading up a wall above the baseboard in the corner of a room',
 'blog/mold-cost':'Large area of dark mold growth across an interior wall',
 'blog/mold-expect':'Crew in white protective suits working inside a room with mold on the walls',
 'blog/drying-company':'Blue and red air movers set up to dry a tiled floor',
 'blog/hardwood-cupping':'Water droplet on a wet wood floor with boards beginning to lift',
 'blog/what-is-restoration':'Technician setting up equipment in a flooded hallway',
 'blog/black-mold':'Black and green mold on a peeling painted wall',
 'blog/kills-mold':'Gloved hands scrubbing a moldy wall with a sponge and spray bottle',
}
for k,(d,n) in PICKS.items():
    im=Image.open(f'{R}{d}/{n}.jpg').convert('RGB')
    big=im if k in('home',) or '/' not in k else im.resize((1280,720),Image.LANCZOS)
    if k=='home' or '/' not in k: big=im.resize((1600,900),Image.LANCZOS)
    big.save(f'{OUT}/{k}.webp','WEBP',quality=74,method=6)
    if k.startswith('blog/'):
        im.resize((640,360),Image.LANCZOS).save(f'{OUT}/{k}-thumb.webp','WEBP',quality=76,method=6)
json.dump(ALT,open(OUT+'/alt.json','w'),indent=1)
print(sum(os.path.getsize(os.path.join(dp,f)) for dp,_,fs in os.walk(OUT) for f in fs)//1024,'KB')
