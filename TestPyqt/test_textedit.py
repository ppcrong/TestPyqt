from PyQt5.Qt import *

"""
ref: https://blog.csdn.net/weixin_43717845/article/details/104159995
"""


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit_文本光标')
        self.resize(500, 500)
        self.init_ui()

    def init_ui(self):
        te = QTextEdit(self)
        self.te = te
        te.resize(self.width() * 7 / 8, self.height() * 7 / 8)
        te.move((self.width() - te.width()) / 2, 2)
        te.setStyleSheet('background-color:cyan;font-size:20px')
        te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.te.textChanged.connect(self.on_edit_textChanged)

        btn = QPushButton(self)
        self.btn = btn
        self.btn_w = self.width() / 3
        self.btn_h = self.height() * 3 / 32
        self.btn.resize(self.btn_w, self.btn_h)
        self.btn_x = (self.width() - self.btn_w) / 3
        self.btn_y = self.height() * 7 / 8 + (self.height() / 8 - self.btn_h) / 2
        self.btn.setText('add text')
        self.btn.setStyleSheet('font-size:30px')
        self.btn.move(self.btn_x, self.btn_y)

        btn_pos = QPushButton(self)
        self.btn_pos = btn_pos
        btn_w = self.width() / 3
        btn_h = self.height() * 3 / 32
        self.btn_pos.resize(btn_w, btn_h)
        btn_x = (self.width() - btn_w) / 3 + btn_w
        btn_y = self.height() * 7 / 8 + (self.height() / 8 - btn_h) / 2
        self.btn_pos.setText('cursor')
        self.btn_pos.setStyleSheet('font-size:30px')
        self.btn_pos.move(btn_x, btn_y)

    @pyqtSlot()
    def on_edit_textChanged(self):
        print(self.te.toPlainText())

    #########################################################################光标位置 判定与获取
    # 现在需求:
    #           判断光标的位置是否在 文档 开始 末尾
    #                            文本块 开始 末尾
    #
    # 解决方法:
    #         返回布尔值
    #                   tc.atEnd()          光标是否在文档末尾
    #                   tc.atStart()        光标是否在文档开始
    #                   tc.atBlockEnd()     光标是否在段落末尾
    #                   tc.atBlockStart()   光标是否在段落末尾
    #
    #         返回位置数值
    #                   tc.columnNumber()   光标所在的列数
    #                   tc.position()       光标所在文档整体中的位置
    #                   tc.positionInBlock()光标所在段落中的位置
    #
    #
    def text_pos(self):
        print('光标是否在文档末尾', self.tc.atEnd())
        print('光标是否在文档开始', self.tc.atStart())
        print('光标是否在段落末尾', self.tc.atBlockEnd())
        print('光标所在的列数', self.tc.columnNumber())
        print('光标所在文档整体中的位置', self.tc.position())
        print('光标所在段落中的位置', self.tc.positionInBlock())

    ############################################################################光标位置 判定与获取

    ##############################################开始编辑 结束编辑 标识
    #
    # 现在需求:
    #           撤销与重做操作 中，例如，我刚刚来连续写错三处代码，现在需要撤销三次，回到刚开始的正确代码
    #           连续使用撤销操作三次 即可解决，
    #           现在想把三次撤销操作 合为一次操作
    #           这样做的目的仅仅是 方便后续修改时，
    #                           可以快速撤销大块的操作
    #                           （一般比较肯定这一大块代码是百分百正确无误）
    # 解决方法:
    #           beginEditBlock()
    #               code1
    #               code2
    #               ……
    #           endEditBlock()
    #
    #           把多此零散的操作放在begin end之间，揉在一次，相当于创建一个宏

    def text_edit_block(self):
        self.tc = self.te.textCursor()

        self.tc.beginEditBlock()  # 用于整体操作的代码头
        self.tc.insertText('123')
        self.tc.insertBlock()
        self.tc.insertText('456')
        self.tc.insertBlock()
        self.tc.endEditBlock()  # 用于整体操作的代码尾

        self.tc.insertText('789')
        self.tc.insertBlock()

    #############################开始编辑 结束编辑 标识


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = MyWindow()

    win.btn.clicked.connect(win.text_edit_block)
    win.btn_pos.clicked.connect(win.text_pos)
    win.show()
    sys.exit(app.exec_())
