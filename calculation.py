import array
import numpy as np
from numpy import unravel_index


class Cell:

    def __init__(self, unit_profit, transportation):
        self.unit_profit = unit_profit
        self.transportation = transportation
        self.used = False


class Calculation:

    def __init__(self, supply, demand, transport_cost, supply_cost, demand_cost):
        self.row = len(demand) + 1
        self.col = len(supply) + 1
        self.supply = supply
        self.demand = demand
        self.supply_cost = supply_cost
        self.demand_cost = demand_cost
        self.transport_cost = transport_cost
        self.balanced = True
        self.grid = [0] * self.col
        self.alfa = [0] * self.col
        self.beta = [0] * self.row
        self.delta = [0] * (self.col - 1)
        self.index_of_unit_profit = [0] * (self.col * self.row)
        self.index_of_transportation = [0] * (self.col * self.row)
        self.index_of_route = [0] * 4
        self.purchase_cost = 0
        self.transportation_cost = 0
        self.income = 0
        self.available = True
        self.data_array = []

    def solve_problem(self):
        self.create_grid()
        self.set_supply_demands()
        self.unit_profit_indexes()
        self.set_transport()
        self.update_index_transportion()
        self.set_alfa_beta()
        self.set_delta()
        self.iteration()
        return self.data_array

    def unit_profit_indexes(self):
        unit_profits = []

        for inx_col in range(self.col - 1):
            for inx_row in range(self.row - 1):
                unit_profits.append(self.grid[inx_col][inx_row].unit_profit)

        i = 0
        while len(unit_profits) > 0:
            actual_max_profit = max(unit_profits)
            indexes_list = self.get_index_unit_profit(actual_max_profit)
            idx = unit_profits.index(actual_max_profit)
            self.index_of_unit_profit[i][0] = indexes_list[0]
            self.index_of_unit_profit[i][1] = indexes_list[1]
            del unit_profits[idx]
            i = i + 1

        for inx_col in range(self.col):
            for inx_row in range(self.row):
                if not self.has_assigned_array(self.index_of_unit_profit, [inx_col, inx_row]):
                    self.index_of_unit_profit[i][0] = inx_col
                    self.index_of_unit_profit[i][1] = inx_row
                    i = i + 1

    def has_assigned_array(self, array, subarray):
        for inx_i, el_i in enumerate(array):
            flag = False
            for inx_j, el_j in enumerate(el_i):
                if array[inx_i][inx_j] == subarray[inx_j]:
                    flag = True
                else:
                    flag = False
                    break

            if flag == True: return True

        return False

    def get_index_unit_profit(self, unit_profit):
        list = []
        for inx_col in range(self.col - 1):
            for inx_row in range(self.row - 1):
                if self.grid[inx_col][inx_row].unit_profit == unit_profit and len(list) == 0 and not self.grid[inx_col][
                    inx_row].used:
                    self.grid[inx_col][inx_row].used = True
                    list.append(inx_col)
                    list.append(inx_row)

        return list

    def create_grid(self):

        for i in range(4):
            self.index_of_route[i] = [0, 0]

        for i in range(self.row):
            self.beta[i] = [0, 0]

        for i in range(self.col):
            self.alfa[i] = [0, 0]

        for i in range(self.col * self.row):
            self.index_of_unit_profit[i] = [0, 0]

        for i in range(self.col):
            self.grid[i] = ([0] * self.row)

        for inx_col in range(self.col):
            for inx_row in range(self.row):
                if inx_col <= (self.col - 2) and inx_row <= (self.row - 2):
                    unit_profit = self.demand_cost[inx_row] - self.supply_cost[inx_col] - self.transport_cost[inx_col][
                        inx_row]
                    self.grid[inx_col][inx_row] = Cell(unit_profit, 0)
                else:
                    self.grid[inx_col][inx_row] = Cell(0, 0)

    def set_transport(self):
        tmp_supply = []
        tmp_demand = []

        for i in self.supply:
            tmp_supply.append(i)

        for j in self.demand:
            tmp_demand.append(j)

        for idx in self.index_of_unit_profit:
            x = idx[0]
            y = idx[1]
            if tmp_supply[x] < tmp_demand[y]:
                self.grid[x][y].transportation = tmp_supply[x]
                tmp_demand[y] -= tmp_supply[x]
                tmp_supply[x] = 0
            else:
                self.grid[x][y].transportation = tmp_demand[y]
                tmp_supply[x] -= tmp_demand[y]
                tmp_demand[y] = 0

    def set_supply_demands(self):
        if np.sum(self.supply) != np.sum(self.demand):
            self.balanced = False
        supply_sum = np.sum(self.supply)
        demand_sum = np.sum(self.demand)
        self.supply.append(demand_sum)
        self.demand.append(supply_sum)

    def update_index_transportion(self):

        i = 0
        self.index_of_transportation = [0] * (self.col * self.row)
        for z in range(self.col * self.row):
            self.index_of_transportation[z] = [0, 0]

        if self.balanced:
            for inx_i in range(self.col):
                for inx_j in range(self.row):
                    if self.grid[inx_i][inx_j].transportation > 0:
                        self.index_of_transportation[i][0] = inx_i
                        self.index_of_transportation[i][1] = inx_j
                        i = i + 1
        else:
            for k in range((self.col - 1), -1, -1):
                for j in range((self.row - 1), -1, -1):
                    if self.grid[k][j].transportation > 0:
                        self.index_of_transportation[i][0] = k
                        self.index_of_transportation[i][1] = j
                        i = i + 1

        length = self.col * self.row
        while length > i:
            self.index_of_transportation.pop()
            length = length - 1

        for a in self.alfa:
            a[1] = 0
            a[0] = 0

        for b in self.beta:
            b[1] = 0
            b[0] = 0

    def set_alfa_beta(self):
        self.update_index_transportion()
        if self.balanced:
            self.alfa[0][1] = 1
            self.alfa[0][0] = 0
        else:
            self.alfa[self.col - 1][1] = 1
            self.alfa[self.col - 1][0] = 0
        for idx in self.index_of_transportation:
            x = idx[0]
            y = idx[1]

            if self.alfa[x][1] != 1 and self.beta[y][1] == 1:
                self.alfa[x][0] = self.grid[x][y].unit_profit - self.beta[y][0]
                self.alfa[x][1] = 1
            elif self.alfa[x][1] == 1 and self.beta[y][1] != 1:
                self.beta[y][0] = self.grid[x][y].unit_profit - self.alfa[x][0]
                self.beta[y][1] = 1

    def set_delta(self):
        for i in range(self.col - 1):
            self.delta[i] = [0] * (self.row - 1)

        for i in range(self.col - 1):
            for j in range(self.row - 1):
                if self.grid[i][j].transportation == 0:
                    self.delta[i][j] = self.grid[i][j].unit_profit - self.alfa[i][0] - self.beta[j][0]
                else:
                    self.delta[i][j] = 0

    def print_grid(self):
        k = 0
        for i in range(self.col - 1):
            for j in range(self.row - 1):
                print("unit profit: " + str(self.grid[i][j].unit_profit) + " transporation " + str(
                    self.grid[i][j].transportation) + " step: " + str(k))
                k = k + 1

    def iteration(self):
        self.print_grid()
        print("=========================================================================")
        self.set_index_route()
        self.get_costs()
        self.set_array_of_data()
        max_row = np.array(np.max(self.delta, axis=0))
        max_positive_value = max(max_row)
        if max_positive_value > 0 and self.available:
            self.print_grid()
            print("=========================================================================")
            self.set_alfa_beta()
            self.set_delta()
            self.set_index_route()
            self.get_costs()
            self.set_array_of_data()
        # self.print_grid()
        print("=========================================================================")

    def set_array_of_data(self):
        array_of_transport = []
        array_of_unit_profit = []
        alfa = []
        beta = []
        col = self.col
        row = self.row
        alfa_l = len(self.alfa)
        beta_l = len(self.beta)
        if self.balanced:
            col = self.col - 1
            row = self.row - 1
            alfa_l = len(self.alfa) - 1
            beta_l = len(self.beta) - 1

        for i in range(col):
            transport = []
            unit_profit = []
            for j in range(row):
                transport.append(self.grid[i][j].transportation)
                unit_profit.append(self.grid[i][j].unit_profit)
            array_of_transport.append(transport)
            array_of_unit_profit.append(unit_profit)

        for z in range(alfa_l):
            alfa.append(self.alfa[z][0])

        for k in range(beta_l):
            beta.append(self.beta[k][0])

        profit = self.income - self.transportation_cost - self.purchase_cost
        all_cost = self.purchase_cost + self.transportation_cost

        self.data_array.append([self.supply, self.demand, array_of_unit_profit, array_of_transport, alfa, beta,
                                self.transportation_cost, self.purchase_cost, self.income, all_cost, profit])

    def get_costs(self):
        self.income = 0
        self.transportation_cost = 0
        self.purchase_cost = 0
        for i in range(self.col - 1):
            for j in range(self.row - 1):
                if self.grid[i][j].transportation > 0:
                    self.transportation_cost += self.grid[i][j].transportation * self.transport_cost[i][j]
                    self.purchase_cost += self.supply_cost[i] * self.grid[i][j].transportation
                    self.income += self.demand_cost[j] * self.grid[i][j].transportation

    def set_index_route(self):
        max_row = np.max(self.delta, axis=0)
        max_positive_value = max(max_row)
        if max_positive_value > 0:
            array_of_index = self.get_index_delta(max_positive_value)
            y = array_of_index[0]
            x = array_of_index[1]
            self.index_of_route[0][0] = x
            self.index_of_route[0][1] = y
            self.available = False
            for i in range(self.col):
                if i != y:
                    for j in range(self.row - 1):
                        if self.grid[y][j].transportation > 0:
                            if self.grid[i][j].transportation > 0 and self.grid[i][x].transportation > 0:
                                self.available = True
                                self.index_of_route[1][0] = x
                                self.index_of_route[1][1] = i
                                self.index_of_route[2][0] = j
                                self.index_of_route[2][1] = i
                                self.index_of_route[3][0] = j
                                self.index_of_route[3][1] = y

            if self.available:
                self.set_Route()

    def get_index_delta(self, max):
        indexes = []
        for i in range(self.col - 1):
            for j in range(self.row - 1):
                if self.delta[i][j] == max and len(indexes) == 0:
                    indexes.append(i)
                    indexes.append(j)
        return indexes

    def set_Route(self):
        transportation_value = []
        for i in range(4):
            if i > 0:
                idx = self.index_of_route[i]
                transportation_value.append(self.grid[idx[1]][idx[0]].transportation)

        min_value = min(transportation_value)
        for i in range(4):
            idx = self.index_of_route[i]
            if i % 2 == 0:
                self.grid[idx[1]][idx[0]].transportation += min_value
            else:
                self.grid[idx[1]][idx[0]].transportation -= min_value
