import time
import unittest
from observer import InteractionQueue, Task
from chimeras import *


# 导入所有奇美拉类（例如Myz, Zys, Xtt等）
# 假设所有奇美拉类已正确导入
class StateSnapshot:
    """用于捕获队列状态变化的上下文管理器"""

    def __init__(self, queue):
        self.queue = queue

    def __enter__(self):
        """记录初始状态"""
        self.initial_hp = [chi.hp for chi in self.queue.members_list]
        self.initial_atk = [chi.atk for chi in self.queue.members_list]
        self.initial_on=[chi.on for chi in self.queue.members_list]
        self.initial_complete_work_num = [chi.complete_work_num for chi in self.queue.members_list]
        self.initial_position=[chi.name for chi in self.queue.members_list]

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出时自动比较状态"""
        current_hp = [chi.hp for chi in self.queue.members_list]
        current_atk = [chi.atk for chi in self.queue.members_list]
        current_on = [chi.on for chi in self.queue.members_list]
        current_complete_work_num = [chi.complete_work_num for chi in self.queue.members_list]
        current_position = [chi.name for chi in self.queue.members_list]

        # 打印调试信息
        print("\n[状态变化对比]")
        print(f"初始HP: {self.initial_hp} -> 当前HP: {current_hp}")
        print(f"初始ATK: {self.initial_atk} -> 当前ATK: {current_atk}")
        print(f"初始on: {self.initial_on} -> 当前on: {current_on}")
        print(f"初始com_work_num: {self.initial_complete_work_num} -> 当前com_work_num: {current_complete_work_num}")
        print(f"初始position: {self.initial_position} -> 当前position: {current_position}")

class TestChimeras(unittest.TestCase):
    def setUp(self):
        self.queue = InteractionQueue()
        self.task = Task()  # 假设任务初始HP=150, ATK=5

    def test_zys(self):
        zys=Zys("治愈师")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.add_member(zys)
        ini_hp=zls.hp
        zys.episode += 1

        self.assertEqual(zls.hp, ini_hp)

    def test_xtt(self):
        xtt=Xtt("小团体")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(xtt)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)

        with StateSnapshot(self.queue):
            xtt.episode += 1
        # self.assertEqual()

    def test_hbw(self):

        hbw=Hbw("画饼王")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(hbw)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)


        with StateSnapshot(self.queue):
            hbw.on=True  # 直接修改属性触发观察者逻辑

        with StateSnapshot(self.queue):
            hbw.episode += 1  # 直接修改属性触发观察者逻辑

        with StateSnapshot(self.queue):
            hbw.episode += 1  # 直接修改属性触发观察者逻辑
        # self.assertEqual()

    def test_pfw(self):

        pfw=Pfw("平凡王")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(pfw)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        # 触发回合更新（假设回合数变化触发技能）

        with StateSnapshot(self.queue):
            pfw.on=True  # 直接修改属性触发观察者逻辑

    def test_hpq(self):
        hpq=Hpq("坏脾气")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(hpq)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)

        with StateSnapshot(self.queue):
            hpq.on=True  # 直接修改属性触发观察者逻辑
            hpq.work_num+=1

    def test_kyb(self):
        kyb=Kyb("抗压包")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(kyb)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)


        with StateSnapshot(self.queue):
            kyb.on=True  # 直接修改属性触发观察者逻辑
            kyb.hp-=1

    def test_Qjk(self):
        test_chi=Qjk("请假狂")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(test_chi)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)


        with StateSnapshot(self.queue):
            test_chi.on=True  # 直接修改属性触发观察者逻辑
            test_chi.hp-=1
            test_chi.hp-=1

    def test_Qjw(self):
        test_chi=Qjw("请假王")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(test_chi)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)


        with StateSnapshot(self.queue):
            test_chi.on=True  # 直接修改属性触发观察者逻辑
            test_chi.hp-=1
        with StateSnapshot(self.queue):
            test_chi.on = True  # 直接修改属性触发观察者逻辑
            test_chi.hp -= 1

    def test_Njw(self):
        test_chi=Njw("内卷王")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(test_chi)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)


        with StateSnapshot(self.queue):
            test_chi.on=True  # 直接修改属性触发观察者逻辑
            test_chi.hp-=8
            test_chi.complete_work_num+=1

    def test_Sqb(self):
        test_chi=Sqb("受气包")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(test_chi)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)


        with StateSnapshot(self.queue):
            test_chi.on=True  # 直接修改属性触发观察者逻辑
            test_chi.hp-=1

    def test_Xkk(self):
        test_chi=Xkk("小夸夸")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(test_chi)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        with StateSnapshot(self.queue):
            for chi in self.queue.members_list:
                if chi!=test_chi:
                    print("asdf")
                    chi.append_work_num+=1
        for chi in self.queue.members_list:
            print(chi.work_num)

    def test_plx(self):
        test_chi=Plx("跑路侠")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.add_member(test_chi)
        for chi in self.queue.members_list:
            chi.on=True
        with StateSnapshot(self.queue):
            test_chi.hp-=1

    def test_klz(self):
        test_chi=Klz("看乐子")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        with StateSnapshot(self.queue):
            for chi in self.queue.members_list:
                if chi!=test_chi:
                    chi.hp-=100

    def test_bgx(self):
        test_chi=Bgx("背锅侠")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        for chi in self.queue.members_list:
            chi.on=True
        with StateSnapshot(self.queue):
            for chi in self.queue.members_list:
                if chi!=test_chi:
                    chi.hp-=2

    def test_qgl(self):
        test_chi=Qgl("抢功劳")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.work=Task(atk=5,hp=14)
        print(self.queue.work.hp)

        #设置登场
        for chi in self.queue.members_list:
            chi.on=True
        #设置epsidoe
        for chi in self.queue.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()

        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].work_num+=1

        print(self.queue.work.hp)

    def test_jxf(self):
        test_chi=Jxf("急先锋")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.work=Task(atk=5,hp=14)

        #设置登场
        for chi in self.queue.members_list:
            chi.on=True
        #设置epsidoe
        for chi in self.queue.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()

        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].append_work_num+=1

        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].work_num+=1

        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].work_num+=1

        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].work_num+=1

    def test_Sgh(self):
        test_chi=Sgh("说怪话")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.work=Task(atk=5,hp=14)

        #设置登场
        for chi in self.queue.members_list:
            chi.on=True
        #设置epsidoe
        for chi in self.queue.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].complete_work_num+=1

    def test_Bdm(self):
        test_chi=Bdm("帮倒忙")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.work=Task(atk=5,hp=14)

        print("工作的hp",self.queue.work.hp)
        #设置登场
        for chi in self.queue.members_list:
            chi.on=True
        #设置epsidoe
        for chi in self.queue.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].work_num+=1
            self.queue.members_list[-1].work_num += 1
            self.queue.members_list[-1].work_num += 1

        print("工作的hp",self.queue.work.hp)

    def test_Gzk(self):
        test_chi=Gzk("工作狂")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(test_chi)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.work=Task(atk=5,hp=14)

        print("工作的hp",self.queue.work.hp)
        #设置登场
        for chi in self.queue.members_list:
            chi.on=True
        #设置epsidoe
        for chi in self.queue.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
        with StateSnapshot(self.queue):
            #同伴工作时
            self.queue.members_list[-1].append_work_num+=1
            self.queue.members_list[-1].work_num += 1

        print("工作的hp",self.queue.work.hp)

    def test_Leader_Zyjl(self):
        test_chi=Zyjl("职业经理")
        gzk=Gzk("工作狂")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(gzk)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.add_leader(test_chi)

        self.queue.work=Task(atk=5,hp=14)


        #设置登场
        for chi in self.queue.members_list:
            chi.on=True
        #设置epsidoe
        for chi in self.queue.members_list:
            chi.episode+=1
        #开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
        with StateSnapshot(self.queue):
            #同伴工作时
            test_chi.on=True

    def test_Leader_ykem(self):
        test_chi = Ykem("严酷恶魔")
        gzk = Gzk("工作狂")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(gzk)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.add_leader(test_chi)

        self.queue.work = Task(atk=5, hp=14)

        # 设置登场
        for chi in self.queue.members_list:
            chi.on = True
        # 设置epsidoe
        for chi in self.queue.members_list:
            chi.episode += 1
        # 开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
            # 同伴工作时
        test_chi.on = True

        with StateSnapshot(self.queue):
            for chi in self.queue.members_list:
                chi.complete_work_num+=1


    def test_Leader_Zcql(self):
        test_chi = Zcql("职场清流")
        gzk = Gzk("工作狂")
        myz = Myz("摸鱼仔")
        fnl = Fnl("负能量")
        zls = Zls("真老实")
        self.queue.add_member(gzk)
        self.queue.add_member(myz)
        self.queue.add_member(fnl)
        self.queue.add_member(zls)
        self.queue.add_leader(test_chi)

        self.queue.work = Task(atk=5, hp=14)

        # 设置登场
        for chi in self.queue.members_list:
            chi.on = True
        # 设置epsidoe
        for chi in self.queue.members_list:
            chi.episode += 1
        # 开始工作前的最后时刻固定攻击力
        for chi in self.queue.members_list:
            # 固定奇美拉攻击力
            chi.set_fix_atk()
            # 同伴工作时
        with StateSnapshot(self.queue):
            test_chi.on = True

        with StateSnapshot(self.queue):
            for chi in self.queue.members_list:
                chi.append_work_num+=1
if __name__ == '__main__':
    unittest.main()