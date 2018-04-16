from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if CSP.is_complete(self, assignment):
            return assignment
        someVariable = CSP.select_unassigned_variable(self,assignment)
        for value in CSP.order_domain_values(self, someVariable, assignment):
            if CSP.is_consistent(self, someVariable, value, assignment):
                assignment[someVariable] = value
                assignment.update({someVariable: value})
                result = CSP.recursive_backtracking(self, assignment)
                if result != None:
                    return result
                assignment[someVariable].remove(value)

        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_south_america_csp():
    cr, pan, ven, col, guy, sur, guyf, ecu, per, bra, bol, chi, par, arg, uru = 'CR', 'PAN', 'VEN', 'COL', 'GUY', 'SUR', 'GUYF', 'ECU', 'PER', 'BRA', 'BOL', 'CHI', 'PAR', 'ARG', 'URU'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cr, pan, ven, col, guy, sur, guyf, ecu, per, bra, bol, chi, par, arg, uru]
    domains = {
        cr: values[:],
        pan: values[:],
        ven: values[:],
        col: values[:],
        guy: values[:],
        sur: values[:],
        guyf: values[:],
        ecu: values[:],
        per: values[:],
        bra: values[:],
        bol: values[:],
        chi: values[:],
        par: values[:],
        arg: values[:],
        uru: values[:],

    }
    neighbours = {
        cr: [pan],
        pan: [cr, col],
        ven: [col, bra, guy],
        col: [ecu, per, bra, ven],
        guy: [ven, bra, sur],
        sur: [guy, bra, guyf],
        guyf: [sur, bra],
        ecu: [col, per],
        per: [ecu, col, bra, bol, chi],
        bra: [uru, par, arg, bol, per, col, ven, guy, sur, guyf],
        bol: [per, bra, par, arg, chi],
        chi: [per, bol, arg],
        par: [bol, bra, arg],
        arg: [chi, bol, par, uru],
        uru: [arg, bra],

    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cr: constraint_function,
        pan: constraint_function,
        ven: constraint_function,
        col: constraint_function,
        guy: constraint_function,
        sur: constraint_function,
        guyf: constraint_function,
        ecu: constraint_function,
        per: constraint_function,
        bra: constraint_function,
        bol: constraint_function,
        chi: constraint_function,
        par: constraint_function,
        arg: constraint_function,
        uru: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
