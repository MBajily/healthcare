/*
 Highcharts JS v5.0.2 (2016-10-26)
 Exporting module

 (c) 2010-2016 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(q){"object"===typeof module&&module.exports?module.exports=q:q(Highcharts)})(function(q){(function(f){var q=f.defaultOptions,v=f.doc,A=f.Chart,x=f.addEvent,F=f.removeEvent,G=f.fireEvent,w=f.createElement,B=f.discardElement,H=f.css,p=f.merge,C=f.pick,u=f.each,y=f.extend,I=f.splat,z=f.win,D=f.SVGRenderer,J=f.Renderer.prototype.symbols;y(q.lang,{printChart:"Print chart",downloadPNG:"Download PNG image",downloadJPEG:"Download JPEG image",downloadPDF:"Download PDF document",downloadSVG:"Download SVG vector image",
contextButtonTitle:"Chart context menu"});q.navigation={buttonOptions:{theme:{},symbolSize:14,symbolX:12.5,symbolY:10.5,align:"right",buttonSpacing:3,height:22,verticalAlign:"top",width:24}};q.exporting={type:"image/png",url:"https://export.highcharts.com/",printMaxWidth:780,scale:2,buttons:{contextButton:{className:"highcharts-contextbutton",menuClassName:"highcharts-contextmenu",symbol:"menu",_titleKey:"contextButtonTitle",menuItems:[{textKey:"printChart",onclick:function(){this.print()}},{separator:!0},
{textKey:"downloadPNG",onclick:function(){this.exportChart()}},{textKey:"downloadJPEG",onclick:function(){this.exportChart({type:"image/jpeg"})}},{textKey:"downloadPDF",onclick:function(){this.exportChart({type:"application/pdf"})}},{textKey:"downloadSVG",onclick:function(){this.exportChart({type:"image/svg+xml"})}}]}}};f.post=function(a,b,d){var e;a=w("form",p({method:"post",action:a,enctype:"multipart/form-data"},d),{display:"none"},v.body);for(e in b)w("input",{type:"hidden",name:e,value:b[e]},
null,a);a.submit();B(a)};y(A.prototype,{sanitizeSVG:function(a){return a=a.replace(/zIndex="[^"]+"/g,"").replace(/isShadow="[^"]+"/g,"").replace(/symbolName="[^"]+"/g,"").replace(/jQuery[0-9]+="[^"]+"/g,"").replace(/url\(("|&quot;)(\S+)("|&quot;)\)/g,"url($2)").replace(/url\([^#]+#/g,"url(#").replace(/<svg /,'\x3csvg xmlns:xlink\x3d"http://www.w3.org/1999/xlink" ').replace(/ (NS[0-9]+\:)?href=/g," xlink:href\x3d").replace(/\n/," ").replace(/<\/svg>.*?$/,"\x3c/svg\x3e").replace(/(fill|stroke)="rgba\(([ 0-9]+,[ 0-9]+,[ 0-9]+),([ 0-9\.]+)\)"/g,
'$1\x3d"rgb($2)" $1-opacity\x3d"$3"').replace(/&nbsp;/g,"\u00a0").replace(/&shy;/g,"\u00ad")},getChartHTML:function(){this.inlineStyles();return this.container.innerHTML},getSVG:function(a){var b=this,d,e,g,E,k,c=p(b.options,a),n=c.exporting.allowHTML;v.createElementNS||(v.createElementNS=function(a,b){return v.createElement(b)});e=w("div",null,{position:"absolute",top:"-9999em",width:b.chartWidth+"px",height:b.chartHeight+"px"},v.body);g=b.renderTo.style.width;k=b.renderTo.style.height;g=c.exporting.sourceWidth||
c.chart.width||/px$/.test(g)&&parseInt(g,10)||600;k=c.exporting.sourceHeight||c.chart.height||/px$/.test(k)&&parseInt(k,10)||400;y(c.chart,{animation:!1,renderTo:e,forExport:!0,renderer:"SVGRenderer",width:g,height:k});c.exporting.enabled=!1;delete c.data;c.series=[];u(b.series,function(a){E=p(a.userOptions,{animation:!1,enableMouseTracking:!1,showCheckbox:!1,visible:a.visible});E.isInternal||c.series.push(E)});a&&u(["xAxis","yAxis"],function(b){u(I(a[b]),function(a,e){c[b][e]=p(c[b][e],a)})});d=
new f.Chart(c,b.callback);u(["xAxis","yAxis"],function(a){u(b[a],function(b,e){e=d[a][e];var c=b.getExtremes();b=c.userMin;c=c.userMax;!e||void 0===b&&void 0===c||e.setExtremes(b,c,!0,!1)})});g=d.getChartHTML();c=null;d.destroy();B(e);n&&(e=g.match(/<\/svg>(.*?$)/))&&(e='\x3cforeignObject x\x3d"0" y\x3d"0" width\x3d"200" height\x3d"200"\x3e\x3cbody xmlns\x3d"http://www.w3.org/1999/xhtml"\x3e'+e[1]+"\x3c/body\x3e\x3c/foreignObject\x3e",g=g.replace("\x3c/svg\x3e",e+"\x3c/svg\x3e"));g=this.sanitizeSVG(g);
return g=g.replace(/(url\(#highcharts-[0-9]+)&quot;/g,"$1").replace(/&quot;/g,"'")},getSVGForExport:function(a,b){var d=this.options.exporting;return this.getSVG(p({chart:{borderRadius:0}},d.chartOptions,b,{exporting:{sourceWidth:a&&a.sourceWidth||d.sourceWidth,sourceHeight:a&&a.sourceHeight||d.sourceHeight}}))},exportChart:function(a,b){b=this.getSVGForExport(a,b);a=p(this.options.exporting,a);f.post(a.url,{filename:a.filename||"chart",type:a.type,width:a.width||0,scale:a.scale,svg:b},a.formAttributes)},
print:function(){var a=this,b=a.container,d=[],e=b.parentNode,g=v.body,f=g.childNodes,k=a.options.exporting.printMaxWidth,c,n;if(!a.isPrinting){a.isPrinting=!0;a.pointer.reset(null,0);G(a,"beforePrint");if(n=k&&a.chartWidth>k)c=[a.options.chart.width,void 0,!1],a.setSize(k,void 0,!1);u(f,function(a,b){1===a.nodeType&&(d[b]=a.style.display,a.style.display="none")});g.appendChild(b);z.focus();z.print();setTimeout(function(){e.appendChild(b);u(f,function(a,b){1===a.nodeType&&(a.style.display=d[b])});
a.isPrinting=!1;n&&a.setSize.apply(a,c);G(a,"afterPrint")},1E3)}},contextMenu:function(a,b,d,e,g,f,k){var c=this,n=c.chartWidth,h=c.chartHeight,l="cache-"+a,m=c[l],r=Math.max(g,f),t,p,q=function(b){c.pointer.inClass(b.target,a)||p()};m||(c[l]=m=w("div",{className:a},{position:"absolute",zIndex:1E3,padding:r+"px"},c.container),t=w("div",{className:"highcharts-menu"},null,m),p=function(){H(m,{display:"none"});k&&k.setState(0);c.openMenu=!1},x(m,"mouseleave",function(){m.hideTimer=setTimeout(p,500)}),
x(m,"mouseenter",function(){clearTimeout(m.hideTimer)}),x(v,"mouseup",q),x(c,"destroy",function(){F(v,"mouseup",q)}),u(b,function(a){if(a){var b;b=a.separator?w("hr",null,null,t):w("div",{className:"highcharts-menu-item",onclick:function(b){b&&b.stopPropagation();p();a.onclick&&a.onclick.apply(c,arguments)},innerHTML:a.text||c.options.lang[a.textKey]},null,t);c.exportDivElements.push(b)}}),c.exportDivElements.push(t,m),c.exportMenuWidth=m.offsetWidth,c.exportMenuHeight=m.offsetHeight);b={display:"block"};
d+c.exportMenuWidth>n?b.right=n-d-g-r+"px":b.left=d-r+"px";e+f+c.exportMenuHeight>h&&"top"!==k.alignOptions.verticalAlign?b.bottom=h-e-r+"px":b.top=e+f-r+"px";H(m,b);c.openMenu=!0},addButton:function(a){var b=this,d=b.renderer,e=p(b.options.navigation.buttonOptions,a),g=e.onclick,f=e.menuItems,k,c,n=e.symbolSize||12;b.btnCount||(b.btnCount=0);b.exportDivElements||(b.exportDivElements=[],b.exportSVGElements=[]);if(!1!==e.enabled){var h=e.theme,l=h.states,m=l&&l.hover,l=l&&l.select,r;delete h.states;
g?r=function(a){a.stopPropagation();g.call(b,a)}:f&&(r=function(){b.contextMenu(c.menuClassName,f,c.translateX,c.translateY,c.width,c.height,c);c.setState(2)});e.text&&e.symbol?h.paddingLeft=C(h.paddingLeft,25):e.text||y(h,{width:e.width,height:e.height,padding:0});c=d.button(e.text,0,0,r,h,m,l).addClass(a.className).attr({title:b.options.lang[e._titleKey],zIndex:3});c.menuClassName=a.menuClassName||"highcharts-menu-"+b.btnCount++;e.symbol&&(k=d.symbol(e.symbol,e.symbolX-n/2,e.symbolY-n/2,n,n).addClass("highcharts-button-symbol").attr({zIndex:1}).add(c));
c.add().align(y(e,{width:c.width,x:C(e.x,b.buttonOffset)}),!0,"spacingBox");b.buttonOffset+=(c.width+e.buttonSpacing)*("right"===e.align?-1:1);b.exportSVGElements.push(c,k)}},destroyExport:function(a){var b=a?a.target:this;a=b.exportSVGElements;var d=b.exportDivElements;a&&(u(a,function(a,d){a&&(a.onclick=a.ontouchstart=null,b.exportSVGElements[d]=a.destroy())}),a.length=0);d&&(u(d,function(a,d){clearTimeout(a.hideTimer);F(a,"mouseleave");b.exportDivElements[d]=a.onmouseout=a.onmouseover=a.ontouchstart=
a.onclick=null;B(a)}),d.length=0)}});D.prototype.inlineToAttributes="fill stroke strokeLinecap strokeLinejoin strokeWidth textAnchor x y".split(" ");D.prototype.inlineBlacklist=[/-/,/^(clipPath|cssText|d|height|width)$/,/^font$/,/[lL]ogical(Width|Height)$/,/perspective/,/TapHighlightColor/,/^transition/];D.prototype.unstyledElements=["clipPath","defs","desc"];A.prototype.inlineStyles=function(){function a(a){return a.replace(/([A-Z])/g,function(a,b){return"-"+b.toLowerCase()})}function b(d){var h,
l,m,r="",t,n;if(1===d.nodeType&&-1===q.indexOf(d.nodeName)){l=z.getComputedStyle(d,null);m="svg"===d.nodeName?{}:z.getComputedStyle(d.parentNode,null);k[d.nodeName]||(c||(c=v.createElementNS(f.SVG_NS,"svg"),c.setAttribute("version","1.1"),v.body.appendChild(c)),t=v.createElementNS(d.namespaceURI,d.nodeName),c.appendChild(t),k[d.nodeName]=p(z.getComputedStyle(t,null)),c.removeChild(t));for(h in l){t=!1;for(n=g.length;n--&&!t;)t=g[n].test(h)||"function"===typeof l[h];t||m[h]!==l[h]&&k[d.nodeName][h]!==
l[h]&&(-1!==e.indexOf(h)?d.setAttribute(a(h),l[h]):r+=a(h)+":"+l[h]+";")}r&&(h=d.getAttribute("style"),d.setAttribute("style",(h?h+";":"")+r));"text"!==d.nodeName&&u(d.children||d.childNodes,b)}}var d=this.renderer,e=d.inlineToAttributes,g=d.inlineBlacklist,q=d.unstyledElements,k={},c;b(this.container.querySelector("svg"));c.parentNode.removeChild(c)};J.menu=function(a,b,d,e){return["M",a,b+2.5,"L",a+d,b+2.5,"M",a,b+e/2+.5,"L",a+d,b+e/2+.5,"M",a,b+e-1.5,"L",a+d,b+e-1.5]};A.prototype.renderExporting=
function(){var a,b=this.options.exporting,d=b.buttons,e=this.isDirtyExporting||!this.exportSVGElements;this.buttonOffset=0;this.isDirtyExporting&&this.destroyExport();if(e&&!1!==b.enabled){for(a in d)this.addButton(d[a]);this.isDirtyExporting=!1}x(this,"destroy",this.destroyExport)};A.prototype.callbacks.push(function(a){a.renderExporting();x(a,"redraw",a.renderExporting);u(["exporting","navigation"],function(b){a[b]={update:function(d,e){a.isDirtyExporting=!0;p(!0,a.options[b],d);C(e,!0)&&a.redraw()}}})})})(q)});
