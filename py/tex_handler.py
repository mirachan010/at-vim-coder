import re
#import requests
#from bs4 import BeautifulSoup

class AVC_tex_handler:
	def __init__(self):
		self._conv_table = [
				(re.compile(r'\\sqrt'), '√'),
				(re.compile(r'\\pm'), '±'),
				(re.compile(r'\\div'), '÷'),
				(re.compile(r'\\times'), '×'),
				(re.compile(r'\\leq'), '≤'),
				(re.compile(r'\\leqq'), '≦'),
				(re.compile(r'\\geq'), '≥'),
				(re.compile(r'\\geqq'), '≧'),
				(re.compile(r'\\cap'), '∩'),
				(re.compile(r'\\cup'), '∪'),
				(re.compile(r'\\subset'), '⊂'),
				(re.compile(r'\\supset'), '⊃'),
				(re.compile(r'\\subseteq'), '⊆'),
				(re.compile(r'\\supseteq'), '⊇'),
				(re.compile(r'\\in'), '∈'),
				(re.compile(r'\\ni'), '∋'),
				(re.compile(r'\\vee'), '∨'),
				(re.compile(r'\\\wedge'), '∧'),
				(re.compile(r'\\bullet'), '⦁'),
				(re.compile(r'\\cdot'), '∙'),
				(re.compile(r'\\cdots'), '⋯'),
				(re.compile(r'\\ldots'), '…'),
				(re.compile(r'\\vdots'), '⋮'),
				(re.compile(r'\\left'), ''),
				(re.compile(r'\\right'), ''),
				(re.compile(r'\\max'), 'max'),
				(re.compile(r'\\min'), 'min'),
				(re.compile(r'\\ '), '')
				]
		self._exclude_pattern = re.compile(r'^[a-zA-Z0-9(...)\s,+=-]+$')

	def replace_var_text(self, section):
		var_tags = section.findAll('var')
		for var_tag in var_tags:
			if var_tag != [] and not self._exclude_pattern.match(var_tag.text):
				for tex_expression in self._conv_table:
					if tex_expression[0].search(var_tag.text):
						var_tag.string = tex_expression[0].sub(tex_expression[1], var_tag.text)

#tex_handler = AVC_tex_handler()
#response = requests.get('https://atcoder.jp/contests/abc123/tasks/abc123_d')
#soup = BeautifulSoup(response.text, 'lxml')
#sections = soup.findAll('section')
#for section in sections:
#	tex_handler.replace_var_text(section)
#print(sections)

