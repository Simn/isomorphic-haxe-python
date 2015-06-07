import math as python_lib_Math
import math as Math
from flask import Flask as Flask
import functools as python_lib_Functools
import inspect as python_lib_Inspect
from io import StringIO as python_lib_io_StringIO


class _hx_AnonObject:
	def __init__(self, fields):
		self.__dict__ = fields


class Enum:
	_hx_class_name = "Enum"
	_hx_fields = ["tag", "index", "params"]
	_hx_methods = ["__str__"]

	def __init__(self,tag,index,params):
		self.tag = None
		self.index = None
		self.params = None
		self.tag = tag
		self.index = index
		self.params = params

	def __str__(self):
		tmp = self.params
		tmp1 = (tmp is None)
		tmp2 = None
		if tmp1:
			tmp2 = self.tag
		else:
			tmp3 = self.tag
			tmp4 = (("null" if tmp3 is None else tmp3) + "(")
			tmp5 = ",".join([python_Boot.toString1(x1,'') for x1 in self.params])
			tmp6 = tmp5
			tmp7 = (("null" if tmp4 is None else tmp4) + ("null" if tmp6 is None else tmp6))
			tmp2 = (("null" if tmp7 is None else tmp7) + ")")
		return tmp2



class Class:
	_hx_class_name = "Class"


class Reflect:
	_hx_class_name = "Reflect"
	_hx_statics = ["field"]

	@staticmethod
	def field(o,field):
		tmp = o
		tmp1 = field
		tmp2 = python_Boot.field(tmp,tmp1)
		return tmp2


class Server:
	_hx_class_name = "Server"
	_hx_statics = ["main", "clientSide", "serverSide"]

	@staticmethod
	def main():
		app = Flask(__name__)
		app.route("/server")(Server.serverSide)
		app.route("/client")(Server.clientSide)
		app.run()

	@staticmethod
	def clientSide():
		return "\n      <html>\n        <body>\n         <div id=\"content\"></div>\n          <script src=\"static/js/client.js\"></script>\n        </body>\n      </html>\n\n    "

	@staticmethod
	def serverSide():
		tmp = Template()
		template = tmp
		template.title = "Hello from server side"
		template.body = "This content is rendered in python"
		tmp1 = template.execute()
		return tmp1


