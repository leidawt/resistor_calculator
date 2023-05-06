#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
本代码由[Tkinter布局助手]生成
当前版本:3.2.4
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict
from res_calculator import ResCalculator
import utils
from PIL.ImageTk import PhotoImage
import sys
import os


class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.calculator = ResCalculator()
        self.divider_type=StringVar(value=1)
        self.res_compose_type=StringVar(value=1)

        self.__win()
        self.widget_dic["tk_tabs_lhbmo7q9"] = self.__tk_tabs_lhbmo7q9(self)
        self.widget_dic["tk_text_lhbny85f"].insert(END,self.calculator.get_res_table())


    def __win(self):
        self.title("电阻凑算工具")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)

    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
        
    def __tk_tabs_lhbmo7q9(self,parent):
        frame = Notebook(parent)

        self.widget_dic["tk_tabs_lhbmo7q9_0"] = self.__tk_frame_lhbmo7q9_0(frame)
        frame.add(self.widget_dic["tk_tabs_lhbmo7q9_0"], text="分压")

        self.widget_dic["tk_tabs_lhbmo7q9_1"] = self.__tk_frame_lhbmo7q9_1(frame)
        frame.add(self.widget_dic["tk_tabs_lhbmo7q9_1"], text="凑电阻")

        self.widget_dic["tk_tabs_lhbmo7q9_2"] = self.__tk_frame_lhbmo7q9_2(frame)
        frame.add(self.widget_dic["tk_tabs_lhbmo7q9_2"], text="设置")

        frame.place(x=20, y=10, width=560, height=480)
        return frame

    def __tk_frame_lhbmo7q9_0(self,parent):
        frame = Frame(parent)
        frame.place(x=20, y=10, width=560, height=480)

        self.widget_dic["tk_label_frame_lhbmohd8"] = self.__tk_label_frame_lhbmohd8(frame)
        self.widget_dic["tk_label_lhbmtl8h"] = self.__tk_label_lhbmtl8h(frame)
        self.widget_dic["tk_input_lhbmtn25"] = self.__tk_input_lhbmtn25(frame)
        self.widget_dic["tk_label_lhbmtpxy"] = self.__tk_label_lhbmtpxy(frame)
        self.widget_dic["tk_label_lhbmtras"] = self.__tk_label_lhbmtras(frame)
        self.widget_dic["tk_input_lhbmurrf"] = self.__tk_input_lhbmurrf(frame)
        self.widget_dic["tk_label_lhbmv08f"] = self.__tk_label_lhbmv08f(frame)
        self.widget_dic["tk_label_lhbmv12m"] = self.__tk_label_lhbmv12m(frame)
        self.widget_dic["tk_label_lhbmvt01"] = self.__tk_label_lhbmvt01(frame)
        self.widget_dic["tk_label_lhbmwagr"] = self.__tk_label_lhbmwagr(frame)
        self.widget_dic["tk_label_lhbmwcfd"] = self.__tk_label_lhbmwcfd(frame)
        self.widget_dic["tk_label_lhbmwga8"] = self.__tk_label_lhbmwga8(frame)
        self.widget_dic["tk_input_lhbmwkar"] = self.__tk_input_lhbmwkar(frame)
        self.widget_dic["tk_input_lhbmwq7s"] = self.__tk_input_lhbmwq7s(frame)
        self.widget_dic["tk_input_lhbmwujp"] = self.__tk_input_lhbmwujp(frame)
        self.widget_dic["tk_input_lhbmwwhb"] = self.__tk_input_lhbmwwhb(frame)
        self.widget_dic["tk_label_lhbmycfz"] = self.__tk_label_lhbmycfz(frame)
        self.widget_dic["tk_label_lhbmyxnu"] = self.__tk_label_lhbmyxnu(frame)
        self.widget_dic["tk_label_lhbmz319"] = self.__tk_label_lhbmz319(frame)
        self.widget_dic["tk_label_lhbmz4t3"] = self.__tk_label_lhbmz4t3(frame)
        self.widget_dic["tk_label_lhbmzk5h"] = self.__tk_label_lhbmzk5h(frame)
        self.widget_dic["tk_table_lhbn5jnk"] = self.__tk_table_lhbn5jnk(frame)
        self.widget_dic["tk_button_lhbn5n3b"] = self.__tk_button_lhbn5n3b(frame)
        self.widget_dic["tk_label_lhbueduo"] = self.__tk_label_lhbueduo(frame)
        return frame

    def __tk_label_lhbmtl8h(self,parent):
        label = Label(parent,text="VIN=",anchor="center")
        label.place(x=30, y=80, width=50, height=30)
        return label

    def __tk_input_lhbmtn25(self,parent):
        ipt = Entry(parent)
        ipt.place(x=80, y=80, width=70, height=30)
        return ipt

    def __tk_label_lhbmtpxy(self,parent):
        label = Label(parent,text="V",anchor="center")
        label.place(x=150, y=80, width=20, height=30)
        return label

    def __tk_label_lhbmtras(self,parent):
        label = Label(parent,text="VOUT=",anchor="center")
        label.place(x=30, y=120, width=50, height=30)
        return label

    def __tk_input_lhbmurrf(self,parent):
        ipt = Entry(parent)
        ipt.place(x=80, y=120, width=70, height=30)
        return ipt

    def __tk_label_lhbmv08f(self,parent):
        label = Label(parent,text="R1",anchor="center")
        label.place(x=210, y=80, width=50, height=30)
        return label

    def __tk_label_lhbmv12m(self,parent):
        label = Label(parent,text="R2",anchor="center")
        label.place(x=210, y=120, width=50, height=30)
        return label

    def __tk_label_lhbmvt01(self,parent):
        label = Label(parent,text="MIN=",anchor="center")
        label.place(x=270, y=80, width=46, height=30)
        return label

    def __tk_label_lhbmwagr(self,parent):
        label = Label(parent,text="MIN=",anchor="center")
        label.place(x=270, y=120, width=46, height=30)
        return label

    def __tk_label_lhbmwcfd(self,parent):
        label = Label(parent,text="MAX=",anchor="center")
        label.place(x=410, y=80, width=46, height=30)
        return label

    def __tk_label_lhbmwga8(self,parent):
        label = Label(parent,text="MAX=",anchor="center")
        label.place(x=410, y=120, width=46, height=30)
        return label

    def __tk_input_lhbmwkar(self,parent):
        ipt = Entry(parent)
        ipt.place(x=320, y=80, width=55, height=30)
        return ipt

    def __tk_input_lhbmwq7s(self,parent):
        ipt = Entry(parent)
        ipt.place(x=320, y=120, width=55, height=30)
        return ipt

    def __tk_input_lhbmwujp(self,parent):
        ipt = Entry(parent)
        ipt.place(x=460, y=80, width=55, height=30)
        return ipt

    def __tk_input_lhbmwwhb(self,parent):
        ipt = Entry(parent)
        ipt.place(x=460, y=120, width=55, height=30)
        return ipt

    def __tk_label_lhbmycfz(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=380, y=80, width=20, height=30)
        return label

    def __tk_label_lhbmyxnu(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=380, y=120, width=20, height=30)
        return label

    def __tk_label_lhbmz319(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=520, y=80, width=20, height=30)
        return label

    def __tk_label_lhbmz4t3(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=520, y=120, width=20, height=30)
        return label

    def __tk_label_lhbmzk5h(self,parent):
        label = Label(parent,text="V",anchor="center")
        label.place(x=150, y=120, width=20, height=30)
        return label

    def __tk_table_lhbn5jnk(self,parent):
        # 表头字段 表头宽度
        columns = {"R1":112,"R2":112,"VOUT":112,"误差":112}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=20, y=230, width=450, height=219)
        
        vbar = Scrollbar(parent)
        tk_table.configure(yscrollcommand=vbar.set)
        vbar.config(command=tk_table.yview)
        vbar.place(x=455, y=230, width=15, height=219)
        self.scrollbar_autohide(vbar,tk_table)
        return tk_table

    def __tk_button_lhbn5n3b(self,parent):
        btn = Button(parent, text="计算")
        btn.place(x=480, y=330, width=50, height=30)
        return btn
    
    def __tk_label_lhbueduo(self,parent):
        label = Label(parent,text="标签",anchor="center")
        label.place(x=30, y=170, width=493, height=51)
        return label

    def __tk_frame_lhbmo7q9_1(self,parent):
        frame = Frame(parent)
        frame.place(x=20, y=10, width=560, height=480)

        self.widget_dic["tk_label_lhbn763h"] = self.__tk_label_lhbn763h(frame)
        self.widget_dic["tk_input_lhbn7or6"] = self.__tk_input_lhbn7or6(frame)
        self.widget_dic["tk_label_lhbn81re"] = self.__tk_label_lhbn81re(frame)
        self.widget_dic["tk_label_frame_lhbn9t2y"] = self.__tk_label_frame_lhbn9t2y(frame)
        self.widget_dic["tk_frame_lhbnbkh6"] = self.__tk_frame_lhbnbkh6(frame)
        self.widget_dic["tk_table_lhbnewl1"] = self.__tk_table_lhbnewl1(frame)
        self.widget_dic["tk_button_lhbnf1zk"] = self.__tk_button_lhbnf1zk(frame)
        return frame

    def __tk_label_lhbn763h(self,parent):
        label = Label(parent,text="期望R值",anchor="center")
        label.place(x=20, y=20, width=50, height=30)
        return label

    def __tk_input_lhbn7or6(self,parent):
        ipt = Entry(parent)
        ipt.place(x=80, y=20, width=77, height=30)
        return ipt

    def __tk_label_lhbn81re(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=160, y=20, width=28, height=30)
        return label

    def __tk_table_lhbnewl1(self,parent):
        # 表头字段 表头宽度
        columns = {"R1":89,"R2":89,"R3":89,"R":89,"误差":89}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=20, y=230, width=450, height=219)
        
        vbar = Scrollbar(parent)
        tk_table.configure(yscrollcommand=vbar.set)
        vbar.config(command=tk_table.yview)
        vbar.place(x=455, y=230, width=15, height=219)
        self.scrollbar_autohide(vbar,tk_table)
        return tk_table

    def __tk_button_lhbnf1zk(self,parent):
        btn = Button(parent, text="计算")
        btn.place(x=480, y=330, width=50, height=30)
        return btn

    def __tk_frame_lhbmo7q9_2(self,parent):
        frame = Frame(parent)
        frame.place(x=20, y=10, width=560, height=480)

        self.widget_dic["tk_label_frame_lhbnuzvr"] = self.__tk_label_frame_lhbnuzvr(frame)
        self.widget_dic["tk_label_frame_lhbnxq01"] = self.__tk_label_frame_lhbnxq01(frame)
        return frame

    def __tk_label_frame_lhbmohd8(self,parent):
        frame = LabelFrame(parent)
    
        frame.configure(text="类型")
        frame.place(x=10, y=10, width=233, height=50)

        self.widget_dic["tk_radio_button_lhbmrg3d"] = self.__tk_radio_button_lhbmrg3d(frame)
        self.widget_dic["tk_radio_button_lhbmrjiz"] = self.__tk_radio_button_lhbmrjiz(frame)
        return frame
    def __tk_radio_button_lhbmrg3d(self,parent):
        rb = Radiobutton(parent,text="降压",variable=self.divider_type, value=1)
        rb.place(x=10, y=0, width=80, height=25)
        return rb

    def __tk_radio_button_lhbmrjiz(self,parent):
        rb = Radiobutton(parent,text="升压",variable=self.divider_type, value=2)
        rb.place(x=100, y=0, width=80, height=25)
        return rb

    def __tk_label_frame_lhbn9t2y(self,parent):
        frame = LabelFrame(parent)
    
        frame.configure(text="拓扑")
        frame.place(x=220, y=0, width=289, height=67)

        self.widget_dic["tk_radio_button_lhbn9vxx"] = self.__tk_radio_button_lhbn9vxx(frame)
        self.widget_dic["tk_radio_button_lhbn9xmo"] = self.__tk_radio_button_lhbn9xmo(frame)
        self.widget_dic["tk_radio_button_lhbn9z6i"] = self.__tk_radio_button_lhbn9z6i(frame)
        return frame
    def __tk_radio_button_lhbn9vxx(self,parent):
        rb = Radiobutton(parent,text="R1+R2",variable=self.res_compose_type, value=1)
        rb.place(x=10, y=10, width=80, height=30)
        return rb

    def __tk_radio_button_lhbn9xmo(self,parent):
        rb = Radiobutton(parent,text="R1//R2+R3",variable=self.res_compose_type, value=3)
        rb.place(x=170, y=10, width=112, height=30)
        return rb

    def __tk_radio_button_lhbn9z6i(self,parent):
        rb = Radiobutton(parent,text="R1//R2",variable=self.res_compose_type, value=2)
        rb.place(x=90, y=10, width=80, height=30)
        return rb

    def __tk_frame_lhbnbkh6(self,parent):
        frame = Frame(parent)
        frame.place(x=20, y=70, width=385, height=150)

        self.widget_dic["tk_label_lhbnbuja"] = self.__tk_label_lhbnbuja(frame)
        self.widget_dic["tk_input_lhbnc1sa"] = self.__tk_input_lhbnc1sa(frame)
        self.widget_dic["tk_label_lhbnc2y3"] = self.__tk_label_lhbnc2y3(frame)
        self.widget_dic["tk_label_lhbnclao"] = self.__tk_label_lhbnclao(frame)
        self.widget_dic["tk_input_lhbncnhk"] = self.__tk_input_lhbncnhk(frame)
        self.widget_dic["tk_label_lhbncqal"] = self.__tk_label_lhbncqal(frame)
        self.widget_dic["tk_label_lhbndkze"] = self.__tk_label_lhbndkze(frame)
        self.widget_dic["tk_label_lhbnl410"] = self.__tk_label_lhbnl410(frame)
        self.widget_dic["tk_label_lhbnofss"] = self.__tk_label_lhbnofss(frame)
        self.widget_dic["tk_label_lhbnogju"] = self.__tk_label_lhbnogju(frame)
        self.widget_dic["tk_label_lhbnoh63"] = self.__tk_label_lhbnoh63(frame)
        self.widget_dic["tk_input_lhbnohw1"] = self.__tk_input_lhbnohw1(frame)
        self.widget_dic["tk_label_lhbnoiut"] = self.__tk_label_lhbnoiut(frame)
        self.widget_dic["tk_input_lhbnoq64"] = self.__tk_input_lhbnoq64(frame)
        self.widget_dic["tk_label_lhbnoxiw"] = self.__tk_label_lhbnoxiw(frame)
        self.widget_dic["tk_label_lhbnoy31"] = self.__tk_label_lhbnoy31(frame)
        self.widget_dic["tk_input_lhbnoypr"] = self.__tk_input_lhbnoypr(frame)
        self.widget_dic["tk_label_lhbnozmq"] = self.__tk_label_lhbnozmq(frame)
        self.widget_dic["tk_label_lhbnp0e3"] = self.__tk_label_lhbnp0e3(frame)
        self.widget_dic["tk_input_lhbnp1be"] = self.__tk_input_lhbnp1be(frame)
        self.widget_dic["tk_label_lhbnp2df"] = self.__tk_label_lhbnp2df(frame)
        return frame

    def __tk_label_lhbnbuja(self,parent):
        label = Label(parent,text="R1",anchor="center")
        label.place(x=0, y=10, width=50, height=30)
        return label

    def __tk_input_lhbnc1sa(self,parent):
        ipt = Entry(parent)
        ipt.place(x=110, y=10, width=46, height=30)
        return ipt

    def __tk_label_lhbnc2y3(self,parent):
        label = Label(parent,text="MIN=",anchor="center")
        label.place(x=60, y=10, width=50, height=30)
        return label

    def __tk_label_lhbnclao(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=160, y=10, width=20, height=30)
        return label

    def __tk_input_lhbncnhk(self,parent):
        ipt = Entry(parent)
        ipt.place(x=260, y=10, width=46, height=30)
        return ipt

    def __tk_label_lhbncqal(self,parent):
        label = Label(parent,text="MAX=",anchor="center")
        label.place(x=210, y=10, width=50, height=30)
        return label

    def __tk_label_lhbndkze(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=310, y=50, width=20, height=30)
        return label

    def __tk_label_lhbnl410(self,parent):
        label = Label(parent,text="R1",anchor="center")
        label.place(x=0, y=50, width=50, height=30)
        return label

    def __tk_label_lhbnofss(self,parent):
        label = Label(parent,text="MIN=",anchor="center")
        label.place(x=60, y=50, width=50, height=30)
        return label

    def __tk_label_lhbnogju(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=160, y=50, width=20, height=30)
        return label

    def __tk_label_lhbnoh63(self,parent):
        label = Label(parent,text="MAX=",anchor="center")
        label.place(x=210, y=50, width=50, height=30)
        return label

    def __tk_input_lhbnohw1(self,parent):
        ipt = Entry(parent)
        ipt.place(x=260, y=50, width=46, height=30)
        return ipt

    def __tk_label_lhbnoiut(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=310, y=10, width=20, height=30)
        return label

    def __tk_input_lhbnoq64(self,parent):
        ipt = Entry(parent)
        ipt.place(x=110, y=50, width=46, height=30)
        return ipt

    def __tk_label_lhbnoxiw(self,parent):
        label = Label(parent,text="R1",anchor="center")
        label.place(x=0, y=90, width=50, height=30)
        return label

    def __tk_label_lhbnoy31(self,parent):
        label = Label(parent,text="MIN=",anchor="center")
        label.place(x=60, y=90, width=50, height=30)
        return label

    def __tk_input_lhbnoypr(self,parent):
        ipt = Entry(parent)
        ipt.place(x=110, y=90, width=46, height=30)
        return ipt

    def __tk_label_lhbnozmq(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=160, y=90, width=20, height=30)
        return label

    def __tk_label_lhbnp0e3(self,parent):
        label = Label(parent,text="MAX=",anchor="center")
        label.place(x=210, y=90, width=50, height=30)
        return label

    def __tk_input_lhbnp1be(self,parent):
        ipt = Entry(parent)
        ipt.place(x=260, y=90, width=46, height=30)
        return ipt

    def __tk_label_lhbnp2df(self,parent):
        label = Label(parent,text="Ω",anchor="center")
        label.place(x=310, y=90, width=20, height=30)
        return label

    def __tk_label_frame_lhbnuzvr(self,parent):
        frame = LabelFrame(parent)
    
        frame.configure(text="电阻表导入(逗号分隔)")
        frame.place(x=10, y=20, width=537, height=161)

        self.widget_dic["tk_button_lhbnwwer"] = self.__tk_button_lhbnwwer(frame)
        self.widget_dic["tk_text_lhbnzn1i"] = self.__tk_text_lhbnzn1i(frame)
        return frame
    def __tk_button_lhbnwwer(self,parent):
        btn = Button(parent, text="导入")
        btn.place(x=460, y=50, width=50, height=30)
        return btn

    def __tk_text_lhbnzn1i(self,parent):
        text = Text(parent)
        text.place(x=20, y=10, width=433, height=123)
        
        return text

    def __tk_label_frame_lhbnxq01(self,parent):
        frame = LabelFrame(parent)
    
        frame.configure(text="当前电阻表")
        frame.place(x=10, y=240, width=537, height=184)

        self.widget_dic["tk_text_lhbny85f"] = self.__tk_text_lhbny85f(frame)
        return frame
    def __tk_text_lhbny85f(self,parent):
        text = Text(parent)
        text.place(x=10, y=10, width=521, height=144)
        
        return text

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def handle_divider_cal(self,evt):
        vin=utils.get_float_input(self,"lhbmtn25")
        vout=utils.get_float_input(self,"lhbmurrf")
        cal_type=int(self.divider_type.get())
        r1_min=utils.get_float_input(self,"lhbmwkar")
        r1_max=utils.get_float_input(self,"lhbmwujp")
        r2_min=utils.get_float_input(self,"lhbmwq7s")
        r2_max=utils.get_float_input(self,"lhbmwwhb")
        # print(vin, vout, cal_type, r1_min, r1_max, r2_min, r2_max)
        self.calculator.voltage_divider_cal(vin, vout, cal_type, r1_min, r1_max, r2_min, r2_max)
        results = self.calculator.get_results(len=20)
        table = self.widget_dic["tk_table_lhbn5jnk"]
        table.delete(*table.get_children())
        for li in results:
            table.insert('','end',values=li)
        
    def handle_res_cal(self,evt):
        cal_type=int(self.res_compose_type.get())
        desired=utils.get_float_input(self,"lhbn7or6")
        r1_min=utils.get_float_input(self,"lhbnc1sa")
        r1_max=utils.get_float_input(self,"lhbncnhk")
        r2_min=utils.get_float_input(self,"lhbnoq64")
        r2_max=utils.get_float_input(self,"lhbnohw1")
        r3_min=utils.get_float_input(self,"lhbnoypr")
        r3_max=utils.get_float_input(self,"lhbnp1be")

        # print((desired, cal_type, r1_min, r1_max, r2_min, r2_max, r3_min, r3_max))
        self.calculator.res_compose_cal(desired, cal_type, r1_min, r1_max, r2_min, r2_max, r3_min, r3_max)
        results = self.calculator.get_results(len=20)
        table = self.widget_dic["tk_table_lhbnewl1"]
        table.delete(*table.get_children())
        for li in results:
            table.insert('','end',values=li)

        
    def handle_res_import(self,evt):
        res_text = self.widget_dic["tk_text_lhbnzn1i"].get("1.0",END).split(",")
        res_table=[float(r) for r in res_text]
        self.calculator.res_table = res_table
        # print(res_text)
        res_output_text = self.widget_dic["tk_text_lhbny85f"]
        res_output_text.delete("1.0",END)
        res_output_text.insert(END,self.calculator.get_res_table())
        
    def __event_bind(self):
        self.widget_dic["tk_button_lhbn5n3b"].bind('<Button-1>',self.handle_divider_cal)
        self.widget_dic["tk_button_lhbnf1zk"].bind('<Button-1>',self.handle_res_cal)
        self.widget_dic["tk_button_lhbnwwer"].bind('<Button-1>',self.handle_res_import)
        
if __name__ == "__main__":
    win = Win()
    # 需先建立TK对象再挂载贴图
    # 如需pyinstaller打包，此处需额外处理：
    # https://stackoverflow.com/questions/53587322/how-do-i-include-files-with-pyinstaller
    if getattr(sys, 'frozen', False):
        img = PhotoImage(file=os.path.join(sys._MEIPASS, "./topology.png"))
    else:
        img = PhotoImage(file="./topology.png")
    # img=PhotoImage(file='./topology.png')
    win.widget_dic["tk_label_lhbueduo"].configure(image=img)
    win.mainloop()
