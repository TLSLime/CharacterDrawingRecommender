#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示数据生成脚本
为新用户生成一些示例角色数据
"""

import sys
sys.path.insert(0, '.')

from database.database_manager import DatabaseManager
from datetime import datetime


def create_demo_data():
    """创建演示数据"""
    print("正在创建演示数据...")
    
    db_manager = DatabaseManager()
    
    # 示例角色数据
    demo_characters = [
        {
            'name': '初音未来',
            'base_favor': 95,
            'work_favor': 90,
            'popularity': 8500,
            'is_favorite': True,
            'birthday': '08-31',
            'work_release_date': '08-31'
        },
        {
            'name': '洛天依',
            'base_favor': 85,
            'work_favor': 80,
            'popularity': 5500,
            'is_favorite': False,
            'birthday': '07-12',
            'work_release_date': '07-12'
        },
        {
            'name': '巡音流歌',
            'base_favor': 70,
            'work_favor': 75,
            'popularity': 3200,
            'is_favorite': False,
            'birthday': '01-27',
            'work_release_date': '01-27'
        },
        {
            'name': '镜音铃',
            'base_favor': 80,
            'work_favor': 85,
            'popularity': 4500,
            'is_favorite': False,
            'birthday': '12-27',
            'work_release_date': '12-27'
        },
        {
            'name': '镜音连',
            'base_favor': 75,
            'work_favor': 80,
            'popularity': 4200,
            'is_favorite': False,
            'birthday': '12-27',
            'work_release_date': '12-27'
        },
        {
            'name': '结月缘',
            'base_favor': 65,
            'work_favor': 70,
            'popularity': 2800,
            'is_favorite': False,
            'birthday': '04-30',
            'work_release_date': '04-30'
        }
    ]
    
    character_ids = []
    
    for char_data in demo_characters:
        char_id = db_manager.add_character(**char_data)
        character_ids.append(char_id)
        print(f"✅ 添加角色: {char_data['name']} (ID: {char_id})")
    
    # 创建一些创作记录
    import random
    for i in range(8):
        char_id = random.choice(character_ids)
        work_favor = random.randint(60, 95)
        creation_id = db_manager.add_creation(char_id, work_favor=work_favor)
        char = db_manager.get_character(char_id)
        print(f"✅ 添加创作记录: {char['name']} (满意度: {work_favor})")
    
    # 创建月度目标
    today = datetime.now()
    selected_chars = random.sample(character_ids, 3)
    goal_id = db_manager.add_monthly_goal(today.month, today.year, selected_chars)
    print(f"✅ 创建月度目标 (包含 {len(selected_chars)} 个角色)")
    
    print("\n🎉 演示数据创建完成！")
    print("现在可以启动程序体验完整功能了。")


def main():
    """主函数"""
    print("智能绘画角色推荐系统 - 演示数据生成器")
    print("=" * 50)
    
    try:
        # 检查是否已有数据
        db_manager = DatabaseManager()
        existing_chars = db_manager.get_all_characters()
        
        if existing_chars:
            print(f"检测到已存在 {len(existing_chars)} 个角色")
            response = input("是否要添加更多演示数据？(y/N): ").strip().lower()
            if response not in ['y', 'yes', '是']:
                print("已取消操作")
                return
        
        create_demo_data()
        
    except Exception as e:
        print(f"❌ 创建演示数据失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
