from search import Problem


def is_valid(state):
    lupStanga, capraStanga, varzaStanga, om, lupDreapta, capraDreapta, varzaDreapta = state
    if (lupStanga == capraStanga == 1 and om == 'DREAPTA') or (lupDreapta == capraDreapta == 1 and om == 'STANGA') or \
            (varzaStanga == capraStanga == 1 and om == 'DREAPTA') or (varzaDreapta == capraDreapta == 1 and om == 'STANGA'):
        return False
    return True


class VCL(Problem):
    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def value(self, state):
        pass

    def __init__(self, initial, goal):
        self.goal = goal
        self.initial = initial
        self.visited_states = []
        Problem.__init__(self, self.initial, self.goal)

    def __repr__(self):
        return "< State (%s, %s) >" % (self.initial, self.goal)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, cur_state):
        actions = []

        self.visited_states.append(cur_state)
        if cur_state[3] == 'STANGA':

            # Duce lupul
            new_state = (0, cur_state[1], cur_state[2], 'DREAPTA', 1, cur_state[5], cur_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            # Duce capra
            new_state = (cur_state[0], 0, cur_state[2], 'DREAPTA', cur_state[4], 1, cur_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            # Duce varza
            new_state = (cur_state[0], cur_state[1], 0, 'DREAPTA', cur_state[4], cur_state[5], 1)
            if is_valid(new_state):
                actions.append(new_state)
        else:
            # Se intoarce cu lupul
            new_state = (1, cur_state[1], cur_state[2], 'STANGA', 0, cur_state[5], cur_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            # Se intoarce cu capra
            new_state = (cur_state[0], 1, cur_state[2], 'STANGA', cur_state[4], 0, cur_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            # Se intoarce cu varza
            new_state = (1, cur_state[1], cur_state[2], 'STANGA', 0, cur_state[5], cur_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            # Se intoarce gol
            new_state = (cur_state[0], cur_state[1], cur_state[2], 'STANGA', cur_state[4], cur_state[5], cur_state[6])
            if is_valid(new_state):
                actions.append(new_state)

        return actions
