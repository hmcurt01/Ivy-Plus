# college class
class College:
    def __init__(self, name, ed, aid, intvw, cadone, casent, fafsa, css, par, ty, choose, accept):
        self.name = name
        self.ed = ed
        self.aid = aid
        self.intvw = intvw
        self.cadone = cadone
        self.casent = casent
        self.fafsa = fafsa
        self.css = css
        self.par = par
        self.ty = ty
        self.choose = choose
        self.accept = accept

    # change attributes of object
    def change_attr(self, value, new):
        if value == "name":
            self.name = new
        elif value == "ed":
            self.ed = new
        elif value == "aid":
            self.aid = new
        elif value == "intvw":
            self.intvw = new
        elif value == "cadone":
            self.cadone = new
        elif value == "casent":
            self.casent = new
        elif value == "fafsa":
            self.fafsa = new
        elif value == "css":
            self.css = new
        elif value == "par":
            self.par = new
        elif value == "ty":
            self.ty = new
        elif value == "choose":
            self.choose = new
        elif value == "accept":
            self.accept = new
