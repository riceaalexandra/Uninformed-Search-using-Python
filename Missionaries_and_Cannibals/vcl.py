from search import Problem


def is_valid(state):
    nr_canibali_stanga, nr_misionari_stanga, barca, nr_canibali_dreapta, nr_misionari_dreapta = state
    if (nr_canibali_stanga > nr_misionari_stanga > 0) or (nr_misionari_dreapta > nr_misionari_dreapta > 0):
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
        if cur_state[2] == 'STANGA':
            if cur_state[0] >= 1:
                new_state = (cur_state[0] - 1, cur_state[1], 'DREAPTA', cur_state[3] + 1, cur_state[4])
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[0] >= 2:
                new_state = (cur_state[0] - 2, cur_state[1], 'DREAPTA', cur_state[3] + 2, cur_state[4])
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[1] >= 1:
                new_state = (cur_state[0], cur_state[1] - 1, 'DREAPTA', cur_state[3], cur_state[4] + 1)
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[1] >= 2:
                new_state = (cur_state[0], cur_state[1] - 2, 'DREAPTA', cur_state[3], cur_state[4] + 2)
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[0] >= 1 and cur_state[1] >= 1:
                new_state = (cur_state[0] - 1, cur_state[1] - 1, 'DREAPTA', cur_state[3] + 1, cur_state[4] + 1)
                if is_valid(new_state):
                    actions.append(new_state)
        else:
            if cur_state[3] >= 1:
                new_state = (cur_state[0] + 1, cur_state[1], 'STANGA', cur_state[3] - 1, cur_state[4])
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[3] >= 2:
                new_state = (cur_state[0] + 2, cur_state[1], 'STANGA', cur_state[3] - 2, cur_state[4])
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[4] >= 1:
                new_state = (cur_state[0], cur_state[1] + 1, 'STANGA', cur_state[3], cur_state[4] - 1)
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[4] >= 2:
                new_state = (cur_state[0], cur_state[1] + 2, 'STANGA', cur_state[3], cur_state[4] - 2)
                if is_valid(new_state):
                    actions.append(new_state)
            if cur_state[3] >= 1 and cur_state[4] >= 1:
                new_state = (cur_state[0] + 1, cur_state[1] + 1, 'STANGA', cur_state[3] - 1, cur_state[4] - 1)
                if is_valid(new_state):
                    actions.append(new_state)
        return actions