class Std:
	_hx_class_name = "Std"
	_hx_statics = ["is", "string"]

	@staticmethod
	def _hx_is(v,t):
		if ((v is None) and ((t is None))):
			return False
		if (t is None):
			return False
		if (t == Dynamic):
			return True
		isBool = isinstance(v,bool)
		if ((t == Bool) and isBool):
			return True
		if ((((not isBool) and (not (t == Bool))) and (t == Int)) and isinstance(v,int)):
			return True
		vIsFloat = isinstance(v,float)
		def _hx_local_0():
			f = v
			return (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
		def _hx_local_1():
			x = v
			def _hx_local_4():
				def _hx_local_3():
					_hx_local_2 = None
					try:
						_hx_local_2 = int(x)
					except Exception as _hx_e:
						_hx_e1 = _hx_e
						e = _hx_e1
						_hx_local_2 = None
					return _hx_local_2
				return _hx_local_3()
			return _hx_local_4()
		if (((((((not isBool) and vIsFloat) and (t == Int)) and _hx_local_0()) and ((v == _hx_local_1()))) and ((v <= 2147483647))) and ((v >= -2147483648))):
			return True
		if (((not isBool) and (t == Float)) and isinstance(v,(float, int))):
			return True
		if (t == str):
			return isinstance(v,str)
		isEnumType = (t == Enum)
		if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
			return True
		if isEnumType:
			return False
		isClassType = (t == Class)
		if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
			return True
		if isClassType:
			return False
		def _hx_local_6():
			_hx_local_5 = None
			try:
				_hx_local_5 = isinstance(v,t)
			except Exception as _hx_e:
				_hx_e1 = _hx_e
				e1 = _hx_e1
				_hx_local_5 = False
			return _hx_local_5
		if _hx_local_6():
			return True
		if python_lib_Inspect.isclass(t):
			def _hx_local_7():
				loop1 = None
				def _hx_local_9(intf):
					f1 = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
					if (f1 is not None):
						_g = 0
						while (_g < len(f1)):
							i = (f1[_g] if _g >= 0 and _g < len(f1) else None)
							_g = (_g + 1)
							if HxOverrides.eq(i,t):
								return True
							else:
								l = loop1(i)
								if l:
									return True
						return False
					else:
						return False
				loop1 = _hx_local_9
				return loop1
			loop = _hx_local_7()
			currentClass = v.__class__
			while (currentClass is not None):
				if loop(currentClass):
					return True
				currentClass = python_Boot.getSuperClass(currentClass)
			return False
		else:
			return False

	@staticmethod
	def string(s):
		tmp = s
		tmp1 = python_Boot.toString1(tmp,"")
		return tmp1


class Float:
	_hx_class_name = "Float"


class Int:
	_hx_class_name = "Int"


class Bool:
	_hx_class_name = "Bool"


class Dynamic:
	_hx_class_name = "Dynamic"


class StringBuf:
	_hx_class_name = "StringBuf"
	_hx_fields = ["b"]

	def __init__(self):
		self.b = None
		tmp = python_lib_io_StringIO()
		self.b = tmp



class StringTools:
	_hx_class_name = "StringTools"
	_hx_statics = ["htmlEscape"]

	@staticmethod
	def htmlEscape(s,quotes = None):
		tmp = None
		tmp1 = None
		tmp2 = None
		tmp3 = None
		tmp4 = None
		_this = s.split("&")
		tmp5 = "&amp;".join([python_Boot.toString1(x1,'') for x1 in _this])
		tmp4 = tmp5
		_this1 = tmp4
		tmp3 = _this1.split("<")
		_this2 = tmp3
		tmp6 = "&lt;".join([python_Boot.toString1(x1,'') for x1 in _this2])
		tmp2 = tmp6
		_this3 = tmp2
		tmp1 = _this3.split(">")
		_this4 = tmp1
		tmp7 = "&gt;".join([python_Boot.toString1(x1,'') for x1 in _this4])
		tmp = tmp7
		s = tmp
		tmp8 = None
		if quotes:
			tmp9 = None
			tmp10 = None
			_this5 = s.split("\"")
			tmp11 = "&quot;".join([python_Boot.toString1(x1,'') for x1 in _this5])
			tmp10 = tmp11
			_this6 = tmp10
			tmp9 = _this6.split("'")
			_this7 = tmp9
			tmp12 = "&#039;".join([python_Boot.toString1(x1,'') for x1 in _this7])
			tmp8 = tmp12
		else:
			tmp8 = s
		return tmp8


class erazor_macro_Template:
	_hx_class_name = "erazor.macro.Template"

	def __init__(self):
		pass


class erazor_macro_HtmlTemplate(erazor_macro_Template):
	_hx_class_name = "erazor.macro.HtmlTemplate"
	_hx_fields = []
	_hx_methods = ["escape"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = erazor_macro_Template


	def __init__(self):
		super().__init__()

	def escape(self,_hx_str):
		tmp = _hx_str
		tmp1 = StringTools.htmlEscape(tmp,True)
		return tmp1



class Template(erazor_macro_HtmlTemplate):
	_hx_class_name = "Template"
	_hx_fields = ["title", "body"]
	_hx_methods = ["execute"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = erazor_macro_HtmlTemplate


	def __init__(self):
		self.title = None
		self.body = None
		super().__init__()

	def execute(self):
		tmp = self.escape
		tmp1 = erazor_Output(tmp)
		__b__ = tmp1
		__b__.b.write("<h1>")
		tmp2 = self.title
		__b__.unsafeAdd(tmp2)
		__b__.b.write("</h1>\n<br>\n<p>")
		tmp3 = self.body
		__b__.unsafeAdd(tmp3)
		__b__.b.write("</p>\n")
		tmp4 = __b__.b.getvalue()
		return tmp4



class erazor_TString:
	_hx_class_name = "erazor.TString"
	_hx_fields = ["s"]
	_hx_methods = ["toString"]

	def toString(self):
		tmp = self.s
		return tmp



class erazor_UnsafeString(erazor_TString):
	_hx_class_name = "erazor.UnsafeString"
	_hx_fields = []
	_hx_methods = ["escape", "toString"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = erazor_TString


	def escape(self,_hx_str):
		tmp = _hx_str
		tmp1 = StringTools.htmlEscape(tmp,True)
		return tmp1

	def toString(self):
		tmp = self.s
		tmp1 = self.escape(tmp)
		return tmp1



class erazor_Output(StringBuf):
	_hx_class_name = "erazor.Output"
	_hx_fields = []
	_hx_methods = ["escape", "unsafeAdd"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = StringBuf


	def __init__(self,escapeMethod = None):
		tmp = (escapeMethod is not None)
		if tmp:
			self.escape = escapeMethod
		super().__init__()

	def escape(self,_hx_str):
		tmp = _hx_str
		return tmp

	def unsafeAdd(self,_hx_str):
		tmp = _hx_str
		tmp1 = Std._hx_is(tmp,erazor_TString)
		tmp2 = None
		if tmp1:
			tmp2 = Reflect.field(_hx_str,"toString")()
		else:
			tmp3 = _hx_str
			tmp4 = Std.string(tmp3)
			tmp2 = self.escape(tmp4)
		val = tmp2
		tmp5 = self.b
		tmp6 = Std.string(val)
		tmp5.write(tmp6)



class python_Boot:
	_hx_class_name = "python.Boot"
	_hx_statics = ["keywords", "toString1", "fields", "simpleField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

	@staticmethod
	def toString1(o,s):
		if (o is None):
			return "null"
		if isinstance(o,str):
			return o
		if (s is None):
			s = ""
		if (len(s) >= 5):
			return "<...>"
		if isinstance(o,bool):
			if o:
				return "true"
			else:
				return "false"
		if isinstance(o,int):
			return str(o)
		if isinstance(o,float):
			try:
				if (o == int(o)):
					def _hx_local_1():
						def _hx_local_0():
							v = o
							return Math.floor((v + 0.5))
						return str(_hx_local_0())
					return _hx_local_1()
				else:
					return str(o)
			except Exception as _hx_e:
				_hx_e1 = _hx_e
				e = _hx_e1
				return str(o)
		if isinstance(o,list):
			o1 = o
			l = len(o1)
			st = "["
			s = (("null" if s is None else s) + "\t")
			_g = 0
			while (_g < l):
				i = _g
				_g = (_g + 1)
				prefix = ""
				if (i > 0):
					prefix = ","
				st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
			st = (("null" if st is None else st) + "]")
			return st
		try:
			if hasattr(o,"toString"):
				return o.toString()
		except Exception as _hx_e:
			_hx_e1 = _hx_e
			pass
		if (python_lib_Inspect.isfunction(o) or python_lib_Inspect.ismethod(o)):
			return "<function>"
		if hasattr(o,"__class__"):
			if isinstance(o,_hx_AnonObject):
				toStr = None
				try:
					fields = python_Boot.fields(o)
					def _hx_local_5():
						_g1 = []
						_g11 = 0
						while (_g11 < len(fields)):
							f = (fields[_g11] if _g11 >= 0 and _g11 < len(fields) else None)
							_g11 = (_g11 + 1)
							x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
							_g1.append(x)
						return _g1
					fieldsStr = _hx_local_5()
					toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
				except Exception as _hx_e:
					_hx_e1 = _hx_e
					e2 = _hx_e1
					return "{ ... }"
				if (toStr is None):
					return "{ ... }"
				else:
					return toStr
			if isinstance(o,Enum):
				o2 = o
				l1 = len(o2.params)
				hasParams = (l1 > 0)
				if hasParams:
					paramsStr = ""
					_g2 = 0
					while (_g2 < l1):
						i1 = _g2
						_g2 = (_g2 + 1)
						prefix1 = ""
						if (i1 > 0):
							prefix1 = ","
						paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix1 is None else prefix1) + HxOverrides.stringOrNull(python_Boot.toString1((o2.params[i1] if i1 >= 0 and i1 < len(o2.params) else None),s))))))
					return (((HxOverrides.stringOrNull(o2.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
				else:
					return o2.tag
			if hasattr(o,"_hx_class_name"):
				if (o.__class__.__name__ != "type"):
					fields1 = python_Boot.getInstanceFields(o)
					def _hx_local_8():
						_g3 = []
						_g12 = 0
						while (_g12 < len(fields1)):
							f1 = (fields1[_g12] if _g12 >= 0 and _g12 < len(fields1) else None)
							_g12 = (_g12 + 1)
							x1 = ((("" + ("null" if f1 is None else f1)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f1),(("null" if s is None else s) + "\t"))))
							_g3.append(x1)
						return _g3
					fieldsStr1 = _hx_local_8()
					toStr1 = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr1]))) + " )")
					return toStr1
				else:
					fields2 = python_Boot.getClassFields(o)
					def _hx_local_10():
						_g4 = []
						_g13 = 0
						while (_g13 < len(fields2)):
							f2 = (fields2[_g13] if _g13 >= 0 and _g13 < len(fields2) else None)
							_g13 = (_g13 + 1)
							x2 = ((("" + ("null" if f2 is None else f2)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f2),(("null" if s is None else s) + "\t"))))
							_g4.append(x2)
						return _g4
					fieldsStr2 = _hx_local_10()
					toStr2 = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr2]))) + " )")
					return toStr2
			if (o == str):
				return "#String"
			if (o == list):
				return "#Array"
			if callable(o):
				return "function"
			try:
				if hasattr(o,"__repr__"):
					return o.__repr__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e
				pass
			if hasattr(o,"__str__"):
				return o.__str__([])
			if hasattr(o,"__name__"):
				return o.__name__
			return "???"
		else:
			return str(o)

	@staticmethod
	def fields(o):
		a = []
		if (o is not None):
			if hasattr(o,"_hx_fields"):
				fields = o._hx_fields
				return list(fields)
			if isinstance(o,_hx_AnonObject):
				d = o.__dict__
				keys = d.keys()
				handler = python_Boot.unhandleKeywords
				for k in keys:
					a.append(handler(k))
			elif hasattr(o,"__dict__"):
				a1 = []
				d1 = o.__dict__
				keys1 = d1.keys()
				for k in keys1:
					a.append(k)
		return a

	@staticmethod
	def simpleField(o,field):
		tmp = (field is None)
		if tmp:
			return None
		tmp1 = None
		if field in python_Boot.keywords:
			tmp1 = ("_hx_" + field)
		else:
			tmp2 = (len(field) > 2)
			tmp3 = tmp2
			tmp4 = None
			if tmp3:
				tmp5 = ord(field[0])
				tmp6 = tmp5
				tmp7 = tmp6
				tmp4 = (tmp7 == 95)
			else:
				tmp4 = False
			tmp8 = tmp4
			tmp9 = None
			if tmp8:
				tmp10 = ord(field[1])
				tmp11 = tmp10
				tmp12 = tmp11
				tmp9 = (tmp12 == 95)
			else:
				tmp9 = False
			tmp13 = None
			if tmp9:
				tmp14 = ord(field[(len(field) - 1)])
				tmp15 = tmp14
				tmp13 = (tmp15 != 95)
			else:
				tmp13 = False
			if tmp13:
				tmp1 = ("_hx_" + field)
			else:
				tmp1 = field
		field1 = tmp1
		tmp16 = o
		tmp17 = hasattr(tmp16,field1)
		tmp18 = None
		if tmp17:
			tmp19 = o
			tmp18 = getattr(tmp19,field1)
		else:
			tmp18 = None
		return tmp18

	@staticmethod
	def field(o,field):
		tmp = (field is None)
		if tmp:
			return None
		tmp1 = field
		_hx_local_0 = len(tmp1)
		if (_hx_local_0 == 10):
			if (tmp1 == "charCodeAt"):
				tmp29 = o
				tmp30 = str
				tmp31 = isinstance(tmp29,tmp30)
				if tmp31:
					tmp32 = None
					s4 = o
					def _hx_local_1(a11):
						tmp33 = s4
						tmp34 = a11
						tmp35 = HxString.charCodeAt(tmp33,tmp34)
						return tmp35
					tmp32 = _hx_local_1
					return tmp32
		elif (_hx_local_0 == 11):
			if (tmp1 == "toLowerCase"):
				tmp10 = o
				tmp11 = str
				tmp12 = isinstance(tmp10,tmp11)
				if tmp12:
					tmp13 = None
					s1 = o
					def _hx_local_2():
						tmp14 = s1
						tmp15 = HxString.toLowerCase(tmp14)
						return tmp15
					tmp13 = _hx_local_2
					return tmp13
			elif (tmp1 == "toUpperCase"):
				tmp16 = o
				tmp17 = str
				tmp18 = isinstance(tmp16,tmp17)
				if tmp18:
					tmp19 = None
					s2 = o
					def _hx_local_3():
						tmp20 = s2
						tmp21 = HxString.toUpperCase(tmp20)
						return tmp21
					tmp19 = _hx_local_3
					return tmp19
			elif (tmp1 == "lastIndexOf"):
				tmp50 = o
				tmp51 = str
				tmp52 = isinstance(tmp50,tmp51)
				if tmp52:
					tmp53 = None
					s6 = o
					def _hx_local_4(a13):
						tmp54 = s6
						tmp55 = a13
						tmp56 = HxString.lastIndexOf(tmp54,tmp55)
						return tmp56
					tmp53 = _hx_local_4
					return tmp53
				else:
					tmp57 = o
					tmp58 = list
					tmp59 = isinstance(tmp57,tmp58)
					if tmp59:
						tmp60 = None
						a2 = o
						def _hx_local_5(x2):
							tmp61 = a2
							tmp62 = x2
							tmp63 = python_internal_ArrayImpl.lastIndexOf(tmp61,tmp62)
							return tmp63
						tmp60 = _hx_local_5
						return tmp60
		elif (_hx_local_0 == 9):
			if (tmp1 == "substring"):
				tmp78 = o
				tmp79 = str
				tmp80 = isinstance(tmp78,tmp79)
				if tmp80:
					tmp81 = None
					s9 = o
					def _hx_local_6(a15):
						tmp82 = s9
						tmp83 = a15
						tmp84 = HxString.substring(tmp82,tmp83)
						return tmp84
					tmp81 = _hx_local_6
					return tmp81
		elif (_hx_local_0 == 5):
			if (tmp1 == "split"):
				tmp64 = o
				tmp65 = str
				tmp66 = isinstance(tmp64,tmp65)
				if tmp66:
					tmp67 = None
					s7 = o
					def _hx_local_7(d):
						tmp68 = s7
						tmp69 = d
						tmp70 = HxString.split(tmp68,tmp69)
						return tmp70
					tmp67 = _hx_local_7
					return tmp67
			elif (tmp1 == "shift"):
				tmp172 = o
				tmp173 = list
				tmp174 = isinstance(tmp172,tmp173)
				if tmp174:
					tmp175 = None
					x14 = o
					def _hx_local_8():
						tmp176 = x14
						tmp177 = python_internal_ArrayImpl.shift(tmp176)
						return tmp177
					tmp175 = _hx_local_8
					return tmp175
			elif (tmp1 == "slice"):
				tmp178 = o
				tmp179 = list
				tmp180 = isinstance(tmp178,tmp179)
				if tmp180:
					tmp181 = None
					x15 = o
					def _hx_local_9(a18):
						tmp182 = x15
						tmp183 = a18
						tmp184 = python_internal_ArrayImpl.slice(tmp182,tmp183)
						return tmp184
					tmp181 = _hx_local_9
					return tmp181
		elif (_hx_local_0 == 4):
			if (tmp1 == "copy"):
				tmp118 = o
				tmp119 = list
				tmp120 = isinstance(tmp118,tmp119)
				if tmp120:
					def _hx_local_10():
						tmp121 = None
						x6 = o
						tmp122 = x6
						tmp121 = list(tmp122)
						return tmp121
					return _hx_local_10
			elif (tmp1 == "join"):
				tmp136 = o
				tmp137 = list
				tmp138 = isinstance(tmp136,tmp137)
				if tmp138:
					def _hx_local_11(sep):
						tmp139 = None
						x9 = o
						tmp140 = sep.join([python_Boot.toString1(x1,'') for x1 in x9])
						tmp139 = tmp140
						return tmp139
					return _hx_local_11
			elif (tmp1 == "push"):
				tmp147 = o
				tmp148 = list
				tmp149 = isinstance(tmp147,tmp148)
				if tmp149:
					tmp150 = None
					x11 = o
					def _hx_local_12(e):
						tmp151 = x11
						tmp152 = e
						tmp153 = python_internal_ArrayImpl.push(tmp151,tmp152)
						return tmp153
					tmp150 = _hx_local_12
					return tmp150
			elif (tmp1 == "sort"):
				tmp185 = o
				tmp186 = list
				tmp187 = isinstance(tmp185,tmp186)
				if tmp187:
					tmp188 = None
					x16 = o
					def _hx_local_13(f2):
						tmp189 = x16
						tmp190 = f2
						python_internal_ArrayImpl.sort(tmp189,tmp190)
					tmp188 = _hx_local_13
					return tmp188
		elif (_hx_local_0 == 7):
			if (tmp1 == "indexOf"):
				tmp36 = o
				tmp37 = str
				tmp38 = isinstance(tmp36,tmp37)
				if tmp38:
					tmp39 = None
					s5 = o
					def _hx_local_14(a12):
						tmp40 = s5
						tmp41 = a12
						tmp42 = HxString.indexOf(tmp40,tmp41)
						return tmp42
					tmp39 = _hx_local_14
					return tmp39
				else:
					tmp43 = o
					tmp44 = list
					tmp45 = isinstance(tmp43,tmp44)
					if tmp45:
						tmp46 = None
						a = o
						def _hx_local_15(x1):
							tmp47 = a
							tmp48 = x1
							tmp49 = python_internal_ArrayImpl.indexOf(tmp47,tmp48)
							return tmp49
						tmp46 = _hx_local_15
						return tmp46
			elif (tmp1 == "unshift"):
				tmp154 = o
				tmp155 = list
				tmp156 = isinstance(tmp154,tmp155)
				if tmp156:
					tmp157 = None
					x12 = o
					def _hx_local_16(e1):
						tmp158 = x12
						tmp159 = e1
						python_internal_ArrayImpl.unshift(tmp158,tmp159)
					tmp157 = _hx_local_16
					return tmp157
			elif (tmp1 == "reverse"):
				tmp167 = o
				tmp168 = list
				tmp169 = isinstance(tmp167,tmp168)
				if tmp169:
					tmp170 = None
					a4 = o
					def _hx_local_17():
						tmp171 = a4
						python_internal_ArrayImpl.reverse(tmp171)
					tmp170 = _hx_local_17
					return tmp170
		elif (_hx_local_0 == 3):
			if (tmp1 == "map"):
				tmp97 = o
				tmp98 = list
				tmp99 = isinstance(tmp97,tmp98)
				if tmp99:
					tmp100 = None
					x4 = o
					def _hx_local_18(f):
						tmp101 = x4
						tmp102 = f
						tmp103 = python_internal_ArrayImpl.map(tmp101,tmp102)
						return tmp103
					tmp100 = _hx_local_18
					return tmp100
			elif (tmp1 == "pop"):
				tmp141 = o
				tmp142 = list
				tmp143 = isinstance(tmp141,tmp142)
				if tmp143:
					tmp144 = None
					x10 = o
					def _hx_local_19():
						tmp145 = x10
						tmp146 = python_internal_ArrayImpl.pop(tmp145)
						return tmp146
					tmp144 = _hx_local_19
					return tmp144
		elif (_hx_local_0 == 8):
			if (tmp1 == "toString"):
				tmp85 = o
				tmp86 = str
				tmp87 = isinstance(tmp85,tmp86)
				if tmp87:
					tmp88 = None
					s10 = o
					def _hx_local_20():
						tmp89 = s10
						tmp90 = HxString.toString(tmp89)
						return tmp90
					tmp88 = _hx_local_20
					return tmp88
				else:
					tmp91 = o
					tmp92 = list
					tmp93 = isinstance(tmp91,tmp92)
					if tmp93:
						tmp94 = None
						x3 = o
						def _hx_local_21():
							tmp95 = x3
							tmp96 = python_internal_ArrayImpl.toString(tmp95)
							return tmp96
						tmp94 = _hx_local_21
						return tmp94
			elif (tmp1 == "iterator"):
				tmp123 = o
				tmp124 = list
				tmp125 = isinstance(tmp123,tmp124)
				if tmp125:
					tmp126 = None
					x7 = o
					def _hx_local_22():
						tmp127 = x7
						tmp128 = python_internal_ArrayImpl.iterator(tmp127)
						return tmp128
					tmp126 = _hx_local_22
					return tmp126
		elif (_hx_local_0 == 6):
			if (tmp1 == "length"):
				tmp2 = o
				tmp3 = str
				tmp4 = isinstance(tmp2,tmp3)
				if tmp4:
					tmp5 = None
					s = o
					tmp5 = len(s)
					return tmp5
				else:
					tmp6 = o
					tmp7 = list
					tmp8 = isinstance(tmp6,tmp7)
					if tmp8:
						tmp9 = None
						x = o
						tmp9 = len(x)
						return tmp9
			elif (tmp1 == "charAt"):
				tmp22 = o
				tmp23 = str
				tmp24 = isinstance(tmp22,tmp23)
				if tmp24:
					tmp25 = None
					s3 = o
					def _hx_local_23(a1):
						tmp26 = s3
						tmp27 = a1
						tmp28 = HxString.charAt(tmp26,tmp27)
						return tmp28
					tmp25 = _hx_local_23
					return tmp25
			elif (tmp1 == "substr"):
				tmp71 = o
				tmp72 = str
				tmp73 = isinstance(tmp71,tmp72)
				if tmp73:
					tmp74 = None
					s8 = o
					def _hx_local_24(a14):
						tmp75 = s8
						tmp76 = a14
						tmp77 = HxString.substr(tmp75,tmp76)
						return tmp77
					tmp74 = _hx_local_24
					return tmp74
			elif (tmp1 == "filter"):
				tmp104 = o
				tmp105 = list
				tmp106 = isinstance(tmp104,tmp105)
				if tmp106:
					tmp107 = None
					x5 = o
					def _hx_local_25(f1):
						tmp108 = x5
						tmp109 = f1
						tmp110 = python_internal_ArrayImpl.filter(tmp108,tmp109)
						return tmp110
					tmp107 = _hx_local_25
					return tmp107
			elif (tmp1 == "concat"):
				tmp111 = o
				tmp112 = list
				tmp113 = isinstance(tmp111,tmp112)
				if tmp113:
					tmp114 = None
					a16 = o
					def _hx_local_26(a21):
						tmp115 = a16
						tmp116 = a21
						tmp117 = python_internal_ArrayImpl.concat(tmp115,tmp116)
						return tmp117
					tmp114 = _hx_local_26
					return tmp114
			elif (tmp1 == "insert"):
				tmp129 = o
				tmp130 = list
				tmp131 = isinstance(tmp129,tmp130)
				if tmp131:
					tmp132 = None
					a3 = o
					def _hx_local_27(a17,x8):
						tmp133 = a3
						tmp134 = a17
						tmp135 = x8
						python_internal_ArrayImpl.insert(tmp133,tmp134,tmp135)
					tmp132 = _hx_local_27
					return tmp132
			elif (tmp1 == "remove"):
				tmp160 = o
				tmp161 = list
				tmp162 = isinstance(tmp160,tmp161)
				if tmp162:
					tmp163 = None
					x13 = o
					def _hx_local_28(e2):
						tmp164 = x13
						tmp165 = e2
						tmp166 = python_internal_ArrayImpl.remove(tmp164,tmp165)
						return tmp166
					tmp163 = _hx_local_28
					return tmp163
			elif (tmp1 == "splice"):
				tmp191 = o
				tmp192 = list
				tmp193 = isinstance(tmp191,tmp192)
				if tmp193:
					tmp194 = None
					x17 = o
					def _hx_local_29(a19,a22):
						tmp195 = x17
						tmp196 = a19
						tmp197 = a22
						tmp198 = python_internal_ArrayImpl.splice(tmp195,tmp196,tmp197)
						return tmp198
					tmp194 = _hx_local_29
					return tmp194
		else:
			pass
		tmp199 = None
		if field in python_Boot.keywords:
			tmp199 = ("_hx_" + field)
		else:
			tmp200 = (len(field) > 2)
			tmp201 = tmp200
			tmp202 = None
			if tmp201:
				tmp203 = ord(field[0])
				tmp204 = tmp203
				tmp205 = tmp204
				tmp202 = (tmp205 == 95)
			else:
				tmp202 = False
			tmp206 = tmp202
			tmp207 = None
			if tmp206:
				tmp208 = ord(field[1])
				tmp209 = tmp208
				tmp210 = tmp209
				tmp207 = (tmp210 == 95)
			else:
				tmp207 = False
			tmp211 = None
			if tmp207:
				tmp212 = ord(field[(len(field) - 1)])
				tmp213 = tmp212
				tmp211 = (tmp213 != 95)
			else:
				tmp211 = False
			if tmp211:
				tmp199 = ("_hx_" + field)
			else:
				tmp199 = field
		field1 = tmp199
		tmp214 = o
		tmp215 = hasattr(tmp214,field1)
		tmp216 = None
		if tmp215:
			tmp217 = o
			tmp216 = getattr(tmp217,field1)
		else:
			tmp216 = None
		return tmp216

	@staticmethod
	def getInstanceFields(c):
		f = (c._hx_fields if (hasattr(c,"_hx_fields")) else [])
		if hasattr(c,"_hx_methods"):
			def _hx_local_0():
				a = c._hx_methods
				return (f + a)
			f = _hx_local_0()
		sc = python_Boot.getSuperClass(c)
		if (sc is None):
			return f
		else:
			scArr = python_Boot.getInstanceFields(sc)
			scMap = set(scArr)
			res = []
			_g = 0
			while (_g < len(f)):
				f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
				_g = (_g + 1)
				if (not f1 in scMap):
					scArr.append(f1)
			return scArr

	@staticmethod
	def getSuperClass(c):
		if (c is None):
			return None
		try:
			if hasattr(c,"_hx_super"):
				return c._hx_super
			return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e
			pass
		return None

	@staticmethod
	def getClassFields(c):
		if hasattr(c,"_hx_statics"):
			x = c._hx_statics
			return list(x)
		else:
			return []

	@staticmethod
	def unhandleKeywords(name):
		tmp = name
		tmp1 = python_Boot.prefixLength
		tmp2 = HxString.substr(tmp,0,tmp1)
		tmp3 = (tmp2 == "_hx_")
		if tmp3:
			tmp4 = name
			tmp5 = python_Boot.prefixLength
			tmp6 = HxString.substr(tmp4,tmp5,None)
			real = tmp6
			if real in python_Boot.keywords:
				return real
		tmp7 = name
		return tmp7


