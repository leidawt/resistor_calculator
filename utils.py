def get_float_input(self, id):
    val = self.widget_dic["tk_input_"+id].get()
    if val == "":
        val = 0
    else:
        if 'k' in val or 'K' in val:
            val = float(val[:-1])*1e3
        elif 'M' in val:
            val = float(val[:-1])*1e6
        else:
            val = float(val)
    return val


if __name__ == "__main__":
    val = "2k"
    if val == "":
        val = 0
    else:
        if 'k' in val or 'K' in val:
            val = float(val[:-1])*1e3
        elif 'M' in val:
            val = float(val[:-1])*1e6
        else:
            ValueError(f"Err: can not handle input {val}")
    print(val)
