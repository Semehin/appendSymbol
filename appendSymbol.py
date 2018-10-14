import sublime_plugin

class AppendSymbol(sublime_plugin.TextCommand):
	def run(self, edit, **args):

		symb = args['symb']

		def insertSymb(point):
			self.view.insert(edit, point, symb)

		def isSymb(point):
			return self.view.substr(point) == symb

		for reg in self.view.sel():
			line = self.view.line(reg)
			lBeg = line.begin()
			lEnd = line.end()

			while(self.view.substr(lEnd - 1).isspace() and lEnd != lBeg):
				lEnd -= 1

			if lEnd == lBeg:
				continue

			if self.view.match_selector(lEnd - 1, 'comment'):
				point = self.view.extract_scope(lEnd - 1).a - 1

				if point < lBeg:
					continue
					
				while(self.view.substr(point).isspace() and point != lBeg):
					point -= 1

				if not self.view.substr(point).isspace() and not isSymb(point):
					insertSymb(point + 1)

			elif not isSymb(lEnd - 1):
				insertSymb(lEnd)
				
		if ('callback' in args and args['callback'] == 'jumpToEOL'):
			self.view.run_command("move_to", {"to": "eol"})
		if ('callback' in args and args['callback'] == 'addLine'):
			self.view.run_command("run_macro_file", {"file": "Packages/Default/Add Line.sublime-macro"})