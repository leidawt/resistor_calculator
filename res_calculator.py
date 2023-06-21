#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分压凑算器
import itertools
import math


class ResCalculator():
    def __init__(self) -> None:
        self.res_table = [10, 12, 15, 20, 22, 27, 30, 33, 39, 47, 51, 56, 68, 75, 82, 91, 100, 120, 150, 200, 220, 270, 300, 330, 390, 470, 510, 560, 680, 750, 820, 910, 1e3, 1.2e3, 1.5e3, 2e3, 2.2e3, 2.7e3, 3e3, 3.3e3, 3.9e3, 4.7e3, 5.1e3, 5.6e3, 6.8e3, 7.5e3,
                          8.2e3, 9.1e3, 10e3, 12e3, 15e3, 20e3, 22e3, 27e3, 30e3, 33e3, 39e3, 47e3, 51e3, 56e3, 68e3, 75e3, 82e3, 91e3, 100e3, 120e3, 150e3, 200e3, 220e3, 270e3, 300e3, 330e3, 390e3, 470e3, 510e3, 560e3, 680e3, 750e3, 820e3, 910e3, 1000e3, 1.8e3, 18e3, 180e3]
        self.results = []
        self.results_type = ""

    def get_res_table(self):
        return ",".join([self.res_print_helper(r) for r in self.res_table])

    def res_print_helper(self, r):
        if r < 1e3:
            return "{:>.2f}Ω".format(r)
        elif r < 1e6:
            return "{:>.2f}KΩ".format(r/1e3)
        elif r < 1e9:
            return "{:>.2f}MΩ".format(r/1e6)
        else:
            raise ValueError(f"r={r}")

    def voltage_divider_cal(self, vin, vout, type, r1_min, r1_max, r2_min, r2_max):
        r1_max = math.inf if r1_max == 0 else r1_max
        r2_max = math.inf if r2_max == 0 else r2_max
        self.results = []
        for (r1, r2) in itertools.product(self.res_table, self.res_table):
            if type == 1:
                v_div = r2/(r1+r2)*vin
            elif type == 2:
                v_div = vin/r2*(r1+r2)
            else:
                raise ValueError(f"Err type: {type}")
            err = abs(v_div-vout)/vout
            if r1 >= r1_min and r1 <= r1_max and r2 >= r2_min and r2 <= r2_max:
                self.results.append((r1, r2, v_div, err))
        self.results.sort(key=lambda ele: ele[3])
        self.results_type = "voltage_divider_cal"
        return self.results

    def res_compose_cal(self, desired, type, r1_min, r1_max, r2_min, r2_max, r3_min, r3_max):
        # type=1 R1+R2
        # type=2 R1//R2
        # type=3 R1//R2+R3
        r1_max = math.inf if r1_max == 0 else r1_max
        r2_max = math.inf if r2_max == 0 else r2_max
        r3_max = math.inf if r3_max == 0 else r3_max
        self.results = []
        r3_table = self.res_table if type == 3 else [r3_min]
        for (r1, r2, r3) in itertools.product(self.res_table, self.res_table, r3_table):
            if r1 >= r1_min and r1 <= r1_max and r2 >= r2_min and r2 <= r2_max and r3 >= r3_min and r3 <= r3_max and r1 <= r2:
                if type == 1:
                    r = r1+r2
                elif type == 2:
                    r = r1*r2/(r1+r2)
                elif type == 3:
                    r = r1*r2/(r1+r2)+r3
                else:
                    ValueError(f"Unsupported type {type}")
                err = abs(r-desired)/desired
                self.results.append((r1, r2, r3, r, err))
        self.results.sort(key=lambda ele: ele[4])
        self.results_type = "res_compose_cal"
        return self.results

    def get_results(self, len="inf", return_raw=False):
        if len == "inf":
            raw_results = self.results
        else:
            assert(isinstance(len, int))
            raw_results = self.results[:len]
        if return_raw:
            return raw_results
        else:
            results = []
            if self.results_type == "voltage_divider_cal":
                for each in raw_results:
                    r1, r2, v_div, err = each
                    r1 = self.res_print_helper(r1)
                    r2 = self.res_print_helper(r2)
                    v_div = "{:.3f}V".format(v_div)
                    err = "{:.2%}".format(err)
                    results.append((r1, r2, v_div, err))
            elif self.results_type == "res_compose_cal":
                for each in raw_results:
                    r1, r2, r3, r, err = each
                    r1 = self.res_print_helper(r1)
                    r2 = self.res_print_helper(r2)
                    r3 = self.res_print_helper(r3)
                    r = self.res_print_helper(r)
                    err = "{:.2%}".format(err)
                    results.append((r1, r2, r3, r, err))
            else:
                raise ValueError(f"Err results_type={self.results_type}")
            return results


if __name__ == "__main__":
    res_cal = ResCalculator()
    # res_cal.voltage_divider_cal(3.3, 1)
    # res_cal.print()
    res_cal.res_compose_cal(1e6, 1, 0, 0, 0, 0, 0, 0)
