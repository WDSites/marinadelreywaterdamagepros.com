(function(){
function qs(id){return document.getElementById(id);}
var t=qs("mob-toggle"),d=qs("mob-drawer"),o=qs("mob-overlay"),c=qs("drawer-close");
function openMenu(){d.removeAttribute("hidden");o.classList.add("visible");t.setAttribute("aria-expanded","true");t.setAttribute("aria-label","Close navigation menu");document.documentElement.style.overflow="hidden";}
function closeMenu(){d.setAttribute("hidden","");o.classList.remove("visible");t.setAttribute("aria-expanded","false");t.setAttribute("aria-label","Open navigation menu");document.documentElement.style.overflow="";}
if(t&&d&&o){
t.addEventListener("click",function(){if(t.getAttribute("aria-expanded")==="true"){closeMenu();}else{openMenu();}});
if(c){c.addEventListener("click",closeMenu);}
o.addEventListener("click",closeMenu);
var links=d.querySelectorAll("a");for(var i=0;i<links.length;i++){links[i].addEventListener("click",closeMenu);}
document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeMenu();}});
var mq=window.matchMedia("(min-width: 769px)");
var onChange=function(e){if(e.matches){closeMenu();}};
if(mq.addEventListener){mq.addEventListener("change",onChange);}
}
var qb=document.querySelectorAll(".faq-q");
for(var j=0;j<qb.length;j++){qb[j].addEventListener("click",function(){var it=this.parentNode;var open=it.classList.toggle("open");this.setAttribute("aria-expanded",open?"true":"false");});}
})();
