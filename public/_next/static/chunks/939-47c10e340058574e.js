(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[939],{2171:function(e,t,r){"use strict";r.d(t,{Z:function(){return n}});let n=(0,r(6583).Z)("ChevronDown",[["path",{d:"m6 9 6 6 6-6",key:"qrunsl"}]])},4298:function(e,t,r){e.exports=r(3381)},4511:function(e,t,r){"use strict";r.d(t,{SV:function(){return a}});var n=r(7294);let o=(0,n.createContext)(null),i={didCatch:!1,error:null};class a extends n.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=i}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,r,n=arguments.length,o=Array(n),a=0;a<n;a++)o[a]=arguments[a];null===(t=(r=this.props).onReset)||void 0===t||t.call(r,{args:o,reason:"imperative-api"}),this.setState(i)}}componentDidCatch(e,t){var r,n;null===(r=(n=this.props).onError)||void 0===r||r.call(n,e,t)}componentDidUpdate(e,t){let{didCatch:r}=this.state,{resetKeys:n}=this.props;if(r&&null!==t.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,r)=>!Object.is(e,t[r]))}(e.resetKeys,n)){var o,a;null===(o=(a=this.props).onReset)||void 0===o||o.call(a,{next:n,prev:e.resetKeys,reason:"keys"}),this.setState(i)}}render(){let{children:e,fallbackRender:t,FallbackComponent:r,fallback:i}=this.props,{didCatch:a,error:s}=this.state,l=e;if(a){let e={error:s,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)l=t(e);else if(r)l=(0,n.createElement)(r,e);else if(void 0!==i)l=i;else throw s}return(0,n.createElement)(o.Provider,{value:{didCatch:a,error:s,resetErrorBoundary:this.resetErrorBoundary}},l)}}},6866:function(e,t,r){"use strict";r.d(t,{VY:function(){return es},h4:function(){return ei},ck:function(){return eo},fC:function(){return en},xz:function(){return ea}});var n=r(7294),o=r(5893);function i(e,t=[]){let r=[],i=()=>{let t=r.map(e=>n.createContext(e));return function(r){let o=r?.[e]||t;return n.useMemo(()=>({[`__scope${e}`]:{...r,[e]:o}}),[r,o])}};return i.scopeName=e,[function(t,i){let a=n.createContext(i),s=r.length;r=[...r,i];let l=t=>{let{scope:r,children:i,...l}=t,d=r?.[e]?.[s]||a,c=n.useMemo(()=>l,Object.values(l));return(0,o.jsx)(d.Provider,{value:c,children:i})};return l.displayName=t+"Provider",[l,function(r,o){let l=o?.[e]?.[s]||a,d=n.useContext(l);if(d)return d;if(void 0!==i)return i;throw Error(`\`${r}\` must be used within \`${t}\``)}]},function(...e){let t=e[0];if(1===e.length)return t;let r=()=>{let r=e.map(e=>({useScope:e(),scopeName:e.scopeName}));return function(e){let o=r.reduce((t,{useScope:r,scopeName:n})=>{let o=r(e)[`__scope${n}`];return{...t,...o}},{});return n.useMemo(()=>({[`__scope${t.scopeName}`]:o}),[o])}};return r.scopeName=t.scopeName,r}(i,...t)]}var a=r(4548),s=r(8771),l=r(6206),d=r(7342),c=r(5320),u=r(9981),p=e=>{let t,r;let{present:o,children:i}=e,a=function(e){var t,r;let[o,i]=n.useState(),a=n.useRef({}),s=n.useRef(e),l=n.useRef("none"),[d,c]=(t=e?"mounted":"unmounted",r={mounted:{UNMOUNT:"unmounted",ANIMATION_OUT:"unmountSuspended"},unmountSuspended:{MOUNT:"mounted",ANIMATION_END:"unmounted"},unmounted:{MOUNT:"mounted"}},n.useReducer((e,t)=>r[e][t]??e,t));return n.useEffect(()=>{let e=f(a.current);l.current="mounted"===d?e:"none"},[d]),(0,u.b)(()=>{let t=a.current,r=s.current;if(r!==e){let n=l.current,o=f(t);e?c("MOUNT"):"none"===o||t?.display==="none"?c("UNMOUNT"):r&&n!==o?c("ANIMATION_OUT"):c("UNMOUNT"),s.current=e}},[e,c]),(0,u.b)(()=>{if(o){let e;let t=o.ownerDocument.defaultView??window,r=r=>{let n=f(a.current).includes(r.animationName);if(r.target===o&&n&&(c("ANIMATION_END"),!s.current)){let r=o.style.animationFillMode;o.style.animationFillMode="forwards",e=t.setTimeout(()=>{"forwards"===o.style.animationFillMode&&(o.style.animationFillMode=r)})}},n=e=>{e.target===o&&(l.current=f(a.current))};return o.addEventListener("animationstart",n),o.addEventListener("animationcancel",r),o.addEventListener("animationend",r),()=>{t.clearTimeout(e),o.removeEventListener("animationstart",n),o.removeEventListener("animationcancel",r),o.removeEventListener("animationend",r)}}c("ANIMATION_END")},[o,c]),{isPresent:["mounted","unmountSuspended"].includes(d),ref:n.useCallback(e=>{e&&(a.current=getComputedStyle(e)),i(e)},[])}}(o),l="function"==typeof i?i({present:a.isPresent}):n.Children.only(i),d=(0,s.e)(a.ref,(t=Object.getOwnPropertyDescriptor(l.props,"ref")?.get)&&"isReactWarning"in t&&t.isReactWarning?l.ref:(t=Object.getOwnPropertyDescriptor(l,"ref")?.get)&&"isReactWarning"in t&&t.isReactWarning?l.props.ref:l.props.ref||l.ref);return"function"==typeof i||a.isPresent?n.cloneElement(l,{ref:d}):null};function f(e){return e?.animationName||"none"}p.displayName="Presence";var m=r(1276),h="Collapsible",[v,y]=i(h),[b,g]=v(h),N=n.forwardRef((e,t)=>{let{__scopeCollapsible:r,open:i,defaultOpen:a,disabled:s,onOpenChange:l,...u}=e,[p=!1,f]=(0,d.T)({prop:i,defaultProp:a,onChange:l});return(0,o.jsx)(b,{scope:r,disabled:s,contentId:(0,m.M)(),open:p,onOpenToggle:n.useCallback(()=>f(e=>!e),[f]),children:(0,o.jsx)(c.WV.div,{"data-state":j(p),"data-disabled":s?"":void 0,...u,ref:t})})});N.displayName=h;var w="CollapsibleTrigger",x=n.forwardRef((e,t)=>{let{__scopeCollapsible:r,...n}=e,i=g(w,r);return(0,o.jsx)(c.WV.button,{type:"button","aria-controls":i.contentId,"aria-expanded":i.open||!1,"data-state":j(i.open),"data-disabled":i.disabled?"":void 0,disabled:i.disabled,...n,ref:t,onClick:(0,l.M)(e.onClick,i.onOpenToggle)})});x.displayName=w;var C="CollapsibleContent",A=n.forwardRef((e,t)=>{let{forceMount:r,...n}=e,i=g(C,e.__scopeCollapsible);return(0,o.jsx)(p,{present:r||i.open,children:({present:e})=>(0,o.jsx)(R,{...n,ref:t,present:e})})});A.displayName=C;var R=n.forwardRef((e,t)=>{let{__scopeCollapsible:r,present:i,children:a,...l}=e,d=g(C,r),[p,f]=n.useState(i),m=n.useRef(null),h=(0,s.e)(t,m),v=n.useRef(0),y=v.current,b=n.useRef(0),N=b.current,w=d.open||p,x=n.useRef(w),A=n.useRef();return n.useEffect(()=>{let e=requestAnimationFrame(()=>x.current=!1);return()=>cancelAnimationFrame(e)},[]),(0,u.b)(()=>{let e=m.current;if(e){A.current=A.current||{transitionDuration:e.style.transitionDuration,animationName:e.style.animationName},e.style.transitionDuration="0s",e.style.animationName="none";let t=e.getBoundingClientRect();v.current=t.height,b.current=t.width,x.current||(e.style.transitionDuration=A.current.transitionDuration,e.style.animationName=A.current.animationName),f(i)}},[d.open,i]),(0,o.jsx)(c.WV.div,{"data-state":j(d.open),"data-disabled":d.disabled?"":void 0,id:d.contentId,hidden:!w,...l,ref:h,style:{"--radix-collapsible-content-height":y?`${y}px`:void 0,"--radix-collapsible-content-width":N?`${N}px`:void 0,...e.style},children:w&&a})});function j(e){return e?"open":"closed"}var E=r(8990),_="Accordion",O=["Home","End","ArrowDown","ArrowUp","ArrowLeft","ArrowRight"],[I,M,T]=(0,a.B)(_),[k,D]=i(_,[T,y]),U=y(),P=n.forwardRef((e,t)=>{let{type:r,...n}=e;return(0,o.jsx)(I.Provider,{scope:e.__scopeAccordion,children:"multiple"===r?(0,o.jsx)(F,{...n,ref:t}):(0,o.jsx)(V,{...n,ref:t})})});P.displayName=_;var[S,B]=k(_),[W,L]=k(_,{collapsible:!1}),V=n.forwardRef((e,t)=>{let{value:r,defaultValue:i,onValueChange:a=()=>{},collapsible:s=!1,...l}=e,[c,u]=(0,d.T)({prop:r,defaultProp:i,onChange:a});return(0,o.jsx)(S,{scope:e.__scopeAccordion,value:c?[c]:[],onItemOpen:u,onItemClose:n.useCallback(()=>s&&u(""),[s,u]),children:(0,o.jsx)(W,{scope:e.__scopeAccordion,collapsible:s,children:(0,o.jsx)(z,{...l,ref:t})})})}),F=n.forwardRef((e,t)=>{let{value:r,defaultValue:i,onValueChange:a=()=>{},...s}=e,[l=[],c]=(0,d.T)({prop:r,defaultProp:i,onChange:a}),u=n.useCallback(e=>c((t=[])=>[...t,e]),[c]),p=n.useCallback(e=>c((t=[])=>t.filter(t=>t!==e)),[c]);return(0,o.jsx)(S,{scope:e.__scopeAccordion,value:l,onItemOpen:u,onItemClose:p,children:(0,o.jsx)(W,{scope:e.__scopeAccordion,collapsible:!0,children:(0,o.jsx)(z,{...s,ref:t})})})}),[$,K]=k(_),z=n.forwardRef((e,t)=>{let{__scopeAccordion:r,disabled:i,dir:a,orientation:d="vertical",...u}=e,p=n.useRef(null),f=(0,s.e)(p,t),m=M(r),h="ltr"===(0,E.gm)(a),v=(0,l.M)(e.onKeyDown,e=>{if(!O.includes(e.key))return;let t=e.target,r=m().filter(e=>!e.ref.current?.disabled),n=r.findIndex(e=>e.ref.current===t),o=r.length;if(-1===n)return;e.preventDefault();let i=n,a=o-1,s=()=>{(i=n+1)>a&&(i=0)},l=()=>{(i=n-1)<0&&(i=a)};switch(e.key){case"Home":i=0;break;case"End":i=a;break;case"ArrowRight":"horizontal"===d&&(h?s():l());break;case"ArrowDown":"vertical"===d&&s();break;case"ArrowLeft":"horizontal"===d&&(h?l():s());break;case"ArrowUp":"vertical"===d&&l()}let c=i%o;r[c].ref.current?.focus()});return(0,o.jsx)($,{scope:r,disabled:i,direction:a,orientation:d,children:(0,o.jsx)(I.Slot,{scope:r,children:(0,o.jsx)(c.WV.div,{...u,"data-orientation":d,ref:f,onKeyDown:i?void 0:v})})})}),H="AccordionItem",[q,Z]=k(H),Y=n.forwardRef((e,t)=>{let{__scopeAccordion:r,value:n,...i}=e,a=K(H,r),s=B(H,r),l=U(r),d=(0,m.M)(),c=n&&s.value.includes(n)||!1,u=a.disabled||e.disabled;return(0,o.jsx)(q,{scope:r,open:c,disabled:u,triggerId:d,children:(0,o.jsx)(N,{"data-orientation":a.orientation,"data-state":er(c),...l,...i,ref:t,disabled:u,open:c,onOpenChange:e=>{e?s.onItemOpen(n):s.onItemClose(n)}})})});Y.displayName=H;var G="AccordionHeader",J=n.forwardRef((e,t)=>{let{__scopeAccordion:r,...n}=e,i=K(_,r),a=Z(G,r);return(0,o.jsx)(c.WV.h3,{"data-orientation":i.orientation,"data-state":er(a.open),"data-disabled":a.disabled?"":void 0,...n,ref:t})});J.displayName=G;var Q="AccordionTrigger",X=n.forwardRef((e,t)=>{let{__scopeAccordion:r,...n}=e,i=K(_,r),a=Z(Q,r),s=L(Q,r),l=U(r);return(0,o.jsx)(I.ItemSlot,{scope:r,children:(0,o.jsx)(x,{"aria-disabled":a.open&&!s.collapsible||void 0,"data-orientation":i.orientation,id:a.triggerId,...l,...n,ref:t})})});X.displayName=Q;var ee="AccordionContent",et=n.forwardRef((e,t)=>{let{__scopeAccordion:r,...n}=e,i=K(_,r),a=Z(ee,r),s=U(r);return(0,o.jsx)(A,{role:"region","aria-labelledby":a.triggerId,"data-orientation":i.orientation,...s,...n,ref:t,style:{"--radix-accordion-content-height":"var(--radix-collapsible-content-height)","--radix-accordion-content-width":"var(--radix-collapsible-content-width)",...e.style}})});function er(e){return e?"open":"closed"}et.displayName=ee;var en=P,eo=Y,ei=J,ea=X,es=et}}]);