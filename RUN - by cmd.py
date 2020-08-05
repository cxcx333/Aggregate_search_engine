import tkinter as tk
import re
from urllib.parse import quote
import webbrowser


def search_panel():
    # region # 参考资料
    # Reference:https://www.cnblogs.com/pinpin/p/10052193.html
    # https://www.runoob.com/python/python-gui-tkinter.html
    # https://www.cnblogs.com/myshuzhimei/p/11764503.html
    # endregion

    # region # 定义搜索函数
    def specify_search(url):
        webbrowser.open_new_tab(url.replace('%s', quote(t1.get())))
        window.destroy()

    def default_search(event):
        input_word = t1.get()
        if re.match('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', input_word):
            webbrowser.open(t1.get())
        else:
            webbrowser.open_new_tab(r'https://www.google.com/search?q=%s'.replace('%s', quote(input_word)))
        window.destroy()

    # endregion
    # region # 导入搜索引擎
    with open(r'P:\Pycharm projects\聚合搜索引擎\engines.csv', encoding='utf8') as f:
        content = f.readlines()
    search_engines = {}
    for line in content:
        element = line.split(',')
        if element[0] not in search_engines:
            search_engines[element[0]] = {}
        if element[0] in search_engines:
            if element[1] not in search_engines[element[0]]:
                search_engines[element[0]][element[1]] = []
        if {element[2]: element[3]} not in search_engines[element[0]][element[1]]:
            search_engines[element[0]][element[1]].append({element[2]: element[3]})
    # endregion
    # print(time() - t0, 1)
    # region # 建立根窗口

    window = tk.Tk()

    root_frame = tk.Frame(window)
    root_frame.pack()
    # endregion
    # print(time() - t0, 2)
    # region # 建立并嵌入两张frame
    frame_input = tk.Frame(root_frame, bg='red')
    frame_input.pack()
    frame_button = tk.Frame(root_frame, bg='grey')
    frame_button.pack()
    # endregion
    # print(time() - t0, 3)
    # region # 设置输入框
    t1 = tk.StringVar()
    entry = tk.Entry(frame_input, textvariable=t1, width=20, font=('Consolas', 20))
    entry.pack(anchor='center')
    entry.focus_force()
    # endregion
    # print(time() - t0, 4)
    # region # 设置标签、按钮
    row = 1
    for class_0 in search_engines:
        column = 1
        tk.Label(frame_button, text=class_0, bg='pink', font=('Consolas', 14), width=5, height=1).grid(row=row,
                                                                                                       column=column,
                                                                                                       padx=10, pady=8)
        for class_1 in search_engines[class_0]:
            column = 2
            tk.Label(frame_button, text=class_1, bg='grey', font=('Consolas', 10), width=4, height=1).grid(row=row,
                                                                                                           column=column + 1,
                                                                                                           padx=3,
                                                                                                           pady=10)
            for website in search_engines[class_0][class_1]:
                for name, format_url in website.items():
                    tk.Button(frame_button, text=name, font=('Consolas', 10), width=10, height=1,
                              command=lambda format_url=format_url: specify_search(format_url)).grid(row=row,
                                                                                                     column=column + 2,
                                                                                                     padx=10, pady=10)
                column += 1
            row += 1
        row += 1
    # endregion
    # print(time() - t0, 5)
    # region # 设置窗口的显示状态
    window.title('聚合搜索')  # 窗口标题
    window.wm_attributes('-topmost', 1)  # 置顶窗口
    window.overrideredirect(1)  # 隐藏边框，不显示在任务栏，此时不可移动窗口
    window.update_idletasks()  # 更新？？不懂，但是确实有效果
    window.geometry('{}x{}+{}+{}'.format(window.winfo_width(), window.winfo_height(),
                                         int((window.winfo_screenwidth() - window.winfo_width()) / 2),
                                         int((window.winfo_screenheight() - window.winfo_height()) / 2)))  # 居中显示

    # endregion
    # print(time() - t0, 6)
    # region # 给窗口绑定事件
    window.bind('<Escape>', lambda e: window.destroy())  # 按Esc退出
    window.bind('<FocusOut>', lambda e: window.destroy())  # 丢失焦点时退出
    window.bind('<Return>', default_search)  # 按回车时使用默认搜索引擎
    window.update_idletasks()
    # endregion
    # print(time() - t0, 7)
    window.mainloop()


search_panel()
