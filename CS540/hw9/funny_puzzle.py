import heapq
import copy



def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    coords = []
    for box in from_state:
        if box != 0:
            from_x = from_state.index(box) % 3
            from_y = int(from_state.index(box) / 3)
            to_x = to_state.index(box) % 3
            to_y = int(to_state.index(box) / 3)
            coords.append(abs(from_x - to_x) + abs(from_y - to_y))
    return sum(coords)



def print_succ(state):
    """
    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """

    succ_states = []
    for i in range(len(state)):
        if state[i] == 0:
            x_coord = i % 3
            y_coord = int(i / 3)
            # if x_coord == 0:
            #     if y_coord == 0:
            #         if state[i + 1] != 0:
            #             succ_states.append(right_tile(state, i))
            #         if state[i + 3] != 0:
            #             succ
            if i == 0:
                if state[1] != 0:
                    succ_states.append(right_tile(state, i))
                if state[3] != 0:
                    succ_states.append(down_tile(state, i))
            if i == 1:
                if state[0] != 0:
                    succ_states.append(left_tile(state, i))
                if state[2] != 0:
                    succ_states.append(right_tile(state, i))
                if state[4] != 0:
                    succ_states.append(down_tile(state, i))
            if i == 2:
                if state[1] != 0:
                    succ_states.append(left_tile(state, i))
                if state[5] != 0:
                    succ_states.append(down_tile(state, i))
            if i == 3:
                if state[0] != 0:
                    succ_states.append(up_tile(state, i))
                if state[4] != 0:
                    succ_states.append(right_tile(state, i))
                if state[6] != 0:
                    succ_states.append(down_tile(state, i))
            if i == 4:
                if state[1] != 0:
                    succ_states.append(up_tile(state, i))
                if state[3] != 0:
                    succ_states.append(left_tile(state, i))
                if state[5] != 0:
                    succ_states.append(right_tile(state, i))
                if state[7] != 0:
                    succ_states.append(down_tile(state, i))
            if i == 5:
                if state[2] != 0:
                    succ_states.append(up_tile(state, i))
                if state[4] != 0:
                    succ_states.append(left_tile(state, i))
                if state[8] != 0:
                    succ_states.append(down_tile(state, i))
            if i == 6:
                if state[3] != 0:
                    succ_states.append(up_tile(state, i))
                if state[7] != 0:
                    succ_states.append(right_tile(state, i))
            if i == 7:
                if state[4] != 0:
                    succ_states.append(up_tile(state, i))
                if state[6] != 0:
                    succ_states.append(left_tile(state, i))
                if state[8] != 0:
                    succ_states.append(right_tile(state, i))
            if i == 8:
                if state[5] != 0:
                    succ_states.append(up_tile(state, i))
                if state[7] != 0:
                    succ_states.append(left_tile(state, i))
    return sorted(succ_states)

def up_tile(state, i):
    copy_state = copy.deepcopy(state)
    copy_state[i], copy_state[i - 3] = copy_state[i - 3], copy_state[i]
    return copy_state

def down_tile(state, i):
    copy_state = copy.deepcopy(state)
    copy_state[i], copy_state[i + 3] = copy_state[i + 3], copy_state[i]
    return copy_state

def left_tile(state, i):
    copy_state = copy.deepcopy(state)
    copy_state[i], copy_state[i - 1] = copy_state[i - 1], copy_state[i]
    return copy_state

def right_tile(state, i):
    copy_state = copy.deepcopy(state)
    copy_state[i], copy_state[i + 1] = copy_state[i + 1], copy_state[i]
    return copy_state

def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    open = []
    closed = []
    dist_state = get_manhattan_distance(state, goal_state)
    heapq.heappush(open, (dist_state, state, (0, dist_state, -1)))
    while len(open) != 0:
        n = heapq.heappop(open)
        closed.append(n)
        (n_gh, n_state, (n_g, n_h, n_index)) = n
        successors = get_succ(n_state)
        if n_state == goal_state:
            break
        for succ in successors:
            g = n_g + 1
            h = get_manhattan_distance(succ, goal_state)
            for w in range(len(closed)):
                if closed[w] == n:
                    ind = w
            com_list = closed + open
            if any(succ in x for x in com_list):
                for x in com_list:
                    (x_gh, x_state, (x_g, x_h, x_pindex)) = x
                    if succ == x_state:
                        if g < x_g:
                            open.remove(x)
                            heapq.heappush(open, (g + h, succ, (g, h, ind)))
            elif not any(succ in x for x in com_list):
                heapq.heappush(open, (g + h, succ, (g, h, ind)))

    closed_last = closed[-1]
    closed_last_third = closed_last[2]
    index = closed_last_third[2]
    solution = []
    solution.insert(0, closed[-1])
    while index != -1:
        solution = [closed[index]] + solution
        index = closed[index][2][2]
    for x in solution:
        (gh, state, (g, h, index)) = x
        print(str(state) + " h=" + str(get_manhattan_distance(state, goal_state)) + " moves: " + str(g))

if __name__ == "__main__":
    test_matrix = [2,5,1,4,0,6,7,0,3]
    print_succ([2,5,1,4,0,6,7,0,3])
    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    solve([1, 2, 3, 4, 0, 6, 7, 5, 0])