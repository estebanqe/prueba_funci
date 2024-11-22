"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[503],{1568:function(e,t,r){r.d(t,{Z:function(){return n}});let n=(0,r(9648).Z)("ChevronDown",[["path",{d:"m6 9 6 6 6-6",key:"qrunsl"}]])},7398:function(e,t,r){r.d(t,{VY:function(){return ea},h4:function(){return el},ck:function(){return en},fC:function(){return er},xz:function(){return eo}});var n=r(7294),l=r(5360),o=r(4548),a=r(8771),i=r(6206),d=r(7342),u=r(9602),s=r(9981),c=r(9115),f=r(1276),m=r(5893),p="Collapsible",[h,v]=(0,l.b)(p),[b,C]=h(p),g=n.forwardRef((e,t)=>{let{__scopeCollapsible:r,open:l,defaultOpen:o,disabled:a,onOpenChange:i,...s}=e,[c=!1,p]=(0,d.T)({prop:l,defaultProp:o,onChange:i});return(0,m.jsx)(b,{scope:r,disabled:a,contentId:(0,f.M)(),open:c,onOpenToggle:n.useCallback(()=>p(e=>!e),[p]),children:(0,m.jsx)(u.WV.div,{"data-state":k(c),"data-disabled":a?"":void 0,...s,ref:t})})});g.displayName=p;var y="CollapsibleTrigger",w=n.forwardRef((e,t)=>{let{__scopeCollapsible:r,...n}=e,l=C(y,r);return(0,m.jsx)(u.WV.button,{type:"button","aria-controls":l.contentId,"aria-expanded":l.open||!1,"data-state":k(l.open),"data-disabled":l.disabled?"":void 0,disabled:l.disabled,...n,ref:t,onClick:(0,i.M)(e.onClick,l.onOpenToggle)})});w.displayName=y;var E="CollapsibleContent",x=n.forwardRef((e,t)=>{let{forceMount:r,...n}=e,l=C(E,e.__scopeCollapsible);return(0,m.jsx)(c.z,{present:r||l.open,children:({present:e})=>(0,m.jsx)(R,{...n,ref:t,present:e})})});x.displayName=E;var R=n.forwardRef((e,t)=>{let{__scopeCollapsible:r,present:l,children:o,...i}=e,d=C(E,r),[c,f]=n.useState(l),p=n.useRef(null),h=(0,a.e)(t,p),v=n.useRef(0),b=v.current,g=n.useRef(0),y=g.current,w=d.open||c,x=n.useRef(w),R=n.useRef();return n.useEffect(()=>{let e=requestAnimationFrame(()=>x.current=!1);return()=>cancelAnimationFrame(e)},[]),(0,s.b)(()=>{let e=p.current;if(e){R.current=R.current||{transitionDuration:e.style.transitionDuration,animationName:e.style.animationName},e.style.transitionDuration="0s",e.style.animationName="none";let t=e.getBoundingClientRect();v.current=t.height,g.current=t.width,x.current||(e.style.transitionDuration=R.current.transitionDuration,e.style.animationName=R.current.animationName),f(l)}},[d.open,l]),(0,m.jsx)(u.WV.div,{"data-state":k(d.open),"data-disabled":d.disabled?"":void 0,id:d.contentId,hidden:!w,...i,ref:h,style:{"--radix-collapsible-content-height":b?`${b}px`:void 0,"--radix-collapsible-content-width":y?`${y}px`:void 0,...e.style},children:w&&o})});function k(e){return e?"open":"closed"}var F=r(8990),A="Accordion",N=["Home","End","ArrowDown","ArrowUp","ArrowLeft","ArrowRight"],[_,j,M]=(0,o.B)(A),[S,I]=(0,l.b)(A,[M,v]),T=v(),V=n.forwardRef((e,t)=>{let{type:r,...n}=e;return(0,m.jsx)(_.Provider,{scope:e.__scopeAccordion,children:"multiple"===r?(0,m.jsx)(q,{...n,ref:t}):(0,m.jsx)(O,{...n,ref:t})})});V.displayName=A;var[D,Z]=S(A),[P,$]=S(A,{collapsible:!1}),O=n.forwardRef((e,t)=>{let{value:r,defaultValue:l,onValueChange:o=()=>{},collapsible:a=!1,...i}=e,[u,s]=(0,d.T)({prop:r,defaultProp:l,onChange:o});return(0,m.jsx)(D,{scope:e.__scopeAccordion,value:u?[u]:[],onItemOpen:s,onItemClose:n.useCallback(()=>a&&s(""),[a,s]),children:(0,m.jsx)(P,{scope:e.__scopeAccordion,collapsible:a,children:(0,m.jsx)(z,{...i,ref:t})})})}),q=n.forwardRef((e,t)=>{let{value:r,defaultValue:l,onValueChange:o=()=>{},...a}=e,[i=[],u]=(0,d.T)({prop:r,defaultProp:l,onChange:o}),s=n.useCallback(e=>u((t=[])=>[...t,e]),[u]),c=n.useCallback(e=>u((t=[])=>t.filter(t=>t!==e)),[u]);return(0,m.jsx)(D,{scope:e.__scopeAccordion,value:i,onItemOpen:s,onItemClose:c,children:(0,m.jsx)(P,{scope:e.__scopeAccordion,collapsible:!0,children:(0,m.jsx)(z,{...a,ref:t})})})}),[L,W]=S(A),z=n.forwardRef((e,t)=>{let{__scopeAccordion:r,disabled:l,dir:o,orientation:d="vertical",...s}=e,c=n.useRef(null),f=(0,a.e)(c,t),p=j(r),h="ltr"===(0,F.gm)(o),v=(0,i.M)(e.onKeyDown,e=>{if(!N.includes(e.key))return;let t=e.target,r=p().filter(e=>!e.ref.current?.disabled),n=r.findIndex(e=>e.ref.current===t),l=r.length;if(-1===n)return;e.preventDefault();let o=n,a=l-1,i=()=>{(o=n+1)>a&&(o=0)},u=()=>{(o=n-1)<0&&(o=a)};switch(e.key){case"Home":o=0;break;case"End":o=a;break;case"ArrowRight":"horizontal"===d&&(h?i():u());break;case"ArrowDown":"vertical"===d&&i();break;case"ArrowLeft":"horizontal"===d&&(h?u():i());break;case"ArrowUp":"vertical"===d&&u()}let s=o%l;r[s].ref.current?.focus()});return(0,m.jsx)(L,{scope:r,disabled:l,direction:o,orientation:d,children:(0,m.jsx)(_.Slot,{scope:r,children:(0,m.jsx)(u.WV.div,{...s,"data-orientation":d,ref:f,onKeyDown:l?void 0:v})})})}),B="AccordionItem",[H,U]=S(B),K=n.forwardRef((e,t)=>{let{__scopeAccordion:r,value:n,...l}=e,o=W(B,r),a=Z(B,r),i=T(r),d=(0,f.M)(),u=n&&a.value.includes(n)||!1,s=o.disabled||e.disabled;return(0,m.jsx)(H,{scope:r,open:u,disabled:s,triggerId:d,children:(0,m.jsx)(g,{"data-orientation":o.orientation,"data-state":et(u),...i,...l,ref:t,disabled:s,open:u,onOpenChange:e=>{e?a.onItemOpen(n):a.onItemClose(n)}})})});K.displayName=B;var Y="AccordionHeader",G=n.forwardRef((e,t)=>{let{__scopeAccordion:r,...n}=e,l=W(A,r),o=U(Y,r);return(0,m.jsx)(u.WV.h3,{"data-orientation":l.orientation,"data-state":et(o.open),"data-disabled":o.disabled?"":void 0,...n,ref:t})});G.displayName=Y;var J="AccordionTrigger",Q=n.forwardRef((e,t)=>{let{__scopeAccordion:r,...n}=e,l=W(A,r),o=U(J,r),a=$(J,r),i=T(r);return(0,m.jsx)(_.ItemSlot,{scope:r,children:(0,m.jsx)(w,{"aria-disabled":o.open&&!a.collapsible||void 0,"data-orientation":l.orientation,id:o.triggerId,...i,...n,ref:t})})});Q.displayName=J;var X="AccordionContent",ee=n.forwardRef((e,t)=>{let{__scopeAccordion:r,...n}=e,l=W(A,r),o=U(X,r),a=T(r);return(0,m.jsx)(x,{role:"region","aria-labelledby":o.triggerId,"data-orientation":l.orientation,...a,...n,ref:t,style:{"--radix-accordion-content-height":"var(--radix-collapsible-content-height)","--radix-accordion-content-width":"var(--radix-collapsible-content-width)",...e.style}})});function et(e){return e?"open":"closed"}ee.displayName=X;var er=V,en=K,el=G,eo=Q,ea=ee},1149:function(e,t,r){r.d(t,{fC:function(){return $}});var n=r(7462),l=r(7294),o=r.t(l,2);function a(e,t,{checkForDefaultPrevented:r=!0}={}){return function(n){if(null==e||e(n),!1===r||!n.defaultPrevented)return null==t?void 0:t(n)}}function i(...e){return t=>e.forEach(e=>{"function"==typeof e?e(t):null!=e&&(e.current=t)})}function d(...e){return(0,l.useCallback)(i(...e),e)}let u=(null==globalThis?void 0:globalThis.document)?l.useLayoutEffect:()=>{},s=o["useId".toString()]||(()=>void 0),c=0;function f(e){let[t,r]=l.useState(s());return u(()=>{e||r(e=>null!=e?e:String(c++))},[e]),e||(t?`radix-${t}`:"")}r(3935);let m=(0,l.forwardRef)((e,t)=>{let{children:r,...o}=e,a=l.Children.toArray(r),i=a.find(v);if(i){let e=i.props.children,r=a.map(t=>t!==i?t:l.Children.count(e)>1?l.Children.only(null):(0,l.isValidElement)(e)?e.props.children:null);return(0,l.createElement)(p,(0,n.Z)({},o,{ref:t}),(0,l.isValidElement)(e)?(0,l.cloneElement)(e,void 0,r):null)}return(0,l.createElement)(p,(0,n.Z)({},o,{ref:t}),r)});m.displayName="Slot";let p=(0,l.forwardRef)((e,t)=>{let{children:r,...n}=e;return(0,l.isValidElement)(r)?(0,l.cloneElement)(r,{...function(e,t){let r={...t};for(let n in t){let l=e[n],o=t[n];/^on[A-Z]/.test(n)?l&&o?r[n]=(...e)=>{o(...e),l(...e)}:l&&(r[n]=l):"style"===n?r[n]={...l,...o}:"className"===n&&(r[n]=[l,o].filter(Boolean).join(" "))}return{...e,...r}}(n,r.props),ref:t?function(...e){return t=>e.forEach(e=>{"function"==typeof e?e(t):null!=e&&(e.current=t)})}(t,r.ref):r.ref}):l.Children.count(r)>1?l.Children.only(null):null});p.displayName="SlotClone";let h=({children:e})=>(0,l.createElement)(l.Fragment,null,e);function v(e){return(0,l.isValidElement)(e)&&e.type===h}let b=["a","button","div","form","h2","h3","img","input","label","li","nav","ol","p","span","svg","ul"].reduce((e,t)=>{let r=(0,l.forwardRef)((e,r)=>{let{asChild:o,...a}=e,i=o?m:t;return(0,l.useEffect)(()=>{window[Symbol.for("radix-ui")]=!0},[]),(0,l.createElement)(i,(0,n.Z)({},a,{ref:r}))});return r.displayName=`Primitive.${t}`,{...e,[t]:r}},{}),C=((e,t)=>(0,l.createElement)(b.label,(0,n.Z)({},e,{ref:t,onMouseDown:t=>{var r;null===(r=e.onMouseDown)||void 0===r||r.call(e,t),!t.defaultPrevented&&t.detail>1&&t.preventDefault()}})),(0,l.forwardRef)((e,t)=>{let{children:r,...o}=e,a=l.Children.toArray(r),i=a.find(w);if(i){let e=i.props.children,r=a.map(t=>t!==i?t:l.Children.count(e)>1?l.Children.only(null):(0,l.isValidElement)(e)?e.props.children:null);return(0,l.createElement)(g,(0,n.Z)({},o,{ref:t}),(0,l.isValidElement)(e)?(0,l.cloneElement)(e,void 0,r):null)}return(0,l.createElement)(g,(0,n.Z)({},o,{ref:t}),r)}));C.displayName="Slot";let g=(0,l.forwardRef)((e,t)=>{let{children:r,...n}=e;return(0,l.isValidElement)(r)?(0,l.cloneElement)(r,{...function(e,t){let r={...t};for(let n in t){let l=e[n],o=t[n];/^on[A-Z]/.test(n)?l&&o?r[n]=(...e)=>{o(...e),l(...e)}:l&&(r[n]=l):"style"===n?r[n]={...l,...o}:"className"===n&&(r[n]=[l,o].filter(Boolean).join(" "))}return{...e,...r}}(n,r.props),ref:t?i(t,r.ref):r.ref}):l.Children.count(r)>1?l.Children.only(null):null});g.displayName="SlotClone";let y=({children:e})=>(0,l.createElement)(l.Fragment,null,e);function w(e){return(0,l.isValidElement)(e)&&e.type===y}let E=["a","button","div","form","h2","h3","img","input","label","li","nav","ol","p","span","svg","ul"].reduce((e,t)=>{let r=(0,l.forwardRef)((e,r)=>{let{asChild:o,...a}=e,i=o?C:t;return(0,l.useEffect)(()=>{window[Symbol.for("radix-ui")]=!0},[]),(0,l.createElement)(i,(0,n.Z)({},a,{ref:r}))});return r.displayName=`Primitive.${t}`,{...e,[t]:r}},{}),[x,R]=function(e,t=[]){let r=[],n=()=>{let t=r.map(e=>(0,l.createContext)(e));return function(r){let n=(null==r?void 0:r[e])||t;return(0,l.useMemo)(()=>({[`__scope${e}`]:{...r,[e]:n}}),[r,n])}};return n.scopeName=e,[function(t,n){let o=(0,l.createContext)(n),a=r.length;function i(t){let{scope:r,children:n,...i}=t,d=(null==r?void 0:r[e][a])||o,u=(0,l.useMemo)(()=>i,Object.values(i));return(0,l.createElement)(d.Provider,{value:u},n)}return r=[...r,n],i.displayName=t+"Provider",[i,function(r,i){let d=(null==i?void 0:i[e][a])||o,u=(0,l.useContext)(d);if(u)return u;if(void 0!==n)return n;throw Error(`\`${r}\` must be used within \`${t}\``)}]},function(...e){let t=e[0];if(1===e.length)return t;let r=()=>{let r=e.map(e=>({useScope:e(),scopeName:e.scopeName}));return function(e){let n=r.reduce((t,{useScope:r,scopeName:n})=>{let l=r(e)[`__scope${n}`];return{...t,...l}},{});return(0,l.useMemo)(()=>({[`__scope${t.scopeName}`]:n}),[n])}};return r.scopeName=t.scopeName,r}(n,...t)]}("Form"),k="Form",[F,A]=x(k),[N,_]=x(k),j=(0,l.forwardRef)((e,t)=>{let{__scopeForm:r,onClearServerErrors:o=()=>{},...i}=e,u=d(t,(0,l.useRef)(null)),[s,c]=(0,l.useState)({}),f=(0,l.useCallback)(e=>s[e],[s]),m=(0,l.useCallback)((e,t)=>c(r=>{var n;return{...r,[e]:{...null!==(n=r[e])&&void 0!==n?n:{},...t}}}),[]),p=(0,l.useCallback)(e=>{c(t=>({...t,[e]:void 0})),w(t=>({...t,[e]:{}}))},[]),[h,v]=(0,l.useState)({}),b=(0,l.useCallback)(e=>{var t;return null!==(t=h[e])&&void 0!==t?t:[]},[h]),C=(0,l.useCallback)((e,t)=>{v(r=>{var n;return{...r,[e]:[...null!==(n=r[e])&&void 0!==n?n:[],t]}})},[]),g=(0,l.useCallback)((e,t)=>{v(r=>{var n;return{...r,[e]:(null!==(n=r[e])&&void 0!==n?n:[]).filter(e=>e.id!==t)}})},[]),[y,w]=(0,l.useState)({}),x=(0,l.useCallback)(e=>{var t;return null!==(t=y[e])&&void 0!==t?t:{}},[y]),R=(0,l.useCallback)((e,t)=>{w(r=>{var n;return{...r,[e]:{...null!==(n=r[e])&&void 0!==n?n:{},...t}}})},[]),[k,A]=(0,l.useState)({}),_=(0,l.useCallback)((e,t)=>{A(r=>{let n=new Set(r[e]).add(t);return{...r,[e]:n}})},[]),j=(0,l.useCallback)((e,t)=>{A(r=>{let n=new Set(r[e]);return n.delete(t),{...r,[e]:n}})},[]),M=(0,l.useCallback)(e=>{var t;return Array.from(null!==(t=k[e])&&void 0!==t?t:[]).join(" ")||void 0},[k]);return(0,l.createElement)(F,{scope:r,getFieldValidity:f,onFieldValidityChange:m,getFieldCustomMatcherEntries:b,onFieldCustomMatcherEntryAdd:C,onFieldCustomMatcherEntryRemove:g,getFieldCustomErrors:x,onFieldCustomErrorsChange:R,onFieldValiditionClear:p},(0,l.createElement)(N,{scope:r,onFieldMessageIdAdd:_,onFieldMessageIdRemove:j,getFieldDescription:M},(0,l.createElement)(E.form,(0,n.Z)({},i,{ref:u,onInvalid:a(e.onInvalid,e=>{let t=function(e){let[t]=Array.from(e.elements).filter(Z).filter(P);return t}(e.currentTarget);t===e.target&&t.focus(),e.preventDefault()}),onSubmit:a(e.onSubmit,o,{checkForDefaultPrevented:!1}),onReset:a(e.onReset,o)}))))}),[M,S]=x("FormField"),I="This value is not valid",T={badInput:I,patternMismatch:"This value does not match the required pattern",rangeOverflow:"This value is too large",rangeUnderflow:"This value is too small",stepMismatch:"This value does not match the required step",tooLong:"This value is too long",tooShort:"This value is too short",typeMismatch:"This value does not match the required type",valid:void 0,valueMissing:"This value is missing"},V="FormMessage",D=((e,t)=>{let{match:r,forceMatch:o=!1,name:a,children:i,...d}=e,u=A(V,d.__scopeForm).getFieldValidity(a);return o||(null==u?void 0:u[r])?(0,l.createElement)(D,(0,n.Z)({ref:t},d,{name:a}),null!=i?i:T[r]):null},(0,l.forwardRef)((e,t)=>{let{__scopeForm:r,id:o,name:a,...i}=e,d=_(V,r),u=f(),s=null!=o?o:u,{onFieldMessageIdAdd:c,onFieldMessageIdRemove:m}=d;return(0,l.useEffect)(()=>(c(a,s),()=>m(a,s)),[a,s,c,m]),(0,l.createElement)(E.span,(0,n.Z)({id:s},i,{ref:t}))}));function Z(e){return e instanceof HTMLElement}function P(e){return"validity"in e&&(!1===e.validity.valid||"true"===e.getAttribute("aria-invalid"))}let $=j}}]);