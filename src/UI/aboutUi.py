# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 384)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbIcon = QLabel(Form)
        self.lbIcon.setObjectName(u"lbIcon")
        self.lbIcon.setMinimumSize(QSize(300, 300))
        self.lbIcon.setMaximumSize(QSize(300, 300))

        self.gridLayout.addWidget(self.lbIcon, 0, 0, 2, 1)

        self.lbTitle = QLabel(Form)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setMinimumSize(QSize(0, 30))
        self.lbTitle.setMaximumSize(QSize(16777215, 30))
        self.lbTitle.setStyleSheet(u"font-size: 24px; font-weight: bold;")

        self.gridLayout.addWidget(self.lbTitle, 0, 1, 1, 2)

        self.lbDesc = QLabel(Form)
        self.lbDesc.setObjectName(u"lbDesc")
        self.lbDesc.setStyleSheet(u"font-size: 15px")
        self.lbDesc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lbDesc, 1, 1, 1, 2)

        self.lbNotice = QLabel(Form)
        self.lbNotice.setObjectName(u"lbNotice")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbNotice.sizePolicy().hasHeightForWidth())
        self.lbNotice.setSizePolicy(sizePolicy)
        self.lbNotice.setMinimumSize(QSize(0, 30))
        self.lbNotice.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lbNotice, 2, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(493, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 2)

        self.btnClose = QPushButton(Form)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btnClose, 3, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbIcon.setText("")
        self.btnClose.setText(QCoreApplication.translate("Form", u"\ub2eb\uae30", None))
    # retranslateUi

