
class Parser(object):
    def __init__(self, file):
        self.edb = []
        self.idb = {}

    def parse(self, lines):
        i = 0

        # parse entity
        # example: Person(pID,name,sex,married).
        while lines[i] != "%IDB":
            o = lines[i].split('(')
            self.edb.append(o[0])
            i += 1

        # parse predicat
        # example: Singleman(x) :- Man(x), not Husband(x).
        while i < len(lines):
            o = lines[i].split(":-")
            left = o[0].split("(")[0]
            right = o[1]
            preds_right = []
            for p in right.split(","):
                # negated subgoal
                if "not" in p.split("(")[0]:
                    preds_right.append(
                        [p.split("(")[0].split("not")[1].trim(), True])
                else:
                    # nonnegated subgoal
                    preds_right.append([p.split("(")[0].trim(), False])

            if left in self.idb:
                # list merge
                self.idb[left] += preds_right
            else:
                self.idb[left] = preds_right

            i += 1
