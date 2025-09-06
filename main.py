"""
智能绘画角色推荐系统
主程序入口
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.main_window import MainWindow
from database.database_manager import DatabaseManager


def main():
    """主函数"""
    # 创建应用程序
    app = QApplication(sys.argv)
    app.setApplicationName("智能绘画角色推荐系统")
    app.setApplicationVersion("1.0.0")
    
    # 设置应用程序图标（如果有的话）
    # app.setWindowIcon(QIcon("icon.ico"))
    
    try:
        # 初始化数据库
        db_manager = DatabaseManager()
        
        # 创建主窗口
        main_window = MainWindow()
        main_window.show()
        
        # 运行应用程序
        sys.exit(app.exec_())
        
    except Exception as e:
        # 显示错误信息
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setWindowTitle("启动错误")
        error_msg.setText("应用程序启动失败")
        error_msg.setDetailedText(str(e))
        error_msg.exec_()
        sys.exit(1)


if __name__ == "__main__":
    main()