class python_HaxeIterator:
	_hx_class_name = "python.HaxeIterator"
	_hx_fields = ["it", "x", "has", "checked"]
	_hx_methods = ["next", "hasNext"]

	def __init__(self,it):
		self.it = None
		self.x = None
		self.has = None
		self.checked = None
		self.checked = False
		self.has = False
		self.x = None
		self.it = it

	def next(self):
		tmp = self.checked
		tmp1 = (not tmp)
		if tmp1:
			self.hasNext()
		self.checked = False
		tmp2 = self.x
		return tmp2

	def hasNext(self):
		tmp = self.checked
		tmp1 = (not tmp)
		if tmp1:
			try:
				tmp2 = self.it
				tmp3 = tmp2.__next__()
				self.x = tmp3
				self.has = True
			except Exception as _hx_e:
				_hx_e1 = _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					self.has = False
					self.x = None
				else:
					raise _hx_e
			self.checked = True
		tmp4 = self.has
		return tmp4



class python_internal_ArrayImpl:
	_hx_class_name = "python.internal.ArrayImpl"
	_hx_statics = ["concat", "iterator", "indexOf", "lastIndexOf", "toString", "pop", "push", "unshift", "remove", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get"]

	@staticmethod
	def concat(a1,a2):
		return (a1 + a2)

	@staticmethod
	def iterator(x):
		tmp = python_HaxeIterator(x.__iter__())
		return tmp

	@staticmethod
	def indexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		tmp = (fromIndex is None)
		tmp1 = None
		if tmp:
			tmp1 = 0
		else:
			tmp2 = (fromIndex < 0)
			if tmp2:
				tmp1 = (_hx_len + fromIndex)
			else:
				tmp1 = fromIndex
		l = tmp1
		tmp3 = (l < 0)
		if tmp3:
			l = 0
		_g = l
		while True:
			tmp4 = (_g < _hx_len)
			tmp5 = (not tmp4)
			if tmp5:
				break
			tmp6 = _g
			_g = (_g + 1)
			i = tmp6
			tmp7 = (a[i] == x)
			if tmp7:
				return i
		return -1

	@staticmethod
	def lastIndexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		tmp = (fromIndex is None)
		tmp1 = None
		if tmp:
			tmp1 = _hx_len
		else:
			tmp2 = (fromIndex < 0)
			if tmp2:
				tmp3 = (_hx_len + fromIndex)
				tmp1 = (tmp3 + 1)
			else:
				tmp1 = (fromIndex + 1)
		l = tmp1
		tmp4 = (l > _hx_len)
		if tmp4:
			l = _hx_len
		while True:
			l = (l - 1)
			tmp5 = l
			tmp6 = (tmp5 > -1)
			tmp7 = (not tmp6)
			if tmp7:
				break
			tmp8 = (a[l] == x)
			if tmp8:
				tmp9 = l
				return tmp9
		return -1

	@staticmethod
	def toString(x):
		tmp = ",".join([python_Boot.toString1(x1,'') for x1 in x])
		tmp1 = tmp
		tmp2 = ("[" + ("null" if tmp1 is None else tmp1))
		tmp3 = (("null" if tmp2 is None else tmp2) + "]")
		return tmp3

	@staticmethod
	def pop(x):
		tmp = (len(x) == 0)
		tmp1 = None
		if tmp:
			tmp1 = None
		else:
			tmp1 = x.pop()
		return tmp1

	@staticmethod
	def push(x,e):
		x.append(e)
		tmp = len(x)
		return tmp

	@staticmethod
	def unshift(x,e):
		x.insert(0, e)

	@staticmethod
	def remove(x,e):
		try:
			x.remove(e)
			return True
		except Exception as _hx_e:
			_hx_e1 = _hx_e
			e1 = _hx_e1
			return False

	@staticmethod
	def shift(x):
		tmp = (len(x) == 0)
		if tmp:
			return None
		return x.pop(0)

	@staticmethod
	def slice(x,pos,end = None):
		return x[pos:end]

	@staticmethod
	def sort(x,f):
		x.sort(key= python_lib_Functools.cmp_to_key(f))

	@staticmethod
	def splice(x,pos,_hx_len):
		tmp = (pos < 0)
		if tmp:
			tmp1 = (len(x) + pos)
			pos = tmp1
		tmp2 = (pos < 0)
		if tmp2:
			pos = 0
		res = x[pos:(pos + _hx_len)]
		del x[pos:(pos + _hx_len)]
		return res

	@staticmethod
	def map(x,f):
		tmp = f
		tmp1 = x
		tmp2 = map(tmp,tmp1)
		tmp3 = list(tmp2)
		return tmp3

	@staticmethod
	def filter(x,f):
		tmp = f
		tmp1 = x
		tmp2 = filter(tmp,tmp1)
		tmp3 = list(tmp2)
		return tmp3

	@staticmethod
	def insert(a,pos,x):
		a.insert(pos, x)

	@staticmethod
	def reverse(a):
		a.reverse()

	@staticmethod
	def _get(x,idx):
		tmp = (idx > -1)
		tmp1 = None
		if tmp:
			tmp1 = (idx < len(x))
		else:
			tmp1 = False
		tmp2 = None
		if tmp1:
			tmp2 = x[idx]
		else:
			tmp2 = None
		return tmp2


class HxOverrides:
	_hx_class_name = "HxOverrides"
	_hx_statics = ["eq", "stringOrNull"]

	@staticmethod
	def eq(a,b):
		if (isinstance(a,list) or isinstance(b,list)):
			return a is b
		return (a == b)

	@staticmethod
	def stringOrNull(s):
		tmp = (s is None)
		tmp1 = None
		if tmp:
			tmp1 = "null"
		else:
			tmp1 = s
		return tmp1


class HxString:
	_hx_class_name = "HxString"
	_hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "toString", "substring", "substr"]

	@staticmethod
	def split(s,d):
		tmp = (d == "")
		tmp1 = None
		if tmp:
			tmp2 = s
			tmp1 = list(tmp2)
		else:
			tmp1 = s.split(d)
		return tmp1

	@staticmethod
	def charCodeAt(s,index):
		tmp = (s is None)
		tmp1 = (not tmp)
		tmp2 = tmp1
		tmp3 = None
		if tmp2:
			tmp3 = (len(s) == 0)
		else:
			tmp3 = True
		tmp4 = (not tmp3)
		tmp5 = tmp4
		tmp6 = None
		if tmp5:
			tmp6 = (index < 0)
		else:
			tmp6 = True
		tmp7 = (not tmp6)
		tmp8 = None
		if tmp7:
			tmp8 = (index >= len(s))
		else:
			tmp8 = True
		tmp9 = None
		if tmp8:
			tmp9 = None
		else:
			tmp9 = ord(s[index])
		return tmp9

	@staticmethod
	def charAt(s,index):
		tmp = (index < 0)
		tmp1 = (not tmp)
		tmp2 = None
		if tmp1:
			tmp2 = (index >= len(s))
		else:
			tmp2 = True
		tmp3 = None
		if tmp2:
			tmp3 = ""
		else:
			tmp3 = s[index]
		return tmp3

	@staticmethod
	def lastIndexOf(s,_hx_str,startIndex = None):
		tmp = (startIndex is None)
		if tmp:
			return s.rfind(_hx_str, 0, len(s))
		else:
			i = s.rfind(_hx_str, 0, (startIndex + 1))
			tmp1 = (i == -1)
			tmp2 = None
			if tmp1:
				tmp3 = (startIndex + 1)
				tmp4 = len(_hx_str)
				tmp5 = (tmp3 - tmp4)
				tmp2 = max(0,tmp5)
			else:
				tmp2 = (i + 1)
			startLeft = tmp2
			check = s.find(_hx_str, startLeft, len(s))
			tmp6 = (check > i)
			tmp7 = None
			if tmp6:
				tmp7 = (check <= startIndex)
			else:
				tmp7 = False
			if tmp7:
				return check
			else:
				tmp8 = i
				return tmp8

	@staticmethod
	def toUpperCase(s):
		return s.upper()

	@staticmethod
	def toLowerCase(s):
		return s.lower()

	@staticmethod
	def indexOf(s,_hx_str,startIndex = None):
		tmp = (startIndex is None)
		if tmp:
			return s.find(_hx_str)
		else:
			return s.find(_hx_str, startIndex)

	@staticmethod
	def toString(s):
		tmp = s
		return tmp

	@staticmethod
	def substring(s,startIndex,endIndex = None):
		tmp = (startIndex < 0)
		if tmp:
			startIndex = 0
		tmp1 = (endIndex is None)
		if tmp1:
			return s[startIndex:]
		else:
			tmp2 = (endIndex < 0)
			if tmp2:
				endIndex = 0
			tmp3 = (endIndex < startIndex)
			if tmp3:
				return s[endIndex:startIndex]
			else:
				return s[startIndex:endIndex]

	@staticmethod
	def substr(s,startIndex,_hx_len = None):
		tmp = (_hx_len is None)
		if tmp:
			return s[startIndex:]
		else:
			tmp1 = (_hx_len == 0)
			if tmp1:
				return ""
			return s[startIndex:(startIndex + _hx_len)]

tmp = float("-inf")
Math.NEGATIVE_INFINITY = tmp
tmp1 = float("inf")
Math.POSITIVE_INFINITY = tmp1
tmp2 = float("nan")
Math.NaN = tmp2
tmp3 = python_lib_Math.pi
Math.PI = tmp3

def _hx_init_python_Boot_keywords():
	def _hx_local_0():
		tmp = ["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"]
		return set(tmp)
	return _hx_local_0()
python_Boot.keywords = _hx_init_python_Boot_keywords()
python_Boot.prefixLength = len("_hx_")

Server.main()