
from pypy.translator.js.modules import dom
from pypy.translator.js.modules.mochikit import log, createLoggingPane
from web import exported_methods

class Page:
    def set_pages(self, elements):
        self.pages = elements
        self.counter = 0
        self.shown = 0

    def right(self):
        if self.counter < len(self.pages) - 1:
            self.counter += 1
            self.show(self.counter)

    def left(self):
        if self.counter > 0:
            self.counter -= 1
            self.show(self.counter)

    def delete_nodes(self):
        content = dom.get_document().getElementById("contentspace")
        for child in content.childNodes[:]:
            content.removeChild(child)

    def show(self, num):
        content = dom.get_document().getElementById("contentspace")
        if len(content.childNodes) > 0:
            content.removeChild(content.childNodes[0])
        content.appendChild(self.pages[num])
        self.shown = num

page = Page()

def keydown(key):
    c = key.keyCode
    if c == 39:
        page.right()
    elif c == 37:
        page.left()

def show():
    elements = [i for i in dom.get_document().getElementsByTagName('div')\
                if i.getAttribute('class')=='section']

    page.set_pages(elements)
    page.delete_nodes()
    page.show(0)
    dom.get_document().onkeypress = keydown
    createLoggingPane(True)

def comeback(msg):
    pass

def flow():
    exported_methods.flow_basic(comeback)
