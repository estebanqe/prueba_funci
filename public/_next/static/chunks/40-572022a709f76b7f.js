(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[40],{6691:function(e,t){"use strict";var r,n,o,l;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var r in t)Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}(t,{ACTION_FAST_REFRESH:function(){return c},ACTION_NAVIGATE:function(){return i},ACTION_PREFETCH:function(){return s},ACTION_REFRESH:function(){return u},ACTION_RESTORE:function(){return f},ACTION_SERVER_ACTION:function(){return d},ACTION_SERVER_PATCH:function(){return a},PrefetchCacheEntryStatus:function(){return n},PrefetchKind:function(){return r},isThenable:function(){return p}});let u="refresh",i="navigate",f="restore",a="server-patch",s="prefetch",c="fast-refresh",d="server-action";function p(e){return e&&("object"==typeof e||"function"==typeof e)&&"function"==typeof e.then}(o=r||(r={})).AUTO="auto",o.FULL="full",o.TEMPORARY="temporary",(l=n||(n={})).fresh="fresh",l.reusable="reusable",l.expired="expired",l.stale="stale",("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},4318:function(e,t,r){"use strict";function n(e,t,r,n){return!1}Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"getDomainLocale",{enumerable:!0,get:function(){return n}}),r(8364),("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},9577:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return g}});let n=r(8754),o=r(5893),l=n._(r(7294)),u=r(1401),i=r(2045),f=r(7420),a=r(7201),s=r(1443),c=r(9953),d=r(5320),p=r(2905),h=r(4318),y=r(953),v=r(6691),b=new Set;function _(e,t,r,n,o,l){if(l||(0,i.isLocalURL)(t)){if(!n.bypassPrefetchedCheck){let o=t+"%"+r+"%"+(void 0!==n.locale?n.locale:"locale"in e?e.locale:void 0);if(b.has(o))return;b.add(o)}(async()=>l?e.prefetch(t,o):e.prefetch(t,r,n))().catch(e=>{})}}function E(e){return"string"==typeof e?e:(0,f.formatUrl)(e)}let g=l.default.forwardRef(function(e,t){let r,n;let{href:f,as:b,children:g,prefetch:C=null,passHref:O,replace:m,shallow:j,scroll:P,locale:R,onClick:T,onMouseEnter:M,onTouchStart:A,legacyBehavior:k=!1,...x}=e;r=g,k&&("string"==typeof r||"number"==typeof r)&&(r=(0,o.jsx)("a",{children:r}));let S=l.default.useContext(c.RouterContext),I=l.default.useContext(d.AppRouterContext),L=null!=S?S:I,N=!S,U=!1!==C,w=null===C?v.PrefetchKind.AUTO:v.PrefetchKind.FULL,{href:K,as:B}=l.default.useMemo(()=>{if(!S){let e=E(f);return{href:e,as:b?E(b):e}}let[e,t]=(0,u.resolveHref)(S,f,!0);return{href:e,as:b?(0,u.resolveHref)(S,b):t||e}},[S,f,b]),D=l.default.useRef(K),F=l.default.useRef(B);k&&(n=l.default.Children.only(r));let H=k?n&&"object"==typeof n&&n.ref:t,[V,q,z]=(0,p.useIntersection)({rootMargin:"200px"}),G=l.default.useCallback(e=>{(F.current!==B||D.current!==K)&&(z(),F.current=B,D.current=K),V(e),H&&("function"==typeof H?H(e):"object"==typeof H&&(H.current=e))},[B,H,K,z,V]);l.default.useEffect(()=>{L&&q&&U&&_(L,K,B,{locale:R},{kind:w},N)},[B,K,q,R,U,null==S?void 0:S.locale,L,N,w]);let Y={ref:G,onClick(e){k||"function"!=typeof T||T(e),k&&n.props&&"function"==typeof n.props.onClick&&n.props.onClick(e),L&&!e.defaultPrevented&&function(e,t,r,n,o,u,f,a,s){let{nodeName:c}=e.currentTarget;if("A"===c.toUpperCase()&&(function(e){let t=e.currentTarget.getAttribute("target");return t&&"_self"!==t||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}(e)||!s&&!(0,i.isLocalURL)(r)))return;e.preventDefault();let d=()=>{let e=null==f||f;"beforePopState"in t?t[o?"replace":"push"](r,n,{shallow:u,locale:a,scroll:e}):t[o?"replace":"push"](n||r,{scroll:e})};s?l.default.startTransition(d):d()}(e,L,K,B,m,j,P,R,N)},onMouseEnter(e){k||"function"!=typeof M||M(e),k&&n.props&&"function"==typeof n.props.onMouseEnter&&n.props.onMouseEnter(e),L&&(U||!N)&&_(L,K,B,{locale:R,priority:!0,bypassPrefetchedCheck:!0},{kind:w},N)},onTouchStart:function(e){k||"function"!=typeof A||A(e),k&&n.props&&"function"==typeof n.props.onTouchStart&&n.props.onTouchStart(e),L&&(U||!N)&&_(L,K,B,{locale:R,priority:!0,bypassPrefetchedCheck:!0},{kind:w},N)}};if((0,a.isAbsoluteUrl)(B))Y.href=B;else if(!k||O||"a"===n.type&&!("href"in n.props)){let e=void 0!==R?R:null==S?void 0:S.locale,t=(null==S?void 0:S.isLocaleDomain)&&(0,h.getDomainLocale)(B,e,null==S?void 0:S.locales,null==S?void 0:S.domainLocales);Y.href=t||(0,y.addBasePath)((0,s.addLocale)(B,e,null==S?void 0:S.defaultLocale))}return k?l.default.cloneElement(n,Y):(0,o.jsx)("a",{...x,...Y,children:r})});("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},2905:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useIntersection",{enumerable:!0,get:function(){return f}});let n=r(7294),o=r(3815),l="function"==typeof IntersectionObserver,u=new Map,i=[];function f(e){let{rootRef:t,rootMargin:r,disabled:f}=e,a=f||!l,[s,c]=(0,n.useState)(!1),d=(0,n.useRef)(null),p=(0,n.useCallback)(e=>{d.current=e},[]);return(0,n.useEffect)(()=>{if(l){if(a||s)return;let e=d.current;if(e&&e.tagName)return function(e,t,r){let{id:n,observer:o,elements:l}=function(e){let t;let r={root:e.root||null,margin:e.rootMargin||""},n=i.find(e=>e.root===r.root&&e.margin===r.margin);if(n&&(t=u.get(n)))return t;let o=new Map;return t={id:r,observer:new IntersectionObserver(e=>{e.forEach(e=>{let t=o.get(e.target),r=e.isIntersecting||e.intersectionRatio>0;t&&r&&t(r)})},e),elements:o},i.push(r),u.set(r,t),t}(r);return l.set(e,t),o.observe(e),function(){if(l.delete(e),o.unobserve(e),0===l.size){o.disconnect(),u.delete(n);let e=i.findIndex(e=>e.root===n.root&&e.margin===n.margin);e>-1&&i.splice(e,1)}}}(e,e=>e&&c(e),{root:null==t?void 0:t.current,rootMargin:r})}else if(!s){let e=(0,o.requestIdleCallback)(()=>c(!0));return()=>(0,o.cancelIdleCallback)(e)}},[a,r,t,s,d.current]),[p,s,(0,n.useCallback)(()=>{c(!1)},[])]}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},1664:function(e,t,r){e.exports=r(9577)},4298:function(e,t,r){e.exports=r(2892)},4511:function(e,t,r){"use strict";r.d(t,{SV:function(){return u}});var n=r(7294);let o=(0,n.createContext)(null),l={didCatch:!1,error:null};class u extends n.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=l}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,r,n=arguments.length,o=Array(n),u=0;u<n;u++)o[u]=arguments[u];null===(t=(r=this.props).onReset)||void 0===t||t.call(r,{args:o,reason:"imperative-api"}),this.setState(l)}}componentDidCatch(e,t){var r,n;null===(r=(n=this.props).onError)||void 0===r||r.call(n,e,t)}componentDidUpdate(e,t){let{didCatch:r}=this.state,{resetKeys:n}=this.props;if(r&&null!==t.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,r)=>!Object.is(e,t[r]))}(e.resetKeys,n)){var o,u;null===(o=(u=this.props).onReset)||void 0===o||o.call(u,{next:n,prev:e.resetKeys,reason:"keys"}),this.setState(l)}}render(){let{children:e,fallbackRender:t,FallbackComponent:r,fallback:l}=this.props,{didCatch:u,error:i}=this.state,f=e;if(u){let e={error:i,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)f=t(e);else if(r)f=(0,n.createElement)(r,e);else if(null===l||(0,n.isValidElement)(l))f=l;else throw i}return(0,n.createElement)(o.Provider,{value:{didCatch:u,error:i,resetErrorBoundary:this.resetErrorBoundary}},f)}}}}]);