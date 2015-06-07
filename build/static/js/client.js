(function (console) { "use strict";
function $extend(from, fields) {
	function Inherit() {} Inherit.prototype = from; var proto = new Inherit();
	for (var name in fields) proto[name] = fields[name];
	if( fields.toString !== Object.prototype.toString ) proto.toString = fields.toString;
	return proto;
}
var Client = function() { };
Client.__name__ = true;
Client.main = function() {
	var template = new Template();
	template.title = "Hello for client side";
	template.body = "This content is rendered in javascript";
	window.document.getElementById("content").innerHTML = template.execute();
};
Math.__name__ = true;
var Std = function() { };
Std.__name__ = true;
Std.string = function(s) {
	return js_Boot.__string_rec(s,"");
};
var StringBuf = function() {
	this.b = "";
};
StringBuf.__name__ = true;
StringBuf.prototype = {
	__class__: StringBuf
};
var StringTools = function() { };
StringTools.__name__ = true;
StringTools.htmlEscape = function(s,quotes) {
	s = s.split("&").join("&amp;").split("<").join("&lt;").split(">").join("&gt;");
	return quotes?s.split("\"").join("&quot;").split("'").join("&#039;"):s;
};
var erazor_macro_Template = function() {
};
erazor_macro_Template.__name__ = true;
erazor_macro_Template.prototype = {
	__class__: erazor_macro_Template
};
var erazor_macro_HtmlTemplate = function() {
	erazor_macro_Template.call(this);
};
erazor_macro_HtmlTemplate.__name__ = true;
erazor_macro_HtmlTemplate.__super__ = erazor_macro_Template;
erazor_macro_HtmlTemplate.prototype = $extend(erazor_macro_Template.prototype,{
	escape: function(str) {
		return StringTools.htmlEscape(str,true);
	}
	,__class__: erazor_macro_HtmlTemplate
});
var Template = function() {
	erazor_macro_HtmlTemplate.call(this);
};
Template.__name__ = true;
Template.__super__ = erazor_macro_HtmlTemplate;
Template.prototype = $extend(erazor_macro_HtmlTemplate.prototype,{
	execute: function() {
		var __b__ = new erazor_Output($bind(this,this.escape));
		__b__.b += "<h1>";
		__b__.unsafeAdd(this.title);
		__b__.b += "</h1>\n<br>\n<p>";
		__b__.unsafeAdd(this.body);
		__b__.b += "</p>\n";
		return __b__.b;
	}
	,__class__: Template
});
var erazor_TString = function() { };
erazor_TString.__name__ = true;
erazor_TString.prototype = {
	toString: function() {
		return this.s;
	}
	,__class__: erazor_TString
};
var erazor_UnsafeString = function() { };
erazor_UnsafeString.__name__ = true;
erazor_UnsafeString.__super__ = erazor_TString;
erazor_UnsafeString.prototype = $extend(erazor_TString.prototype,{
	escape: function(str) {
		return StringTools.htmlEscape(str,true);
	}
	,toString: function() {
		return this.escape(this.s);
	}
	,__class__: erazor_UnsafeString
});
var erazor_Output = function(escapeMethod) {
	if(escapeMethod != null) this.escape = escapeMethod;
	StringBuf.call(this);
};
erazor_Output.__name__ = true;
erazor_Output.__super__ = StringBuf;
erazor_Output.prototype = $extend(StringBuf.prototype,{
	escape: function(str) {
		return str;
	}
	,unsafeAdd: function(str) {
		var val = js_Boot.__instanceof(str,erazor_TString)?str.toString():this.escape(Std.string(str));
		this.b += val == null?"null":"" + val;
	}
	,__class__: erazor_Output
});
var js_Boot = function() { };
js_Boot.__name__ = true;
js_Boot.getClass = function(o) {
	if((o instanceof Array) && o.__enum__ == null) return Array; else {
		var cl = o.__class__;
		if(cl != null) return cl;
		var name = js_Boot.__nativeClassName(o);
		if(name != null) return js_Boot.__resolveNativeClass(name);
		return null;
	}
};
js_Boot.__string_rec = function(o,s) {
	if(o == null) return "null";
	if(s.length >= 5) return "<...>";
	var t = typeof(o);
	if(t == "function" && (o.__name__ || o.__ename__)) t = "object";
	switch(t) {
	case "object":
		if(o instanceof Array) {
			if(o.__enum__) {
				if(o.length == 2) return o[0];
				var str2 = o[0] + "(";
				s += "\t";
				var _g1 = 2;
				var _g = o.length;
				while(_g1 < _g) {
					var i1 = _g1++;
					if(i1 != 2) str2 += "," + js_Boot.__string_rec(o[i1],s); else str2 += js_Boot.__string_rec(o[i1],s);
				}
				return str2 + ")";
			}
			var l = o.length;
			var i;
			var str1 = "[";
			s += "\t";
			var _g2 = 0;
			while(_g2 < l) {
				var i2 = _g2++;
				str1 += (i2 > 0?",":"") + js_Boot.__string_rec(o[i2],s);
			}
			str1 += "]";
			return str1;
		}
		var tostr;
		try {
			tostr = o.toString;
		} catch( e ) {
			return "???";
		}
		if(tostr != null && tostr != Object.toString && typeof(tostr) == "function") {
			var s2 = o.toString();
			if(s2 != "[object Object]") return s2;
		}
		var k = null;
		var str = "{\n";
		s += "\t";
		var hasp = o.hasOwnProperty != null;
		for( var k in o ) {
		if(hasp && !o.hasOwnProperty(k)) {
			continue;
		}
		if(k == "prototype" || k == "__class__" || k == "__super__" || k == "__interfaces__" || k == "__properties__") {
			continue;
		}
		if(str.length != 2) str += ", \n";
		str += s + k + " : " + js_Boot.__string_rec(o[k],s);
		}
		s = s.substring(1);
		str += "\n" + s + "}";
		return str;
	case "function":
		return "<function>";
	case "string":
		return o;
	default:
		return String(o);
	}
};
js_Boot.__interfLoop = function(cc,cl) {
	if(cc == null) return false;
	if(cc == cl) return true;
	var intf = cc.__interfaces__;
	if(intf != null) {
		var _g1 = 0;
		var _g = intf.length;
		while(_g1 < _g) {
			var i = _g1++;
			var i1 = intf[i];
			if(i1 == cl || js_Boot.__interfLoop(i1,cl)) return true;
		}
	}
	return js_Boot.__interfLoop(cc.__super__,cl);
};
js_Boot.__instanceof = function(o,cl) {
	if(cl == null) return false;
	switch(cl) {
	case Int:
		return (o|0) === o;
	case Float:
		return typeof(o) == "number";
	case Bool:
		return typeof(o) == "boolean";
	case String:
		return typeof(o) == "string";
	case Array:
		return (o instanceof Array) && o.__enum__ == null;
	case Dynamic:
		return true;
	default:
		if(o != null) {
			if(typeof(cl) == "function") {
				if(o instanceof cl) return true;
				if(js_Boot.__interfLoop(js_Boot.getClass(o),cl)) return true;
			} else if(typeof(cl) == "object" && js_Boot.__isNativeObj(cl)) {
				if(o instanceof cl) return true;
			}
		} else return false;
		if(cl == Class && o.__name__ != null) return true;
		if(cl == Enum && o.__ename__ != null) return true;
		return o.__enum__ == cl;
	}
};
js_Boot.__nativeClassName = function(o) {
	var name = js_Boot.__toStr.call(o).slice(8,-1);
	if(name == "Object" || name == "Function" || name == "Math" || name == "JSON") return null;
	return name;
};
js_Boot.__isNativeObj = function(o) {
	return js_Boot.__nativeClassName(o) != null;
};
js_Boot.__resolveNativeClass = function(name) {
	return (Function("return typeof " + name + " != \"undefined\" ? " + name + " : null"))();
};
var $_, $fid = 0;
function $bind(o,m) { if( m == null ) return null; if( m.__id__ == null ) m.__id__ = $fid++; var f; if( o.hx__closures__ == null ) o.hx__closures__ = {}; else f = o.hx__closures__[m.__id__]; if( f == null ) { f = function(){ return f.method.apply(f.scope, arguments); }; f.scope = o; f.method = m; o.hx__closures__[m.__id__] = f; } return f; }
String.prototype.__class__ = String;
String.__name__ = true;
Array.__name__ = true;
var Int = { __name__ : ["Int"]};
var Dynamic = { __name__ : ["Dynamic"]};
var Float = Number;
Float.__name__ = ["Float"];
var Bool = Boolean;
Bool.__ename__ = ["Bool"];
var Class = { __name__ : ["Class"]};
var Enum = { };
js_Boot.__toStr = {}.toString;
Client.main();
})(typeof console != "undefined" ? console : {log:function(){}});
